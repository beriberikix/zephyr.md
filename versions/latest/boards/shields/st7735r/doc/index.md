---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/st7735r/doc/index.html
original_path: boards/shields/st7735r/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Generic ST7735R Display Shield

## Overview

This is a generic shield for display shields based on ST7735R display
controller. More information about the controller can be found in
[ST7735R Datasheet](https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/) [[1]](#id1).

### Pins Assignment of the Generic ST7735R Display Shield

| Arduino Connector Pin | Function | |
| --- | --- | --- |
| D8 | ST7735R Reset |  |
| D9 | ST7735R DC | (Data/Command) |
| D10 | SPI SS | (Serial Slave Select) |
| D11 | SPI MOSI | (Serial Data Input) |
| D12 | SPI MISO | (Serial Data Out) |
| D13 | SPI SCK | (Serial Clock Input) |

### Current supported displays

| Display | Shield Designation |
| --- | --- |
| adafruit 160x128 18bit TFT | st7735r\_ada\_160x128 |

## Requirements

This shield can only be used with a board that provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=st7735r_ada_160x128` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=st7735r_ada_160x128
```

## References

[[1](#id2)]

[https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/](https://www.crystalfontz.com/controllers/Sitronix/ST7735R/319/)
