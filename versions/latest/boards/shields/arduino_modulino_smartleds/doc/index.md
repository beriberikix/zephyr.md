---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/arduino_modulino_smartleds/doc/index.html
original_path: boards/shields/arduino_modulino_smartleds/doc/index.html
---

# Arduino Modulino smart LEDs

## Overview

The Arduino Modulino smart LEDs is a QWIIC compatible module with 8 addressable
LEDs.

![Arduino Modulino Smart LEDs](https://docs.zephyrproject.org/4.2.0/_images/arduino_modulino_smartleds.webp)

## Programming

Set `--shield arduino_modulino_smartleds` when you invoke `west build`, the
leds will be available through the LED strip subsystem.

For example,

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi --shield arduino_modulino_smartleds samples/drivers/led/led_strip
```
