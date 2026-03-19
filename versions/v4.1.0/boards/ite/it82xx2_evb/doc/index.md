---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ite/it82xx2_evb/doc/index.html
original_path: boards/ite/it82xx2_evb/doc/index.html
---

# IT82XX2 series

Board Overview

[![../../../../_images/it82xx2_evb_wiring.jpg](../../../../_images/it82xx2_evb_wiring.jpg)
](../../../../_images/it82xx2_evb_wiring.jpg)

IT82XX2 series

Name:
:   `it82xx2_evb`

Vendor:
:   ITE Tech. Inc.

Architecture:
:   riscv

SoC:
:   it82202ax

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ite/it82xx2_evb/doc/index.rst/../..)

## Overview

The IT82XX2 is a 32-bit RISC-V microcontroller.
And a highly integrated embedded controller with system functions.
It is suitable for mobile system applications. The picture below is
the IT82202 development board (also known as it82xx2\_evb) and its debug card.

![IT82202 EVB](../../../../_images/it82xx2_evb_and_debug_card.jpg)

To find out more about ITE, visit our World Wide Web at:[ITE’s website](https://www.ite.com.tw/zh-tw/product/view?mid=169) [[1]](#id2)

## Hardware

The IT82XX2 series contains different chip types(ex, it82202, it82302),
and they support different hardware features.
Listing the IT82202 hardware features as following:

- RISC-V RV32IMAFC instruction set
- 4KB instruction cache size
- 256KB SRAM in total
- Built-in 32.768 kHz clock generator
- Embedded Flash, 512K/1024K-byte e-flash
- eSPI, SSPI, SPI slave, BRAM, KBC, PECI, UART
- GPIO, PWM, ADC, INTC, WUC, Timer, Watchdog, KB scan, JTAG
- Support 6 Voltage Comparator
- Support Cryptographic Engine
- 6 SMBus channels, with 6 DMA controller, compatible with I2C
- USB 2.0 Full-speed Controller
- USB Type-c CC Logic
- USB Power Delivery

### Supported Features

The `it82xx2_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and debugging on it82202

In order to upload the application to the device,
you’ll need our flash tool and Download board.
You can get them at: [ITE’s website](https://www.ite.com.tw/zh-tw/product/view?mid=169) [[1]](#id2).

### Wiring

1. Connect the Download Board to your host computer using the USB cable.
2. Connect the it82xx2\_evb to the evolution motherboard.
3. Connect the Download Board J5 to J41 on the evolution motherboard.
4. Connect the USB to UART wire to J33 on the evolution motherboard.

   ![it82xx2_evb wiring](../../../../_images/it82xx2_evb_wiring1.jpg)

   Note

   Be careful during connection!
   Use separate wires to connect I2C pins with pins on the it82xx2\_evb board.
   Wiring connection is described in the table below.

   | J5 Connector | it82xx2\_evb J41 Connector |
   | --- | --- |
   | 2 | E0 |
   | 3 | E7 |
   | 4 | GND |

   For USB to UART cable, connect the evolution motherboard as below:

   | USB to UART cable | Evolution motherboard J33 Connector |
   | --- | --- |
   | RX | B0 |
   | TX | B1 |
   | GND | GND |

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do
   (see :[Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/getting_started/index.html) [[2]](#id5)):.

   ```shell
   # From the root of the zephyr repository
   west build -b it82xx2_evb samples/hello_world
   ```
2. The file `zephyr.bin` will be created by west.

### Flashing

#### Windows

Use the winflash tool to program a zephyr application
to the it82xx2 board flash.

1. Open the winflash tool and make sure the order you open the switch is right.
   First, turn on the Download board switch.
   Second, turn on the it82xx2\_evb board switch.
   Then, configure your winflash tool like below.

   > ![../../../../_images/WinFlashTool_P2.jpg](../../../../_images/WinFlashTool_P2.jpg)
   >
   > ![../../../../_images/WinFlashTool_P4.jpg](../../../../_images/WinFlashTool_P4.jpg)
2. Using the winflash tool flash `zephyr.bin` into your ITE board.
   First, click the `Load` button and select your `zephyr.bin` file.
   Second, click `run` to flash the image into board.

   > ![../../../../_images/WinFlashTool_P3.jpg](../../../../_images/WinFlashTool_P3.jpg)
3. At this point, you have flashed your image into ITE board and
   it will work if you turn on the ITE board. You can use a terminal program
   to verify flashing worked correctly.

   For example, open device manager to find the USB Serial Port(COM4) and use your
   terminal program to connect it(Speed: 115200).

   > ![../../../../_images/WinFlashTool_P1.jpg](../../../../_images/WinFlashTool_P1.jpg)
4. Turn on the it82xx2\_evb board switch, you should see `"Hello World! it82xx2_evb"`
   sent by the board. If you don’t see this message, press the Reset button and the
   message should appear.

#### Ubuntu

1. Run your favorite terminal program to listen for output.
   Under Linux the terminal should be `/dev/ttyUSB0`. Do not close it.

   For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -b 115200
   ```
2. Open a second terminal window and use the Linux flash tool to flash your board.

   ```shell
   $ sudo ~/itetool/ite -f build/zephyr/zephyr.bin
   ```

   Note

   The source code of ITE tool can be downloaded here:
   [https://www.ite.com.tw/upload/2024\_01\_23/6\_20240123162336wu55j1Rjm4.bz2](https://www.ite.com.tw/upload/2024_01_23/6_20240123162336wu55j1Rjm4.bz2)
3. Split first and second terminal windows to view both of them.
   You should see `"Hello World! it82xx2_evb"` in the first terminal window.
   If you don’t see this message, press the Reset button and the message should appear.

### Debugging

it82xx2\_evb board can be debugged by connecting USB to UART. We can write commands and
read messages through minicom in the Ubuntu terminal.

### Troubleshooting

1. If the flash tool reports a failure, re-plug the 8390 Download board or
   power cycle the it82xx2\_evb board and try again.

### References

[1]
([1](#id3),[2](#id4))

[https://www.ite.com.tw/zh-tw/product/view?mid=169](https://www.ite.com.tw/zh-tw/product/view?mid=169)

[[2](#id6)]

[https://docs.zephyrproject.org/latest/getting\_started/index.html](https://docs.zephyrproject.org/latest/getting_started/index.html)
