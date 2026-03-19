---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/modules/compression/lz4/README.html
original_path: samples/modules/compression/lz4/README.html
---

# LZ4

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/modules/compression/lz4/README.rst/..)

## Overview

A simple sample that can be used with any [supported board](../../../../boards/index.md#boards) and
compress & decompress the user data to the console.

## Building and Running

Add the lz4 module to your West manifest and pull it:

```shell
west config manifest.project-filter -- +lz4
west update
```

The sample can be built and executed on nrf52840dk/nrf52840 as follows:

```shell
west build -b nrf52840dk/nrf52840 samples/modules/compression/lz4
west flash
```

To build for another board, change “nrf52840dk/nrf52840” above to that board’s name.
