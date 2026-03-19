---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32f470i_eval/doc/index.html
original_path: boards/gd/gd32f470i_eval/doc/index.html
---

# GD32F470I-EVAL

Board Overview

[![../../../../_images/gd32f470i_eval.jpg](../../../../_images/gd32f470i_eval.jpg)
](../../../../_images/gd32f470i_eval.jpg)

GD32F470I-EVAL

Name:
:   `gd32f470i_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f470

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f470i_eval/doc/index.rst/../..)

## Overview

The GD32F470I-EVAL board is a hardware platform that enables prototyping
on GD32F470IK Cortex-M4F Stretch Performance MCU.

The GD32F470IK features a single-core ARM Cortex-M4F MCU which can run up
to 240 MHz with flash accesses zero wait states, 3072kiB of Flash, 256kiB of
SRAM and 140 GPIOs.

## Hardware

- GD32F470IKH6 MCU
- 2Kb EEPROM
- 16Mbit SPI and QSPI NOR Flash
- 256Mbit SDRAM
- 3 x User LEDs
- 3 x User Push buttons
- 1 x USART (RS-232 at J1 connector)
- 1 x POT connected to an ADC input
- Headphone interface
- Micro SD Card Interface
- USB FS connector
- USB HS connector
- 1 x CAN
- Ethernet Interface
- 4.3” LCD (480x272)
- OV2640 Digital Camera
- GD-Link on board programmer
- J-Link/JTAG connector

For more information about the GD32F470 SoC and GD32F470I-EVAL board:

- [GigaDevice Cortex-M4F Stretch Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/gd32f470-series/)
- [GD32F470IKH6 Specifications](https://www.gigadevice.com/microcontroller/gd32f470ikh6/)
- [GD32F470xx Datasheet](https://gd32mcu.com/data/documents/datasheet/GD32F470xx_Datasheet_Rev1.3.pdf)
- [GD32F4xx User Manual](https://gd32mcu.com/data/documents/userManual/GD32F4xx_User_Manual_Rev2.7.pdf)

### Supported Features

The `gd32f470i_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The GD32F470I-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

Before programming your board make sure to configure boot and serial jumpers
as follows:

- J2/3: Select 2-3 for both (boot from user memory)
- J5: Select 1-2 position (labeled as `USART0`)

### Using GD-Link

The GD32F470I-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a JTAG header
(J1) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. On Linux the
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
3. To flash an image:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32f470i\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32f470i_eval samples/hello_world
   west debug
   ```
