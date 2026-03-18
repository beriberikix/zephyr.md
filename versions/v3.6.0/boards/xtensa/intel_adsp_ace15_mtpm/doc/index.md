---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/xtensa/intel_adsp_ace15_mtpm/doc/index.html
original_path: boards/xtensa/intel_adsp_ace15_mtpm/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Intel ADSP ACE 1.5

## Overview

This board configuration is used to run Zephyr on the Intel ACE 1.5 Audio DSP.
This configuration is present, for example, on Intel Meteor Lake microprocessors.
Refer to [Intel ADSP cAVS and ACE](../../intel_adsp_cavs25/doc/intel_adsp_generic.md#intel-adsp-generic) for more details on Intel ADSP ACE and CAVS.

## System requirements

### Xtensa Toolchain

If you choose to build with the Xtensa toolchain instead of the Zephyr SDK, set
the following environment variables specific to the board in addition to the
Xtensa toolchain environment variables listed in [Intel ADSP cAVS and ACE](../../intel_adsp_cavs25/doc/intel_adsp_generic.md#intel-adsp-generic).

```shell
export ZEPHYR_TOOLCHAIN_VARIANT=xt-clang
export TOOLCHAIN_VER=RI-2021.7-linux
export XTENSA_CORE=ace10_LX7HiFi4
```

For older versions of the toolchain, set the toolchain variant to `xcc`.

## Programming and Debugging

Refer to [Intel ADSP cAVS and ACE](../../intel_adsp_cavs25/doc/intel_adsp_generic.md#intel-adsp-generic) for generic instructions on programming and
debugging applicable to all CAVS and ACE platforms.
