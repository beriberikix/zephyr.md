---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ztest__expect.html
original_path: doxygen/html/group__ztest__expect.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest expectation macros

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module provides expectations when using Ztest.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [zexpect\_true](#gaef66b2764b6086dfbe8cbc933a8cfdc3)(cond, ...) |
|  | Expect that *cond* is true, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_false](#ga619bd320e39799414383a228dc2d8299)(cond, ...) |
|  | Expect that *cond* is false, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_ok](#gaab325ee22058252c6a1c3243f3226657)(cond, ...) |
|  | Expect that *cond* is 0 (success), otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_ok](#gabde5406775f05d5fcd135eb926969004)(cond, ...) |
|  | Expect that *cond* is not 0 (failure), otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_is\_null](#ga10b2c904f1c68b816eae2ad53e2b9f90)(ptr, ...) |
|  | Expect that *ptr* is NULL, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_null](#gaa51053fe2a07c6417db7952d7a594798)(ptr, ...) |
|  | Expect that *ptr* is not NULL, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_equal](#ga5ba65dbf95c204ed60694c5757db247f)(a, b, ...) |
|  | Expect that *a* equals *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_equal](#ga31d83ab89828a03aebe0d0dc003f5232)(a, b, ...) |
|  | Expect that *a* does not equal *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_equal\_ptr](#gabf791d13c5781fc2215289d6dd925b3e)(a, b, ...) |
|  | Expect that *a* equals *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_within](#ga907afb07269bbc444a3d8ffee46839b5)(a, b, delta, ...) |
|  | Expect that *a* is within *b* with delta *d*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_between\_inclusive](#gac37ebea6a9c71e3666a4911ceea5c913)(a, lower, upper, ...) |
|  | Expect that *a* is greater than or equal to *l* and less than or equal to *u*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_mem\_equal](#gaee52264e5f92a606a2a85f5fbb0a85fb)(buf, exp, size, ...) |
|  | Expect that 2 memory buffers have the same contents, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_str\_equal](#gacd5ef284610ca2027fc2e892243dfd38)(s1, s2, ...) |
|  | Expect that 2 strings have the same contents, otherwise mark test as failed but continue its execution. |

## Detailed Description

This module provides expectations when using Ztest.

## Macro Definition Documentation

## [◆ ](#gac37ebea6a9c71e3666a4911ceea5c913)zexpect\_between\_inclusive

| #define zexpect\_between\_inclusive | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *lower*, |
|  |  |  | *upper*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(((a) >= (lower)) && ((a) <= (upper)), \

#a " not between " #lower " and " #upper " inclusive", ##\_\_VA\_ARGS\_\_)

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)

#define zexpect(cond, default\_msg,...)

**Definition** ztest\_assert.h:261

Expect that *a* is greater than or equal to *l* and less than or equal to *u*, otherwise mark test as failed but continue its execution.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | lower | Lower limit |
    | upper | Upper limit |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#ga5ba65dbf95c204ed60694c5757db247f)zexpect\_equal

| #define zexpect\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)((a) == (b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Expect that *a* equals *b*, otherwise mark test as failed but continue its execution.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gabf791d13c5781fc2215289d6dd925b3e)zexpect\_equal\_ptr

| #define zexpect\_equal\_ptr | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)((void \*)(a) == (void \*)(b), #a " not equal to " #b, ##\_\_VA\_ARGS\_\_)

Expect that *a* equals *b*, otherwise mark test as failed but continue its execution.

*a* and *b* will be converted to void \* before comparing.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#ga619bd320e39799414383a228dc2d8299)zexpect\_false

| #define zexpect\_false | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(!(cond), #cond " is true", ##\_\_VA\_ARGS\_\_)

Expect that *cond* is false, otherwise mark test as failed but continue its execution.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#ga10b2c904f1c68b816eae2ad53e2b9f90)zexpect\_is\_null

| #define zexpect\_is\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)((ptr) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), #ptr " is not NULL", ##\_\_VA\_ARGS\_\_)

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Expect that *ptr* is NULL, otherwise mark test as failed but continue its execution.

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gaee52264e5f92a606a2a85f5fbb0a85fb)zexpect\_mem\_equal

