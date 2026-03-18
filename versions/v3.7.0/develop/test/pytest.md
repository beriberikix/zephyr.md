---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/develop/test/pytest.html
original_path: develop/test/pytest.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Integration with pytest test framework

*Please mind that integration of twister with pytest is still work in progress. Not every platform
type is supported in pytest (yet). If you find any issue with the integration or have an idea for
an improvement, please, let us know about it and open a GitHub issue/enhancement.*

## Introduction

Pytest is a python framework that *“makes it easy to write small, readable tests, and can scale to
support complex functional testing for applications and libraries”* ([https://docs.pytest.org/en/7.3.x/](https://docs.pytest.org/en/7.3.x/)).
Python is known for its free libraries and ease of using it for scripting. In addition, pytest
utilizes the concept of plugins and fixtures, increasing its expendability and reusability.
A pytest plugin pytest-twister-harness was introduced to provide an integration between pytest
and twister, allowing Zephyr’s community to utilize pytest functionality with keeping twister as
the main framework.

## Integration with twister

By default, there is nothing to be done to enable pytest support in twister. The plugin is
developed as a part of Zephyr’s tree. To enable install-less operation, twister first extends
`PYTHONPATH` with path to this plugin, and then during pytest call, it appends the command with
`-p twister_harness.plugin` argument. If one prefers to use the installed version of the plugin,
they must add `--allow-installed-plugin` flag to twister’s call.

Pytest-based test suites are discovered the same way as other twister tests, i.e., by a presence
of test/sample.yaml. Inside, a keyword `harness` tells twister how to handle a given test.
In the case of `harness: pytest`, most of twister workflow (test suites discovery,
parallelization, building and reporting) remains the same as for other harnesses. The change
happens during the execution step. The below picture presents a simplified overview of the
integration.

![../../_images/twister_and_pytest.svg](../../_images/twister_and_pytest.svg)

If `harness: pytest` is used, twister delegates the test execution to pytest, by calling it as
a subprocess. Required parameters (such as build directory, device to be used, etc.) are passed
through a CLI command. When pytest is done, twister looks for a pytest report (results.xml) and
sets the test result accordingly.

## How to create a pytest test

An example folder containing a pytest test, application source code and Twister configuration .yaml
file can look like the following:

```text
test_foo/
├─── pytest/
│    └─── test_foo.py
├─── src/
│    └─── main.c
├─── CMakeList.txt
├─── prj.conf
└─── testcase.yaml
```

An example of a pytest test is given at
[samples/subsys/testsuite/pytest/shell/pytest/test\_shell.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/testsuite/pytest/shell/pytest/test_shell.py). Using the configuration
provided in the `testcase.yaml` file, Twister builds the application from `src` and then, if the
.yaml file contains a `harness: pytest` entry, it calls pytest in a separate subprocess. A sample
configuration file may look like this:

```yaml
tests:
   some.foo.test:
      harness: pytest
      tags: foo
```

By default, pytest tries to look for tests in a `pytest` directory located next to a directory
with binary sources. A keyword `pytest_root` placed under `harness_config` section in .yaml file
can be used to point to other files, directories or subtests (more info [here](twister.md#pytest-root)).

Pytest scans the given locations looking for tests, following its default
[discovery rules](https://docs.pytest.org/en/7.1.x/explanation/goodpractices.html#conventions-for-python-test-discovery).

### Passing extra arguments

There are two ways for passing extra arguments to the called pytest subprocess:

1. From .yaml file, using `pytest_args` placed under `harness_config` section - more info
   [here](twister.md#pytest-args).
2. Through Twister command line interface as `--pytest-args` argument. This can be particularly
   useful when one wants to select a specific testcase from a test suite. For instance, one can use
   a command:

   ```shell
   $ ./scripts/twister --platform native_sim -T samples/subsys/testsuite/pytest/shell \
   -s samples/subsys/testsuite/pytest/shell/sample.pytest.shell \
   --pytest-args='-k test_shell_print_version'
   ```

## Fixtures

### dut

Give access to a [DeviceAdapter](#deviceadapter) type object, that represents Device Under Test. This fixture is
the core of pytest harness plugin. It is required to launch DUT (initialize logging, flash device,
connect serial etc). This fixture yields a device prepared according to the requested type
(`native`, `qemu`, `hardware`, etc.). All types of devices share the same API. This allows for
writing tests which are device-type-agnostic. Scope of this fixture is determined by the
`pytest_dut_scope` keyword placed under `harness_config` section (more info
[here](twister.md#pytest-dut-scope)).

```python
from twister_harness import DeviceAdapter

def test_sample(dut: DeviceAdapter):
   dut.readlines_until('Hello world')
```

### shell

Provide a [Shell](#shell-class) class object with methods used to interact with shell application.
It calls `wait_for_promt` method, to not start scenario until DUT is ready. The shell fixture
calls `dut` fixture, hence has access to all its methods. The `shell` fixture adds methods
optimized for interactions with a shell. It can be used instead of `dut` for tests. Scope of this
fixture is determined by the `pytest_dut_scope` keyword placed under `harness_config` section
(more info [here](twister.md#pytest-dut-scope)).

```python
from twister_harness import Shell

def test_shell(shell: Shell):
   shell.exec_command('help')
```

### mcumgr

Sample fixture to wrap `mcumgr` command-line tool used to manage remote devices. More information
about MCUmgr can be found here [MCUmgr](../../services/device_mgmt/mcumgr.md#mcu-mgr).

Note

This fixture requires the `mcumgr` available in the system PATH

Only selected functionality of MCUmgr is wrapped by this fixture. For example, here is a test with
a fixture `mcumgr`

```python
from twister_harness import DeviceAdapter, Shell, McuMgr

def test_upgrade(dut: DeviceAdapter, shell: Shell, mcumgr: McuMgr):
   # free the serial port for mcumgr
   dut.disconnect()
   # upload the signed image
   mcumgr.image_upload('path/to/zephyr.signed.bin')
   # obtain the hash of uploaded image from the device
   second_hash = mcumgr.get_hash_to_test()
   # test a new upgrade image
   mcumgr.image_test(second_hash)
   # reset the device remotely
   mcumgr.reset_device()
   # continue test scenario, check version etc.
```

## Classes

### DeviceAdapter

*class* twister\_harness.DeviceAdapter(*device\_config: DeviceConfig*)
:   This class defines a common interface for all device types (hardware,
    simulator, QEMU) used in tests to gathering device output and send data to
    it.

    launch() → None
    :   Start by closing previously running application (no effect if not
        needed). Then, flash and run test application. Finally, start an
        internal reader thread capturing an output from a device.

    connect(*retry\_s: int = 0*) → None
    :   Connect to device - allow for output gathering.

    readline(*timeout: float | None = None*, *print\_output: bool = True*) → str
    :   Read line from device output. If timeout is not provided, then use
        base\_timeout.

    readlines(*print\_output: bool = True*) → list[str]
    :   Read all available output lines produced by device from internal buffer.

    readlines\_until(*regex: str | None = None*, *num\_of\_lines: int | None = None*, *timeout: float | None = None*, *print\_output: bool = True*) → list[str]
    :   Read available output lines produced by device from internal buffer
        until following conditions:

        1. If regex is provided - read until regex regex is found in read
           line (or until timeout).
        2. If num\_of\_lines is provided - read until number of read lines is
           equal to num\_of\_lines (or until timeout).
        3. If none of above is provided - return immediately lines collected so
           far in internal buffer.

        If timeout is not provided, then use base\_timeout.

    write(*data: bytes*) → None
    :   Write data bytes to device.

    disconnect() → None
    :   Disconnect device - block output gathering.

    close() → None
    :   Disconnect, close device and close reader thread.

### Shell

*class* twister\_harness.Shell(*device: [DeviceAdapter](#twister_harness.DeviceAdapter)*, *prompt: str = 'uart:~$'*, *timeout: float | None = None*)
:   Helper class that provides methods used to interact with shell application.

    exec\_command(*command: str*, *timeout: float | None = None*, *print\_output: bool = True*) → list[str]
    :   Send shell command to a device and return response. Passed command
        is extended by double enter sings - first one to execute this command
        on a device, second one to receive next prompt what is a signal that
        execution was finished. Method returns printout of the executed command.

    wait\_for\_prompt(*timeout: float | None = None*) → bool
    :   Send every 0.5 second “enter” command to the device until shell prompt
        statement will occur (return True) or timeout will be exceeded (return
        False).

## Examples of pytest tests in the Zephyr project

- [Pytest shell application testing](../../samples/subsys/testsuite/pytest/shell/README.md#pytest_shell "Execute pytest tests against the Zephyr shell.")
- MCUmgr tests - [tests/boot/with\_mcumgr](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/boot/with_mcumgr)
- LwM2M tests - [tests/net/lib/lwm2m/interop](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/net/lib/lwm2m/interop)
- GDB stub tests - [tests/subsys/debug/gdbstub](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/subsys/debug/gdbstub)

## FAQ

### How to flash/run application only once per pytest session?

> `dut` is a fixture responsible for flashing/running application. By default, its scope is set
> as `function`. This can be changed by adding to .yaml file `pytest_dut_scope` keyword placed
> under `harness_config` section:
>
> ```yaml
> harness: pytest
> harness_config:
>    pytest_dut_scope: session
> ```
>
> More info can be found [here](twister.md#pytest-dut-scope).

### How to run only one particular test from a python file?

> This can be achieved in several ways. In .yaml file it can be added using a `pytest_root` entry
> placed under `harness_config` with list of tests which should be run:
>
> ```yaml
> harness: pytest
> harness_config:
>    pytest_root:
>       - "pytest/test_shell.py::test_shell_print_help"
> ```
>
> Particular tests can be also chosen by pytest `-k` option (more info about pytest keyword
> filter can be found
> [here](https://docs.pytest.org/en/latest/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)
> ). It can be applied by adding `-k` filter in `pytest_args` in .yaml file:
>
> ```yaml
> harness: pytest
> harness_config:
>    pytest_args:
>       - "-k test_shell_print_help"
> ```
>
> or by adding it to Twister command overriding parameters from the .yaml file:
>
> ```shell
> $ ./scripts/twister ... --pytest-args='-k test_shell_print_help'
> ```

### How to get information about used device type in test?

> This can be taken from `dut` fixture (which represents [DeviceAdapter](#deviceadapter) object):
>
> ```python
> device_type: str = dut.device_config.type
> if device_type == 'hardware':
>    ...
> elif device_type == 'native':
>    ...
> ```

### How to rerun locally pytest tests without rebuilding application by Twister?

> This can be achieved by running Twister once again with `--test-only` argument added to Twister
> command. Another way is running Twister with highest verbosity level (`-vv`) and then
> copy-pasting from logs command dedicated for spawning pytest (log started by `Running pytest
> command: ...`).

### Is this possible to run pytest tests in parallel?

> Basically `pytest-harness-plugin` wasn’t written with intention of running pytest tests in
> parallel. Especially those one dedicated for hardware. There was assumption that parallelization
> of tests is made by Twister, and it is responsible for managing available sources (jobs and
> hardwares). If anyone is interested in doing this for some reasons (for example via
> [pytest-xdist plugin](https://pytest-xdist.readthedocs.io/en/stable/)) they do so at their own
> risk.

## Limitations

- Not every platform type is supported in the plugin (yet).
