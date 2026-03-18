---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__ccc__getcaps.html
original_path: doxygen/html/structi3c__ccc__getcaps.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_getcaps Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for GETCAPS CCC (Get Optional Feature Capabilities).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [getcaps](#ab16e2b0e084371a9cbf57abf518f3e7e) [4] |
|  | GETCAP[1-4] bytes. |

## Detailed Description

Payload for GETCAPS CCC (Get Optional Feature Capabilities).

Note
:   Only support GETCAPS Format 1.

## Field Documentation

## [◆ ](#ab16e2b0e084371a9cbf57abf518f3e7e)getcaps

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getcaps::getcaps[4] |
| --- |

GETCAP[1-4] bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_getcaps](structi3c__ccc__getcaps.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
