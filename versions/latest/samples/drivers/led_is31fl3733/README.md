---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/drivers/led_is31fl3733/README.html
original_path: samples/drivers/led_is31fl3733/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IS31FL3733 LED Matrix

## Overview

This sample controls a matrix of up to 192 LEDs. The sample performs the
following test steps in an infinite loop:

- Set all LEDs to full brightness with [`led_write_channels()`](../../../hardware/peripherals/led.md#c.led_write_channels "led_write_channels") API
- Disable upper quadrant of LED array with [`led_write_channels()`](../../../hardware/peripherals/led.md#c.led_write_channels "led_write_channels") API
- Dim each LED in sequence using [`led_set_brightness()`](../../../hardware/peripherals/led.md#c.led_set_brightness "led_set_brightness") API
- Toggle each LED in sequency using [`led_on()`](../../../hardware/peripherals/led.md#c.led_on "led_on") and `led_of()` APIs
- Toggle between low or high current limit using `is31fl3733_current_limit()`
  API, and repeat the above tests

### Sample Configuration

The number of LEDs can be limited using the following sample specific Kconfigs:

- `CONFIG_LED_ROW_COUNT`
- `CONFIG_LED_COLUMN_COUNT`

## Building and Running

This sample can be run on any board with an IS31FL3733 LED driver connected via
I2C, and a node with the issi,is31fl3733 compatible present in its devicetree.

This sample provides a DTS overlay for the [NXP FRDM-K22F](../../../boards/arm/frdm_k22f/doc/index.md#frdm-k22f) board
(`boards/frdm_k22f.overlay`). It assumes that the IS31FL3733 LED
controller is connected to I2C0, at address 0x50. The SDB GPIO should be
connected to PTC2 (A3 on the arduino header)
