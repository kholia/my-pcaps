OSPF v2 on RHEL / CentOS 6.4
============================

Router 1 (R1, 192.168.56.20) is connected to two networks

- eth0 192.168.56.0/24
- eth1 172.16.1.0/24

Router 2 (R2, 192.168.56.40) is connected to two networks

- eth0 192.168.56.0/24
- eth1 172.16.2.0/24

* Install, configure and start quagga (on both R1 and R2).

  ::

    yum install quagga

    cd /etc/quagga

    cp zebra.conf.sample zebra.conf

    cp ospfd.conf.sample ospfd.conf

    service zebra start

    service ospfd satrt


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

* Setup OSPF on Router 1 (R1). Login to the ripd vty for setting up the RIP
  routing protocol.

  ::

    # telnet localhost 2604
    ...
    Password:
    ospfd> enable
    ospfd# config term
    ospfd(config)# router ospf
    ospfd(config)# passive-interface default
    ospfd(config-router)# no passive-interface eth0
    ospfd(config-router)# log-adjacency-changes detail
    ospfd(config-router)# network 192.168.56.0/24 area 0
    ospfd(config-router)# area 0 authentication message-digest
    ospfd(config-router)# exit
    ospfd(config)# int eth0
    ospfd(config-if)# ip ospf message-digest-key 1 md5 abcdefghijklmnopqrstuvwxyz
    ospfd(config-if)# write
    Configuration saved to /etc/quagga/ospfd.conf

* See the routing tables (on R1).

  ::

    # telnet localhost 2604
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

    XXX
    R1#

Credits
=======

* XXX
