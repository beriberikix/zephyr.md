---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/develop/toolchains/cadence_xcc.html
original_path: develop/toolchains/cadence_xcc.html
---

# Cadence Tensilica Xtensa C/C++ Compiler (XCC)

1. Obtain Tensilica Software Development Toolkit targeting the specific SoC
   on hand. This usually contains two parts:

   - The Xtensa Xplorer which contains the necessary executables and
     libraries.
   - A SoC-specific add-on to be installed on top of Xtensa Xplorer.

     - This add-on allows the compiler to generate code for the SoC on hand.
2. Install Xtensa Xplorer and then the SoC add-on.

   - Follow the instruction from Cadence on how to install the SDK.
   - Depending on the SDK, there are two set of compilers:

     - GCC-based compiler: `xt-xcc` and its friends.
     - Clang-based compiler: `xt-clang` and its friends.
3. Make sure you have obtained a license to use the SDK, or has access to
   a remote licensing server.
4. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `xcc` or `xt-clang`.
   - Set `XTENSA_TOOLCHAIN_PATH` to the toolchain installation
     directory.
   - There are two ways to specify the SoC ID and the SDK version to use.
     They are mutually exclusive, and cannot be used together.

     1. When building for a single SoC:

        - Set `XTENSA_CORE` to the SoC ID where application is being
          targeted.
        - Set `TOOLCHAIN_VER` to the Xtensa SDK version.
     2. When building for multiple SoCs, for each SoC and board combination:

        - Set `XTENSA_CORE_{normalized_board_target}`
          to the SoC ID where application is being targeted.
        - Set `TOOLCHAIN_VAR_{normalized_board_target}`
          to the Xtensa SDK version.
5. For example, assuming the SDK is installed in `/opt/xtensa`, and
   using the SDK for application development on `intel_adsp/ace15_mtpm`,
   setup the environment using the two above mentioned ways:

   1. Single SoC:

      ```shell
      # Linux
      export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
      export XTENSA_TOOLCHAIN_PATH=/opt/xtensa/XtDevTools/install/tools/
      export XTENSA_CORE=ace10_LX7HiFi4_2022_10
      export TOOLCHAIN_VER=RI-2022.10-linux
      ```
   2. Multiple SoCs:

      ```shell
      # Linux
      export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
      export XTENSA_TOOLCHAIN_PATH=/opt/xtensa/XtDevTools/install/tools/
      export TOOLCHAIN_VER_intel_adsp_ace15_mtpm=RI-2022.10-linux
      export XTENSA_CORE_intel_adsp_ace15_mtpm=ace10_LX7HiFi4_2022_10
      ```
6. To use Clang-based compiler:

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `xt-clang`.
   - Note that the Clang-based compiler may contain an old LLVM bug which
     results in the following error:

     ```shell
     /tmp/file.s: Assembler messages:
     /tmp/file.s:20: Error: file number 1 already allocated
     clang-3.9: error: Xtensa-as command failed with exit code 1
     ```

     If this happens, set `XCC_NO_G_FLAG` to `1`.

     - For example:

       ```shell
       # Linux
       export XCC_NO_G_FLAG=1
       ```
