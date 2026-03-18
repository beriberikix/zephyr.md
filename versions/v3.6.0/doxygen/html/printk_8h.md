---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/printk_8h.html
original_path: doxygen/html/printk_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

printk.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <stddef.h>`  
`#include <stdarg.h>`  
`#include <[inttypes.h](inttypes_8h_source.md)>`

[Go to the source code of this file.](printk_8h_source.md)

| Functions | |
| --- | --- |
| static void | [printk](#a768a7dff8592b69f327a08f96b00fa54) (const char \*fmt,...) |
|  | Print kernel debugging message. |
| static void | [vprintk](#a23609ef1acea586b44f71d32283fea23) (const char \*fmt, va\_list ap) |
| int | [snprintk](#a0b0af71688f7e9170103d771d4e1eab2) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*fmt,...) |
| int | [vsnprintk](#ae824cc3368607ee5d45f860a1389794a) (char \*str, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const char \*fmt, va\_list ap) |

## Function Documentation

## [◆ ](#a768a7dff8592b69f327a08f96b00fa54)printk()

| | void printk | ( | const char \* | *fmt*, | | --- | --- | --- | --- | |  |  |  | *...* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Print kernel debugging message.

This routine prints a kernel debugging message to the system console. Output is send immediately, without any mutual exclusion or buffering.

A basic set of conversion specifier characters are supported:

- signed decimal: %d, %i
- unsigned decimal: %u
- unsigned hexadecimal: %x (%X is treated as %x)
- pointer: %p
- string: %s
- character: %c
- percent: %%

Field width (with or without leading zeroes) is supported. Length attributes h, hh, l, ll and z are supported. However, integral values with lld and lli are only printed if they fit in a long otherwise 'ERR' is printed. Full 64-bit values may be printed with llx. Flags and precision attributes are not supported.

Parameters
:   | fmt | Format string. |
    | --- | --- |
    | ... | Optional list of format arguments. |

## [◆ ](#a0b0af71688f7e9170103d771d4e1eab2)snprintk()

| int snprintk | ( | char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const char \* | *fmt*, |
|  |  |  | *...* ) |

## [◆ ](#a23609ef1acea586b44f71d32283fea23)vprintk()

| | void vprintk | ( | const char \* | *fmt*, | | --- | --- | --- | --- | |  |  | va\_list | *ap* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae824cc3368607ee5d45f860a1389794a)vsnprintk()

| int vsnprintk | ( | char \* | *str*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | const char \* | *fmt*, |
|  |  | va\_list | *ap* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [printk.h](printk_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
