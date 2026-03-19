---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/application_development/code_relocation_nocopy/README.html
original_path: samples/application_development/code_relocation_nocopy/README.html
---

# Code relocation nocopy

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/application_development/code_relocation_nocopy/README.rst/..)

## Overview

A simple example that demonstrates how relocation of code, data or bss sections
using a custom linker script.

Differently from the code relocation sample, this sample is relocating the
content of the ext\_code.c file to a different FLASH section and the code is XIP
directly from there without the need to copy / relocate the code. All other code
(e.g. main(), Zephyr kernel) stays in the internal flash.

## nRF5340 DK platform instructions

The nRF5340 DK has a 64 Mb external flash memory supporting Quad SPI. It is
mapped to 0x10000000.

To build and flash the application (including the external memory part):

```shell
west build -b nrf5340dk/nrf5340/cpuapp samples/application_development/code_relocation_nocopy
west flash
```

## STM32F769I-Discovery platform instructions

The stm32f769i\_disco has 64MB of external flash attached via QSPI. It is mapped
to 0x90000000.

```shell
west build -b stm32f769i_disco samples/application_development/code_relocation_nocopy
west flash
```

## STM32 b\_u585i\_iot02a Discovery kit instructions

The b\_u585i\_iot02a has 64MB of external flash attached via OSPI. It is mapped
to 0x70000000.

```shell
west build -b b_u585i_iot02a samples/application_development/code_relocation_nocopy
west flash
```

## Execution output

```shell
*** Booting Zephyr OS build v3.0.0-rc3-25-g0df32cec1ff2  ***
Address of main function 0x4f9
Address of function_in_ext_flash 0x10000001
Address of var_ext_sram_data 0x200000a0 (10)
Address of function_in_sram 0x20000001
Address of var_sram_data 0x200000a4 (10)
Hello World! nrf5340dk/nrf5340/cpuapp
```
