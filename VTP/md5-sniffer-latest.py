#!/usr/bin/gdb -x
# This script is a sniffer for the IOU's internal MD5 "body" function.
#
# Based on https://github.com/crossbowerbt/GDB-Python-Utils
#
# Tested on GDB 7.7 running on Ubuntu 14.04 LTS

import gdb
import binascii
import traceback
import socket
import struct


def usage():
    print("Usage:")
    print("\tsudo ./md5-sniffer -p <pid>")
    gdb.execute('quit')


class SnifferBreakpoint(gdb.Breakpoint):

    # Initialize the breakpoint
    def __init__(self):
        # i86bi_linux_l2-ipbasek9-ms.may8-2013-team_track
        super(SnifferBreakpoint, self).__init__('*0x0a45ff8c')  # L2 image

    # Called when the breakpoint is hit
    def stop(self):
        # fff = gdb.execute('bt', to_string=True)

        # get the string
        length = int(gdb.parse_and_eval('$ecx'))
        length = socket.ntohl(length)
        print(length)

        registers = ["$edx"]
        # registers = ["$esp", "$ebp", "$esi", "$eax", "$ecx", "$edx", "$ebx", "$edi"]
        for register in registers:
            address = gdb.parse_and_eval(register)
            address = int(address)
            p = struct.pack(">i", address)
            u = struct.unpack("<I", p)
            address = u[0]
            print(address)
            try:
                data = gdb.inferiors()[0].read_memory(address, length)
                print(register, binascii.hexlify(data), length, address)
            except gdb.MemoryError:
                print("FFFFFFFFFFFFFFFFFF")
            except:
                # print("Register %s failed." % register)
                traceback.print_exc()
                return False

        # return False to continue the execution of the program
        return False


# GDB setup
gdb.execute("set print repeats unlimited")
gdb.execute("set print elements unlimited")
gdb.execute("set pagination off")

# generate sniffer breakpoint
SnifferBreakpoint()

# run and sniff...
gdb.execute('continue')

# gdb.execute('detach')
# gdb.execute('quit')
