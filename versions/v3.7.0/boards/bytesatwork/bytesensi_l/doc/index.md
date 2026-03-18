---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/bytesatwork/bytesensi_l/doc/index.html
original_path: boards/bytesatwork/bytesensi_l/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# bytesatwork byteSENSI-L

## Overview

The byteSENSI-L is a fun LoRa device based on nRF52 MCU that integrates many
sensors.

[![byteSENSI-L](../../../../_images/byteSENSI-L.jpg)](../../../../_images/byteSENSI-L.jpg)

## Hardware

### Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| RADIO | on-chip | Bluetooth |
| RADIO | Semtech | LoRa |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| WDT | on-chip | watchdog |

### Connections and IOs

#### External Connectors

External Supply @ X1

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VBAT | Power input instead of CR2477 battery |
| 2 | GND | Ground |

Programming Connector @ SL1

| PIN # | Signal Name |
| --- | --- |
| 1 | VBAT |
| 2 | SWDIO |
| 3 | GND |
| 4 | SWDCLK |
| 5 | GND |
| 6 | NC (SWO) |
| 7 | NC (Key) |
| 8 | NC |
| 9 | GND |
| 10 | nReset |

I2C Sensor @ X3

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VBAT | Power out |
| 2 | SCL | I2C clock at P0.15 |
| 3 | SDA | I2C data at P0.16 |
| 4 | INT | Interrupt at P0.13 |
| 5 | I2C\_ADDR | tied to VBAT |
| 6 | GND | Ground |

One Wire Sensor @ X2

| PIN # | Signal Name | Function |
| --- | --- | --- |
| 1 | VDD | 4V8 |
| 2 | IO | One Wire |
| 3 | GND | Ground |

External BLE Antenna @ J1

External LoRa Antenna @ J2

External GPS Antenna @ J3

## Programming and Debugging

### Flashing

The byteSENSI-L board can be flashed with the SEGGER JLink programmer.

You can build and flash applications in the usual way. Here is an example for
the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

> ```shell
> west build -b bytesensi_l samples/hello_world
> west flash
> ```

### Debugging

Debugging your application can be done with `west debug`.

### Serial console

The byteSENSI-L board only uses Segger’s RTT console for providing serial
console. There is no physical serial port available.

## References

- [bytesatwork website](https://www.bytesatwork.io/)
- [bytesatwork wiki](https://wiki.bytesatwork.io/)
