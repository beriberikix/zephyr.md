---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/lp50xx/README.html
original_path: samples/drivers/led/lp50xx/README.html
---

# LP50XX RGB LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/lp50xx/README.rst/..)

## Overview

This sample controls up to 12 LEDs connected to a LP50xx driver.

First, for each LED information is retrieved using the led\_get\_info syscall
and printed in the log messages. Next, from an infinite loop, a test pattern
(described below) is applied to all the LEDs simultaneously (using the
[`led_write_channels()`](../../../../doxygen/html/group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a) syscall) and then to each LED one by one (using the
[`led_set_brightness()`](../../../../doxygen/html/group__led__interface.md#gaca479fd77518331f4fc84f788e345882) and [`led_set_color()`](../../../../doxygen/html/group__led__interface.md#ga94dd46cc96f6ade5cebaa46a5f7ca5ea) syscalls).

### Test pattern

For all the LEDs first (using channel API) and then for each LED one by one:

For each color in red green blue white yellow purple cyan orange:

- set the color
- turn on
- turn off
- set the brightness gradually to the maximum level
- turn off

## Building and Running

This sample can be built and executed on boards with an I2C LP5009, LP5012,
LP5018, LP5024, LP5030 or LP5036 LED driver connected. A node matching the
the device type binding should be defined in the board DTS files.

As an example this sample provides a DTS overlay for the [LPCXpresso11U68](../../../../boards/nxp/lpcxpresso11u68/doc/index.md#lpcxpresso11u68)
board (`boards/lpcxpresso11u68.overlay`). It assumes that a I2C LP5030
LED driver (with 10 LEDs wired) is connected to the I2C0 bus at address 0x30.

## References

- LP5009/LP5012: [https://www.ti.com/lit/ds/symlink/lp5012.pdf](https://www.ti.com/lit/ds/symlink/lp5012.pdf)
- LP5018/LP5024: [https://www.ti.com/lit/ds/symlink/lp5024.pdf](https://www.ti.com/lit/ds/symlink/lp5024.pdf)
- LP5030/LP5036: [https://www.ti.com/lit/ds/symlink/lp5036.pdf](https://www.ti.com/lit/ds/symlink/lp5036.pdf)

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
