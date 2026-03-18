---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__ieee802154__l2.html
original_path: doxygen/html/group__ieee802154__l2.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IEEE 802.15.4 L2

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md)

IEEE 802.15.4 L2 APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_security\_ctx](structieee802154__security__ctx.md) |
|  | Interface-level security attributes, see section 9.5. [More...](structieee802154__security__ctx.md#details) |
| struct | [ieee802154\_context](structieee802154__context.md) |
|  | IEEE 802.15.4 L2 context. [More...](structieee802154__context.md#details) |

| Macros | |
| --- | --- |
| #define | [IEEE802154\_MAX\_PHY\_PACKET\_SIZE](#gac63b5ae7ed99b168871b5fc08ecde7a1)   127 |
|  | Represents the PHY constant aMaxPhyPacketSize, see section 11.3. |
| #define | [IEEE802154\_FCS\_LENGTH](#ga1243000b59167777e078060fd3c1c218)   2 |
|  | Represents the frame check sequence length, see section 7.2.1.1. |
| #define | [IEEE802154\_MTU](#ga987d42d1d8117ec58cf3f9cae4e66139)   ([IEEE802154\_MAX\_PHY\_PACKET\_SIZE](#gac63b5ae7ed99b168871b5fc08ecde7a1) - [IEEE802154\_FCS\_LENGTH](#ga1243000b59167777e078060fd3c1c218)) |
|  | IEEE 802.15.4 "hardware" MTU (not to be confused with L3/IP MTU), i.e. |
| #define | [IEEE802154\_SHORT\_ADDR\_LENGTH](#gaee7ec8e4ba396f3cd658bcb22a9352e8)   2 |
|  | IEEE 802.15.4 short address length. |
| #define | [IEEE802154\_EXT\_ADDR\_LENGTH](#ga355350794ec26788bc855da53d311bea)   8 |
|  | IEEE 802.15.4 extended address length. |
| #define | [IEEE802154\_MAX\_ADDR\_LENGTH](#gae405ed23baf91fa3d96c81d5121faa1a)   [IEEE802154\_EXT\_ADDR\_LENGTH](#ga355350794ec26788bc855da53d311bea) |
|  | IEEE 802.15.4 maximum address length. |
| #define | [IEEE802154\_NO\_CHANNEL](#ga692a16d957c1e1ce76808cda325fd6c5)   USHRT\_MAX |
|  | A special channel value that symbolizes "all" channels or "any" channel - depending on context. |
| #define | [IEEE802154\_BROADCAST\_ADDRESS](#gafae1906dc9b39c93690b127efaaacacb)   0xffff |
|  | Represents the IEEE 802.15.4 broadcast short address, see sections 6.1 and 8.4.3, table 8-94, macShortAddress. |
| #define | [IEEE802154\_NO\_SHORT\_ADDRESS\_ASSIGNED](#ga43369b4a9ea0961395cd135b9fe18d03)   0xfffe |
|  | Represents a special IEEE 802.15.4 short address that indicates that a device has been associated with a coordinator but did not receive a short address, see sections 6.4.1 and 8.4.3, table 8-94, macShortAddress. |
| #define | [IEEE802154\_BROADCAST\_PAN\_ID](#ga1a40fed9dcd802af0283d7808e8b283b)   0xffff |
|  | Represents the IEEE 802.15.4 broadcast PAN ID, see section 6.1. |
| #define | [IEEE802154\_SHORT\_ADDRESS\_NOT\_ASSOCIATED](#gaf6718b4e9873d9b2e6786103ebcea1bc)   [IEEE802154\_BROADCAST\_ADDRESS](#gafae1906dc9b39c93690b127efaaacacb) |
|  | Represents a special value of the macShortAddress MAC PIB attribute, while the device is not associated, see section 8.4.3, table 8-94. |
| #define | [IEEE802154\_PAN\_ID\_NOT\_ASSOCIATED](#ga89cc35f42374255c986bcd23f15bfc14)   [IEEE802154\_BROADCAST\_PAN\_ID](#ga1a40fed9dcd802af0283d7808e8b283b) |
|  | Represents a special value of the macPanId MAC PIB attribute, while the device is not associated, see section 8.4.3, table 8-94. |

| Enumerations | |
| --- | --- |
| enum | [ieee802154\_device\_role](#ga7a4fb2d89381bba54514bf8396fb6d26) { [IEEE802154\_DEVICE\_ROLE\_ENDDEVICE](#gga7a4fb2d89381bba54514bf8396fb6d26a9909ce934f56e6b5b6c1bc53345a65b5) , [IEEE802154\_DEVICE\_ROLE\_COORDINATOR](#gga7a4fb2d89381bba54514bf8396fb6d26abc23f55210c7ff0747bddc9c679b4f68) , [IEEE802154\_DEVICE\_ROLE\_PAN\_COORDINATOR](#gga7a4fb2d89381bba54514bf8396fb6d26a2b25d9e19f374d3f3ef6329bdf942340) } |
|  | IEEE 802.15.4 device role. [More...](#ga7a4fb2d89381bba54514bf8396fb6d26) |

## Detailed Description

IEEE 802.15.4 L2 APIs.

Since
:   1.0

Version
:   0.8.0

This API provides integration with Zephyr's sockets and network contexts. **Application and driver developers should never interface directly with this API.** It is of interest to subsystem maintainers only.

The API implements and extends the following structures:

- implements Zephyr's internal L2-level socket and network context abstractions (context/socket operations, see [Network L2 Abstraction Layer](group__net__l2.md "Network L2 Abstraction Layer")),
- protocol-specific extension to the interface structure (see [Network Interface abstraction layer](group__net__if.md "Network Interface abstraction layer"))
- protocol-specific extensions to the network packet structure (see [Network Packet Library](group__net__pkt.md "Network Packet Library")),

Note
:   All section, table and figure references are to the IEEE 802.15.4-2020 standard.

## Macro Definition Documentation

## [◆ ](#gafae1906dc9b39c93690b127efaaacacb)IEEE802154\_BROADCAST\_ADDRESS

| #define IEEE802154\_BROADCAST\_ADDRESS   0xffff |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents the IEEE 802.15.4 broadcast short address, see sections 6.1 and 8.4.3, table 8-94, macShortAddress.

## [◆ ](#ga1a40fed9dcd802af0283d7808e8b283b)IEEE802154\_BROADCAST\_PAN\_ID

| #define IEEE802154\_BROADCAST\_PAN\_ID   0xffff |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents the IEEE 802.15.4 broadcast PAN ID, see section 6.1.

## [◆ ](#ga355350794ec26788bc855da53d311bea)IEEE802154\_EXT\_ADDR\_LENGTH

| #define IEEE802154\_EXT\_ADDR\_LENGTH   8 |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

IEEE 802.15.4 extended address length.

## [◆ ](#ga1243000b59167777e078060fd3c1c218)IEEE802154\_FCS\_LENGTH

| #define IEEE802154\_FCS\_LENGTH   2 |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents the frame check sequence length, see section 7.2.1.1.

Note
:   Currently only a 2 byte FCS is supported although some PHYs (e.g. SUN, TVWS, ...) optionally support a 4 byte FCS. Needs to be changed once those PHYs should be fully supported.

## [◆ ](#gae405ed23baf91fa3d96c81d5121faa1a)IEEE802154\_MAX\_ADDR\_LENGTH

| #define IEEE802154\_MAX\_ADDR\_LENGTH   [IEEE802154\_EXT\_ADDR\_LENGTH](#ga355350794ec26788bc855da53d311bea) |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

IEEE 802.15.4 maximum address length.

## [◆ ](#gac63b5ae7ed99b168871b5fc08ecde7a1)IEEE802154\_MAX\_PHY\_PACKET\_SIZE

| #define IEEE802154\_MAX\_PHY\_PACKET\_SIZE   127 |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents the PHY constant aMaxPhyPacketSize, see section 11.3.

Note
:   Currently only 127 byte sized packets are supported although some PHYs (e.g. SUN, MSK, LECIM, ...) support larger packet sizes. Needs to be changed once those PHYs should be fully supported.

## [◆ ](#ga987d42d1d8117ec58cf3f9cae4e66139)IEEE802154\_MTU

| #define IEEE802154\_MTU   ([IEEE802154\_MAX\_PHY\_PACKET\_SIZE](#gac63b5ae7ed99b168871b5fc08ecde7a1) - [IEEE802154\_FCS\_LENGTH](#ga1243000b59167777e078060fd3c1c218)) |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

IEEE 802.15.4 "hardware" MTU (not to be confused with L3/IP MTU), i.e.

the actual payload available to the next higher layer.

This is equivalent to the IEEE 802.15.4 MAC frame length minus checksum bytes which is again equivalent to the PHY payload aka PSDU length minus checksum bytes. This definition exists for compatibility with the same concept in Linux and Zephyr's L3. It is not a concept from the IEEE 802.15.4 standard.

Note
:   Currently only the original frame size from the 2006 standard version and earlier is supported. The 2015+ standard introduced PHYs with larger PHY payload. These are not (yet) supported in Zephyr.

## [◆ ](#ga692a16d957c1e1ce76808cda325fd6c5)IEEE802154\_NO\_CHANNEL

| #define IEEE802154\_NO\_CHANNEL   USHRT\_MAX |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

A special channel value that symbolizes "all" channels or "any" channel - depending on context.

## [◆ ](#ga43369b4a9ea0961395cd135b9fe18d03)IEEE802154\_NO\_SHORT\_ADDRESS\_ASSIGNED

| #define IEEE802154\_NO\_SHORT\_ADDRESS\_ASSIGNED   0xfffe |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents a special IEEE 802.15.4 short address that indicates that a device has been associated with a coordinator but did not receive a short address, see sections 6.4.1 and 8.4.3, table 8-94, macShortAddress.

## [◆ ](#ga89cc35f42374255c986bcd23f15bfc14)IEEE802154\_PAN\_ID\_NOT\_ASSOCIATED

| #define IEEE802154\_PAN\_ID\_NOT\_ASSOCIATED   [IEEE802154\_BROADCAST\_PAN\_ID](#ga1a40fed9dcd802af0283d7808e8b283b) |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents a special value of the macPanId MAC PIB attribute, while the device is not associated, see section 8.4.3, table 8-94.

## [◆ ](#gaee7ec8e4ba396f3cd658bcb22a9352e8)IEEE802154\_SHORT\_ADDR\_LENGTH

| #define IEEE802154\_SHORT\_ADDR\_LENGTH   2 |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

IEEE 802.15.4 short address length.

## [◆ ](#gaf6718b4e9873d9b2e6786103ebcea1bc)IEEE802154\_SHORT\_ADDRESS\_NOT\_ASSOCIATED

| #define IEEE802154\_SHORT\_ADDRESS\_NOT\_ASSOCIATED   [IEEE802154\_BROADCAST\_ADDRESS](#gafae1906dc9b39c93690b127efaaacacb) |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

Represents a special value of the macShortAddress MAC PIB attribute, while the device is not associated, see section 8.4.3, table 8-94.

## Enumeration Type Documentation

## [◆ ](#ga7a4fb2d89381bba54514bf8396fb6d26)ieee802154\_device\_role

| enum [ieee802154\_device\_role](#ga7a4fb2d89381bba54514bf8396fb6d26) |
| --- |

`#include <[ieee802154.h](ieee802154_8h.md)>`

IEEE 802.15.4 device role.

| Enumerator | |
| --- | --- |
| IEEE802154\_DEVICE\_ROLE\_ENDDEVICE | End device. |
| IEEE802154\_DEVICE\_ROLE\_COORDINATOR | Coordinator. |
| IEEE802154\_DEVICE\_ROLE\_PAN\_COORDINATOR | PAN coordinator. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
