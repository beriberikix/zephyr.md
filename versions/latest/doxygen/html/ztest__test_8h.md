---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ztest__test_8h.html
original_path: doxygen/html/ztest__test_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_test.h File Reference

Zephyr testing framework \_test.
[More...](#details)

`#include <[zephyr/app_memory/app_memdomain.h](app__memdomain_8h_source.md)>`  
`#include <[zephyr/init.h](init_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <syscalls/ztest_test.h>`

[Go to the source code of this file.](ztest__test_8h_source.md)

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
| #define | [ZTEST\_EXPECT\_FAIL](#aeaa5b96855dd45e015b9556212f8945a)(\_suite\_name, \_test\_name) |
|  | Expect a test to fail (mark it passing if it failed). |
| #define | [ZTEST\_EXPECT\_SKIP](#acb6f06920e522b9a9f6e7a98f0620f38)(\_suite\_name, \_test\_name) |
|  | Expect a test to skip (mark it passing if it failed). |
| #define | [ZTEST\_TEST\_COUNT](#a8777ca60bd21cc128f64833bd7921b9c)   (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start) |
| #define | [ZTEST\_SUITE\_COUNT](#a678b4ae96879c029e6e567a326bbf027)   (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start) |
| #define | [ZTEST\_SUITE](#aef8892743e2d47c983efcb61beeedeb3)(SUITE\_NAME, PREDICATE, setup\_fn, before\_fn, after\_fn, teardown\_fn) |
|  | Create and register a ztest suite. |
| #define | [ZTEST\_DMEM](#a2c7d0aa85e7f320d582395c5ded90133)   [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| #define | [ZTEST\_BMEM](#ac3de5965061b1164a8033712c9094e23)   [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| #define | [ZTEST\_SECTION](#a44777f5011728bbff63fe3639c1b4aa8)   [K\_APP\_DMEM\_SECTION](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| #define | [ZTEST](group__ztest__test.md#gac25858f76ea667d07de422a3b489cb15)(suite, fn) |
|  | Create and register a new unit test. |
| #define | [ZTEST\_USER](group__ztest__test.md#ga7121acc7ee00646cacefa773ff9631c8)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_F](group__ztest__test.md#gacd3ab522e0e5c8a270e86b0cb6bd81b2)(suite, fn) |
|  | Define a test function. |
| #define | [ZTEST\_USER\_F](group__ztest__test.md#ga12ccce144e577cac6ba763982ad14def)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_RULE](group__ztest__test.md#ga2a0a5e3b6e8fa1c9a03e7600895d875f)(name, before\_each\_fn, after\_each\_fn) |
|  | Define a test rule that will run before/after each unit test. |
| #define | [ztest\_run\_test\_suite](group__ztest__test.md#ga29557673d07a87d5d4ace36521937848)(suite, shuffle, suite\_iter, case\_iter) |
|  | Run the specified test suite. |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [ztest\_suite\_setup\_t](#a0063907dd70b9eb817ea472162693ee4)) (void) |
|  | Setup function to run before running this suite. |
| typedef void(\* | [ztest\_suite\_before\_t](#ac8a204832c267fed047e7707b65be74d)) (void \*fixture) |
|  | Function to run before each test in this suite. |
| typedef void(\* | [ztest\_suite\_after\_t](#a0f9eeb8ddae455c1e7cc7a388a7b013c)) (void \*fixture) |
|  | Function to run after each test in this suite. |
| typedef void(\* | [ztest\_suite\_teardown\_t](#a7769b894fdac5283ac949ce8fceea0dd)) (void \*fixture) |
|  | Teardown function to run after running this suite. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [ztest\_suite\_predicate\_t](#ad5323aa82773dac33cf0930e9524420c)) (const void \*global\_state) |
|  | An optional predicate function to determine if the test should run. |
| typedef void(\* | [ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162)) (const struct [ztest\_unit\_test](structztest__unit__test.md) \*test, void \*data) |
|  | Test rule callback function signature. |

| Enumerations | |
| --- | --- |
| enum | [ztest\_expected\_result](#af4dfaad1b5f1059e87f406979769aa26) { [ZTEST\_EXPECTED\_RESULT\_FAIL](#af4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) = 0 , [ZTEST\_EXPECTED\_RESULT\_SKIP](#af4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a) } |
|  | The expected result of a test. [More...](#af4dfaad1b5f1059e87f406979769aa26) |
| enum | [ztest\_result](#ac2842295307e7286d256bb179be60b02) {     [ZTEST\_RESULT\_PENDING](#ac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc) , [ZTEST\_RESULT\_PASS](#ac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e) , [ZTEST\_RESULT\_FAIL](#ac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888) , [ZTEST\_RESULT\_SKIP](#ac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4) ,     [ZTEST\_RESULT\_SUITE\_SKIP](#ac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e) , [ZTEST\_RESULT\_SUITE\_FAIL](#ac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)   } |
|  | The result of the current running test. [More...](#ac2842295307e7286d256bb179be60b02) |
| enum | [ztest\_phase](#a5dde8913cf45656bca8a48c825a95d59) {     [TEST\_PHASE\_SETUP](#a5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf) , [TEST\_PHASE\_BEFORE](#a5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765) , [TEST\_PHASE\_TEST](#a5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1) , [TEST\_PHASE\_AFTER](#a5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663) ,     [TEST\_PHASE\_TEARDOWN](#a5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901) , [TEST\_PHASE\_FRAMEWORK](#a5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)   } |
|  | Each enum member represents a distinct phase of execution for the test binary. [More...](#a5dde8913cf45656bca8a48c825a95d59) |

| Functions | |
| --- | --- |
| void | [ztest\_run\_all](#ac6b1f8b820cd682094b7aaeebdaa106e) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Default entry point for running or listing registered unit tests. |
| int | [ztest\_run\_test\_suites](#aafb3cba3a9637839952b2db2486ab88c) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Run the registered unit tests which return true from their predicate function. |
| void | [ztest\_verify\_all\_test\_suites\_ran](#a349fda278dff713debfd2a3b94b8b1eb) (void) |
|  | Fails the test if any of the registered tests did not run. |
| void | [ztest\_test\_fail](group__ztest__test.md#gacd6eb423f54dce8544f7c3b1618c0374) (void) |
|  | Fail the currently running test. |
| void | [ztest\_test\_pass](group__ztest__test.md#ga085d30a04102ebb8c3f2206020723ee0) (void) |
|  | Pass the currently running test. |
| void | [ztest\_test\_skip](group__ztest__test.md#gada3b1fcfa71db1bf7787c03ff45256d5) (void) |
|  | Skip the current test. |
| void | [ztest\_skip\_failed\_assumption](group__ztest__test.md#ga17537c79021fbc12e56b72ccec4b99c5) (void) |
| void | [ztest\_simple\_1cpu\_before](group__ztest__test.md#gac7ddc33b5a0d11e2ffa0a564019c5e3d) (void \*data) |
|  | A 'before' function to use in test suites that just need to start 1cpu. |
| void | [ztest\_simple\_1cpu\_after](group__ztest__test.md#gaa53486873430dd8fa978745d8a1d0686) (void \*data) |
|  | A 'after' function to use in test suites that just need to stop 1cpu. |
| void | [sys\_clock\_tick\_set](#a846fcbfbda9794cba2dcf1c34bd9be1b) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tick) |

| Variables | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446) |

## Detailed Description

Zephyr testing framework \_test.

## Macro Definition Documentation

## [◆ ](#ac3de5965061b1164a8033712c9094e23)ZTEST\_BMEM

| #define ZTEST\_BMEM   [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

## [◆ ](#a2c7d0aa85e7f320d582395c5ded90133)ZTEST\_DMEM

| #define ZTEST\_DMEM   [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

## [◆ ](#aeaa5b96855dd45e015b9556212f8945a)ZTEST\_EXPECT\_FAIL

| #define ZTEST\_EXPECT\_FAIL | ( |  | *\_suite\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_test\_name* ) |

**Value:**

\_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, [ZTEST\_EXPECTED\_RESULT\_FAIL](#af4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d))

[ZTEST\_EXPECTED\_RESULT\_FAIL](#af4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d)

@ ZTEST\_EXPECTED\_RESULT\_FAIL

Expect a test to fail.

**Definition** ztest\_test.h:38

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

## [◆ ](#acb6f06920e522b9a9f6e7a98f0620f38)ZTEST\_EXPECT\_SKIP

| #define ZTEST\_EXPECT\_SKIP | ( |  | *\_suite\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_test\_name* ) |

**Value:**

\_\_ZTEST\_EXPECT(\_suite\_name, \_test\_name, [ZTEST\_EXPECTED\_RESULT\_SKIP](#af4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a))

[ZTEST\_EXPECTED\_RESULT\_SKIP](#af4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a)

@ ZTEST\_EXPECTED\_RESULT\_SKIP

Expect a test to pass.

**Definition** ztest\_test.h:39

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

## [◆ ](#a44777f5011728bbff63fe3639c1b4aa8)ZTEST\_SECTION

| #define ZTEST\_SECTION   [K\_APP\_DMEM\_SECTION](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)([ztest\_mem\_partition](#a3adced2fdda96833e6b1ecbf3d61d446)) |
| --- |

## [◆ ](#aef8892743e2d47c983efcb61beeedeb3)ZTEST\_SUITE

| #define ZTEST\_SUITE | ( |  | *SUITE\_NAME*, |
| --- | --- | --- | --- |
|  |  |  | *PREDICATE*, |
|  |  |  | *setup\_fn*, |
|  |  |  | *before\_fn*, |
|  |  |  | *after\_fn*, |
|  |  |  | *teardown\_fn* ) |

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

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[ztest\_suite\_node](structztest__suite__node.md)

A single node of test suite.

**Definition** ztest\_test.h:178

[ztest\_suite\_stats](structztest__suite__stats.md)

Stats about a ztest suite.

**Definition** ztest\_test.h:115

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Create and register a ztest suite.

Using this macro creates a new test suite (using ztest\_test\_suite). It then creates a struct [ztest\_suite\_node](structztest__suite__node.md "A single node of test suite.") in a specific linker section.

Tests can then be run by calling ztest\_run\_test\_suites(const void \*state) by passing in the current state. See the documentation for ztest\_run\_test\_suites for more info.

Parameters
:   | SUITE\_NAME | The name of the suite (see ztest\_test\_suite for more info) |
    | --- | --- |
    | PREDICATE | A function to test against the state and determine if the test should run. |
    | setup\_fn | The setup function to call before running this test suite |
    | before\_fn | The function to call before each unit test in this suite |
    | after\_fn | The function to call after each unit test in this suite |
    | teardown\_fn | The function to call after running all the tests in this suite |

## [◆ ](#a678b4ae96879c029e6e567a326bbf027)ZTEST\_SUITE\_COUNT

| #define ZTEST\_SUITE\_COUNT   (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start) |
| --- |

## [◆ ](#a8777ca60bd21cc128f64833bd7921b9c)ZTEST\_TEST\_COUNT

| #define ZTEST\_TEST\_COUNT   (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start) |
| --- |

## Typedef Documentation

## [◆ ](#a0f9eeb8ddae455c1e7cc7a388a7b013c)ztest\_suite\_after\_t

| typedef void(\* ztest\_suite\_after\_t) (void \*fixture) |
| --- |

Function to run after each test in this suite.

Parameters
:   | fixture | The test suite's fixture returned from setup() |
    | --- | --- |

## [◆ ](#ac8a204832c267fed047e7707b65be74d)ztest\_suite\_before\_t

| typedef void(\* ztest\_suite\_before\_t) (void \*fixture) |
| --- |

Function to run before each test in this suite.

Parameters
:   | fixture | The test suite's fixture returned from setup() |
    | --- | --- |

## [◆ ](#ad5323aa82773dac33cf0930e9524420c)ztest\_suite\_predicate\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* ztest\_suite\_predicate\_t) (const void \*global\_state) |
| --- |

An optional predicate function to determine if the test should run.

If NULL, then the test will only run once on the first attempt.

Parameters
:   | global\_state | The current state of the test application. |
    | --- | --- |

Returns
:   True if the suite should be run; false to skip.

## [◆ ](#a0063907dd70b9eb817ea472162693ee4)ztest\_suite\_setup\_t

| typedef void \*(\* ztest\_suite\_setup\_t) (void) |
| --- |

Setup function to run before running this suite.

Returns
:   Pointer to the data structure that will be used throughout this test suite

## [◆ ](#a7769b894fdac5283ac949ce8fceea0dd)ztest\_suite\_teardown\_t

| typedef void(\* ztest\_suite\_teardown\_t) (void \*fixture) |
| --- |

Teardown function to run after running this suite.

Parameters
:   | fixture | The test suite's data returned from setup() |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#af4dfaad1b5f1059e87f406979769aa26)ztest\_expected\_result

| enum [ztest\_expected\_result](#af4dfaad1b5f1059e87f406979769aa26) |
| --- |

The expected result of a test.

See also
:   [ZTEST\_EXPECT\_FAIL](#aeaa5b96855dd45e015b9556212f8945a)
:   [ZTEST\_EXPECT\_SKIP](#acb6f06920e522b9a9f6e7a98f0620f38)

| Enumerator | |
| --- | --- |
| ZTEST\_EXPECTED\_RESULT\_FAIL | Expect a test to fail. |
| ZTEST\_EXPECTED\_RESULT\_SKIP | Expect a test to pass. |

## [◆ ](#a5dde8913cf45656bca8a48c825a95d59)ztest\_phase

| enum [ztest\_phase](#a5dde8913cf45656bca8a48c825a95d59) |
| --- |

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

## [◆ ](#ac2842295307e7286d256bb179be60b02)ztest\_result

| enum [ztest\_result](#ac2842295307e7286d256bb179be60b02) |
| --- |

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

## [◆ ](#a846fcbfbda9794cba2dcf1c34bd9be1b)sys\_clock\_tick\_set()

| void sys\_clock\_tick\_set | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *tick* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6b1f8b820cd682094b7aaeebdaa106e)ztest\_run\_all()

| void ztest\_run\_all | ( | const void \* | *state*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *shuffle*, |
|  |  | int | *suite\_iter*, |
|  |  | int | *case\_iter* ) |

Default entry point for running or listing registered unit tests.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The current state of the machine as it relates to the test executable. |
    | --- | --- |
    | shuffle | Shuffle tests |
    | suite\_iter | Test suite repetitions. |
    | case\_iter | Test case repetitions. |

## [◆ ](#aafb3cba3a9637839952b2db2486ab88c)ztest\_run\_test\_suites()

| int ztest\_run\_test\_suites | ( | const void \* | *state*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *shuffle*, |
|  |  | int | *suite\_iter*, |
|  |  | int | *case\_iter* ) |

Run the registered unit tests which return true from their predicate function.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The current state of the machine as it relates to the test executable. |
    | --- | --- |
    | shuffle | Shuffle tests |
    | suite\_iter | Test suite repetitions. |
    | case\_iter | Test case repetitions. |

Returns
:   The number of tests that ran.

## [◆ ](#a349fda278dff713debfd2a3b94b8b1eb)ztest\_verify\_all\_test\_suites\_ran()

| void ztest\_verify\_all\_test\_suites\_ran | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Fails the test if any of the registered tests did not run.

When registering test suites, a pragma function can be provided to determine WHEN the test should run. It is possible that a test suite could be registered but the pragma always prevents it from running. In cases where a test should make sure that ALL suites ran at least once, this function may be called at the end of [test\_main()](ztest_8h.md#a8a4533f287d99bb2d7c24c0e29c9a449). It will cause the test to fail if any suite was registered but never ran.

## Variable Documentation

## [◆ ](#a3adced2fdda96833e6b1ecbf3d61d446)ztest\_mem\_partition

| | struct [k\_mem\_partition](structk__mem__partition.md) ztest\_mem\_partition | | --- | | extern |
| --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_test.h](ztest__test_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
