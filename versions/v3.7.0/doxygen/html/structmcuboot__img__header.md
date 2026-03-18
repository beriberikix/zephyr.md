---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmcuboot__img__header.html
original_path: doxygen/html/structmcuboot__img__header.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcuboot\_img\_header Struct Reference

[Third-party](group__third__party.md) » [MCUboot image control API](group__mcuboot__api.md)

Model for the MCUBoot image header.
[More...](#details)

`#include <[mcuboot.h](mcuboot_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mcuboot\_version](#ab5147e9586062d4dd5b381af13f1e82d) |
|  | The version of MCUboot the header is built for. |
| union { |  |
| struct [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md)   [v1](#aff12aff412ea774f96948e7db0b25009) |  |
|  | Header information for MCUboot version 1. [More...](#aff12aff412ea774f96948e7db0b25009) |
| } | [h](#a34f5595bbd5b974c04386b568c88e39f) |
|  | The header information. |

## Detailed Description

Model for the MCUBoot image header.

This contains the decoded image header, along with the major version of MCUboot that the header was built for.

(The MCUboot project guarantees that incompatible changes to the image header will result in major version changes to the bootloader itself, and will be detectable in the persistent representation of the header.)

## Field Documentation

## [◆ ](#a34f5595bbd5b974c04386b568c88e39f)[union]

| union { ... } mcuboot\_img\_header::h |
| --- |

The header information.

It is only valid to access fields in the union member corresponding to the mcuboot\_version field above.

## [◆ ](#ab5147e9586062d4dd5b381af13f1e82d)mcuboot\_version

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mcuboot\_img\_header::mcuboot\_version |
| --- |

The version of MCUboot the header is built for.

The value 1 corresponds to MCUboot versions 1.x.y.

## [◆ ](#aff12aff412ea774f96948e7db0b25009)v1

| struct [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md) mcuboot\_img\_header::v1 |
| --- |

Header information for MCUboot version 1.

---

The documentation for this struct was generated from the following file:

- zephyr/dfu/[mcuboot.h](mcuboot_8h_source.md)

- [mcuboot\_img\_header](structmcuboot__img__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
