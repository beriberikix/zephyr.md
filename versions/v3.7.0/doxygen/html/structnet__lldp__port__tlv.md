---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__lldp__port__tlv.html
original_path: doxygen/html/structnet__lldp__port__tlv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_lldp\_port\_tlv Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Link Layer Discovery Protocol definitions and helpers](group__lldp.md)

Port ID TLV, see chapter 8.5.3 in IEEE 802.1AB.
[More...](#details)

`#include <[lldp.h](lldp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [type\_length](#a710beaeda2ddd7933464e07cb87a2bfe) |
|  | 7 bits for type, 9 bits for length |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subtype](#a572a6fd721c68796a572410ac62f2f93) |
|  | ID subtype. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [value](#aecc83eaec39284b33c2e7cf07f0ffa05) [NET\_LLDP\_PORT\_ID\_VALUE\_LEN] |
|  | Port ID value. |

## Detailed Description

Port ID TLV, see chapter 8.5.3 in IEEE 802.1AB.

## Field Documentation

## [◆ ](#a572a6fd721c68796a572410ac62f2f93)subtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_lldp\_port\_tlv::subtype |
| --- |

ID subtype.

## [◆ ](#a710beaeda2ddd7933464e07cb87a2bfe)type\_length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_lldp\_port\_tlv::type\_length |
| --- |

7 bits for type, 9 bits for length

## [◆ ](#aecc83eaec39284b33c2e7cf07f0ffa05)value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_lldp\_port\_tlv::value[NET\_LLDP\_PORT\_ID\_VALUE\_LEN] |
| --- |

Port ID value.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lldp.h](lldp_8h_source.md)

- [net\_lldp\_port\_tlv](structnet__lldp__port__tlv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
