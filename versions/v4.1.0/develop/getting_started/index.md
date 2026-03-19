---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/getting_started/index.html
original_path: develop/getting_started/index.html
---

# Getting Started Guide

Follow this guide to:

- Set up a command-line Zephyr development environment on Ubuntu, macOS, or
  Windows (instructions for other Linux distributions are discussed in
  [Install Linux Host Dependencies](installation_linux.md#installation-linux))
- Get the source code
- Build, flash, and run a sample application

## Select and Update OS

Click the operating system you are using.

UbuntumacOSWindows

This guide covers Ubuntu version 20.04 LTS and later.
If you are using a different Linux distribution see [Install Linux Host Dependencies](installation_linux.md#installation-linux).

```shell
sudo apt update
sudo apt upgrade
```

On macOS Mojave or later, select *System Preferences* >
*Software Update*. Click *Update Now* if necessary.

On other versions, see [this Apple support topic](https://support.apple.com/en-us/HT201541).

Select *Start* > *Settings* > *Update & Security* > *Windows Update*.
Click *Check for updates* and install any that are available.

## Install dependencies

Next, you’ll install some host dependencies using your package manager.

The current minimum required version for the main dependencies are:

| Tool | Min. Version |
| --- | --- |
| [CMake](https://cmake.org/) | 3.20.5 |
| [Python](https://www.python.org/) | 3.10 |
| [Devicetree compiler](https://www.devicetree.org/) | 1.4.6 |

UbuntumacOSWindows

1. If using an Ubuntu version older than 22.04, it is necessary to add extra
   repositories to meet the minimum required versions for the main
   dependencies listed above. In that case, download, inspect and execute
   the Kitware archive script to add the Kitware APT repository to your
   sources list.
   A detailed explanation of `kitware-archive.sh` can be found here
   [kitware third-party apt repository](https://apt.kitware.com/):

   ```shell
   wget https://apt.kitware.com/kitware-archive.sh
   sudo bash kitware-archive.sh
   ```
2. Use `apt` to install the required dependencies:

   ```shell
   sudo apt install --no-install-recommends git cmake ninja-build gperf \
     ccache dfu-util device-tree-compiler wget \
     python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
     make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
   ```

   Note

   Due to the unavailability of `gcc-multilib` and `g++-multilib` on AArch64
   (ARM64) systems, you may need to remove them from the list of packages to install.
3. Verify the versions of the main dependencies installed on your system by entering:

   ```shell
   cmake --version
   python3 --version
   dtc --version
   ```

   Check those against the versions in the table in the beginning of this section.
   Refer to the [Install Linux Host Dependencies](installation_linux.md#installation-linux) page for additional information on updating
   the dependencies manually.

1. Install [Homebrew](https://brew.sh/):

   ```shell
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. After the Homebrew installation script completes, follow the on-screen
   instructions to add the Homebrew installation to the path.

   - On macOS running on Apple Silicon, this is achieved with:

     ```shell
     (echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> ~/.zprofile
     source ~/.zprofile
     ```
   - On macOS running on Intel, use the command for Apple Silicon, but replace `/opt/homebrew/` with `/usr/local/`.
3. Use `brew` to install the required dependencies:

   ```shell
   brew install cmake ninja gperf python3 python-tk ccache qemu dtc libmagic wget openocd
   ```
4. Add the Homebrew Python folder to the path, in order to be able to
   execute `python` and `pip` as well `python3` and `pip3`.

   > ```shell
   > (echo; echo 'export PATH="'$(brew --prefix)'/opt/python/libexec/bin:$PATH"') >> ~/.zprofile
   > source ~/.zprofile
   > ```

Note

Due to issues finding executables, the Zephyr Project doesn’t
currently support application flashing using the [Windows Subsystem
for Linux (WSL)](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
(WSL).

Therefore, we don’t recommend using WSL when getting started.

In modern version of Windows (10 and later) it is recommended to install the Windows Terminal
application from the Microsoft Store. Instructions are provided for a `cmd.exe` or
PowerShell command prompts.

These instructions rely on [Chocolatey](https://chocolatey.org/). If Chocolatey isn’t an option,
you can install dependencies from their respective websites and ensure
the command line tools are on your [`PATH`](../env_vars.md#envvar-PATH) [environment
variable](../env_vars.md#env-vars).

1. [Install chocolatey](https://chocolatey.org/install).
2. Open a `cmd.exe` or PowerShell terminal window as **Administrator**.
   To do so, press the Windows key, type `cmd.exe` or PowerShell, right-click the
   Command Prompt or PowerShell search result, and choose
   Run as Administrator.
3. Disable global confirmation to avoid having to confirm the
   installation of individual programs:

   ```bat
   choco feature enable -n allowGlobalConfirmation
   ```
4. Use `choco` to install the required dependencies:

   ```bat
   choco install cmake --installargs 'ADD_CMAKE_TO_PATH=System'
   choco install ninja gperf python311 git dtc-msys2 wget 7zip strawberryperl
   ```

   Warning

   As of November 2024, Python 3.13 is not recommended for Zephyr development on Windows,
   as some required Python dependencies may be difficult to install.
5. Close the terminal window.

## Get Zephyr and install Python dependencies

Next, clone Zephyr and its [modules](../modules.md#modules) into a new [west](../west/index.md#west) workspace. In the following instructions the name `zephyrproject`
is used for the workspace, however in practice its name and location can be freely
chosen. You’ll also install Zephyr’s additional Python dependencies in a
[Python virtual environment](https://docs.python.org/3/library/venv.html).

UbuntumacOSWindows

1. Use `apt` to install Python `venv` package:

   ```shell
   sudo apt install python3-venv
   ```
2. Create a new virtual environment:

   ```shell
   python3 -m venv ~/zephyrproject/.venv
   ```
3. Activate the virtual environment:

   ```shell
   source ~/zephyrproject/.venv/bin/activate
   ```

   Once activated your shell will be prefixed with `(.venv)`. The
   virtual environment can be deactivated at any time by running
   `deactivate`.

   Note

   Remember to activate the virtual environment every time you
   start working.
4. Install west:

   ```shell
   pip install west
   ```
5. Get the Zephyr source code:

   ```shell
   west init ~/zephyrproject
   cd ~/zephyrproject
   west update
   ```
6. Export a [Zephyr CMake package](../../build/zephyr_cmake_package.md#cmake-pkg). This allows CMake to
   automatically load boilerplate code required for building Zephyr
   applications.

   ```shell
   west zephyr-export
   ```
7. The Zephyr west extension command, `west packages` can be used to install Python
   dependencies.

   ```shell
   west packages pip --install
   ```

1. Create a new virtual environment:

   ```shell
   python3 -m venv ~/zephyrproject/.venv
   ```
2. Activate the virtual environment:

   ```shell
   source ~/zephyrproject/.venv/bin/activate
   ```

   Once activated your shell will be prefixed with `(.venv)`. The
   virtual environment can be deactivated at any time by running
   `deactivate`.

   Note

   Remember to activate the virtual environment every time you
   start working.
3. Install west:

   ```shell
   pip install west
   ```
4. Get the Zephyr source code:

   ```shell
   west init ~/zephyrproject
   cd ~/zephyrproject
   west update
   ```
5. Export a [Zephyr CMake package](../../build/zephyr_cmake_package.md#cmake-pkg). This allows CMake to
   automatically load boilerplate code required for building Zephyr
   applications.

   ```shell
   west zephyr-export
   ```
6. The Zephyr west extension command, `west packages` can be used to install Python
   dependencies.

   ```shell
   west packages pip --install
   ```

1. Open a `cmd.exe` or PowerShell terminal window **as a regular user**
2. Create a new virtual environment:

   BatchfilePowerShell

   ```bat
   cd %HOMEPATH%
   python -m venv zephyrproject\.venv
   ```

   ```powershell
   cd $Env:HOMEPATH
   python -m venv zephyrproject\.venv
   ```
3. Activate the virtual environment:

   BatchfilePowerShell

   ```bat
   zephyrproject\.venv\Scripts\activate.bat
   ```

   ```powershell
   zephyrproject\.venv\Scripts\Activate.ps1
   ```

   Once activated your shell will be prefixed with `(.venv)`. The
   virtual environment can be deactivated at any time by running
   `deactivate`.

   Note

   Remember to activate the virtual environment every time you
   start working.
4. Install west:

   ```bat
   pip install west
   ```
5. Get the Zephyr source code:

   ```bat
   west init zephyrproject
   cd zephyrproject
   west update
   ```
6. Export a [Zephyr CMake package](../../build/zephyr_cmake_package.md#cmake-pkg). This allows CMake to
   automatically load boilerplate code required for building Zephyr
   applications.

   ```bat
   west zephyr-export
   ```
7. The Zephyr west extension command, `west packages` can be used to install Python
   dependencies.

   ```bat
   west packages pip --install
   ```

## Install the Zephyr SDK

The [Zephyr Software Development Kit (SDK)](../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk)
contains toolchains for each of Zephyr’s supported architectures, which
include a compiler, assembler, linker and other programs required to build
Zephyr applications.

For Linux, it also contains additional host tools, such as custom QEMU and OpenOCD builds
that are used to emulate, flash and debug Zephyr applications.

UbuntumacOSWindows

Install the Zephyr SDK using the `west sdk install`.

> ```shell
> cd ~/zephyrproject/zephyr
> west sdk install
> ```

Tip

Using the command options, you can specify the SDK installation destination
and which architecture of toolchains to install.
See `west sdk install --help` for details.

Install the Zephyr SDK using the `west sdk install`.

> ```shell
> cd ~/zephyrproject/zephyr
> west sdk install
> ```

Tip

Using the command options, you can specify the SDK installation destination
and which architecture of toolchains to install.
See `west sdk install --help` for details.

Install the Zephyr SDK using the `west sdk install`.

> BatchfilePowerShell
>
> ```bat
> cd %HOMEPATH%\zephyrproject\zephyr
> west sdk install
> ```
>
> ```powershell
> cd $Env:HOMEPATH\zephyrproject\zephyr
> west sdk install
> ```

Tip

Using the command options, you can specify the SDK installation destination
and which architecture of toolchains to install.
See `west sdk install --help` for details.

Note

If you want to install Zephyr SDK without using the `west sdk` command,
please see [Zephyr SDK installation](../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk-install).

## Build the Blinky Sample

Note

[Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") is compatible with most, but not all, [Supported Boards and Shields](../../boards/index.md#boards). If your board
does not meet Blinky’s [Requirements](../../samples/basic/blinky/README.md#blinky-sample-requirements), then
[Hello World](../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is a good alternative.

If you are unsure what name west uses for your board, `west boards`
can be used to obtain a list of all boards Zephyr supports.

Build the [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") with [west build](../west/build-flash-debug.md#west-building), changing
`<your-board-name>` appropriately for your board:

UbuntumacOSWindows

```shell
cd ~/zephyrproject/zephyr
west build -p always -b <your-board-name> samples/basic/blinky
```

```shell
cd ~/zephyrproject/zephyr
west build -p always -b <your-board-name> samples/basic/blinky
```

BatchfilePowerShell

```bat
cd %HOMEPATH%\zephyrproject\zephyr
west build -p always -b <your-board-name> samples\basic\blinky
```

```powershell
cd $Env:HOMEPATH\zephyrproject\zephyr
west build -p always -b <your-board-name> samples\basic\blinky
```

The `-p always` option forces a pristine build, and is recommended for new
users. Users may also use the `-p auto` option, which will use
heuristics to determine if a pristine build is required, such as when building
another sample.

Note

A board may contain one or multiple SoCs, Also, each SoC may contain one or
more CPU clusters.
When building for such boards it is necessary to specify the SoC or CPU
cluster for which the sample must be built.
For example to build [Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") for the `cpuapp` core on
the [nRF5340DK](../../boards/nordic/nrf5340dk/doc/index.md#nrf5340dk-nrf5340) the board must be provided as:
`nrf5340dk/nrf5340/cpuapp`. See also [Board terminology](../../hardware/porting/board_porting.md#board-terminology) for more
details.

## Flash the Sample

Connect your board, usually via USB, and turn it on if there’s a power switch.
If in doubt about what to do, check your board’s page in [Supported Boards and Shields](../../boards/index.md#boards).

Then flash the sample using [west flash](../west/build-flash-debug.md#west-flashing):

```shell
west flash
```

Note

You may need to install additional [host tools](../flash_debug/host-tools.md#flash-debug-host-tools)
required by your board. The `west flash` command will print an error if any
required dependencies are missing.

Note

When using Linux, you may need to configure udev rules the first time
of using a debug probe.
Please also see [Setting udev rules](../beyond-GSG.md#setting-udev-rules).

If you’re using blinky, the LED will start to blink as shown in this figure:

[![../../_images/ReelBoard-Blinky.png](../../_images/ReelBoard-Blinky.png)
](../../_images/ReelBoard-Blinky.png)

Phytec [reel\_board](../../boards/phytec/reel_board/doc/index.md#reel-board) running blinky

## Next Steps

Here are some next steps for exploring Zephyr:

- Try other [Samples and Demos](../../samples/index.md#samples)
- Learn about [Application Development](../application/index.md#application) and the [west](../west/index.md#west) tool
- Find out about west’s [flashing and debugging](../west/build-flash-debug.md#west-build-flash-debug)
  features, or more about [Flashing and Hardware Debugging](../flash_debug/index.md#flashing-and-debugging) in general
- Check out [Beyond the Getting Started Guide](../beyond-GSG.md#beyond-gsg) for additional setup alternatives and ideas
- Discover [Resources](../../introduction/index.md#project-resources) for getting help from the Zephyr
  community

## Troubleshooting Installation

Here are some tips for fixing some issues related to the installation process.

### Double Check the Zephyr SDK Variables When Updating

When updating Zephyr SDK, check whether the [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT)
or [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) environment variables are already set.
See [Updating the Zephyr SDK toolchain](../beyond-GSG.md#gs-toolchain-update) for more information.

For more information about these environment variables in Zephyr, see [Important Environment Variables](../env_vars.md#env-vars-important).

## Asking for Help

You can ask for help on a mailing list or on Discord. Please send bug reports and
feature requests to GitHub.

- **Mailing Lists**: [users@lists.zephyrproject.org](mailto:users%40lists.zephyrproject.org) is usually the right list to
  ask for help. [Search archives and sign up here](https://lists.zephyrproject.org/g/users).
- **Discord**: You can join with this [Discord invite](https://chat.zephyrproject.org).
- **GitHub**: Use [GitHub issues](https://github.com/zephyrproject-rtos/zephyr/issues) for bugs and feature requests.

### How to Ask

Important

Please search this documentation and the mailing list archives first. Your
question may have an answer there.

Don’t just say “this isn’t working” or ask “is this working?”. Include as much
detail as you can about:

1. What you want to do
2. What you tried (commands you typed, etc.)
3. What happened (output of each command, etc.)

### Use Copy/Paste

Please **copy/paste text** instead of taking a picture or a screenshot of it.
Text includes source code, terminal commands, and their output.

Doing this makes it easier for people to help you, and also helps other users
search the archives. Unnecessary screenshots exclude vision impaired
developers; some are major Zephyr contributors. [Accessibility](https://www.w3.org/standards/webdesign/accessibility) has been
recognized as a basic human right by the United Nations.

When copy/pasting more than 5 lines of computer text into Discord or Github,
create a snippet using three backticks to delimit the snippet.
