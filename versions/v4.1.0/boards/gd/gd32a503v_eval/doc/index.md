---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/gd/gd32a503v_eval/doc/index.html
original_path: boards/gd/gd32a503v_eval/doc/index.html
---

# GD32A503V-EVAL

Board Overview

[![../../../../_images/gd32a503v_eval.jpg](../../../../_images/gd32a503v_eval.jpg)
](../../../../_images/gd32a503v_eval.jpg)

GD32A503V-EVAL

Name:
:   `gd32a503v_eval`

Vendor:
:   GigaDevice Semiconductor

Architecture:
:   arm

SoC:
:   gd32a503

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/gd/gd32a503v_eval/doc/index.rst/../..)

## Overview

The GD32A503V-EVAL board is a hardware platform that enables design and debug
of the GigaDevice A503 Cortex-M4F High Performance MCU.

The GD32A503VD features a single-core ARM Cortex-M4F MCU which can run up
to 120-MHz with flash accesses zero wait states, 384kiB of Flash, 48kiB of
SRAM and 88 GPIOs.

## Hardware

- 2 user LEDs
- 2 user push buttons
- Reset Button
- ADC connected to a potentiometer
- 1 DAC channels
- GD25Q16 2Mib SPI Flash
- AT24C02C 2KiB EEPROM
- CS4344 Stereo DAC with Headphone Amplifier
- GD-Link interface

  - CMSIS-DAP swd debug interface over USB HID.
- 2 CAN FD ports

For more information about the GD32A503 SoC and GD32A503V-EVAL board:

- [GigaDevice Cortex-M33 High Performance SoC Website](https://www.gigadevice.com.cn/product/mcu/arm-cortex-m33/gd32a503vdt3)
- [GD32A503 Datasheet](https://www.gd32mcu.com/download/down/document_id/401/path_type/1)
- [GD32A503 Reference Manual](https://www.gd32mcu.com/download/down/document_id/402/path_type/1)
- [GD32A503V Eval Schematics](https://www.gd32mcu.com/download/down/document_id/404/path_type/1)
- [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

### Supported Features

The `gd32a503v_eval` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Serial Port

The GD32A503V-EVAL board has 3 serial communication ports. The default port
is UART0 at PIN-72 and PIN-73.

## Programming and Debugging

Before program your board make sure to configure boot setting and serial port.
The default serial port is USART0.

| Boot-0 | Boot-1 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | SRAM |
| 1-2 | 2-3 | Bootloader |
| 2-3 | Any | Flash |

### Using GD-Link

The GD32A503V-EVAL includes an onboard programmer/debugger (GD-Link) which
allow flash programming and debug over USB. There are also program and debug
headers J2 and J100 that can be used with any ARM compatible tools.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   ```
2. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1
3. To flash an image:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32a503v\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   west debug
   ```

### Using ROM bootloader

The GD32A503 MCU have a ROM bootloader which allow flash programming. User
should install [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1) software at some Linux path. The recommended
is `$HOME/.local/bin`.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application:

   ```shell
   west build -b gd32a503v_eval samples/hello_world
   ```
2. Enable board bootloader:

   - Remove boot-0 jumper
   - press reset button
3. To flash an image:

   ```shell
   west flash -r gd32isp [--port=/dev/ttyUSB0]
   ```
4. Run your favorite terminal program to listen for output. Under Linux the
   terminal should be `/dev/ttyUSB0`. For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -o
   ```

   The -o option tells minicom not to send the modem initialization
   string. Connection should be configured as follows:

   > - Speed: 115200
   > - Data: 8 bits
   > - Parity: None
   > - Stop bits: 1

   Press reset button

   You should see “Hello World! gd32a503v\_eval” in your terminal.
