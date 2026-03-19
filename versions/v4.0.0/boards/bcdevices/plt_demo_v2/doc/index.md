---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/bcdevices/plt_demo_v2/doc/index.html
original_path: boards/bcdevices/plt_demo_v2/doc/index.html
---

# Blue Clover PLT Demo V2 nRF52832

Board Overview

[![../../../../_images/blueclover_plt_demo_v2.jpg](../../../../_images/blueclover_plt_demo_v2.jpg)
](../../../../_images/blueclover_plt_demo_v2.jpg)

Blue Clover PLT Demo V2 nRF52832

Vendor:
:   Blue Clover Devices

Architecture:
:   arm

SoC:
:   nrf52832

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

The Blue Clover PLT Demo V2 board configuration supports the
following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| MPU | on-chip | arch/arm |
| NVIC | on-chip | arch/arm |
| PWM | on-chip | pwm |
| RADIO | on-chip | Bluetooth |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

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
