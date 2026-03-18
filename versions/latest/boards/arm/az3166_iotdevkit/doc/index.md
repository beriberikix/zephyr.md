---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/az3166_iotdevkit/doc/index.html
original_path: boards/arm/az3166_iotdevkit/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# AZ3166 MXChip IoT DevKit

## Overview

The AZ3166 IoT DevKit from MXChip is a development board designed for IoT (Internet of Things)
projects. It’s an all-in-one board powered by an Arm Cortex-M4 processor. On-board peripherals
include an OLED screen, headphone output, stereo microphone and abundant sensors like humidity &
temperature, pressure, motion (accelerometer & gyroscope) and magnetometer.

![AZ3166 MXChip IoT DevKit](../../../../_images/az3166-iotdevkit.webp)

AZ3166 MXChip IoT DevKit (Credit: MXChip)

More information about the board can be found at the [MXChip AZ3166 website](https://www.mxchip.com/en/az3166) [[1]](#id2).

## Hardware

The MXChip AZ3166 IoT DevKit has the following physical features:

- STM32F412 Arm Cortex M4F processor at 96 MHz
- Working voltage: 3.3v or USB power supply
- Supports 3.3V DC-DC, maximum current 1.5A
- OLED display, 128x64 pixels
- 2 programmable buttons
- 1 RGB LED
- 3 LED for status indicators (“Wi-Fi”, “Azure”, “User”)
- Security encryption chip
- Infrared emitter for IR remote control or interaction
- Motion sensor (LSM6DSL)
- Magnetometer sensor (LIS3MDL)
- Atmospheric pressure sensor (LPS22HB)
- Temperature and humidity sensor (HTS221)
- EMW3166 Wi-Fi module with 256K SRAM，1M+2M Byte SPI Flash

### Supported Features

The az3166\_iotdevkit board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |

Note

The EMW3166 Wi-Fi module is currently not supported.

## Programming and Debugging

### Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the micro:bit board
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b az3166_iotdevkit samples/hello_world
west flash
```

## References

[[1](#id3)]

[https://www.mxchip.com/en/az3166](https://www.mxchip.com/en/az3166)
