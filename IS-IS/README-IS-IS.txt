RSVP setup
==========

Router 1
--------

❯ ./start-1.sh
***************************************************************
IOS On Unix - Cisco Systems confidential, internal use only
Under no circumstances is this software to be provided to any
non Cisco staff or customers.  To do so is likely to result
in disciplinary action. Please refer to the IOU Usage policy at
wwwin-iou.cisco.com for more information.
***************************************************************
Port 0/0 is connected to:
        20:0/0

              Restricted Rights Legend

...

         --- System Configuration Dialog ---

Would you like to enter the initial configuration dialog? [yes/no]: no

Would you like to terminate autoinstall? [yes]:


Router>enable
Router#configure t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface loopback0
Router(config-if)#ip address 192.168.1.5 255.255.255.255
Router(config-if)#end
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Ethernet0/0
Router(config-if)#ip address 192.168.120.5 255.255.255.0
Router(config-if)#no shutdown
Router(config-if)#ip router isis
Router(config-if)#end
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#router isis
Router(config-router)#is-type level-1
Router(config-router)#passive-interface loo
Router(config-router)#passive-interface loopback0
Router(config-router)#net 49.0001.1921.6800.1005.00
Router(config-router)#end
Router#
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Ethernet0/0
Router(config-if)#end
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#key chain test
Router(config-keychain)#key 1
Router(config-keychain-key)#key-string password12345
Router(config-keychain-key)#end
Router#
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#interface Ethernet0/0
Router(config-if)#ip router isis
Router(config-if)#isis authentication mode md5
Router(config-if)#isi authentication key-chain test
Router(config-if)#end
Router#
*Oct 17 18:34:44.255: %SYS-5-CONFIG_I: Configured from console by console
Router#
*Oct 17 18:34:46.708: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
*Oct 17 18:35:22.069: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
*Oct 17 18:35:56.758: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
*Oct 17 18:36:31.309: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
*Oct 17 18:37:04.012: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
*Oct 17 18:37:37.976: %CLNS-4-AUTH_FAIL: ISIS: LAN IIH authentication failed
Router#
