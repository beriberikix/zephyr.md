---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__evt__le__ext__advertising__info.html
original_path: doxygen/html/structbt__hci__evt__le__ext__advertising__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_evt\_le\_ext\_advertising\_info Struct Reference

`#include <[hci_types.h](hci__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [evt\_type](#a040c27dbcb337162f7ca857b8cb84cfe) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [addr](#acec6858e41ae1b44a2a2ee6d6dbc294d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prim\_phy](#a088f0e6ea0dfbad25d5f72d0741f7d6d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sec\_phy](#af4d863e12e6f8f19426a14af292fa6d2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sid](#a5b4d4adff4d97c06311a76abd9847727) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a39217e77e495e8c4c6288917f8e4d2dc) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [rssi](#a6213edbc3ae30f02a6bf2d8e069cd035) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a7da4e49c49eccbf009491bb7da01e111) |
| [bt\_addr\_le\_t](structbt__addr__le__t.md) | [direct\_addr](#a37f4e4981566b43d6e7c7dfffc5b13fb) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [length](#a20ca10813f6b3aaba2756a5fe00d3878) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a9e5536277b0132c8374147677a787b68) [0] |

## Field Documentation

## [◆ ](#acec6858e41ae1b44a2a2ee6d6dbc294d)addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_ext\_advertising\_info::addr |
| --- |

## [◆ ](#a9e5536277b0132c8374147677a787b68)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_ext\_advertising\_info::data[0] |
| --- |

## [◆ ](#a37f4e4981566b43d6e7c7dfffc5b13fb)direct\_addr

| [bt\_addr\_le\_t](structbt__addr__le__t.md) bt\_hci\_evt\_le\_ext\_advertising\_info::direct\_addr |
| --- |

## [◆ ](#a040c27dbcb337162f7ca857b8cb84cfe)evt\_type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_ext\_advertising\_info::evt\_type |
| --- |

## [◆ ](#a7da4e49c49eccbf009491bb7da01e111)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_evt\_le\_ext\_advertising\_info::interval |
| --- |

## [◆ ](#a20ca10813f6b3aaba2756a5fe00d3878)length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_ext\_advertising\_info::length |
| --- |

## [◆ ](#a088f0e6ea0dfbad25d5f72d0741f7d6d)prim\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_ext\_advertising\_info::prim\_phy |
| --- |

## [◆ ](#a6213edbc3ae30f02a6bf2d8e069cd035)rssi

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_evt\_le\_ext\_advertising\_info::rssi |
| --- |

## [◆ ](#af4d863e12e6f8f19426a14af292fa6d2)sec\_phy

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_ext\_advertising\_info::sec\_phy |
| --- |

## [◆ ](#a5b4d4adff4d97c06311a76abd9847727)sid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_evt\_le\_ext\_advertising\_info::sid |
| --- |

## [◆ ](#a39217e77e495e8c4c6288917f8e4d2dc)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_evt\_le\_ext\_advertising\_info::tx\_power |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_types.h](hci__types_8h_source.md)

- [bt\_hci\_evt\_le\_ext\_advertising\_info](structbt__hci__evt__le__ext__advertising__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
