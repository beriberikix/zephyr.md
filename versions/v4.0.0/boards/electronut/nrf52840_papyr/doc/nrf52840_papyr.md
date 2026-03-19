---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.html
original_path: boards/electronut/nrf52840_papyr/doc/nrf52840_papyr.html
---

# Labs Papyr

Board Overview

[![../../../../_images/nrf52840_papyr.jpg](../../../../_images/nrf52840_papyr.jpg)
](../../../../_images/nrf52840_papyr.jpg)

Labs Papyr

Vendor:
:   Electronut Labs

Architecture:
:   arm

SoC:
:   nrf52840

## Overview

Zephyr applications use the nrf52840\_papyr board configuration
to run on Electronut Labs Papyr hardware. It provides
support for the Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU and
the following devices:

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
- SPI
- UART
- USB
- WDT
- COUNTER

More information about the board is available at [https://gitlab.com/electronutlabs-public/papyr](https://gitlab.com/electronutlabs-public/papyr).

## Hardware

Papyr has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 32 MHz.

### Supported Features

The nrf52840\_papyr board configuration supports the following
hardware features currently:

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
| SPI(M/S) | on-chip | spi |
| UART | on-chip | serial |
| USB | on-chip | usb |
| WDT | on-chip | watchdog |

### Connections and IOs

#### LED

- LED1 (green) = P0.13
- LED2 (blue) = P0.15
- LED3 (red) = P0.14

#### Push buttons

- Reset = SW0 = P0.18 (can be used as GPIO also)

#### UART

- TX = P0.8
- RX = P0.7

#### I2C

I2C pins connected to onboard sensors (I2C\_0):

- SDA = P0.5
- SCL = P0.6

#### SPI

The e-paper display is connected to the chip via SPI on the following pins (SPI\_1):

- SCK = P0.31
- MOSI = P0.29
- MISO = P1.1 (not used by the display)

NOTE: P1.1 is pin 33 in absolute enumeration.

Other pins used by the e-paper display are:

- E-ink enable = P0.11 (cuts off power to the display with MOSFET)
- CS = P0.30
- BUSY = P0.3
- D/C = P0.28
- RES = P0.2

## Programming and Debugging

Applications for the `nrf52840_papyr` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details); Black Magic
Probe debugger presents itself as two USB-serial ports. On Linux,
they may come up as `/dev/ttyACM0` and `/dev/ttyACM1`. The first
one of these (`/dev/ttyACM0` here) is the debugger port.
GDB can directly connect to this port without requiring a GDB server by specifying
`target external /dev/ttyACM0`. The second port acts as a
serial port, connected to the SoC.

### Flashing

By default, papyr is configured to be used with a blackmagicprobe compatible
debugger (see \_Bumpy).

Applications are flashed and run as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the serial port of Black Magic Probe.
For example, under Linux, `/dev/ttyACM1`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b nrf52840_papyr samples/hello_world
west flash
```

### Debugging

Debug and attach configurations are available using Black Magic Probe, and
`ninja debug`, or `ninja attach` (or with `make`) are available.

NOTE: You may need to press the reset button once after using `ninja flash`
to start executing the code. (not required with `debug` or `attach`)

## References
