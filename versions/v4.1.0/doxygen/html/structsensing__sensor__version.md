---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensing__sensor__version.html
original_path: doxygen/html/structsensing__sensor__version.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_version Struct Reference

[Sensing](group__sensing.md) » [Sensing Subsystem API](group__sensing__api.md)

Sensor Version.
[More...](#details)

`#include <[sensing.h](sensing_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [value](#a0023cbb5114f4a3d3a1cf388e5034cfc) |  |
|  | The version represented as a 32-bit value. [More...](#a0023cbb5114f4a3d3a1cf388e5034cfc) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [major](#ad7275123dd08f06ee0307325c8f5fb37) |  |
|  | The major version number. [More...](#ad7275123dd08f06ee0307325c8f5fb37) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [minor](#a8d41ea3c181c7062aa8f76b17c652b41) |  |
|  | The minor version number. [More...](#a8d41ea3c181c7062aa8f76b17c652b41) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [hotfix](#a10fe885cd0cd9a6a5209308e188def3d) |  |
|  | The hotfix version number. [More...](#a10fe885cd0cd9a6a5209308e188def3d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [build](#a668f5d23171c38e1cc13a4221e639815) |  |
|  | The build version number. [More...](#a668f5d23171c38e1cc13a4221e639815) |
| } |  |
| }; |  |

## Detailed Description

Sensor Version.

## Field Documentation

## [◆ ](#a1c51022dff29bcc4fbc4b984ab72a48b)[union]

| union { ... } [sensing\_sensor\_version](structsensing__sensor__version.md) |
| --- |

## [◆ ](#a668f5d23171c38e1cc13a4221e639815)build

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor\_version::build |
| --- |

The build version number.

## [◆ ](#a10fe885cd0cd9a6a5209308e188def3d)hotfix

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor\_version::hotfix |
| --- |

The hotfix version number.

## [◆ ](#ad7275123dd08f06ee0307325c8f5fb37)major

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor\_version::major |
| --- |

The major version number.

## [◆ ](#a8d41ea3c181c7062aa8f76b17c652b41)minor

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor\_version::minor |
| --- |

The minor version number.

## [◆ ](#a0023cbb5114f4a3d3a1cf388e5034cfc)value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_version::value |
| --- |

The version represented as a 32-bit value.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing.h](sensing_8h_source.md)

- [sensing\_sensor\_version](structsensing__sensor__version.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
