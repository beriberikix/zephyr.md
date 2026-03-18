---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/adafruit_data_logger/doc/index.html
original_path: boards/shields/adafruit_data_logger/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Adafruit Data Logger Shield

## Overview

The [Adafruit Data Logger Shield](https://learn.adafruit.com/adafruit-data-logger-shield/) rev. B features an [NXP PCF8523 Real-Time Clock/Calendar with
Battery Backup](https://www.nxp.com/docs/en/data-sheet/PCF8523.pdf), an SD card interface, two user LEDs, and a prototyping area.

![Adafruit Data Logger Shield](../../../../_images/adafruit_data_logger.jpg)

Adafruit Data Logger Shield (Credit: Adafruit)

Note

The older revision A of the Adafruit Data Logger Shield is not supported.

### Pin Assignments

| Shield Connector Pin | Function |
| --- | --- |
| D3 | User LED1 (green) [[1]](#id5) |
| D4 | User LED2 (red) [[1]](#id5) |
| D7 | PCF8523 RTC INT1 [[2]](#id6) |
| D10 | SD card SPI CS |
| D11 | SD card SPI MOSI |
| D12 | SD card SPI MISO |
| D13 | SD card SPI SCK |
| SDA | PCF8523 RTC I2C SDA |
| SCL | PCF8523 RTC I2C SCL |

[1]
([1](#id2),[2](#id3))

The user LEDs are not connected to `D3` and `D4` by default. Jumper or jumper wire
connections must be established between the `L1` and `Digital I/O 3` pins for `LED1`
and `L2` and `Digital I/O 4` pins for `LED2` if they are to be used.

[[2](#id4)]

The PCF8523 RTC `INT1` interrupt output pin is not connected to `D7` by default. A jumper
wire connection must be established between the `SQ` pin and the `Digital I/O 7` pin in
order to use the RTC interrupt functionality (i.e. alarm callback, 1 pulse per second
callback). The `INT1` interrupt output is open-drain, but the shield definition enables an
internal GPIO pull-up and thus no external pull-up resistor is needed.

## Requirements

This shield can only be used with a board which provides a configuration for Arduino connectors and
defines node aliases for SPI and GPIO interfaces (see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=adafruit_data_logger` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b frdm_k64f tests/drivers/rtc/rtc_api -- -DSHIELD=adafruit_data_logger
```
