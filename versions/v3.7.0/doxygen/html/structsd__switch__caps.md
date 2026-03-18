---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsd__switch__caps.html
original_path: doxygen/html/structsd__switch__caps.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_switch\_caps Struct Reference

SD switch capabilities.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [hs\_max\_data\_rate](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c) | [hs\_max\_dtr](#a7465b3fe6bd1f317eeb3283a25da7278) |
| enum [uhs\_max\_data\_rate](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a) | [uhs\_max\_dtr](#ab09d80f61bc79857ee39604959c8a578) |
| enum [sd\_bus\_speed](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36) | [bus\_speed](#a29024de744d65fb3d8fe51c4d4424aee) |
| enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) | [sd\_drv\_type](#a7262e4be5e3f59d047e569e1c24f04b3) |
| enum [sd\_current\_limit](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537) | [sd\_current\_limit](#a4b531af598bea14c90b8973daf1422dc) |

## Detailed Description

SD switch capabilities.

records switch capabilities for SD card. These capabilities are set and queried via CMD6

## Field Documentation

## [◆ ](#a29024de744d65fb3d8fe51c4d4424aee)bus\_speed

| enum [sd\_bus\_speed](sd__spec_8h.md#a6b42b86d8f2ba4f29787c7c6f3d97f36) sd\_switch\_caps::bus\_speed |
| --- |

## [◆ ](#a7465b3fe6bd1f317eeb3283a25da7278)hs\_max\_dtr

| enum [hs\_max\_data\_rate](sd__spec_8h.md#a2093143614e52f69e173289391d7e91c) sd\_switch\_caps::hs\_max\_dtr |
| --- |

## [◆ ](#a4b531af598bea14c90b8973daf1422dc)sd\_current\_limit

| enum [sd\_current\_limit](sd__spec_8h.md#a238de48c0cb55d173b6b874f4930c537) sd\_switch\_caps::sd\_current\_limit |
| --- |

## [◆ ](#a7262e4be5e3f59d047e569e1c24f04b3)sd\_drv\_type

| enum [sd\_driver\_type](sd__spec_8h.md#a314c38b1b0603c003e67b5dec2228d4b) sd\_switch\_caps::sd\_drv\_type |
| --- |

## [◆ ](#ab09d80f61bc79857ee39604959c8a578)uhs\_max\_dtr

| enum [uhs\_max\_data\_rate](sd__spec_8h.md#a5466ef2e30578d03c61831aa09fd7b9a) sd\_switch\_caps::uhs\_max\_dtr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [sd\_switch\_caps](structsd__switch__caps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
