---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/nordic/nrf51dongle/doc/index.html
original_path: boards/nordic/nrf51dongle/doc/index.html
---

# nRF51 Dongle

## Overview

The nRF51 Dongle (PCA10031) hardware provides support for the Nordic
Semiconductor nRF51822 ARM Cortex-M0 CPU and the following devices:

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

![nRF51 Dongle](../../../../_images/nrf51dongle_nrf51822.jpg)

nRF51 Dongle (Credit: Nordic Semiconductor)

More information about the board can be found at the
[nRF51 Dongle website](http://www.nordicsemi.com/eng/Products/nRF51-Dongle) [[1]](#id2). The [Nordic Semiconductor TechDocs](https://docs.nordicsemi.com/) [[2]](#id5)
contains the processor’s information and the datasheet.

## Hardware

nRF51 Dongle has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 16 MHz.

### Supported Features

The nrf51dongle/nrf51822 board configuration supports the following nRF51
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
See [nRF51 Dongle website](http://www.nordicsemi.com/eng/Products/nRF51-Dongle) [[1]](#id2) and [Nordic Semiconductor TechDocs](https://docs.nordicsemi.com/) [[2]](#id5)
for a complete list of nRF51 Dongle hardware features.

### Connections and IOs

#### LED

- LED1 (red) = P0.21
- LED1 (green) = P0.22
- LED1 (blue) = P0.23

#### Push buttons

- BOOT = SW1 = boot/reset

## Programming and Debugging

### Flashing

Follow the instructions in the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to install
and configure all the necessary software. Further information can be
found in [Flashing](../../../../develop/flash_debug/nordic_segger.md#nordic-segger-flashing). Then build and flash
applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the board nRF51 Dongle
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf51dongle/nrf51822 samples/hello_world
west flash
```

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

## Testing the LEDs on the nRF51 Dongle

Build and flash the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample to test that the onboard LED
is working properly with Zephyr.

## References

[1]
([1](#id3),[2](#id4))

[http://www.nordicsemi.com/eng/Products/nRF51-Dongle](http://www.nordicsemi.com/eng/Products/nRF51-Dongle)

[2]
([1](#id6),[2](#id7))

[https://docs.nordicsemi.com/](https://docs.nordicsemi.com/)
