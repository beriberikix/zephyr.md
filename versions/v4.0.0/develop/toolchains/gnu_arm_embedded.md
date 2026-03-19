---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/develop/toolchains/gnu_arm_embedded.html
original_path: develop/toolchains/gnu_arm_embedded.html
---

# GNU Arm Embedded

1. Download and install a [GNU Arm Embedded](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm) build for your operating system
   and extract it on your file system.

   Note

   On Windows, we’ll assume for this guide that you install into the directory
   `C:\gnu_arm_embedded`. You can also choose the default installation
   path used by the ARM GCC installer, in which case you will need to adjust the path
   accordingly in the guide below.

   Warning

   On macOS Catalina or later you might need to [change a security
   policy](../getting_started/installation_mac.md#mac-gatekeeper) for the toolchain to be able to run from the
   terminal.
2. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `gnuarmemb`.
   - Set `GNUARMEMB_TOOLCHAIN_PATH` to the toolchain installation
     directory.
3. To check that you have set these variables correctly in your current
   environment, follow these example shell sessions (the
   `GNUARMEMB_TOOLCHAIN_PATH` values may be different on your system):

   ```shell
   # Linux, macOS:
   $ echo $ZEPHYR_TOOLCHAIN_VARIANT
   gnuarmemb
   $ echo $GNUARMEMB_TOOLCHAIN_PATH
   /home/you/Downloads/gnu_arm_embedded

   # Windows:
   > echo %ZEPHYR_TOOLCHAIN_VARIANT%
   gnuarmemb
   > echo %GNUARMEMB_TOOLCHAIN_PATH%
   C:\gnu_arm_embedded
   ```

   Warning

   On macOS, if you are having trouble with the suggested procedure, there is an unofficial package on brew that might help you.
   Run `brew install gcc-arm-embedded` and configure the variables

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `gnuarmemb`.
   - Set `GNUARMEMB_TOOLCHAIN_PATH` to the brew installation directory (something like `/usr/local`)
