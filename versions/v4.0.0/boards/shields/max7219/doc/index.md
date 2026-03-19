---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/max7219/doc/index.html
original_path: boards/shields/max7219/doc/index.html
---

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

Set `--shield max7219_8x8` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield max7219_8x8 samples/drivers/display/
```
