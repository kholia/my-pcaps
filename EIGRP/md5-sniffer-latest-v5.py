#!/usr/bin/gdb -x
# This script is a sniffer for the IOU's internal MD5 implementation.
#
# Based on https://github.com/crossbowerbt/GDB-Python-Utils
#
# Tested on GDB 7.7 running on Ubuntu 14.04 LTS

import gdb
import binascii
import traceback
import struct


def usage():
    print("Usage:")
    print("\tsudo ./md5-sniffer-latest-v4.py -p <pid>")
    gdb.execute('quit')


class SnifferBreakpoint(gdb.Breakpoint):

    # Initialize the breakpoint
    def __init__(self):
        # Can we discover the crypto functions (and Xrefs) automagically?
        # 50d1c5aaf1976e4622daf9eaa2632212  i86bi_linux-adventerprisek9-ms.154-2.T.bin
        # super(SnifferBreakpoint, self).__init__('*0x0d796e4c')  # not called, md5_4
        # super(SnifferBreakpoint, self).__init__('*0x0d6642ec')  # not called, md5_3
        # super(SnifferBreakpoint, self).__init__('*0x0d4329e0')  # called, md5_2
        super(SnifferBreakpoint, self).__init__('*0x0d4328cc')  # MD5_Update, calls md5_2
        # super(SnifferBreakpoint, self).__init__('*0x0a58b1c0')  # not called, md5_1
        self.trailing_calls = 0

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
                # reduce noise by checking for password ("passsword12345"), not strictly required :-)
                # if "70617373776f72643132333435" in str(binascii.hexlify(data)):
                # self.trailing_calls = 1
                print(register, binascii.hexlify(data), length)
                # elif self.trailing_calls > 0:
                #    print(register, binascii.hexlify(data), length)
                #    self.trailing_calls = self.trailing_calls - 1
            except gdb.MemoryError:
                traceback.print_exc()
                return True
            except:
                traceback.print_exc()
                return True

        # return False to continue the execution of the program
        return False


# GDB setup
gdb.execute("set print repeats unlimited")
gdb.execute("set print elements unlimited")
gdb.execute("set pagination off")

# generate sniffer breakpoint
SnifferBreakpoint()

# run and sniff
gdb.execute('continue')

# gdb.execute('detach')
# gdb.execute('quit')
