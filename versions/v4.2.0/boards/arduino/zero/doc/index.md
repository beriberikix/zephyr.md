---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/zero/doc/index.html
original_path: boards/arduino/zero/doc/index.html
---

# Arduino/Genuino Zero

Board Overview

[![../../../../_images/arduino_zero.jpg](../../../../_images/arduino_zero.jpg)
](../../../../_images/arduino_zero.jpg)

Arduino/Genuino Zero

Name:
:   `arduino_zero`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   samd21g18a

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/zero/doc/index.rst/../..)

## Overview

The Arduino Zero is a maker-friendly development board with
Atmel’s Embedded Debugger (EDBG), which provides a full
debug interface without the need for additional hardware.

## Hardware

- ATSAMD21G18A ARM Cortex-M0+ processor at 48 MHz
- 32.768 kHz crystal oscillator
- 256 KiB flash memory and 32 KiB of RAM
- 3 user LEDs
- One reset button
- On-board USB based EDBG unit with serial console
- Native USB port

### Supported Features

The `arduino_zero` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Arduino store](https://store.arduino.cc/genuino-zero) [[1]](#id2) has detailed information about board
connections. Download the [Arduino Zero Schematic](https://www.arduino.cc/en/uploads/Main/Zero_V1.0.pdf) [[2]](#id4) for more detail.

### System Clock

The SAMD21 MCU is configured to use the 32.768 kHz external oscillator
with the on-chip PLL generating the 48 MHz system clock. The internal
APB and GCLK unit are set up in the same way as the upstream Arduino
libraries.

### Serial Port

The SAMD21 MCU has 6 SERCOM based USARTs. One of the USARTs
(SERCOM5) is connected to the onboard Atmel Embedded Debugger (EDBG).
SERCOM0 is available on the D0/D1 pins.

### PWM

The SAMD21 MCU has 3 TCC based PWM units with up to 4 outputs each and a period
of 24 bits or 16 bits. If `CONFIG_PWM_SAM0_TCC` is enabled then LED0 is
driven by TCC2 instead of by GPIO.

### SPI Port

The SAMD21 MCU has 6 SERCOM based SPIs. On the Arduino Zero, SERCOM4
is available on the 6 pin connector at the edge of the board.

### USB Device Port

The SAMD21 MCU has a USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.

### DAC

The SAMD21 MCU has a single channel DAC with 10 bits of resolution. On the
Arduino Zero, the DAC is available on pin A0.

## Programming and Debugging

The `arduino_zero` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The Arduino Zero comes with a Atmel Embedded Debugger (EDBG). This
provides a debug interface to the SAMD21 chip and is supported by
OpenOCD.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b arduino_zero samples/hello_world
   ```
2. Connect the Arduino Zero to your host computer using the USB debug
   port.
3. Run your favorite terminal program to listen for output. Under Linux the
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
4. To flash an image:

   ```shell
   west build -b arduino_zero samples/hello_world
   west flash
   ```

   You should see “Hello World! arduino\_zero” in your terminal.

## References

[[1](#id3)]

[https://store.arduino.cc/genuino-zero](https://store.arduino.cc/genuino-zero)

[[2](#id5)]

[https://www.arduino.cc/en/uploads/Main/Zero\_V1.0.pdf](https://www.arduino.cc/en/uploads/Main/Zero_V1.0.pdf)
