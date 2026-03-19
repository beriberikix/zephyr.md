---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/drivers/led/pwm/README.html
original_path: samples/drivers/led/pwm/README.html
---

# LED PWM

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/drivers/led/pwm/README.rst/..)

## Overview

This sample allows to test the led-pwm driver. The first “pwm-leds” compatible
device instance found in DT is used. For each LEDs attached to this device
(child nodes) the same test pattern (described below) is executed. The LED API
functions are used to control the LEDs.

### Test pattern

For each PWM LEDs (one after the other):

- Turning on
- Turning off
- Increasing brightness gradually
- Decreasing brightness gradually
- Blinking on: 0.1 sec, off: 0.1 sec
- Blinking on: 1 sec, off: 1 sec
- Turning off

## Building and Running

This sample can be built and executed on all the boards with PWM LEDs connected.
The LEDs must be correctly described in the DTS: the compatible property of the
device node must match “pwm-leds”. And for each LED, a child node must be
defined and the PWM configuration must be provided through a “pwms” phandle’s
node.

## See also

[LED Interface](../../../../doxygen/html/group__led__interface.md)
