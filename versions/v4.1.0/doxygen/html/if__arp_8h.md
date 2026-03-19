---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/if__arp_8h.html
original_path: doxygen/html/if__arp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

if\_arp.h File Reference

[Go to the source code of this file.](if__arp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ARPHRD\_NETROM](#ae1acb8a91a94d38dd411fb5e719f35b0)   0 /\* From KA9Q: NET/ROM pseudo. \*/ |
| #define | [ARPHRD\_ETHER](#a99b0f33012409144fc0b51bfa835dcba)   1 /\* Ethernet 10/100Mbps. \*/ |
| #define | [ARPHRD\_EETHER](#aa2d3040a4ca3fa7aa832b0863bb032a4)   2 /\* Experimental Ethernet. \*/ |
| #define | [ARPHRD\_AX25](#aeaba33578b2449674b76cd29692a687c)   3 /\* AX.25 Level 2. \*/ |
| #define | [ARPHRD\_PRONET](#a394dfc37c8b6c429af9d6562a76b0c99)   4 /\* PROnet token ring. \*/ |
| #define | [ARPHRD\_CHAOS](#a6b5310b0311353a79e66f7700ce88e8d)   5 /\* Chaosnet. \*/ |
| #define | [ARPHRD\_IEEE802](#a63153ce22626e108b5046b89d918803f)   6 /\* IEEE 802.2 Ethernet/TR/TB. \*/ |
| #define | [ARPHRD\_ARCNET](#ade606bd55e7f4f0a03278eed4a8badf8)   7 /\* ARCnet. \*/ |
| #define | [ARPHRD\_APPLETLK](#a7614228ba176316183dc2ccd61134b6a)   8 /\* APPLEtalk. \*/ |
| #define | [ARPHRD\_DLCI](#af02df7fa9173bc0716fe46eb5d45c3e1)   15 /\* Frame Relay DLCI. \*/ |
| #define | [ARPHRD\_ATM](#a52fe51e586dd5952a78a42de1a2992e8)   19 /\* ATM. \*/ |
| #define | [ARPHRD\_METRICOM](#ad597c946041d8b4d02b41c3b2145e10a)   23 /\* Metricom STRIP (new IANA id). \*/ |
| #define | [ARPHRD\_IEEE1394](#a4d072593e2ce7018e74f42eab74b1506)   24 /\* IEEE 1394 IPv4 - RFC 2734. \*/ |
| #define | [ARPHRD\_EUI64](#abbc7280c99b6907038c8e2a433091133)   27 /\* EUI-64. \*/ |
| #define | [ARPHRD\_INFINIBAND](#abb8ca5a62f0f53187a295f0e96ba208b)   32 /\* InfiniBand. \*/ |
| #define | [ARPHRD\_SLIP](#a45d939a8b7cfeb1145cc5a49f6d2a399)   256 |
| #define | [ARPHRD\_CSLIP](#a6651e9c8291dccd470c9426986a160ad)   257 |
| #define | [ARPHRD\_SLIP6](#ae35c4cbe46fc19d363a7af42c6dcf273)   258 |
| #define | [ARPHRD\_CSLIP6](#ab05b137e1709daec52097cd07d9c86c7)   259 |
| #define | [ARPHRD\_RSRVD](#af34e0978e6bb11cf230b5b691a5a1b8a)   260 /\* Notional KISS type. \*/ |
| #define | [ARPHRD\_ADAPT](#a74df13d4969bcad5e7bf0db3706dc388)   264 |
| #define | [ARPHRD\_ROSE](#aea2aa154ca4cc488c86727dc44b36b19)   270 |
| #define | [ARPHRD\_X25](#a1faa7cf295013abcee809dc908d9be6b)   271 /\* CCITT X.25. \*/ |
| #define | [ARPHRD\_HWX25](#a0eb9519f0ea218877755913bb4533091)   272 /\* Boards with X.25 in firmware. \*/ |
| #define | [ARPHRD\_CAN](#a07220dd6d6e255e11f0ea1cf99feba0d)   280 /\* Controller Area Network. \*/ |
| #define | [ARPHRD\_MCTP](#ab490545ded34d438fe2fcc1eaaa39c1e)   290 |
| #define | [ARPHRD\_PPP](#a18dec8be041946b4a3a75ec73bb4293c)   512 |
| #define | [ARPHRD\_CISCO](#a410eced86d38da357b0ffb10adba4ca2)   513 /\* Cisco HDLC. \*/ |
| #define | [ARPHRD\_HDLC](#a8e2c80f4cd4774f76cd7803ba31b27e1)   [ARPHRD\_CISCO](#a410eced86d38da357b0ffb10adba4ca2) |
| #define | [ARPHRD\_LAPB](#af09e5ae697b5b32f1e9d053b22a2642c)   516 /\* LAPB. \*/ |
| #define | [ARPHRD\_DDCMP](#a3d7f861b4576376afe5a406179df42d8)   517 /\* Digital'[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) DDCMP. \*/ |
| #define | [ARPHRD\_RAWHDLC](#a67c7faf6cac1fbc281e82cae47360f30)   518 /\* Raw HDLC. \*/ |
| #define | [ARPHRD\_RAWIP](#ab2b4f27b07b7e2d03e5873f32089dc23)   519 /\* Raw IP. \*/ |
| #define | [ARPHRD\_TUNNEL](#a258c6b24592ed0bfffd287bcf72184cd)   768 /\* IPIP tunnel. \*/ |
| #define | [ARPHRD\_TUNNEL6](#a28d782f6db80ae8ada7f213842ff2869)   769 /\* IPIP6 tunnel. \*/ |
| #define | [ARPHRD\_FRAD](#a49796245f7c1f8f4d58e5ead7af6c66d)   770 /\* Frame Relay Access Device. \*/ |
| #define | [ARPHRD\_SKIP](#a282f35b40f5bdb27cfa179e498934c81)   771 /\* SKIP vif. \*/ |
| #define | [ARPHRD\_LOOPBACK](#a4ee77f8d80bda9f59f5bd7163854e425)   772 /\* Loopback device. \*/ |
| #define | [ARPHRD\_LOCALTLK](#a2a6a8456b8d00c4751937f7361d77c87)   773 /\* Localtalk device. \*/ |
| #define | [ARPHRD\_FDDI](#a270793cc06db405a5f814e4ad8743802)   774 /\* Fiber Distributed Data Interface. \*/ |
| #define | [ARPHRD\_BIF](#aaa09c89bce8795a20f412e75cb441adf)   775 /\* AP1000 BIF. \*/ |
| #define | [ARPHRD\_SIT](#a40d57acc78d91f5f2bd6ebae7db18aeb)   776 /\* sit0 [device](structdevice.md) - IPv6-in-IPv4. \*/ |
| #define | [ARPHRD\_IPDDP](#a47668de0966a3040187f2a640253278b)   777 /\* IP-in-DDP tunnel. \*/ |
| #define | [ARPHRD\_IPGRE](#abc6758e951b1761b8ae3748d66b8b830)   778 /\* GRE over IP. \*/ |
| #define | [ARPHRD\_PIMREG](#a90dfe4049e2164cc19bd3b54f2bd2e3f)   779 /\* PIMSM register interface. \*/ |
| #define | [ARPHRD\_HIPPI](#a41de3e5719f2d77703b7da4dced39096)   780 /\* High Performance Parallel I'face. \*/ |
| #define | [ARPHRD\_ASH](#acb4198100868cf41fbbce66aca49b616)   781 /\* (Nexus Electronics) Ash. \*/ |
| #define | [ARPHRD\_ECONET](#a0b809ee9057fcd57da421e5e0aae06a7)   782 /\* Acorn Econet. \*/ |
| #define | [ARPHRD\_IRDA](#a09d2e25da54b5044c67e6ea285a26728)   783 /\* Linux-IrDA. \*/ |
| #define | [ARPHRD\_FCPP](#aaea9329315517c7ca86311f8644cd254)   784 /\* Point to point fibrechanel. \*/ |
| #define | [ARPHRD\_FCAL](#ab57dbb123cafe8fab5d73fe516cbaab4)   785 /\* Fibrechanel arbitrated loop. \*/ |
| #define | [ARPHRD\_FCPL](#ac8dc8a30027ee7ffca6fff796ad61d56)   786 /\* Fibrechanel public loop. \*/ |
| #define | [ARPHRD\_FCFABRIC](#ac1156888d5f5f118bdb6308cdb3d019f)   787 /\* Fibrechanel fabric. \*/ |
| #define | [ARPHRD\_IEEE802\_TR](#a00bc6b1bb5f426bb58241ba16ad870e7)   800 /\* Magic type ident for TR. \*/ |
| #define | [ARPHRD\_IEEE80211](#acc8226bf5c1c690acdeb7d827e061107)   801 /\* IEEE 802.11. \*/ |
| #define | [ARPHRD\_IEEE80211\_PRISM](#a9b01c3c5cd6cce41e141cb185ffc2f65)   802 /\* IEEE 802.11 + Prism2 header. \*/ |
| #define | [ARPHRD\_IEEE80211\_RADIOTAP](#a7b897c5160766a1c3f1ea51635419b48)   803 /\* IEEE 802.11 + radiotap header. \*/ |
| #define | [ARPHRD\_IEEE802154](#adff33b6bd20a8b03fedce3b7fec456e9)   804 /\* IEEE 802.15.4 header. \*/ |
| #define | [ARPHRD\_IEEE802154\_PHY](#a2794d558aa2c279f8ac4e3f4e11f72cd)   805 /\* IEEE 802.15.4 PHY header. \*/ |
| #define | [ARPHRD\_VOID](#a9bc958dad255bdc3fc3fbe067adaf017)   0xFFFF /\* Void type, nothing is known. \*/ |
| #define | [ARPHRD\_NONE](#af54d98448c0e1e1b02d9e565508a4280)   0xFFFE /\* Zero header length. \*/ |

## Macro Definition Documentation

## [◆ ](#a74df13d4969bcad5e7bf0db3706dc388)ARPHRD\_ADAPT

| #define ARPHRD\_ADAPT   264 |
| --- |

## [◆ ](#a7614228ba176316183dc2ccd61134b6a)ARPHRD\_APPLETLK

| #define ARPHRD\_APPLETLK   8 /\* APPLEtalk. \*/ |
| --- |

## [◆ ](#ade606bd55e7f4f0a03278eed4a8badf8)ARPHRD\_ARCNET

| #define ARPHRD\_ARCNET   7 /\* ARCnet. \*/ |
| --- |

## [◆ ](#acb4198100868cf41fbbce66aca49b616)ARPHRD\_ASH

| #define ARPHRD\_ASH   781 /\* (Nexus Electronics) Ash. \*/ |
| --- |

## [◆ ](#a52fe51e586dd5952a78a42de1a2992e8)ARPHRD\_ATM

| #define ARPHRD\_ATM   19 /\* ATM. \*/ |
| --- |

## [◆ ](#aeaba33578b2449674b76cd29692a687c)ARPHRD\_AX25

| #define ARPHRD\_AX25   3 /\* AX.25 Level 2. \*/ |
| --- |

## [◆ ](#aaa09c89bce8795a20f412e75cb441adf)ARPHRD\_BIF

| #define ARPHRD\_BIF   775 /\* AP1000 BIF. \*/ |
| --- |

## [◆ ](#a07220dd6d6e255e11f0ea1cf99feba0d)ARPHRD\_CAN

| #define ARPHRD\_CAN   280 /\* Controller Area Network. \*/ |
| --- |

## [◆ ](#a6b5310b0311353a79e66f7700ce88e8d)ARPHRD\_CHAOS

| #define ARPHRD\_CHAOS   5 /\* Chaosnet. \*/ |
| --- |

## [◆ ](#a410eced86d38da357b0ffb10adba4ca2)ARPHRD\_CISCO

| #define ARPHRD\_CISCO   513 /\* Cisco HDLC. \*/ |
| --- |

## [◆ ](#a6651e9c8291dccd470c9426986a160ad)ARPHRD\_CSLIP

| #define ARPHRD\_CSLIP   257 |
| --- |

## [◆ ](#ab05b137e1709daec52097cd07d9c86c7)ARPHRD\_CSLIP6

| #define ARPHRD\_CSLIP6   259 |
| --- |

## [◆ ](#a3d7f861b4576376afe5a406179df42d8)ARPHRD\_DDCMP

| #define ARPHRD\_DDCMP   517 /\* Digital'[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) DDCMP. \*/ |
| --- |

## [◆ ](#af02df7fa9173bc0716fe46eb5d45c3e1)ARPHRD\_DLCI

| #define ARPHRD\_DLCI   15 /\* Frame Relay DLCI. \*/ |
| --- |

## [◆ ](#a0b809ee9057fcd57da421e5e0aae06a7)ARPHRD\_ECONET

| #define ARPHRD\_ECONET   782 /\* Acorn Econet. \*/ |
| --- |

## [◆ ](#aa2d3040a4ca3fa7aa832b0863bb032a4)ARPHRD\_EETHER

| #define ARPHRD\_EETHER   2 /\* Experimental Ethernet. \*/ |
| --- |

## [◆ ](#a99b0f33012409144fc0b51bfa835dcba)ARPHRD\_ETHER

| #define ARPHRD\_ETHER   1 /\* Ethernet 10/100Mbps. \*/ |
| --- |

## [◆ ](#abbc7280c99b6907038c8e2a433091133)ARPHRD\_EUI64

| #define ARPHRD\_EUI64   27 /\* EUI-64. \*/ |
| --- |

## [◆ ](#ab57dbb123cafe8fab5d73fe516cbaab4)ARPHRD\_FCAL

| #define ARPHRD\_FCAL   785 /\* Fibrechanel arbitrated loop. \*/ |
| --- |

## [◆ ](#ac1156888d5f5f118bdb6308cdb3d019f)ARPHRD\_FCFABRIC

| #define ARPHRD\_FCFABRIC   787 /\* Fibrechanel fabric. \*/ |
| --- |

## [◆ ](#ac8dc8a30027ee7ffca6fff796ad61d56)ARPHRD\_FCPL

| #define ARPHRD\_FCPL   786 /\* Fibrechanel public loop. \*/ |
| --- |

## [◆ ](#aaea9329315517c7ca86311f8644cd254)ARPHRD\_FCPP

| #define ARPHRD\_FCPP   784 /\* Point to point fibrechanel. \*/ |
| --- |

## [◆ ](#a270793cc06db405a5f814e4ad8743802)ARPHRD\_FDDI

| #define ARPHRD\_FDDI   774 /\* Fiber Distributed Data Interface. \*/ |
| --- |

## [◆ ](#a49796245f7c1f8f4d58e5ead7af6c66d)ARPHRD\_FRAD

| #define ARPHRD\_FRAD   770 /\* Frame Relay Access Device. \*/ |
| --- |

## [◆ ](#a8e2c80f4cd4774f76cd7803ba31b27e1)ARPHRD\_HDLC

| #define ARPHRD\_HDLC   [ARPHRD\_CISCO](#a410eced86d38da357b0ffb10adba4ca2) |
| --- |

## [◆ ](#a41de3e5719f2d77703b7da4dced39096)ARPHRD\_HIPPI

| #define ARPHRD\_HIPPI   780 /\* High Performance Parallel I'face. \*/ |
| --- |

## [◆ ](#a0eb9519f0ea218877755913bb4533091)ARPHRD\_HWX25

| #define ARPHRD\_HWX25   272 /\* Boards with X.25 in firmware. \*/ |
| --- |

## [◆ ](#a4d072593e2ce7018e74f42eab74b1506)ARPHRD\_IEEE1394

| #define ARPHRD\_IEEE1394   24 /\* IEEE 1394 IPv4 - RFC 2734. \*/ |
| --- |

## [◆ ](#a63153ce22626e108b5046b89d918803f)ARPHRD\_IEEE802

| #define ARPHRD\_IEEE802   6 /\* IEEE 802.2 Ethernet/TR/TB. \*/ |
| --- |

## [◆ ](#acc8226bf5c1c690acdeb7d827e061107)ARPHRD\_IEEE80211

| #define ARPHRD\_IEEE80211   801 /\* IEEE 802.11. \*/ |
| --- |

## [◆ ](#a9b01c3c5cd6cce41e141cb185ffc2f65)ARPHRD\_IEEE80211\_PRISM

| #define ARPHRD\_IEEE80211\_PRISM   802 /\* IEEE 802.11 + Prism2 header. \*/ |
| --- |

## [◆ ](#a7b897c5160766a1c3f1ea51635419b48)ARPHRD\_IEEE80211\_RADIOTAP

| #define ARPHRD\_IEEE80211\_RADIOTAP   803 /\* IEEE 802.11 + radiotap header. \*/ |
| --- |

## [◆ ](#adff33b6bd20a8b03fedce3b7fec456e9)ARPHRD\_IEEE802154

| #define ARPHRD\_IEEE802154   804 /\* IEEE 802.15.4 header. \*/ |
| --- |

## [◆ ](#a2794d558aa2c279f8ac4e3f4e11f72cd)ARPHRD\_IEEE802154\_PHY

| #define ARPHRD\_IEEE802154\_PHY   805 /\* IEEE 802.15.4 PHY header. \*/ |
| --- |

## [◆ ](#a00bc6b1bb5f426bb58241ba16ad870e7)ARPHRD\_IEEE802\_TR

| #define ARPHRD\_IEEE802\_TR   800 /\* Magic type ident for TR. \*/ |
| --- |

## [◆ ](#abb8ca5a62f0f53187a295f0e96ba208b)ARPHRD\_INFINIBAND

| #define ARPHRD\_INFINIBAND   32 /\* InfiniBand. \*/ |
| --- |

## [◆ ](#a47668de0966a3040187f2a640253278b)ARPHRD\_IPDDP

| #define ARPHRD\_IPDDP   777 /\* IP-in-DDP tunnel. \*/ |
| --- |

## [◆ ](#abc6758e951b1761b8ae3748d66b8b830)ARPHRD\_IPGRE

| #define ARPHRD\_IPGRE   778 /\* GRE over IP. \*/ |
| --- |

## [◆ ](#a09d2e25da54b5044c67e6ea285a26728)ARPHRD\_IRDA

| #define ARPHRD\_IRDA   783 /\* Linux-IrDA. \*/ |
| --- |

## [◆ ](#af09e5ae697b5b32f1e9d053b22a2642c)ARPHRD\_LAPB

| #define ARPHRD\_LAPB   516 /\* LAPB. \*/ |
| --- |

## [◆ ](#a2a6a8456b8d00c4751937f7361d77c87)ARPHRD\_LOCALTLK

| #define ARPHRD\_LOCALTLK   773 /\* Localtalk device. \*/ |
| --- |

## [◆ ](#a4ee77f8d80bda9f59f5bd7163854e425)ARPHRD\_LOOPBACK

| #define ARPHRD\_LOOPBACK   772 /\* Loopback device. \*/ |
| --- |

## [◆ ](#ab490545ded34d438fe2fcc1eaaa39c1e)ARPHRD\_MCTP

| #define ARPHRD\_MCTP   290 |
| --- |

## [◆ ](#ad597c946041d8b4d02b41c3b2145e10a)ARPHRD\_METRICOM

| #define ARPHRD\_METRICOM   23 /\* Metricom STRIP (new IANA id). \*/ |
| --- |

## [◆ ](#ae1acb8a91a94d38dd411fb5e719f35b0)ARPHRD\_NETROM

| #define ARPHRD\_NETROM   0 /\* From KA9Q: NET/ROM pseudo. \*/ |
| --- |

## [◆ ](#af54d98448c0e1e1b02d9e565508a4280)ARPHRD\_NONE

| #define ARPHRD\_NONE   0xFFFE /\* Zero header length. \*/ |
| --- |

## [◆ ](#a90dfe4049e2164cc19bd3b54f2bd2e3f)ARPHRD\_PIMREG

| #define ARPHRD\_PIMREG   779 /\* PIMSM register interface. \*/ |
| --- |

## [◆ ](#a18dec8be041946b4a3a75ec73bb4293c)ARPHRD\_PPP

| #define ARPHRD\_PPP   512 |
| --- |

## [◆ ](#a394dfc37c8b6c429af9d6562a76b0c99)ARPHRD\_PRONET

| #define ARPHRD\_PRONET   4 /\* PROnet token ring. \*/ |
| --- |

## [◆ ](#a67c7faf6cac1fbc281e82cae47360f30)ARPHRD\_RAWHDLC

| #define ARPHRD\_RAWHDLC   518 /\* Raw HDLC. \*/ |
| --- |

## [◆ ](#ab2b4f27b07b7e2d03e5873f32089dc23)ARPHRD\_RAWIP

| #define ARPHRD\_RAWIP   519 /\* Raw IP. \*/ |
| --- |

## [◆ ](#aea2aa154ca4cc488c86727dc44b36b19)ARPHRD\_ROSE

| #define ARPHRD\_ROSE   270 |
| --- |

## [◆ ](#af34e0978e6bb11cf230b5b691a5a1b8a)ARPHRD\_RSRVD

| #define ARPHRD\_RSRVD   260 /\* Notional KISS type. \*/ |
| --- |

## [◆ ](#a40d57acc78d91f5f2bd6ebae7db18aeb)ARPHRD\_SIT

| #define ARPHRD\_SIT   776 /\* sit0 [device](structdevice.md) - IPv6-in-IPv4. \*/ |
| --- |

## [◆ ](#a282f35b40f5bdb27cfa179e498934c81)ARPHRD\_SKIP

| #define ARPHRD\_SKIP   771 /\* SKIP vif. \*/ |
| --- |

## [◆ ](#a45d939a8b7cfeb1145cc5a49f6d2a399)ARPHRD\_SLIP

| #define ARPHRD\_SLIP   256 |
| --- |

## [◆ ](#ae35c4cbe46fc19d363a7af42c6dcf273)ARPHRD\_SLIP6

| #define ARPHRD\_SLIP6   258 |
| --- |

## [◆ ](#a258c6b24592ed0bfffd287bcf72184cd)ARPHRD\_TUNNEL

| #define ARPHRD\_TUNNEL   768 /\* IPIP tunnel. \*/ |
| --- |

## [◆ ](#a28d782f6db80ae8ada7f213842ff2869)ARPHRD\_TUNNEL6

| #define ARPHRD\_TUNNEL6   769 /\* IPIP6 tunnel. \*/ |
| --- |

## [◆ ](#a9bc958dad255bdc3fc3fbe067adaf017)ARPHRD\_VOID

| #define ARPHRD\_VOID   0xFFFF /\* Void type, nothing is known. \*/ |
| --- |

## [◆ ](#a1faa7cf295013abcee809dc908d9be6b)ARPHRD\_X25

| #define ARPHRD\_X25   271 /\* CCITT X.25. \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [net](dir_2c168081a5287170970afe4d92a99d1b.md)
- [if\_arp.h](if__arp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
