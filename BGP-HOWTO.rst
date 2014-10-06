BGP on RHEL / CentOS 6.4
========================

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

    cp bgpd.conf.sample bgpd.conf

    service zebra start

    service bgpdd satrt


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

* Setup BGP on Router 1 (R1).

  ::

    # telnet localhost 2605  # netstat -nltp
    ...
    Password:
    bgpd> enable
    bgpd# config term
    bgpd(config)# router bgp 7675
    bgpd(config-router)# bgp log-neighbor-changes
    bgpd(config-router)# bgp always-compare-med
    bgpd(config-router)# bgp graceful-restart
    bgpd(config-router)# network 192.168.56.0/24
    bgpd(config-router)# network 172.16.1.0/24
    bgpd(config-router)# neighbor 192.168.56.40 remote-as 7676
    bgpd(config-router)# neighbor 192.168.56.40 password lolcats
    bgpd(config-router)# exit
    bgpd(config)# write
    Configuration saved to /etc/quagga/bgpd.conf

* Configure BGP on R2 in a similar fashion.

Credits
=======

* johnx@elwico.pl

