---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/adafruit/feather_m0_lora/doc/index.html
original_path: boards/adafruit/feather_m0_lora/doc/index.html
---

# Feather M0 LoRa

Board Overview

[![../../../../_images/adafruit_feather_m0_lora.jpg](../../../../_images/adafruit_feather_m0_lora.jpg)
](../../../../_images/adafruit_feather_m0_lora.jpg)

Feather M0 LoRa

Name:
:   `adafruit_feather_m0_lora`

Vendor:
:   Adafruit Industries, LLC

Architecture:
:   arm

SoC:
:   samd21g18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adafruit/feather_m0_lora/doc/index.rst/../..)

## Overview

The Adafruit Feather M0 Lora is a thin, light ARM development
boards with an onboard battery connector and charger for 3.7 V lithium
polymer batteries, charging status indicator and user LEDs, native USB
connector, 20 I/O pins, and a LoRa radio module from Semtech.

## Hardware

- ATSAMD21G18A ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory and 32 KiB of RAM
- Battery connector and charger for 3.7 V lithium polymer batteries
- Charging indicator LED
- User LED
- Reset button
- Native USB port
- SX127x LoRa radio

### Supported Features

The `adafruit_feather_m0_lora` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Adafruit Feather M0 with LoRa radio module Learn site](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module) [[1]](#id2) has detailed
information about the board including [pinouts](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/pinouts) [[2]](#id4) and the [schematic](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/downloads) [[3]](#id6).

### System Clock

The SAMD21 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock.

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the Adafruit Feather M0
with LoRa, SERCOM0 is the Zephyr console and is available on pins 0
(RX) and 1 (TX).

### I2C Port

The SAMD21 MCU has 6 SERCOM based USARTs. On the Adafruit Feather M0
with LoRa, SERCOM3 is available on pin 20 (SDA) and pin 21 (SCL).

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the Adafruit Feather M0
with LoRa, SERCOM4 is available on pin 22 (MISO), pin 23 (MOSI), and
pin 24 (SCK).

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

### LoRa Radio

The Semtech SX127x radio chip on the Adafruit Feather M0 with LoRa
is attached to the SPI port (SERCOM4). Depending on the hardware
version, 433MHz or 900MHz is supported.

## Programming and Debugging

The Adafruit Feather M0 with LoRa ships with a BOSSA compatible
SAM-BA bootloader. The bootloader can be entered by quickly tapping
the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b adafruit_feather_m0_lora samples/hello_world
   ```
2. Connect the Adafruit Feather M0 with LoRa to your host computer
   using USB
3. Connect a 3.3 V USB to serial adapter to the board and to the
   host. See the [Serial Port](#serial-port) section above for the board’s pin
   connections.
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
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
   west build -b adafruit_feather_m0_lora samples/hello_world
   west flash
   ```

   You should see “Hello World! adafruit\_feather\_m0\_lora” in your terminal.

## References

[[1](#id3)]

[https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module)

[[2](#id5)]

[https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/pinouts](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/pinouts)

[[3](#id7)]

[https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/downloads](https://learn.adafruit.com/adafruit-feather-m0-radio-with-lora-radio-module/downloads)
