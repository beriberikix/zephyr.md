---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__SPSC__PBUF__FLAGS.html
original_path: doxygen/html/group__SPSC__PBUF__FLAGS.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SPSC packet buffer flags

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC (Single producer, single consumer) packet buffer API](group__spsc__buf.md)

| Macros | |
| --- | --- |
| #define | [SPSC\_PBUF\_CACHE](#ga97255180be37860a513d0a87b3dac573)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that cache shall be handled. |
| #define | [SPSC\_PBUF\_UTILIZATION\_BITS](#gaaaccc1ca6c802c2740b4af07ba1650b9)   24 |
|  | Size of the field which stores maximum utilization. |
| #define | [SPSC\_PBUF\_UTILIZATION\_OFFSET](#ga5c1783e202a62161b6f5b0f11fb62f8a)   8 |
|  | Offset of the field which stores maximum utilization. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga97255180be37860a513d0a87b3dac573)SPSC\_PBUF\_CACHE

| #define SPSC\_PBUF\_CACHE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Flag indicating that cache shall be handled.

## [◆ ](#gaaaccc1ca6c802c2740b4af07ba1650b9)SPSC\_PBUF\_UTILIZATION\_BITS

| #define SPSC\_PBUF\_UTILIZATION\_BITS   24 |
| --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Size of the field which stores maximum utilization.

## [◆ ](#ga5c1783e202a62161b6f5b0f11fb62f8a)SPSC\_PBUF\_UTILIZATION\_OFFSET

| #define SPSC\_PBUF\_UTILIZATION\_OFFSET   8 |
| --- |

`#include <[spsc_pbuf.h](spsc__pbuf_8h.md)>`

Offset of the field which stores maximum utilization.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
