---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__le__cs__set__procedure__parameters__param.html
original_path: doxygen/html/structbt__le__cs__set__procedure__parameters__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_cs\_set\_procedure\_parameters\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Channel Sounding (CS)](group__bt__le__cs.md)

`#include <[cs.h](cs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [config\_id](#a03e8b91ccc78b02faed1864e6b4ad885) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_len](#a9b28e4b6f887201ca7f2188b07d37e4c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_procedure\_interval](#a967adc0e39da8e3ff96b998f3807542e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_interval](#ac48eb6d0021c676738f17437fdcbc3e8) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_procedure\_count](#a7a00113e7849b604efc38d904fce0389) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [min\_subevent\_len](#ab45195cbf8021c861384ead2cedae8da) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_subevent\_len](#a0166c72225d70e7c1afc9cf9be613835) |
| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) | [tone\_antenna\_config\_selection](#a3f7c838bcfb9c0e3d7ad803aefdc33c4) |
| enum [bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4) | [phy](#a7f42131c93874c0be297752d8103b585) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power\_delta](#abb995a318cf74ff7cbd8882ddfb155cc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [preferred\_peer\_antenna](#aa1158161ee5e49217ad6a85b6c92d993) |
| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) | [snr\_control\_initiator](#a2fb81c447beb1238cb88610589458816) |
| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) | [snr\_control\_reflector](#ab053facc218a6566a31e33d0831d385f) |

## Field Documentation

## [◆ ](#a03e8b91ccc78b02faed1864e6b4ad885)config\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_set\_procedure\_parameters\_param::config\_id |
| --- |

## [◆ ](#a7a00113e7849b604efc38d904fce0389)max\_procedure\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_count |
| --- |

## [◆ ](#ac48eb6d0021c676738f17437fdcbc3e8)max\_procedure\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_interval |
| --- |

## [◆ ](#a9b28e4b6f887201ca7f2188b07d37e4c)max\_procedure\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_set\_procedure\_parameters\_param::max\_procedure\_len |
| --- |

## [◆ ](#a0166c72225d70e7c1afc9cf9be613835)max\_subevent\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_cs\_set\_procedure\_parameters\_param::max\_subevent\_len |
| --- |

## [◆ ](#a967adc0e39da8e3ff96b998f3807542e)min\_procedure\_interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_cs\_set\_procedure\_parameters\_param::min\_procedure\_interval |
| --- |

## [◆ ](#ab45195cbf8021c861384ead2cedae8da)min\_subevent\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_le\_cs\_set\_procedure\_parameters\_param::min\_subevent\_len |
| --- |

## [◆ ](#a7f42131c93874c0be297752d8103b585)phy

| enum [bt\_le\_cs\_procedure\_phy](group__bt__le__cs.md#ga9e008daa9c0c1702aa3b4479e7a37ca4) bt\_le\_cs\_set\_procedure\_parameters\_param::phy |
| --- |

## [◆ ](#aa1158161ee5e49217ad6a85b6c92d993)preferred\_peer\_antenna

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_cs\_set\_procedure\_parameters\_param::preferred\_peer\_antenna |
| --- |

## [◆ ](#a2fb81c447beb1238cb88610589458816)snr\_control\_initiator

| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) bt\_le\_cs\_set\_procedure\_parameters\_param::snr\_control\_initiator |
| --- |

## [◆ ](#ab053facc218a6566a31e33d0831d385f)snr\_control\_reflector

| enum [bt\_le\_cs\_snr\_control](group__bt__le__cs.md#gaf34c59887e8a6da0560b6428733fe8d0) bt\_le\_cs\_set\_procedure\_parameters\_param::snr\_control\_reflector |
| --- |

## [◆ ](#a3f7c838bcfb9c0e3d7ad803aefdc33c4)tone\_antenna\_config\_selection

| enum [bt\_conn\_le\_cs\_tone\_antenna\_config\_selection](group__bt__conn.md#gab7acdbdf273fc760799cf0d8cf71591c) bt\_le\_cs\_set\_procedure\_parameters\_param::tone\_antenna\_config\_selection |
| --- |

## [◆ ](#abb995a318cf74ff7cbd8882ddfb155cc)tx\_power\_delta

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_le\_cs\_set\_procedure\_parameters\_param::tx\_power\_delta |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[cs.h](cs_8h_source.md)

- [bt\_le\_cs\_set\_procedure\_parameters\_param](structbt__le__cs__set__procedure__parameters__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
