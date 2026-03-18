---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/beagle_bcf/doc/index.html
original_path: boards/arm/beagle_bcf/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# BeagleConnect Freedom

## Overview

BeagleBoard.org BeagleConnect Freedom is a wireless
Internet of Things board based on the SimpleLink multi-Standard CC1352P7 wireless MCU.

[![BeagleBoard.org BeagleConnect Freedom](../../../../_images/beagleconnect_freedom.webp)](../../../../_images/beagleconnect_freedom.webp)

BeagleBoard.org BeagleConnect Freedom

## Hardware

BeagleBoard.org BeagleConnect Freedom board features the TI CC1352P7 wireless microcontroller.
The BeagleConnect Freedom is the first available BeagleConnect solution consisting
of a board and a case which ships programmed and ready to be used.

BeagleConnect Freedom board runs the Zephyr RTOS and has mikroBUS ports along
with BLE and Sub-GHz radios on it.

The CC1352P7 wireless MCU has a 48 MHz Arm Cortex-M4F SoC and a Bluetooth Low Energy and IEEE 802.15.4.

The board also features a TI MSP430F5503 microcontroller used as a USB-to-serial bridge and
GPIO expander.

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| GPIO | on-chip | gpio |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PINMUX | on-chip | pinmux |
| UART | on-chip | serial |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| HWINFO | on-chip | hwinfo |
| I2C | off-chip | OPT3001 |
| I2C | off-chip | HDC2010 |
| I2C | off-chip | BCF\_BRIDGE\_MCU |

### Connections and IOs

[![Front connections](../../../../_images/beagleconnect_freedom_front_annotated.webp)](../../../../_images/beagleconnect_freedom_front_annotated.webp)

BeagleConnect Freedom front connections

[![Back connections](../../../../_images/beagleconnect_freedom_back_annotated.webp)](../../../../_images/beagleconnect_freedom_back_annotated.webp)

BeagleConnect Freedom back connections

| Pin | Function | Usage |
| --- | --- | --- |
| DIO5 | RST\_MB2 | Reset mikroBUS port 2 |
| DIO6 | RST\_MB1 | Reset mikroBUS port 1 |
| DIO7 | INT\_SENSOR | On-board sensor interrupts |
| DIO8 | FLASH\_CS | SPI flash chip-select |
| DIO9 | SDO / PICO | SPI serial data output |
| DIO10 | SCK | SPI serial clock |
| DIO11 | SDI / POCI | SPI serial data input |
| DIO12 | CC1352\_RX | UART RXD mikroBUS port 1 or MSP430 |
| DIO13 | CC1352\_TX | UART TXD mikroBUS port 1 or MSP430 |
| DIO14 | I2C\_CTRL | Enable on-board sensor I2C bus |
| DIO15 | USER\_BOOT | BOOT button status |
| DIO16 | INT\_MB1 | INTERRUPT PIN on mikroBUS port 1 |
| DIO17 | PWM\_MB1 | PWM PIN on mikroBUS port 1 |
| DIO18 | LED\_LINK | Radio link indicator LED |
| DIO19 | PWM\_MB2 | PWM PIN on mikroBUS port 2 |
| DIO20 | INT\_MB2 | INTERRUPT PIN on mikroBUS port 2 |
| DIO21 | MB2\_RX | UART RXD on mikroBUS port 2 |
| DIO22 | MB2\_TX | UART TXD on mikroBUS port 2 |
| DIO23 | AN\_MB1 | ANALOG PIN on mikroBUS port 1 |
| DIO24 | AN\_MB2 | ANALOG PIN on mikroBUS port 2 |
| DIO25 | SCL | I2C SCL |
| DIO26 | SDA | I2C SDA |
| DIO27 | CS\_MB2 | SPI CS on microBUS port 2 |
| DIO28 | CS\_MB1 | SPI CS on microBUS port 1 |
| DIO29 | REF\_SW\_CTRL1 | Antenna mux PA enable |
| DIO30 | REF\_SW\_CTRL2 | Antenna mux SubG enable |

### System requirements

#### Prerequisites

BeagleConnect Freedom requires [CC1352 Flasher](https://pypi.org/project/cc1352-flasher/) for
flashing Zephyr firmware using `west flash`.

```shell
pip3 install cc1352-flasher
```

## References

BeagleBoard.org BeagleConnect Freedom reference:
:   [https://beagleconnect.org](https://beagleconnect.org)
