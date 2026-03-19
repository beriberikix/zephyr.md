---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__vlan__api.html
original_path: doxygen/html/group__vlan__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Virtual LAN definitions and helpers

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

VLAN definitions and helpers.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [NET\_VLAN\_TAG\_UNSPEC](#ga665458f4b8f9c83ea0c1609207d3dd70)   0x0fff |
|  | Unspecified VLAN tag value. |
| #define | [NET\_VLAN\_TAG\_PRIORITY](#gad1db5bb85a9744c8a8af8d2e1ebcfe69)   0x0000 |
|  | VLAN ID for forwarding to the native interface (priority tagging). |

| Functions | |
| --- | --- |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_get\_vid](#gad12123bb6c9920f21a6faed0e9bf70a6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get VLAN identifier from TCI. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_eth\_vlan\_get\_dei](#ga090648b166db1dc5ee9db71bfba1f97b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get Drop Eligible Indicator from TCI. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_eth\_vlan\_get\_pcp](#gafc746a075a23e4ad2c1c76328a8d773a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get Priority Code Point from TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_vid](#ga06b2977281f627ebb9529512aecc20dd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set VLAN identifier to TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_dei](#ga6fcea099258c6be9c7cbfbd92fd4e8ab) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dei) |
|  | Set Drop Eligible Indicator to TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_pcp](#gadee54f9a2af345dd3981f39d73e1bc10) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcp) |
|  | Set Priority Code Point to TCI. |

## Detailed Description

VLAN definitions and helpers.

Since
:   1.12

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gad1db5bb85a9744c8a8af8d2e1ebcfe69)NET\_VLAN\_TAG\_PRIORITY

| #define NET\_VLAN\_TAG\_PRIORITY   0x0000 |
| --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

VLAN ID for forwarding to the native interface (priority tagging).

## [◆ ](#ga665458f4b8f9c83ea0c1609207d3dd70)NET\_VLAN\_TAG\_UNSPEC

| #define NET\_VLAN\_TAG\_UNSPEC   0x0fff |
| --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Unspecified VLAN tag value.

## Function Documentation

## [◆ ](#ga090648b166db1dc5ee9db71bfba1f97b)net\_eth\_vlan\_get\_dei()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_eth\_vlan\_get\_dei | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Get Drop Eligible Indicator from TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |

Returns
:   Drop eligible indicator.

## [◆ ](#gafc746a075a23e4ad2c1c76328a8d773a)net\_eth\_vlan\_get\_pcp()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_eth\_vlan\_get\_pcp | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Get Priority Code Point from TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |

Returns
:   Priority code point.

## [◆ ](#gad12123bb6c9920f21a6faed0e9bf70a6)net\_eth\_vlan\_get\_vid()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_eth\_vlan\_get\_vid | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Get VLAN identifier from TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |

Returns
:   VLAN identifier.

## [◆ ](#ga6fcea099258c6be9c7cbfbd92fd4e8ab)net\_eth\_vlan\_set\_dei()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_eth\_vlan\_set\_dei | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *dei* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Set Drop Eligible Indicator to TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |
    | dei | Drop eligible indicator. |

Returns
:   New TCI value.

## [◆ ](#gadee54f9a2af345dd3981f39d73e1bc10)net\_eth\_vlan\_set\_pcp()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_eth\_vlan\_set\_pcp | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pcp* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Set Priority Code Point to TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |
    | pcp | Priority code point. |

Returns
:   New TCI value.

## [◆ ](#ga06b2977281f627ebb9529512aecc20dd)net\_eth\_vlan\_set\_vid()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_eth\_vlan\_set\_vid | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tci*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vid* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ethernet_vlan.h](ethernet__vlan_8h.md)>`

Set VLAN identifier to TCI.

Parameters
:   | tci | VLAN tag control information. |
    | --- | --- |
    | vid | VLAN identifier. |

Returns
:   New TCI value.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
