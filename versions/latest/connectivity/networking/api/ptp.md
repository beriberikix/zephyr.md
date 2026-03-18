---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/ptp.html
original_path: connectivity/networking/api/ptp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Precision Time Protocol (PTP)

## [Overview](#id3)

PTP is a network protocol implemented in the application layer, used to synchronize
clocks in a computer network. It’s accurate up to less than a microsecond.
The stack supports the protocol and procedures as defined in the [IEEE 1588-2019 standard](https://standards.ieee.org/ieee/1588/6825/)
(IEEE Standard for a Precision Clock Synchronization Protocol
for Networked Measurement and Control Systems). It has multiple profiles,
and can be implemented on top of L2 (Ethernet) or L3 (UDP/IPv4 or UDP/IPv6).
Its accuracy is achieved by using hardware timestamping of the protocol packets.

Zephyr’s implementation of PTP stack consist following items:

- PTP stack thread that handles incoming messages and events
- Integration with ptp\_clock driver
- PTP stack initialization executed during system init

The implementation automatically creates PTP Ports (each PTP Port corresponds to unique interface).

## [Supported features](#id4)

Implementation of the stack doesn’t support all features specified in the standard.
In the table below all supported features are listed.

Supported features

| Feature | Supported |
| --- | --- |
| Ordinary Clock | yes |
| Boundary Clock | yes |
| Transparent Clock |  |
| Management Node |  |
| End to end delay mechanism | yes |
| Peer to peer delay mechanism |  |
| Multicast operation mode |  |
| Hybrid operation mode |  |
| Unicast operation mode |  |
| Non-volatile storage |  |
| UDP IPv4 transport protocol | yes |
| UDP IPv6 transport protocol | yes |
| IEEE 802.3 (Ethernet) transport protocol |  |
| Hardware timestamping | yes |
| Software timestamping |  |
| TIME\_RECEIVER\_ONLY PTP Instance | yes |
| TIME\_TRANSMITTER\_ONLY PTP Instance |  |

## [Supported Management messages](#id5)

Based on Table 59 from section 15.5.2.3 of the IEEE 1588-2019 following management TLVs
are supported:

Supported management message’s IDs

| Management\_ID | Management\_ID name | Allowed actions |
| --- | --- | --- |
| 0x0000 | NULL\_PTP\_MANAGEMENT | GET SET COMMAND |
| 0x0001 | CLOCK\_DESCRIPTION | GET |
| 0x0002 | USER\_DESCRIPTION | GET |
| 0x0003 | SAVE\_IN\_NON\_VOLATILE\_STORAGE |  |
| 0x0004 | RESET\_NON\_VOLATILE\_STORAGE |  |
| 0x0005 | INITIALIZE |  |
| 0x0006 | FAULT\_LOG |  |
| 0x0007 | FAULT\_LOG\_RESET |  |
| 0x2000 | DEFAULT\_DATA\_SET | GET |
| 0x2001 | CURRENT\_DATA\_SET | GET |
| 0x2002 | PARENT\_DATA\_SET | GET |
| 0x2003 | TIME\_PROPERTIES\_DATA\_SET | GET |
| 0x2004 | PORT\_DATA\_SET | GET |
| 0x2005 | PRIORITY1 | GET SET |
| 0x2006 | PRIORITY2 | GET SET |
| 0x2007 | DOMAIN | GET SET |
| 0x2008 | TIME\_RECEIVER\_ONLY | GET SET |
| 0x2009 | LOG\_ANNOUNCE\_INTERVAL | GET SET |
| 0x200A | ANNOUNCE\_RECEIPT\_TIMEOUT | GET SET |
| 0x200B | LOG\_SYNC\_INTERVAL | GET SET |
| 0x200C | VERSION\_NUMBER | GET SET |
| 0x200D | ENABLE\_PORT | COMMAND |
| 0x200E | DISABLE\_PORT | COMMAND |
| 0x200F | TIME | GET SET |
| 0x2010 | CLOCK\_ACCURACY | GET SET |
| 0x2011 | UTC\_PROPERTIES | GET SET |
| 0x2012 | TRACEBILITY\_PROPERTIES | GET SET |
| 0x2013 | TIMESCALE\_PROPERTIES | GET SET |
| 0x2014 | UNICAST\_NEGOTIATION\_ENABLE |  |
| 0x2015 | PATH\_TRACE\_LIST |  |
| 0x2016 | PATH\_TRACE\_ENABLE |  |
| 0x2017 | GRANDMASTER\_CLUSTER\_TABLE |  |
| 0x2018 | UNICAST\_TIME\_TRANSMITTER\_TABLE |  |
| 0x2019 | UNICAST\_TIME\_TRANSMITTER\_MAX\_TABLE\_SIZE |  |
| 0x201A | ACCEPTABLE\_TIME\_TRANSMITTER\_TABLE |  |
| 0x201B | ACCEPTABLE\_TIME\_TRANSMITTER\_TABLE\_ENABLED |  |
| 0x201C | ACCEPTABLE\_TIME\_TRANSMITTER\_MAX\_TABLE\_SIZE |  |
| 0x201D | ALTERNATE\_TIME\_TRANSMITTER |  |
| 0x201E | ALTERNATE\_TIME\_OFFSET\_ENABLE |  |
| 0x201F | ALTERNATE\_TIME\_OFFSET\_NAME |  |
| 0x2020 | ALTERNATE\_TIME\_OFFSET\_MAX\_KEY |  |
| 0x2021 | ALTERNATE\_TIME\_OFFSET\_PROPERTIES |  |
| 0x3000 | EXTERNAL\_PORT\_CONFIGURATION\_ENABLED |  |
| 0x3001 | TIME\_TRANSMITTER\_ONLY |  |
| 0x3002 | HOLDOVER\_UPGRADE\_ENABLE |  |
| 0x3003 | EXT\_PORT\_CONFIG\_PORT\_DATA\_SET |  |
| 0x4000 | TRANSPARENT\_CLOCK\_DEFAULT\_DATA\_SET |  |
| 0x4001 | TRANSPARENT\_CLOCK\_PORT\_DATA\_SET |  |
| 0x4002 | PRIMARY\_DOMAIN |  |
| 0x6000 | DELAY\_MECHANISM | GET |
| 0x6001 | LOG\_MIN\_PDELAY\_REQ\_INTERVAL | GET SET |

## [Enabling the stack](#id6)

The following configuration option must me enabled in `prj.conf` file.

- [`CONFIG_PTP`](../../../kconfig.md#CONFIG_PTP "CONFIG_PTP")

## [Testing](#id7)

The stack has been informally tested using the
[Linux ptp4l](http://linuxptp.sourceforge.net/) daemons.
The [PTP sample application](../../../samples/net/ptp/README.md#ptp "Enable PTP support and monitor messages and events via logging.") from the Zephyr
source distribution can be used for testing.

## [API Reference](#id8)

Related code samples

[PTP](../../../samples/net/ptp/README.md#ptp "Enable PTP support and monitor messages and events via logging.")
:   Enable PTP support and monitor messages and events via logging.

*group* PTP support
:   Precision Time Protocol (PTP) support.

    Defines

    PTP\_MAJOR\_VERSION
    :   Major PTP Version.

    PTP\_MINOR\_VERSION
    :   Minor PTP Version.

    PTP\_VERSION
    :   PTP version IEEE-1588:2019.
