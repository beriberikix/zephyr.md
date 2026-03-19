---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsis__rtos__thread__cb.html
original_path: doxygen/html/structcmsis__rtos__thread__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_rtos\_thread\_cb Struct Reference

Control block for a CMSIS-RTOSv2 thread.
[More...](#details)

`#include <[cmsis_types.h](cmsis__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#a4105af0bf74ca757ded20f1cf8d8a32b) |
| struct [k\_poll\_signal](structk__poll__signal.md) | [poll\_signal](#a1141cf4f98f7942e4b303673ef0c2bb0) |
| struct [k\_poll\_event](structk__poll__event.md) | [poll\_event](#a536f754d15b6bc836de9d469ab5cb23a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [signal\_results](#af3061152f322434776156246c08651dc) |
| char | [name](#ac97e3f4f2aa71804a578392f154fc942) [16] |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [attr\_bits](#aa1aabdd8a7d59b0939e9c3822af26700) |
| struct k\_sem | [join\_guard](#ac07201f80219ef4e8d6bb4244de7d82f) |
| char | [has\_joined](#a39207f4007b39e9295507e63b1194c04) |

## Detailed Description

Control block for a CMSIS-RTOSv2 thread.

Application can use manual user-defined allocation for RTOS objects by supplying a pointer to thread control block. Control block is initiazed within osThreadNew().

## Field Documentation

## [◆ ](#aa1aabdd8a7d59b0939e9c3822af26700)attr\_bits

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cmsis\_rtos\_thread\_cb::attr\_bits |
| --- |

## [◆ ](#a39207f4007b39e9295507e63b1194c04)has\_joined

| char cmsis\_rtos\_thread\_cb::has\_joined |
| --- |

## [◆ ](#ac07201f80219ef4e8d6bb4244de7d82f)join\_guard

| struct k\_sem cmsis\_rtos\_thread\_cb::join\_guard |
| --- |

## [◆ ](#ac97e3f4f2aa71804a578392f154fc942)name

| char cmsis\_rtos\_thread\_cb::name[16] |
| --- |

## [◆ ](#a4105af0bf74ca757ded20f1cf8d8a32b)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) cmsis\_rtos\_thread\_cb::node |
| --- |

## [◆ ](#a536f754d15b6bc836de9d469ab5cb23a)poll\_event

| struct [k\_poll\_event](structk__poll__event.md) cmsis\_rtos\_thread\_cb::poll\_event |
| --- |

## [◆ ](#a1141cf4f98f7942e4b303673ef0c2bb0)poll\_signal

| struct [k\_poll\_signal](structk__poll__signal.md) cmsis\_rtos\_thread\_cb::poll\_signal |
| --- |

## [◆ ](#af3061152f322434776156246c08651dc)signal\_results

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cmsis\_rtos\_thread\_cb::signal\_results |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/portability/[cmsis\_types.h](cmsis__types_8h_source.md)

- [cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
