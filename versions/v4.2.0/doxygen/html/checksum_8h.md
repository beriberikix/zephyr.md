---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/checksum_8h.html
original_path: doxygen/html/checksum_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

checksum.h File Reference

[Go to the source code of this file.](checksum_8h_source.md)

| Macros | |
| --- | --- |
| #define | [UBX\_CSUM\_A](#a6d1496f64e46cba548340c9c98697758)(...) |
|  | Macrobatics to compute UBX checksum at compile time. |
| #define | [UBX\_CSUM\_A\_](#a326f038f1130800d50ff861f5a7e0d9d)(...) |
| #define | [UBX\_CSUM\_A\_I](#a72257fa1af8c2e6addda019b8da4b19c)(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...) |
| #define | [UBX\_CSUM\_B](#a01922620d77048df31c70368a68062c0)(...) |
| #define | [UBX\_CSUM\_B\_](#a6d53729decd2998ddd2894d711397e0d)(...) |
| #define | [UBX\_CSUM\_B\_I](#a98cbec44089842c71101b16342be39ac)(len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...) |
| #define | [UBX\_CSUM](#af30e21304d2621a9ef9d2a6edfe7332c)(...) |

## Macro Definition Documentation

## [◆ ](#af30e21304d2621a9ef9d2a6edfe7332c)UBX\_CSUM

| #define UBX\_CSUM | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_CSUM\_A](#a6d1496f64e46cba548340c9c98697758)(\_\_VA\_ARGS\_\_), [UBX\_CSUM\_B](#a01922620d77048df31c70368a68062c0)(\_\_VA\_ARGS\_\_)

[UBX\_CSUM\_B](#a01922620d77048df31c70368a68062c0)

#define UBX\_CSUM\_B(...)

**Definition** checksum.h:23

[UBX\_CSUM\_A](#a6d1496f64e46cba548340c9c98697758)

#define UBX\_CSUM\_A(...)

Macrobatics to compute UBX checksum at compile time.

**Definition** checksum.h:13

## [◆ ](#a6d1496f64e46cba548340c9c98697758)UBX\_CSUM\_A

| #define UBX\_CSUM\_A | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_CSUM\_A\_](#a326f038f1130800d50ff861f5a7e0d9d)(\_\_VA\_ARGS\_\_)

[UBX\_CSUM\_A\_](#a326f038f1130800d50ff861f5a7e0d9d)

#define UBX\_CSUM\_A\_(...)

**Definition** checksum.h:15

Macrobatics to compute UBX checksum at compile time.

## [◆ ](#a326f038f1130800d50ff861f5a7e0d9d)UBX\_CSUM\_A\_

| #define UBX\_CSUM\_A\_ | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_CSUM\_A\_I](#a72257fa1af8c2e6addda019b8da4b19c)(\_\_VA\_ARGS\_\_, \

0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

[UBX\_CSUM\_A\_I](#a72257fa1af8c2e6addda019b8da4b19c)

#define UBX\_CSUM\_A\_I(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20,...)

**Definition** checksum.h:18

## [◆ ](#a72257fa1af8c2e6addda019b8da4b19c)UBX\_CSUM\_A\_I

| #define UBX\_CSUM\_A\_I | ( |  | *a1*, |
| --- | --- | --- | --- |
|  |  |  | *a2*, |
|  |  |  | *a3*, |
|  |  |  | *a4*, |
|  |  |  | *a5*, |
|  |  |  | *a6*, |
|  |  |  | *a7*, |
|  |  |  | *a8*, |
|  |  |  | *a9*, |
|  |  |  | *a10*, |
|  |  |  | *a11*, |
|  |  |  | *a12*, |
|  |  |  | *a13*, |
|  |  |  | *a14*, |
|  |  |  | *a15*, |
|  |  |  | *a16*, |
|  |  |  | *a17*, |
|  |  |  | *a18*, |
|  |  |  | *a19*, |
|  |  |  | *a20*, |
|  |  |  | ... ) |

**Value:**

((a1) + (a2) + (a3) + (a4) + (a5) + (a6) + (a7) + (a8) + (a9) + (a10) + \

(a11) + (a12) + (a13) + (a14) + (a15) + (a16) + (a17) + (a18) + (a19) + (a20)) & 0xFF

## [◆ ](#a01922620d77048df31c70368a68062c0)UBX\_CSUM\_B

| #define UBX\_CSUM\_B | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_CSUM\_B\_](#a6d53729decd2998ddd2894d711397e0d)(\_\_VA\_ARGS\_\_)

[UBX\_CSUM\_B\_](#a6d53729decd2998ddd2894d711397e0d)

#define UBX\_CSUM\_B\_(...)

**Definition** checksum.h:25

## [◆ ](#a6d53729decd2998ddd2894d711397e0d)UBX\_CSUM\_B\_

| #define UBX\_CSUM\_B\_ | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[UBX\_CSUM\_B\_I](#a98cbec44089842c71101b16342be39ac)([NUM\_VA\_ARGS](group__sys-util.md#ga1e5b59140ab2bf4471a512b689eda2cb)(\_\_VA\_ARGS\_\_), \_\_VA\_ARGS\_\_, \

0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

[UBX\_CSUM\_B\_I](#a98cbec44089842c71101b16342be39ac)

#define UBX\_CSUM\_B\_I(len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20,...)

**Definition** checksum.h:28

[NUM\_VA\_ARGS](group__sys-util.md#ga1e5b59140ab2bf4471a512b689eda2cb)

#define NUM\_VA\_ARGS(...)

Number of arguments in the variable arguments list.

**Definition** util\_macro.h:684

## [◆ ](#a98cbec44089842c71101b16342be39ac)UBX\_CSUM\_B\_I

| #define UBX\_CSUM\_B\_I | ( |  | *len*, |
| --- | --- | --- | --- |
|  |  |  | *a1*, |
|  |  |  | *a2*, |
|  |  |  | *a3*, |
|  |  |  | *a4*, |
|  |  |  | *a5*, |
|  |  |  | *a6*, |
|  |  |  | *a7*, |
|  |  |  | *a8*, |
|  |  |  | *a9*, |
|  |  |  | *a10*, |
|  |  |  | *a11*, |
|  |  |  | *a12*, |
|  |  |  | *a13*, |
|  |  |  | *a14*, |
|  |  |  | *a15*, |
|  |  |  | *a16*, |
|  |  |  | *a17*, |
|  |  |  | *a18*, |
|  |  |  | *a19*, |
|  |  |  | *a20*, |
|  |  |  | ... ) |

**Value:**

(((len) \* a1) + ((len - 1) \* a2) + ((len - 2) \* a3) + ((len - 3) \* a4) + \

((len - 4) \* a5) + ((len - 5) \* a6) + ((len - 6) \* a7) + ((len - 7) \* a8) + \

((len - 8) \* a9) + ((len - 9) \* a10) + ((len - 10) \* a11) + ((len - 11) \* a12) + \

((len - 12) \* a13) + ((len - 13) \* a14) + ((len - 14) \* a15) + ((len - 15) \* a16) + \

((len - 16) \* a17) + ((len - 17) \* a18) + ((len - 18) \* a19) + ((len - 19) \* a20)) & 0xFF

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx](dir_0a499179f9adf90767e72c7eb481b4fc.md)
- [checksum.h](checksum_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
