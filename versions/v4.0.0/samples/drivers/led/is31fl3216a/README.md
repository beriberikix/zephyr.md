---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/drivers/led/is31fl3216a/README.html
original_path: samples/drivers/led/is31fl3216a/README.html
---

# IS31FL3216A LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/is31fl3216a/README.rst/..)

## Overview

This sample controls up to 16 LEDs connected to a is31fl3216a driver.

Each LED is gradually pulsed until it reach 100% of luminosity and gradually
turned off again.

Once each LED was pulsed, multiple LEDs are pulse simultaneously using the
[`led_write_channels()`](../../../../doxygen/html/group__led__interface.md#ga24d4007f81483d0fe8b9988288adf59a) API.

### Test pattern

For each LED:

- Increase the luminosity until 100% is reached
- Decrease the luminosity until completely turned off
- Increase the luminosity of LEDs 2 to 4 until 100% is reached
- Decrease the luminosity of LEDs 2 to 4 until completely turned off

## Building and Running

This sample can be built and executed when the devicetree has an I2C device node
with compatible [`issi,is31fl3216a`](../../../../build/dts/api/bindings/led/issi%2Cis31fl3216a.md#std-dtcompatible-issi-is31fl3216a) enabled, along with the relevant
bus controller node also being enabled.

As an example this sample provides a DTS overlay for the [LPCXpresso55S28](../../../../boards/nxp/lpcxpresso55s28/doc/index.md#lpcxpresso55s28)
board (`boards/lpcxpresso55s28.overlay`). It assumes that a I2C
\_is31fl3216a LED driver (with 16 LEDs wired) is connected to the I2C bus at
address 0x74.

## References

- is31fl3216a: [https://lumissil.com/assets/pdf/core/IS31FL3216A\_DS.pdf](https://lumissil.com/assets/pdf/core/IS31FL3216A_DS.pdf)

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
