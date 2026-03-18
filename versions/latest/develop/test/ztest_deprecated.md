---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/test/ztest_deprecated.html
original_path: develop/test/ztest_deprecated.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ZTest Deprecated APIs

Ztest is currently being migrated to a new API, this documentation provides information about the
deprecated APIs which will eventually be removed. See [Test Framework](ztest.md#test-framework) for the new API.
Similarly, ZTest’s mocking framework is also deprecated (see [Mocking via FFF](ztest.md#mocking-fff)).

## Quick start - Unit testing

Ztest can be used for unit testing. This means that rather than including the
entire Zephyr OS for testing a single function, you can focus the testing
efforts into the specific module in question. This will speed up testing since
only the module will have to be compiled in, and the tested functions will be
called directly.

Since you won’t be including basic kernel data structures that most code
depends on, you have to provide function stubs in the test. Ztest provides
some helpers for mocking functions, as demonstrated below.

In a unit test, mock objects can simulate the behavior of complex real objects
and are used to decide whether a test failed or passed by verifying whether an
interaction with an object occurred, and if required, to assert the order of
that interaction.

### Best practices for declaring the test suite

*twister* and other validation tools need to obtain the list of
subcases that a Zephyr *ztest* test image will expose.

Rationale

This all is for the purpose of traceability. It’s not enough to
have only a semaphore test project. We also need to show that we
have testpoints for all APIs and functionality, and we trace back
to documentation of the API, and functional requirements.

The idea is that test reports show results for every sub-testcase
as passed, failed, blocked, or skipped. Reporting on only the
high-level test project level, particularly when tests do too
many things, is too vague.

There exist two alternatives to writing tests. The first, and more verbose,
approach is to directly declare and run the test suites.
Here is a generic template for a test showing the expected use of
`ztest_test_suite()`:

```c
#include <zephyr/ztest.h>

extern void test_sometest1(void);
extern void test_sometest2(void);
#ifndef CONFIG_WHATEVER              /* Conditionally skip test_sometest3 */
void test_sometest3(void)
{
     ztest_test_skip();
}
#else
extern void test_sometest3(void);
#endif
extern void test_sometest4(void);
...

void test_main(void)
{
     ztest_test_suite(common,
                         ztest_unit_test(test_sometest1),
                         ztest_unit_test(test_sometest2),
                         ztest_unit_test(test_sometest3),
                         ztest_unit_test(test_sometest4)
                );
     ztest_run_test_suite(common);
}
```

Alternatively, it is possible to split tests across multiple files using
`ztest_register_test_suite()` which bypasses the need for `extern`:

```c
#include <zephyr/ztest.h>

void test_sometest1(void) {
      zassert_true(1, "true");
}

ztest_register_test_suite(common, NULL,
                          ztest_unit_test(test_sometest1)
                          );
```

The above sample simple registers the test suite and uses a `NULL` pragma
function (more on that later). It is important to note that the test suite isn’t
directly run in this file. Instead two alternatives exist for running the suite.
First, if to do nothing. A default `test_main` function is provided by
ztest. This is the preferred approach if the test doesn’t involve a state and
doesn’t require use of the pragma.

In cases of an integration test it is possible that some general state needs to
be set between test suites. This can be thought of as a state diagram in which
`test_main` simply goes through various actions that modify the board’s
state and different test suites need to run. This is achieved in the following:

```c
#include <zephyr/ztest.h>

struct state {
      bool is_hibernating;
      bool is_usb_connected;
}

static bool pragma_always(const void *state)
{
      return true;
}

static bool pragma_not_hibernating_not_connected(const void *s)
{
      struct state *state = s;
      return !state->is_hibernating && !state->is_usb_connected;
}

static bool pragma_usb_connected(const void *s)
{
      return ((struct state *)s)->is_usb_connected;
}

ztest_register_test_suite(baseline, pragma_always,
                          ztest_unit_test(test_case0));
ztest_register_test_suite(before_usb, pragma_not_hibernating_not_connected,
                          ztest_unit_test(test_case1),
                          ztest_unit_test(test_case2));
ztest_register_test_suite(with_usb, pragma_usb_connected,,
                          ztest_unit_test(test_case3),
                          ztest_unit_test(test_case4));

void test_main(void)
{
      struct state state;

      /* Should run `baseline` test suite only. */
      ztest_run_registered_test_suites(&state);

      /* Simulate power on and update state. */
      emulate_power_on();
      /* Should run `baseline` and `before_usb` test suites. */
      ztest_run_registered_test_suites(&state);

      /* Simulate plugging in a USB device. */
      emulate_plugging_in_usb();
      /* Should run `baseline` and `with_usb` test suites. */
      ztest_run_registered_test_suites(&state);

      /* Verify that all the registered test suites actually ran. */
      ztest_verify_all_registered_test_suites_ran();
}
```

For *twister* to parse source files and create a list of subcases,
the declarations of `ztest_test_suite()` and
`ztest_register_test_suite()` must follow a few rules:

- one declaration per line
- conditional execution by using [`ztest_test_skip()`](ztest.md#c.ztest_test_skip "ztest_test_skip")

What to avoid:

- packing multiple testcases in one source file

  ```c
  void test_main(void)
  {
  #ifdef TEST_feature1
          ztest_test_suite(feature1,
                           ztest_unit_test(test_1a),
                           ztest_unit_test(test_1b),
                           ztest_unit_test(test_1c)
                           );
          ztest_run_test_suite(feature1);
  #endif

  #ifdef TEST_feature2
          ztest_test_suite(feature2,
                           ztest_unit_test(test_2a),
                           ztest_unit_test(test_2b)
                           );
          ztest_run_test_suite(feature2);
  #endif
  }
  ```
- Do not use `#if`

  ```c
          ztest_test_suite(common,
                           ztest_unit_test(test_sometest1),
                           ztest_unit_test(test_sometest2),
  #ifdef CONFIG_WHATEVER
                           ztest_unit_test(test_sometest3),
  #endif
                           ztest_unit_test(test_sometest4),
          ...
  ```
- Do not add comments on lines with a call to `ztest_unit_test()`:

  ```c
  ztest_test_suite(common,
                   ztest_unit_test(test_sometest1),
                   ztest_unit_test(test_sometest2) /* will fail */,
  /* will fail! */ ztest_unit_test(test_sometest3),
                   ztest_unit_test(test_sometest4),
  ...
  ```
- Do not define multiple definitions of unit / user unit test case per
  line

  ```c
  ztest_test_suite(common,
                   ztest_unit_test(test_sometest1), ztest_unit_test(test_sometest2),
                   ztest_unit_test(test_sometest3),
                   ztest_unit_test(test_sometest4),
  ...
  ```

Other questions:

- Why not pre-scan with CPP and then parse? or post scan the ELF file?

  If C pre-processing or building fails because of any issue, then we
  won’t be able to tell the subcases.
- Why not declare them in the YAML testcase description?

  A separate testcase description file would be harder to maintain
  than just keeping the information in the test source files
  themselves – only one file to update when changes are made
  eliminates duplication.

## Mocking

These functions allow abstracting callbacks and related functions and
controlling them from specific tests. You can enable the mocking framework by
setting [`CONFIG_ZTEST_MOCKING`](../../kconfig.md#CONFIG_ZTEST_MOCKING "CONFIG_ZTEST_MOCKING") to “y” in the configuration file of the
test. The amount of concurrent return values and expected parameters is
limited by [`CONFIG_ZTEST_PARAMETER_COUNT`](../../kconfig.md#CONFIG_ZTEST_PARAMETER_COUNT "CONFIG_ZTEST_PARAMETER_COUNT").

Here is an example for configuring the function `expect_two_parameters` to
expect the values `a=2` and `b=3`, and telling `returns_int` to return
`5`:

```c
 1#include <zephyr/ztest.h>
 2
 3static void expect_two_parameters(int a, int b)
 4{
 5	ztest_check_expected_value(a);
 6	ztest_check_expected_value(b);
 7}
 8
 9static void parameter_tests(void)
10{
11	ztest_expect_value(expect_two_parameters, a, 2);
12	ztest_expect_value(expect_two_parameters, b, 3);
13	expect_two_parameters(2, 3);
14}
15
16static int returns_int(void)
17{
18	return ztest_get_return_value();
19}
20
21static void return_value_tests(void)
22{
23	ztest_returns_value(returns_int, 5);
24	zassert_equal(returns_int(), 5, NULL);
25}
26
27void test_main(void)
28{
29	ztest_test_suite(mock_framework_tests,
30		ztest_unit_test(parameter_test),
31		ztest_unit_test(return_value_test)
32	);
33
34	ztest_run_test_suite(mock_framework_tests);
35}
```

*group* ztest\_mock
:   This module provides simple mocking functions for unit testing.

    These need CONFIG\_ZTEST\_MOCKING=y.

    Defines

    ztest\_expect\_value(func, param, value)
    :   Tell function *func* to expect the value *value* for *param*.

        When using [ztest\_check\_expected\_value()](#group__ztest__mock_1gae9af6ba8e51738e938763c896f17ea8f), tell that the value of *param* should be *value*. The value will internally be stored as an `uintptr_t`.

        Parameters:
        :   - **func** – Function in question
            - **param** – Parameter for which the value should be set
            - **value** – Value for *param*

    ztest\_check\_expected\_value(param)
    :   If *param* doesn’t match the value set by [ztest\_expect\_value()](#group__ztest__mock_1ga58c2f0c0e628e73a2268a3d18b0440d6), fail the test.

        This will first check that does *param* have a value to be expected, and then checks whether the value of the parameter is equal to the expected value. If either of these checks fail, the current test will fail. This must be called from the called function.

        Parameters:
        :   - **param** – Parameter to check

    ztest\_expect\_data(func, param, data)
    :   Tell function *func* to expect the data *data* for *param*.

        When using [ztest\_check\_expected\_data()](#group__ztest__mock_1ga805cf99272f147beeeee5ad6ca2553f5), the data pointed to by *param* should be same *data* in this function. Only data pointer is stored by this function, so it must still be valid when ztest\_check\_expected\_data is called.

        Parameters:
        :   - **func** – Function in question
            - **param** – Parameter for which the data should be set
            - **data** – pointer for the data for parameter *param*

    ztest\_check\_expected\_data(param, length)
    :   If data pointed by *param* don’t match the data set by [ztest\_expect\_data()](#group__ztest__mock_1gac1a64d8bf9c877e8666e0c6d93b0dbab), fail the test.

        This will first check that *param* is expected to be null or non-null and then check whether the data pointed by parameter is equal to expected data. If either of these checks fail, the current test will fail. This must be called from the called function.

        Parameters:
        :   - **param** – Parameter to check
            - **length** – Length of the data to compare

    ztest\_return\_data(func, param, data)
    :   Tell function *func* to return the data *data* for *param*.

        When using [ztest\_return\_data()](#group__ztest__mock_1gac79d097a6b274b25286f2b0e80fbd6e9), the data pointed to by *param* should be same *data* in this function. Only data pointer is stored by this function, so it must still be valid when ztest\_copy\_return\_data is called.

        Parameters:
        :   - **func** – Function in question
            - **param** – Parameter for which the data should be set
            - **data** – pointer for the data for parameter *param*

    ztest\_copy\_return\_data(param, length)
    :   Copy the data set by ztest\_return\_data to the memory pointed by *param*.

        This will first check that *param* is not null and then copy the data. This must be called from the called function.

        Parameters:
        :   - **param** – Parameter to return data for
            - **length** – Length of the data to return

    ztest\_returns\_value(func, value)
    :   Tell *func* that it should return *value*.

        Parameters:
        :   - **func** – Function that should return *value*
            - **value** – Value to return from *func*

    ztest\_get\_return\_value()
    :   Get the return value for current function.

        The return value must have been set previously with [ztest\_returns\_value()](#group__ztest__mock_1ga2ec539b4c0f3e4efb695213b4fd08c2c). If no return value exists, the current test will fail.

        Returns:
        :   The value the current function should return

    ztest\_get\_return\_value\_ptr()
    :   Get the return value as a pointer for current function.

        The return value must have been set previously with [ztest\_returns\_value()](#group__ztest__mock_1ga2ec539b4c0f3e4efb695213b4fd08c2c). If no return value exists, the current test will fail.

        Returns:
        :   The value the current function should return as a `void *`
