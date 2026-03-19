---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/is31fl3733/README.html
original_path: samples/drivers/led/is31fl3733/README.html
---

# IS31FL3733 LED Matrix

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/is31fl3733/README.rst/..)

## Overview

This sample controls a matrix of up to 192 LEDs. The sample performs the
following test steps in an infinite loop:

- Set all LEDs to full brightness with [`led_write_channels()`](../../../../doxygen/html/group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a) API
- Disable upper quadrant of LED array with [`led_write_channels()`](../../../../doxygen/html/group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a) API
- Dim each LED in sequence using [`led_set_brightness()`](../../../../doxygen/html/group__led__interface.md#gaca479fd77518331f4fc84f788e345882) API
- Toggle each LED in sequency using [`led_on()`](../../../../doxygen/html/group__led__interface.md#gad4daafd7fcab22d1d68745b7264d0f73) and `led_of()` APIs
- Toggle between low or high current limit using [`is31fl3733_current_limit()`](../../../../doxygen/html/is31fl3733_8h.md#ad3de611ed4641cccaaa0920cee160eed)
  API, and repeat the above tests

### Sample Configuration

The number of LEDs can be limited using the following sample specific Kconfigs:

- `CONFIG_LED_ROW_COUNT`
- `CONFIG_LED_COLUMN_COUNT`

## Building and Running

This sample can be run on any board with an IS31FL3733 LED driver connected via
I2C, and a node with the [`issi,is31fl3733`](../../../../build/dts/api/bindings/led/issi%2Cis31fl3733.md#std-dtcompatible-issi-is31fl3733) compatible present in its devicetree.

This sample provides a DTS overlay for the [FRDM-K22F](../../../../boards/nxp/frdm_k22f/doc/index.md#frdm_k22f) board
(`boards/frdm_k22f.overlay`). It assumes that the IS31FL3733 LED
controller is connected to I2C0, at address 0x50. The SDB GPIO should be
connected to PTC2 (A3 on the arduino header)

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
