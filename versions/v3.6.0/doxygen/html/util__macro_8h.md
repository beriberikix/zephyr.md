---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/util__macro_8h.html
original_path: doxygen/html/util__macro_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

util\_macro.h File Reference

Macro utilities.
[More...](#details)

`#include <[zephyr/sys/util_internal.h](util__internal_8h_source.md)>`

[Go to the source code of this file.](util__macro_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(n) |
|  | Unsigned integer with bit position `n` set (signed in assembly language). |
| #define | [BIT64](group__sys-util.md#gacfdade52af3ced2d87472cec47d14a76)(\_n) |
|  | 64-bit unsigned integer with bit position `_n` set. |
| #define | [WRITE\_BIT](group__sys-util.md#ga23a900e882ecb48455e70f01fd45b246)(var, bit, set) |
|  | Set or clear a bit depending on a boolean value. |
| #define | [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(n) |
|  | Bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0. |
| #define | [BIT64\_MASK](group__sys-util.md#ga1a138896caafcb2429a6483ea7412d12)(n) |
|  | 64-bit bit mask with bits 0 through n-1 (inclusive) set, or 0 if `n` is 0. |
| #define | [IS\_POWER\_OF\_TWO](group__sys-util.md#ga52d277cbf33f76350b2fcb21c24640ee)(x) |
|  | Check if a `x` is a power of two. |
| #define | [IS\_SHIFTED\_BIT\_MASK](group__sys-util.md#ga406b5955c2803cdd9d9f19c90f242662)(m, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Check if bits are set continuously from the specified bit. |
| #define | [IS\_BIT\_MASK](group__sys-util.md#ga6d4b02e5da10bf93c4697dd6bf239ffd)(m) |
|  | Check if bits are set continuously from the LSB. |
| #define | [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(config\_macro) |
|  | Check for macro definition in compiler-visible expressions. |
| #define | [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\_flag, \_if\_1\_code, \_else\_code) |
|  | Insert code depending on whether `_flag` expands to 1 or not. |
| #define | [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)(\_flag, \_if\_0\_code, \_else\_code) |
|  | Like [COND\_CODE\_1()](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20 "Insert code depending on whether _flag expands to 1 or not.") except tests if `_flag` is 0. |
| #define | [IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(\_flag, \_code) |
|  | Insert code if `_flag` is defined and equals 1. |
| #define | [IF\_DISABLED](group__sys-util.md#gaa65e031f24a2c0fb4eae240e2c60b36a)(\_flag, \_code) |
|  | Insert code if `_flag` is not defined as 1. |
| #define | [IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(...) |
|  | Check if a macro has a replacement expression. |
| #define | [IS\_EQ](group__sys-util.md#gaa35a6894bca38a8ffb558c2c22a1eee1)(a, b) |
|  | Like a == b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(...) |
|  | Remove empty arguments from list. |
| #define | [EMPTY](group__sys-util.md#ga2b7cf2a3641be7b89138615764d60ba3) |
|  | Macro with an empty expansion. |
| #define | [IDENTITY](group__sys-util.md#gaaed493c6115c04272077a0f3854b9a83)(V) |
|  | Macro that expands to its argument. |
| #define | [GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(N, ...) |
|  | Get nth argument from argument list. |
| #define | [GET\_ARGS\_LESS\_N](group__sys-util.md#ga01e1dc9b92e5be6895528d1da5f0c88b)(N, ...) |
|  | Strips n first arguments from the argument list. |
| #define | [UTIL\_OR](group__sys-util.md#ga50cfdf948906976562c3f0625c84c2b2)(a, b) |
|  | Like a || b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [UTIL\_AND](group__sys-util.md#ga26179b776b4a03143e8be1612ef6d853)(a, b) |
|  | Like a && b, but does evaluation and short-circuiting at C preprocessor time. |
| #define | [UTIL\_INC](group__sys-util.md#ga90a54212306c3e210ac87fd0bd7b32da)(x) |
|  | [UTIL\_INC(x)](group__sys-util.md#ga90a54212306c3e210ac87fd0bd7b32da "UTIL_INC(x) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1.") for an integer literal x from 0 to 4095 expands to an integer literal whose value is x+1. |
| #define | [UTIL\_DEC](group__sys-util.md#gaa7623e1e33316024217094698e4d8258)(x) |
|  | [UTIL\_DEC(x)](group__sys-util.md#gaa7623e1e33316024217094698e4d8258 "UTIL_DEC(x) for an integer literal x from 0 to 4095 expands to an integer literal whose value is x-1.") for an integer literal x from 0 to 4095 expands to an integer literal whose value is x-1. |
| #define | [UTIL\_X2](group__sys-util.md#gab23deac75762adfb6bdde2c15d51f158)(y) |
|  | [UTIL\_X2(y)](group__sys-util.md#gab23deac75762adfb6bdde2c15d51f158 "UTIL_X2(y) for an integer literal y from 0 to 4095 expands to an integer literal whose value is 2y.") for an integer literal y from 0 to 4095 expands to an integer literal whose value is 2y. |
| #define | [LISTIFY](group__sys-util.md#ga81cbc0233cf73048d65b76f716653af6)(LEN, F, sep, ...) |
|  | Generates a sequence of code with configurable separator. |
| #define | [FOR\_EACH](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12)(F, sep, ...) |
|  | Call a macro `F` on each provided argument with a given separator between each call. |
| #define | [FOR\_EACH\_NONEMPTY\_TERM](group__sys-util.md#ga24b3862161d725f5503b1bb08f4e339f)(F, term, ...) |
|  | Like [FOR\_EACH()](group__sys-util.md#ga278c8b7cbbea2f585e371d3568f3cb12 "Call a macro F on each provided argument with a given separator between each call."), but with a terminator instead of a separator, and drops empty elements from the argument list. |
| #define | [FOR\_EACH\_IDX](group__sys-util.md#ga069f709e18eeafb8d276b5ff4fc09d31)(F, sep, ...) |
|  | Call macro `F` on each provided argument, with the argument's index as an additional parameter. |
| #define | [FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)(F, sep, fixed\_arg, ...) |
|  | Call macro `F` on each provided argument, with an additional fixed argument as a parameter. |
| #define | [FOR\_EACH\_IDX\_FIXED\_ARG](group__sys-util.md#ga2ab7377f5493123ffd29ebd1286457a9)(F, sep, fixed\_arg, ...) |
|  | Calls macro `F` for each variable argument with an index and fixed argument. |
| #define | [REVERSE\_ARGS](group__sys-util.md#ga58de032c2ed7b4094c447c512dfd3784)(...) |
|  | Reverse arguments order. |
| #define | [NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(...) |
|  | Number of arguments in the variable arguments list minus one. |
| #define | [MACRO\_MAP\_CAT](group__sys-util.md#gaf82371bd6bf317add5276fc6cbd66662)(...) |
|  | Mapping macro that pastes results together. |
| #define | [MACRO\_MAP\_CAT\_N](group__sys-util.md#ga58eba1f911e21da46b8beea264934d55)(N, ...) |
|  | Mapping macro that pastes a fixed number of results together. |

## Detailed Description

Macro utilities.

Macro utilities are the public interface for C/C++ code and device tree related implementation. In general, C/C++ will include <[sys/util.h](util_8h.md "Misc utilities.")> instead this file directly. For device tree implementation, this file should be include instead <[sys/util\_internal.h](util__internal_8h.md "Misc utilities.")>

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [util\_macro.h](util__macro_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
