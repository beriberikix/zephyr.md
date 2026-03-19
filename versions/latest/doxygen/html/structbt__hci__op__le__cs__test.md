---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__hci__op__le__cs__test.html
original_path: doxygen/html/structbt__hci__op__le__cs__test.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_op\_le\_cs\_test Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [main\_mode\_type](#af4cdfd8c8cab500277c06a82ac088577) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sub\_mode\_type](#a090c5d03cf829011196d644cd9f7c7db) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [main\_mode\_repetition](#a60cc9a7c46f8cd0933dc2f5a68cca627) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mode\_0\_steps](#aaf480890608b5cfc9151dac844e9a337) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [role](#afa0310f818002d7c1ac048f0db8c7f1c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rtt\_type](#ae0234031d94e93653dd45e6e657c199f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cs\_sync\_phy](#af42701651bca5fe0353ae1de9c453f47) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cs\_sync\_antenna\_selection](#aef335dd7738634cb8f81c18e0350141e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent\_len](#a8ad67a5a0138f32cc5295074011a3808) [3] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [subevent\_interval](#ad52cd2862d2544448a5e175c58541f89) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_num\_subevents](#a1c105f7a4d48754322fee6992db8c175) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [transmit\_power\_level](#adf2f24dc6988f1f0e0457a6cf3141521) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip1\_time](#a0675dfbb050838d98f21cfa28af8615b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_ip2\_time](#a7538e91b5ced2702965a21f8e754ebcc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_fcs\_time](#aa3d510663e5dcc44b5acd9d1c41746d5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_pm\_time](#a981da50e0594b8bc05f811e5170b10f5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [t\_sw\_time](#a09c40ecd0d4e325e0c0504a9d8cd977b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tone\_antenna\_config\_selection](#acaa428a37e68ff56c311397e53f46526) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [reserved](#a9021c55f8cddb741fb1f86317625723e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snr\_control\_initiator](#a551c06e651180867dd1d23b3fdf4c031) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [snr\_control\_reflector](#a3c949d9a7eb4f56427f6e9f8be7cb77b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [drbg\_nonce](#aee8c125df0f7136a0ecdb9f04903aaef) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_map\_repetition](#a8c23c2e6e8c38bf33fcd6d1e343f5982) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [override\_config](#acc2d0768b69e5f5b593e5aff71b17f20) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [override\_parameters\_length](#a373372a93d94e70d674c1c7b4c126734) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [override\_parameters\_data](#a15a68fe7c98b2e242afd6eb67dd9b40a) [] |

## Field Documentation

## [◆ ](#a8c23c2e6e8c38bf33fcd6d1e343f5982)channel\_map\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::channel\_map\_repetition |
| --- |

## [◆ ](#aef335dd7738634cb8f81c18e0350141e)cs\_sync\_antenna\_selection

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::cs\_sync\_antenna\_selection |
| --- |

## [◆ ](#af42701651bca5fe0353ae1de9c453f47)cs\_sync\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::cs\_sync\_phy |
| --- |

## [◆ ](#aee8c125df0f7136a0ecdb9f04903aaef)drbg\_nonce

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_op\_le\_cs\_test::drbg\_nonce |
| --- |

## [◆ ](#a60cc9a7c46f8cd0933dc2f5a68cca627)main\_mode\_repetition

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::main\_mode\_repetition |
| --- |

## [◆ ](#af4cdfd8c8cab500277c06a82ac088577)main\_mode\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::main\_mode\_type |
| --- |

## [◆ ](#a1c105f7a4d48754322fee6992db8c175)max\_num\_subevents

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::max\_num\_subevents |
| --- |

## [◆ ](#aaf480890608b5cfc9151dac844e9a337)mode\_0\_steps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::mode\_0\_steps |
| --- |

## [◆ ](#acc2d0768b69e5f5b593e5aff71b17f20)override\_config

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_op\_le\_cs\_test::override\_config |
| --- |

## [◆ ](#a15a68fe7c98b2e242afd6eb67dd9b40a)override\_parameters\_data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::override\_parameters\_data[] |
| --- |

## [◆ ](#a373372a93d94e70d674c1c7b4c126734)override\_parameters\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::override\_parameters\_length |
| --- |

## [◆ ](#a9021c55f8cddb741fb1f86317625723e)reserved

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::reserved |
| --- |

## [◆ ](#afa0310f818002d7c1ac048f0db8c7f1c)role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::role |
| --- |

## [◆ ](#ae0234031d94e93653dd45e6e657c199f)rtt\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::rtt\_type |
| --- |

## [◆ ](#a551c06e651180867dd1d23b3fdf4c031)snr\_control\_initiator

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::snr\_control\_initiator |
| --- |

## [◆ ](#a3c949d9a7eb4f56427f6e9f8be7cb77b)snr\_control\_reflector

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::snr\_control\_reflector |
| --- |

## [◆ ](#a090c5d03cf829011196d644cd9f7c7db)sub\_mode\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::sub\_mode\_type |
| --- |

## [◆ ](#ad52cd2862d2544448a5e175c58541f89)subevent\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_op\_le\_cs\_test::subevent\_interval |
| --- |

## [◆ ](#a8ad67a5a0138f32cc5295074011a3808)subevent\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::subevent\_len[3] |
| --- |

## [◆ ](#aa3d510663e5dcc44b5acd9d1c41746d5)t\_fcs\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::t\_fcs\_time |
| --- |

## [◆ ](#a0675dfbb050838d98f21cfa28af8615b)t\_ip1\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::t\_ip1\_time |
| --- |

## [◆ ](#a7538e91b5ced2702965a21f8e754ebcc)t\_ip2\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::t\_ip2\_time |
| --- |

## [◆ ](#a981da50e0594b8bc05f811e5170b10f5)t\_pm\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::t\_pm\_time |
| --- |

## [◆ ](#a09c40ecd0d4e325e0c0504a9d8cd977b)t\_sw\_time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::t\_sw\_time |
| --- |

## [◆ ](#acaa428a37e68ff56c311397e53f46526)tone\_antenna\_config\_selection

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::tone\_antenna\_config\_selection |
| --- |

## [◆ ](#adf2f24dc6988f1f0e0457a6cf3141521)transmit\_power\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_op\_le\_cs\_test::transmit\_power\_level |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_op\_le\_cs\_test](structbt__hci__op__le__cs__test.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
