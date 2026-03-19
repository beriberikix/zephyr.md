---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/st7789v_generic/doc/index.html
original_path: boards/shields/st7789v_generic/doc/index.html
---

# Generic ST7789V Display Shield

## Overview

This is a generic shield for display shields based on ST7789V display
controller. More information about the controller can be found in
[ST7789V Datasheet](https://www.newhavendisplay.com/appnotes/datasheets/LCDs/ST7789V.pdf) [[1]](#id1).

### Pins Assignment of the Generic ST7789V Display Shield

| Arduino Connector Pin | Function | |
| --- | --- | --- |
| D8 | ST7789V Reset |  |
| D9 | ST7789V DC | (Data/Command) |
| D10 | SPI SS | (Serial Slave Select) |
| D11 | SPI MOSI | (Serial Data Input) |
| D12 | SPI MISO | (Serial Data Out) |
| D13 | SPI SCK | (Serial Clock Input) |

### Current supported displays

| Display | Shield Designation |
| --- | --- |
| TL019FQV01 | st7789v\_tl019fqv01 |
| Waveshare 240x240 1.3inch IPS LCD | st7789v\_waveshare\_240x240 |

## Requirements

This shield can only be used with a board that provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield st7789v_tl019fqv01` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield st7789v_tl019fqv01 samples/subsys/display/lvgl
```

## References

[[1](#id2)]

[https://www.newhavendisplay.com/appnotes/datasheets/LCDs/ST7789V.pdf](https://www.newhavendisplay.com/appnotes/datasheets/LCDs/ST7789V.pdf)
