---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/toolchains/arm_compiler.html
original_path: develop/toolchains/arm_compiler.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Arm Compiler 6

1. Download and install a development suite containing the [Arm Compiler 6](https://developer.arm.com/tools-and-software/embedded/arm-compiler/downloads/version-6)
   for your operating system.
2. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `armclang`.
   - Set `ARMCLANG_TOOLCHAIN_PATH` to the toolchain installation
     directory.
3. The Arm Compiler 6 needs the `ARMLMD_LICENSE_FILE` environment
   variable to point to your license file or server.

For example:

> ```shell
> # Linux, macOS, license file:
> export ARMLMD_LICENSE_FILE=/<path>/license_armds.dat
> # Linux, macOS, license server:
> export ARMLMD_LICENSE_FILE=8224@myserver
> ```
>
> ```batch
> # Windows, license file:
> set ARMLMD_LICENSE_FILE=c:\<path>\license_armds.dat
> # Windows, license server:
> set ARMLMD_LICENSE_FILE=8224@myserver
> ```

1. If the Arm Compiler 6 was installed as part of an Arm Development Studio, then
   you must set the `ARM_PRODUCT_DEF` to point to the product definition file:
   See also: [Product and toolkit configuration](https://developer.arm.com/tools-and-software/software-development-tools/license-management/resources/product-and-toolkit-configuration).
   For example if the Arm Development Studio is installed in:
   `/opt/armds-2020-1` with a Gold license, then set `ARM_PRODUCT_DEF`
   to point to `/opt/armds-2020-1/gold.elmap`.

   Note

   The Arm Compiler 6 uses `armlink` for linking. This is incompatible
   with Zephyr’s linker script template, which works with GNU ld. Zephyr’s
   Arm Compiler 6 support Zephyr’s CMake linker script generator, which
   supports generating scatter files. Basic scatter file support is in
   place, but there are still areas covered in ld templates which are not
   fully supported by the CMake linker script generator.

   Some Zephyr subsystems or modules may also contain C or assembly code
   that relies on GNU intrinsics and have not yet been updated to work fully
   with `armclang`.
