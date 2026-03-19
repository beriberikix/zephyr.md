---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/grand_central_m4_express/doc/index.html
original_path: boards/adafruit/grand_central_m4_express/doc/index.html
---

# Grand Central M4 Express

Board Overview

[![../../../../_images/adafruit_grand_central_m4_express.webp](../../../../_images/adafruit_grand_central_m4_express.webp)
](../../../../_images/adafruit_grand_central_m4_express.webp)

Grand Central M4 Express

Name:
:   `adafruit_grand_central_m4_express`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   samd51p20a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/grand_central_m4_express/doc/index.rst/../..)

## Overview

The Adafruit Grand Central M4 Express is an ARM development board with the
form factor of an Arduino Mega.
It features 70 GPIO pins, a microSDHC slot and 8MiB of QSPI Flash.

## Hardware

- ATSAMD51P20A ARM Cortex-M4F processor at 120 MHz
- 1024 KiB of flash memory and 256 KiB of RAM
- 8 MiB of QSPI flash
- A red user LED
- A RGB “NeoPixel” / WS2812B LED
- A microSDHC slot (connected via SPI)
- Native USB port

### Supported Features

The `adafruit_grand_central_m4_express` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Adafruit Learning System](https://learn.adafruit.com/adafruit-grand-central) [[1]](#id2) has detailed information about
the board including [pinouts](https://learn.adafruit.com/adafruit-grand-central/pinouts) [[2]](#id4) and the [schematics](https://learn.adafruit.com/adafruit-grand-central/downloads) [[3]](#id6).

### System Clock

The SAMD51 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 120 MHz system clock.

### Serial Port

The SAMD51 MCU has 8 SERCOM based UARTs. On the Grand Central, SERCOM0 is
the Zephyr console and is available on RX(PB25) and TX(PB24).

### SPI Port

The SAMD51 MCU has 8 SERCOM based SPIs. On the Grand Central, SERCOM7 has been
set into SPI mode to connect to devices over the SCK(PD09), MOSI(PD08), and MISO(PD11) pins.
Additionally SERCOM2 has been configured as SPI to access the microSDHC card.

### I2C Port

The SAMD51 MCU has 8 SERCOM based I2Cs. On the Grand Central, SERCOM3 has been
configured as I2C to connect to devices over the SCL(PB21) and SDA(PB20) pins.

### USB Device Port

The SAMD51 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

## Programming and Debugging

The Grand Central ships with a BOSSA compatible UF2 bootloader.
The bootloader can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b adafruit_grand_central_m4_express samples/hello_world
   ```
2. Connect the Grand Central to your host computer using USB.
3. Connect a 3.3 V USB to serial adapter to the board and to the
   host. See the [Serial Port](#serial-port) section above for the board’s pin
   connections.
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
5. Tap the reset button twice quickly to enter bootloader mode
6. Flash the image:

   ```shell
   west build -b adafruit_grand_central_m4_express samples/hello_world
   west flash
   ```

   You should see “Hello World! adafruit\_grand\_central\_m4\_express” in your terminal.

### Debugging

In addition to the built-in bootloader, the Grand Central can be flashed and
debugged using a SWD probe such as the Segger J-Link.

1. Connect the probe to the board using the 10-pin SWD interface.
2. Flash the image:

   ```shell
   west build -b adafruit_grand_central_m4_express samples/hello_world
   west flash -r openocd
   ```
3. Start debugging:

   ```shell
   west build -b adafruit_grand_central_m4_express samples/hello_world
   west debug
   ```

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-grand-central](https://learn.adafruit.com/adafruit-grand-central)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-grand-central/pinouts](https://learn.adafruit.com/adafruit-grand-central/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-grand-central/downloads](https://learn.adafruit.com/adafruit-grand-central/downloads)