| #define zexpect\_mem\_equal | ( |  | *buf*, |
| --- | --- | --- | --- |
|  |  |  | *exp*, |
|  |  |  | *size*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)([memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)(buf, exp, size) == 0, #buf " not equal to " #exp, ##\_\_VA\_ARGS\_\_)

[memcmp](string_8h.md#ad8bfbfa1e4ad284ded921dd775735521)

int memcmp(const void \*m1, const void \*m2, size\_t n)

Expect that 2 memory buffers have the same contents, otherwise mark test as failed but continue its execution.

Parameters
:   | buf | Buffer to compare |
    | --- | --- |
    | exp | Buffer with expected contents |
    | size | Size of buffers |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#ga31d83ab89828a03aebe0d0dc003f5232)zexpect\_not\_equal

| #define zexpect\_not\_equal | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)((a) != (b), #a " equal to " #b, ##\_\_VA\_ARGS\_\_)

Expect that *a* does not equal *b*, otherwise mark test as failed but continue its execution.

*a* and *b* won't be converted and will be compared directly.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gaa51053fe2a07c6417db7952d7a594798)zexpect\_not\_null

| #define zexpect\_not\_null | ( |  | *ptr*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)((ptr) != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), #ptr " is NULL", ##\_\_VA\_ARGS\_\_)

Expect that *ptr* is not NULL, otherwise mark test as failed but continue its execution.

Parameters
:   | ptr | Pointer to compare |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gabde5406775f05d5fcd135eb926969004)zexpect\_not\_ok

| #define zexpect\_not\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(!!(cond), #cond " is zero", ##\_\_VA\_ARGS\_\_)

Expect that *cond* is not 0 (failure), otherwise mark test as failed but continue its execution.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gaab325ee22058252c6a1c3243f3226657)zexpect\_ok

| #define zexpect\_ok | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(!(cond), #cond " is non-zero", ##\_\_VA\_ARGS\_\_)

Expect that *cond* is 0 (success), otherwise mark test as failed but continue its execution.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gacd5ef284610ca2027fc2e892243dfd38)zexpect\_str\_equal

| #define zexpect\_str\_equal | ( |  | *s1*, |
| --- | --- | --- | --- |
|  |  |  | *s2*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)([strcmp](string_8h.md#a11bd144d7d44914099a3aeddf1c8567d)(s1, s2) == 0, #s1 " not equal to " #s2, ##\_\_VA\_ARGS\_\_)

[strcmp](string_8h.md#a11bd144d7d44914099a3aeddf1c8567d)

int strcmp(const char \*s1, const char \*s2)

Expect that 2 strings have the same contents, otherwise mark test as failed but continue its execution.

Parameters
:   | s1 | The first string |
    | --- | --- |
    | s2 | The second string |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#gaef66b2764b6086dfbe8cbc933a8cfdc3)zexpect\_true

| #define zexpect\_true | ( |  | *cond*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(cond, #cond " is false", ##\_\_VA\_ARGS\_\_)

Expect that *cond* is true, otherwise mark test as failed but continue its execution.

Parameters
:   | cond | Condition to check |
    | --- | --- |
    | ... | Optional message and variables to print if the expectation fails |

## [◆ ](#ga907afb07269bbc444a3d8ffee46839b5)zexpect\_within

| #define zexpect\_within | ( |  | *a*, |
| --- | --- | --- | --- |
|  |  |  | *b*, |
|  |  |  | *delta*, |
|  |  |  | ... ) |

`#include <[ztest_assert.h](ztest__assert_8h.md)>`

**Value:**

[zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(((a) >= ((b) - (delta))) && ((a) <= ((b) + (delta))), \

#a " not within " #b " +/- " #delta, ##\_\_VA\_ARGS\_\_)

Expect that *a* is within *b* with delta *d*, otherwise mark test as failed but continue its execution.

Parameters
:   | a | Value to compare |
    | --- | --- |
    | b | Value to compare |
    | delta | Difference between a and b |
    | ... | Optional message and variables to print if the expectation fails |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
