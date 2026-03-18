---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__lldp__chassis__tlv.html
original_path: doxygen/html/structnet__lldp__chassis__tlv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_lldp\_chassis\_tlv Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Link Layer Discovery Protocol definitions and helpers](group__lldp.md)

Chassis ID TLV, see chapter 8.5.2 in IEEE 802.1AB.
[More...](#details)

`#include <[lldp.h](lldp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [type\_length](#af81d3102ad0ec1f7ef76bb1533dcc7cd) |
|  | 7 bits for type, 9 bits for length |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subtype](#ad9d415f6a1e9018953728de1b529fd98) |
|  | ID subtype. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [value](#a37b7e81a670595d1c6c77a45bf9cfc73) [NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN] |
|  | Chassis ID value. |

## Detailed Description

Chassis ID TLV, see chapter 8.5.2 in IEEE 802.1AB.

## Field Documentation

## [◆ ](#ad9d415f6a1e9018953728de1b529fd98)subtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_lldp\_chassis\_tlv::subtype |
| --- |

ID subtype.

## [◆ ](#af81d3102ad0ec1f7ef76bb1533dcc7cd)type\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_lldp\_chassis\_tlv::type\_length |
| --- |

7 bits for type, 9 bits for length

## [◆ ](#a37b7e81a670595d1c6c77a45bf9cfc73)value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_lldp\_chassis\_tlv::value[NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN] |
| --- |

Chassis ID value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lldp.h](lldp_8h_source.md)

- [net\_lldp\_chassis\_tlv](structnet__lldp__chassis__tlv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
