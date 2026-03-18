---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsd__cid.html
original_path: doxygen/html/structsd__cid.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_cid Struct Reference

SD card identification register.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [manufacturer](#a7d97bc0f58c766abd2501d923e163d40) |
|  | Manufacturer ID [127:120]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [application](#a11ec5fa23ae13ee084c093b27c1d381a) |
|  | OEM/Application ID [119:104]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [name](#a46f36abc3c2b1f3e9aa34c199d2bfcf3) [5] |
|  | Product name [103:64]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [version](#aba79f6a5bdf963772ac3c77ac209faf2) |
|  | Product revision [63:56]. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ser\_num](#ace04f0f28cb7e058e69fbbc643f66052) |
|  | Product serial number [55:24]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [date](#a50fbbc6844a1fde29a25a803ed9d0df7) |
|  | Manufacturing date [19:8]. |

## Detailed Description

SD card identification register.

Layout of SD card identification register

## Field Documentation

## [◆ ](#a11ec5fa23ae13ee084c093b27c1d381a)application

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_cid::application |
| --- |

OEM/Application ID [119:104].

## [◆ ](#a50fbbc6844a1fde29a25a803ed9d0df7)date

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_cid::date |
| --- |

Manufacturing date [19:8].

## [◆ ](#a7d97bc0f58c766abd2501d923e163d40)manufacturer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_cid::manufacturer |
| --- |

Manufacturer ID [127:120].

## [◆ ](#a46f36abc3c2b1f3e9aa34c199d2bfcf3)name

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_cid::name[5] |
| --- |

Product name [103:64].

## [◆ ](#ace04f0f28cb7e058e69fbbc643f66052)ser\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_cid::ser\_num |
| --- |

Product serial number [55:24].

## [◆ ](#aba79f6a5bdf963772ac3c77ac209faf2)version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_cid::version |
| --- |

Product revision [63:56].

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [sd\_cid](structsd__cid.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
