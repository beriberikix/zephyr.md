---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structaddress__trans__params.html
original_path: doxygen/html/structaddress__trans__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

address\_trans\_params Struct Reference

Parameters for address\_trans\_init.
[More...](#details)

`#include <[rat.h](rat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_regions](#a1ea9c3785d02e9f5124786c3da7dc4e7) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rat\_base\_addr](#a9bcd9e881f8acff531f100ad06ab8e2d) |
| struct [address\_trans\_region\_config](structaddress__trans__region__config.md) \* | [region\_config](#a28afbd17772097ab9aabcbc654e364e0) |

## Detailed Description

Parameters for address\_trans\_init.

## Field Documentation

## [◆ ](#a1ea9c3785d02e9f5124786c3da7dc4e7)num\_regions

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address\_trans\_params::num\_regions |
| --- |

## [◆ ](#a9bcd9e881f8acff531f100ad06ab8e2d)rat\_base\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address\_trans\_params::rat\_base\_addr |
| --- |

## [◆ ](#a28afbd17772097ab9aabcbc654e364e0)region\_config

| struct [address\_trans\_region\_config](structaddress__trans__region__config.md)\* address\_trans\_params::region\_config |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mm/[rat.h](rat_8h_source.md)

- [address\_trans\_params](structaddress__trans__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
