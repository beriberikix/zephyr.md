---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet__vlan_8h.html
original_path: doxygen/html/ethernet__vlan_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_vlan.h File Reference

VLAN specific definitions.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](ethernet__vlan_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_VLAN\_TAG\_UNSPEC](group__vlan__api.md#ga665458f4b8f9c83ea0c1609207d3dd70)   0x0fff |
|  | Unspecified VLAN tag value. |
| #define | [NET\_VLAN\_TAG\_PRIORITY](group__vlan__api.md#gad1db5bb85a9744c8a8af8d2e1ebcfe69)   0x0000 |
|  | VLAN ID for forwarding to the native interface (priority tagging). |

| Functions | |
| --- | --- |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_get\_vid](group__vlan__api.md#gad12123bb6c9920f21a6faed0e9bf70a6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get VLAN identifier from TCI. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_eth\_vlan\_get\_dei](group__vlan__api.md#ga090648b166db1dc5ee9db71bfba1f97b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get Drop Eligible Indicator from TCI. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_eth\_vlan\_get\_pcp](group__vlan__api.md#gafc746a075a23e4ad2c1c76328a8d773a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci) |
|  | Get Priority Code Point from TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_vid](group__vlan__api.md#ga06b2977281f627ebb9529512aecc20dd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set VLAN identifier to TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_dei](group__vlan__api.md#ga6fcea099258c6be9c7cbfbd92fd4e8ab) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dei) |
|  | Set Drop Eligible Indicator to TCI. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_vlan\_set\_pcp](group__vlan__api.md#gadee54f9a2af345dd3981f39d73e1bc10) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tci, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcp) |
|  | Set Priority Code Point to TCI. |

## Detailed Description

VLAN specific definitions.

Virtual LAN specific definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_vlan.h](ethernet__vlan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
