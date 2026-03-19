---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/bbc/microbit_v2/doc/index.html
original_path: boards/bbc/microbit_v2/doc/index.html
---

# micro:bit V2

Board Overview

[![../../../../_images/bbc_microbit2.jpg](../../../../_images/bbc_microbit2.jpg)
](../../../../_images/bbc_microbit2.jpg)

micro:bit V2

Vendor:
:   BBC

Architecture:
:   arm

SoC:
:   nrf52833

## Overview

The Micro Bit (also referred to as BBC Micro Bit, stylized as micro:bit) is an
ARM-based embedded system designed by the BBC for use in computer education in
the UK.

The board is 4 cm × 5 cm and has an ARM Cortex-M4F processor, accelerometer and
magnetometer sensors, Bluetooth and USB connectivity, a display consisting of
25 LEDs, a microphone, two programmable buttons, and can be powered by either
USB or an external battery pack. The device inputs and outputs are through five
ring connectors that are part of the 23-pin edge connector.

More information about the board can be found at the [microbit website](http://www.microbit.org/) [[1]](#id2).

## Hardware

The micro:bit-v2 has the following physical features:

- 25 individually-programmable LEDs
- 2 programmable buttons
- Microphone sensors
- Physical connection pins
- Light and temperature sensors
- Motion sensors (accelerometer and compass)
- Wireless Communication, via Radio and Bluetooth 5
- USB interface

### Supported Features

The bbc\_microbit\_v2 board configuration supports the following
hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| RTC | on-chip | system clock |
| UART | on-chip | serial port |
| GPIO | on-chip | gpio |
| FLASH | on-chip | flash |
| RADIO | on-chip | Bluetooth |

## Programming and Debugging

### Flashing

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

First, run your favorite terminal program to listen for output.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the micro:bit board
can be found. For example, under Linux, `/dev/ttyACM0`.

Then build and flash the application in the usual way.

```shell
# From the root of the zephyr repository
west build -b bbc_microbit_v2 samples/hello_world
west flash
```

## References

[[1](#id3)]

[http://www.microbit.org/](http://www.microbit.org/)
