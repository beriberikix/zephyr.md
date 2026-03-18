---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/test/twister/twister_blackbox.html
original_path: develop/test/twister/twister_blackbox.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Twister blackbox tests

This guide aims to explain the structure of a test file so the reader will be able
to understand existing files and create their own. All developers should fix any tests
they break and create new ones when introducing new features, so this knowledge is
important for any Twister developer.

## Basics

Twister blackbox tests are written in python, using the `pytest` library.
Read up on it [here](../pytest.md#integration-with-pytest) .
Auxiliary test data follows whichever format it was in originally.
Tests and data are wholly contained in the [scripts/tests/twister\_blackbox](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/tests/twister_blackbox)
directory and prepended with `test_`.

Blackbox tests should not be aware of the internal twister code. Instead, they should
call twister as user would and check the results.

## Sample test file

```python
 1#!/usr/bin/env python3
 2# Copyright (c) 2024 Intel Corporation
 3#
 4# SPDX-License-Identifier: Apache-2.0
 5
 6import importlib
 7import mock
 8import os
 9import pytest
10import sys
11import json
12
13from conftest import ZEPHYR_BASE, TEST_DATA, testsuite_filename_mock
14from twisterlib.testplan import TestPlan
15
16
17class TestDummy:
18    TESTDATA_X = [
19        ("smoke", 5),
20        ("acceptance", 6),
21    ]
22
23    @classmethod
24    def setup_class(cls):
25        apath = os.path.join(ZEPHYR_BASE, "scripts", "twister")
26        cls.loader = importlib.machinery.SourceFileLoader("__main__", apath)
27        cls.spec = importlib.util.spec_from_loader(cls.loader.name, cls.loader)
28        cls.twister_module = importlib.util.module_from_spec(cls.spec)
29
30    @classmethod
31    def teardown_class(cls):
32        pass
33
34    @pytest.mark.parametrize(
35        "level, expected_tests", TESTDATA_X, ids=["smoke", "acceptance"]
36    )
37    @mock.patch.object(TestPlan, "TESTSUITE_FILENAME", testsuite_filename_mock)
38    def test_level(self, capfd, out_path, level, expected_tests):
39        # Select platforms used for the tests
40        test_platforms = ["qemu_x86", "frdm_k64f"]
41        # Select test root
42        path = os.path.join(TEST_DATA, "tests")
43        config_path = os.path.join(TEST_DATA, "test_config.yaml")
44
45        # Set flags for our Twister command as a list of strs
46        args = (
47            # Flags related to the generic test setup:
48            # * Control the level of detail in stdout/err
49            # * Establish the output directory
50            # * Select Zephyr tests to use
51            # * Control whether to only build or build and run aforementioned tests
52            ["-i", "--outdir", out_path, "-T", path, "-y"]
53            # Flags under test
54            + ["--level", level]
55            # Flags required for the test
56            + ["--test-config", config_path]
57            # Flags related to platform selection
58            + [
59                val
60                for pair in zip(["-p"] * len(test_platforms), test_platforms)
61                for val in pair
62            ]
63        )
64
65        # First, provide the args variable as our Twister command line arguments.
66        # Then, catch the exit code in the sys_exit variable.
67        with mock.patch.object(sys, "argv", [sys.argv[0]] + args), pytest.raises(
68            SystemExit
69        ) as sys_exit:
70            # Execute the Twister call itself.
71            self.loader.exec_module(self.twister_module)
72
73        # Check whether the Twister call succeeded
74        assert str(sys_exit.value) == "0"
75
76        # Access to the test file output
77        with open(os.path.join(out_path, "testplan.json")) as f:
78            j = json.load(f)
79        filtered_j = [
80            (ts["platform"], ts["name"], tc["identifier"])
81            for ts in j["testsuites"]
82            for tc in ts["testcases"]
83            if "reason" not in tc
84        ]
85
86        # Read stdout and stderr to out and err variables respectively
87        out, err = capfd.readouterr()
88        # Rewrite the captured buffers to stdout and stderr so the user can still read them
89        sys.stdout.write(out)
90        sys.stderr.write(err)
91
92        # Test-relevant checks
93        assert expected_tests == len(filtered_j)
```

## Comparison with CLI

Test above runs the command

```shell
twister -i --outdir $OUTDIR -T $TEST_DATA/tests -y --level $LEVEL
--test-config $TEST_DATA/test_config.yaml -p qemu_x86 -p frdm_k64f
```

It presumes a CLI with the `zephyr-env.sh` or `zephyr-env.cmd` already run.

Such a test provides us with all the outputs we typically expect of a Twister run thanks to
`importlib` ‘s `exec_module()` [[1]](#f1) .
We can easily set up all flags that we expect from a Twister call via `args` variable [[2]](#f2) .
We can check the standard output or stderr in `out` and `err` variables.

Beside the standard outputs, we can also investigate the file outputs, normally placed in
`twister-out` directories. Most of the time, we will use the `out_path` fixture in conjunction
with `--outdir` flag (L52) to keep test-generated files in temporary directories.
Typical files read in blackbox tests are `testplan.json` , `twister.xml` and `twister.log` .

## Other functionalities

### Decorators

- `@pytest.mark.usefixtures('clear_log')`
  :   - allows us to use `clear_log` fixture from `conftest.py` .
        The fixture is to become `autouse` in the future.
        After that, this decorator can be removed.
- `@pytest.mark.parametrize('level, expected_tests', TESTDATA_X, ids=['smoke', 'acceptance'])`
  :   - this is an example of `pytest` ‘s test parametrization.
        Read up on it [here](https://docs.pytest.org/en/7.1.x/example/parametrize.html#different-options-for-test-ids).
        TESTDATAs are most often declared as class fields.
- `@mock.patch.object(TestPlan, 'TESTSUITE_FILENAME', testsuite_filename_mock)`
  :   - this decorator allows us to use only tests defined in the `test_data` and
        ignore the Zephyr testcases in the `tests` directory. **Note that all ``test\_data``
        tests use** `test_data.yaml` **as a filename, not** `testcase.yaml` **!**
        Read up on the `mock` library
        [here](https://docs.python.org/3/library/unittest.mock.html).

### Fixtures

Blackbox tests use `pytest` ‘s fixtures, further reading on which is available
[here](https://docs.pytest.org/en/6.2.x/fixture.html).

If you would like to add your own fixtures,
consider whether they will be used in just one test file, or in many.

- If in many, create such a fixture in the
  [scripts/tests/twister\_blackbox/conftest.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/tests/twister_blackbox/conftest.py) file.

  > - [scripts/tests/twister\_blackbox/conftest.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/tests/twister_blackbox/conftest.py) already contains some fixtures -
  >   take a look there for an example.
- If in just one, declare it in that file.

  > - Consider using class fields instead - look at TESTDATAs for an example.

## How do I…

### Call Twister multiple times in one test?

Sometimes we want to test something that requires prior Twister use. `--test-only`
flag would be a typical example, as it is to be coupled with previous `--build-only`
Twister call. How should we approach that?

If we just call the `importlib` ‘s `exec_module` two times, we will experience log
duplication. `twister.log` will duplicate every line (triplicate if we call it three times, etc.)
instead of overwriting the log or appending to the end of it.

It is caused by the use of logger module variables in the Twister files.
Thus us executing the module again causes the loggers to have multiple handles.

To overcome this, between the calls you ought to use

```python
capfd.readouterr()   # To remove output from the buffer
                     # Note that if you want output from all runs after each other,
                     # skip this line.
clear_log_in_test()  # To remove log duplication
```

---

Footnotes

[[1](#id1)]

Take note of the `setup_class()` class function, which allows us to run
`twister` python file as if it were called directly
(bypassing the `__name__ == '__main__'` check).

[[2](#id2)]

We advise you to keep the first section of `args` definition intact in almost all
of your tests, as it is used for the common test setup.
