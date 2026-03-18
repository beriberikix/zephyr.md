---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/toolchains/zephyr_sdk.html
original_path: develop/toolchains/zephyr_sdk.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Zephyr SDK

The Zephyr Software Development Kit (SDK) contains toolchains for each of
Zephyr’s supported architectures. It also includes additional host tools, such
as custom QEMU and OpenOCD.

Use of the Zephyr SDK is highly recommended and may even be required under
certain conditions (for example, running tests in QEMU for some architectures).

## Supported architectures

The Zephyr SDK supports the following target architectures:

- ARC (32-bit and 64-bit; ARCv1, ARCv2, ARCv3)
- ARM (32-bit and 64-bit; ARMv6, ARMv7, ARMv8; A/R/M Profiles)
- MIPS (32-bit and 64-bit)
- Nios II
- RISC-V (32-bit and 64-bit; RV32I, RV32E, RV64I)
- x86 (32-bit and 64-bit)
- Xtensa

## Installation bundle and variables

The Zephyr SDK bundle supports all major operating systems (Linux, macOS and
Windows) and is delivered as a compressed file.
The installation consists of extracting the file and running the included setup
script. Additional OS-specific instructions are described in the sections below.

If no toolchain is selected, the build system looks for Zephyr SDK and uses the toolchain
from there. You can enforce this by setting the environment variable
[`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `zephyr`.

If you install the Zephyr SDK outside any of the default locations (listed in
the operating system specific instructions below) and you want automatic discovery
of the Zephyr SDK, then you must register the Zephyr SDK in the CMake package registry
by running the setup script. If you decide not to register the Zephyr SDK in the CMake registry,
then the [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) can be used to point to the Zephyr SDK installation
directory.

You can also set [`ZEPHYR_SDK_INSTALL_DIR`](../env_vars.md#envvar-ZEPHYR_SDK_INSTALL_DIR) to point to a directory
containing multiple Zephyr SDKs, allowing for automatic toolchain selection. For
example, you can set `ZEPHYR_SDK_INSTALL_DIR` to `/company/tools`, where the
`company/tools` folder contains the following subfolders:

- `/company/tools/zephyr-sdk-0.13.2`
- `/company/tools/zephyr-sdk-a.b.c`
- `/company/tools/zephyr-sdk-x.y.z`

This allows the Zephyr build system to choose the correct version of the SDK,
while allowing multiple Zephyr SDKs to be grouped together at a specific path.

## Zephyr SDK version compatibility

In general, the Zephyr SDK version referenced in this page should be considered
the recommended version for the corresponding Zephyr version.

For the full list of compatible Zephyr and Zephyr SDK versions, refer to the
[Zephyr SDK Version Compatibility Matrix](https://github.com/zephyrproject-rtos/sdk-ng/wiki/Zephyr-SDK-Version-Compatibility-Matrix).

## Zephyr SDK installation

Note

You can change `0.16.5` to another version in the instructions below
if needed; the [Zephyr SDK Releases](https://github.com/zephyrproject-rtos/sdk-ng/tags) page contains all available
SDK releases.

Note

If you want to uninstall the SDK, you may simply remove the directory
where you installed it.

UbuntumacOSWindows

1. Download and verify the [Zephyr SDK bundle](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.5):

   ```
   cd ~
   wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/zephyr-sdk-0.16.5_linux-x86_64.tar.xz
   wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/sha256.sum | shasum --check --ignore-missing
   ```

   If your host architecture is 64-bit ARM (for example, Raspberry Pi), replace `x86_64`
   with `aarch64` in order to download the 64-bit ARM Linux SDK.
2. Extract the Zephyr SDK bundle archive:

   ```
   tar xvf zephyr-sdk-0.16.5_linux-x86_64.tar.xz
   ```

   Note

   It is recommended to extract the Zephyr SDK bundle at one of the following locations:

   - `$HOME`
   - `$HOME/.local`
   - `$HOME/.local/opt`
   - `$HOME/bin`
   - `/opt`
   - `/usr/local`

   The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>`
   directory and, when extracted under `$HOME`, the resulting
   installation path will be `$HOME/zephyr-sdk-<version>`.
3. Run the Zephyr SDK bundle setup script:

   ```
   cd zephyr-sdk-0.16.5
   ./setup.sh
   ```

   Note

   You only need to run the setup script once after extracting the Zephyr SDK bundle.

   You must rerun the setup script if you relocate the Zephyr SDK bundle directory after
   the initial setup.
4. Install [udev](https://en.wikipedia.org/wiki/Udev) rules, which
   allow you to flash most Zephyr boards as a regular user:

   ```
   sudo cp ~/zephyr-sdk-0.16.5/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
   sudo udevadm control --reload
   ```

1. Download and verify the [Zephyr SDK bundle](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.5):

   ```
   cd ~
   curl -L -O https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/zephyr-sdk-0.16.5_macos-x86_64.tar.xz
   curl -L https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/sha256.sum | shasum --check --ignore-missing
   ```

   If your host architecture is 64-bit ARM (Apple Silicon, also known as M1), replace
   `x86_64` with `aarch64` in order to download the 64-bit ARM macOS SDK.
2. Extract the Zephyr SDK bundle archive:

   ```
   tar xvf zephyr-sdk-0.16.5_macos-x86_64.tar.xz
   ```

   Note

   It is recommended to extract the Zephyr SDK bundle at one of the following locations:

   - `$HOME`
   - `$HOME/.local`
   - `$HOME/.local/opt`
   - `$HOME/bin`
   - `/opt`
   - `/usr/local`

   The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>`
   directory and, when extracted under `$HOME`, the resulting
   installation path will be `$HOME/zephyr-sdk-<version>`.
3. Run the Zephyr SDK bundle setup script:

   ```
   cd zephyr-sdk-0.16.5
   ./setup.sh
   ```

   Note

   You only need to run the setup script once after extracting the Zephyr SDK bundle.

   You must rerun the setup script if you relocate the Zephyr SDK bundle directory after
   the initial setup.

1. Open a `cmd.exe` terminal window **as a regular user**
2. Download the [Zephyr SDK bundle](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.5):

   ```
   cd %HOMEPATH%
   wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.5/zephyr-sdk-0.16.5_windows-x86_64.7z
   ```
3. Extract the Zephyr SDK bundle archive:

   ```
   7z x zephyr-sdk-0.16.5_windows-x86_64.7z
   ```

   Note

   It is recommended to extract the Zephyr SDK bundle at one of the following locations:

   - `%HOMEPATH%`
   - `%PROGRAMFILES%`

   The Zephyr SDK bundle archive contains the `zephyr-sdk-<version>`
   directory and, when extracted under `%HOMEPATH%`, the resulting
   installation path will be `%HOMEPATH%\zephyr-sdk-<version>`.
4. Run the Zephyr SDK bundle setup script:

   ```
   cd zephyr-sdk-0.16.5
   setup.cmd
   ```

   Note

   You only need to run the setup script once after extracting the Zephyr SDK bundle.

   You must rerun the setup script if you relocate the Zephyr SDK bundle directory after
   the initial setup.
