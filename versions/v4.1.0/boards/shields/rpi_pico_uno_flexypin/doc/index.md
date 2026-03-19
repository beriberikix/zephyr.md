---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/rpi_pico_uno_flexypin/doc/index.html
original_path: boards/shields/rpi_pico_uno_flexypin/doc/index.html
---

# RaspberryPi Pico to UNO FlexyPin Adapter

## Overview

The Raspberry Pi Pico to Uno FlexyPin Adapter is an open-source hardware converter PCB that adapts
the Raspberry Pi Pico to the Arduino UNO form factor
This board is designed to be use with FlexyPin connector pins.
The FlexyPin holds Pico and contacts to castellated through-hole.

With simple soldering, it can also be used as a board to convert the Rapsberry Pi Pico
to the Arduino UNO form factor.

![RaspberryPi Pico to UNO FlexyPin Adapter](../../../../_images/rpi_pico_uno_flexypin.png)

### Pins Assignment of the RaspberryPi Pico to UNO FlexyPin Adapter

| Rpi-Pico Pin | UNO Header |
| --- | --- |
| GP0 (UART0 TX) | D1 |
| GP1 (UART0 RX) | D0 |
| GP2 | D8 |
| GP3 | D9 |
| GP4 | D2 |
| GP5 | D3 |
| GP6 | D4 |
| GP7 | D5 |
| GP8 | D6 |
| GP9 | D7 |
| GP13 | A3 |
| GP14 (I2C1 SDA) | A4 |
| GP15 (I2C1 SCL) | A5 |
| GP16 (SPI0 RX/CIPO) | D12 |
| GP17 (SPI0 CS) | D10 |
| GP18 (SPI0 SCK) | D13 |
| GP19 (SPI0 TX/COPI) | D11 |
| GP20 | D14 |
| GP21 (I2C0 SCL) | D15 |
| GP26 (I2C0 SDA) | A0 |
| GP27 | A1 |
| GP28 | A2 |

## Programming

Set `--shield rpi_pico_uno_flexypin` when you invoke `west build`.
This shield is just a converter, so it is usually used with other Arduino shield.

For example,

```shell
# From the root of the zephyr repository
west build -b rpi_pico --shield rpi_pico_uno_flexypin --shield esp_8266_arduino samples/net/wifi
```

## References
