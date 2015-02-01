Connecting IOU to the real world
================================

Using "i86bi_linux-adventerprisek9-ms.154-2.T.bin" with iou2net.

$ cat start-1.sh
#!/bin/bash

LD_LIBRARY_PATH=. ./IOS.bin 10



...

$ ./start-1.sh
...
*Feb  1 22:07:42.271: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/1, changed state to down
*Feb  1 22:07:42.276: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/2, changed state to down
*Feb  1 22:07:42.276: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet1/3, changed state to down
*Feb  1 22:07:44.999: AUTOINSTALL: Ethernet0/0 is assigned 192.168.0.14
...
Router#ping 8.8.8.8
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 8/11/12 ms
Router#

...

$ sudo perl iou2net.pl -v -i eth0 -n NETMAP -p 150
ou2net.pl, Version v0.5, 20-Sep-2011.
UID: 1000
Socket base directory: /tmp/netio1000
Found valid mapping line in NETMAP: 10:0/0@roameo 150:0/0@roameo
Using pseudoinstance 150, interface 0/0
Created pseudo IOU socket at /tmp/netio1000/150
Attached to real IOU socket at /tmp/netio1000/10
Precomputed IOU Header: 000a009600000100
Working in pcap mode.
Using MAC 0E:00:03:E8:0A:00.
Capture filter set: (ether[0] & 1 = 1) or (ether dst '0E:00:03:E8:0A:00') or
                    (ether[0] = 0x02 and ether[1:2] = 0x03e8) or
                    (ether[0] = 0xaa and ether[1:2] = 0xbbcc)
Forwarding frames between interface eth0 and IOU instance 10, int 0/0 (MAC: 0E:00:03:E8:0A:00)


...


$ cat NETMAP
/* Used by iou2net.pl to bridge 10's e0/0 to physical network */
10:0/0@roameo 150:0/0@roameo

Connecting multiple IOU instances to the real world
===================================================

iou2net says that "for bridging multiple router interfaces, separate instances
of this script must be launched, and you need an unique pseudo IOU ID per
instance".

$ cat NETMAP
10:0/0@phoenix 100:0/0@phoenix
20:0/0@phoenix 200:0/0@phoenix

$ sudo perl iou2net.pl -d -v -i eth0 -n NETMAP -p 100

...

$ sudo perl iou2net.pl -d -v -i eth0 -n NETMAP -p 200

...

Tested on 64-bit Ubuntu 14.10 (in February 2015).


Resources
---------

* https://github.com/jlgaddis/iou2net
