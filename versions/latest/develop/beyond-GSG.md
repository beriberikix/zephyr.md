---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/beyond-GSG.html
original_path: develop/beyond-GSG.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Beyond the Getting Started Guide

The [Getting Started Guide](getting_started/index.md#getting-started) gives a straight-forward path to set up
your Linux, macOS, or Windows environment for Zephyr development. In
this document, we delve deeper into Zephyr development setup
issues and alternatives.

## Python and pip

Python 3 and its package manager, pip[[1]](#pip), are used extensively by Zephyr
to install and run scripts required to compile and run Zephyr
applications, set up and maintain the Zephyr development environment,
and build project documentation.

Depending on your operating system, you may need to provide the
`--user` flag to the `pip3` command when installing new packages. This is
documented throughout the instructions.
See [Installing Packages](https://packaging.python.org/tutorials/installing-packages/) in the Python Packaging User Guide for more
information about pip[[1]](#pip), including [information on -\-user](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site).

- On Linux, make sure `~/.local/bin` is at the front of your [`PATH`](env_vars.md#envvar-PATH)
  [environment variable](env_vars.md#env-vars), or programs installed with `--user`
  won’t be found. Installing with `--user` avoids conflicts between pip
  and the system package manager, and is the default on Debian-based
  distributions.
- On macOS, [Homebrew disables -\-user](https://docs.brew.sh/Homebrew-and-Python#note-on-pip-install---user).
- On Windows, see the [Installing Packages](https://packaging.python.org/tutorials/installing-packages/) information on `--user` if you
  require using this option.

On all operating systems, pip’s `-U` flag installs or updates the package if the
package is already installed locally but a more recent version is available. It
is good practice to use this flag if the latest version of a package is
required. (Check the [scripts/requirements.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/requirements.txt) file to
see if a specific Python package version is expected.)

## Advanced Platform Setup

Here are some alternative instructions for more advanced platform setup
configurations for supported development platforms:

## Install a Toolchain

Zephyr binaries are compiled and linked by a *toolchain* comprised of
a cross-compiler and related tools which are different from the compiler
and tools used for developing software that runs natively on your host
operating system.

You can install the [Zephyr SDK](toolchains/zephyr_sdk.md#toolchain-zephyr-sdk) to get toolchains for all
supported architectures, or install an [alternate toolchain](toolchains/index.md#toolchains)
recommended by the SoC vendor or a specific board (check your specific
[board-level documentation](../boards/index.md#boards)).

You can configure the Zephyr build system to use a specific toolchain by
setting [environment variables](env_vars.md#env-vars) such as
[`ZEPHYR_TOOLCHAIN_VARIANT`](env_vars.md#envvar-TOOLCHAIN-_TOOLCHAIN_PATH) to a supported
value, along with additional variable(s) specific to the toolchain variant.

## Updating the Zephyr SDK toolchain

When updating Zephyr SDK, check whether the [`ZEPHYR_TOOLCHAIN_VARIANT`](env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
or [`ZEPHYR_SDK_INSTALL_DIR`](env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) environment variables are already set.

- If the variables are not set, the latest compatible version of Zephyr SDK will be selected
  by default. Proceed to next step without making any changes.
- If [`ZEPHYR_TOOLCHAIN_VARIANT`](env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) is set, the corresponding toolchain will be selected
  at build time. Zephyr SDK is identified by the value `zephyr`.
  If the [`ZEPHYR_TOOLCHAIN_VARIANT`](env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) environment variable is not `zephyr`, then either
  unset it or change its value to `zephyr` to make sure Zephyr SDK is selected.
- If the [`ZEPHYR_SDK_INSTALL_DIR`](env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) environment variable is set, it will override
  the default lookup location for Zephyr SDK. If you install Zephyr SDK to one
  of the [recommended locations](toolchains/zephyr_sdk.md#toolchain-zephyr-sdk-bundle-variables),
  you can unset this variable. Otherwise, set it to your chosen install location.

For more information about these environment variables in Zephyr, see [Important Environment Variables](env_vars.md#env-vars-important).

## Cloning the Zephyr Repositories

The Zephyr project source is maintained in the [GitHub zephyr repo](https://github.com/zephyrproject-rtos/zephyr). External modules used
by Zephyr are found in the parent [GitHub Zephyr project](https://github.com/zephyrproject-rtos/). Because of these
dependencies, it’s convenient to use the Zephyr-created [west](west/index.md#west) tool to fetch and manage the Zephyr and external module source
code. See [Basics](west/basics.md#west-basics) for more details.

Once your development tools are installed, use [West (Zephyr’s meta-tool)](west/index.md#west) to create,
initialize, and download sources from the zephyr and external module
repos. We’ll use the name `zephyrproject`, but you can choose any
name that does not contain a space anywhere in the path.

```shell
west init zephyrproject
cd zephyrproject
west update
```

The `west update` command fetches and keeps [Modules (External projects)](modules.md#modules) in the
`zephyrproject` folder in sync with the code in the local zephyr
repo.

Warning

You must run `west update` any time the `zephyr/west.yml`
changes, caused, for example, when you pull the `zephyr`
repository, switch branches in it, or perform a `git bisect` inside of
it.

### Keeping Zephyr updated

To update the Zephyr project source code, you need to get the latest
changes via `git`. Afterwards, run `west update` as mentioned in
the previous paragraph.

```shell
# replace zephyrproject with the path you gave west init
cd zephyrproject/zephyr
git pull
west update
```

## Export Zephyr CMake package

The [Zephyr CMake Package](../build/zephyr_cmake_package.md#cmake-pkg) can be exported to CMake’s user package registry if it has
not already been done as part of [Getting Started Guide](getting_started/index.md#getting-started).

## Board Aliases

Developers who work with multiple boards may find explicit board names
cumbersome and want to use aliases for common targets. This is
supported by a CMake file with content like this:

```cmake
# Variable foo_BOARD_ALIAS=bar replaces BOARD=foo with BOARD=bar and
# sets BOARD_ALIAS=foo in the CMake cache.
set(pca10028_BOARD_ALIAS nrf51dk_nrf51422)
set(pca10056_BOARD_ALIAS nrf52840dk_nrf52840)
set(k64f_BOARD_ALIAS frdm_k64f)
set(sltb004a_BOARD_ALIAS efr32mg_sltb004a)
```

and specifying its location in [`ZEPHYR_BOARD_ALIASES`](env_vars.md#envvar-ZEPHYR_BOARD_ALIASES). This
enables use of aliases `pca10028` in contexts like
`cmake -DBOARD=pca10028` and `west -b pca10028`.

## Build and Run an Application

You can build, flash, and run Zephyr applications on real
hardware using a supported host system. Depending on your operating system,
you can also run it in emulation with QEMU, or as a native application with
[native\_sim](../boards/posix/native_sim/doc/index.md#native-sim).
Additional information about building applications can be found in the
[Building an Application](application/index.md#build-an-application) section.

### Build Blinky

Let’s build the [Blinky](../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

Zephyr applications are built to run on specific hardware, called a
“board”[[2]](#board-misnomer). We’ll use the Phytec [reel\_board](../boards/arm/reel_board/doc/index.md#reel-board) here, but you can change the `reel_board` build target
to another value if you have a different board. See [Supported Boards](../boards/index.md#boards) or run
`west boards` from anywhere inside the `zephyrproject` directory for
a list of supported boards.

1. Go to the zephyr repository:

   ```shell
   cd zephyrproject/zephyr
   ```
2. Build the blinky sample for the `reel_board`:

   ```shell
   west build -b reel_board samples/basic/blinky
   ```

The main build products will be in `build/zephyr`;
`build/zephyr/zephyr.elf` is the blinky application binary in ELF
format. Other binary formats, disassembly, and map files may be present
depending on your board.

The other sample applications in the [samples](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples) folder are
documented in [Samples and Demos](../samples/index.md#samples-and-demos).

Note

If you want to reuse an
existing build directory for another board or application, you need to
add the parameter `-p=auto` to `west build` to clean out settings
and artifacts from the previous build.

### Run the Application by Flashing to a Board

Most hardware boards supported by Zephyr can be flashed by running
`west flash`. This may require board-specific tool installation and
configuration to work properly.

See [Run an Application](application/index.md#application-run) and your specific board’s documentation in
[Supported Boards](../boards/index.md#boards) for additional details.

### Setting udev rules

Flashing a board requires permission to directly access the board
hardware, usually managed by installation of the flashing tools. On
Linux systems, if the `west flash` command fails, you likely need to
define udev rules to grant the needed access permission.

Udev is a device manager for the Linux kernel and the udev daemon
handles all user space events raised when a hardware device is added (or
removed) from the system. We can add a rules file to grant access
permission by non-root users to certain USB-connected devices.

The OpenOCD (On-Chip Debugger) project conveniently provides a rules
file that defined board-specific rules for most Zephyr-supported
arm-based boards, so we recommend installing this rules
file by downloading it from their sourceforge repo, or if you’ve
installed the Zephyr SDK there is a copy of this rules file in the SDK
folder:

- Either download the OpenOCD rules file and copy it to the right
  location:

  ```text
  wget -O 60-openocd.rules https://sf.net/p/openocd/code/ci/master/tree/contrib/60-openocd.rules?format=raw
  sudo cp 60-openocd.rules /etc/udev/rules.d
  ```
- or copy the rules file from the Zephyr SDK folder:

  ```text
  sudo cp ${ZEPHYR_SDK_INSTALL_DIR}/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
  ```

Then, in either case, ask the udev daemon to reload these rules:

```text
sudo udevadm control --reload
```

Unplug and plug in the USB connection to your board, and you should have
permission to access the board hardware for flashing. Check your
board-specific documentation ([Supported Boards](../boards/index.md#boards)) for further information if
needed.

### Run the Application in QEMU

On Linux and macOS, you can run Zephyr applications via emulation on your host
system using [QEMU](https://www.qemu.org/) when targeting either
the x86 or ARM Cortex-M3 architectures. (QEMU is included with the Zephyr
SDK installation.)

On Windows, you need to install QEMU manually from
[Download QEMU](https://www.qemu.org/download/#windows). After installation,
add path to QEMU installation folder to PATH environment variable.
To enable QEMU in Test Runner (Twister) on Windows,
[set the environment variable](env_vars.md#env-vars)
`QEMU_BIN_PATH` to the path of QEMU installation folder.

For example, you can build and run the [Hello World](../samples/hello_world/README.md#hello-world) sample using
the x86 emulation board configuration (`qemu_x86`), with:

```shell
# From the root of the zephyr repository
west build -b qemu_x86 samples/hello_world
west build -t run
```

To exit QEMU, type `Ctrl-a`, then `x`.

Use `qemu_cortex_m3` to target an emulated Arm Cortex-M3 sample.

### Run a Sample Application natively (Linux)

You can compile some samples to run as host programs
on Linux. See [Native simulator - native\_sim](../boards/posix/native_sim/doc/index.md#native-sim) for more information. On 64-bit host operating systems, you
need to install a 32-bit C library, or build targeting [native\_sim\_64](../boards/posix/native_sim/doc/index.md#native-sim32-64).

First, build Hello World for `native_sim`.

```shell
# From the root of the zephyr repository
west build -b native_sim samples/hello_world
```

Next, run the application.

```shell
west build -t run
# or just run zephyr.exe directly:
./build/zephyr/zephyr.exe
```

Press `Ctrl-C` to exit.

You can run `./build/zephyr/zephyr.exe --help` to get a list of available
options.

This executable can be instrumented using standard tools, such as gdb or
valgrind.

Footnotes

[1]
([1](#id1),[2](#id2))

pip is Python’s package installer. Its `install` command first tries to
reuse packages and package dependencies already installed on your computer.
If that is not possible, `pip install` downloads them from the Python
Package Index (PyPI) on the Internet.

The package versions requested by Zephyr’s `requirements.txt` may
conflict with other requirements on your system, in which case you may
want to set up a virtualenv for Zephyr development.

[[2](#id3)]

This has become something of a misnomer over time. While the target can be,
and often is, a microprocessor running on its own dedicated hardware
board, Zephyr also supports using QEMU to run targets built for other
architectures in emulation, targets which produce native host system
binaries that implement Zephyr’s driver interfaces with POSIX APIs, and even
running different Zephyr-based binaries on CPU cores of differing
architectures on the same physical chip. Each of these hardware
configurations is called a “board,” even though that doesn’t always make
perfect sense in context.
