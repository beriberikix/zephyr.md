---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__ztest__test.html
original_path: doxygen/html/group__ztest__test.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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
| struct | [ztest\_expected\_result\_entry](structztest__expected__result__entry.md) |
|  | A single expectation entry allowing tests to fail/skip and be considered passing. [More...](structztest__expected__result__entry.md#details) |
| struct | [ztest\_unit\_test](structztest__unit__test.md) |
| struct | [ztest\_suite\_stats](structztest__suite__stats.md) |
|  | Stats about a ztest suite. [More...](structztest__suite__stats.md#details) |
| struct | [ztest\_unit\_test\_stats](structztest__unit__test__stats.md) |
| struct | [ztest\_suite\_node](structztest__suite__node.md) |
|  | A single node of test suite. [More...](structztest__suite__node.md#details) |
| struct | [ztest\_arch\_api](structztest__arch__api.md) |
|  | Structure for architecture specific APIs. [More...](structztest__arch__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ZTEST\_EXPECT\_FAIL](#gaeaa5b96855dd45e015b9556212f8945a)(\_suite\_name, \_test\_name) |
|  | Expect a test to fail (mark it passing if it failed). |
| #define | [ZTEST\_EXPECT\_SKIP](#gacb6f06920e522b9a9f6e7a98f0620f38)(\_suite\_name, \_test\_name) |
|  | Expect a test to skip (mark it passing if it failed). |
| #define | [ZTEST\_TEST\_COUNT](#ga8777ca60bd21cc128f64833bd7921b9c)   (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start) |
|  | Number of registered unit tests. |
| #define | [ZTEST\_SUITE\_COUNT](#ga678b4ae96879c029e6e567a326bbf027)   (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start) |
|  | Number of registered test suites. |
| #define | [ZTEST\_SUITE](#gaef8892743e2d47c983efcb61beeedeb3)(SUITE\_NAME, PREDICATE, setup\_fn, before\_fn, after\_fn, teardown\_fn) |
|  | Create and register a ztest suite. |
| #define | [ZTEST\_DMEM](#ga2c7d0aa85e7f320d582395c5ded90133)   [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Make data section used by Ztest userspace accessible. |
| #define | [ZTEST\_BMEM](#gac3de5965061b1164a8033712c9094e23)   [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Make bss section used by Ztest userspace accessible. |
| #define | [ZTEST\_SECTION](#ga44777f5011728bbff63fe3639c1b4aa8)   [K\_APP\_DMEM\_SECTION](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Ztest data section for accessing data from userspace. |
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
| typedef void \*(\* | [ztest\_suite\_setup\_t](#ga0063907dd70b9eb817ea472162693ee4)) (void) |
|  | Setup function to run before running this suite. |
| typedef void(\* | [ztest\_suite\_before\_t](#gac8a204832c267fed047e7707b65be74d)) (void \*fixture) |
|  | Function to run before each test in this suite. |
| typedef void(\* | [ztest\_suite\_after\_t](#ga0f9eeb8ddae455c1e7cc7a388a7b013c)) (void \*fixture) |
|  | Function to run after each test in this suite. |
| typedef void(\* | [ztest\_suite\_teardown\_t](#ga7769b894fdac5283ac949ce8fceea0dd)) (void \*fixture) |
|  | Teardown function to run after running this suite. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [ztest\_suite\_predicate\_t](#gad5323aa82773dac33cf0930e9524420c)) (const void \*global\_state) |
|  | An optional predicate function to determine if the test should run. |
| typedef void(\* | [ztest\_rule\_cb](#ga2090c493018a95112b89c5f83b5d8162)) (const struct [ztest\_unit\_test](structztest__unit__test.md) \*test, void \*data) |
|  | Test rule callback function signature. |

| Enumerations | |
| --- | --- |
| enum | [ztest\_expected\_result](#gaf4dfaad1b5f1059e87f406979769aa26) { [ZTEST\_EXPECTED\_RESULT\_FAIL](#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) = 0 , [ZTEST\_EXPECTED\_RESULT\_SKIP](#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a) } |
|  | The expected result of a test. [More...](#gaf4dfaad1b5f1059e87f406979769aa26) |
| enum | [ztest\_result](#gac2842295307e7286d256bb179be60b02) {     [ZTEST\_RESULT\_PENDING](#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc) , [ZTEST\_RESULT\_PASS](#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e) , [ZTEST\_RESULT\_FAIL](#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888) , [ZTEST\_RESULT\_SKIP](#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4) ,     [ZTEST\_RESULT\_SUITE\_SKIP](#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e) , [ZTEST\_RESULT\_SUITE\_FAIL](#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)   } |
|  | The result of the current running test. [More...](#gac2842295307e7286d256bb179be60b02) |
| enum | [ztest\_phase](#ga5dde8913cf45656bca8a48c825a95d59) {     [TEST\_PHASE\_SETUP](#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf) , [TEST\_PHASE\_BEFORE](#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765) , [TEST\_PHASE\_TEST](#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1) , [TEST\_PHASE\_AFTER](#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663) ,     [TEST\_PHASE\_TEARDOWN](#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901) , [TEST\_PHASE\_FRAMEWORK](#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)   } |
|  | Each enum member represents a distinct phase of execution for the test binary. [More...](#ga5dde8913cf45656bca8a48c825a95d59) |

| Functions | |
| --- | --- |
| void | [ztest\_run\_all](#gac6b1f8b820cd682094b7aaeebdaa106e) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Default entry point for running or listing registered unit tests. |
| int | [ztest\_run\_test\_suites](#gaafb3cba3a9637839952b2db2486ab88c) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Run the registered unit tests which return true from their predicate function. |
| void | [ztest\_verify\_all\_test\_suites\_ran](#ga349fda278dff713debfd2a3b94b8b1eb) (void) |
|  | Fails the test if any of the registered tests did not run. |
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

| Variables | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446) |

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

## [◆ ](#gac3de5965061b1164a8033712c9094e23)ZTEST\_BMEM

| #define ZTEST\_BMEM   [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Make bss section used by Ztest userspace accessible.

## [◆ ](#ga2c7d0aa85e7f320d582395c5ded90133)ZTEST\_DMEM

| #define ZTEST\_DMEM   [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Make data section used by Ztest userspace accessible.

## [◆ ](#gaeaa5b96855dd45e015b9556212f8945a)ZTEST\_EXPECT\_FAIL

| #define ZTEST\_EXPECT\_FAIL | ( |  | *\_suite\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_test\_name* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

\_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, [ZTEST\_EXPECTED\_RESULT\_FAIL](#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d))

[ZTEST\_EXPECTED\_RESULT\_FAIL](#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)

@ ZTEST\_EXPECTED\_RESULT\_FAIL

Expect a test to fail.

**Definition** ztest\_test.h:49

Expect a test to fail (mark it passing if it failed).

Adding this macro to your logic will allow the failing test to be considered passing, example:

```
ZTEST_EXPECT_FAIL(my_suite, test_x);
ZTEST(my_suite, text_x) {
  zassert_true(false, NULL);
}
```

Parameters
:   | \_suite\_name | The name of the suite |
    | --- | --- |
    | \_test\_name | The name of the test |

## [◆ ](#gacb6f06920e522b9a9f6e7a98f0620f38)ZTEST\_EXPECT\_SKIP

| #define ZTEST\_EXPECT\_SKIP | ( |  | *\_suite\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_test\_name* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

\_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, [ZTEST\_EXPECTED\_RESULT\_SKIP](#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a))

[ZTEST\_EXPECTED\_RESULT\_SKIP](#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)

@ ZTEST\_EXPECTED\_RESULT\_SKIP

Expect a test to pass.

**Definition** ztest\_test.h:50

Expect a test to skip (mark it passing if it failed).

Adding this macro to your logic will allow the failing test to be considered passing, example:

```
ZTEST_EXPECT_SKIP(my_suite, test_x);
ZTEST(my_suite, text_x) {
  zassume_true(false, NULL);
}
```

Parameters
:   | \_suite\_name | The name of the suite |
    | --- | --- |
    | \_test\_name | The name of the test |

## [◆ ](#gacd3ab522e0e5c8a270e86b0cb6bd81b2)ZTEST\_F

| #define ZTEST\_F | ( |  | *suite*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

Z\_ZTEST\_F(suite, fn, 0)

Define a test function.

This macro behaves exactly the same as [ZTEST()](#gac25858f76ea667d07de422a3b489cb15), but the function takes an argument for the fixture of type struct suite##\_fixture\* named fixture.

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

## [◆ ](#ga44777f5011728bbff63fe3639c1b4aa8)ZTEST\_SECTION

| #define ZTEST\_SECTION   [K\_APP\_DMEM\_SECTION](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)([ztest\_mem\_partition](#ga3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Ztest data section for accessing data from userspace.

## [◆ ](#gaef8892743e2d47c983efcb61beeedeb3)ZTEST\_SUITE

| #define ZTEST\_SUITE | ( |  | *SUITE\_NAME*, |
| --- | --- | --- | --- |
|  |  |  | *PREDICATE*, |
|  |  |  | *setup\_fn*, |
|  |  |  | *before\_fn*, |
|  |  |  | *after\_fn*, |
|  |  |  | *teardown\_fn* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

**Value:**

struct [ztest\_suite\_stats](structztest__suite__stats.md) [UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(z\_ztest\_suite\_node\_stats\_, SUITE\_NAME); \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([ztest\_suite\_node](structztest__suite__node.md), \

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(z\_ztest\_test\_node\_, SUITE\_NAME)) = { \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(SUITE\_NAME), \

.setup = (setup\_fn), \

.before = (before\_fn), \

.after = (after\_fn), \

.teardown = (teardown\_fn), \

.predicate = PREDICATE, \

.stats = &[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(z\_ztest\_suite\_node\_stats\_, SUITE\_NAME), \

}

[ztest\_suite\_node](structztest__suite__node.md)

A single node of test suite.

**Definition** ztest\_test.h:190

[ztest\_suite\_stats](structztest__suite__stats.md)

Stats about a ztest suite.

**Definition** ztest\_test.h:127

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Create and register a ztest suite.

Using this macro creates a new test suite. It then creates a struct [ztest\_suite\_node](structztest__suite__node.md "A single node of test suite.") in a specific linker section.

Tests can then be run by calling ztest\_run\_test\_suites(const void \*state) by passing in the current state. See the documentation for ztest\_run\_test\_suites for more info.

Parameters
:   | SUITE\_NAME | The name of the suite |
    | --- | --- |
    | PREDICATE | A function to test against the state and determine if the test should run. |
    | setup\_fn | The setup function to call before running this test suite |
    | before\_fn | The function to call before each unit test in this suite |
    | after\_fn | The function to call after each unit test in this suite |
    | teardown\_fn | The function to call after running all the tests in this suite |

## [◆ ](#ga678b4ae96879c029e6e567a326bbf027)ZTEST\_SUITE\_COUNT

| #define ZTEST\_SUITE\_COUNT   (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Number of registered test suites.

## [◆ ](#ga8777ca60bd21cc128f64833bd7921b9c)ZTEST\_TEST\_COUNT

| #define ZTEST\_TEST\_COUNT   (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Number of registered unit tests.

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

**Definition** kernel.h:194

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

If CONFIG\_USERSPACE is not enabled, this is functionally identical to [ZTEST\_F()](#gacd3ab522e0e5c8a270e86b0cb6bd81b2). The test function takes a single fixture argument of type struct suite##\_fixture\* named fixture.

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

## [◆ ](#ga0f9eeb8ddae455c1e7cc7a388a7b013c)ztest\_suite\_after\_t

| typedef void(\* ztest\_suite\_after\_t) (void \*fixture) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Function to run after each test in this suite.

Parameters
:   | fixture | The test suite's fixture returned from setup() |
    | --- | --- |

## [◆ ](#gac8a204832c267fed047e7707b65be74d)ztest\_suite\_before\_t

| typedef void(\* ztest\_suite\_before\_t) (void \*fixture) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Function to run before each test in this suite.

Parameters
:   | fixture | The test suite's fixture returned from setup() |
    | --- | --- |

## [◆ ](#gad5323aa82773dac33cf0930e9524420c)ztest\_suite\_predicate\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* ztest\_suite\_predicate\_t) (const void \*global\_state) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

An optional predicate function to determine if the test should run.

If NULL, then the test will only run once on the first attempt.

Parameters
:   | global\_state | The current state of the test application. |
    | --- | --- |

Returns
:   True if the suite should be run; false to skip.

## [◆ ](#ga0063907dd70b9eb817ea472162693ee4)ztest\_suite\_setup\_t

| typedef void \*(\* ztest\_suite\_setup\_t) (void) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Setup function to run before running this suite.

Returns
:   Pointer to the data structure that will be used throughout this test suite

## [◆ ](#ga7769b894fdac5283ac949ce8fceea0dd)ztest\_suite\_teardown\_t

| typedef void(\* ztest\_suite\_teardown\_t) (void \*fixture) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Teardown function to run after running this suite.

Parameters
:   | fixture | The test suite's data returned from setup() |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#gaf4dfaad1b5f1059e87f406979769aa26)ztest\_expected\_result

| enum [ztest\_expected\_result](#gaf4dfaad1b5f1059e87f406979769aa26) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

The expected result of a test.

See also
:   [ZTEST\_EXPECT\_FAIL](#gaeaa5b96855dd45e015b9556212f8945a)
:   [ZTEST\_EXPECT\_SKIP](#gacb6f06920e522b9a9f6e7a98f0620f38)

| Enumerator | |
| --- | --- |
| ZTEST\_EXPECTED\_RESULT\_FAIL | Expect a test to fail. |
| ZTEST\_EXPECTED\_RESULT\_SKIP | Expect a test to pass. |

## [◆ ](#ga5dde8913cf45656bca8a48c825a95d59)ztest\_phase

| enum [ztest\_phase](#ga5dde8913cf45656bca8a48c825a95d59) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Each enum member represents a distinct phase of execution for the test binary.

TEST\_PHASE\_FRAMEWORK is active when internal ztest code is executing; the rest refer to corresponding phases of user test code.

| Enumerator | |
| --- | --- |
| TEST\_PHASE\_SETUP |  |
| TEST\_PHASE\_BEFORE |  |
| TEST\_PHASE\_TEST |  |
| TEST\_PHASE\_AFTER |  |
| TEST\_PHASE\_TEARDOWN |  |
| TEST\_PHASE\_FRAMEWORK |  |

## [◆ ](#gac2842295307e7286d256bb179be60b02)ztest\_result

| enum [ztest\_result](#gac2842295307e7286d256bb179be60b02) |
| --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

The result of the current running test.

It's possible that the setup function sets the result to ZTEST\_RESULT\_SUITE\_\* which will apply the failure/skip to every test in the suite.

| Enumerator | |
| --- | --- |
| ZTEST\_RESULT\_PENDING |  |
| ZTEST\_RESULT\_PASS |  |
| ZTEST\_RESULT\_FAIL |  |
| ZTEST\_RESULT\_SKIP |  |
| ZTEST\_RESULT\_SUITE\_SKIP |  |
| ZTEST\_RESULT\_SUITE\_FAIL |  |

## Function Documentation

## [◆ ](#gac6b1f8b820cd682094b7aaeebdaa106e)ztest\_run\_all()

| void ztest\_run\_all | ( | const void \* | *state*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *shuffle*, |
|  |  | int | *suite\_iter*, |
|  |  | int | *case\_iter* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Default entry point for running or listing registered unit tests.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The current state of the machine as it relates to the test executable. |
    | --- | --- |
    | shuffle | Shuffle tests |
    | suite\_iter | Test suite repetitions. |
    | case\_iter | Test case repetitions. |

## [◆ ](#gaafb3cba3a9637839952b2db2486ab88c)ztest\_run\_test\_suites()

| int ztest\_run\_test\_suites | ( | const void \* | *state*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *shuffle*, |
|  |  | int | *suite\_iter*, |
|  |  | int | *case\_iter* ) |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Run the registered unit tests which return true from their predicate function.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The current state of the machine as it relates to the test executable. |
    | --- | --- |
    | shuffle | Shuffle tests |
    | suite\_iter | Test suite repetitions. |
    | case\_iter | Test case repetitions. |

Returns
:   The number of tests that ran.

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

## [◆ ](#ga349fda278dff713debfd2a3b94b8b1eb)ztest\_verify\_all\_test\_suites\_ran()

| void ztest\_verify\_all\_test\_suites\_ran | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

Fails the test if any of the registered tests did not run.

When registering test suites, a pragma function can be provided to determine WHEN the test should run. It is possible that a test suite could be registered but the pragma always prevents it from running. In cases where a test should make sure that ALL suites ran at least once, this function may be called at the end of [test\_main()](ztest_8h.md#a8a4533f287d99bb2d7c24c0e29c9a449). It will cause the test to fail if any suite was registered but never ran.

## Variable Documentation

## [◆ ](#ga3adced2fdda96833e6b1ecbf3d61d446)ztest\_mem\_partition

| | struct [k\_mem\_partition](structk__mem__partition.md) ztest\_mem\_partition | | --- | | extern |
| --- | --- | --- |

`#include <[ztest_test.h](ztest__test_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
