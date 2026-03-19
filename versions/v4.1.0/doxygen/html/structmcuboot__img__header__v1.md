---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmcuboot__img__header__v1.html
original_path: doxygen/html/structmcuboot__img__header__v1.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcuboot\_img\_header\_v1 Struct Reference

[Third-party](group__third__party.md) » [MCUboot image control API](group__mcuboot__api.md)

Model for the MCUboot image header as of version 1.
[More...](#details)

`#include <[mcuboot.h](mcuboot_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [image\_size](#a83a042079d850f383eef7a46cad14fa4) |
|  | The size of the image, in bytes. |
| struct [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md) | [sem\_ver](#a01dd3b50bb00accf4108b08c01df4e2b) |
|  | The image version. |

## Detailed Description

Model for the MCUboot image header as of version 1.

This represents the data present in the image header, in version 1 of the header format.

Some information present in the header but not currently relevant to applications is omitted.

## Field Documentation

## [◆ ](#a83a042079d850f383eef7a46cad14fa4)image\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mcuboot\_img\_header\_v1::image\_size |
| --- |

The size of the image, in bytes.

## [◆ ](#a01dd3b50bb00accf4108b08c01df4e2b)sem\_ver

| struct [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md) mcuboot\_img\_header\_v1::sem\_ver |
| --- |

The image version.

---

The documentation for this struct was generated from the following file:

- zephyr/dfu/[mcuboot.h](mcuboot_8h_source.md)

- [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
