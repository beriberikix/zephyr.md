---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/samples/basic/rgb_led/README.html
original_path: samples/basic/rgb_led/README.html
---

# PWM RGB LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/rgb_led/README.rst/..)

## Overview

This is a sample app which drives an RGB LED using the [PWM API](../../../hardware/peripherals/pwm.md#pwm-api).

There are three single-color component LEDs in an RGB LED. Each component LED
is driven by a PWM port where the pulse width is changed from zero to the period
indicated in Devicetree. Such period should be fast enough to be above the
flicker fusion threshold (the minimum flicker rate where the LED is perceived as
being steady). The sample causes each LED component to step from dark to max
brightness. Three **for** loops (one for each component LED) generate a gradual
range of color changes from the RGB LED, and the sample repeats forever.

## Requirements

The board must have red, green, and blue LEDs connected via PWM output channels.

The LED PWM channels must be configured using the following [devicetree](../../../build/dts/index.md#dt-guide) aliases, usually in the [BOARD.dts file](../../../build/dts/intro-input-output.md#devicetree-in-out-files):

- `red-pwm-led`
- `green-pwm-led`
- `blue-pwm-led`

You will see at least one of these errors if you try to build this sample for
an unsupported board:

```text
Unsupported board: red-pwm-led devicetree alias is not defined
Unsupported board: green-pwm-led devicetree alias is not defined
Unsupported board: blue-pwm-led devicetree alias is not defined
```

See [boards/nxp/hexiwear/hexiwear\_mk64f12.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/hexiwear/hexiwear_mk64f12.dts) for an example
`BOARD.dts` file which supports this sample.

## Wiring

No additional wiring is necessary if the required devicetree aliases refer to
hardware that is already connected to LEDs on the board.

Otherwise, LEDs should be connected to the appropriate PWM channels.

## Building and Running

For example, to build and flash this board for [Hexiwear](../../../boards/nxp/hexiwear/doc/index.md#hexiwear):

```shell
west build -b hexiwear/mk64f12 samples/basic/rgb_led
west flash
```

Change `hexiwear/mk64f12` appropriately for other supported boards.

## See also

[PWM Interface](../../../doxygen/html/group__pwm__interface.md)
