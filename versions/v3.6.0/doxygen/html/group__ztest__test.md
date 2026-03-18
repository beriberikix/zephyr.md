---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ztest__test.html
original_path: doxygen/html/group__ztest__test.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ztest testing macros

[Testing](group__testing.md) » [Zephyr Testing Framework (ZTest)](group__ztest.md)

This module eases the testing process by providing helpful macros and other testing structures.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ztest\_arch\_api](structztest__arch__api.md) |
|  | Structure for architecture specific APIs. [More...](structztest__arch__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ZTEST](#gac25858f76ea667d07de422a3b489cb15)(suite, fn) |
|  | Create and register a new unit test. |
| #define | [ZTEST\_USER](#ga7121acc7ee00646cacefa773ff9631c8)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_F](#gacd3ab522e0e5c8a270e86b0cb6bd81b2)(suite, fn) |
|  | Define a test function. |
| #define | [ZTEST\_USER\_F](#ga12ccce144e577cac6ba763982ad14def)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_RULE](#ga2a0a5e3b6e8fa1c9a03e7600895d875f)(name, before\_each\_fn, after\_each\_fn) |
|  | Define a test rule that will run before/after each unit test. |
| #define | [ztest\_run\_test\_suite](#ga29557673d07a87d5d4ace36521937848)(suite, shuffle, suite\_iter, case\_iter) |
|  | Run the specified test suite. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ztest\_rule\_cb](#ga2090c493018a95112b89c5f83b5d8162)) (const struct [ztest\_unit\_test](structztest__unit__test.md) \*test, void \*data) |
|  | Test rule callback function signature. |

| Functions | |
| --- | --- |
| void | [ztest\_test\_fail](#gacd6eb423f54dce8544f7c3b1618c0374) (void) |
|  | Fail the currently running test. |
| void | [ztest\_test\_pass](#ga085d30a04102ebb8c3f2206020723ee0) (void) |
|  | Pass the currently running test. |
| void | [ztest\_test\_skip](#gada3b1fcfa71db1bf7787c03ff45256d5) (void) |
|  | Skip the current test. |
| void | [ztest\_skip\_failed\_assumption](#ga17537c79021fbc12e56b72ccec4b99c5) (void) |
| void | [ztest\_simple\_1cpu\_before](#gac7ddc33b5a0d11e2ffa0a564019c5e3d) (void \*data) |
|  | A 'before' function to use in test suites that just need to start 1cpu. |
| void | [ztest\_simple\_1cpu\_after](#gaa53486873430dd8fa978745d8a1d0686) (void \*data) |
|  | A 'after' function to use in test suites that just need to stop 1cpu. |

## Detailed Description

This module eases the testing process by providing helpful macros and other testing structures.

## Macro Definition Documentation

## [◆ ](#gac25858f76ea667d07de422a3b489cb15)ZTEST

| #define ZTEST | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

Z\_ZTEST(suite, fn, 0)

Create and register a new unit test.

Calling this macro will create a new unit test and attach it to the declared suite. The suite does not need to be defined in the same compilation unit.

Parameters
:   | suite | The name of the test suite to attach this test |
    | --- | --- |
    | fn | The test function to call. |

## [◆ ](#gacd3ab522e0e5c8a270e86b0cb6bd81b2)ZTEST\_F

| #define ZTEST\_F | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

Z\_ZTEST\_F(suite, fn, 0)

Define a test function.

This macro behaves exactly the same as [ZTEST()](#gac25858f76ea667d07de422a3b489cb15), but the function takes an argument for the fixture of type struct suite##\_fixture\* named this.

Parameters
:   | suite | The name of the test suite to attach this test |
    | --- | --- |
    | fn | The test function to call. |

## [◆ ](#ga2a0a5e3b6e8fa1c9a03e7600895d875f)ZTEST\_RULE

| #define ZTEST\_RULE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *before\_each\_fn*, |
|  |  |  | *after\_each\_fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(ztest\_test\_rule, z\_ztest\_test\_rule\_##name) = { \

.before\_each = (before\_each\_fn), \

.after\_each = (after\_each\_fn), \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Define a test rule that will run before/after each unit test.

Functions defined here will run before/after each unit test for every test suite. Along with the callback, the test functions are provided a pointer to the test being run, and the data. This provides a mechanism for tests to perform custom operations depending on the specific test or the data (for example logging may use the test's name).

Ordering:

- Test rule's before function will run before the suite's before function. This is done to allow the test suite's customization to take precedence over the rule which is applied to all suites.
- Test rule's after function is not guaranteed to run in any particular order.

Parameters
:   | name | The name for the test rule (must be unique within the compilation unit) |
    | --- | --- |
    | before\_each\_fn | The callback function ([ztest\_rule\_cb](#ga2090c493018a95112b89c5f83b5d8162)) to call before each test (may be NULL) |
    | after\_each\_fn | The callback function ([ztest\_rule\_cb](#ga2090c493018a95112b89c5f83b5d8162)) to call after each test (may be NULL) |

## [◆ ](#ga29557673d07a87d5d4ace36521937848)ztest\_run\_test\_suite

| #define ztest\_run\_test\_suite | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *shuffle*, |
|  |  |  | *suite\_iter*, |
|  |  |  | *case\_iter* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

z\_ztest\_run\_test\_suite([STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(suite), shuffle, suite\_iter, case\_iter)

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

Run the specified test suite.

Parameters
:   | suite | Test suite to run. |
    | --- | --- |
    | shuffle | Shuffle tests |
    | suite\_iter | Test suite repetitions. |
    | case\_iter | Test case repetitions. |

## [◆ ](#ga7121acc7ee00646cacefa773ff9631c8)ZTEST\_USER

| #define ZTEST\_USER | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

Z\_ZTEST(suite, fn, [K\_USER](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc))

[K\_USER](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc)

#define K\_USER

user mode thread

**Definition** kernel.h:192

Define a test function that should run as a user thread.

This macro behaves exactly the same as ZTEST, but calls the test function in user space if CONFIG\_USERSPACE was enabled.

Parameters
:   | suite | The name of the test suite to attach this test |
    | --- | --- |
    | fn | The test function to call. |

## [◆ ](#ga12ccce144e577cac6ba763982ad14def)ZTEST\_USER\_F

| #define ZTEST\_USER\_F | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

Z\_ZTEST\_F(suite, fn, [K\_USER](group__thread__apis.md#gacb5340339892f22301e02697c6039ccc))

Define a test function that should run as a user thread.

If CONFIG\_USERSPACE is not enabled, this is functionally identical to [ZTEST\_F()](#gacd3ab522e0e5c8a270e86b0cb6bd81b2). The test function takes a single fixture argument of type struct suite##\_fixture\* named this.

Parameters
:   | suite | The name of the test suite to attach this test |
    | --- | --- |
    | fn | The test function to call. |

## Typedef Documentation

## [◆ ](#ga2090c493018a95112b89c5f83b5d8162)ztest\_rule\_cb

| typedef void(\* ztest\_rule\_cb) (const struct [ztest\_unit\_test](structztest__unit__test.md) \*test, void \*data) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Test rule callback function signature.

The function signature that can be used to register a test rule's before/after callback. This provides access to the test and the fixture data (if provided).

Parameters
:   | test | Pointer to the unit test in context |
    | --- | --- |
    | data | Pointer to the test's fixture data (may be NULL) |

## Function Documentation

## [◆ ](#gaa53486873430dd8fa978745d8a1d0686)ztest\_simple\_1cpu\_after()

| void ztest\_simple\_1cpu\_after | ( | void \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

A 'after' function to use in test suites that just need to stop 1cpu.

Ignores data, and calls z\_test\_1cpu\_stop()

Parameters
:   | data | The test suite's data |
    | --- | --- |

## [◆ ](#gac7ddc33b5a0d11e2ffa0a564019c5e3d)ztest\_simple\_1cpu\_before()

| void ztest\_simple\_1cpu\_before | ( | void \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

A 'before' function to use in test suites that just need to start 1cpu.

Ignores data, and calls z\_test\_1cpu\_start()

Parameters
:   | data | The test suite's data |
    | --- | --- |

## [◆ ](#ga17537c79021fbc12e56b72ccec4b99c5)ztest\_skip\_failed\_assumption()

| void ztest\_skip\_failed\_assumption | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

## [◆ ](#gacd6eb423f54dce8544f7c3b1618c0374)ztest\_test\_fail()

| void ztest\_test\_fail | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Fail the currently running test.

This is the function called from failed assertions and the like. You probably don't need to call it yourself.

## [◆ ](#ga085d30a04102ebb8c3f2206020723ee0)ztest\_test\_pass()

| void ztest\_test\_pass | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Pass the currently running test.

Normally a test passes just by returning without an assertion failure. However, if the success case for your test involves a fatal fault, you can call this function from k\_sys\_fatal\_error\_handler to indicate that the test passed before aborting the thread.

## [◆ ](#gada3b1fcfa71db1bf7787c03ff45256d5)ztest\_test\_skip()

| void ztest\_test\_skip | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Skip the current test.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
