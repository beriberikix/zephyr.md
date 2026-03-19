---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mld.html
original_path: doxygen/html/group__mld.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Multicast Listener Discovery API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

MLD (Multicast Listener Discovery).
[More...](#details)

| Functions | |
| --- | --- |
| static int | [net\_ipv6\_mld\_join](#ga53af11b1107b0375d219f2a3f517fcce) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Join a given multicast group. |
| static int | [net\_ipv6\_mld\_leave](#gaa1ccc2b362787fe28fb118af51b49465) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Leave a given multicast group. |

## Detailed Description

MLD (Multicast Listener Discovery).

Since
:   1.8

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga53af11b1107b0375d219f2a3f517fcce)net\_ipv6\_mld\_join()

| | int net\_ipv6\_mld\_join | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mld.h](mld_8h.md)>`

Join a given multicast group.

Parameters
:   | iface | Network interface where join message is sent |
    | --- | --- |
    | addr | Multicast group to join |

Returns
:   0 if joining was done, <0 otherwise.

## [◆ ](#gaa1ccc2b362787fe28fb118af51b49465)net\_ipv6\_mld\_leave()

| | int net\_ipv6\_mld\_leave | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mld.h](mld_8h.md)>`

Leave a given multicast group.

Parameters
:   | iface | Network interface where leave message is sent |
    | --- | --- |
    | addr | Multicast group to leave |

Returns
:   0 if leaving is done, <0 otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
