---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ruiside/ra8d1_vision_board/doc/index.html
original_path: boards/ruiside/ra8d1_vision_board/doc/index.html
---

# RA8D1 Vision Board

Board Overview

[![../../../../_images/ra8d1_vision_board.webp](../../../../_images/ra8d1_vision_board.webp)
](../../../../_images/ra8d1_vision_board.webp)

RA8D1 Vision Board

Name:
:   `ra8d1_vision_board`

Vendor:
:   Shanghai Ruiside Electronic Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   r7fa8d1bhecbd

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruiside/ra8d1_vision_board/doc/index.rst/../..)

## Overview

The RA8D1-VISION-BOARD, based on the Renesas Cortex-M85 architecture RA8D1 chip, offers
engineers a flexible and comprehensive development platform, empowering them to explore the realm of
machine vision more deeply.

Key Features

- Arm Cortex-M85
- 480MHz frequency, on-chip 2Mb Flash, 1Mb SRAM
- 32Mb-SDRAM; 8Mb-QSPI Flash
- MIPI-DSI; RGB666; 8bit Camera
- On-board DAP-LINK debugger with CMSIS-DAP
- Raspberry Pi Interface

More information about the board can be found at the [RA8D1-VISION-BOARD website](https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board) [[1]](#id2).

## Hardware

Detailed Hardware features for the RA8D1 MCU group can be found at [RA8D1 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/ra8d1-group-users-manual-hardware) [[2]](#id4)

### Supported Features

The `ra8d1_vision_board` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### Default Zephyr Peripheral Mapping:

The RA8D1-VISION-BOARD board features a On-board CMSIS-DAP debugger/programmer. Board is configured as follows:

- UART9 TX/RX : P209/P208 (CMSIS-DAP Virtual Port Com)
- LED0 : P102
- LED1 : P106
- LED2 : PA07
- USER BUTTON : P907

## Programming and Debugging

The `ra8d1_vision_board` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

Applications for the `ra8d1_vision_board` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

**Note:** Only support from SDK v0.16.6 in which GCC for Cortex Arm-M85 was available.
To build for RA8D1-VISION-BOARD user need to get and install GNU Arm Embedded toolchain from [https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6)

### Flashing

Program can be flashed to RA8D1-VISION-BOARD via the on-board DAP-LINK debugger.

Linux users: to fix the permission issue, simply add the following udev rule for the
CMSIS-DAP interface:

```shell
$ echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="0416", ATTR{idProduct}=="7687", MODE:="666"' > /etc/udev/rules.d/50-cmsis-dap.rules
```

To flash the program to board

1. Connect to DAP-LINK via USB port to host PC
2. Execute west command

   > ```shell
   > west flash
   > ```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b ra8d1_vision_board samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board](https://github.com/RT-Thread-Studio/sdk-bsp-ra8d1-vision-board)

[[2](#id5)]

[https://www.renesas.com/us/en/document/mah/ra8d1-group-users-manual-hardware](https://www.renesas.com/us/en/document/mah/ra8d1-group-users-manual-hardware)
