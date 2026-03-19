---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ebyte/e73_tbb/doc/index.html
original_path: boards/ebyte/e73_tbb/doc/index.html
---

# E73-TBB

Board Overview

[![../../../../_images/ebyte_e73_tbb_nrf52832.jpg](../../../../_images/ebyte_e73_tbb_nrf52832.jpg)
](../../../../_images/ebyte_e73_tbb_nrf52832.jpg)

E73-TBB

Name:
:   `ebyte_e73_tbb`

Vendor:
:   Chengdu Ebyte Electronic Technology

Architecture:
:   arm

SoC:
:   nrf52832

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ebyte/e73_tbb/doc/index.rst/../..)

## Overview

The EBYTE E73-TBB hardware provides
support for the Nordic Semiconductor nRF52832 ARM Cortex-M4F CPU and
the following devices:

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

More information about the board can be found at the
[E73-TBB website](https://www.cdebyte.com/products/E73-TBB) [[1]](#id2). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

E73-TBB has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz. Additionally the board features CH340 USB-UART converter.
It is possible to connect external BT antenna using U.FL socket
and solder NFC antenna using NFC\_ANT connector.

### Supported Features

The `ebyte_e73_tbb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

See [E73-TBB website](https://www.cdebyte.com/products/E73-TBB) [[1]](#id2) and [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
for a complete list of nRF52832 hardware features.

### Connections and IOs

#### LED

- LED0 (red) = P0.17
- LED1 (red) = P0.18

#### Push buttons

- BUTTON0 = SW1 = P0.14
- BUTTON1 = SW2 = P0.13

#### External Connectors

P1 Header

| PIN # | Signal Name |
| --- | --- |
| 1 | GND |
| 2 | 3.3V |
| 3 | P0.04 |
| 4 | P0.03 |
| 5 | P0.02 |
| 6 | P0.31 |
| 7 | P0.30 |
| 8 | P0.29 |
| 9 | P0.28 |
| 10 | P0.27 |
| 11 | P0.26 |
| 12 | P0.25 |

P2 Header

| PIN # | Signal Name |
| --- | --- |
| 1 | P0.24 |
| 2 | P0.23 |
| 3 | P0.22 |
| 4 | SWDIO |
| 5 | SWDCLK |
| 6 | P0.21/RST |
| 7 | P0.20 |
| 8 | P0.19 |
| 9 | P0.16 |
| 10 | P0.15 |
| 11 | P0.12 |
| 12 | P0.11 |

NFC\_ANT

| PIN # | Signal Name |
| --- | --- |
| 1 | P0.10 |
| 2 | P0.09 |

## Programming and Debugging

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software.
To flash the board connect pins: SWDIO, SWDCLK, RST, GND from E73-TBB
to corresponding pins on your J-Link device, then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b ebyte_e73_tbb/nrf52832 samples/basic/blinky
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic chips with a
Segger IC.

## Testing the LEDs and buttons in the E73-TBB

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```shell
:zephyr:code-sample:`blinky`
:zephyr:code-sample:`button`
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/ebyte/e73\_tbb/ebyte\_e73\_tbb\_nrf52832.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ebyte/e73_tbb/ebyte_e73_tbb_nrf52832.dts).

## References

[1]
([1](#id3),[2](#id4))

[https://www.cdebyte.com/products/E73-TBB](https://www.cdebyte.com/products/E73-TBB)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)
