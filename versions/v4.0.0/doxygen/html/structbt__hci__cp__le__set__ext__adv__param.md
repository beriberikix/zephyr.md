---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__cp__le__set__ext__adv__param.html
original_path: doxygen/html/structbt__hci__cp__le__set__ext__adv__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_le\_set\_ext\_adv\_param Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [handle](#a65fe609dde9515212659087a024e7c65) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [props](#a4af102ae90ca6917b3134491c5ff079f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prim\_min\_interval](#ab5a80941b3d832c2906daed8cf069a02) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prim\_max\_interval](#a08aa741a56e825a11424bf024ac65e14) [3] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prim\_channel\_map](#ad7a0b9028bcdb57a9011d4677412aed5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [own\_addr\_type](#a3594f7337ccd739f59ac7845757de0e8) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [peer\_addr](#a819e599df4025036fab2dabd7c61ea37) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [filter\_policy](#a29a62f8989f89b014cadbad9b94e996a) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a5f7f3e477b5b0b8122b85f3e53dd7878) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prim\_adv\_phy](#a048874197ccbdbc626f0563be5c41ec7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sec\_adv\_max\_skip](#a5793c6afe545290a1e792bcc73585b72) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sec\_adv\_phy](#abc82ba984647eb00bc490c01ce746a15) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#af8bc3509fdd5e89c27db466727fe1cd9) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [scan\_req\_notify\_enable](#ae694df46b1db4b029d1e177768b3821f) |

## Field Documentation

## [◆ ](#a29a62f8989f89b014cadbad9b94e996a)filter\_policy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::filter\_policy |
| --- |

## [◆ ](#a65fe609dde9515212659087a024e7c65)handle

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::handle |
| --- |

## [◆ ](#a3594f7337ccd739f59ac7845757de0e8)own\_addr\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::own\_addr\_type |
| --- |

## [◆ ](#a819e599df4025036fab2dabd7c61ea37)peer\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_cp\_le\_set\_ext\_adv\_param::peer\_addr |
| --- |

## [◆ ](#a048874197ccbdbc626f0563be5c41ec7)prim\_adv\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_adv\_phy |
| --- |

## [◆ ](#ad7a0b9028bcdb57a9011d4677412aed5)prim\_channel\_map

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_channel\_map |
| --- |

## [◆ ](#a08aa741a56e825a11424bf024ac65e14)prim\_max\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_max\_interval[3] |
| --- |

## [◆ ](#ab5a80941b3d832c2906daed8cf069a02)prim\_min\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::prim\_min\_interval[3] |
| --- |

## [◆ ](#a4af102ae90ca6917b3134491c5ff079f)props

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_le\_set\_ext\_adv\_param::props |
| --- |

## [◆ ](#ae694df46b1db4b029d1e177768b3821f)scan\_req\_notify\_enable

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::scan\_req\_notify\_enable |
| --- |

## [◆ ](#a5793c6afe545290a1e792bcc73585b72)sec\_adv\_max\_skip

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_max\_skip |
| --- |

## [◆ ](#abc82ba984647eb00bc490c01ce746a15)sec\_adv\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::sec\_adv\_phy |
| --- |

## [◆ ](#af8bc3509fdd5e89c27db466727fe1cd9)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_le\_set\_ext\_adv\_param::sid |
| --- |

## [◆ ](#a5f7f3e477b5b0b8122b85f3e53dd7878)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_cp\_le\_set\_ext\_adv\_param::tx\_power |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_cp\_le\_set\_ext\_adv\_param](structbt__hci__cp__le__set__ext__adv__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
