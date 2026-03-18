---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ztest__assert.html
original_path: doxygen/html/group__ztest__assert.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest assertion macros

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module provides assertions when using Ztest.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(cond, default\_msg, ...) |
| #define | [zassume](#ga5a4319eec770be532f34acb86e022c48)(cond, default\_msg, ...) |
| #define | [zexpect](#ga7bd837a8164123e3a06795b9f87a308d)(cond, default\_msg, ...) |
| #define | [zassert\_unreachable](#ga300684a6b56e73e2cad6fd7458541129)(...) |
|  | Assert that this function call won't be reached. |
| #define | [zassert\_true](#gaeebddde19012223e3d5e853a1dac3ac5)(cond, ...) |
|  | Assert that *cond* is true. |
| #define | [zassert\_false](#ga7330d1794fb961e07ee40294019dead0)(cond, ...) |
|  | Assert that *cond* is false. |
| #define | [zassert\_ok](#gade40e2ec78ec813739e7725524fae7f0)(cond, ...) |
|  | Assert that *cond* is 0 (success). |
| #define | [zassert\_not\_ok](#gafe0e2609f77906ab0caddc31448a4fc8)(cond, ...) |
|  | Assert that *cond* is not 0 (failure). |
| #define | [zassert\_is\_null](#gac0839891fd8bb7313b98551465e04c19)(ptr, ...) |
|  | Assert that *ptr* is NULL. |
| #define | [zassert\_not\_null](#ga849adad4afe893a7ae3dc2fbe750dc00)(ptr, ...) |
|  | Assert that *ptr* is not NULL. |
| #define | [zassert\_equal](#gacd075c7ee4dc2d64701bd3098a31b673)(a, b, ...) |
|  | Assert that *a* equals *b*. |
| #define | [zassert\_not\_equal](#ga43f306bf33d5e837b8927df16b82a363)(a, b, ...) |
|  | Assert that *a* does not equal *b*. |
| #define | [zassert\_equal\_ptr](#gabf20273fcba9cc45939a9f7db77f0bfc)(a, b, ...) |
|  | Assert that *a* equals *b*. |
| #define | [zassert\_within](#gacc930af1a66e8533c5eca9526e198b4b)(a, b, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), ...) |
|  | Assert that *a* is within *b* with delta *d*. |
| #define | [zassert\_between\_inclusive](#ga2b6b41de3e4856b21458febab3261b91)(a, l, u, ...) |
|  | Assert that *a* is greater than or equal to *l* and less than or equal to *u*. |
| #define | [zassert\_mem\_equal](#gabbfcf6345172387326d35b5d0e2bb051)(...) |
|  | Assert that 2 memory buffers have the same contents. |
| #define | [zassert\_mem\_equal\_\_](#ga30e5fefa185944d3e949d4023c2eea27)(buf, exp, size, ...) |
|  | Internal assert that 2 memory buffers have the same contents. |

## Detailed Description

This module provides assertions when using Ztest.

## Macro Definition Documentation

## [◆ ](#ga0911ad9e94cdf1fe011d21316683ee7f)zassert

| #define zassert | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | *default\_msg*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

\_zassert\_va(cond, default\_msg, [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

## [◆ ](#ga2b6b41de3e4856b21458febab3261b91)zassert\_between\_inclusive

| #define zassert\_between\_inclusive | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *l*, |
|  |  |  | *u*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(((a) >= (l)) && ((a) <= (u)), #a " not between " #l " and " #u " inclusive", \

##\_\_VA\_ARGS\_\_)

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)

#define zassert(cond, default\_msg,...)

**Definition** ztest\_assert.h:188

Assert that *a* is greater than or equal to *l* and less than or equal to *u*.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | l | Lower limit |
    | u | Upper limit |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gacd075c7ee4dc2d64701bd3098a31b673)zassert\_equal

| #define zassert\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Assert that *a* equals *b*.

*a* and *b* won't be converted and will be compared directly.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gabf20273fcba9cc45939a9f7db77f0bfc)zassert\_equal\_ptr

| #define zassert\_equal\_ptr | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Assert that *a* equals *b*.

*a* and *b* will be converted to void \* before comparing.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#ga7330d1794fb961e07ee40294019dead0)zassert\_false

| #define zassert\_false | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

Assert that *cond* is false.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gac0839891fd8bb7313b98551465e04c19)zassert\_is\_null

