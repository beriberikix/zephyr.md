---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/rakwireless/rak5010/doc/index.html
original_path: boards/rakwireless/rak5010/doc/index.html
---

# RAK5010

Board Overview

[![../../../../_images/rak5010-front-parts.jpg](../../../../_images/rak5010-front-parts.jpg)
](../../../../_images/rak5010-front-parts.jpg)

RAK5010

Name:
:   `rak5010`

Vendor:
:   RAKwireless Technology Limited

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/rakwireless/rak5010/doc/index.rst/../..)

## Overview

WisTrio NB-IoT Tracker Pro (RAK5010) is a tracker
with integrated LTE CAT M1 & NB1, GPS, BLE, and sensors.
It is built on the Quectel BG96 LTE CAT M1 & NB1 module,
which has an integrated GPS receiver. The MCU running
the board is a Nordic nRF52840 controller.

As it has both GPS and BLE it can be used for outdoor
and indoor scenarios, where location-based services need be present.

The built-in sensors for RAK5010 are temperature and
humidity sensor, motion sensor, pressure sensor, and light sensor.
The extension IOs allow adding more sensors in addition to the on-board ones.

This board is particularly suitable to be used as a
quick testing and prototyping tool for applications
requiring NB-IoT connectivity. Application development
supports the GCC environment.

## Hardware

- nRF52840 ARM Cortex-M4F Processor
- 32.768 kHz crystal oscillator
- 1 Micro-AB USB OTG host/device
- Quectel BG96, with LTE CAT M1, LTE NB1, and GNSS
- iPEX connectors for the LTE and GPS antenna and an on-board ceramic antenna for the BLE.
- nano-SIM and ESIM options.
- Multiple interfaces, I2C, UART, GPIO, ADC
- 1 user LED
- 1 SHTC3 Humidity and Temperature Sensor
- 1 OPT3001DNPR Ambient Light Sensor
- 1 LPS22HB Pressure Sensor
- 1 LIS3DH Motion Sensor
- Powered by either Micro USB, 3.7V rechargeable battery or a 5V Solar Panel Port

### Supported Features

The `rak5010` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### LED

- LED0 (green) = P0.12

## Programming and Debugging

The RAK5010 board shall be connected to a Segger Embedded Debugger Unit
[J-Link OB](https://www.segger.com/jlink-ob.html). This provides a debug
interface to the NRF52840 chip. You can use JLink to communicate with
the NRF52840.

### Flashing

1. Download JLink from the Segger [JLink Downloads Page](https://www.segger.com/downloads/jlink) [[1]](#id2). Go to the section
   “J-Link Software and Documentation Pack” and install the “J-Link Software
   and Documentation pack for Linux”. The application JLinkExe needs to be
   accessible from your path.
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyACM0`. For example:

   ```shell
   $ minicom -D /dev/ttyACM0 -o
   ```

   The -o option tells minicom not to send the modem initialization string.
   Connection should be configured as follows:

   - Speed: 115200
   - Data: 8 bits
   - Parity: None
   - Stop bits: 1
3. Connect the RAK5010 board to your host computer using the USB debug port.
   Then build and flash the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

   ```shell
   # From the root of the zephyr repository
   west build -b rak5010/nrf52840 samples/hello_world
   west flash
   ```

   You should see “Hello World! rak5010\_nrf52840” in your terminal.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rak5010/nrf52840 samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.segger.com/downloads/jlink](https://www.segger.com/downloads/jlink)
