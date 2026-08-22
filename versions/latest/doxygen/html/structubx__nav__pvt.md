---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structubx__nav__pvt.html
original_path: doxygen/html/structubx__nav__pvt.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx\_nav\_pvt Struct Reference

`#include <[zephyr/modem/ubx/protocol.h](modem_2ubx_2protocol_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [itow](#a426086b12ff09fb8a00dd4623fea307e) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [year](#a84c6640806485f270b8d51d06cc49709) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [month](#ad90042dc5e00b91f004badcb0c3a5f4c) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [day](#aeadb05fe45a3a0539c899129e40059fd) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [hour](#aeb710663626935d21c77a5cfe1030795) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [minute](#a18b61263b433dc5f81c2becff9c6743c) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [second](#a10b14934d80d80d3c2f0c36866bd4a64) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [valid](#a450638fda7b9d1929145575e4c576ec1) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [tacc](#a1753595f0a3935449dee4d0c57e88a6e) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [nano](#a1c21c3b882412f36f96c59cda1d948d9) |  |
| } | [time](#ad63cfcbcefd262731920954bab9c6758) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fix\_type](#a3b780d7b790b07a8ee23431969cbc318) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a1bdc3cb0e4a2b6bef1c4216963e5c29c) |
|  | See [ubx\_nav\_fix\_type](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fef). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags2](#a2ff7d8bcc13ee956d9535c61efefada6) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [num\_sv](#aea613eb3d604d33120e82c569c5f10e9) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [longitude](#ae47fc34dfd91687590bd96afe2fab091) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [latitude](#a34ec5fc41c4b323b4719803f1ff01bed) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [height](#ab0df156e9f8009bebfbbdb39c63c4191) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [hmsl](#ae6ba97f3406b9fdbbf04c4bb3e744668) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [horiz\_acc](#acbb58f36eb572ce27b050a8c7540f91d) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [vert\_acc](#af5b3e0e70b3470bd1686ddbfefb419f9) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [vel\_north](#a1d50e696fa2684b55d04c652c85f2e16) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [vel\_east](#a17c628b0acca293f068b58eff32ae4dd) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [vel\_down](#a4958a6c11bd812477d11467ab3384161) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [ground\_speed](#a38a8612a53966a1d598bf6d17443da7d) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [head\_motion](#abd97f003ba43b70ffea2e9fdf5702c4f) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [speed\_acc](#a955d0f7927f68f540f2e9a2c91e46e79) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [head\_acc](#aa332fc93448eb6b30ad8bbaa5760db5c) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [pdop](#a7e5dc3449e52a36cb2bc5841bbf6fec8) |  |
|  | Heading accuracy estimate (both motion and vehicle). [More...](#a7e5dc3449e52a36cb2bc5841bbf6fec8) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [flags3](#a39b72f654fc8130c611ac839189914ed) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved](#a80139f6d95bf943f5c6de6af1ea50e3e) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [head\_vehicle](#a8fc4b24fb8ffde02d306bc1b6770b1d8) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [mag\_decl](#a4f63a0f15b823e5258fdb826d2636828) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [magacc](#ac0265c113f01ae2bab8553eb7148e3ae) |  |
| } | [nav](#aa8b31a49c2844501505412da226872e1) |

## Field Documentation

## [◆ ](#aeadb05fe45a3a0539c899129e40059fd)day

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::day |
| --- |

## [◆ ](#a3b780d7b790b07a8ee23431969cbc318)fix\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::fix\_type |
| --- |

## [◆ ](#a1bdc3cb0e4a2b6bef1c4216963e5c29c)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::flags |
| --- |

See [ubx\_nav\_fix\_type](modem_2ubx_2protocol_8h.md#a173b6c1016562da43b8131b8d8f04fef).

## [◆ ](#a2ff7d8bcc13ee956d9535c61efefada6)flags2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::flags2 |
| --- |

## [◆ ](#a39b72f654fc8130c611ac839189914ed)flags3

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_nav\_pvt::flags3 |
| --- |

## [◆ ](#a38a8612a53966a1d598bf6d17443da7d)ground\_speed

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::ground\_speed |
| --- |

## [◆ ](#aa332fc93448eb6b30ad8bbaa5760db5c)head\_acc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::head\_acc |
| --- |

## [◆ ](#abd97f003ba43b70ffea2e9fdf5702c4f)head\_motion

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::head\_motion |
| --- |

## [◆ ](#a8fc4b24fb8ffde02d306bc1b6770b1d8)head\_vehicle

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::head\_vehicle |
| --- |

## [◆ ](#ab0df156e9f8009bebfbbdb39c63c4191)height

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::height |
| --- |

## [◆ ](#ae6ba97f3406b9fdbbf04c4bb3e744668)hmsl

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::hmsl |
| --- |

## [◆ ](#acbb58f36eb572ce27b050a8c7540f91d)horiz\_acc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::horiz\_acc |
| --- |

## [◆ ](#aeb710663626935d21c77a5cfe1030795)hour

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::hour |
| --- |

## [◆ ](#a426086b12ff09fb8a00dd4623fea307e)itow

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::itow |
| --- |

## [◆ ](#a34ec5fc41c4b323b4719803f1ff01bed)latitude

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::latitude |
| --- |

## [◆ ](#ae47fc34dfd91687590bd96afe2fab091)longitude

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::longitude |
| --- |

## [◆ ](#a4f63a0f15b823e5258fdb826d2636828)mag\_decl

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) ubx\_nav\_pvt::mag\_decl |
| --- |

## [◆ ](#ac0265c113f01ae2bab8553eb7148e3ae)magacc

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_nav\_pvt::magacc |
| --- |

## [◆ ](#a18b61263b433dc5f81c2becff9c6743c)minute

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::minute |
| --- |

## [◆ ](#ad90042dc5e00b91f004badcb0c3a5f4c)month

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::month |
| --- |

## [◆ ](#a1c21c3b882412f36f96c59cda1d948d9)nano

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::nano |
| --- |

## [◆ ](#aa8b31a49c2844501505412da226872e1)[struct]

| struct { ... } ubx\_nav\_pvt::nav |
| --- |

## [◆ ](#aea613eb3d604d33120e82c569c5f10e9)num\_sv

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::num\_sv |
| --- |

## [◆ ](#a7e5dc3449e52a36cb2bc5841bbf6fec8)pdop

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_nav\_pvt::pdop |
| --- |

Heading accuracy estimate (both motion and vehicle).

Degrees. scaling: 1e-5.

## [◆ ](#a80139f6d95bf943f5c6de6af1ea50e3e)reserved

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::reserved |
| --- |

## [◆ ](#a10b14934d80d80d3c2f0c36866bd4a64)second

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::second |
| --- |

## [◆ ](#a955d0f7927f68f540f2e9a2c91e46e79)speed\_acc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::speed\_acc |
| --- |

## [◆ ](#a1753595f0a3935449dee4d0c57e88a6e)tacc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::tacc |
| --- |

## [◆ ](#ad63cfcbcefd262731920954bab9c6758)[struct]

| struct { ... } ubx\_nav\_pvt::time |
| --- |

## [◆ ](#a450638fda7b9d1929145575e4c576ec1)valid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_nav\_pvt::valid |
| --- |

## [◆ ](#a4958a6c11bd812477d11467ab3384161)vel\_down

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::vel\_down |
| --- |

## [◆ ](#a17c628b0acca293f068b58eff32ae4dd)vel\_east

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::vel\_east |
| --- |

## [◆ ](#a1d50e696fa2684b55d04c652c85f2e16)vel\_north

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ubx\_nav\_pvt::vel\_north |
| --- |

## [◆ ](#af5b3e0e70b3470bd1686ddbfefb419f9)vert\_acc

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ubx\_nav\_pvt::vert\_acc |
| --- |

## [◆ ](#a84c6640806485f270b8d51d06cc49709)year

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_nav\_pvt::year |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/ubx/[protocol.h](modem_2ubx_2protocol_8h_source.md)

- [ubx\_nav\_pvt](structubx__nav__pvt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
