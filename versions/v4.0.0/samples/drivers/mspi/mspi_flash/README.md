---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/mspi/mspi_flash/README.html
original_path: samples/drivers/mspi/mspi_flash/README.html
---

# JEDEC MSPI-NOR flash

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/mspi/mspi_flash/README.rst/..)

## Overview

This sample demonstrates using the [flash API](../../../../hardware/peripherals/flash.md#flash-api) on a MSPI NOR serial flash
memory device. While trivial it is an example of direct access and
allows confirmation that the flash is working and that automatic power
savings is correctly implemented.

## Building and Running

The application will build only for a target that has a [devicetree](../../../../build/dts/index.md#dt-guide)
`flash0` alias that refers to an entry with the following bindings as a compatible:

- [`ambiq,mspi-device`](../../../../build/dts/api/bindings/mspi/ambiq%2Cmspi-device.md#std-dtcompatible-ambiq-mspi-device), [`mspi-atxp032`](../../../../build/dts/api/bindings/mtd/mspi-atxp032.md#std-dtcompatible-mspi-atxp032)

```shell
west build -b apollo3p_evb samples/drivers/mspi/mspi_flash
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v2.3.0-2142-gca01d2e1d748  ***

JEDEC MSPI-NOR flash testing
==========================

Test 1: Flash erase
Flash erase succeeded!

Test 2: Flash write
Attempting to write 4 bytes
Data read matches data written. Good!
```

## See also

[FLASH Interface](../../../../doxygen/html/group__flash__interface.md)
