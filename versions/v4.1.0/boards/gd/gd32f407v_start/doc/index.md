---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32f407v_start/doc/index.html
original_path: boards/gd/gd32f407v_start/doc/index.html
---

# GD32F407V-START

Board Overview

[![../../../../_images/gd32f407v_start.webp](../../../../_images/gd32f407v_start.webp)
](../../../../_images/gd32f407v_start.webp)

GD32F407V-START

Name:
:   `gd32f407v_start`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f407

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f407v_start/doc/index.rst/../..)

## Overview

The GD32F407V-START board is a hardware platform that enables prototyping
on GD32F407VE Cortex-M4 High Performance MCU.

The GD32F407VE features a single-core ARM Cortex-M4 MCU which can run up
to 168 MHz with flash accesses zero wait states, 3072kiB of Flash, 192kiB of
SRAM and 82 GPIOs.

## Hardware

- GD32F407VET6 MCU
- 1 x User LEDs
- 1 x User Push buttons
- 1 x USART
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32F407 SoC and GD32F407V-START board:

- [GigaDevice Cortex-M4 High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/high-performance-line/)
- [GD32F407X Datasheet](https://gd32mcu.com/data/documents/datasheet/GD32F407xx_Datasheet_Rev2.5.pdf)
- [GD32F40X User Manual](https://gd32mcu.com/data/documents/userManual/GD32F4xx_User_Manual_Rev2.7.pdf)
- [GD32F407V-START User Manual](https://www.gd32mcu.com/data/documents/evaluationBoard/GD32F4xx_Demo_Suites_V2.6.1.rar)

### Supported Features

The `gd32f407v_start` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The GD32F407V-START board has one serial communication port. The default port
is USART0 with TX connected at PB6 and RX at PB7.

## Programming and Debugging

Before programming your board make sure to configure boot jumpers as
follows:

- JP3/4: Select 2-3 for both (boot from user memory)

### Using GD-Link or J-Link

The board comes with an embedded GD-Link programmer.
You need to install CMSIS-Pack which is required by pyOCD
when programming or debugging by the GD-Link programmer.
Execute the following command to install CMSIS-Pack for GD32F407VK
if not installed yet.

> ```shell
> pyocd pack install gd32f407vk
> ```

Also, J-Link can be used to program the board via the SWD interface
(PA13/SWDIO and PA14/SWCLK in the JP6 header).

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   ```
2. Connect Serial-USB adapter to PB6, PB7, and GND.
3. Run your favorite terminal program to listen for output. On Linux the
   terminal should be something like `/dev/ttyUSB0`. For example:

   ```shell
   minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
4. To flash an image:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   west flash
   ```

   When using J-Link, append `--runner jlink` option after `west flash`.

   You should see “Hello World! gd32f407v\_start” in your terminal.
5. To debug an image:

   ```shell
   west build -b gd32f407v_start samples/hello_world
   west debug
   ```

   When using J-Link, append `--runner jlink` option after `west debug`.
