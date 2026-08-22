---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/portenta_c33/doc/index.html
original_path: boards/arduino/portenta_c33/doc/index.html
---

# Arduino Portenta C33

Board Overview

[![../../../../_images/portenta_c33.webp](../../../../_images/portenta_c33.webp)
](../../../../_images/portenta_c33.webp)

Arduino Portenta C33

Name:
:   `arduino_portenta_c33`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   r7fa6m5bh3cfc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/portenta_c33/doc/index.rst/../..)

## Overview

The Portenta C33 is a powerful System-on-Module based on the Renesas RA6M5
microcontroller group, which utilizes the high-performance Arm® Cortex®-M33
core. The Portenta C33 shares the same form factor as the Portenta H7 and is
backward compatible with it, making it fully compatible with all Portenta
family shields and carriers through its High-Density connectors.

## Hardware

- Renesas RA6M5 ARM Cortex-M33 processor at 200 MHz
- 24 MHz crystal oscillator
- 32.768 kHz crystal oscillator for RTC
- 2 MB flash memory and 512 KiB of RAM
- 16 MB external QSPI flash
- One RGB user LED
- One reset button
- NXP SE050 secure element
- Onboard 10/100 Ethernet PHY
- WiFi + Bluetooth via ESP32-C3 running [esp-hosted](https://github.com/espressif/esp-hosted) [[3]](#id6) firmware
- Battery charger
- MKR header connector exposing standard peripherals (UART, SPI, I2C, ADC, PWM)
- 160 pins high density Portenta connectors exposing SD, CAN, I2S, SWD interfaces

### Supported Features

The `arduino_portenta_c33` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The [Arduino store](https://store.arduino.cc/products/portenta-c33) [[1]](#id2) has detailed information about board connections. Download
the [Arduino Portenta C33 Schematic](http://docs.arduino.cc/resources/schematics/ABX00074-schematics.pdf) [[2]](#id4) for more details.

### Serial Port

The Portenta C33 exposes 4 serial ports with hardware flow control.

### PWM

The Portenta C33 exposes 10 dedicated independent PWM pins.

### USB Device Port

The RA6M5 MCU has an high speed USB device port that can be used to communicate
with a host PC. See the [USB device support](../../../../samples/subsys/usb/usb.md#usb) sample applications for
more, such as the [USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.") sample which sets up a virtual
serial port that echos characters back to the host PC.
A second full speed USB interface is exposed on the high density connectors.

### DAC

The RA6M5 MCU has two DACs with 12 bits of resolution. On the
Arduino Portenta C33, the DACs are available on pins A5 and A6.

## Programming and Debugging

The `arduino_portenta_c33` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The Arduino Portenta C33 ships with a DFU compatible bootloader. The
bootloader can be entered by quickly tapping the reset button twice.

### Flashing

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b arduino_portenta_c33 samples/hello_world
   ```
2. Connect the Portenta C33 to your host computer using USB
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
   west build -b arduino_portenta_c33 samples/hello_world
   west flash
   ```

   You should see “Hello World! arduino\_portenta\_c33” in your terminal.

## References

[[1](#id3)]

[https://store.arduino.cc/products/portenta-c33](https://store.arduino.cc/products/portenta-c33)

[[2](#id5)]

[http://docs.arduino.cc/resources/schematics/ABX00074-schematics.pdf](http://docs.arduino.cc/resources/schematics/ABX00074-schematics.pdf)

[[3](#id7)]

[https://github.com/espressif/esp-hosted](https://github.com/espressif/esp-hosted)
