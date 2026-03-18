---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structlwm2m__time__series__elem.html
original_path: doxygen/html/structlwm2m__time__series__elem.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_time\_series\_elem Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

LwM2M Time series data structure.
[More...](#details)

`#include <[lwm2m.h](lwm2m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) | [t](#acd00227c551b6ee1960b3881819ef90b) |
|  | Cached data Unix timestamp. |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [u8](#abb0726f2ba23ab5f3229342d62f63e6b) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [u16](#ad0cd9f29ce0d7e99c1ae411bd89a29fa) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [u32](#a58b1e7f9eb00d58421aec63bfbc732ed) |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [u64](#ae432e592ddceb17113f25bef77308f1b) |  |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)   [i8](#ab895cd3addf57b8e59c8a1282588ee2d) |  |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)   [i16](#a37489f6edbcb125691bd02f28346c788) |  |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)   [i32](#a61f4d65dd7e6e2e6b215fdc800bba6e4) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [i64](#a2cccc464d029dc0f3f748b2a48f5cb50) |  |
| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7)   [time](#af25edfa95c28e43bb5abc60f3027ed9a) |  |
| double   [f](#a3f25d66fa0e7918326a522e76451d6ae) |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [b](#ae6b37f532055bdd6b5b39c909a6873e7) |  |
| }; |  |

## Detailed Description

LwM2M Time series data structure.

## Field Documentation

## [◆ ](#a270084824d5685f4e9552d4249218c0b)[union]

| union { ... } [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md) |
| --- |

## [◆ ](#ae6b37f532055bdd6b5b39c909a6873e7)b

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_time\_series\_elem::b |
| --- |

## [◆ ](#a3f25d66fa0e7918326a522e76451d6ae)f

| double lwm2m\_time\_series\_elem::f |
| --- |

## [◆ ](#a37489f6edbcb125691bd02f28346c788)i16

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) lwm2m\_time\_series\_elem::i16 |
| --- |

## [◆ ](#a61f4d65dd7e6e2e6b215fdc800bba6e4)i32

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) lwm2m\_time\_series\_elem::i32 |
| --- |

## [◆ ](#a2cccc464d029dc0f3f748b2a48f5cb50)i64

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) lwm2m\_time\_series\_elem::i64 |
| --- |

## [◆ ](#ab895cd3addf57b8e59c8a1282588ee2d)i8

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) lwm2m\_time\_series\_elem::i8 |
| --- |

## [◆ ](#acd00227c551b6ee1960b3881819ef90b)t

| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) lwm2m\_time\_series\_elem::t |
| --- |

Cached data Unix timestamp.

## [◆ ](#af25edfa95c28e43bb5abc60f3027ed9a)time

| [time\_t](__timespec_8h.md#aa17c461cd5eca7fc12a66daa803c7fd7) lwm2m\_time\_series\_elem::time |
| --- |

## [◆ ](#ad0cd9f29ce0d7e99c1ae411bd89a29fa)u16

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_time\_series\_elem::u16 |
| --- |

## [◆ ](#a58b1e7f9eb00d58421aec63bfbc732ed)u32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lwm2m\_time\_series\_elem::u32 |
| --- |

## [◆ ](#ae432e592ddceb17113f25bef77308f1b)u64

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) lwm2m\_time\_series\_elem::u64 |
| --- |

## [◆ ](#abb0726f2ba23ab5f3229342d62f63e6b)u8

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lwm2m\_time\_series\_elem::u8 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lwm2m.h](lwm2m_8h_source.md)

- [lwm2m\_time\_series\_elem](structlwm2m__time__series__elem.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
