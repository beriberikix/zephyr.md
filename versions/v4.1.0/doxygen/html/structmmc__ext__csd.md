---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmmc__ext__csd.html
original_path: doxygen/html/structmmc__ext__csd.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mmc\_ext\_csd Struct Reference

MMC extended card specific data register.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sec\_count](#a44aa7d6d1282a00a1875e92fb5b3c4b8) |
|  | Sector Count [215:212]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bus\_width](#a63545477058cce0c5727637bcbb06a47) |
|  | Bus Width Mode [183]. |
| enum [mmc\_timing\_mode](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345) | [hs\_timing](#a25fe8f962635be3d40b449203e7d34a2) |
|  | High Speed Timing Mode [185]. |
| struct [mmc\_device\_type](structmmc__device__type.md) | [device\_type](#a4c26010052a69e060742e0a05b6ad98b) |
|  | Device Type [196]. |
| enum [mmc\_ext\_csd\_rev](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81) | [rev](#a3ee512cb3c0e3698d940c04eed3aa665) |
|  | Extended CSD Revision [192]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [power\_class](#a286b2783ac15dbec6fa3953f0cd69af4) |
|  | Selected power class [187]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mmc\_driver\_strengths](#a29a7f7502e6e6d93e76392b8ac45356f) |
|  | Driver strengths [197]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pwr\_class\_200MHZ\_VCCQ195](#acab002b3a28a3dc9bf58187e9e19a9fe) |
|  | Power class information for HS200 at VCC!=1.95V [237]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pwr\_class\_HS400](#a3a38f805cac18f3429f57edc7cbf2134) |
|  | Power class information for HS400 [253]. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cache\_size](#a3aafc3e2b5b59cb79535411178a35efe) |
|  | Size of eMMC cache [252:249]. |

## Detailed Description

MMC extended card specific data register.

Extended card specific data register. Contains additional additional data about MMC card.

## Field Documentation

## [◆ ](#a63545477058cce0c5727637bcbb06a47)bus\_width

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mmc\_ext\_csd::bus\_width |
| --- |

Bus Width Mode [183].

## [◆ ](#a3aafc3e2b5b59cb79535411178a35efe)cache\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mmc\_ext\_csd::cache\_size |
| --- |

Size of eMMC cache [252:249].

## [◆ ](#a4c26010052a69e060742e0a05b6ad98b)device\_type

| struct [mmc\_device\_type](structmmc__device__type.md) mmc\_ext\_csd::device\_type |
| --- |

Device Type [196].

## [◆ ](#a25fe8f962635be3d40b449203e7d34a2)hs\_timing

| enum [mmc\_timing\_mode](sd__spec_8h.md#ae1956c4b374e2c8b6a585596e93ac345) mmc\_ext\_csd::hs\_timing |
| --- |

High Speed Timing Mode [185].

## [◆ ](#a29a7f7502e6e6d93e76392b8ac45356f)mmc\_driver\_strengths

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mmc\_ext\_csd::mmc\_driver\_strengths |
| --- |

Driver strengths [197].

## [◆ ](#a286b2783ac15dbec6fa3953f0cd69af4)power\_class

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mmc\_ext\_csd::power\_class |
| --- |

Selected power class [187].

## [◆ ](#acab002b3a28a3dc9bf58187e9e19a9fe)pwr\_class\_200MHZ\_VCCQ195

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mmc\_ext\_csd::pwr\_class\_200MHZ\_VCCQ195 |
| --- |

Power class information for HS200 at VCC!=1.95V [237].

## [◆ ](#a3a38f805cac18f3429f57edc7cbf2134)pwr\_class\_HS400

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mmc\_ext\_csd::pwr\_class\_HS400 |
| --- |

Power class information for HS400 [253].

## [◆ ](#a3ee512cb3c0e3698d940c04eed3aa665)rev

| enum [mmc\_ext\_csd\_rev](sd__spec_8h.md#ac86d8a44f37c771cb666f69a516dff81) mmc\_ext\_csd::rev |
| --- |

Extended CSD Revision [192].

## [◆ ](#a44aa7d6d1282a00a1875e92fb5b3c4b8)sec\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mmc\_ext\_csd::sec\_count |
| --- |

Sector Count [215:212].

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [mmc\_ext\_csd](structmmc__ext__csd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
