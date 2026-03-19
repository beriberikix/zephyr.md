---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__pacs__register__param.html
original_path: doxygen/html/structbt__pacs__register__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_pacs\_register\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Published Audio Capabilities Service (PACS)](group__bt__pacs.md)

Structure for registering PACS.
[More...](#details)

`#include <[pacs.h](pacs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [snk\_pac](#a7b5d14b7206a593821af96343120edbb) |
|  | Enables or disables registration of Sink PAC Characteristic. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [snk\_loc](#a3eda569266531da60342f0a170c4d152) |
|  | Enables or disables registration of Sink Location Characteristic. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [src\_pac](#a922188bb4e989aabb6b4cbba43d457c8) |
|  | Enables or disables registration of Source PAC Characteristic. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [src\_loc](#af377b54efe30f22f4bfb1677964a1f00) |
|  | Enables or disables registration of Source Location Characteristic. |

## Detailed Description

Structure for registering PACS.

## Field Documentation

## [◆ ](#a3eda569266531da60342f0a170c4d152)snk\_loc

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_pacs\_register\_param::snk\_loc |
| --- |

Enables or disables registration of Sink Location Characteristic.

Registration of Sink Location is dependent on [bt\_pacs\_register\_param::snk\_pac](#a7b5d14b7206a593821af96343120edbb) also being set.

## [◆ ](#a7b5d14b7206a593821af96343120edbb)snk\_pac

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_pacs\_register\_param::snk\_pac |
| --- |

Enables or disables registration of Sink PAC Characteristic.

## [◆ ](#af377b54efe30f22f4bfb1677964a1f00)src\_loc

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_pacs\_register\_param::src\_loc |
| --- |

Enables or disables registration of Source Location Characteristic.

Registration of Source Location is dependent on [bt\_pacs\_register\_param::src\_pac](#a922188bb4e989aabb6b4cbba43d457c8) also being set.

## [◆ ](#a922188bb4e989aabb6b4cbba43d457c8)src\_pac

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_pacs\_register\_param::src\_pac |
| --- |

Enables or disables registration of Source PAC Characteristic.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[pacs.h](pacs_8h_source.md)

- [bt\_pacs\_register\_param](structbt__pacs__register__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
