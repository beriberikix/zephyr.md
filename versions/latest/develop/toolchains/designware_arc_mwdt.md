---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/develop/toolchains/designware_arc_mwdt.html
original_path: develop/toolchains/designware_arc_mwdt.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DesignWare ARC MetaWare Development Toolkit (MWDT)

1. You need to have [ARC MWDT](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware) installed on
   your host.
2. You need to have [Zephyr SDK](zephyr_sdk.md#toolchain-zephyr-sdk) installed on your host.

   Note

   A Zephyr SDK is used as a source of tools like device tree compiler (DTC), QEMU, etc…
   Even though ARC MWDT toolchain is used for Zephyr RTOS build, still the GNU preprocessor & GNU
   objcopy might be used for some steps like device tree preprocessing and `.bin` file
   generation. We used Zephyr SDK as a source of these ARC GNU tools as well.
3. [Set these environment variables](../env_vars.md#env-vars):

   - Set [`ZEPHYR_TOOLCHAIN_VARIANT`](../env_vars.md#envvar-ZEPHYR_TOOLCHAIN_VARIANT) to `arcmwdt`.
   - Set `ARCMWDT_TOOLCHAIN_PATH` to the toolchain installation directory. MWDT installation
     provides `METAWARE_ROOT` so simply set `ARCMWDT_TOOLCHAIN_PATH` to
     `$METAWARE_ROOT/../` (Linux) or `%METAWARE_ROOT%\..\` (Windows).

   Tip

   If you have only one ARC MWDT toolchain version installed on your machine you may skip setting
   `ARCMWDT_TOOLCHAIN_PATH` - it would be detected automatically.
4. To check that you have set these variables correctly in your current
   environment, follow these example shell sessions (the
   `ARCMWDT_TOOLCHAIN_PATH` values may be different on your system):

   ```shell
   # Linux:
   $ echo $ZEPHYR_TOOLCHAIN_VARIANT
   arcmwdt
   $ echo $ARCMWDT_TOOLCHAIN_PATH
   /home/you/ARC/MWDT_2023.03/

   # Windows:
   > echo %ZEPHYR_TOOLCHAIN_VARIANT%
   arcmwdt
   > echo %ARCMWDT_TOOLCHAIN_PATH%
   C:\ARC\MWDT_2023.03\
   ```
