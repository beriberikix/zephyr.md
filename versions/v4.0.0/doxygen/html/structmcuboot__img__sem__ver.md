---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmcuboot__img__sem__ver.html
original_path: doxygen/html/structmcuboot__img__sem__ver.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcuboot\_img\_sem\_ver Struct Reference

[Third-party](group__third__party.md) » [MCUboot image control API](group__mcuboot__api.md)

MCUboot image header representation for image version.
[More...](#details)

`#include <[mcuboot.h](mcuboot_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [major](#ae6fa8e6cc51e57e24a2d99670e543998) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [minor](#a3ab711b800ab894e201d175b491a9552) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [revision](#aabecc9fffb8ec7a7f02f2894f8d6e0f0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [build\_num](#abf2e489560daefaa0c5d33e9c7535dab) |

## Detailed Description

MCUboot image header representation for image version.

The header for an MCUboot firmware image contains an embedded version number, in semantic versioning format. This structure represents the information it contains.

## Field Documentation

## [◆ ](#abf2e489560daefaa0c5d33e9c7535dab)build\_num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mcuboot\_img\_sem\_ver::build\_num |
| --- |

## [◆ ](#ae6fa8e6cc51e57e24a2d99670e543998)major

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mcuboot\_img\_sem\_ver::major |
| --- |

## [◆ ](#a3ab711b800ab894e201d175b491a9552)minor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mcuboot\_img\_sem\_ver::minor |
| --- |

## [◆ ](#aabecc9fffb8ec7a7f02f2894f8d6e0f0)revision

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mcuboot\_img\_sem\_ver::revision |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/dfu/[mcuboot.h](mcuboot_8h_source.md)

- [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
