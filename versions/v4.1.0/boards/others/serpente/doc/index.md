---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/others/serpente/doc/index.html
original_path: boards/others/serpente/doc/index.html
---

# Arturo182 Serpente

Board Overview

[![../../../../_images/serpente.jpg](../../../../_images/serpente.jpg)
](../../../../_images/serpente.jpg)

Arturo182 Serpente

Name:
:   `serpente`

Vendor:
:   Other/Unknown

Architecture:
:   arm

SoC:
:   samd21e18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/others/serpente/doc/index.rst/../..)

## Overview

The Serpente is a very small low-cost development and prototyping
board equipped with 4MiB flash storage, a PWM enabled RGB led and 6 I/O pins.
The board comes with 3 different USB connector options: USB Type-C plug,
USB Type-C socket and USB Type-A plug.

## Hardware

- ATSAMD21E18A ARM Cortex-M0+ processor at 48 MHz
- 256 KiB flash memory and 32 KiB of RAM
- Extra 4MiB SPI flash memory
- RGB User LED
- Reset button
- Native USB port

### Supported Features

The `serpente` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Serpente documentation](https://www.solder.party/docs/serpente/r2/) [[1]](#id2) has detailed information about the board
including [pinouts](https://www.solder.party/docs/serpente/r2/pinout/) [[2]](#id4) and the [schematic](https://www.solder.party/docs/serpente/r2/downloads/) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 8MHz internal oscillator
with the on-chip PLL generating the 48 MHz system clock.

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which prints “Hello World!”
to the host PC.

### Programming and Debugging

The Serpente ships the BOSSA compatible UF2 bootloader. The bootloader
can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application:

   ```shell
   west build -b serpente samples/basic/blinky
   ```
2. Connect the Serpente to your host computer using USB
3. Tap the reset button twice quickly to enter bootloader mode
4. Flash the image:

   ```shell
   west build -b serpente samples/basic/blinky
   west flash
   ```

   You should see the User LED blink.

## References

[[1](#id3)]

[https://www.solder.party/docs/serpente/r2/](https://www.solder.party/docs/serpente/r2/)

[[2](#id5)]

[https://www.solder.party/docs/serpente/r2/pinout/](https://www.solder.party/docs/serpente/r2/pinout/)

[[3](#id7)]

[https://www.solder.party/docs/serpente/r2/downloads/](https://www.solder.party/docs/serpente/r2/downloads/)
