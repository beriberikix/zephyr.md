---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/test/ztest.html
original_path: develop/test/ztest.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Test Framework

The Zephyr Test Framework (Ztest) provides a simple testing framework intended
to be used during development. It provides basic assertion macros and a generic
test structure.

The framework can be used in two ways, either as a generic framework for
integration testing, or for unit testing specific modules.

## Creating a test suite

Using Ztest to create a test suite is as easy as calling the [`ZTEST_SUITE`](#c.ZTEST_SUITE). The macro
accepts the following arguments:

- `suite_name` - The name of the suite. This name must be unique within a single binary.
- [`ztest_suite_predicate_t`](#c.ztest_suite_predicate_t) - An optional predicate function to allow choosing when the
  test will run. The predicate will get a pointer to the global state passed in through
  [`ztest_run_all()`](#c.ztest_run_all) and should return a boolean to decide if the suite should run.
- [`ztest_suite_setup_t`](#c.ztest_suite_setup_t) - An optional setup function which returns a test fixture. This
  will be called and run once per test suite run.
- [`ztest_suite_before_t`](#c.ztest_suite_before_t) - An optional before function which will run before every single
  test in this suite.
- [`ztest_suite_after_t`](#c.ztest_suite_after_t) - An optional after function which will run after every single
  test in this suite.
- [`ztest_suite_teardown_t`](#c.ztest_suite_teardown_t) - An optional teardown function which will run at the end of
  all the tests in the suite.

Below is an example of a test suite using a predicate:

```c
#include <zephyr/ztest.h>
#include "test_state.h"

static bool predicate(const void *global_state)
{
     return ((const struct test_state*)global_state)->x == 5;
}

ZTEST_SUITE(alternating_suite, predicate, NULL, NULL, NULL, NULL);
```

## Adding tests to a suite

There are 4 macros used to add a test to a suite, they are:

- [`ZTEST`](#c.ZTEST) `(suite_name, test_name)` - Which can be used to add a test by `test_name` to a
  given suite by `suite_name`.
- [`ZTEST_USER`](#c.ZTEST_USER) `(suite_name, test_name)` - Which behaves the same as [`ZTEST`](#c.ZTEST), only
  that when [`CONFIG_USERSPACE`](../../kconfig.md#CONFIG_USERSPACE "CONFIG_USERSPACE") is enabled, then the test will be run in a userspace
  thread.
- [`ZTEST_F`](#c.ZTEST_F) `(suite_name, test_name)` - Which behaves the same as [`ZTEST`](#c.ZTEST), only
  that the test function will already include a variable named `fixture` with the type
  `<suite_name>_fixture`.
- [`ZTEST_USER_F`](#c.ZTEST_USER_F) `(suite_name, test_name)` - Which combines the fixture feature of
  [`ZTEST_F`](#c.ZTEST_F) with the userspace threading for the test.

### Test fixtures

Test fixtures can be used to help simplify repeated test setup operations. In many cases, tests in
the same suite will require some initial setup followed by some form of reset between each test.
This is achieved via fixtures in the following way:

```c
#include <zephyr/ztest.h>

struct my_suite_fixture {
     size_t max_size;
     size_t size;
     uint8_t buff[1];
};

static void *my_suite_setup(void)
{
     /* Allocate the fixture with 256 byte buffer */
   struct my_suite_fixture *fixture = malloc(sizeof(struct my_suite_fixture) + 255);

     zassume_not_null(fixture, NULL);
     fixture->max_size = 256;

     return fixture;
}

static void my_suite_before(void *f)
{
     struct my_suite_fixture *fixture = (struct my_suite_fixture *)f;
     memset(fixture->buff, 0, fixture->max_size);
     fixture->size = 0;
}

static void my_suite_teardown(void *f)
{
   free(f);
}

ZTEST_SUITE(my_suite, NULL, my_suite_setup, my_suite_before, NULL, my_suite_teardown);

ZTEST_F(my_suite, test_feature_x)
{
     zassert_equal(0, fixture->size);
     zassert_equal(256, fixture->max_size);
}
```

Using memory allocated by a test fixture in a userspace thread, such as during execution of
[`ZTEST_USER`](#c.ZTEST_USER) or [`ZTEST_USER_F`](#c.ZTEST_USER_F), requires that memory to be declared userspace
accessible. This is because the fixture memory is owned and initialized by kernel space. The Ztest
framework provides the [`ZTEST_DMEM`](#c.ZTEST_DMEM) and [`ZTEST_BMEM`](#c.ZTEST_BMEM) macros for use of such
user/kernel space shared memory.

## Advanced features

### Test result expectations

Some tests were made to be broken. In cases where the test is expected to fail or skip due to the
nature of the code, it’s possible to annotate the test as such. For example:

> ```c
> #include <zephyr/ztest.h>
>
> ZTEST_SUITE(my_suite, NULL, NULL, NULL, NULL, NULL);
>
> ZTEST_EXPECT_FAIL(my_suite, test_fail);
> ZTEST(my_suite, test_fail)
> {
>   /** This will fail the test */
>   zassert_true(false, NULL);
> }
>
> ZTEST_EXPECT_SKIP(my_suite, test_skip);
> ZTEST(my_suite, test_skip)
> {
>   /** This will skip the test */
>   zassume_true(false, NULL);
> }
> ```

In this example, the above tests should be marked as failed and skipped respectively. Instead,
Ztest will mark both as passed due to the expectation.

### Test rules

Test rules are a way to run the same logic for every test and every suite. There are a lot of cases
where you might want to reset some state for every test in the binary (regardless of which suite is
currently running). As an example, this could be to reset mocks, reset emulators, flush the UART,
etc.:

```c
#include <zephyr/fff.h>
#include <zephyr/ztest.h>

#include "test_mocks.h"

DEFINE_FFF_GLOBALS;

DEFINE_FAKE_VOID_FUN(my_weak_func);

static void fff_reset_rule_before(const struct ztest_unit_test *test, void *fixture)
{
     ARG_UNUSED(test);
     ARG_UNUSED(fixture);

     RESET_FAKE(my_weak_func);
}

ZTEST_RULE(fff_reset_rule, fff_reset_rule_before, NULL);
```

### A custom `test_main`

While the Ztest framework provides a default `test_main()` function, it’s possible that some
applications will want to provide custom behavior. This is particularly true if there’s some global
state that the tests depend on and that state either cannot be replicated or is difficult to
replicate without starting the process over. For example, one such state could be a power sequence.
Assuming there’s a board with several steps in the power-on sequence a test suite can be written
using the `predicate` to control when it would run. In that case, the `test_main()`
function can be written as follows:

```c
#include <zephyr/ztest.h>

#include "my_test.h"

void test_main(void)
{
     struct power_sequence_state state;

     /* Only suites that use a predicate checking for phase == PWR_PHASE_0 will run. */
     state.phase = PWR_PHASE_0;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_1 will run. */
     state.phase = PWR_PHASE_1;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_2 will run. */
     state.phase = PWR_PHASE_2;
     ztest_run_all(&state, false, 1, 1);

     /* Check that all the suites in this binary ran at least once. */
     ztest_verify_all_test_suites_ran();
}
```

## Quick start - Integration testing

A simple working base is located at [samples/subsys/testsuite/integration](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/testsuite/integration).
To make a test application for the **bar** component of **foo**, you should copy the
sample folder to `tests/foo/bar` and edit files there adjusting for your test
application’s purposes.

To build and execute all applicable test scenarios defined in your test application
use the [Twister](twister.md#twister-script) tool, for example:

```shell
./scripts/twister -T tests/foo/bar/
```

To select just one of the test scenarios, run Twister with `--scenario` command:

```shell
./scripts/twister --scenario tests/foo/bar/your.test.scenario.name
```

In the command line above `tests/foo/bar` is the path to your test application and
`your.test.scenario.name` references a test scenario defined in `testcase.yaml`
file, which is like `sample.testing.ztest` in the boilerplate test suite sample.

See [Twister test project diagram](twister.md#twister-test-project-diagram) for more details
on how Twister deals with Ztest application.

The sample contains the following files:

CMakeLists.txt

```cmake
1# SPDX-License-Identifier: Apache-2.0
2
3cmake_minimum_required(VERSION 3.20.0)
4find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
5project(integration)
6
7FILE(GLOB app_sources src/*.c)
8target_sources(app PRIVATE ${app_sources})
```

testcase.yaml

```yaml
 1tests:
 2  # section.subsection
 3  sample.testing.ztest:
 4    build_only: true
 5    platform_allow:
 6      - native_posix
 7      - native_sim
 8    integration_platforms:
 9      - native_sim
10    tags: test_framework
```

prj.conf

```text
1CONFIG_ZTEST=y
```

src/main.c (see [best practices](ztest_deprecated.md#main-c-bp))

```c
 1/*
 2 * Copyright (c) 2016 Intel Corporation
 3 *
 4 * SPDX-License-Identifier: Apache-2.0
 5 */
 6
 7#include <zephyr/ztest.h>
 8
 9
10ZTEST_SUITE(framework_tests, NULL, NULL, NULL, NULL, NULL);
11
12/**
13 * @brief Test Asserts
14 *
15 * This test verifies various assert macros provided by ztest.
16 *
17 */
18ZTEST(framework_tests, test_assert)
19{
20	zassert_true(1, "1 was false");
21	zassert_false(0, "0 was true");
22	zassert_is_null(NULL, "NULL was not NULL");
23	zassert_not_null("foo", "\"foo\" was NULL");
24	zassert_equal(1, 1, "1 was not equal to 1");
25	zassert_equal_ptr(NULL, NULL, "NULL was not equal to NULL");
26}
```

A test application may consist of multiple test suites that
either can be testing functionality or APIs. Functions implementing a test case
should follow the guidelines below:

- Test cases function names should be prefixed with **test\_**
- Test cases should be documented using doxygen
- Test case function names should be unique within the section or component being
  tested

For example:

```c
/**
 * @brief Test Asserts
 *
 * This test case verifies the zassert_true macro.
 */
ZTEST(my_suite, test_assert)
{
        zassert_true(1, "1 was false");
}
```

### [Listing Tests](#contents)

Tests (test applications) in the Zephyr tree consist of many test scenarios that run as
part of a project and test similar functionality, for example an API or a
feature. The `twister` script can parse the test scenarios, suites and cases in all
test applications or a subset of them, and can generate reports on a granular
level, i.e. if test cases have passed or failed or if they were blocked or skipped.

Twister parses the source files looking for test case names, so you
can list all kernel test cases, for example, by running:

```shell
./scripts/twister --list-tests -T tests/kernel
```

### [Skipping Tests](#contents)

Special- or architecture-specific tests cannot run on all
platforms and architectures, however we still want to count those and
report them as being skipped. Because the test inventory and
the list of tests is extracted from the code, adding
conditionals inside the test suite is sub-optimal. Tests that need
to be skipped for a certain platform or feature need to explicitly
report a skip using [`ztest_test_skip()`](#c.ztest_test_skip) or `Z_TEST_SKIP_IFDEF`. If the test runs,
it needs to report either a pass or fail. For example:

```c
#ifdef CONFIG_TEST1
ZTEST(common, test_test1)
{
     zassert_true(1, "true");
}
#else
ZTEST(common, test_test1)
{
     ztest_test_skip();
}
#endif

ZTEST(common, test_test2)
{
     Z_TEST_SKIP_IFDEF(CONFIG_BUGxxxxx);
     zassert_equal(1, 0, NULL);
}

ZTEST_SUITE(common, NULL, NULL, NULL, NULL, NULL);
```

## Quick start - Unit testing

Ztest can be used for unit testing. This means that rather than including the
entire Zephyr OS for testing a single function, you can focus the testing
efforts into the specific module in question. This will speed up testing since
only the module will have to be compiled in, and the tested functions will be
called directly.

Examples of unit tests can be found in the [tests/unit/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/unit/) folder.
In order to declare the unit tests present in a source folder, you need to add
the relevant source files to the `testbinary` target from the CMake
[unittest ](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/unittest.cmake) component. See a minimal
example below:

```cmake
cmake_minimum_required(VERSION 3.20.0)

project(app)
find_package(Zephyr COMPONENTS unittest REQUIRED HINTS $ENV{ZEPHYR_BASE})
target_sources(testbinary PRIVATE main.c)
```

Since you won’t be including basic kernel data structures that most code
depends on, you have to provide function stubs in the test. Ztest provides
some helpers for mocking functions, as demonstrated below.

In a unit test, mock objects can simulate the behavior of complex real objects
and are used to decide whether a test failed or passed by verifying whether an
interaction with an object occurred, and if required, to assert the order of
that interaction.

## Best practices for declaring the test suite

*twister* and other validation tools need to obtain the list of
test cases that a Zephyr *ztest* test image will expose.

Rationale

This all is for the purpose of traceability. It’s not enough to
have only a semaphore test application. We also need to show that we
have testpoints for all APIs and functionality, and we trace back
to documentation of the API, and functional requirements.

The idea is that test reports show results for every test case
as passed, failed, blocked, or skipped. Reporting on only the
high-level test application, particularly when tests do too
many things, is too vague.

Other questions:

- Why not pre-scan with CPP and then parse? or post scan the ELF file?

  If C pre-processing or building fails because of any issue, then we
  won’t be able to tell the subcases.
- Why not declare them in the YAML test configuration?

  A separate test case description file would be harder to maintain
  than just keeping the information in the test source files
  themselves – only one file to update when changes are made
  eliminates duplication.

## Stress test framework

Zephyr stress test framework (Ztress) provides an environment for executing user
functions in multiple priority contexts. It can be used to validate that code is
resilient to preemptions. The framework tracks the number of executions and preemptions
for each context. Execution can have various completion conditions like timeout,
number of executions or number of preemptions.

The framework is setting up the environment by creating the requested number of threads
(each on different priority), optionally starting a timer. For each context, a user
function (different for each context) is called and then the context sleeps for
a randomized amount of system ticks. The framework is tracking CPU load and adjusts sleeping
periods to achieve higher CPU load. In order to increase the probability of preemptions,
the system clock frequency should be relatively high. The default 100 Hz on QEMU x86
is much too low and it is recommended to increase it to 100 kHz.

The stress test environment is setup and executed using [`ZTRESS_EXECUTE`](#c.ZTRESS_EXECUTE) which
accepts a variable number of arguments. Each argument is a context that is
specified by [`ZTRESS_TIMER`](#c.ZTRESS_TIMER) or [`ZTRESS_THREAD`](#c.ZTRESS_THREAD) macros. Contexts
are specified in priority descending order. Each context specifies completion
conditions by providing the minimum number of executions and preemptions. When all
conditions are met and the execution has completed, an execution report is printed
and the macro returns. Note that while the test is executing, a progress report is
periodically printed.

Execution can be prematurely completed by specifying a test timeout ([`ztress_set_timeout()`](#c.ztress_set_timeout))
or an explicit abort ([`ztress_abort()`](#c.ztress_abort)).

User function parameters contains an execution counter and a flag indicating if it is
the last execution.

The example below presents how to setup and run 3 contexts (one of which is k\_timer
interrupt handler context). Completion criteria is set to at least 10000 executions
of each context and 1000 preemptions of the lowest priority context. Additionally,
the timeout is configured to complete after 10 seconds if those conditions are not met.
The last argument of each context is the initial sleep time which will be adjusted throughout
the test to achieve the highest CPU load.

> ```c
> ztress_set_timeout(K_MSEC(10000));
> ZTRESS_EXECUTE(ZTRESS_TIMER(foo_0, user_data_0, 10000, Z_TIMEOUT_TICKS(20)),
>                ZTRESS_THREAD(foo_1, user_data_1, 10000, 0, Z_TIMEOUT_TICKS(20)),
>                ZTRESS_THREAD(foo_2, user_data_2, 10000, 1000, Z_TIMEOUT_TICKS(20)));
> ```

### Configuration

Static configuration of Ztress contains:

> - [`CONFIG_ZTRESS_MAX_THREADS`](../../kconfig.md#CONFIG_ZTRESS_MAX_THREADS "CONFIG_ZTRESS_MAX_THREADS") - number of supported threads.
> - [`CONFIG_ZTRESS_STACK_SIZE`](../../kconfig.md#CONFIG_ZTRESS_STACK_SIZE "CONFIG_ZTRESS_STACK_SIZE") - Stack size of created threads.
> - [`CONFIG_ZTRESS_REPORT_PROGRESS_MS`](../../kconfig.md#CONFIG_ZTRESS_REPORT_PROGRESS_MS "CONFIG_ZTRESS_REPORT_PROGRESS_MS") - Test progress report interval.

## API reference

### Running tests

*group* Ztest testing macros
:   This module eases the testing process by providing helpful macros and other testing structures.

    Defines

    ZTEST\_EXPECT\_FAIL(\_suite\_name, \_test\_name)
    :   Expect a test to fail (mark it passing if it failed).

        Adding this macro to your logic will allow the failing test to be considered passing, example:

        ```text
        ZTEST_EXPECT_FAIL(my_suite, test_x);
        ZTEST(my_suite, text_x) {
          zassert_true(false, NULL);
        }
        ```

        Parameters:
        :   - **\_suite\_name** – The name of the suite
            - **\_test\_name** – The name of the test

    ZTEST\_EXPECT\_SKIP(\_suite\_name, \_test\_name)
    :   Expect a test to skip (mark it passing if it failed).

        Adding this macro to your logic will allow the failing test to be considered passing, example:

        ```text
        ZTEST_EXPECT_SKIP(my_suite, test_x);
        ZTEST(my_suite, text_x) {
          zassume_true(false, NULL);
        }
        ```

        Parameters:
        :   - **\_suite\_name** – The name of the suite
            - **\_test\_name** – The name of the test

    ZTEST\_TEST\_COUNT
    :   Number of registered unit tests.

    ZTEST\_SUITE\_COUNT
    :   Number of registered test suites.

    ZTEST\_SUITE(SUITE\_NAME, PREDICATE, setup\_fn, before\_fn, after\_fn, teardown\_fn)
    :   Create and register a ztest suite.

        Using this macro creates a new test suite. It then creates a struct [ztest\_suite\_node](#structztest__suite__node) in a specific linker section.

        Tests can then be run by calling ztest\_run\_test\_suites(const void \*state) by passing in the current state. See the documentation for ztest\_run\_test\_suites for more info.

        Parameters:
        :   - **SUITE\_NAME** – The name of the suite
            - **PREDICATE** – A function to test against the state and determine if the test should run.
            - **setup\_fn** – The setup function to call before running this test suite
            - **before\_fn** – The function to call before each unit test in this suite
            - **after\_fn** – The function to call after each unit test in this suite
            - **teardown\_fn** – The function to call after running all the tests in this suite

    ZTEST\_DMEM
    :   Make data section used by Ztest userspace accessible.

    ZTEST\_BMEM
    :   Make bss section used by Ztest userspace accessible.

    ZTEST\_SECTION
    :   Ztest data section for accessing data from userspace.

    ZTEST(suite, fn)
    :   Create and register a new unit test.

        Calling this macro will create a new unit test and attach it to the declared `suite`. The `suite` does not need to be defined in the same compilation unit.

        Parameters:
        :   - **suite** – The name of the test suite to attach this test
            - **fn** – The test function to call.

    ZTEST\_USER(suite, fn)
    :   Define a test function that should run as a user thread.

        This macro behaves exactly the same as ZTEST, but calls the test function in user space if `CONFIG_USERSPACE` was enabled.

        Parameters:
        :   - **suite** – The name of the test suite to attach this test
            - **fn** – The test function to call.

    ZTEST\_F(suite, fn)
    :   Define a test function.

        This macro behaves exactly the same as [ZTEST()](#group__ztest__test_1gac25858f76ea667d07de422a3b489cb15), but the function takes an argument for the fixture of type `struct suite##_fixture*` named `fixture`.

        Parameters:
        :   - **suite** – The name of the test suite to attach this test
            - **fn** – The test function to call.

    ZTEST\_USER\_F(suite, fn)
    :   Define a test function that should run as a user thread.

        If CONFIG\_USERSPACE is not enabled, this is functionally identical to [ZTEST\_F()](#group__ztest__test_1gacd3ab522e0e5c8a270e86b0cb6bd81b2). The test function takes a single fixture argument of type `struct suite##_fixture*` named `fixture`.

        Parameters:
        :   - **suite** – The name of the test suite to attach this test
            - **fn** – The test function to call.

    ZTEST\_RULE(name, before\_each\_fn, after\_each\_fn)
    :   Define a test rule that will run before/after each unit test.

        Functions defined here will run before/after each unit test for every test suite. Along with the callback, the test functions are provided a pointer to the test being run, and the data. This provides a mechanism for tests to perform custom operations depending on the specific test or the data (for example logging may use the test’s name).

        Ordering:

        - Test rule’s `before` function will run before the suite’s `before` function. This is done to allow the test suite’s customization to take precedence over the rule which is applied to all suites.
        - Test rule’s `after` function is not guaranteed to run in any particular order.

        Parameters:
        :   - **name** – The name for the test rule (must be unique within the compilation unit)
            - **before\_each\_fn** – The callback function ([ztest\_rule\_cb](#group__ztest__test_1ga2090c493018a95112b89c5f83b5d8162)) to call before each test (may be NULL)
            - **after\_each\_fn** – The callback function ([ztest\_rule\_cb](#group__ztest__test_1ga2090c493018a95112b89c5f83b5d8162)) to call after each test (may be NULL)

    ztest\_run\_test\_suite(suite, shuffle, suite\_iter, case\_iter)
    :   Run the specified test suite.

        Parameters:
        :   - **suite** – Test suite to run.
            - **shuffle** – Shuffle tests
            - **suite\_iter** – Test suite repetitions.
            - **case\_iter** – Test case repetitions.

    Typedefs

    typedef void \*(\*ztest\_suite\_setup\_t)(void)
    :   Setup function to run before running this suite.

        Return:
        :   Pointer to the data structure that will be used throughout this test suite

    typedef void (\*ztest\_suite\_before\_t)(void \*fixture)
    :   Function to run before each test in this suite.

        Param fixture:
        :   The test suite’s fixture returned from setup()

    typedef void (\*ztest\_suite\_after\_t)(void \*fixture)
    :   Function to run after each test in this suite.

        Param fixture:
        :   The test suite’s fixture returned from setup()

    typedef void (\*ztest\_suite\_teardown\_t)(void \*fixture)
    :   Teardown function to run after running this suite.

        Param fixture:
        :   The test suite’s data returned from setup()

    typedef bool (\*ztest\_suite\_predicate\_t)(const void \*global\_state)
    :   An optional predicate function to determine if the test should run.

        If NULL, then the test will only run once on the first attempt.

        Param global\_state:
        :   The current state of the test application.

        Return:
        :   True if the suite should be run; false to skip.

    typedef void (\*ztest\_rule\_cb)(const struct [ztest\_unit\_test](#c.ztest_unit_test) \*test, void \*data)
    :   Test rule callback function signature.

        The function signature that can be used to register a test rule’s before/after callback. This provides access to the test and the fixture data (if provided).

        Param test:
        :   Pointer to the unit test in context

        Param data:
        :   Pointer to the test’s fixture data (may be NULL)

    Enums

    enum ztest\_expected\_result
    :   The expected result of a test.

        See also

        [ZTEST\_EXPECT\_FAIL](#group__ztest__test_1gaeaa5b96855dd45e015b9556212f8945a)

        See also

        [ZTEST\_EXPECT\_SKIP](#group__ztest__test_1gacb6f06920e522b9a9f6e7a98f0620f38)

        *Values:*

        enumerator ZTEST\_EXPECTED\_RESULT\_FAIL = 0
        :   Expect a test to fail.

        enumerator ZTEST\_EXPECTED\_RESULT\_SKIP
        :   Expect a test to pass.

    enum ztest\_result
    :   The result of the current running test.

        It’s possible that the setup function sets the result to ZTEST\_RESULT\_SUITE\_\* which will apply the failure/skip to every test in the suite.

        *Values:*

        enumerator ZTEST\_RESULT\_PENDING

        enumerator ZTEST\_RESULT\_PASS

        enumerator ZTEST\_RESULT\_FAIL

        enumerator ZTEST\_RESULT\_SKIP

        enumerator ZTEST\_RESULT\_SUITE\_SKIP

        enumerator ZTEST\_RESULT\_SUITE\_FAIL

    enum ztest\_phase
    :   Each enum member represents a distinct phase of execution for the test binary.

        TEST\_PHASE\_FRAMEWORK is active when internal ztest code is executing; the rest refer to corresponding phases of user test code.

        *Values:*

        enumerator TEST\_PHASE\_SETUP

        enumerator TEST\_PHASE\_BEFORE

        enumerator TEST\_PHASE\_TEST

        enumerator TEST\_PHASE\_AFTER

        enumerator TEST\_PHASE\_TEARDOWN

        enumerator TEST\_PHASE\_FRAMEWORK

    Functions

    void ztest\_run\_all(const void \*state, bool shuffle, int suite\_iter, int case\_iter)
    :   Default entry point for running or listing registered unit tests.

        Parameters:
        :   - **state** – The current state of the machine as it relates to the test executable.
            - **shuffle** – Shuffle tests
            - **suite\_iter** – Test suite repetitions.
            - **case\_iter** – Test case repetitions.

    int ztest\_run\_test\_suites(const void \*state, bool shuffle, int suite\_iter, int case\_iter)
    :   Run the registered unit tests which return true from their predicate function.

        Parameters:
        :   - **state** – The current state of the machine as it relates to the test executable.
            - **shuffle** – Shuffle tests
            - **suite\_iter** – Test suite repetitions.
            - **case\_iter** – Test case repetitions.

        Returns:
        :   The number of tests that ran.

    void ztest\_verify\_all\_test\_suites\_ran(void)
    :   Fails the test if any of the registered tests did not run.

        When registering test suites, a pragma function can be provided to determine WHEN the test should run. It is possible that a test suite could be registered but the pragma always prevents it from running. In cases where a test should make sure that ALL suites ran at least once, this function may be called at the end of test\_main(). It will cause the test to fail if any suite was registered but never ran.

    void ztest\_test\_fail(void)
    :   Fail the currently running test.

        This is the function called from failed assertions and the like. You probably don’t need to call it yourself.

    void ztest\_test\_pass(void)
    :   Pass the currently running test.

        Normally a test passes just by returning without an assertion failure. However, if the success case for your test involves a fatal fault, you can call this function from k\_sys\_fatal\_error\_handler to indicate that the test passed before aborting the thread.

    void ztest\_test\_skip(void)
    :   Skip the current test.

    void ztest\_skip\_failed\_assumption(void)

    void ztest\_simple\_1cpu\_before(void \*data)
    :   A ‘before’ function to use in test suites that just need to start 1cpu.

        Ignores data, and calls z\_test\_1cpu\_start()

        Parameters:
        :   - **data** – The test suite’s data

    void ztest\_simple\_1cpu\_after(void \*data)
    :   A ‘after’ function to use in test suites that just need to stop 1cpu.

        Ignores data, and calls z\_test\_1cpu\_stop()

        Parameters:
        :   - **data** – The test suite’s data

    Variables

    struct [k\_mem\_partition](../../kernel/usermode/memory_domain.md#c.k_mem_partition "k_mem_partition") ztest\_mem\_partition

    struct ztest\_expected\_result\_entry
    :   *#include <ztest\_test.h>*

        A single expectation entry allowing tests to fail/skip and be considered passing.

        See also

        [ZTEST\_EXPECT\_FAIL](#group__ztest__test_1gaeaa5b96855dd45e015b9556212f8945a)

        See also

        [ZTEST\_EXPECT\_SKIP](#group__ztest__test_1gacb6f06920e522b9a9f6e7a98f0620f38)

        Public Members

        const char \*test\_suite\_name
        :   The test suite’s name for the expectation.

        const char \*test\_name
        :   The test’s name for the expectation.

        enum [ztest\_expected\_result](#c.ztest_expected_result) expected\_result
        :   The expectation.

    struct ztest\_unit\_test
    :   *#include <ztest\_test.h>*

        Public Members

        struct [ztest\_unit\_test\_stats](#c.ztest_unit_test_stats) \*const stats
        :   Stats.

    struct ztest\_suite\_stats
    :   *#include <ztest\_test.h>*

        Stats about a ztest suite.

        Public Members

        uint32\_t run\_count
        :   The number of times that the suite ran.

        uint32\_t skip\_count
        :   The number of times that the suite was skipped.

        uint32\_t fail\_count
        :   The number of times that the suite failed.

    struct ztest\_unit\_test\_stats
    :   *#include <ztest\_test.h>*

        Public Members

        uint32\_t run\_count
        :   The number of times that the test ran.

        uint32\_t skip\_count
        :   The number of times that the test was skipped.

        uint32\_t fail\_count
        :   The number of times that the test failed.

        uint32\_t pass\_count
        :   The number of times that the test passed.

        uint32\_t duration\_worst\_ms
        :   The longest duration of the test across multiple times.

    struct ztest\_suite\_node
    :   *#include <ztest\_test.h>*

        A single node of test suite.

        Each node should be added to a single linker section which will allow [ztest\_run\_test\_suites()](#group__ztest__test_1gaafb3cba3a9637839952b2db2486ab88c) to iterate over the various nodes.

        Public Members

        const char \*const name
        :   The name of the test suite.

        const [ztest\_suite\_setup\_t](#c.ztest_suite_setup_t) setup
        :   Setup function.

        const [ztest\_suite\_before\_t](#c.ztest_suite_before_t) before
        :   Before function.

        const [ztest\_suite\_after\_t](#c.ztest_suite_after_t) after
        :   After function.

        const [ztest\_suite\_teardown\_t](#c.ztest_suite_teardown_t) teardown
        :   Teardown function.

        const [ztest\_suite\_predicate\_t](#c.ztest_suite_predicate_t) predicate
        :   Optional predicate filter.

        struct [ztest\_suite\_stats](#c.ztest_suite_stats) \*const stats
        :   Stats.

    struct ztest\_test\_rule

    struct ztest\_arch\_api
    :   *#include <ztest\_test.h>*

        Structure for architecture specific APIs.

### Assertions

These macros will instantly fail the test if the related assertion fails.
When an assertion fails, it will print the current file, line and function,
alongside a reason for the failure and an optional message. If the config
[`CONFIG_ZTEST_ASSERT_VERBOSE`](../../kconfig.md#CONFIG_ZTEST_ASSERT_VERBOSE "CONFIG_ZTEST_ASSERT_VERBOSE") is 0, the assertions will only print the
file and line numbers, reducing the binary size of the test.

Example output for a failed macro from
`zassert_equal(buf->ref, 2, "Invalid refcount")`:

```text
Assertion failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
Aborted at unit test function
```

*group* Ztest assertion macros
:   This module provides assertions when using Ztest.

    Defines

    zassert(cond, default\_msg, ...)

    zassume(cond, default\_msg, ...)

    zexpect(cond, default\_msg, ...)

    zassert\_unreachable(...)
    :   Assert that this function call won’t be reached.

        Parameters:
        :   - **...** – Optional message and variables to print if the assertion fails

    zassert\_true(cond, ...)
    :   Assert that *cond* is true.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_false(cond, ...)
    :   Assert that *cond* is false.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_ok(cond, ...)
    :   Assert that *cond* is 0 (success).

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_not\_ok(cond, ...)
    :   Assert that *cond* is not 0 (failure).

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_is\_null(ptr, ...)
    :   Assert that *ptr* is NULL.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_not\_null(ptr, ...)
    :   Assert that *ptr* is not NULL.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_equal(a, b, ...)
    :   Assert that *a* equals *b*.

        *a* and *b* won’t be converted and will be compared directly.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_not\_equal(a, b, ...)
    :   Assert that *a* does not equal *b*.

        *a* and *b* won’t be converted and will be compared directly.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_equal\_ptr(a, b, ...)
    :   Assert that *a* equals *b*.

        *a* and *b* will be converted to `void *` before comparing.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_within(a, b, d, ...)
    :   Assert that *a* is within *b* with delta *d*.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **d** – Delta
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_between\_inclusive(a, l, u, ...)
    :   Assert that *a* is greater than or equal to *l* and less than or equal to *u*.

        Parameters:
        :   - **a** – Value to compare
            - **l** – Lower limit
            - **u** – Upper limit
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_mem\_equal(...)
    :   Assert that 2 memory buffers have the same contents.

        This macro calls the final memory comparison assertion macro. Using double expansion allows providing some arguments by macros that would expand to more than one values (ANSI-C99 defines that all the macro arguments have to be expanded before macro call).

        Parameters:
        :   - **...** – Arguments, see [zassert\_mem\_equal\_\_](#group__ztest__assert_1ga30e5fefa185944d3e949d4023c2eea27) for real arguments accepted.

    zassert\_mem\_equal\_\_(buf, exp, size, ...)
    :   Internal assert that 2 memory buffers have the same contents.

        Note

        This is internal macro, to be used as a second expansion. See [zassert\_mem\_equal](#group__ztest__assert_1gabbfcf6345172387326d35b5d0e2bb051).

        Parameters:
        :   - **buf** – Buffer to compare
            - **exp** – Buffer with expected contents
            - **size** – Size of buffers
            - **...** – Optional message and variables to print if the assertion fails

    zassert\_str\_equal(s1, s2, ...)
    :   Assert that 2 strings have the same contents.

        Parameters:
        :   - **s1** – The first string
            - **s2** – The second string
            - **...** – Optional message and variables to print if the expectation fails

### Expectations

These macros will continue test execution if the related expectation fails and subsequently fail the
test at the end of its execution. When an expectation fails, it will print the current file, line,
and function, alongside a reason for the failure and an optional message but continue executing the
test. If the config [`CONFIG_ZTEST_ASSERT_VERBOSE`](../../kconfig.md#CONFIG_ZTEST_ASSERT_VERBOSE "CONFIG_ZTEST_ASSERT_VERBOSE") is 0, the expectations will only print the
file and line numbers, reducing the binary size of the test.

For example, if the following expectations fail:

```c
zexpect_equal(buf->ref, 2, "Invalid refcount");
zexpect_equal(buf->ref, 1337, "Invalid refcount");
```

The output will look something like:

```text
START - test_get_single_buffer
    Expectation failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
    Expectation failed at main.c:63: test_get_single_buffer: Invalid refcount (buf->ref not equal to 1337)
 FAIL - test_get_single_buffer in 0.0 seconds
```

*group* Ztest expectation macros
:   This module provides expectations when using Ztest.

    Defines

    zexpect\_true(cond, ...)
    :   Expect that *cond* is true, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_false(cond, ...)
    :   Expect that *cond* is false, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_ok(cond, ...)
    :   Expect that *cond* is 0 (success), otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_not\_ok(cond, ...)
    :   Expect that *cond* is not 0 (failure), otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_is\_null(ptr, ...)
    :   Expect that *ptr* is NULL, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_not\_null(ptr, ...)
    :   Expect that *ptr* is not NULL, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_equal(a, b, ...)
    :   Expect that *a* equals *b*, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_not\_equal(a, b, ...)
    :   Expect that *a* does not equal *b*, otherwise mark test as failed but continue its execution.

        *a* and *b* won’t be converted and will be compared directly.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_equal\_ptr(a, b, ...)
    :   Expect that *a* equals *b*, otherwise mark test as failed but continue its execution.

        *a* and *b* will be converted to `void *` before comparing.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_within(a, b, delta, ...)
    :   Expect that *a* is within *b* with delta *d*, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **delta** – Difference between a and b
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_between\_inclusive(a, lower, upper, ...)
    :   Expect that *a* is greater than or equal to *l* and less than or equal to *u*, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **a** – Value to compare
            - **lower** – Lower limit
            - **upper** – Upper limit
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_mem\_equal(buf, exp, size, ...)
    :   Expect that 2 memory buffers have the same contents, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **buf** – Buffer to compare
            - **exp** – Buffer with expected contents
            - **size** – Size of buffers
            - **...** – Optional message and variables to print if the expectation fails

    zexpect\_str\_equal(s1, s2, ...)
    :   Expect that 2 strings have the same contents, otherwise mark test as failed but continue its execution.

        Parameters:
        :   - **s1** – The first string
            - **s2** – The second string
            - **...** – Optional message and variables to print if the expectation fails

### Assumptions

These macros will instantly skip the test or suite if the related assumption fails.
When an assumption fails, it will print the current file, line, and function,
alongside a reason for the failure and an optional message. If the config
[`CONFIG_ZTEST_ASSERT_VERBOSE`](../../kconfig.md#CONFIG_ZTEST_ASSERT_VERBOSE "CONFIG_ZTEST_ASSERT_VERBOSE") is 0, the assumptions will only print the
file and line numbers, reducing the binary size of the test.

Example output for a failed macro from
`zassume_equal(buf->ref, 2, "Invalid refcount")`:

*group* Ztest assumption macros
:   This module provides assumptions when using Ztest.

    Defines

    zassume\_true(cond, ...)
    :   Assume that *cond* is true.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_false(cond, ...)
    :   Assume that *cond* is false.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_ok(cond, ...)
    :   Assume that *cond* is 0 (success).

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_not\_ok(cond, ...)
    :   Assume that *cond* is not 0 (failure).

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **cond** – Condition to check
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_is\_null(ptr, ...)
    :   Assume that *ptr* is NULL.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_not\_null(ptr, ...)
    :   Assume that *ptr* is not NULL.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **ptr** – Pointer to compare
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_equal(a, b, ...)
    :   Assume that *a* equals *b*.

        *a* and *b* won’t be converted and will be compared directly. If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_not\_equal(a, b, ...)
    :   Assume that *a* does not equal *b*.

        *a* and *b* won’t be converted and will be compared directly. If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_equal\_ptr(a, b, ...)
    :   Assume that *a* equals *b*.

        *a* and *b* will be converted to `void *` before comparing. If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_within(a, b, d, ...)
    :   Assume that *a* is within *b* with delta *d*.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **a** – Value to compare
            - **b** – Value to compare
            - **d** – Delta
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_between\_inclusive(a, l, u, ...)
    :   Assume that *a* is greater than or equal to *l* and less than or equal to *u*.

        If the assumption fails, the test will be marked as “skipped”.

        Parameters:
        :   - **a** – Value to compare
            - **l** – Lower limit
            - **u** – Upper limit
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_mem\_equal(...)
    :   Assume that 2 memory buffers have the same contents.

        This macro calls the final memory comparison assumption macro. Using double expansion allows providing some arguments by macros that would expand to more than one values (ANSI-C99 defines that all the macro arguments have to be expanded before macro call).

        Parameters:
        :   - **...** – Arguments, see [zassume\_mem\_equal\_\_](#group__ztest__assume_1gaaed6045f194ead4ffe1dd72a6fa5175d) for real arguments accepted.

    zassume\_mem\_equal\_\_(buf, exp, size, ...)
    :   Internal assume that 2 memory buffers have the same contents.

        If the assumption fails, the test will be marked as “skipped”.

        Note

        This is internal macro, to be used as a second expansion. See [zassume\_mem\_equal](#group__ztest__assume_1ga62be45256399530167745e71226e4a37).

        Parameters:
        :   - **buf** – Buffer to compare
            - **exp** – Buffer with expected contents
            - **size** – Size of buffers
            - **...** – Optional message and variables to print if the assumption fails

    zassume\_str\_equal(s1, s2, ...)
    :   Assumes that 2 strings have the same contents.

        Parameters:
        :   - **s1** – The first string
            - **s2** – The second string
            - **...** – Optional message and variables to print if the expectation fails

### Ztress

*group* Ztest ztress macros
:   This module provides test stress when using Ztest.

    Defines

    ZTRESS\_TIMER(handler, user\_data, exec\_cnt, init\_timeout)
    :   Descriptor of a k\_timer handler execution context.

        The handler is executed in the k\_timer handler context which typically means interrupt context. This context will preempt any other used in the set.

        Note

        There can only be up to one k\_timer context in the set and it must be the first argument of [ZTRESS\_EXECUTE](#group__ztest__ztress_1ga6acc3a50e0eff7360873006482f5c8e9).

        Parameters:
        :   - **handler** – User handler of type [ztress\_handler](#group__ztest__ztress_1ga633439263754bf08baee06c37dddab40).
            - **user\_data** – User data passed to the `handler`.
            - **exec\_cnt** – Number of handler executions to complete the test. If 0 then this is not included in completion criteria.
            - **init\_timeout** – Initial backoff time base (given in [k\_timeout\_t](../../kernel/services/timing/clocks.md#structk__timeout__t)). It is adjusted during the test to optimize CPU load. The actual timeout used for the timer is randomized.

    ZTRESS\_THREAD(handler, user\_data, exec\_cnt, preempt\_cnt, init\_timeout)
    :   Descriptor of a thread execution context.

        The handler is executed in the thread context. The priority of the thread is determined based on the order in which contexts are listed in [ZTRESS\_EXECUTE](#group__ztest__ztress_1ga6acc3a50e0eff7360873006482f5c8e9).

        Note

        thread sleeps for random amount of time. Additionally, the thread busy-waits for a random length of time to further increase randomization in the test.

        Parameters:
        :   - **handler** – User handler of type [ztress\_handler](#group__ztest__ztress_1ga633439263754bf08baee06c37dddab40).
            - **user\_data** – User data passed to the `handler`.
            - **exec\_cnt** – Number of handler executions to complete the test. If 0 then this is not included in completion criteria.
            - **preempt\_cnt** – Number of preemptions of that context to complete the test. If 0 then this is not included in completion criteria.
            - **init\_timeout** – Initial backoff time base (given in [k\_timeout\_t](../../kernel/services/timing/clocks.md#structk__timeout__t)). It is adjusted during the test to optimize CPU load. The actual timeout used for sleeping is randomized.

    ZTRESS\_CONTEXT\_INITIALIZER(\_handler, \_user\_data, \_exec\_cnt, \_preempt\_cnt, \_t)
    :   Initialize context structure.

        For argument types see [ztress\_context\_data](#structztress__context__data). For more details see [ZTRESS\_THREAD](#group__ztest__ztress_1gaed561641541e8ced6866f2f1227f21c0).

        Parameters:
        :   - **\_handler** – Handler.
            - **\_user\_data** – User data passed to the handler.
            - **\_exec\_cnt** – Execution count limit.
            - **\_preempt\_cnt** – Preemption count limit.
            - **\_t** – Initial timeout.

    ZTRESS\_EXECUTE(...)
    :   Setup and run stress test.

        It initialises all contexts and calls [ztress\_execute](#group__ztest__ztress_1gaf706f1af4c42f5925d7545dadf5548fd).

        Parameters:
        :   - **...** – List of contexts. Contexts are configured using [ZTRESS\_TIMER](#group__ztest__ztress_1gabab05b8db44a7024ce23cb34bf999e42) and [ZTRESS\_THREAD](#group__ztest__ztress_1gaed561641541e8ced6866f2f1227f21c0) macros. [ZTRESS\_TIMER](#group__ztest__ztress_1gabab05b8db44a7024ce23cb34bf999e42) must be the first argument if used. Each thread context has an assigned priority. The priority is assigned in a descending order (first listed thread context has the highest priority). The maximum number of supported thread contexts, including the timer context, is configurable in Kconfig (ZTRESS\_MAX\_THREADS).

    Typedefs

    typedef bool (\*ztress\_handler)(void \*user\_data, uint32\_t cnt, bool last, int prio)
    :   User handler called in one of the configured contexts.

        Param user\_data:
        :   User data provided in the context descriptor.

        Param cnt:
        :   Current execution counter. Counted from 0.

        Param last:
        :   Flag set to true indicates that it is the last execution because completion criteria are met, test timed out or was aborted.

        Param prio:
        :   Context priority counting from 0 which indicates the highest priority.

        Retval true:
        :   continue test.

        Retval false:
        :   stop executing the current context.

    Functions

    int ztress\_execute(struct [ztress\_context\_data](#c.ztress_context_data) \*timer\_data, struct [ztress\_context\_data](#c.ztress_context_data) \*thread\_data, size\_t cnt)
    :   Execute contexts.

        The test runs until all completion requirements are met or until the test times out (use [ztress\_set\_timeout](#group__ztest__ztress_1ga5b3069bb2aa35ddc64c46c18d2e30091) to configure timeout) or until the test is aborted ([ztress\_abort](#group__ztest__ztress_1ga57f171e230fba462b3dea6b2d3cf71f6)).

        on test completion a report is printed ([ztress\_report](#group__ztest__ztress_1gaf4db2092eee17d863c9810333ba4c870) is called internally).

        Parameters:
        :   - **timer\_data** – Timer context. NULL if timer context is not used.
            - **thread\_data** – List of thread contexts descriptors in priority descending order.
            - **cnt** – Number of thread contexts.

        Return values:
        :   - **-EINVAL** – If configuration is invalid.
            - **0** – if test is successfully performed.

    void ztress\_abort(void)
    :   Abort ongoing stress test.

    void ztress\_set\_timeout([k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") t)
    :   Set test timeout.

        Test is terminated after timeout disregarding completion criteria. Setting is persistent between executions.

        Parameters:
        :   - **t** – Timeout.

    void ztress\_report(void)
    :   Print last test report.

        Report contains number of executions and preemptions for each context, initial and adjusted timeouts and CPU load during the test.

    int ztress\_exec\_count(uint32\_t id)
    :   Get number of executions of a given context in the last test.

        Parameters:
        :   - **id** – Context id. 0 means the highest priority.

        Returns:
        :   Number of executions.

    int ztress\_preempt\_count(uint32\_t id)
    :   Get number of preemptions of a given context in the last test.

        Parameters:
        :   - **id** – Context id. 0 means the highest priority.

        Returns:
        :   Number of preemptions.

    uint32\_t ztress\_optimized\_ticks(uint32\_t id)
    :   Get optimized timeout base of a given context in the last test.

        Optimized value can be used to update initial value. It will improve the test since optimal CPU load will be reach immediately.

        Parameters:
        :   - **id** – Context id. 0 means the highest priority.

        Returns:
        :   Optimized timeout base.

    struct ztress\_context\_data
    :   *#include <ztress.h>*

### Mocking via FFF

Zephyr has integrated with FFF for mocking. See [FFF](https://github.com/meekrosoft/fff) for documentation. To use it,
include the relevant header:

```c
#include <zephyr/fff.h>
```

Zephyr provides several FFF-based fake drivers which can be used as either stubs or mocks. Fake
driver instances are configured via [Devicetree](../../build/dts/index.md#devicetree) and [Configuration System (Kconfig)](../../build/kconfig/index.md#kconfig). See the following
devicetree bindings for more information:

> - [`zephyr,fake-can`](../../build/dts/api/bindings/can/zephyr%2Cfake-can.md#std-dtcompatible-zephyr-fake-can)
> - [`zephyr,fake-eeprom`](../../build/dts/api/bindings/mtd/zephyr%2Cfake-eeprom.md#std-dtcompatible-zephyr-fake-eeprom)

Zephyr also has defined extensions to FFF for simplified declarations of fake functions.
See [FFF Extensions](#fff-extensions).

## Customizing Test Output

Customization is enabled by setting [`CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE`](../../kconfig.md#CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE "CONFIG_ZTEST_TC_UTIL_USER_OVERRIDE") to “y”
and adding a file `tc_util_user_override.h` with your overrides.

Add the line `zephyr_include_directories(my_folder)` to
your project’s `CMakeLists.txt` to let Zephyr find your header file during builds.

See the file [subsys/testsuite/include/zephyr/tc\_util.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/testsuite/include/zephyr/tc_util.h) to see
which macros and/or defines can be overridden.
These will be surrounded by blocks such as:

```c
#ifndef SOMETHING
#define SOMETHING <default implementation>
#endif /* SOMETHING */
```

## Shuffling Test Sequence

By default the tests are sorted and ran in alphanumerical order. Test cases may
be dependent on this sequence. Enable [`CONFIG_ZTEST_SHUFFLE`](../../kconfig.md#CONFIG_ZTEST_SHUFFLE "CONFIG_ZTEST_SHUFFLE") to
randomize the order. The output from the test will display the seed for failed
tests. For native simulator builds you can provide the seed as an argument to
twister with –seed

Static configuration of ZTEST\_SHUFFLE contains:

> - [`CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT`](../../kconfig.md#CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT "CONFIG_ZTEST_SHUFFLE_SUITE_REPEAT_COUNT") - Number of iterations the test suite will run.
> - [`CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT`](../../kconfig.md#CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT "CONFIG_ZTEST_SHUFFLE_TEST_REPEAT_COUNT") - Number of iterations the test will run.

## Test Selection

For tests built for native simulator, use command line arguments to list
or select tests to run. The test argument expects a comma separated list
of `suite::test` . You can substitute the test name with an `*` to run all
tests within a suite.

For example

```shell
$ zephyr.exe -list
$ zephyr.exe -test="fixture_tests::test_fixture_pointer,framework_tests::test_assert_mem_equal"
$ zephyr.exe -test="framework_tests::*"
```

## FFF Extensions

*group* FFF extensions
:   This module provides extensions to FFF for simplifying the configuration and usage of fakes.

    Defines

    RETURN\_HANDLED\_CONTEXT(FUNCNAME, CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY)
    :   Wrap custom fake body to extract defined context struct.

        Add extension macro for simplified creation of fake functions needing call-specific context data.

        This macro enables a fake to be implemented as follows and requires no familiarity with the inner workings of FFF.

        ```text
        struct FUNCNAME##_custom_fake_context
        {
            struct instance * const instance;
            int result;
        };

        int FUNCNAME##_custom_fake(
            const struct instance **instance_out)
        {
            RETURN_HANDLED_CONTEXT(
                FUNCNAME,
                struct FUNCNAME##_custom_fake_context,
                result,
                context,
                {
                    if (context != NULL)
                    {
                        if (context->result == 0)
                        {
                            if (instance_out != NULL)
                            {
                                *instance_out = context->instance;
                            }
                        }
                        return context->result;
                    }
                    return FUNCNAME##_fake.return_val;
                }
            );
        }
        ```

        Parameters:
        :   - **FUNCNAME** – Name of function being faked
            - **CONTEXTTYPE** – type of custom defined fake context struct
            - **RESULTFIELD** – name of field holding the return type & value
            - **CONTEXTPTRNAME** – expected name of pointer to custom defined fake context struct
            - **HANDLERBODY** – in-line custom fake handling logic
