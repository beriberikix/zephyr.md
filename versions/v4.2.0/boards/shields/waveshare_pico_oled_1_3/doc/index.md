---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/shields/waveshare_pico_oled_1_3/doc/index.html
original_path: boards/shields/waveshare_pico_oled_1_3/doc/index.html
---

# Waveshare 1.3inch OLED Display Module for Raspberry Pi Pico

## Overview

The Waveshare 1.3inch OLED Display Module for Raspberry Pi Pico is
a 64x128 vertically long LCD module based on the SinoWealth SH1107 controller.
This module connects via I2C and optionally can use SPI(need soldering).
This display module has two buttons that the user program can use.
It is convenient for implementing user interfaces.

More information about the shield and Arduino adapter can be found at
the [Waveshare Pico OLED 1.3 Module website](https://www.waveshare.com/wiki/Pico-OLED-1.3) [[1]](#id1).

### Pin Assignments

| Name | Function | Usage |
| --- | --- | --- |
| GP6 | I2C\_SDA | I2C Data input (I2C1\_SDA) |
| GP7 | I2C\_SCL | I2C Clock input (I2C1\_SCL) |
| GP8 | OLED\_DC | Data/Command control pin (optional) |
| GP9 | OLED\_CS | SPI Chip Select (SPI1\_CSN, optional) |
| GP10 | OLED\_CLK | SPI Clock input (SPI1\_SCK, optional) |
| GP11 | OLED\_DIN | SPI Data input (SPI1\_TX, optional) |
| GP12 | OLED\_RST | Reset |
| GP15 | GPIO | User Key 0 |
| GP17 | GPIO | User Key 1 |

Note

The SPI interface is not available by default.
Switch the J1, J2, and J3 jumper by moving 0-ohm registers
to the SPI side to enable SPI.

## Programming

Set `-DSHIELD=waveshare_pico_oled_1_3` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b rpi_pico --shield waveshare_pico_oled_1_3 samples/subsys/display/lvgl
```

## References

[[1](#id2)]

[https://www.waveshare.com/wiki/Pico-OLED-1.3](https://www.waveshare.com/wiki/Pico-OLED-1.3)
