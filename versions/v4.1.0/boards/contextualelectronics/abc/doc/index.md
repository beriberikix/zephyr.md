---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/contextualelectronics/abc/doc/index.html
original_path: boards/contextualelectronics/abc/doc/index.html
---

# Advanced BLE Cell

Board Overview

[![../../../../_images/contextualelectronics_abc.jpg](../../../../_images/contextualelectronics_abc.jpg)
](../../../../_images/contextualelectronics_abc.jpg)

Advanced BLE Cell

Name:
:   `contextualelectronics_abc`

Vendor:
:   Contextual Electronics

Architecture:
:   arm

SoC:
:   nrf52840

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/contextualelectronics/abc/doc/index.rst/../..)

## Overview

The Contextual Electronics ABC (PCA10056) hardware provides support for the
Nordic Semiconductor nRF52840 ARM Cortex-M4F CPU and the following devices:

- CLOCK
- FLASH
- GPIO
- I2C
- MPU
- NVIC
- PWM
- Segger RTT (RTT Console)
- SPI
- UART
- Quectel BG95 Modem

More information about the board can be found at the [ABC Board website](https://contextualelectronics.com/courses/advanced-ble-cell-abc-board/) [[1]](#id2).
The [Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5) contains the processor’s information
and the datasheet.

## Hardware

ABC board has two external oscillators. The frequency of the slow clock
is 32.768 kHz. The frequency of the main clock is 32 MHz.

- nRF52840 ARM Cortex-M4F processor at 64 MHz
- 1 MB flash memory and 256 KB of SRAM
- SWD connector

### Supported Features

The `contextualelectronics_abc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

See [ABC Board website](https://contextualelectronics.com/courses/advanced-ble-cell-abc-board/) [[1]](#id2) for more details on this board, and
[Nordic Semiconductor Infocenter](https://infocenter.nordicsemi.com) [[2]](#id5) for a complete list of SoC
features.

## Programming and Debugging

Applications for the `contextualelectronics_abc` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Flashing Zephyr onto the `contextualelectronics_abc` board requires
an external programmer. The programmer is attached to the SWD header.

Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

> ```shell
> west build -b contextualelectronics_abc samples/hello_world
> ```

Flash the image.

> ```shell
> west build -b contextualelectronics_abc samples/hello_world
> west flash
> ```

To see the output, run your favorite terminal program.

```shell
$ minicom -D <tty_device> -b 115200
```

Replace `<tty_device>` with the port where the ABC board
can be found. For example, under Linux, `/dev/ttyACM0`.

### Debugging

Refer to the [Nordic nRF5x Segger J-Link](../../../../develop/flash_debug/nordic_segger.md#nordic-segger) page to learn about debugging Nordic boards with a
Segger IC.

### Selecting the pins

Pins can be configured in the board pinctrl file. To see the available mappings,
open the [nRF52840 Product Specification](http://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.0.pdf) [[3]](#id8), chapter 7 ‘Hardware and Layout’.
In the table 7.1.1 ‘aQFN73 ball assignments’ select the pins marked
‘General purpose I/O’. Note that pins marked as ‘low frequency I/O only’ can only be used
in under-10KHz applications. They are not suitable for 115200 speed of UART.

## References

[1]
([1](#id3),[2](#id4))

[https://contextualelectronics.com/courses/advanced-ble-cell-abc-board/](https://contextualelectronics.com/courses/advanced-ble-cell-abc-board/)

[2]
([1](#id6),[2](#id7))

[https://infocenter.nordicsemi.com](https://infocenter.nordicsemi.com)

[[3](#id9)]

[http://infocenter.nordicsemi.com/pdf/nRF52840\_PS\_v1.0.pdf](http://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.0.pdf)
