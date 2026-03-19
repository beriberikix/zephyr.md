---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/basic/fade_led/README.html
original_path: samples/basic/fade_led/README.html
---

# Fade LED

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/fade_led/README.rst/..)

## Overview

This application “fades” a LED using the [PWM API](../../../hardware/peripherals/pwm.md#pwm-api).

The LED starts off increases its brightness until it is fully or nearly fully
on. The brightness then decreases until the LED is off, completing on fade
cycle. Each cycle takes 2.5 seconds, and the cycles repeat forever. The PWM
period is taken from Devicetree. It should be fast enough to be above the
flicker fusion threshold.

## Requirements and Wiring

This sample has the same requirements and wiring considerations as the
[PWM Blinky](../blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.") sample.

## Building and Running

To build and flash this sample for the [nRF52840 DK](../../../boards/nordic/nrf52840dk/doc/index.md#nrf52840dk-nrf52840):

```shell
west build -b nrf52840dk/nrf52840 samples/basic/fade_led
west flash
```

Change `nrf52840dk/nrf52840` appropriately for other supported boards.

After flashing, the sample starts fading the LED as described above. It also
prints information to the board’s console.

## See also

[PWM Interface](../../../doxygen/html/group__pwm__interface.md)
