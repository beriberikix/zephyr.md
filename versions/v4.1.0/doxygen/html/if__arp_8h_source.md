---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/if__arp_8h_source.html
original_path: doxygen/html/if__arp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

if\_arp.h

[Go to the documentation of this file.](if__arp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_ARP\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_ARP\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

13/\* See https://www.iana.org/assignments/arp-parameters/arp-parameters.xhtml

14 \* for the ARP hardware address type values.

15 \*/

16/\* ARP protocol HARDWARE identifiers. \*/

[ 17](if__arp_8h.md#ae1acb8a91a94d38dd411fb5e719f35b0)#define ARPHRD\_NETROM 0 /\* From KA9Q: NET/ROM pseudo. \*/

[ 18](if__arp_8h.md#a99b0f33012409144fc0b51bfa835dcba)#define ARPHRD\_ETHER 1 /\* Ethernet 10/100Mbps. \*/

[ 19](if__arp_8h.md#aa2d3040a4ca3fa7aa832b0863bb032a4)#define ARPHRD\_EETHER 2 /\* Experimental Ethernet. \*/

[ 20](if__arp_8h.md#aeaba33578b2449674b76cd29692a687c)#define ARPHRD\_AX25 3 /\* AX.25 Level 2. \*/

[ 21](if__arp_8h.md#a394dfc37c8b6c429af9d6562a76b0c99)#define ARPHRD\_PRONET 4 /\* PROnet token ring. \*/

[ 22](if__arp_8h.md#a6b5310b0311353a79e66f7700ce88e8d)#define ARPHRD\_CHAOS 5 /\* Chaosnet. \*/

[ 23](if__arp_8h.md#a63153ce22626e108b5046b89d918803f)#define ARPHRD\_IEEE802 6 /\* IEEE 802.2 Ethernet/TR/TB. \*/

[ 24](if__arp_8h.md#ade606bd55e7f4f0a03278eed4a8badf8)#define ARPHRD\_ARCNET 7 /\* ARCnet. \*/

[ 25](if__arp_8h.md#a7614228ba176316183dc2ccd61134b6a)#define ARPHRD\_APPLETLK 8 /\* APPLEtalk. \*/

[ 26](if__arp_8h.md#af02df7fa9173bc0716fe46eb5d45c3e1)#define ARPHRD\_DLCI 15 /\* Frame Relay DLCI. \*/

[ 27](if__arp_8h.md#a52fe51e586dd5952a78a42de1a2992e8)#define ARPHRD\_ATM 19 /\* ATM. \*/

[ 28](if__arp_8h.md#ad597c946041d8b4d02b41c3b2145e10a)#define ARPHRD\_METRICOM 23 /\* Metricom STRIP (new IANA id). \*/

[ 29](if__arp_8h.md#a4d072593e2ce7018e74f42eab74b1506)#define ARPHRD\_IEEE1394 24 /\* IEEE 1394 IPv4 - RFC 2734. \*/

[ 30](if__arp_8h.md#abbc7280c99b6907038c8e2a433091133)#define ARPHRD\_EUI64 27 /\* EUI-64. \*/

[ 31](if__arp_8h.md#abb8ca5a62f0f53187a295f0e96ba208b)#define ARPHRD\_INFINIBAND 32 /\* InfiniBand. \*/

32

33/\* Dummy types for non ARP hardware \*/

[ 34](if__arp_8h.md#a45d939a8b7cfeb1145cc5a49f6d2a399)#define ARPHRD\_SLIP 256

[ 35](if__arp_8h.md#a6651e9c8291dccd470c9426986a160ad)#define ARPHRD\_CSLIP 257

[ 36](if__arp_8h.md#ae35c4cbe46fc19d363a7af42c6dcf273)#define ARPHRD\_SLIP6 258

[ 37](if__arp_8h.md#ab05b137e1709daec52097cd07d9c86c7)#define ARPHRD\_CSLIP6 259

[ 38](if__arp_8h.md#af34e0978e6bb11cf230b5b691a5a1b8a)#define ARPHRD\_RSRVD 260 /\* Notional KISS type. \*/

[ 39](if__arp_8h.md#a74df13d4969bcad5e7bf0db3706dc388)#define ARPHRD\_ADAPT 264

[ 40](if__arp_8h.md#aea2aa154ca4cc488c86727dc44b36b19)#define ARPHRD\_ROSE 270

[ 41](if__arp_8h.md#a1faa7cf295013abcee809dc908d9be6b)#define ARPHRD\_X25 271 /\* CCITT X.25. \*/

[ 42](if__arp_8h.md#a0eb9519f0ea218877755913bb4533091)#define ARPHRD\_HWX25 272 /\* Boards with X.25 in firmware. \*/

[ 43](if__arp_8h.md#a07220dd6d6e255e11f0ea1cf99feba0d)#define ARPHRD\_CAN 280 /\* Controller Area Network. \*/

[ 44](if__arp_8h.md#ab490545ded34d438fe2fcc1eaaa39c1e)#define ARPHRD\_MCTP 290

[ 45](if__arp_8h.md#a18dec8be041946b4a3a75ec73bb4293c)#define ARPHRD\_PPP 512

[ 46](if__arp_8h.md#a410eced86d38da357b0ffb10adba4ca2)#define ARPHRD\_CISCO 513 /\* Cisco HDLC. \*/

[ 47](if__arp_8h.md#a8e2c80f4cd4774f76cd7803ba31b27e1)#define ARPHRD\_HDLC ARPHRD\_CISCO

[ 48](if__arp_8h.md#af09e5ae697b5b32f1e9d053b22a2642c)#define ARPHRD\_LAPB 516 /\* LAPB. \*/

[ 49](if__arp_8h.md#a3d7f861b4576376afe5a406179df42d8)#define ARPHRD\_DDCMP 517 /\* Digital's DDCMP. \*/

[ 50](if__arp_8h.md#a67c7faf6cac1fbc281e82cae47360f30)#define ARPHRD\_RAWHDLC 518 /\* Raw HDLC. \*/

[ 51](if__arp_8h.md#ab2b4f27b07b7e2d03e5873f32089dc23)#define ARPHRD\_RAWIP 519 /\* Raw IP. \*/

[ 52](if__arp_8h.md#a258c6b24592ed0bfffd287bcf72184cd)#define ARPHRD\_TUNNEL 768 /\* IPIP tunnel. \*/

[ 53](if__arp_8h.md#a28d782f6db80ae8ada7f213842ff2869)#define ARPHRD\_TUNNEL6 769 /\* IPIP6 tunnel. \*/

[ 54](if__arp_8h.md#a49796245f7c1f8f4d58e5ead7af6c66d)#define ARPHRD\_FRAD 770 /\* Frame Relay Access Device. \*/

[ 55](if__arp_8h.md#a282f35b40f5bdb27cfa179e498934c81)#define ARPHRD\_SKIP 771 /\* SKIP vif. \*/

[ 56](if__arp_8h.md#a4ee77f8d80bda9f59f5bd7163854e425)#define ARPHRD\_LOOPBACK 772 /\* Loopback device. \*/

[ 57](if__arp_8h.md#a2a6a8456b8d00c4751937f7361d77c87)#define ARPHRD\_LOCALTLK 773 /\* Localtalk device. \*/

[ 58](if__arp_8h.md#a270793cc06db405a5f814e4ad8743802)#define ARPHRD\_FDDI 774 /\* Fiber Distributed Data Interface. \*/

[ 59](if__arp_8h.md#aaa09c89bce8795a20f412e75cb441adf)#define ARPHRD\_BIF 775 /\* AP1000 BIF. \*/

[ 60](if__arp_8h.md#a40d57acc78d91f5f2bd6ebae7db18aeb)#define ARPHRD\_SIT 776 /\* sit0 device - IPv6-in-IPv4. \*/

[ 61](if__arp_8h.md#a47668de0966a3040187f2a640253278b)#define ARPHRD\_IPDDP 777 /\* IP-in-DDP tunnel. \*/

[ 62](if__arp_8h.md#abc6758e951b1761b8ae3748d66b8b830)#define ARPHRD\_IPGRE 778 /\* GRE over IP. \*/

[ 63](if__arp_8h.md#a90dfe4049e2164cc19bd3b54f2bd2e3f)#define ARPHRD\_PIMREG 779 /\* PIMSM register interface. \*/

[ 64](if__arp_8h.md#a41de3e5719f2d77703b7da4dced39096)#define ARPHRD\_HIPPI 780 /\* High Performance Parallel I'face. \*/

[ 65](if__arp_8h.md#acb4198100868cf41fbbce66aca49b616)#define ARPHRD\_ASH 781 /\* (Nexus Electronics) Ash. \*/

[ 66](if__arp_8h.md#a0b809ee9057fcd57da421e5e0aae06a7)#define ARPHRD\_ECONET 782 /\* Acorn Econet. \*/

[ 67](if__arp_8h.md#a09d2e25da54b5044c67e6ea285a26728)#define ARPHRD\_IRDA 783 /\* Linux-IrDA. \*/

[ 68](if__arp_8h.md#aaea9329315517c7ca86311f8644cd254)#define ARPHRD\_FCPP 784 /\* Point to point fibrechanel. \*/

[ 69](if__arp_8h.md#ab57dbb123cafe8fab5d73fe516cbaab4)#define ARPHRD\_FCAL 785 /\* Fibrechanel arbitrated loop. \*/

[ 70](if__arp_8h.md#ac8dc8a30027ee7ffca6fff796ad61d56)#define ARPHRD\_FCPL 786 /\* Fibrechanel public loop. \*/

[ 71](if__arp_8h.md#ac1156888d5f5f118bdb6308cdb3d019f)#define ARPHRD\_FCFABRIC 787 /\* Fibrechanel fabric. \*/

[ 72](if__arp_8h.md#a00bc6b1bb5f426bb58241ba16ad870e7)#define ARPHRD\_IEEE802\_TR 800 /\* Magic type ident for TR. \*/

[ 73](if__arp_8h.md#acc8226bf5c1c690acdeb7d827e061107)#define ARPHRD\_IEEE80211 801 /\* IEEE 802.11. \*/

[ 74](if__arp_8h.md#a9b01c3c5cd6cce41e141cb185ffc2f65)#define ARPHRD\_IEEE80211\_PRISM 802 /\* IEEE 802.11 + Prism2 header. \*/

[ 75](if__arp_8h.md#a7b897c5160766a1c3f1ea51635419b48)#define ARPHRD\_IEEE80211\_RADIOTAP 803 /\* IEEE 802.11 + radiotap header. \*/

[ 76](if__arp_8h.md#adff33b6bd20a8b03fedce3b7fec456e9)#define ARPHRD\_IEEE802154 804 /\* IEEE 802.15.4 header. \*/

[ 77](if__arp_8h.md#a2794d558aa2c279f8ac4e3f4e11f72cd)#define ARPHRD\_IEEE802154\_PHY 805 /\* IEEE 802.15.4 PHY header. \*/

78

[ 79](if__arp_8h.md#a9bc958dad255bdc3fc3fbe067adaf017)#define ARPHRD\_VOID 0xFFFF /\* Void type, nothing is known. \*/

[ 80](if__arp_8h.md#af54d98448c0e1e1b02d9e565508a4280)#define ARPHRD\_NONE 0xFFFE /\* Zero header length. \*/

81

82#ifdef \_\_cplusplus

83}

84#endif

85

86#endif /\* ZEPHYR\_INCLUDE\_POSIX\_NET\_IF\_ARP\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [net](dir_2c168081a5287170970afe4d92a99d1b.md)
- [if\_arp.h](if__arp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
