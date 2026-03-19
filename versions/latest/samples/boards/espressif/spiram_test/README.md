---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/espressif/spiram_test/README.html
original_path: samples/boards/espressif/spiram_test/README.html
---

# SPIRAM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/spiram_test/README.rst/..)

## Overview

This sample shows how to allocate memory from SPIRAM by using
[`shared_multi_heap_aligned_alloc()`](../../../../doxygen/html/group__shared__multi__heap.md#ga328b199253da06ed724e9b0157167ede) with `SMH_REG_ATTR_EXTERNAL` attribute. Checks if the
memory was correctly allocated then frees it by calling [`shared_multi_heap_free()`](../../../../doxygen/html/group__shared__multi__heap.md#gab968bf26483d22939aaa7c2b1b6743ad).
It also allocates memory from internal memory and checks if the address range is correct.

## Supported SoCs

The following SoCs are supported by this sample code so far:

- ESP32
- ESP32-S2
- ESP32-S3

## Building and Running

Make sure you have your board connected over USB port.

```shell
west build -b esp32s3_devkitm/esp32s3/procpu samples/boards/espressif/spiram_test
west flash
```

If using another supported Espressif board, replace the argument in the above
command with a proper board name (e.g., `esp32s2_saola`).

### Sample Output

To check output of this sample, run `west espressif monitor` or any other serial
console program (e.g., minicom, putty, screen, etc).
This example uses `west espressif monitor`, which automatically detects the serial
port at `/dev/ttyUSB0`:

```shell
$ west espressif monitor
```

```shell
*** Booting Zephyr OS build v3.7.0-446-g93c9da66944c ***
SPIRAM mem test pass
Internal mem test pass
```
