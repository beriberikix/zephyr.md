---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ruuvi/ruuvitag/doc/index.html
original_path: boards/ruuvi/ruuvitag/doc/index.html
---

# RuuviTag

Board Overview

[![../../../../_images/ruuvitag.jpg](../../../../_images/ruuvitag.jpg)
](../../../../_images/ruuvitag.jpg)

RuuviTag

Name:
:   `ruuvi_ruuvitag`

Vendor:
:   Ruuvi Innovations Ltd (Oy)

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruuvi/ruuvitag/doc/index.rst/../..)

## Overview

RuuviTag is an advanced battery-operated open-source Bluetooth
enabled sensor beacon platform capable of sending temperature, humidity,
pressure, and motion information over Bluetooth Low Energy.

More information about the board can be found at the
[ruuvitag website](https://ruuvi.com) [[1]](#id2).

## Hardware

RuuviTag’s have the following physical features:

- Nordic Semiconductor nRF52832 System-on-Chip
- STMicroelectronics LIS2DH12 accelerometer
- Bosch BME 280 temperature + relative air humidity + air pressure sensor
- NFC™-A tag antenna
- 1000mAh CR2477 battery
- 2 buttons
- 1 Green LED
- 1 Red LED
- IP67 Enclosure
- Long range RF antenna

### Supported Features

The `ruuvi_ruuvitag` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

- LED0 (red) = P0.17
- LED1 (green) = P0.19

#### Push buttons

- BUTTON0 = SW1 = P0.13

#### Pin descriptions

![RUUVI Pinout](../../../../_images/pinout1.jpg)

- 2 = P0.29 = SPI\_SCK
- 3 = P0.28 = SPI\_MISO
- 10 = P0.04 = GPIO (can be used as a GPIO / ADC pin)
- 11 = P0.05 = GPIO (can be used as a GPIO / ADC pin)
- 12 = P0.25 = SPI\_MOSI
- 13 = P0.19 = LED2 (green) / GPIO (can be used as a GPIO pin but the LED will blink)
- 14 = P0.17 = LED1 (red) / GPIO (can be used as a GPIO pin but the LED will blink)
- 15 = P0.13 = Button / GPIO (can be used as a GPIO pin)
- 16 = GND (Battery’s negative contact)
- 17 = Battery’s positive contact
- 18 = Battery’s positive contact
- 19 = SWDIO
- 20 = SWDCLK
- 21 = P0.18 = SWO / GPIO (can be used as a GPIO pin)
- 22 = P0.21 = Reset / GPIO (can be used as a GPIO pin if no need to reset the device)
- 23 = GND (Battery’s negative contact)
- 24 = P0.31 = GPIO (can be used as a GPIO / ADC pin)
- 25 = P0.30 = GPIO (can be used as a GPIO / ADC pin)

GPIO = General Purpose Input Output pin

P1 = Standard 10-pin ARM Cortex debug connector (on RuuviTag Rev.B1-B5)

- 1 = VDD
- 2 = SWDIO
- 3 = GND (Battery’s negative contact)
- 4 = SWDCLK
- 5 = GND (Battery’s negative contact)
- 6 = SWO
- 7 = No Connect
- 8 = No Connect
- 9 = GND (Battery’s negative contact)
- 10 = Reset

P1 = TC2030 TagConnect (on RuuviTag Rev.B6)

- 1 = Battery’s positive contact
- 2 = SWDIO
- 3 = Reset
- 4 = SWDCLK
- 5 = GND (Battery’s negative contact)
- 6 = SWO

## Programming and Debugging

### Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

The easiest way to flash Zephyr onto a RuuviTag requires an external Ruuvi DEVKIT. More information about the board can be found at the
[ruuvitag devkit](https://lab.ruuvi.com/devshield/) [[2]](#id4).

Once your tag is connected to the DEVKIT and connected to your PC, build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ruuvi_ruuvitag samples/basic/blinky
west flash
```

Advanced users may want to program the RuuviTag without the DEVKIT, this can be achieved via the SWDIO and SWDCLK pins located on the back of the RuuviTag.

### Debugging

If using the Ruuvi DEVKIT refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons on the RuuviTag

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

- [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
- [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in `boards/ruuvi//ruuvi_ruuvitag/ruuvi_ruuvitag.dts`.

## References

[[1](#id3)]

[https://ruuvi.com](https://ruuvi.com)

[[2](#id5)]

[https://lab.ruuvi.com/devshield/](https://lab.ruuvi.com/devshield/)
