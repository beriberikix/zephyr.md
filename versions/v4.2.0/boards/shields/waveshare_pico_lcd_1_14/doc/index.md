---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/waveshare_pico_lcd_1_14/doc/index.html
original_path: boards/shields/waveshare_pico_lcd_1_14/doc/index.html
---

# Waveshare 1.14inch LCD Display Module for Raspberry Pi Pico

## Overview

The Waveshare 1.14inch LCD Display Module for Raspberry Pi Pico is
a 240x135/65K color IPS LCD module based on the ST7789V controller.
This module connects via SPI.
This display module has two buttons and joystick that the user program can use.
It is convenient for implementing user interfaces.

More information about the shield and Arduino adapter can be found at
the [Waveshare Pico-LCD-1.14 Module website](https://www.waveshare.com/wiki/Pico-LCD-1.14) [[1]](#id1).

### Pin Assignments

| Name | Function | Usage |
| --- | --- | --- |
| GP2 | UP | Joystick Up |
| GP3 | CTRL | Joystick Center |
| GP8 | LCD\_DC | Data/Command control pin |
| GP9 | LCD\_CS | SPI Chip Select (SPI1\_CSN) |
| GP10 | LCD\_CLK | SPI Clock input (SPI1\_SCK) |
| GP11 | LCD\_DIN | SPI Data input (SPI1\_TX) |
| GP12 | LCD\_RST | Reset |
| GP13 | LCD\_BL | Backlight |
| GP15 | GPIO | User Key A |
| GP17 | GPIO | User Key 1 |
| GP18 | DOWN | Joystick Down |
| GP20 | RIGHT | Joystick Right |

## Programming

Set `-DSHIELD=waveshare_pico_lcd_1_14` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_oled_1_14 samples/subsys/display/lvgl
```

## References

[[1](#id2)]

[https://www.waveshare.com/wiki/Pico-LCD-1.14](https://www.waveshare.com/wiki/Pico-LCD-1.14)
