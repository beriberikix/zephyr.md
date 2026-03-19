---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structretained__mem__driver__api.html
original_path: doxygen/html/structretained__mem__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

retained\_mem\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Retained memory driver interface](group__retained__mem__interface.md)

Retained memory driver API API which can be used by a device to store data in a retained memory area.
[More...](#details)

`#include <[retained_mem.h](retained__mem_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06) | [size](#a3743bda91f8700d9ae9cd06fd6780619) |
| [retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58) | [read](#ab68d1cdb15b79ac8d728a94305862c00) |
| [retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909) | [write](#abb3941c6c6465dfbc9a5f97163937526) |
| [retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d) | [clear](#ab0633d684826efcc6ace2f3d9427b406) |

## Detailed Description

Retained memory driver API API which can be used by a device to store data in a retained memory area.

Retained memory is memory that is retained while the device is powered but is lost when power to the device is lost (note that low power modes in some devices may clear the data also). This may be in a non-initialised RAM region, or in specific registers, but is not reset when a different application begins execution or the device is rebooted (without power loss). It must support byte-level reading and writing without a need to erase data before writing.

Note that drivers must implement all functions, none of the functions are optional.

## Field Documentation

## [◆ ](#ab0633d684826efcc6ace2f3d9427b406)clear

| [retained\_mem\_clear\_api](group__retained__mem__interface.md#ga3fde220eceb8a45a7a42cfbb1930e27d) retained\_mem\_driver\_api::clear |
| --- |

## [◆ ](#ab68d1cdb15b79ac8d728a94305862c00)read

| [retained\_mem\_read\_api](group__retained__mem__interface.md#ga3831f3ec0e0de7957cc6ce7da0cfbe58) retained\_mem\_driver\_api::read |
| --- |

## [◆ ](#a3743bda91f8700d9ae9cd06fd6780619)size

| [retained\_mem\_size\_api](group__retained__mem__interface.md#ga684490184eedc8d3f56b25d7b6e50a06) retained\_mem\_driver\_api::size |
| --- |

## [◆ ](#abb3941c6c6465dfbc9a5f97163937526)write

| [retained\_mem\_write\_api](group__retained__mem__interface.md#gaf6e43d230b1a606e90f3a236aeff1909) retained\_mem\_driver\_api::write |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[retained\_mem.h](retained__mem_8h_source.md)

- [retained\_mem\_driver\_api](structretained__mem__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
