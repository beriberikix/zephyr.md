---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/getting_started/installation_linux.html
original_path: develop/getting_started/installation_linux.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Install Linux Host Dependencies

Documentation is available for these Linux distributions:

- Ubuntu
- Fedora
- Clear Linux
- Arch Linux

For distributions that are not based on rolling releases, some of the
requirements and dependencies may not be met by your package manager. In that
case please follow the additional instructions that are provided to find
software from sources other than the package manager.

Note

If you’re working behind a corporate firewall, you’ll likely
need to configure a proxy for accessing the internet, if you haven’t
done so already. While some tools use the environment variables
`http_proxy` and `https_proxy` to get their proxy settings, some
use their own configuration files, most notably `apt` and
`git`.

## Update Your Operating System

Ensure your host system is up to date.

UbuntuFedoraClear LinuxArch Linux

```shell
sudo apt-get update
sudo apt-get upgrade
```

```shell
sudo dnf upgrade
```

```shell
sudo swupd update
```

```shell
sudo pacman -Syu
```

## Install Requirements and Dependencies

Note that both Ninja and Make are installed with these instructions; you only
need one.

UbuntuFedoraClear LinuxArch Linux

```shell
sudo apt-get install --no-install-recommends git cmake ninja-build gperf \
  ccache dfu-util device-tree-compiler wget \
  python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
  make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
```

```shell
sudo dnf group install "Development Tools" "C Development Tools and Libraries"
sudo dnf install cmake ninja-build gperf dfu-util dtc wget which \
  python3-pip python3-tkinter xz file python3-devel SDL2-devel
```

```shell
sudo swupd bundle-add c-basic dev-utils dfu-util dtc \
  os-core-dev python-basic python3-basic python3-tcl
```

