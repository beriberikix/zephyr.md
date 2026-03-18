---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/adafruit_2_8_tft_touch_v2/doc/index.html
original_path: boards/shields/adafruit_2_8_tft_touch_v2/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Adafruit 2.8” TFT Touch Shield v2

## Overview

The Adafruit 2.8” TFT Touch Shield v2 with a
resolution of 320x240 pixels, is based on the ILI9341 controller.
This shield comes with a resistive (STMPE610 controller)
or capacitive (FT6206 controller) touchscreen. While the
Zephyr RTOS supports display output to these screens,
touchscreen input is supported only on Capacitive Touch version.
More information about the shield can be found
at the [Adafruit 2.8” TFT Touch Shield v2 website](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2) [[1]](#id1).

### Pins Assignment of the Adafruit 2.8” TFT Touch Shield v2

| Shield Connector Pin | Function |
| --- | --- |
| D4 | MicroSD SPI CSn |
| D7 | Touch Controller IRQ (see note below) |
| D8 | STMPE610 SPI CSn (Resistive Touch Version) |
| D9 | ILI9341 DC (Data/Command) |
| D10 | ILI9341 SPI CSn |
| D11 | SPI MOSI (Serial Data Input) |
| D12 | SPI MISO (Serial Data Out) |
| D13 | SPI SCK (Serial Clock Input) |
| SDA | FT6206 SDA (Capacitive Touch Version) |
| SCL | FT6206 SCL (Capacitive Touch Version) |

Note

Touch controller IRQ line is not connected by default. You will need to
solder the `ICSP_SI1` jumper to use it. You will also need to adjust
driver configuration and its Device Tree entry to make use of it.

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino or Arduino Nano connectors and defines node aliases for SPI and
GPIO interfaces (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=adafruit_2_8_tft_touch_v2` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/subsys/display/lvgl -- -DSHIELD=adafruit_2_8_tft_touch_v2
```

If the shield is connected to a board which has Arduino Nano connector,
set `-DSHIELD=adafruit_2_8_tft_touch_v2_nano` when you invoke `west build`.

```shell
# From the root of the zephyr repository
west build -b arduino_nano_33_ble samples/subsys/display/lvgl -- -DSHIELD=adafruit_2_8_tft_touch_v2_nano
```

## References

[[1](#id2)]

[https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2](https://learn.adafruit.com/adafruit-2-8-tft-touch-shield-v2)
