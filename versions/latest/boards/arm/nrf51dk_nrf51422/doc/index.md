---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nrf51dk_nrf51422/doc/index.html
original_path: boards/arm/nrf51dk_nrf51422/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# nRF51 DK

## Overview

The nRF51 Development Kit (PCA10028) hardware provides support for the Nordic
Semiconductor nRF51422 ARM Cortex-M0 CPU and the following devices:

- ADC
- CLOCK
- FLASH
- GPIO
- I2C
- NVIC
- RADIO (Bluetooth Low Energy)
- RTC
- Segger RTT (RTT Console)
- SPI
- UART
- WDT

![nRF51 DK](../../../../_images/nrf51dk_nrf51422.jpg)

nRF51 DK (Credit: Nordic Semiconductor)

More information about the board can be found at the
[nRF51 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF51-DK) [[1]](#id2). The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

nRF51 DK has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 16 MHz.

### Supported Features

The nrf51dk\_nrf51422 board configuration supports the following nRF51
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| ADC | on-chip | adc |
| CLOCK | on-chip | clock\_control |
| FLASH | on-chip | flash |
| GPIO | on-chip | gpio |
| I2C(M) | on-chip | i2c |
| NVIC | on-chip | arch/arm |
| RADIO | on-chip | Bluetooth |
| RTC | on-chip | system clock |
| RTT | Segger | console |
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| WDT | on-chip | watchdog |

Other hardware features have not been enabled yet for this board.
See [nRF51 DK website](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF51-DK) [[1]](#id2) and [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5)
for a complete list of nRF51 Development Kit board hardware features.

### Connections and IOs

#### LED

- LED1 (green) = P0.21
- LED2 (green) = P0.22
- LED3 (green) = P0.23
- LED4 (green) = P0.24

#### Push buttons

- BUTTON1 = SW1 = P0.17
- BUTTON2 = SW2 = P0.18
- BUTTON3 = SW3 = P0.19
- BUTTON4 = SW4 = P0.20
- BOOT = SW5 = boot/reset

## Programming and Debugging

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

Replace `<tty_device>` with the port where the board nRF51 DK
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf51dk_nrf51422 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs and buttons in the nRF51 DK

There are 2 samples that allow you to test that the buttons (switches) and LEDs on
the board are working properly with Zephyr:

```shell
samples/basic/blinky
samples/basic/button
```

You can build and flash the examples to make sure Zephyr is running correctly on
your board. The button and LED definitions can be found in
[boards/arm/nrf51dk\_nrf51422/nrf51dk\_nrf51422.dts](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arm/nrf51dk_nrf51422/nrf51dk_nrf51422.dts).

## References

[1]
([1](#id3),[2](#id4))

[https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF51-DK](https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF51-DK)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)
