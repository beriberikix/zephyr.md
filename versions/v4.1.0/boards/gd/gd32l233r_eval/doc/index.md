---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32l233r_eval/doc/index.html
original_path: boards/gd/gd32l233r_eval/doc/index.html
---

# GD32L233R-EVA

Board Overview

[![../../../../_images/gd32l233r_eval.jpg](../../../../_images/gd32l233r_eval.jpg)
](../../../../_images/gd32l233r_eval.jpg)

GD32L233R-EVA

Name:
:   `gd32l233r_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32l233

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32l233r_eval/doc/index.rst/../..)

## Overview

The GD32L233R-EVAL board is a hardware platform that enables design and debug
of the GigaDevice GD32L233 Cortex-M23 Low Power MCU.

The GD32RCT6 features a single-core ARM Cortex-M4F MCU which can run up
to 64-MHz with flash accesses zero wait states, 256kB of Flash, 32kB of
SRAM and 59 GPIOs.

## Hardware

- GD32L233RCT6 MCU
- AT24C02C 2Kb EEPROM
- 4 x User LEDs
- 2 x User Push buttons
- 1 x USART (Mini-USB)
- 1 x POT connected to an ADC input
- Headphone interface
- SLCD segment code screen
- GD-Link on board programmer
- J-Link/SWD connector

For more information about the GD32L233 SoC and GD32L233R-EVAL board:

- [GigaDevice Cortex-M23 Low Power SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m23/low-power-line/)
- [GD32L233xx Datasheet](https://gd32mcu.com/download/down/document_id/289/path_type/1)
- [GD32L23x User Manual](https://gd32mcu.com/download/down/document_id/293/path_type/1)
- [GD32L23x Demo Suites](https://gd32mcu.com/download/down/document_id/292/path_type/1)

### Supported Features

The `gd32l233r_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The GD32L233R-EVAL board has one serial communication port. The default port
is USART1 with TX connected at PA2 and RX at PA3. USART1 have connect to a
CH04E serial connector with Mini-USB.

## Programming and Debugging

### Using J-Link

The GD32L233R-EVAL includes an onboard programmer/debugger (GD-Link) which
allows flash programming and debugging over USB. There is also a SWD header
which can be used with tools like Segger J-Link(latest version required).

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32l233r_eval samples/hello_world
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
   west build -b gd32l233r_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32l233r\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32l233r_eval samples/hello_world
   west debug
   ```
