---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__igmp.html
original_path: doxygen/html/group__igmp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IGMP API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

IGMP (Internet Group Management Protocol).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [igmp\_param](structigmp__param.md) |
|  | IGMP parameters. [More...](structigmp__param.md#details) |

| Functions | |
| --- | --- |
| static int | [net\_ipv4\_igmp\_join](#ga39227f2f4c2f0e7b0be8ac3cff080df0) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr, const struct [igmp\_param](structigmp__param.md) \*param) |
|  | Join a given multicast group. |
| static int | [net\_ipv4\_igmp\_leave](#gae92a971ee047049e05a16779100cb08b) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Leave a given multicast group. |

## Detailed Description

IGMP (Internet Group Management Protocol).

## Function Documentation

## [◆ ](#ga39227f2f4c2f0e7b0be8ac3cff080df0)net\_ipv4\_igmp\_join()

| | int net\_ipv4\_igmp\_join | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr*, | |  |  | const struct [igmp\_param](structigmp__param.md) \* | *param* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[igmp.h](igmp_8h.md)>`

Join a given multicast group.

Parameters
:   | iface | Network interface where join message is sent |
    | --- | --- |
    | addr | Multicast group to join |
    | param | Optional parameters |

Returns
:   Return 0 if joining was done, <0 otherwise.

## [◆ ](#gae92a971ee047049e05a16779100cb08b)net\_ipv4\_igmp\_leave()

| | int net\_ipv4\_igmp\_leave | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[igmp.h](igmp_8h.md)>`

Leave a given multicast group.

Parameters
:   | iface | Network interface where leave message is sent |
    | --- | --- |
    | addr | Multicast group to leave |

Returns
:   Return 0 if leaving is done, <0 otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
