---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/croxel/croxel_cx1825/doc/index.html
original_path: boards/croxel/croxel_cx1825/doc/index.html
---

# CX1825 nRF52840

Board Overview

[![../../../../_images/cx1825_nrf52840.jpg](../../../../_images/cx1825_nrf52840.jpg)
](../../../../_images/cx1825_nrf52840.jpg)

CX1825 nRF52840

Name:
:   `croxel_cx1825`

Vendor:
:   Croxel, Inc.

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/croxel/croxel_cx1825/doc/index.rst/../..)

## Overview

Croxel’s [CX1825 Bluetooth Prototyping board](https://croxel.com/ble) [[1]](#id2) provides support for the Nordic
Semiconductor nRF52840 ARM Cortex-M4F CPU and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy and 802.15.4)
- RTC
- Segger RTT (RTT Console)
- SPI
- USB
- WDT

## Hardware

- Ezurio’s BL654 (nRF52840 ARM Cortex-M4F processor at 64MHz)
- 1 MB flash memory and 256 KB of SRAM
- Coin-cell retainer for Lithium coincell batteries
- 2 Discrete LEDs (Red and Green)
- User Button
- Reset Button
- Accelerometer (LIS3DH)
- Ambient & RGB Light and Proximity Sensor (APDS9960)
- Temperature and Humidity Sensor (HTS221)
- Barometric Pressure sensor (LPS22H)
- Hall Effect Switch (MLX90248)
- RGB LED with Charge-Pump driver (LP5521)
- Digital Microphone
- Beeper
- QWIIC connector supporting expansion for I2C devices
- USB Connector for data and power
- 16-pin Expansion connector
- SWD Connector

### Supported Features

The `croxel_cx1825` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Future Feature Support

- RGB LED (Charge-Pump driver not implemented)
- Microphone

### Connections and IOs

Croxel’s CX1825 Bluetooth Prototyping board has detailed information
about the board ([schematic](https://croxeldata.s3.amazonaws.com/cx1825/CX1825-01_SCH_200424A.PDF) [[2]](#id4))

#### LEDs

- LED1 (red) = P0.8
- LED2 (green) = P0.12

#### Digital Inputs

- User Button = P1.16
- Reset Button = P0.18
- Hall-Effect Switch = P0.15

## Programming and Debugging

Applications for the `croxel_cx1825/nrf52840` board configuration
can be built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Flashing Zephyr onto the `croxel_cx1825_nrf52840` board requires
an external programmer. The programmer is attached to the SWD header.

Build the Zephyr kernel and the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

> ```shell
> west build -b croxel_cx1825/nrf52840 samples/basic/blinky
> ```

Flash the image.

> ```shell
> west build -b croxel_cx1825/nrf52840 samples/basic/blinky
> west flash
> ```

You should see the red LED blink.

## References

[[1](#id3)]

[https://croxel.com/ble](https://croxel.com/ble)

[[2](#id5)]

[https://croxeldata.s3.amazonaws.com/cx1825/CX1825-01\_SCH\_200424A.PDF](https://croxeldata.s3.amazonaws.com/cx1825/CX1825-01_SCH_200424A.PDF)
