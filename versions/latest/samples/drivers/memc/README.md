---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/memc/README.html
original_path: samples/drivers/memc/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Memory controller (MEMC) driver

## Overview

This sample can be used with any memory controller driver that
memory maps external RAM. It is intended to demonstrate
the ability to read and write from the memory mapped region.

Note that the chosen region (set by `sram-ext` dt alias node) should not
overlap with memory used for XIP or SRAM by the application, as the sample
would overwrite this data

## Building and Running

This application can be built and executed on an RT595 EVK as follows:

```shell
west build -b mimxrt595_evk_cm33 samples/drivers/memc
west build -t run
```

To build for another board, change “mimxrt595\_evk\_cm33” above to that
board’s name.

### Sample Output

```shell

```

**\* Booting Zephyr OS build zephyr-v3.2.0-2686-gd52d828c2bdc \***
Writing to memory region with base 0x38000000, size 0x800000

First 1KB of Data in memory:
============================
00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f
10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f
20 21 22 23 24 25 26 27 28 29 2a 2b 2c 2d 2e 2f
….

Read data matches written data
