RIPv2 on RHEL / CentOS 6.4
==========================

* Router 1 (R1, 192.168.56.20) is connected to two networks

  - eth0 192.168.56.0/24
  - eth1 172.16.1.0/24

* Router 2 (R2, 192.168.56.40) is connected to two networks

  - eth0 192.168.56.0/24
  - eth1 172.16.2.0/24

* Install, configure and start quagga (on both R1 and R2).
  
  ::
  
    yum install quagga

    cd /etc/quagga

    cp zebra.conf.sample zebra.conf

    cp ripd.conf.sample ripd.conf

    service zebra start

    service ripd satrt


* Setting up package forwarding (on both R1 and R2).
  
  ::
  
    # sysctl -w net.inet.ip.forwarding=1

* Configure firewall on R1 and R2.

  ::

    # iptables -F  # ;(

* Configure Router 1 (R1). Login to the Zebra vty for setting up the
  interfaces.

  ::

    # telnet localhost 2601
    ...
    Password:
    Router> enable
    Password:
    Router# config term
    Router(config)# interface eth0
    Router(config-if)# ip address 192.168.56.20/24
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# interface eth1
    Router(config-if)# ip address 172.16.1.1/24
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# hostname R1
    R1(config)# write
    Configuration saved to /etc/quagga/zebra.conf

* Configure Router 2 (R2).

  ::

    # telnet localhost 2601
    ...
    Password:
    Router> enable
    Password:
    Router# config term
    Router(config)# interface eth0
    Router(config-if)# ip address 192.168.56.40/24
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# interface eth1
    Router(config-if)# ip address 172.16.2.1/24
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# hostname R2
    R2(config)# write
    Configuration saved to /etc/quagga/zebra.conf

* Setup RIP on Router 1 (R1). Login to the ripd vty for setting up the RIP
  routing protocol.


  ::

    # telnet localhost 2602
    ...
    Password:
    ripd> enable
    ripd# config term
    ripd(config)# router rip
    ripd(config-router)# version 2
    ripd(config-router)# network 192.168.56.0/24
    ripd(config-router)# network 172.16.1.0/24
    ripd(config-router)# passive-interface eth1
    ripd(config-router)# exit
    ripd(config)# key chain kc
    ripd(config-keychain)# key 1
    ripd(config-keychain-key)# key-string quagga
    ripd(config-keychain-key)# exit
    ripd(config-keychain)# exit
    ripd(config)# interface eth0 
    ripd(config-if)# ip rip authentication key-chain kc
    ripd(config-if)# ip rip authentication mode md5
    ripd(config-if)# exit
    ripd(config)# write
    Configuration saved to /etc/quagga/ripd.conf

* Setup RIP on Router 2 (R2). 

  ::

    # telnet localhost 2602
    ...
    Password:
    ripd> enable
    ripd# config term
    ripd(config)# router rip
    ripd(config-router)# version 2
    ripd(config-router)# network 192.168.56.0/24
    ripd(config-router)# network 172.16.2.0/24
    ripd(config-router)# passive-interface eth1
    ripd(config-router)# exit
    ripd(config)# key chain kc
    ripd(config-keychain)# key 1
    ripd(config-keychain-key)# key-string quagga
    ripd(config-keychain-key)# exit
    ripd(config-keychain)# exit
    ripd(config)# interface eth0 
    ripd(config-if)# ip rip authentication key-chain kc
    ripd(config-if)# ip rip authentication mode md5
    ripd(config-if)# exit
    ripd(config)# write
    Configuration saved to /etc/quagga/ripd.conf

* See the routing tables (on R1).

  ::

    # telnet localhost 2601
    ...
    Password:
    R1> enable
    Password:
    R1# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
    O - OSPF, I - IS-IS, B - BGP, A - Babel,
    > - selected route, * - FIB route

    Codes: K - kernel route, C - connected, S - static, R - RIP, O - OSPF,
       I - ISIS, B - BGP, > - selected route, * - FIB route

    K>* 0.0.0.0/0 via 192.168.56.1, eth0
    C>* 127.0.0.0/8 is directly connected, lo
    C>* 172.16.1.0/24 is directly connected, eth1
    R>* 172.16.2.0/24 [120/2] via 192.168.56.40, eth0, 00:00:09
    C>* 192.168.56.0/24 is directly connected, eth0
    R1# 

Credits
=======

* Ivan Mora Pérez
