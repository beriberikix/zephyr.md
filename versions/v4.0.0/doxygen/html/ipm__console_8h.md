---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ipm__console_8h.html
original_path: doxygen/html/ipm__console_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipm\_console.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`

[Go to the source code of this file.](ipm__console_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ipm\_console\_receiver\_config\_info](structipm__console__receiver__config__info.md) |
| struct | [ipm\_console\_receiver\_runtime\_data](structipm__console__receiver__runtime__data.md) |
| struct | [ipm\_console\_sender\_config\_info](structipm__console__sender__config__info.md) |

| Macros | |
| --- | --- |
| #define | [IPM\_CONSOLE\_STDOUT](#accdeb68d3bf39e9fe88ddc13defe8807)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
| #define | [IPM\_CONSOLE\_PRINTK](#ac0d474a4aa232f26194bd897a4611ed7)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)) |
| #define | [IPM\_CONSOLE\_STACK\_SIZE](#a4280a85493aa4df9b591cc3d98c1d4af)   CONFIG\_IPM\_CONSOLE\_STACK\_SIZE |
| #define | [IPM\_CONSOLE\_PRI](#a4d4cc0be8ad727fc09a5d9c694f06a71)   2 |

## Macro Definition Documentation

## [◆ ](#a4d4cc0be8ad727fc09a5d9c694f06a71)IPM\_CONSOLE\_PRI

| #define IPM\_CONSOLE\_PRI   2 |
| --- |

## [◆ ](#ac0d474a4aa232f26194bd897a4611ed7)IPM\_CONSOLE\_PRINTK

| #define IPM\_CONSOLE\_PRINTK   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1)) |
| --- |

## [◆ ](#a4280a85493aa4df9b591cc3d98c1d4af)IPM\_CONSOLE\_STACK\_SIZE

| #define IPM\_CONSOLE\_STACK\_SIZE   CONFIG\_IPM\_CONSOLE\_STACK\_SIZE |
| --- |

## [◆ ](#accdeb68d3bf39e9fe88ddc13defe8807)IPM\_CONSOLE\_STDOUT

| #define IPM\_CONSOLE\_STDOUT   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [ipm\_console.h](ipm__console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
