---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdai__config.html
original_path: doxygen/html/structdai__config.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dai\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DAI Interface](group__dai__interface.md)

Main DAI config structure.
[More...](#details)

`#include <[dai.h](dai_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) | [type](#acfb621417b789c71608ad50d0b54c1f6) |
|  | Type of the DAI. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [dai\_index](#aecb9fe475d71d55d8b19eb3faa697606) |
|  | Index of the DAI. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channels](#ac3f39c351ad9659356ad5ad4306585b8) |
|  | Number of audio channels, words in frame. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rate](#a2d46087a3c94845d52b44386dd20cfc0) |
|  | Frame clock (WS) frequency, sampling rate. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [format](#ac2c2c4a39bfe917d5a784d8bc596eb10) |
|  | DAI specific data stream format. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [options](#ac8b2936e194421f95d03e1c595017306) |
|  | DAI specific configuration options. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [word\_size](#afe7ab1b6c1163ca1bf4141bc6f2439ba) |
|  | Number of bits representing one data word. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [block\_size](#af3c768d9597298cea94bbdd6e5b5c4f3) |
|  | Size of one RX/TX memory block (buffer) in bytes. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [link\_config](#afd3bcee428b5359b7151a269973049a1) |
|  | DAI specific link configuration. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tdm\_slot\_group](#a32830675c7bf7125c5006579d33e5e96) |

## Detailed Description

Main DAI config structure.

Generic DAI interface configuration options.

## Field Documentation

## [◆ ](#af3c768d9597298cea94bbdd6e5b5c4f3)block\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dai\_config::block\_size |
| --- |

Size of one RX/TX memory block (buffer) in bytes.

## [◆ ](#ac3f39c351ad9659356ad5ad4306585b8)channels

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dai\_config::channels |
| --- |

Number of audio channels, words in frame.

## [◆ ](#aecb9fe475d71d55d8b19eb3faa697606)dai\_index

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_config::dai\_index |
| --- |

Index of the DAI.

## [◆ ](#ac2c2c4a39bfe917d5a784d8bc596eb10)format

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dai\_config::format |
| --- |

DAI specific data stream format.

## [◆ ](#afd3bcee428b5359b7151a269973049a1)link\_config

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dai\_config::link\_config |
| --- |

DAI specific link configuration.

tdm slot group number

## [◆ ](#ac8b2936e194421f95d03e1c595017306)options

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dai\_config::options |
| --- |

DAI specific configuration options.

## [◆ ](#a2d46087a3c94845d52b44386dd20cfc0)rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_config::rate |
| --- |

Frame clock (WS) frequency, sampling rate.

## [◆ ](#a32830675c7bf7125c5006579d33e5e96)tdm\_slot\_group

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dai\_config::tdm\_slot\_group |
| --- |

## [◆ ](#acfb621417b789c71608ad50d0b54c1f6)type

| enum [dai\_type](group__dai__interface.md#gac95242d83a2c2b477fcb9eb3da420797) dai\_config::type |
| --- |

Type of the DAI.

## [◆ ](#afe7ab1b6c1163ca1bf4141bc6f2439ba)word\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dai\_config::word\_size |
| --- |

Number of bits representing one data word.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dai.h](dai_8h_source.md)

- [dai\_config](structdai__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
