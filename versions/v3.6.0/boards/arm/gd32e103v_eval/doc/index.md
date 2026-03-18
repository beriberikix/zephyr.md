---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/gd32e103v_eval/doc/index.html
original_path: boards/arm/gd32e103v_eval/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GigaDevice GD32E103V-EVAL

## Overview

The GD32E103V-EVAL board is a hardware platform that enables design and debug
of the GigaDevice E103 Cortex-M4F High Performance MCU.

The GD32E103VB features a single-core ARM Cortex-M4F MCU which can run up
to 120-MHz with flash accesses zero wait states, 128kiB of Flash, 32kiB of
SRAM and 80 GPIOs.

![gd32e103v_eval](../../../../_images/gd32e103v_eval.jpg)

## Hardware

- USB interface with mini-USB connector
- 4 user LEDs
- 4 user push buttons
- Reset Button
- ADC connected to a potentiometer
- 2 DAC channels
- GD25Q16 2Mib SPI Flash
- AT24C02C 2KiB EEPROM
- 3.2 TFT LCD (320x240)
- PCM1770 Stereo DAC with Headphone Amplifier
- GD-Link interface

  - CMSIS-DAP swd debug interface over USB HID.
- 2 CAN FD ports

  - This function is not available in this board due to hardware issues, please check `GD32C103` .

For more information about the GD32E103 SoC and GD32E103V-EVAL board:

- [GigaDevice Cortex-M4F High Performance SoC Website](https://www.gigadevice.com/products/microcontrollers/gd32/arm-cortex-m4/value-line/gd32e103-series/)
- [GD32E103 Datasheet](http://www.gd32mcu.com/download/down/document_id/235/path_type/1)
- [GD32E103 Reference Manual](http://www.gd32mcu.com/download/down/document_id/163/path_type/1)
- [GD32E103V Eval Schematics](http://www.gd32mcu.com/download/down/document_id/178/path_type/1)
- [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1)

### Supported Features

The board configuration supports the following hardware features:

| Peripheral | Kconfig option | Devicetree compatible |
| --- | --- | --- |
| NVIC | N/A | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| SYSTICK | N/A | N/A |
| USART | [`CONFIG_SERIAL`](../../../../kconfig.md#CONFIG_SERIAL "CONFIG_SERIAL") | [`gd,gd32-usart`](../../../../build/dts/api/bindings/serial/gd%2Cgd32-usart.md#std-dtcompatible-gd-gd32-usart) |

### Serial Port

The GD32E103V-EVAL board has 5 serial communication ports. The default port
is UART0 at PIN-9 and PIN-10.

## Programming and Debugging

Before program your board make sure to configure boot setting and serial port.
The default serial port is USART0. This port uses header JP-5/6 to route
signals between USB VBUS/ID and USART J2.

| Boot-0 | Boot-1 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | SRAM |
| 1-2 | 2-3 | Bootloader |
| 2-3 | Any | Flash |

| JP-5 | JP-6 | Function |
| --- | --- | --- |
| 1-2 | 1-2 | USART0 / J2 |
| 2-3 | 2-3 | USB VBUS/ID |
| open | open | Free |

### Using GD-Link

The GD32E103V-EVAL includes an onboard programmer/debugger (GD-Link) which
allow flash programming and debug over USB. There are also program and debug
headers J1 and J100 that can be used with any ARM compatible tools.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello-world) sample application:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
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
   west build -b gd32e103v_eval samples/hello_world
   west flash
   ```

   You should see “Hello World! gd32e103v\_eval” in your terminal.
4. To debug an image:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   west debug
   ```

### Using ROM bootloader

The GD32E103 MCU have a ROM bootloader which allow flash programming. User
should install [GD32 ISP Console](http://www.gd32mcu.com/download/down/document_id/175/path_type/1) software at some Linux path. The recommended
is `$HOME/.local/bin`.

1. Build the Zephyr kernel and the [Hello World](../../../../samples/hello_world/README.md#hello-world) sample application:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
   ```
2. Enable board bootloader:

   - Remove boot-0 jumper
   - press reset button
3. To flash an image:

   ```shell
   west build -b gd32e103v_eval samples/hello_world
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

   You should see “Hello World! gd32e103v\_eval” in your terminal.
