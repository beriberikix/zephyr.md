---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/we_proteus3ev_nrf52840/doc/index.html
original_path: boards/arm/we_proteus3ev_nrf52840/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Würth Elektronik Proteus-III-EV

## Overview

The Proteus-III-EV (evaluation board) hardware provides support
for the Proteus-III radio module that uses the Nordic Semiconductor
nRF52840 ARM Cortex-M4F CPU and the following devices:

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
- UART
- WDT

![Proteus-III EV](../../../../_images/we_proteus3ev_nrf52840.jpg)

Proteus-III EV (Credit: Würth Elektronik)

More information about the radio module can be found the Würth Elektronik
web page [https://www.we-online.com/katalog/de/PROTEUS-III](https://www.we-online.com/katalog/de/PROTEUS-III) .

## Hardware

Proteus-III radio module provides only the internal oscillators. The
frequency of the slow clock is 32.768 kHz. The frequency of the main
clock is 32 MHz.

### Supported Features

The we\_proteus3ev\_nrf52840 board configuration supports the following
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
| RADIO | on-chip | Bluetooth, ieee802154 |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features are not supported by the Zephyr kernel.

### Connections and IOs

#### LED

- LED1 = P0.00
- LED2 = P0.01

#### Push buttons

- BUTTON1 = SW1 = P0.03

## Programming and Debugging

Applications for the `we_proteus3ev_nrf52840` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board Proteus-III-EV
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b we_proteus3ev_nrf52840 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic
boards with a Segger IC.

## Testing the LEDs and buttons in the Proteus-III-EV

There are 2 samples that allow you to test that the buttons (switches) and
LEDs on the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running correctly
on your board. The button and LED definitions can be found in
[boards/arm/we\_proteus3ev\_nrf52840/we\_proteus3ev\_nrf52840.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/we_proteus3ev_nrf52840/we_proteus3ev_nrf52840.dts).

## References
