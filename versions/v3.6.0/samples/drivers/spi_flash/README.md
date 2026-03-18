---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/spi_flash/README.html
original_path: samples/drivers/spi_flash/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# JEDEC SPI-NOR flash

## Overview

This sample demonstrates using the [flash API](../../../hardware/peripherals/flash.md#flash-api) on a SPI NOR serial flash
memory device. While trivial it is an example of direct access and
allows confirmation that the flash is working and that automatic power
savings is correctly implemented.

## Building and Running

The application will build only for a target that has a [devicetree](../../../build/dts/index.md#dt-guide)
`spi-flash0` alias that refers to an entry with one of the following bindings as a compatible:

- [`jedec,spi-nor`](../../../build/dts/api/bindings/mtd/jedec%2Cspi-nor.md#std-dtcompatible-jedec-spi-nor),
- [`st,stm32-qspi-nor`](../../../build/dts/api/bindings/flash_controller/st%2Cstm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor),
- [`st,stm32-ospi-nor`](../../../build/dts/api/bindings/flash_controller/st%2Cstm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor),
- [`nordic,qspi-nor`](../../../build/dts/api/bindings/mtd/nordic%2Cqspi-nor.md#std-dtcompatible-nordic-qspi-nor).

```shell
west build -b nrf52840dk_nrf52840 samples/drivers/spi_flash
west flash
```

### Sample Output

```shell
*** Booting Zephyr OS build zephyr-v2.3.0-2142-gca01d2e1d748  ***

JEDEC QSPI-NOR SPI flash testing
==========================

Test 1: Flash erase
Flash erase succeeded!

Test 2: Flash write
Attempting to write 4 bytes
Data read matches data written. Good!
```
