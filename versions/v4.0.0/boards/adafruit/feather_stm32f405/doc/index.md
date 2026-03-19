---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/adafruit/feather_stm32f405/doc/index.html
original_path: boards/adafruit/feather_stm32f405/doc/index.html
---

# Feather STM32F405 Express

Board Overview

[![../../../../_images/adafruit_feather_stm32f405.jpg](../../../../_images/adafruit_feather_stm32f405.jpg)
](../../../../_images/adafruit_feather_stm32f405.jpg)

Feather STM32F405 Express

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   stm32f405xx

## Overview

The Adafruit Feather STM32F405 is an ARM Development board in the
Feather standard layout, sharing peripheral placement with other
devices labeled as Feathers or FeatherWings. The board is equipped
with a lithium ion battery charger, native USB C connector, 2MB of
external flash memory, and SD card socket.

## Hardware

- STM32F405 Cortex M4 with FPU and 1MB Flash, 168MHz speed
- 192KB RAM total - 128 KB RAM + 64 KB program-only/cache RAM
- USB C power and data
- LiPo connector and charger
- SD socket on the bottom, connected to SDIO port
- 2 MB SPI Flash chip
- Built in NeoPixel indicator
- I2C, UART, GPIO, ADCs, DACs
- Qwiic/STEMMA-QT connector for fast I2C connectivity
- SWD SMT mount region on board underside.

### Supported Features

The Adafruit Feather STM32F405 board configuration supports the
following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| USB | on-chip | USB device |

Other hardware features have not been enabled yet for this board.

### Connections and IOs

The [Adafruit Feather STM32F405 Express Learn site](https://learn.adafruit.com/adafruit-stm32f405-feather-express/) [[1]](#id2) has detailed
information about the board including [pinouts](https://learn.adafruit.com/adafruit-stm32f405-feather-express/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/adafruit-stm32f405-feather-express/downloads) [[3]](#id6).

### System Clock

The STM32F405 is configured to use the 12MHz HSE Oscillator to produce
a 168MHz system clock.

### Serial Port

The STM32F405 UART 3 peripheral is available on the TX (PB10) and RX
(PB11) pins.

### I2C Port

The STM32F405 I2C1 peripheral is available on the SDA (PB7) and SCL
(PB6) pins.

### SPI Port

The STM32F405 SPI2 peripheral is available on the SCK (PB13), MI
(PB14) and MO (PB15) pins.

SPI1 uses SCK (PB3), MI (PB4), MO (PB5) and SS (PA15) pins and is
dedicated to the 2 MB SPI Flash chip.

## Programming and Debugging

DFU-Util programming is supported through Zephyr by default. Set up
of the built in DFU-Util bootloader is possible by following the
[instructions on the Learn website](https://learn.adafruit.com/adafruit-stm32f405-feather-express/dfu-bootloader-details) [[4]](#id8).

### Flashing

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application:

   ```shell
   west build -b adafruit_feather_stm32f405 samples/basic/blinky
   ```
2. On the Adafruit Feather STM32F405, connect the 3.3V pin to the B0 boot pin
   with a jumper wire.
3. Flash the image:

   ```shell
   west build -b adafruit_feather_stm32f405 samples/basic/blinky
   west flash
   ```

   You should see the D13 LED blinking.

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-stm32f405-feather-express/](https://learn.adafruit.com/adafruit-stm32f405-feather-express/)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-stm32f405-feather-express/pinouts](https://learn.adafruit.com/adafruit-stm32f405-feather-express/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-stm32f405-feather-express/downloads](https://learn.adafruit.com/adafruit-stm32f405-feather-express/downloads)

[[4](#id9)]

[https://learn.adafruit.com/adafruit-stm32f405-feather-express/dfu-bootloader-details](https://learn.adafruit.com/adafruit-stm32f405-feather-express/dfu-bootloader-details)
