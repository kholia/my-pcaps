Triggering "Expert Info" manually
---------------------------------

$ tshark -x -r HSRPv1-single-packet.pcap > HSRPv1-single-packet.txt

$ # edit TLV sequence in HSRPv1-single-packet.txt

$ text2pcap HSRPv1-single-packet.txt HSRPv1-single-packet-fuzzed.pcap


$ ./tshark -nVxr HSRPv1-single-packet-fuzzed.pcap
...
User Datagram Protocol, Src Port: 1985, Dst Port: 1985
    Source Port: 1985
    Destination Port: 1985
    Length: 58
    Checksum: 0xc8a5 [validation disabled]
        [Good Checksum: False]
        [Bad Checksum: False]
    [Stream index: 0]
Cisco Hot Standby Router Protocol
    Version: 0
    Op Code: Hello (0)
    State: Active (16)
    Hellotime: Default (3)
    Holdtime: Default (10)
    Priority: 110
    Group: 1
    Reserved: 0
    Authentication Data: Non-Default ()
    Virtual IP Address: 10.0.0.100
    [Expert Info (Warn/Undecoded): Unknown TLV sequence in HSRPv1 dissection, Type=(5) Len=(28)]
        [Unknown TLV sequence in HSRPv1 dissection, Type=(5) Len=(28)]
        [Severity level: Warn]
        [Group: Undecoded]

$ ASAN_OPTIOCNS=detect_leaks=0 ./tshark -2 -r HSRPv1-single-packet-fuzzed.pcap -zexpert,chat
  1   0.000000    10.0.0.10 -> 224.0.0.2    HSRP 92 Hello (state Active)

Warns (1)
=============
   Frequency      Group           Protocol  Summary
           1  Undecoded               HSRP  Unknown TLV sequence in HSRPv1 dissection, Type=(5) Len=(28)
