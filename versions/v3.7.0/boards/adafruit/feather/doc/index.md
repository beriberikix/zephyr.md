---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/adafruit/feather/doc/index.html
original_path: boards/adafruit/feather/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Adafruit Feather nRF52840 Express

## Overview

The Adafruit Feather nRF52840 provides support for the Nordic Semiconductor
nRF52840 ARM Cortex-M4F CPU and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- USB
- WDT

![Adafruit Feather nRF52840 Express](../../../../_images/adafruit_feather_nrf52840.jpg)

## Hardware

- nRF52840 ARM Cortex-M4F processor at 64 MHz
- 1 MB flash memory and 256 KB of SRAM
- Battery connector and charger for 3.7 V lithium polymer batteries
- Charging indicator LED
- 2 User LEDs
- 1 NeoPixel LED
- Reset button
- SWD connector

### Supported Features

The Adafruit Feather nRF52840 board configuration supports the
following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| SPI | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

The [Adafruit Feather nRF52840 Express Learn site](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/) [[1]](#id1) has detailed
information about the board including [pinouts](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts) [[2]](#id3) and the [schematic](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads) [[3]](#id5).

#### LED

- LED0 (red) = P1.15
- LED1 (blue) = P1.10

#### Push buttons

- SWITCH = P1.02
- RESET = P0.18

## Programming and Debugging

Applications for the `adafruit_feather/nrf52840` board configuration
can be built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Flashing Zephyr onto the `adafruit_feather_nrf52480` board requires
an external programmer. The programmer is attached to the SWD header.

Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

> ```shell
> west build -b adafruit_feather/nrf52840 samples/basic/blinky
> ```

Flash the image.

> ```shell
> west build -b adafruit_feather/nrf52840 samples/basic/blinky
> west flash
> ```

You should see the red LED blink.

## References

[[1](#id2)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/)

[[2](#id4)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/pinouts)

[[3](#id6)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/downloads)
