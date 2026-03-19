---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/bcdevices/plt_demo_v2/doc/index.html
original_path: boards/bcdevices/plt_demo_v2/doc/index.html
---

# Blue Clover PLT Demo V2 nRF52832

Board Overview

[![../../../../_images/blueclover_plt_demo_v2.jpg](../../../../_images/blueclover_plt_demo_v2.jpg)
](../../../../_images/blueclover_plt_demo_v2.jpg)

Blue Clover PLT Demo V2 nRF52832

Name:
:   `blueclover_plt_demo_v2`

Vendor:
:   Blue Clover Devices

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/bcdevices/plt_demo_v2/doc/index.rst/../..)

## Overview

The Blue Clover PLT Demo V2 is an open source (OSWHA certified) hardware
product, featuring the Nordic Semiconductor nRF52832 ARM Cortex-M4F MCU
and several useful external peripherals.

The Nordic Semiconductor nRF52832 ARM Cortex-M4F MCU features the following:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

## Hardware

- nRF52832 ARM Cortex-M4F processor at 64 MHz
- 512 KB flash memory and 64 KB of SRAM
- Bosch BMI270 IMU
- Sensiron SHT30 Humidity and Temperature sensor
- Murata PKLCS1212E4001R1 Piezo Buzzer
- Battery connector and charger for 3.7 V lithium polymer batteries
- 4 APA102C Addressable LEDs
- Reset button (can be configured as user button)
- 1 User button
- Tag-Connect TC2030-FP 6-pin Debug Connector

### Supported Features

The `blueclover_plt_demo_v2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

#### Push buttons

- RESET = P0.21
- STATUS = P0.26

#### UART

- TXD = P0.06
- RXD = P0.08

#### Power

- USB-C Connector
- JST-PH Battery Connector

#### NFC

- U.FL Connector, on NFC1/P0.09, NFC2/P0.10

## Programming and Debugging

Applications for the `blueclover_plt_demo_v2/nrf52832` board configuration
can be built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Flashing Zephyr onto the `blueclover_plt_demo_v2/nrf52832` board requires
an external programmer. The programmer is attached to the SWD header.

Build the Zephyr kernel and the [LED strip](../../../../samples/drivers/led/led_strip/README.md#led-strip "Control an LED strip.") sample application.

> ```shell
> west build -b blueclover_plt_demo_v2/nrf52832 samples/drivers/led/led_strip
> ```

Flash the image.

> ```shell
> west build -b blueclover_plt_demo_v2/nrf52832 samples/drivers/led/led_strip
> west flash
> ```

## References
