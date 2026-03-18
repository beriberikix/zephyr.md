---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/compression/lz4/README.html
original_path: samples/compression/lz4/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# LZ4

## Overview

A simple sample that can be used with any [supported board](../../../boards/index.md#boards) and
compress & decompress the user data to the console.

## Building and Running

The sample can be built and executed on nrf52840dk\_nrf52840 as follows:

```shell
west build -b nrf52840dk_nrf52840 samples/compression/lz4
west flash
```

To build for another board, change “nrf52840dk\_nrf52840” above to that board’s name.
