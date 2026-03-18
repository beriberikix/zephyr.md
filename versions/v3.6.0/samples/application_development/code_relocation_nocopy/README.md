---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/application_development/code_relocation_nocopy/README.html
original_path: samples/application_development/code_relocation_nocopy/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Code relocation nocopy

## Overview

A simple example that demonstrates how relocation of code, data or bss sections
using a custom linker script.

Differently from the code relocation sample, this sample is relocating the
content of the ext\_code.c file to a different FLASH section and the code is XIP
directly from there without the need to copy / relocate the code.

## nRF5340 DK platform instructions

The nRF5340 DK has a 64 Mb external flash memory supporting Quad SPI. It is
possible to do XIP from the external flash memory.

The external flash memory is mapped to 0x10000000.

In this sample we relocate some of the code to the external flash memory with
the remaining Zephyr kernel in the internal flash.

To build and flash the application (including the external memory part):

```shell
west build -b nrf5340dk_nrf5340_cpuapp samples/application_development/code_relocation_nocopy
west flash
```

Execution output:

```shell
*** Booting Zephyr OS build v3.0.0-rc3-25-g0df32cec1ff2  ***
Address of main function 0x4f9
Address of function_in_ext_flash 0x10000001
Address of var_ext_sram_data 0x200000a0 (10)
Address of function_in_sram 0x20000001
Address of var_sram_data 0x200000a4 (10)
Hello World! nrf5340dk_nrf5340_cpuapp
```
