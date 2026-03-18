---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/drivers/misc/grove_display/README.html
original_path: samples/drivers/misc/grove_display/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Grove LCD

## Overview

This sample displays an incrementing counter through the Grove LCD, with
changing backlight.

## Requirements

To use this sample, the following hardware is required:

- A board with ADC support
- [Grove LCD module](http://wiki.seeed.cc/Grove-LCD_RGB_Backlight/)
- [Grove Base Shield](https://wiki.seeedstudio.com/Base_Shield_V2/) [Optional]

## Wiring

You will need to connect the Grove LCD via the Grove shield onto a board that
supports Arduino shields.

On some boards you will need to use 2 pull-up resistors (10k Ohm) between the
SCL/SDA lines and 3.3V.

Take note that even though SDA and SCL are connected to a 3.3V power source, the
Grove LCD VDD line needs to be connected to the 5V power line, otherwise
characters will not be displayed on the LCD (3.3V is enough to power just the
backlight).

## Building and Running

This sample should work on any board that has I2C enabled and has an Arduino
shield interface. For example, it can be run on the FRDM K64F board as
described below:

```shell
west build -b frdm_k64f samples/drivers/misc/grove_display
west flash
```
