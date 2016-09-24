# http://www.frida.re/docs/functions/

from __future__ import print_function
import frida
import sys

session = frida.attach(int(sys.argv[1]))  # PID of the IOU process
print(session.enumerate_modules())

script = session.create_script("""
Interceptor.attach(ptr("%s"), {
    onEnter: function(args) {
        var length = this.context.ecx;
        length = ((length & 0xFF) << 24) | ((length & 0xFF00) << 8) | ((length >> 8) & 0xFF00) | ((length >> 24) & 0xFF);
        address = this.context.edx.toString();
        send({ length: length, address: address});
    }
});
""" % int(sys.argv[2], 16))  # address of the function to hook
def on_message(message, data):
    print(message)

script.on('message', on_message)
script.load()
sys.stdin.read()
