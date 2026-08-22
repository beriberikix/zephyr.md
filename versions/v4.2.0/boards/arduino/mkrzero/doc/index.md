---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/mkrzero/doc/index.html
original_path: boards/arduino/mkrzero/doc/index.html
---

# Arduino MKR Zero

Board Overview

[![../../../../_images/arduino_mkrzero.jpg](../../../../_images/arduino_mkrzero.jpg)
](../../../../_images/arduino_mkrzero.jpg)

Arduino MKR Zero

Name:
:   `arduino_mkrzero`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   samd21g18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/mkrzero/doc/index.rst/../..)

## Overview

The Arduino MKR Zero built with smaller MKR form factor and powered by Atmel’s SAMD21 MCU.
This board come with microSD card holder that allows you to play with music files with no extra hardware.

## Hardware

- ATSAMD21G18A ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory and 32 KiB of RAM
- One user LEDs
- One reset button
- microSD card slot
- ATECC508A secure element

### Supported Features

The `arduino_mkrzero` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Arduino store](https://store.arduino.cc/collections/boards/products/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data) [[1]](#id2) has detailed information about board
connections. Download the [Arduino MKR Zero Schematic](https://www.arduino.cc/en/uploads/Main/ArduinoMKRZero-schematic.pdf) [[2]](#id4) for more detail.

### System Clock

The SAMD21 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock. The internal
APB and GCLK unit are set up in the same way as the upstream Arduino
libraries.

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. SERCOM5 is available on pins 13(PA23) and 14(PA22).

### PWM

The SAMD21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the Arduino MKR Zero, SERCOM1
is available on pin 8, 9, and 10.
SERCOM2 connect to microSD card slot as SPI interface.

### I2C Port

The SAMD21 MCU has 6 SERCOM based I2Cs. SERCOM0 is available on pin 11(PA08) and 12(PA09).
This I2C bus also available as ESLOV(JST SH 5pin) socket.
ATECC508A secure element is connect to this I2C bus.

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

### DAC

The SAMD21 MCU has a single channel DAC with 10 bits of resolution. On the
Arduino MKR Zero, the DAC is available on pin A0.

## Programming and Debugging

The `arduino_mkrzero` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The Arduino MKR Zero ships the BOSSA compatible bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b arduino_mkrzero samples/hello_world
   ```
2. Connect the MKR Zero to your host computer using USB
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
   west build -b arduino_mkrzero samples/hello_world
   west flash
   ```

   You should see “Hello World! arduino\_mkrzero” in your terminal.

## References

[[1](#id3)]

[https://store.arduino.cc/collections/boards/products/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data](https://store.arduino.cc/collections/boards/products/arduino-mkr-zero-i2s-bus-sd-for-sound-music-digital-audio-data)

[[2](#id5)]

[https://www.arduino.cc/en/uploads/Main/ArduinoMKRZero-schematic.pdf](https://www.arduino.cc/en/uploads/Main/ArduinoMKRZero-schematic.pdf)
