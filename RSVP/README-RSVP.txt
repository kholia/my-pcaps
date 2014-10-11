RSVP setup
==========

Router 1
--------

Router#configure terminal
Router(config)#interface Ethernet0/0
Router(config-if)#ip rsvp bandwidth 64 32
Router(config-if)#end
Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Ethernet0/0
Router(config-if)#ip address 192.168.1.10 255.255.255.0
Router(config-if)#no shutdown
Router(config-if)#end
*Oct 15 18:51:52.362: %SYS-5-CONFIG_I: Configured from console by console
*Oct 15 18:51:53.801: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Oct 15 18:51:54.805: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up
Router#config terminal
Router(config)#ip rsvp sender-host 192.168.1.20 192.168.1.10 tcp 23 0 64 3
Router(config)#ip rsvp sender-host 192.168.1.20 192.168.1.10 tcp 23 0 128 64

Router#configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Ethernet0/0
Router(config-if)#ip rsvp authentication type md5
Router(config-if)#end
Router#configure terminal
Router(config-if)#ip rsvp authentication key 11223344
Router(config-if)#end
Router#configure terminal
Router(config)#interface Ethernet0/0
Router(config-if)#ip rsvp authentication
Router(config-if)#end
Router#show ip rsvp authentication detail
From:                   192.168.1.10
To:                     192.168.1.20
Neighbor:               192.168.1.20
Interface:              Ethernet0/0
Mode:                   Send
Key ID:                 000114000405
Key Source:             Et0/0 (enabled)
Key Type:               Static per-interface
Handle:                 01000407
Hash Type:              MD5
Lifetime:               00:30:00
Expires:                00:29:24
Challenge:              Supported
Window size:            1
Last seq # sent:        15558040080776953858

Router#show ip rsvp counters
Ethernet0/0             Recv      Xmit                        Recv      Xmit
    Path                    0        20    Resv                    0         0
    PathError               0         0    ResvError               0         0
    PathTear                0         0    ResvTear                0         0
    ResvConf                0         0    RTearConf               0         0
    Ack                     0         0    Srefresh                0         0
    Hello                   0         0    IntegrityChalle         0         0
    IntegrityRespon         0         0    DSBM_WILLING            0         0
    I_AM_DSBM               0         0    Errors                  0         0
Non RSVP i/f's          Recv      Xmit                        Recv      Xmit
    Path                    0         0    Resv                    0         0
    PathError               0         0    ResvError               0         0
    PathTear                0         0    ResvTear                0         0
    ResvConf                0         0    RTearConf               0         0
    Ack                     0         0    Srefresh                0         0
    Hello                   0         0    IntegrityChalle         0         0
    IntegrityRespon         0         0    DSBM_WILLING            0         0
    I_AM_DSBM               0         0    Errors                  0         0
All Interfaces          Recv      Xmit                        Recv      Xmit
    Path                    0        20    Resv                    0         0
    PathError               0         0    ResvError               0         0
    PathTear                0         0    ResvTear                0         0


Router 2
--------

Router#config terminal
Router(config)#interface Ethernet0/0
Router(config-if)#ip address 192.168.1.20 255.255.255.0
Router(config-if)#ip rsvp bandwidth 128 64
Router(config-if)#end
Router#config terminal
Router(config)#interface Ethernet0/0
Router(config-if)#no shutdown
Router(config-if)#end
*Oct 15 18:47:50.657: %SYS-5-CONFIG_I: Configured from console by console
*Oct 15 18:47:51.920: %LINK-3-UPDOWN: Interface Ethernet0/0, changed state to up
*Oct 15 18:47:52.925: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/0, changed state to up


Links
-----

* http://networklessons.com/quality-of-service/introduction-to-rsvp/

* http://tools.ietf.org/html/rfc2747


