---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/led/lp5562/README.html
original_path: samples/drivers/led/lp5562/README.html
---

# LP5562 RGB LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/lp5562/README.rst/..)

## Overview

This sample controls 4 LEDs connected to a TI LP5562 driver, using the
following pattern:

> 1. turn on LEDs to be red
> 2. turn on LEDs to be green
> 3. turn on LEDs to be blue
> 4. turn on LEDs to be white
> 5. turn on LEDs to be yellow
> 6. turn on LEDs to be purple
> 7. turn on LEDs to be cyan
> 8. turn on LEDs to be orange
> 9. turn off LEDs
> 10. blink the LEDs in white
> 11. turn off LEDs
> 12. blink the LEDs in purple
> 13. turn off LEDs

Refer to the [LP5562 Manual](http://www.ti.com/lit/ds/symlink/lp5562.pdf) for the RGB LED connections and color channel
mappings used by this sample.

## Building and Running

Build the application for the [nRF52840 DK](../../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board, and connect
a LP5562 LED driver on the bus I2C0 at the address 0x30.

```shell
west build -b nrf52840dk/nrf52840 samples/drivers/led/lp5562
```

For flashing the application, refer to the Flashing section of the
[nRF52840 DK](../../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840) board documentation.

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
