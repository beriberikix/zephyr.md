---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/toolchains/crosstool_ng.html
original_path: develop/toolchains/crosstool_ng.html
---

# Crosstool-NG (Deprecated)

Warning

`xtools` toolchain variant is deprecated. The
[cross-compile toolchain variant](other_x_compilers.md#other-x-compilers) should be used
when using a custom toolchain built with Crosstool-NG.

You can build toolchains from source code using crosstool-NG.

1. Follow the steps on the crosstool-NG website to [prepare your host](http://crosstool-ng.github.io/docs/os-setup/).
2. Follow the [Zephyr SDK with Crosstool NG instructions](https://github.com/zephyrproject-rtos/sdk-ng/blob/master/README.md) to
   build your toolchain. Repeat as necessary to build toolchains for multiple
   target architectures.

   You will need to clone the `sdk-ng` repo and run the following command:

   ```shell
   ./go.sh <arch>
   ```

   Note

   Currently, only i586 and Arm toolchain builds are verified.
3. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `xtools`.
   - Set `XTOOLS_TOOLCHAIN_PATH` to the toolchain build directory.
4. To check that you have set these variables correctly in your current
   environment, follow these example shell sessions (the
   `XTOOLS_TOOLCHAIN_PATH` values may be different on your system):

   ```shell
   # Linux, macOS:
   $ echo $ZEPHYR_TOOLCHAIN_VARIANT
   xtools
   $ echo $XTOOLS_TOOLCHAIN_PATH
   /Volumes/CrossToolNGNew/build/output/
   ```
