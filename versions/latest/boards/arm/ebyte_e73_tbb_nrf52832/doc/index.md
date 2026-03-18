---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/ebyte_e73_tbb_nrf52832/doc/index.html
original_path: boards/arm/ebyte_e73_tbb_nrf52832/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# EBYTE E73-TBB

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

![EBYTE E73-TBB](../../../../_images/ebyte_e73_tbb_nrf52832.jpg)

EBYTE E73-TBB (Credit: EBYTE)

More information about the board can be found at the
[E73-TBB website](https://www.ebyte.com/en/product-view-news.html?id=889) [[1]](#id2). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

E73-TBB has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz. Additionally the board features CH340 USB-UART converter.
It is possible to connect external BT antenna using U.FL socket
and solder NFC antenna using NFC\_ANT connector.

### Supported Features

The ebyte\_e73\_tbb\_nrf52832 board configuration supports the following
hardware features:

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

Other hardware features are not supported by the Zephyr kernel.
See [E73-TBB website](https://www.ebyte.com/en/product-view-news.html?id=889) [[1]](#id2) and [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
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
west build -b ebyte_e73_tbb_nrf52832 samples/basic/blinky
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
[boards/arm/ebyte\_e73\_tbb\_nrf52832/ebyte\_e73\_tbb\_nrf52832.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/ebyte_e73_tbb_nrf52832/ebyte_e73_tbb_nrf52832.dts).

## References

[1]
([1](#id3),[2](#id4))

[https://www.ebyte.com/en/product-view-news.html?id=889](https://www.ebyte.com/en/product-view-news.html?id=889)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)
