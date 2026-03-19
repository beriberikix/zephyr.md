---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/ht16k33/README.html
original_path: samples/drivers/ht16k33/README.html
---

# HT16K33 LED driver with keyscan

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/ht16k33/README.rst/..)

## Overview

This sample controls the LEDs connected to a [Holtek HT16K33](https://www.holtek.com/page/vg/HT16K33A) [[1]](#id1)
driver. The sample supports up to 128 LEDs connected to the
rows/columns of the HT16K33.

The LEDs are controlled using the following pattern:

> 1. turn on all connected (up to 128) LEDs one-by-one
> 2. blink the LEDs at 2 Hz, 1 Hz, and 0.5 Hz
> 3. reduce the brightness gradually from 100% to 0%
> 4. turn off all LEDs, restore 100% brightness, and start over

The sample logs keyscan events on the console.

## Building and Running

Build the application for the [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board, and
connect an HT16K33 LED driver at address 0x70 on the I2C-0 bus.

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/ht16k33
```

For flashing the application, refer to the Flashing section of the
[nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board documentation.

## References

[[1](#id2)]

[https://www.holtek.com/page/vg/HT16K33A](https://www.holtek.com/page/vg/HT16K33A)

## See also

[LED Interface](../../../doxygen/html/group__led__interface.md)

[Keyboard Scan Driver APIs](../../../doxygen/html/group__kscan__interface.md)
