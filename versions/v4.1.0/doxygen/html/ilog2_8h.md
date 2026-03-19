---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ilog2_8h.html
original_path: doxygen/html/ilog2_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ilog2.h File Reference

Provide [ilog2()](#a2696c6303d4c53b65a3a7f7ff771d5eb) function.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/arch/common/ffs.h](ffs_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](ilog2_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ilog2\_compile\_time\_const\_u32](#a5868c58205e07f1809d0521bf98798c7)(n) |
|  | Calculate the floor of log2 for compile time constant. |
| #define | [ilog2](#a2696c6303d4c53b65a3a7f7ff771d5eb)(n) |
|  | Calculate integer log2. |

## Detailed Description

Provide [ilog2()](#a2696c6303d4c53b65a3a7f7ff771d5eb) function.

## Macro Definition Documentation

## [◆ ](#a2696c6303d4c53b65a3a7f7ff771d5eb)ilog2

| #define ilog2 | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

( \

\_\_builtin\_constant\_p(n) ? \

ilog2\_compile\_time\_const\_u32(n) : \

[find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)(n) - 1 \

)

[find\_msb\_set](ffs_8h.md#a088db7d02e8f1fc559cbe1ec048494e8)

static ALWAYS\_INLINE unsigned int find\_msb\_set(uint32\_t op)

find most significant bit set in a 32-bit word

**Definition** ffs.h:31

Calculate integer log2.

This calculates the floor of log2 (integer of log2).

Warning
:   Will return 0 if input value is 0, which is invalid for log2.

Parameters
:   | n | Input value |
    | --- | --- |

Returns
:   Integer log2 of `n`

## [◆ ](#a5868c58205e07f1809d0521bf98798c7)ilog2\_compile\_time\_const\_u32

| #define ilog2\_compile\_time\_const\_u32 | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

( \

((n) < 2) ? 0 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31)) ? 31 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(30)) ? 30 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29)) ? 29 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28)) ? 28 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27)) ? 27 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26)) ? 26 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25)) ? 25 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24)) ? 24 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23)) ? 23 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22)) ? 22 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21)) ? 21 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20)) ? 20 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19)) ? 19 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18)) ? 18 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17)) ? 17 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16)) ? 16 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15)) ? 15 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14)) ? 14 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13)) ? 13 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12)) ? 12 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11)) ? 11 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10)) ? 10 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9)) ? 9 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8)) ? 8 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7)) ? 7 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6)) ? 6 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) ? 5 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4)) ? 4 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)) ? 3 : \

(((n) & [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) == [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2)) ? 2 : \

1 \

)

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Calculate the floor of log2 for compile time constant.

This calculates the floor of log2 (integer log2) for 32-bit unsigned integer.

Note
:   This should only be used for compile time constant when value is known during preprocessing stage. DO NOT USE for runtime code due to the big tree of nested if-else blocks.

Warning
:   Will return 0 if input value is 0, which is invalid for log2.

Parameters
:   | n | Input value |
    | --- | --- |

Returns
:   Integer log2 of

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [math](dir_76cc2d861a01f89f8d0ad119e28af149.md)
- [ilog2.h](ilog2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
