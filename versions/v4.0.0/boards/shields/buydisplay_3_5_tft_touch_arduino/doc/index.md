---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/buydisplay_3_5_tft_touch_arduino/doc/index.html
original_path: boards/shields/buydisplay_3_5_tft_touch_arduino/doc/index.html
---

# Buydisplay 3.5” TFT Touch Shield with Arduino adapter

## Overview

The Buydisplay 3.5” TFT Touch Shield has a resolution of 320x480
pixels and is based on the ILI9488 controller. On the capacitive touch
version this shield comes with a FT6236 touch controller. The Arduino
adapter is required to use this shield. Note that both display and
Arduino shields are sold in multiple combinations of interfaces. The
current Zephyr driver only supports the 4-wire SPI interface.

More information about the shield and Arduino adapter can be found at
the [Buydisplay 3.5” TFT Touch Shield website](https://www.buydisplay.com/lcd-3-5-inch-320x480-tft-display-module-optl-touch-screen-w-breakout-board) [[1]](#id1) and
[Arduino adapter website](https://www.buydisplay.com/arduino-3-5-tft-lcd-touch-shield-serial-spi-example-for-mega-due) [[2]](#id3).

### Pin Assignments

| Shield Connector Pin | Function |
| --- | --- |
| D5 | Touch Controller IRQ (see note below) |
| D7 | ILI9488 DC (Data/Command) |
| D10 | ILI9488 Reset |
| D9 | ILI9488 SPI CSn |
| D11 | SPI MOSI (Serial Data Input) |
| D12 | SPI MISO (Serial Data Out) |
| D13 | SPI SCK (Serial Clock Input) |
| SDA | FT6236 SDA |
| SCL | FT6236 SCL |

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

Set `--shield buydisplay_3_5_tft_touch_arduino` when you invoke
`west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield buydisplay_3_5_tft_touch_arduino samples/subsys/display/lvgl
```

## References

[[1](#id2)]

[https://www.buydisplay.com/lcd-3-5-inch-320x480-tft-display-module-optl-touch-screen-w-breakout-board](https://www.buydisplay.com/lcd-3-5-inch-320x480-tft-display-module-optl-touch-screen-w-breakout-board)

[[2](#id4)]

[https://www.buydisplay.com/arduino-3-5-tft-lcd-touch-shield-serial-spi-example-for-mega-due](https://www.buydisplay.com/arduino-3-5-tft-lcd-touch-shield-serial-spi-example-for-mega-due)
