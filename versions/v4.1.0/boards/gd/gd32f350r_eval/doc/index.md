---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32f350r_eval/doc/index.html
original_path: boards/gd/gd32f350r_eval/doc/index.html
---

# GD32F350R-EVAL

Board Overview

[![../../../../_images/gd32f350r_eval.webp](../../../../_images/gd32f350r_eval.webp)
](../../../../_images/gd32f350r_eval.webp)

GD32F350R-EVAL

Name:
:   `gd32f350r_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32f350

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32f350r_eval/doc/index.rst/../..)

## Overview

The GD32F350R-EVAL board is a hardware platform that enables design and debug
of the GigaDevice F350 Cortex-M4F High Performance MCU.

The GD32F350RBT6 features a single-core ARM Cortex-M4F MCU which can run up
to 108-MHz with flash accesses zero wait states, 128kB of Flash, 16kB of
SRAM and 55 GPIOs.

## Hardware

- GD32F350RBT6 MCU
- AT24C02C 2Kb EEPROM
- 4 x User LEDs
- 4 x User Push buttons
- 1 x USART (RS-232 at J2 connector)
- 1 x POT connected to an ADC input
- Headphone interface
- Micro SD Card Interface
- 2.4’’ TFT-LCD (36x48)
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32F350 SoC and GD32F350R-EVAL board:

- [GigaDevice Cortex-M4F Stretch Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/stretch-performance-line/)
- [GD32F350xx Datasheet](http://gd32mcu.com/download/down/document_id/133/path_type/1)
- [GD32F3x0 User Manual](http://gd32mcu.com/download/down/document_id/136/path_type/1)
- [GD32F350R-EVAL User Manual](https://www.tme.com/Document/ff0a3609934053c07d78ef8662781da9/GD32350R-EVAL%20User%20Manual-V1.0.pdf)

### Supported Features

The `gd32f350r_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The GD32F350R-EVAL board has one serial communication port. The default port
is USART0 with TX connected at PA9 and RX at PA10.

## Programming and Debugging

Before programming your board make sure to configure boot and serial jumpers as follows:

- J4: Select 2-3 for both (labeled as `L`)
- J13: Select 1-2 position (labeled as `USART`)

### Using GD-Link

The GD32F350R-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
(J3) which can be used with tools like Segger J-Link.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32f350r_eval samples/hello_world
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
   west build -b gd32f350r_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32f350r\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32f350r_eval samples/hello_world
   west debug
   ```
