#!/usr/bin/gdb -x
# This script is a sniffer for the IOU's internal MD5 implementation.
#
# Based on https://github.com/crossbowerbt/GDB-Python-Utils
#
# Tested on GDB 7.11 running on Fedora 24

import gdb
import binascii
import traceback
import struct


def usage():
    print("Usage:")
    print("\tsudo ./md5-sniffer-latest-v7.py -p <pid>")
    gdb.execute('quit')


class SnifferBreakpoint(gdb.Breakpoint):

    # Initialize the breakpoint
    def __init__(self):
        # Can we discover the crypto functions (and Xrefs) automagically?
        # bb1ac1ad9a039cb78319f7a4aaf855c9  i86bi-linux-l2-adventerprisek9-15.6.0.9S.bin

        # We first use FindCrypt2 plugin to find the "MD5_body" function.
        # MD5_body is called by MD5_Update function (use Xrefs to discover
        # this). Finally, we trace the arguments being passed to the MD5_Update
        # function.
        super(SnifferBreakpoint, self).__init__('*0xacd15fc')  # MD5_Update

    # Called when the breakpoint is hit
    def stop(self):
        registers = ["$edx"]
        for register in registers:
            try:
                length = int(gdb.parse_and_eval('$ecx'))  # IDA Demo 6.6 + GDB FTW!
                p = struct.pack(">i", length)
                length = struct.unpack("<I", p)[0]
                address = gdb.parse_and_eval(register)
                address = int(address)
                p = struct.pack(">i", address)
                u = struct.unpack("<I", p)
                address = u[0]
            except:
                traceback.print_exc()
                return True

            try:
                data = gdb.inferiors()[0].read_memory(address, length)
                print(register, binascii.hexlify(data), length)
                out.write("%s %s %s\n" % (register, binascii.hexlify(data), length))
                out.flush()
            except gdb.MemoryError:
                traceback.print_exc()
                return True
            except:
                traceback.print_exc()
                return True

        # return False to continue the execution of the program
        return False

out = open("log.txt", "a")

# GDB setup
gdb.execute("set print repeats unlimited")
gdb.execute("set print elements unlimited")
gdb.execute("set pagination off")
gdb.execute("handle SIGUSR1 nostop")
gdb.execute("handle SIGUSR1 noprint")

# generate sniffer breakpoint
SnifferBreakpoint()

# run and sniff
gdb.execute('continue')

# gdb.execute('detach')
# gdb.execute('quit')
