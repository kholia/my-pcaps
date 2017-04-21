#### SNMP

snmp_usm.pcap contains a series of authenticated and some encrypted SNMPv3 PDUS

The authPassword for all users is pippoxxx and the privPassword is PIPPOxxx.

- pippo uses MD5 and DES
- pippo2 uses SHA1 and DES
- pippo3 uses SHA1 and AES
- pippo4 uses MD5 and AES

Use JtR to crack SNMPv3 USM hashes!

#### SNMP setup

```
$ sudo cat /etc/snmp/snmpd.conf
...
createUser lulu MD5 "1234567£" DES "1234567£"
authuser read -s usm lulu priv .1
agentAddress udp:161,udp6:161
rocommunity6 public default

$ snmpget -v 3 -u lulu -l Priv -a MD5 -A 1234567£ -x DES -X 1234567£ ::1 sysName.0
SNMPv2-MIB::sysName.0 = STRING: localhost.localdomain
```

#### Credits

* http://wiki.wireshark.org/SampleCaptures#SNMP
