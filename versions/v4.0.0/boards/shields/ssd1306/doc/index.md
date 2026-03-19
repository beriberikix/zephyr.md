---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/ssd1306/doc/index.html
original_path: boards/shields/ssd1306/doc/index.html
---

# SSD1306 128x64(/32) pixels generic shield

## Overview

This is a generic shield for 128x64(/32) pixel resolution OLED displays
based on SSD1306 controller. These displays have an I2C interface and
usually only four pins: GND, VCC, SCL and SDA. Display pins can be
connected to the pin header of a board using jumper wires.

### Current supported displays

| Display | Controller / Driver | Shield Designation |
| --- | --- | --- |
| No Name 128x64 pixel | SSD1306 / ssd1306 | ssd1306\_128x64 |
| No Name 128x32 pixel | SSD1306 / ssd1306 | ssd1306\_128x32 |
| No Name 128x64 pixel | SH1106 / ssd1306 | sh1106\_128x64 |

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino connectors and defines a node alias for the I2C interface
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield ssd1306_128x64` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b frdm_k64f --shield ssd1306_128x64 samples/subsys/display/lvgl
```
