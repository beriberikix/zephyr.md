---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/max7219/doc/index.html
original_path: boards/shields/max7219/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MAX7219 LED display driver shield

## Overview

This is a generic shield for LED matrix based on MAX7219.
These displays have an SPI interface and usually
only five pins: VCC, GND, DIN, CS, and CLK.

### Current supported displays

| Display | Controller | Shield Designation |
| --- | --- | --- |
| No Name 8x8 pixel | MAX7219 | max7219\_8x8 |

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino connectors and defines a node alias for the SPI interface
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=max7219_8x8` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/drivers/display/ -- -DSHIELD=max7219_8x8
```