| #define zassert\_is\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)((ptr) == NULL, #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

Assert that *ptr* is NULL.

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gabbfcf6345172387326d35b5d0e2bb051)zassert\_mem\_equal

| #define zassert\_mem\_equal | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert\_mem\_equal\_\_](#ga30e5fefa185944d3e949d4023c2eea27)(\_\_VA\_ARGS\_\_)

[zassert\_mem\_equal\_\_](#ga30e5fefa185944d3e949d4023c2eea27)

#define zassert\_mem\_equal\_\_(buf, exp, size,...)

Internal assert that 2 memory buffers have the same contents.

**Definition** ztest\_assert.h:389

Assert that 2 memory buffers have the same contents.

This macro calls the final memory comparison assertion macro. Using double expansion allows providing some arguments by macros that would expand to more than one values (ANSI-C99 defines that all the macro arguments have to be expanded before macro call).

Parameters
:   | ... | Arguments, see [zassert\_mem\_equal\_\_](#ga30e5fefa185944d3e949d4023c2eea27) for real arguments accepted. |
    | --- | --- |

## [◆ ](#ga30e5fefa185944d3e949d4023c2eea27)zassert\_mem\_equal\_\_

| #define zassert\_mem\_equal\_\_ | ( |  | *buf*, |
| --- | --- | --- | --- |
|  |  |  | *exp*, |
|  |  |  | *size*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

Internal assert that 2 memory buffers have the same contents.

Note
:   This is internal macro, to be used as a second expansion. See [zassert\_mem\_equal](#gabbfcf6345172387326d35b5d0e2bb051).

Parameters
:   | buf | Buffer to compare |
    | --- | --- |
    | exp | Buffer with expected contents |
    | size | Size of buffers |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#ga43f306bf33d5e837b8927df16b82a363)zassert\_not\_equal

| #define zassert\_not\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

Assert that *a* does not equal *b*.

*a* and *b* won't be converted and will be compared directly.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#ga849adad4afe893a7ae3dc2fbe750dc00)zassert\_not\_null

| #define zassert\_not\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)((ptr) != NULL, #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

Assert that *ptr* is not NULL.

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gafe0e2609f77906ab0caddc31448a4fc8)zassert\_not\_ok

| #define zassert\_not\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

Assert that *cond* is not 0 (failure).

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gade40e2ec78ec813739e7725524fae7f0)zassert\_ok

| #define zassert\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

Assert that *cond* is 0 (success).

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#gaeebddde19012223e3d5e853a1dac3ac5)zassert\_true

| #define zassert\_true | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

Assert that *cond* is true.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#ga300684a6b56e73e2cad6fd7458541129)zassert\_unreachable

| #define zassert\_unreachable | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(0, "Reached unreachable code", ##\_\_VA\_ARGS\_\_)

Assert that this function call won't be reached.

Parameters
:   | ... | Optional message and variables to print if the assertion fails |
    | --- | --- |

## [◆ ](#gacc930af1a66e8533c5eca9526e198b4b)zassert\_within

| #define zassert\_within | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zassert](#ga0911ad9e94cdf1fe011d21316683ee7f)(((a) >= ((b) - ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))) && ((a) <= ((b) + ([d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)))), #a " not within " #b " +/- " #[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), \

##\_\_VA\_ARGS\_\_)

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Assert that *a* is within *b* with delta *d*.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Delta |
    | ... | Optional message and variables to print if the assertion fails |

## [◆ ](#ga5a4319eec770be532f34acb86e022c48)zassume

| #define zassume | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | *default\_msg*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

\_zassume\_va(cond, default\_msg, [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

## [◆ ](#ga7bd837a8164123e3a06795b9f87a308d)zexpect

| #define zexpect | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | *default\_msg*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

\_zexpect\_va(cond, default\_msg, [COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(\_\_VA\_OPT\_\_(1), (\_\_VA\_ARGS\_\_), (NULL)))

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
