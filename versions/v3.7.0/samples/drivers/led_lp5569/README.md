---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/led_lp5569/README.html
original_path: samples/drivers/led_lp5569/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# LP5569 9-channel LED controller

## Overview

This sample controls 9 LEDs connected to an LP5569 driver. The sample turns
all LEDs on and switches all LEDs off again within a one second interval.

## Building and Running

Build the application for the [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board, and connect
a LP5569 LED controller on the bus I2C0 at the address 0x32.

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/led_lp5569
```

For flashing the application, refer to the Flashing section of the
[nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board documentation.

```text
*** Booting Zephyr OS build zephyr-v3.3.0 ***
[00:00:00.361,694] <inf> app: Found LED device lp5569@32
[00:00:00.361,694] <inf> app: Testing 9 LEDs ..
```

## References

- LP5569 Datasheet: [https://www.ti.com/product/de-de/LP5569](https://www.ti.com/product/de-de/LP5569)
