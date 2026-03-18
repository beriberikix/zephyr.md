---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.html
original_path: boards/shields/buydisplay_2_8_tft_touch_arduino/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Buydisplay 2.8” TFT Touch Shield with Arduino adapter

## Overview

The Buydisplay 2.8” TFT Touch Shield has a resolution of 320x240
pixels and is based on the ILI9341 controller. This shield comes with
a capacitive FT6206 controller touchscreen. The Arduino adapter is
required to use this shield.

More information about the shield and Arduino adapter can be found at
the [Buydisplay 2.8” TFT Touch Shield website](https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module) [[1]](#id1) and
[Arduino adapter website](https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno) [[2]](#id3).

### Pin Assignments

| Shield Connector Pin | Function |
| --- | --- |
| D5 | Touch Controller IRQ (see note below) |
| D7 | ILI9341 DC (Data/Command) |
| D10 | ILI9341 Reset |
| D9 | ILI9341 SPI CSn |
| D11 | SPI MOSI (Serial Data Input) |
| D12 | SPI MISO (Serial Data Out) |
| D13 | SPI SCK (Serial Clock Input) |
| SDA | FT6206 SDA |
| SCL | FT6206 SCL |

Note

Touch controller IRQ line is not connected by default. You will need
to solder the `5 INT` jumper to use it. You will also need to
adjust driver configuration and its Device Tree entry to make use of
it.

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=buydisplay_2_8_tft_touch_arduino` when you invoke
`west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=buydisplay_2_8_tft_touch_arduino
```

## References

[[1](#id2)]

[https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module](https://www.buydisplay.com/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module)

[[2](#id4)]

[https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno](https://www.buydisplay.com/arduino-shield-for-tft-lcd-with-ili9341-controller-and-arduino-due-mega-uno)
