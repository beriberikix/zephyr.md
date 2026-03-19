---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/west/build-flash-debug.html
original_path: develop/west/build-flash-debug.html
---

# Building, Flashing and Debugging

Zephyr provides several [west extension commands](extensions.md#west-extensions) for
building, flashing, and interacting with Zephyr programs running on a board:
`build`, `flash`, `debug`, `debugserver` and `attach`.

For information on adding board support for the flashing and debugging
commands, see [Flash and debug support](../../hardware/porting/board_porting.md#flash-and-debug-support) in the board porting guide.

## [Building: `west build`](#id10)

Tip

Run `west build -h` for a quick overview.

The `build` command helps you build Zephyr applications from source. You can
use [west config](config.md#west-config-cmd) to configure its behavior.

Its default behavior tries to “do what you mean”:

- If there is a Zephyr build directory named `build` in your current
  working directory, it is incrementally re-compiled. The same is true if you
  run `west build` from a Zephyr build directory.
- Otherwise, if you run `west build` from a Zephyr application’s source
  directory and no build directory is found, a new one is created and the
  application is compiled in it.

### [Basics](#id11)

The easiest way to use `west build` is to go to an application’s root
directory (i.e. the folder containing the application’s `CMakeLists.txt`)
and then run:

```text
west build -b <BOARD>
```

Where `<BOARD>` is the name of the board you want to build for. This is
exactly the same name you would supply to CMake if you were to invoke it with:
`cmake -DBOARD=<BOARD>`.

Tip

You can use the [west boards](zephyr-cmds.md#west-boards) command to list all
supported boards.

A build directory named `build` will be created, and the application will
be compiled there after `west build` runs CMake to create a build system in
that directory. If `west build` finds an existing build directory, the
application is incrementally re-compiled there without re-running CMake. You
can force CMake to run again with `--cmake`.

You don’t need to use the `--board` option if you’ve already got an existing
build directory; `west build` can figure out the board from the CMake cache.
For new builds, the `--board` option, [`BOARD`](../env_vars.md#envvar-BOARD) environment variable,
or `build.board` configuration option are checked (in that order).

### [Sysbuild (multi-domain builds)](#id12)

[Sysbuild (System build)](../../build/sysbuild/index.md#sysbuild) can be used to create a multi-domain build system combining
multiple images for a single or multiple boards.

Use `--sysbuild` to select the [Sysbuild (System build)](../../build/sysbuild/index.md#sysbuild) build infrastructure with
`west build` to build multiple domains.

More detailed information regarding the use of sysbuild can be found in the
[Sysbuild (System build)](../../build/sysbuild/index.md#sysbuild) guide.

Tip

The `build.sysbuild` configuration option can be enabled to tell
`west build` to default build using sysbuild.
`--no-sysbuild` can be used to disable sysbuild for a specific build.

`west build` will build all domains through the top-level build folder of the
domains specified by sysbuild.

A single domain from a multi-domain project can be built by using `--domain`
argument.

### [Examples](#id13)

Here are some `west build` usage examples, grouped by area.

#### [Forcing CMake to Run Again](#id14)

To force a CMake re-run, use the `--cmake` (or `-c`) option:

```text
west build -c
```

#### [Setting a Default Board](#id15)

To configure `west build` to build for the `reel_board` by default:

```text
west config build.board reel_board
```

(You can use any other board supported by Zephyr here; it doesn’t have to be
`reel_board`.)

#### [Setting Source and Build Directories](#id16)

To set the application source directory explicitly, give its path as a
positional argument:

```text
west build -b <BOARD> path/to/source/directory
```

To set the build directory explicitly, use `--build-dir` (or `-d`):

```text
west build -b <BOARD> --build-dir path/to/build/directory
```

To change the default build directory from `build`, use the
`build.dir-fmt` configuration option. This lets you name build
directories using format strings, like this:

```text
west config build.dir-fmt "build/{board}/{app}"
```

With the above, running `west build -b reel_board samples/hello_world` will
use build directory `build/reel_board/hello_world`. See
[Configuration Options](#west-building-config) for more details on this option.

#### [Setting the Build System Target](#id17)

To specify the build system target to run, use `--target` (or `-t`).

For example, on host platforms with QEMU, you can use the `run` target to
build and run the [Hello World](../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample for the emulated
[qemu\_x86](../../boards/qemu/x86/doc/index.md#qemu_x86) board in one command:

```text
west build -b qemu_x86 -t run samples/hello_world
```

As another example, to use `-t` to list all build system targets:

```text
west build -t help
```

As a final example, to use `-t` to run the `pristine` target, which deletes
all the files in the build directory:

```text
west build -t pristine
```

#### [Pristine Builds](#id18)

A *pristine* build directory is essentially a new build directory. All
byproducts from previous builds have been removed.

To force `west build` make the build directory pristine before re-running
CMake to generate a build system, use the `--pristine=always` (or
`-p=always`) option.

Giving `--pristine` or `-p` without a value has the same effect as giving
it the value `always`. For example, these commands are equivalent:

```text
west build -p -b reel_board samples/hello_world
west build -p=always -b reel_board samples/hello_world
```

By default, `west build` makes no attempt to detect if the build directory
needs to be made pristine. This can lead to errors if you do something like
try to reuse a build directory for a different `--board`.

Using `--pristine=auto` makes `west build` detect some of these situations
and make the build directory pristine before trying the build.

Tip

You can run `west config build.pristine always` to always do a pristine
build, or `west config build.pristine never` to disable the heuristic.
See the `west build` [Configuration Options](#west-building-config) for details.

#### [Verbose Builds](#id19)

To print the CMake and compiler commands run by `west build`, use the global
west verbosity option, `-v`:

```text
west -v build -b reel_board samples/hello_world
```

#### [One-Time CMake Arguments](#id20)

To pass additional arguments to the CMake invocation performed by `west
build`, pass them after a `--` at the end of the command line.

Important

Passing additional CMake arguments like this forces `west build` to re-run
the CMake build configuration step, even if a build system has already been
generated. This will make incremental builds slower (but still much faster
than building from scratch).

After using `--` once to generate the build directory, use `west build -d
<build-dir>` on subsequent runs to do incremental builds.

Alternatively, make your CMake arguments permanent as described in the next
section; it will not slow down incremental builds.

For example, to use the Unix Makefiles CMake generator instead of Ninja (which
`west build` uses by default), run:

```text
west build -b reel_board -- -G'Unix Makefiles'
```

To use Unix Makefiles and set [CMAKE\_VERBOSE\_MAKEFILE](https://cmake.org/cmake/help/latest/variable/CMAKE_VERBOSE_MAKEFILE.html) to `ON`:

```text
west build -b reel_board -- -G'Unix Makefiles' -DCMAKE_VERBOSE_MAKEFILE=ON
```

Notice how the `--` only appears once, even though multiple CMake arguments
are given. All command-line arguments to `west build` after a `--` are
passed to CMake.

To set [DTC\_OVERLAY\_FILE](../application/index.md#important-build-vars) to
`enable-modem.overlay`, using that file as a
[devicetree overlay](../../build/dts/index.md#dt-guide):

```text
west build -b reel_board -- -DDTC_OVERLAY_FILE=enable-modem.overlay
```

To merge the `file.conf` Kconfig fragment into your build’s
`.config`:

```text
west build -- -DEXTRA_CONF_FILE=file.conf
```

#### [Permanent CMake Arguments](#id21)

The previous section describes how to add CMake arguments for a single `west
build` command. If you want to save CMake arguments for `west build` to use
every time it generates a new build system instead, you should use the
`build.cmake-args` configuration option. Whenever `west build` runs CMake
to generate a build system, it splits this option’s value according to shell
rules and includes the results in the `cmake` command line.

Remember that, by default, `west build` **tries to avoid generating a new
build system if one is present** in your build directory. Therefore, you need
to either delete any existing build directories or do a [pristine build](#west-building-pristine) after setting `build.cmake-args` to make sure it
will take effect.

For example, to always enable **CMAKE\_EXPORT\_COMPILE\_COMMANDS**, you can
run:

```text
west config build.cmake-args -- -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
```

(The extra `--` is used to force the rest of the command to be treated as a
positional argument. Without it, [west config](config.md#west-config-cmd) would
treat the `-DVAR=VAL` syntax as a use of its `-D` option.)

To enable **CMAKE\_VERBOSE\_MAKEFILE**, so CMake always produces a verbose
build system:

```text
west config build.cmake-args -- -DCMAKE_VERBOSE_MAKEFILE=ON
```

To save more than one argument in `build.cmake-args`, use a single string
whose value can be split into distinct arguments (`west build` uses the
Python function [shlex.split()](https://docs.python.org/3/library/shlex.html#shlex.split) internally to split the value).

For example, to enable both **CMAKE\_EXPORT\_COMPILE\_COMMANDS** and
**CMAKE\_VERBOSE\_MAKEFILE**:

```text
west config build.cmake-args -- "-DCMAKE_EXPORT_COMPILE_COMMANDS=ON -DCMAKE_VERBOSE_MAKEFILE=ON"
```

If you want to save your CMake arguments in a separate file instead, you can
combine CMake’s `-C <initial-cache>` option with `build.cmake-args`. For
instance, another way to set the options used in the previous example is to
create a file named `~/my-cache.cmake` with the following contents:

```cmake
set(CMAKE_EXPORT_COMPILE_COMMANDS ON CACHE BOOL "")
set(CMAKE_VERBOSE_MAKEFILE ON CACHE BOOL "")
```

Then run:

```text
west config build.cmake-args "-C ~/my-cache.cmake"
```

See the [cmake(1) manual page](https://cmake.org/cmake/help/latest/manual/cmake.1.html) and the [set() command](https://cmake.org/cmake/help/latest/command/set.html) documentation for
more details.

#### [Build tool arguments](#id22)

Use `-o` to pass options to the underlying build tool.

This works with both `ninja` ([the default](#west-building-generator))
and `make` based build systems.

For example, to pass `-dexplain` to `ninja`:

```text
west build -o=-dexplain
```

As another example, to pass `--keep-going` to `make`:

```text
west build -o=--keep-going
```

Note that using `-o=--foo` instead of `-o --foo` is required to prevent
`--foo` from being treated as a `west build` option.

#### [Build parallelism](#id23)

By default, `ninja` uses all of your cores to build, while `make` uses only
one. You can control this explicitly with the `-j` option supported by both
tools.

For example, to build with 4 cores:

```text
west build -o=-j4
```

The `-o` option is described further in the previous section.

#### [Build a single domain](#id24)

In a multi-domain build with [Hello World](../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") and [MCUboot](https://mcuboot.com/), you can use
`--domain hello_world` to only build this domain:

```text
west build --sysbuild --domain hello_world
```

The `--domain` argument can be combined with the `--target` argument to
build the specific target for the target, for example:

```text
west build --sysbuild --domain hello_world --target help
```

#### [Use a snippet](#id25)

See [Using Snippets](../../build/snippets/using.md#using-snippets).

### [Configuration Options](#id26)

You can [configure](config.md#west-config-cmd) `west build` using these options.

| Option | Description |
| --- | --- |
| `build.board` | String. If given, this the board used by [west build](#west-building) when `--board` is not given and `BOARD` is unset in the environment. |
| `build.board_warn` | Boolean, default `true`. If `false`, disables warnings when `west build` can’t figure out the target board. |
| `build.cmake-args` | String. If present, the value will be split according to shell rules and passed to CMake whenever a new build system is generated. See [Permanent CMake Arguments](#west-building-cmake-config). |
| `build.dir-fmt` | String, default `build`. The build folder format string, used by west whenever it needs to create or locate a build folder. The currently available arguments are:  - `board`: The board name - `source_dir`: The relative path from the current working directory   to the source directory. If the current working directory is inside   the source directory this will be set to an empty string. - `app`: The name of the source directory. |
| `build.generator` | String, default `Ninja`. The [CMake Generator](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html) to use to create a build system. (To set a generator for a single build, see the [above example](#west-building-generator)) |
| `build.guess-dir` | String, instructs west whether to try to guess what build folder to use when `build.dir-fmt` is in use and not enough information is available to resolve the build folder name. Can take these values:  - `never` (default): Never try to guess, bail out instead and   require the user to provide a build folder with `-d`. - `runners`: Try to guess the folder when using any of the ‘runner’   commands. These are typically all commands that invoke an external   tool, such as `flash` and `debug`. |
| `build.pristine` | String. Controls the way in which `west build` may clean the build folder before building. Can take the following values:  - `never` (default): Never automatically make the build folder   pristine. - `auto`: `west build` will automatically make the build folder   pristine before building, if a build system is present and the build   would fail otherwise (e.g. the user has specified a different board   or application from the one previously used to make the build   directory). - `always`: Always make the build folder pristine before building, if   a build system is present. |
| `build.sysbuild` | Boolean, default `false`. If `true`, build application using the sysbuild infrastructure. |

## [Flashing: `west flash`](#id27)

Tip

Run `west flash -h` for additional help.

### [Basics](#id28)

From a Zephyr build directory, re-build the binary and flash it to
your board:

```text
west flash
```

Without options, the behavior is the same as `ninja flash` (or
`make flash`, etc.).

To specify the build directory, use `--build-dir` (or `-d`):

```text
west flash --build-dir path/to/build/directory
```

If you don’t specify the build directory, `west flash` searches for one in
`build`, then the current working directory. If you set the
`build.dir-fmt` configuration option (see [Setting Source and Build Directories](#west-building-dirs)), `west
flash` searches there instead of `build`.

### [Choosing a Runner](#id29)

If your board’s Zephyr integration supports flashing with multiple
programs, you can specify which one to use using the `--runner` (or
`-r`) option. For example, if West flashes your board with
`nrfjprog` by default, but it also supports JLink, you can override
the default with:

```text
west flash --runner jlink
```

You can override the default flash runner at build time by using the
`BOARD_FLASH_RUNNER` CMake variable, and the debug runner with
`BOARD_DEBUG_RUNNER`.

For example:

```text
# Set the default runner to "jlink", overriding the board's
# usual default.
west build [...] -- -DBOARD_FLASH_RUNNER=jlink
```

See [One-Time CMake Arguments](#west-building-cmake-args) and [Permanent CMake Arguments](#west-building-cmake-config) for
more information on setting CMake arguments.

See [Flash and debug runners](#west-runner) below for more information on the `runner`
library used by West. The list of runners which support flashing can
be obtained with `west flash -H`; if run from a build directory or
with `--build-dir`, this will print additional information on
available runners for your board.

### [Configuration Overrides](#id30)

The CMake cache contains default values West uses while flashing, such
as where the board directory is on the file system, the path to the
zephyr binaries to flash in several formats, and more. You can
override any of this configuration at runtime with additional options.

For example, to override the HEX file containing the Zephyr image to
flash (assuming your runner expects a HEX file), but keep other
flash configuration at default values:

```text
west flash --hex-file path/to/some/other.hex
```

The `west flash -h` output includes a complete list of overrides
supported by all runners.

### [Runner-Specific Overrides](#id31)

Each runner may support additional options related to flashing. For
example, some runners support an `--erase` flag, which mass-erases
the flash storage on your board before flashing the Zephyr image.

To view all of the available options for the runners your board
supports, as well as their usage information, use `--context` (or
`-H`):

```text
west flash --context
```

Important

Note the capital H in the short option name. This re-runs the build
in order to ensure the information displayed is up to date!

When running West outside of a build directory, `west flash -H` just
prints a list of runners. You can use `west flash -H -r
<runner-name>` to print usage information for options supported by
that runner.

For example, to print usage information about the `jlink` runner:

```text
west flash -H -r jlink
```

### [Multi-domain flashing](#id32)

When a [Sysbuild (multi-domain builds)](#west-multi-domain-builds) folder is detected, then `west flash`
will flash all domains in the order defined by sysbuild.

It is possible to flash the image from a single domain in a multi-domain project
by using `--domain`.

For example, in a multi-domain build with [Hello World](../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") and
[MCUboot](https://mcuboot.com/), you can use the `--domain hello_world` domain to only flash
only the image from this domain:

```text
west flash --domain hello_world
```

## [Debugging: `west debug`, `west debugserver`](#id33)

Tip

Run `west debug -h` or `west debugserver -h` for additional help.

### [Basics](#id34)

From a Zephyr build directory, to attach a debugger to your board and
open up a debug console (e.g. a GDB session):

```text
west debug
```

To attach a debugger to your board and open up a local network port
you can connect a debugger to (e.g. an IDE debugger):

```text
west debugserver
```

Without options, the behavior is the same as `ninja debug` and
`ninja debugserver` (or `make debug`, etc.).

To specify the build directory, use `--build-dir` (or `-d`):

```text
west debug --build-dir path/to/build/directory
west debugserver --build-dir path/to/build/directory
```

If you don’t specify the build directory, these commands search for one in
`build`, then the current working directory. If you set the
`build.dir-fmt` configuration option (see [Setting Source and Build Directories](#west-building-dirs)), `west
debug` searches there instead of `build`.

### [Choosing a Runner](#id35)

If your board’s Zephyr integration supports debugging with multiple
programs, you can specify which one to use using the `--runner` (or
`-r`) option. For example, if West debugs your board with
`pyocd-gdbserver` by default, but it also supports JLink, you can
override the default with:

```text
west debug --runner jlink
west debugserver --runner jlink
```

See [Flash and debug runners](#west-runner) below for more information on the `runner`
library used by West. The list of runners which support debugging can
be obtained with `west debug -H`; if run from a build directory or
with `--build-dir`, this will print additional information on
available runners for your board.

### [Configuration Overrides](#id36)

The CMake cache contains default values West uses for debugging, such
as where the board directory is on the file system, the path to the
zephyr binaries containing symbol tables, and more. You can override
any of this configuration at runtime with additional options.

For example, to override the ELF file containing the Zephyr binary and
symbol tables (assuming your runner expects an ELF file), but keep
other debug configuration at default values:

```text
west debug --elf-file path/to/some/other.elf
west debugserver --elf-file path/to/some/other.elf
```

The `west debug -h` output includes a complete list of overrides
supported by all runners.

### [Runner-Specific Overrides](#id37)

Each runner may support additional options related to debugging. For
example, some runners support flags which allow you to set the network
ports used by debug servers.

To view all of the available options for the runners your board
supports, as well as their usage information, use `--context` (or
`-H`):

```text
west debug --context
```

(The command `west debugserver --context` will print the same output.)

Important

Note the capital H in the short option name. This re-runs the build
in order to ensure the information displayed is up to date!

When running West outside of a build directory, `west debug -H` just
prints a list of runners. You can use `west debug -H -r
<runner-name>` to print usage information for options supported by
that runner.

For example, to print usage information about the `jlink` runner:

```text
west debug -H -r jlink
```

### [Multi-domain debugging](#id38)

`west debug` can only debug a single domain at a time. When a
[Sysbuild (multi-domain builds)](#west-multi-domain-builds) folder is detected, `west debug`
will debug the `default` domain specified by sysbuild.

The default domain will be the application given as the source directory.
See the following example:

```text
west build --sysbuild path/to/source/directory
```

For example, when building `hello_world` with [MCUboot](https://mcuboot.com/) using sysbuild,
`hello_world` becomes the default domain:

```text
west build --sysbuild samples/hello_world
```

So to debug `hello_world` you can do:

```text
west debug
```

or:

```text
west debug --domain hello_world
```

If you wish to debug MCUboot, you must explicitly specify MCUboot as the domain
to debug:

```text
west debug --domain mcuboot
```

## [Flash and debug runners](#id39)

The flash and debug commands use Python wrappers around various
[Flash & Debug Host Tools](../flash_debug/host-tools.md#flash-debug-host-tools). These wrappers are all defined in a Python
library at [scripts/west\_commands/runners](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/west_commands/runners). Each wrapper is
called a *runner*. Runners can flash and/or debug Zephyr programs.

The central abstraction within this library is `ZephyrBinaryRunner`, an
abstract class which represents runners. The set of available runners is
determined by the imported subclasses of `ZephyrBinaryRunner`.
`ZephyrBinaryRunner` is available in the `runners.core` module; individual
runner implementations are in other submodules, such as `runners.nrfjprog`,
`runners.openocd`, etc.

## [Running Robot Framework tests: `west robot`](#id40)

Tip

Run `west robot -h` for additional help.

### [Basics](#id41)

Currently the command supports only one runner which is using `renode-test`,
(essentially a wrapper for running Robot tests in Renode), but can be
easily extended by adding other runners.

From a Zephyr build directory, to run a Robot test suite:

```text
west robot --runner=renode-robot --testsuite path/to/testsuite.robot
```

This will run all tests from testsuite.robot and print output provided
by Robot Framework.

To pass additional parameters to Renode use `--renode-robot-args` switch.
For example to show Renode logs in addition to Robot Framework’s output:

> west robot –runner=renode-robot –testsuite path/to/testsuite.robot –renode-robot-arg=”–show-log”

### [Runner-Specific Overrides](#id42)

To view all of the available options for the Robot runners your board
supports, as well as their usage information, use `--context` (or
`-H`):

```text
west robot --runner=renode-robot --context
```

To view all available options “renode-test” runner supports, use:

```text
west robot --runner=renode-robot --renode-robot-help
```

## [Simulating a board with: `west simulate`](#id43)

### [Basics](#id44)

Currently the command supports only one runner which is using Renode,
but can be easily extended by adding other runners.

From a Zephyr build directory, to run the built binary:

```text
west simulate --runner=renode
```

This will start Renode and configure simulation based on a default `.resc` script
for the current platform with the zephyr.elf file loaded by default. The simulation
then can be started by typing “start” or “s” in Renode’s Monitor. This can also be
done by passing a command to Renode, using an argument provided by the runner:

> west simulate –runner=renode –renode-command start

To pass an argument to Renode itself, for example to start Renode in console mode
instead of a separate window:

> west simulate –runner=renode –renode-arg=”–console”

From that point on Renode can be used normally in both console and window modes.
For details on using Renode see [Renode - documentation](http://docs.renode.io).

### [Runner-Specific Overrides](#id45)

To view all of the available options supported by the runners, as well
as their usage information, use `--context` (or `-H`):

```text
west simulate --runner=renode --context
```

To view all available options Renode supports, use:

```text
west simulate --runner=renode --renode-help
```

## [Hacking](#id46)

This section documents the `runners.core` module used by the
flash and debug commands. This is the core abstraction used to implement
support for these features.

Warning

These APIs are provided for reference, but they are more “shared code” used
to implement multiple extension commands than a stable API.

Developers can add support for new ways to flash and debug Zephyr programs by
implementing additional runners. To get this support into upstream Zephyr, the
runner should be added into a new or existing `runners` module, and imported
from `runners/__init__.py`.

Note

The test cases in [scripts/west\_commands/tests](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/west_commands/tests) add unit test
coverage for the runners package and individual runner classes.

Please try to add tests when adding new runners. Note that if your
changes break existing test cases, CI testing on upstream pull
requests will fail.

Zephyr binary runner core interfaces

This provides the core ZephyrBinaryRunner class meant for public use,
as well as some other helpers for concrete runner classes.

class runners.core.BuildConfiguration(*build\_dir: str*)
:   This helper class provides access to build-time configuration.

    Configuration options can be read as if the object were a dict,
    either object[‘CONFIG\_FOO’] or object.get(‘CONFIG\_FOO’).

    Kconfig configuration values are available (parsed from .config).

    getboolean(*option*)
    :   If a boolean option is explicitly set to y or n,
        returns its value. Otherwise, falls back to False.

class runners.core.DeprecatedAction(*option\_strings*, *dest*, *nargs=None*, *const=None*, *default=None*, *type=None*, *choices=None*, *required=False*, *help=None*, *metavar=None*)

class runners.core.FileType(*\*values*)

exception runners.core.MissingProgram(*program*)
:   FileNotFoundError subclass for missing program dependencies.

    No significant changes from the parent FileNotFoundError; this is
    useful for explicitly signaling that the file in question is a
    program that some class requires to proceed.

    The filename attribute contains the missing program.

class runners.core.NetworkPortHelper
:   Helper class for dealing with local IP network ports.

    get\_unused\_ports(*starting\_from*)
    :   Find unused network ports, starting at given values.

        starting\_from is an iterable of ports the caller would like to use.

        The return value is an iterable of ports, in the same order, using
        the given values if they were unused, or the next sequentially
        available unused port otherwise.

        Ports may be bound between this call’s check and actual usage, so
        callers still need to handle errors involving returned ports.

class runners.core.RunnerCaps(*commands: Set[str] = <factory>*, *dev\_id: bool = False*, *flash\_addr: bool = False*, *erase: bool = False*, *reset: bool = False*, *extload: bool = False*, *tool\_opt: bool = False*, *file: bool = False*, *hide\_load\_files: bool = False*, *rtt: bool = False*)
:   This class represents a runner class’s capabilities.

    Each capability is represented as an attribute with the same
    name. Flag attributes are True or False.

    Available capabilities:

    - commands: set of supported commands; default is {‘flash’,
      ‘debug’, ‘debugserver’, ‘attach’, ‘simulate’, ‘robot’, ‘rtt’}.
    - dev\_id: whether the runner supports device identifiers, in the form of an
      -i, –dev-id option. This is useful when the user has multiple debuggers
      connected to a single computer, in order to select which one will be used
      with the command provided.
    - flash\_addr: whether the runner supports flashing to an
      arbitrary address. Default is False. If true, the runner
      must honor the –dt-flash option.
    - erase: whether the runner supports an –erase option, which
      does a mass-erase of the entire addressable flash on the target
      before flashing. On multi-core SoCs, this may only erase portions of
      flash specific the actual target core. (This option can be useful for
      things like clearing out old settings values or other subsystem state
      that may affect the behavior of the zephyr image. It is also sometimes
      needed by SoCs which have flash-like areas that can’t be sector
      erased by the underlying tool before flashing; UICR on nRF SoCs
      is one example.)
    - reset: whether the runner supports a –reset option, which
      resets the device after a flash operation is complete.
    - extload: whether the runner supports a –extload option, which
      must be given one time and is passed on to the underlying tool
      that the runner wraps.
    - tool\_opt: whether the runner supports a –tool-opt (-O) option, which
      can be given multiple times and is passed on to the underlying tool
      that the runner wraps.
    - file: whether the runner supports a –file option, which specifies
      exactly the file that should be used to flash, overriding any default
      discovered in the build directory.
    - hide\_load\_files: whether the elf/hex/bin file arguments should be hidden.
    - rtt: whether the runner supports SEGGER RTT. This adds a –rtt-address
      option.

class runners.core.RunnerConfig(*build\_dir: str*, *board\_dir: str*, *elf\_file: str | None*, *exe\_file: str | None*, *hex\_file: str | None*, *bin\_file: str | None*, *uf2\_file: str | None*, *file: str | None*, *file\_type: [FileType](#runners.core.FileType) | None = FileType.OTHER*, *gdb: str | None = None*, *openocd: str | None = None*, *openocd\_search: List[str] = []*, *rtt\_address: int | None = None*)
:   Runner execution-time configuration.

    This is a common object shared by all runners. Individual runners
    can register specific configuration options using their
    do\_add\_parser() hooks.

    bin\_file: str | None
    :   Alias for field number 5

    board\_dir: str
    :   Alias for field number 1

    build\_dir: str
    :   Alias for field number 0

    elf\_file: str | None
    :   Alias for field number 2

    exe\_file: str | None
    :   Alias for field number 3

    file: str | None
    :   Alias for field number 7

    file\_type: [FileType](#runners.core.FileType) | None
    :   Alias for field number 8

    gdb: str | None
    :   Alias for field number 9

    hex\_file: str | None
    :   Alias for field number 4

    openocd: str | None
    :   Alias for field number 10

    openocd\_search: List[str]
    :   Alias for field number 11

    rtt\_address: int | None
    :   Alias for field number 12

    uf2\_file: str | None
    :   Alias for field number 6

class runners.core.SysbuildConfiguration(*build\_dir: str*)
:   This helper class provides access to sysbuild-time configuration.

    Configuration options can be read as if the object were a dict,
    either object[‘SB\_CONFIG\_FOO’] or object.get(‘SB\_CONFIG\_FOO’).

    Kconfig configuration values are available (parsed from .config).

class runners.core.ZephyrBinaryRunner(*cfg: [RunnerConfig](#runners.core.RunnerConfig)*)
:   Abstract superclass for binary runners (flashers, debuggers).

    **Note**: this class’s API has changed relatively rarely since it
    as added, but it is not considered a stable Zephyr API, and may change
    without notice.

    With some exceptions, boards supported by Zephyr must provide
    generic means to be flashed (have a Zephyr firmware binary
    permanently installed on the device for running) and debugged
    (have a breakpoint debugger and program loader on a host
    workstation attached to a running target).

    This is supported by four top-level commands managed by the
    Zephyr build system:

    - ‘flash’: flash a previously configured binary to the board,
      start execution on the target, then return.
    - ‘debug’: connect to the board via a debugging protocol, program
      the flash, then drop the user into a debugger interface with
      symbol tables loaded from the current binary, and block until it
      exits.
    - ‘debugserver’: connect via a board-specific debugging protocol,
      then reset and halt the target. Ensure the user is now able to
      connect to a debug server with symbol tables loaded from the
      binary.
    - ‘attach’: connect to the board via a debugging protocol, then drop
      the user into a debugger interface with symbol tables loaded from
      the current binary, and block until it exits. Unlike ‘debug’, this
      command does not program the flash.

    This class provides an API for these commands. Every subclass is
    called a ‘runner’ for short. Each runner has a name (like
    ‘pyocd’), and declares commands it can handle (like
    ‘flash’). Boards (like ‘nrf52dk/nrf52832’) declare which runner(s)
    are compatible with them to the Zephyr build system, along with
    information on how to configure the runner to work with the board.

    The build system will then place enough information in the build
    directory to create and use runners with this class’s create()
    method, which provides a command line argument parsing API. You
    can also create runners by instantiating subclasses directly.

    In order to define your own runner, you need to:

    1. Define a ZephyrBinaryRunner subclass, and implement its
       abstract methods. You may need to override capabilities().
    2. Make sure the Python module defining your runner class is
       imported, e.g. by editing this package’s \_\_init\_\_.py (otherwise,
       get\_runners() won’t work).
    3. Give your runner’s name to the Zephyr build system in your
       board’s board.cmake.

    Additional advice:

    - If you need to import any non-standard-library modules, make sure
      to catch ImportError and defer complaints about it to a RuntimeError
      if one is missing. This avoids affecting users that don’t require your
      runner, while still making it clear what went wrong to users that do
      require it that don’t have the necessary modules installed.
    - If you need to ask the user something (e.g. using input()), do it
      in your create() classmethod, not do\_run(). That ensures your
      \_\_init\_\_() really has everything it needs to call do\_run(), and also
      avoids calling input() when not instantiating within a command line
      application.
    - Use self.logger to log messages using the standard library’s
      logging API; your logger is named “runner.<your-runner-name()>”

    For command-line invocation from the Zephyr build system, runners
    define their own argparse-based interface through the common
    add\_parser() (and runner-specific do\_add\_parser() it delegates
    to), and provide a way to create instances of themselves from
    a RunnerConfig and parsed runner-specific arguments via create().

    Runners use a variety of host tools and configuration values, the
    user interface to which is abstracted by this class. Each runner
    subclass should take any values it needs to execute one of these
    commands in its constructor. The actual command execution is
    handled in the run() method.

    classmethod add\_parser(*parser*)
    :   Adds a sub-command parser for this runner.

        The given object, parser, is a sub-command parser from the
        argparse module. For more details, refer to the documentation
        for argparse.ArgumentParser.add\_subparsers().

        The lone common optional argument is:

        - –dt-flash (if the runner capabilities includes flash\_addr)

        Runner-specific options are added through the do\_add\_parser()
        hook.

    classmethod args\_from\_previous\_runner(*previous\_runner*, *args: Namespace*)
    :   Update arguments from a previously created runner.

        This is intended for propagating relevant user responses
        between multiple runs of the same runner, for example a
        JTAG serial number.

    property build\_conf: [BuildConfiguration](#runners.core.BuildConfiguration)
    :   Get a BuildConfiguration for the build directory.

    call(*cmd: List[str]*, *\*\*kwargs*) → int
    :   Subclass subprocess.call() wrapper.

        Subclasses should use this method to run command in a
        subprocess and get its return code, rather than
        using subprocess directly, to keep accurate debug logs.

    classmethod capabilities() → [RunnerCaps](#runners.core.RunnerCaps)
    :   Returns a RunnerCaps representing this runner’s capabilities.

        This implementation returns the default capabilities.

        Subclasses should override appropriately if needed.

    cfg
    :   RunnerConfig for this instance.

    check\_call(*cmd: List[str]*, *\*\*kwargs*)
    :   Subclass subprocess.check\_call() wrapper.

        Subclasses should use this method to run command in a
        subprocess and check that it executed correctly, rather than
        using subprocess directly, to keep accurate debug logs.

    check\_output(*cmd: List[str]*, *\*\*kwargs*) → bytes
    :   Subclass subprocess.check\_output() wrapper.

        Subclasses should use this method to run command in a
        subprocess and check that it executed correctly, rather than
        using subprocess directly, to keep accurate debug logs.

    classmethod create(*cfg: [RunnerConfig](#runners.core.RunnerConfig)*, *args: Namespace*) → [ZephyrBinaryRunner](#runners.core.ZephyrBinaryRunner)
    :   Create an instance from command-line arguments.

        - `cfg`: runner configuration (pass to superclass \_\_init\_\_)
        - `args`: arguments parsed from execution environment, as
          specified by `add_parser()`.

    classmethod dev\_id\_help() → str
    :   Get the ArgParse help text for the –dev-id option.

    abstractmethod classmethod do\_add\_parser(*parser*)
    :   Hook for adding runner-specific options.

    abstractmethod classmethod do\_create(*cfg: [RunnerConfig](#runners.core.RunnerConfig)*, *args: Namespace*) → [ZephyrBinaryRunner](#runners.core.ZephyrBinaryRunner)
    :   Hook for instance creation from command line arguments.

    abstractmethod do\_run(*command: str*, *\*\*kwargs*)
    :   Concrete runner; run() delegates to this. Implement in subclasses.

        In case of an unsupported command, raise a ValueError.

    ensure\_output(*output\_type: str*) → None
    :   Ensure self.cfg has a particular output artifact.

        For example, ensure\_output(‘bin’) ensures that self.cfg.bin\_file
        refers to an existing file. Errors out if it’s missing or undefined.

        Parameters:
        :   **output\_type** – string naming the output type

    classmethod extload\_help() → str
    :   Get the ArgParse help text for the –extload option.

    static flash\_address\_from\_build\_conf(*build\_conf: [BuildConfiguration](#runners.core.BuildConfiguration)*)
    :   If CONFIG\_HAS\_FLASH\_LOAD\_OFFSET is n in build\_conf,
        return the CONFIG\_FLASH\_BASE\_ADDRESS value. Otherwise, return
        CONFIG\_FLASH\_BASE\_ADDRESS + CONFIG\_FLASH\_LOAD\_OFFSET.

    static get\_flash\_address(*args: Namespace*, *build\_conf: [BuildConfiguration](#runners.core.BuildConfiguration)*, *default: int = 0*) → int
    :   Helper method for extracting a flash address.

        If args.dt\_flash is true, returns the address obtained from
        ZephyrBinaryRunner.flash\_address\_from\_build\_conf(build\_conf).

        Otherwise (when args.dt\_flash is False), the default value is
        returned.

    get\_rtt\_address() → int | None
    :   Helper method for extracting a the RTT control block address.

        If args.rtt\_address was supplied, returns that.

        Otherwise, attempt to locate an rtt block in the elf file.
        If this is not found, None is returned

    static get\_runners() → List[Type[[ZephyrBinaryRunner](#runners.core.ZephyrBinaryRunner)]]
    :   Get a list of all currently defined runner classes.

    logger
    :   logging.Logger for this instance.

    abstractmethod classmethod name() → str
    :   Return this runner’s user-visible name.

        When choosing a name, pick something short and lowercase,
        based on the name of the tool (like openocd, jlink, etc.) or
        the target architecture/board (like xtensa etc.).

    popen\_ignore\_int(*cmd: List[str]*, *\*\*kwargs*) → Popen
    :   Spawn a child command, ensuring it ignores SIGINT.

        The returned subprocess.Popen object must be manually terminated.

    static require(*program: str*, *path: str | None = None*) → str
    :   Require that a program is installed before proceeding.

        Parameters:
        :   - **program** – name of the program that is required,
              or path to a program binary.
            - **path** – PATH where to search for the program binary.
              By default check on the system PATH.

        If `program` is an absolute path to an existing program
        binary, this call succeeds. Otherwise, try to find the program
        by name on the system PATH or in the given PATH, if provided.

        If the program can be found, its path is returned.
        Otherwise, raises MissingProgram.

    run(*command: str*, *\*\*kwargs*)
    :   Runs command (‘flash’, ‘debug’, ‘debugserver’, ‘attach’).

        This is the main entry point to this runner.

    run\_client(*client*, *\*\*kwargs*)
    :   Run a client that handles SIGINT.

    run\_server\_and\_client(*server*, *client*, *\*\*kwargs*)
    :   Run a server that ignores SIGINT, and a client that handles it.

        This routine portably:

        - creates a Popen object for the `server` command which ignores
          SIGINT
        - runs `client` in a subprocess while temporarily ignoring SIGINT
        - cleans up the server after the client exits.
        - the keyword arguments, if any, will be passed down to both server and
          client subprocess calls

        It’s useful to e.g. open a GDB server and client.

    run\_telnet\_client(*host: str*, *port: int*) → None
    :   Run a telnet client for user interaction.

    property sysbuild\_conf: [SysbuildConfiguration](#runners.core.SysbuildConfiguration)
    :   Get a SysbuildConfiguration for the sysbuild directory.

    property thread\_info\_enabled: bool
    :   Returns True if self.build\_conf has
        CONFIG\_DEBUG\_THREAD\_INFO enabled.

    classmethod tool\_opt\_help() → str
    :   Get the ArgParse help text for the –tool-opt option.

## [Doing it By Hand](#id47)

If you prefer not to use West to flash or debug your board, simply
inspect the build directory for the binaries output by the build
system. These will be named something like `zephyr/zephyr.elf`,
`zephyr/zephyr.hex`, etc., depending on your board’s build system
integration. These binaries may be flashed to a board using
alternative tools of your choice, or used for debugging as needed,
e.g. as a source of symbol tables.

By default, these West commands rebuild binaries before flashing and
debugging. This can of course also be accomplished using the usual
targets provided by Zephyr’s build system (in fact, that’s how these
commands do it).
