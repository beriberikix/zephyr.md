---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/boards/esp32/spiram_test/README.html
original_path: samples/boards/esp32/spiram_test/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Espressif ESP32 SPIRAM test

## Overview

This sample allocates memory from internal DRAM and SPIRAM by calling
[`k_malloc()`](../../../../kernel/memory_management/heap.md#c.k_malloc "k_malloc"), frees allocated memory by calling [`k_free()`](../../../../kernel/memory_management/heap.md#c.k_free "k_free") and
checks if memory can be allocated again. Capability of allocated memory is
decided by ESP\_HEAP\_MIN\_EXTRAM\_THRESHOLD. If size is less than
ESP\_HEAP\_MIN\_EXTRAM\_THRESHOLD, memory is allocated from internal DRAM. If
size is greater than ESP\_HEAP\_MIN\_EXTRAM\_THRESHOLD, memory is allocated from
SPIRAM.

## Supported SoCs

The following SoCs are supported by this sample code so far:

- ESP32
- ESP32-S2

## Building and Running

Make sure you have your board connected over USB port.

```shell
west build -b esp32_devkitc_wrover samples/boards/esp32/spiram_test
west flash
```

If using another supported Espressif board, replace the argument in the above
command with a proper board name (e.g., esp32s2\_saola).

### Sample Output

To check output of this sample, run `west espressif monitor` or any other serial
console program (e.g., minicom, putty, screen, etc).
This example uses `west espressif monitor`, which automatically detects the serial
port at `/dev/ttyUSB0`:

```shell
$ west espressif monitor
```

```shell
mem test ok! 209
SPIRAM mem test pass
mem test ok! 194
Internal mem test pass
```
