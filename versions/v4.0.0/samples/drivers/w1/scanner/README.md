---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/w1/scanner/README.html
original_path: samples/drivers/w1/scanner/README.html
---

# 1-Wire scanner

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/w1/scanner/README.rst/..)

## Overview

This sample demonstrates how to scan for 1-Wire devices. It runs the 1-Wire
scan routine once and prints the family id as well as serial number of the
devices found.

## Building and Running

Set DTC\_OVERLAY\_FILE to “ds2484.overlay” or “w1\_serial.overlay” in order to
enable and configure the drivers.

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/w1/scanner -- -DDTC_OVERLAY_FILE=w1_serial.overlay
west flash
```

### Sample Output

```shell
[00:00:00.392,272] <inf> main: Device found; family: 0x3a, serial: 0x3af9985800000036
[00:00:00.524,169] <inf> main: Device found; family: 0x3a, serial: 0x3a6ea2580000003b
[00:00:00.656,097] <inf> main: Device found; family: 0x28, serial: 0x2856fb470d000022
[00:00:00.656,097] <inf> main: Number of devices found on bus: 3
```

## See also

[1-Wire Interface](../../../../doxygen/html/group__w1__interface.md)
