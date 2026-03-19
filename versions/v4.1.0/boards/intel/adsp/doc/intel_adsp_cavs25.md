---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/intel/adsp/doc/intel_adsp_cavs25.html
original_path: boards/intel/adsp/doc/intel_adsp_cavs25.html
---

# Intel ADSP CAVS 2.5

## Overview

This board configuration is used to run Zephyr on the Intel CAVS 2.5 Audio DSP.
This configuration is present, for example, on Intel [Tiger Lake](https://www.intel.com/content/www/us/en/products/platforms/details/tiger-lake-h.html) microprocessors.
Refer to [Intel ADSP cAVS and ACE](intel_adsp_generic.md#intel-adsp-generic) for more details on Intel ADSP ACE and CAVS.

## System requirements

### Xtensa Toolchain

If you choose to build with the Xtensa toolchain instead of the Zephyr SDK, set
the following environment variables specific to the board in addition to the
Xtensa toolchain environment variables listed in [Intel ADSP cAVS and ACE](intel_adsp_generic.md#intel-adsp-generic).

```shell
export TOOLCHAIN_VER=RG-2017.8-linux
export XTENSA_CORE=cavs2x_LX6HiFi3_2017_8
```

## Programming and Debugging

Refer to [Intel ADSP cAVS and ACE](intel_adsp_generic.md#intel-adsp-generic) for generic instructions on programming and
debugging applicable to all CAVS and ACE platforms.
