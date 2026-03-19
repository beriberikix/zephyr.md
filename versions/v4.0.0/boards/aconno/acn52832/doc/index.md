---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/aconno/acn52832/doc/index.html
original_path: boards/aconno/acn52832/doc/index.html
---

# acn52832

Board Overview

Vendor:
:   aconno GmbH

Architecture:
:   arm

SoC:
:   nrf52832

## Overview

The acn52832 is a module in a small form factor which features the Nordic Semiconductor
nRF52832 ARM Cortex-M4F CPU and the following devices:

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
- SPI
- UART
- WDT

See [Nordic infocenter](https://infocenter.nordicsemi.com/) [[1]](#id1) for more information about the SoC.

## Hardware

Additionally to the SoC the board provides an on-board antenna with a RF matching circuit,
two external oscillators with 32 MHz and 32.768 kHz, load capacitors, a tag-connector
and a RGB-LED.

### Connections

#### Pinout

| PIN # | Tag-Connect | NRF52832 Functions | Configuration |
| --- | --- | --- | --- |
| 1 | 5 | GND |  |
| 2 |  | P0.25 |  |
| 3 |  | P0.26 |  |
| 4 |  | P0.27 |  |
| 5 |  | P0.28/AIN4 |  |
| 6 |  | P0.29/AIN5 |  |
| 7 |  | P0.30/AIN6 |  |
| 8 |  | P0.31 |  |
| 9 |  | P0.02/AIN0 |  |
| 10 |  | P0.03/AIN1 |  |
| 11 |  | P0.04/AIN2 |  |
| 12 | 5 | GND |  |
| 13 | 5 | GND |  |
| 14 |  | P0.05/AIN3 |  |
| 15 |  | P0.06 | UART\_RX |
| 16 |  | P0.07 | UART\_TX |
| 17 |  | P0.08 |  |
| 18 |  | NFC1/P0.09 |  |
| 19 |  | NFC2/P0.10 |  |
| 20 |  | P0.11 |  |
| 21 |  | P0.12 |  |
| 22 |  | P0.14/TRACEDATA[3] |  |
| 23 | 1 | VCC |  |
| 24 | 1 | VCC |  |
| 25 |  | P0.15/TRACEDATA[2] |  |
| 26 |  | P0.16/TRACEDATA[1] |  |
| 27 |  | P0.17 |  |
| 28 | 6 | P0.18/TRACEDATA[0] |  |
| 29 |  | P0.19 |  |
| 30 |  | P0.20/TRACECLK |  |
| 31 | 3 | P0.21/RESET |  |
| 32 | 1 | VCC |  |
| 33 | 2 | SWDIO |  |
| 34 | 4 | SWDCLK |  |
| 35 | 5 | GND |  |

#### RGB-LED

| LED | Color | NRF52832 Pin |
| --- | --- | --- |
| led0 | red | P0.22 |
| led1 | green | P0.24 |
| led2 | blue | P0.23 |

## References

[[1](#id2)]

[https://infocenter.nordicsemi.com/](https://infocenter.nordicsemi.com/)
