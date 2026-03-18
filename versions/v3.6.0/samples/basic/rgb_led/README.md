---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/basic/rgb_led/README.html
original_path: samples/basic/rgb_led/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# PWM RGB LED

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

See [boards/arm/hexiwear\_k64/hexiwear\_k64.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/hexiwear_k64/hexiwear_k64.dts) for an example
`BOARD.dts` file which supports this sample.

## Wiring

No additional wiring is necessary if the required devicetree aliases refer to
hardware that is already connected to LEDs on the board.

Otherwise, LEDs should be connected to the appropriate PWM channels.

## Building and Running

For example, to build and flash this board for [Hexiwear](../../../boards/arm/hexiwear_k64/doc/index.md#hexiwear-k64):

```shell
west build -b hexiwear_k64 samples/basic/rgb_led
west flash
```

Change `hexiwear_k64` appropriately for other supported boards.
