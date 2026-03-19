---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__MPSC__PBUF__FLAGS.html
original_path: doxygen/html/group__MPSC__PBUF__FLAGS.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MPSC packet buffer flags

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [MPSC (Multi producer, single consumer) packet buffer API](group__mpsc__buf.md)

| Macros | |
| --- | --- |
| #define | [MPSC\_PBUF\_SIZE\_POW2](#ga6bed4eecb4eca06fb86a70c09505ccb8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag indicating that buffer size is power of 2. |
| #define | [MPSC\_PBUF\_MODE\_OVERWRITE](#ga983332f7aff31ed7b7e62cacf7960497)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Flag indicating buffer full policy. |
| #define | [MPSC\_PBUF\_MAX\_UTILIZATION](#gad0f57dbcecbb51a6b5b916c31a8eaab2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Flag indicating that maximum buffer usage is tracked. |
| #define | [MPSC\_PBUF\_FULL](#ga71a287b22771128b80c23d9263677498)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Flag indicated that buffer is currently full. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga71a287b22771128b80c23d9263677498)MPSC\_PBUF\_FULL

| #define MPSC\_PBUF\_FULL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Flag indicated that buffer is currently full.

## [◆ ](#gad0f57dbcecbb51a6b5b916c31a8eaab2)MPSC\_PBUF\_MAX\_UTILIZATION

| #define MPSC\_PBUF\_MAX\_UTILIZATION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Flag indicating that maximum buffer usage is tracked.

## [◆ ](#ga983332f7aff31ed7b7e62cacf7960497)MPSC\_PBUF\_MODE\_OVERWRITE

| #define MPSC\_PBUF\_MODE\_OVERWRITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Flag indicating buffer full policy.

If flag is set then when allocating from a full buffer oldest packets are dropped. When flag is not set then allocation returns null.

## [◆ ](#ga6bed4eecb4eca06fb86a70c09505ccb8)MPSC\_PBUF\_SIZE\_POW2

| #define MPSC\_PBUF\_SIZE\_POW2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mpsc_pbuf.h](mpsc__pbuf_8h.md)>`

Flag indicating that buffer size is power of 2.

When buffer size is power of 2 then optimizations are applied.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