The Clear Linux focus is on *native* performance and security and not
cross-compilation. For that reason it uniquely exports by default to the
[environment](../env_vars.md#env-vars) of all users a list of compiler and linker
flags. Zephyr’s CMake build system will either warn or fail because of
these. To clear the C/C++ flags among these and fix the Zephyr build, run
the following command as root then log out and back in:

```shell
echo 'unset CFLAGS CXXFLAGS' >> /etc/profile.d/unset_cflags.sh
```

Note this command unsets the C/C++ flags for *all users on the
system*. Each Linux distribution has a unique, relatively complex and
potentially evolving sequence of bash initialization files sourcing each
other and Clear Linux is no exception. If you need a more flexible
solution, start by looking at the logic in
`/usr/share/defaults/etc/profile`.

```shell
sudo pacman -S git cmake ninja gperf ccache dfu-util dtc wget \
    python-pip python-setuptools python-wheel tk xz file make
```

### CMake

A [recent CMake version](index.md#install-required-tools) is required. Check what
version you have by using `cmake --version`. If you have an older version,
there are several ways of obtaining a more recent one:

- On Ubuntu, you can follow the instructions for adding the
  [kitware third-party apt repository](https://apt.kitware.com/)
  to get an updated version of cmake using apt.
- Download and install a packaged cmake from the CMake project site.
  (Note this won’t uninstall the previous version of cmake.)

  ```shell
  cd ~
  wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
  chmod +x cmake-3.21.1-Linux-x86_64.sh
  sudo ./cmake-3.21.1-Linux-x86_64.sh --skip-license --prefix=/usr/local
  hash -r
  ```

  The `hash -r` command may be necessary if the installation script
  put cmake into a new location on your PATH.
- Download and install from the pre-built binaries provided by the CMake
  project itself in the [CMake Downloads](https://cmake.org/download) page.
  For example, to install version 3.21.1 in `~/bin/cmake`:

  ```shell
  mkdir $HOME/bin/cmake && cd $HOME/bin/cmake
  wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
  yes | sh cmake-3.21.1-Linux-x86_64.sh | cat
  echo "export PATH=$PWD/cmake-3.21.1-Linux-x86_64/bin:\$PATH" >> $HOME/.zephyrrc
  ```
- Use `pip3`:

  ```shell
  pip3 install --user cmake
  ```

  Note this won’t uninstall the previous version of cmake and will
  install the new cmake into your ~/.local/bin folder so
  you’ll need to add ~/.local/bin to your PATH. (See [Python and pip](../beyond-GSG.md#python-pip)
  for details.)
- Check your distribution’s beta or unstable release package library for an
  update.
- On Ubuntu you can also use snap to get the latest version available:

  ```shell
  sudo snap install cmake
  ```

After updating cmake, verify that the newly installed cmake is found
using `cmake --version`.
You might also want to uninstall the CMake provided by your package manager to
avoid conflicts. (Use `whereis cmake` to find other installed
versions.)

### DTC (Device Tree Compiler)

A [recent DTC version](index.md#install-required-tools) is required. Check what
version you have by using `dtc --version`. If you have an older version,
either install a more recent one by building from source, or use the one that is
bundled in the [Zephyr SDK](../toolchains/zephyr_sdk.md#toolchain-zephyr-sdk) by installing it.

### Python

A [modern Python 3 version](index.md#install-required-tools) is required. Check
what version you have by using `python3 --version`.

If you have an older version, you will need to install a more recent Python 3.
You can build from source, or use a backport from your distribution’s package
manager channels if one is available. Isolating this Python in a virtual
environment is recommended to avoid interfering with your system Python.

## Install the Zephyr Software Development Kit (SDK)

The Zephyr Software Development Kit (SDK) contains toolchains for each of
Zephyr’s supported architectures. It also includes additional host tools, such
as custom QEMU and OpenOCD.

Use of the Zephyr SDK is highly recommended and may even be required under
certain conditions (for example, running tests in QEMU for some architectures).

The Zephyr SDK supports the following target architectures:

- ARC (32-bit and 64-bit; ARCv1, ARCv2, ARCv3)
- ARM (32-bit and 64-bit; ARMv6, ARMv7, ARMv8; A/R/M Profiles)
- MIPS (32-bit and 64-bit)
- Nios II
- RISC-V (32-bit and 64-bit; RV32I, RV32E, RV64I)
- x86 (32-bit and 64-bit)
- Xtensa

Follow these steps to install the Zephyr SDK:

1. Download and verify the [Zephyr SDK bundle](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.5):

   ```
   wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/zephyr-sdk-0.16.5_linux-x86_64.tar.xz
   wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/sha256.sum | shasum --check --ignore-missing
   ```

   You can change `0.16.5` to another version if needed; the
   [Zephyr SDK Releases](https://github.com/zephyrproject-rtos/sdk-ng/tags) page contains all available SDK releases.

   If your host architecture is 64-bit ARM (for example, Raspberry Pi), replace
   `x86_64` with `aarch64` in order to download the 64-bit ARM Linux SDK.
2. Extract the Zephyr SDK bundle archive:

   ```
   cd <sdk download directory>
   tar xvf zephyr-sdk-0.16.5_linux-x86_64.tar.xz
   ```
3. Run the Zephyr SDK bundle setup script:

   ```
   cd zephyr-sdk-0.16.5
   ./setup.sh
   ```

   If this fails, make sure Zephyr’s dependencies were installed as described
   in [Install Requirements and Dependencies](#install-requirements-and-dependencies).

If you want to uninstall the SDK, remove the directory where you installed it.
If you relocate the SDK directory, you need to re-run the setup script.

Note

It is recommended to extract the Zephyr SDK bundle at one of the following locations:

- `$HOME`
- `$HOME/.local`
- `$HOME/.local/opt`
- `$HOME/bin`
- `/opt`
- `/usr/local`

The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>`
directory and, when extracted under `$HOME`, the resulting installation
path will be `$HOME/zephyr-sdk-<version>`.

If you install the Zephyr SDK outside any of these locations, you must
register the Zephyr SDK in the CMake package registry by running the setup
script, or set [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) to point to the Zephyr SDK
installation directory.

You can also use [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) for pointing to a
directory containing multiple Zephyr SDKs, allowing for automatic toolchain
selection. For example, `ZEPHYR_SDK_INSTALL_DIR=/company/tools`, where
the `company/tools` folder contains the following subfolders:

- `/company/tools/zephyr-sdk-0.13.2`
- `/company/tools/zephyr-sdk-a.b.c`
- `/company/tools/zephyr-sdk-x.y.z`

This allows the Zephyr build system to choose the correct version of the
SDK, while allowing multiple Zephyr SDKs to be grouped together at a
specific path.

## Building on Linux without the Zephyr SDK

The Zephyr SDK is provided for convenience and ease of use. It provides
toolchains for all Zephyr target architectures, and does not require any extra
flags when building applications or running tests. In addition to
cross-compilers, the Zephyr SDK also provides prebuilt host tools. It is,
however, possible to build without the SDK’s toolchain by using another
toolchain as described in the [Toolchains](../toolchains/index.md#toolchains) section.

As already noted above, the SDK also includes prebuilt host tools. To use the
SDK’s prebuilt host tools with a toolchain from another source, you must set the
[`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) environment variable to the Zephyr SDK
installation directory. To build without the Zephyr SDK’s prebuilt host tools,
the [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) environment variable must be unset.

To make sure this variable is unset, run:

```shell
unset ZEPHYR_SDK_INSTALL_DIR
```
