---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ztest__assume.html
original_path: doxygen/html/group__ztest__assume.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest assumption macros

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module provides assumptions when using Ztest.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [zassume\_true](#ga6f5778ed8c1205126f7dcafb6eb26905)(cond, ...) |
|  | Assume that *cond* is true. |
| #define | [zassume\_false](#ga5acf4256e5af3afaed06da7400dc3ad5)(cond, ...) |
|  | Assume that *cond* is false. |
| #define | [zassume\_ok](#ga9c6d1c701dd2d50027bf5e24b7567ae4)(cond, ...) |
|  | Assume that *cond* is 0 (success). |
| #define | [zassume\_not\_ok](#ga539831d2f42cc991a8295b388ec12846)(cond, ...) |
|  | Assume that *cond* is not 0 (failure). |
| #define | [zassume\_is\_null](#ga3c5b1814deb5974e8ba0af961b516fa0)(ptr, ...) |
|  | Assume that *ptr* is NULL. |
| #define | [zassume\_not\_null](#ga24f4144edf5cef493c88872c7d56900e)(ptr, ...) |
|  | Assume that *ptr* is not NULL. |
| #define | [zassume\_equal](#ga88c2a3153568a6f621b88dd6ceeb48d6)(a, b, ...) |
|  | Assume that *a* equals *b*. |
| #define | [zassume\_not\_equal](#ga0d90bb874c3135ffee870a4b61607853)(a, b, ...) |
|  | Assume that *a* does not equal *b*. |
| #define | [zassume\_equal\_ptr](#ga78d6fbbf5eb13b32a5164053811b6cca)(a, b, ...) |
|  | Assume that *a* equals *b*. |
| #define | [zassume\_within](#gad808c91e07e6c27b2e28ec7e04e03854)(a, b, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), ...) |
|  | Assume that *a* is within *b* with delta *d*. |
| #define | [zassume\_between\_inclusive](#gacff02eeba8dd334b3727dbe2036617e3)(a, l, u, ...) |
|  | Assume that *a* is greater than or equal to *l* and less than or equal to *u*. |
| #define | [zassume\_mem\_equal](#ga62be45256399530167745e71226e4a37)(...) |
|  | Assume that 2 memory buffers have the same contents. |
| #define | [zassume\_mem\_equal\_\_](#gaaed6045f194ead4ffe1dd72a6fa5175d)(buf, exp, size, ...) |
|  | Internal assume that 2 memory buffers have the same contents. |

## Detailed Description

This module provides assumptions when using Ztest.

## Macro Definition Documentation

## [◆ ](#gacff02eeba8dd334b3727dbe2036617e3)zassume\_between\_inclusive

| #define zassume\_between\_inclusive | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *l*, |
|  |  |  | *u*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

##\_\_VA\_ARGS\_\_)

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)

#define zassume(cond, default\_msg,...)

**Definition** ztest\_assert.h:225

Assume that *a* is greater than or equal to *l* and less than or equal to *u*.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | a | Value to compare |
    | --- | --- |
    | l | Lower limit |
    | u | Upper limit |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga88c2a3153568a6f621b88dd6ceeb48d6)zassume\_equal

| #define zassume\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Assume that *a* equals *b*.

*a* and *b* won't be converted and will be compared directly. If the assumption fails, the test will be marked as "skipped".

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga78d6fbbf5eb13b32a5164053811b6cca)zassume\_equal\_ptr

| #define zassume\_equal\_ptr | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Assume that *a* equals *b*.

*a* and *b* will be converted to void \* before comparing. If the assumption fails, the test will be marked as "skipped".

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga5acf4256e5af3afaed06da7400dc3ad5)zassume\_false

| #define zassume\_false | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

Assume that *cond* is false.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga3c5b1814deb5974e8ba0af961b516fa0)zassume\_is\_null

| #define zassume\_is\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

Assume that *ptr* is NULL.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga62be45256399530167745e71226e4a37)zassume\_mem\_equal

| #define zassume\_mem\_equal | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume\_mem\_equal\_\_](#gaaed6045f194ead4ffe1dd72a6fa5175d)(\_\_VA\_ARGS\_\_)

[zassume\_mem\_equal\_\_](#gaaed6045f194ead4ffe1dd72a6fa5175d)

#define zassume\_mem\_equal\_\_(buf, exp, size,...)

Internal assume that 2 memory buffers have the same contents.

**Definition** ztest\_assert.h:557

Assume that 2 memory buffers have the same contents.

This macro calls the final memory comparison assumption macro. Using double expansion allows providing some arguments by macros that would expand to more than one values (ANSI-C99 defines that all the macro arguments have to be expanded before macro call).

Parameters
:   | ... | Arguments, see [zassume\_mem\_equal\_\_](#gaaed6045f194ead4ffe1dd72a6fa5175d) for real arguments accepted. |
    | --- | --- |

## [◆ ](#gaaed6045f194ead4ffe1dd72a6fa5175d)zassume\_mem\_equal\_\_

| #define zassume\_mem\_equal\_\_ | ( |  | *buf*, |
| --- | --- | --- | --- |
|  |  |  | *exp*, |
|  |  |  | *size*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

Internal assume that 2 memory buffers have the same contents.

If the assumption fails, the test will be marked as "skipped".

Note
:   This is internal macro, to be used as a second expansion. See [zassume\_mem\_equal](#ga62be45256399530167745e71226e4a37).

Parameters
:   | buf | Buffer to compare |
    | --- | --- |
    | exp | Buffer with expected contents |
    | size | Size of buffers |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga0d90bb874c3135ffee870a4b61607853)zassume\_not\_equal

| #define zassume\_not\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

Assume that *a* does not equal *b*.

*a* and *b* won't be converted and will be compared directly. If the assumption fails, the test will be marked as "skipped".

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga24f4144edf5cef493c88872c7d56900e)zassume\_not\_null

| #define zassume\_not\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

Assume that *ptr* is not NULL.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga539831d2f42cc991a8295b388ec12846)zassume\_not\_ok

| #define zassume\_not\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

Assume that *cond* is not 0 (failure).

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga9c6d1c701dd2d50027bf5e24b7567ae4)zassume\_ok

| #define zassume\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

Assume that *cond* is 0 (success).

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#ga6f5778ed8c1205126f7dcafb6eb26905)zassume\_true

| #define zassume\_true | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

Assume that *cond* is true.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assumption fails |

## [◆ ](#gad808c91e07e6c27b2e28ec7e04e03854)zassume\_within

| #define zassume\_within | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(((a) >= ((b) - ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))) && ((a) <= ((b) + ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))), #a " not within " #b " +/- " #[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), \

##\_\_VA\_ARGS\_\_)

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Assume that *a* is within *b* with delta *d*.

If the assumption fails, the test will be marked as "skipped".

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Delta |
    | ... | Optional message and variables to print if the assumption fails |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
