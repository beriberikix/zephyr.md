---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/develop/toolchains/arm_toolchain_for_embedded.html
original_path: develop/toolchains/arm_toolchain_for_embedded.html
---

# Arm Toolchain for Embedded (ATfE)

Arm Toolchain for Embedded (ATfE) is a C and C++ toolchain from Arm based
:   on the free and open-source LLVM Compiler Infrastructure and the Picolib C
    library for baremetal targets.

ATfE is fined-tuned with a particular focus on performance for newer
:   ARM products (post 2024) like 64-bit Arm Architectures (AArch64),
    or the M-Profile Vector Extension (MVE, a 32-bit Armv8.1-M extension).

## Installation

1. Download and install a [Arm toolchain for embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded) build for your operating system
   and extract it on your file system.
2. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `llvm`.
   - Set `LLVM_TOOLCHAIN_PATH` to the toolchain installation directory.
3. To check that you have set these variables correctly in your current
   environment, follow these example shell sessions (the
   `LLVM_TOOLCHAIN_PATH` values may be different on your system):

   UbuntumacOSWindows

   ```shell
   echo $ZEPHYR_TOOLCHAIN_VARIANT
   llvm
   echo $LLVM_TOOLCHAIN_PATH
   /home/you/Downloads/ATfE
   ```

   ```shell
   echo $ZEPHYR_TOOLCHAIN_VARIANT
   llvm
   echo $LLVM_TOOLCHAIN_PATH
   /home/you/Downloads/ATfE
   ```

   ```powershell
   > echo %ZEPHYR_TOOLCHAIN_VARIANT%
   llvm
   > echo %LLVM_TOOLCHAIN_PATH%
   C:\ATfE
   ```
4. You can also set `ZEPHYR_TOOLCHAIN_VARIANT` and `LLVM_TOOLCHAIN_PATH` as CMake
   variables when generating a build system for a Zephyr application, like so:

   > ```shell
   >
   > ```
   >
   > west build … – -DZEPHYR\_TOOLCHAIN\_VARIANT=llvm -DLLVM\_TOOLCHAIN\_PATH=…

## Toolchain settings

Because LLVM is widely compatible with GNU tools, When builiding with any
:   LLVM toolchain, you have to specify some settings to let the compiler
    know what tools to use:

Linker:
:   Set `CONFIG_LLVM_USE_LLD=y` to use LLVM linker.
    set `CONFIG_LLVM_USE_LD=y` to use the GNU LD linker.

Runtime library:
:   Set `CONFIG_COMPILER_RT_RTLIB=y` to use LLVM runtime library.
    Set `CONFIG_LIBGCC_RTLIB=y` to use LibGCC runtime library.

```shell
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=llvm -DLLVM_TOOLCHAIN_PATH=... -DCONFIG_LLVM_USE_LLD=y -DCONFIG_COMPILER_RT_RTLIB=y
```
