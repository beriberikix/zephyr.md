---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/itsybitsy/doc/index.html
original_path: boards/adafruit/itsybitsy/doc/index.html
---

# ItsyBitsy nRF52840

Board Overview

[![../../../../_images/adafruit_itsybitsy_nrf52840.jpeg](../../../../_images/adafruit_itsybitsy_nrf52840.jpeg)
](../../../../_images/adafruit_itsybitsy_nrf52840.jpeg)

ItsyBitsy nRF52840

Name:
:   `adafruit_itsybitsy`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/itsybitsy/doc/index.rst/../..)

## Overview

The Adafruit ItsyBitsy nRF52840 Express is a small (36 mm x 18 mm) ARM
development board with an onboard RGB LED, USB port, 2 MB of QSPI flash,
and range of I/O broken out onto 21 GPIO pins.

This development kit has the following features:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- I2S
- MPU
- NVIC
- PWM
- QSPI
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- SPI
- UARTE
- USB
- WDT

## Hardware

- nRF52840 ARM Cortex-M4F CPU at 64MHz
- 1 MB of flash memory and 256 KB of SRAM
- 2 MB of QSPI flash
- A user LED
- A user switch
- An RGB DotStar LED
- Native USB port
- One reset button

### Supported Features

The `adafruit_itsybitsy` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Adafruit ItsyBitsy nRF52840 Express Learn site](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express) [[1]](#id2) has detailed
information about the board including [pinouts](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads) [[3]](#id6).

#### LED

- LED0 (red) = P0.06
- LED1 (Adafruit DotStar)

  > - DATA = P0.08
  > - CLK = P1.09

#### Push buttons

- SWITCH = P0.29
- RESET = P0.18

#### Logging

Logging is done using the USB-CDC port. See the [Logging](../../../../samples/subsys/logging/logger/README.md#logging "Output log messages to the console using the logging subsystem.") sample
or the [Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.") sample applications to see how this works.

## Testing LEDs and buttons on the Adafruit ItsyBitsy nRF52840 Express

The [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.") sample lets you test the buttons (switches) and the red LED.
The [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample lets you test the red LED.

The DotStar LED has been implemented as a SPI device and can be tested
with the [LED strip](../../../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.") sample application.

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/adafruit/itsybitsy/adafruit\_itsybitsy\_nrf52840.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adafruit/itsybitsy/adafruit_itsybitsy_nrf52840.dts).

## Programming and Debugging

The ItsyBitsy ships with the BOSSA compatible UF2 bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

### First time setup

Some versions of this board were shipped with a buggy bootloader.
Ensure that the bootloader is up to date by following the
[Adafruit UF2 Bootloader update](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader) [[4]](#id8) tutorial. Note that this tutorial
was made for the Adafruit Feather nRF52840, but the steps to update
the bootloader are the same for the ItsyBitsy. The files for the
ItsyBitsy bootloader can be found in the [Adafruit nRF52 Bootloader repo](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases) [[5]](#id10).

The building and flashing of Zephyr applications have been tested with
release 0.7.0 of the UF2 bootloader.

### Flashing

Flashing is done by dragging and dropping the built Zephyr UF2-file
into the `ITSY840BOOT` drive.

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
   sample application:

   ```shell
   west build -b adafruit_itsybitsy/nrf52840 samples/basic/blinky
   ```
2. Connect the ItsyBitsy to your host computer using USB
3. Tap the reset button twice quickly to enter bootloader mode
4. Flash the image:

   Drag and drop the file `samples/basic/blinky/build/zephyr/zephyr.uf2`
   into `ITSY840BOOT`

The device will disconnect and you should see the red LED blink.

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads](https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/downloads)

[[4](#id9)]

[https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather/update-bootloader)

[[5](#id11)]

[https://github.com/adafruit/Adafruit\_nRF52\_Bootloader/releases](https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases)
