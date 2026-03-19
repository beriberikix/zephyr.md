---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/ite/it8xxx2_evb/doc/index.html
original_path: boards/ite/it8xxx2_evb/doc/index.html
---

# ITE IT8XXX2 series

## Overview

The IT8XXX2 is a 32-bit RISC-V Micro-controller.
And a highly integrated embedded controller with system functions.
It is suitable for mobile system applications. The picture below is
the IT81302 MECC board (also known as it8xxx2\_evb) and its debug card.

![IT81302 EVB](../../../../_images/it8xxx2_evb_and_debug_card.jpg)

To find out more about ITE, visit our World Wide Web at:[ITE’s website](https://www.ite.com.tw/en/product/cate2/IT81202) [[1]](#id2)

## Hardware

The IT8XXX2 series contains different chip types(ex, it81302, it83202),
and they support different hardware features.
Listing the IT81302 hardware features as following:

- RISC-V RV32IMAFC instruction set
- 4KB instruction cache size
- 60KB SDRAM in total
- Built-in 32.768 kHz clock generator
- PWM, eSPI, LPC, FLASH, UART, GPIO, Timer, Watchdog, ADC, JTAG
- 6 SMBus channels, with 3 DMA controllers, compatible with I2C
- SPI master/slave
- USB Type-c CC Logic
- USB Power Delivery
- Support KB scan

### Supported Features

currently supports the following hardware features:

Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | interrupt controller |
| TIMER | on-chip | timer |
| UART | on-chip | serial |
| GPIO | on-chip | gpio |
| ADC | on-chip | adc |
| I2C | on-chip | i2c |
| KSCAN | on-chip | kscan |

Other hardware features are not currently supported by Zephyr.

The default configuration can be found in the
[boards/ite/it8xxx2\_evb/it8xxx2\_evb\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it8xxx2_evb/it8xxx2_evb_defconfig) Kconfig file.

## Hardware reworks

Before using the it8xxx2\_evb, some hardware rework is needed. The HW rework
guide can be found in ITE’s website.
[https://www.ite.com.tw/upload/2024\_01\_15/6\_20240115100309cgdjgcLzX3.pdf](https://www.ite.com.tw/upload/2024_01_15/6_20240115100309cgdjgcLzX3.pdf)

## Programming and debugging on it83202

In order to upload the application to the device,
you’ll need our flash tool and Download board.
You can get them at: [ITE’s website](https://www.ite.com.tw/en/product/cate2/IT81202) [[1]](#id2).

### Wiring

1. Connect the Download Board to your host computer using the USB cable.
2. Connect the it8xxx2\_evb to your host computer or a 5V1A USB power supply.
3. Connect the Download Board J5 to J8 on the it8xxx2\_evb board.
4. Connect the USB to UART wire to it8xxx2\_evb.

   ![it8xxx2_evb wiring](../../../../_images/it8xxx2_evb_wiring.jpg)

   Note

   Be careful during connection!
   Use separate wires to connect I2C pins with pins on the it8xxx2\_evb board.
   Wiring connection is described in the table below.

   | J5 Connector | it8xxx2\_evb J8 Connector |
   | --- | --- |
   | 2 | 1 |
   | 3 | 3 |
   | 4 | 5 |

   For USB to UART cable, connect the it8xxx2\_evb as below:

   | USB to UART cable | it8xxx2\_evb J5 Connector |
   | --- | --- |
   | RX | J5.3 |
   | TX | J5.4 |
   | GND | eSPI Debug.10 |

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do
   (see :[Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/getting_started/index.html) [[2]](#id5)):.

   ```shell
   # From the root of the zephyr repository
   west build -b it8xxx2_evb samples/hello_world
   ```
2. The file `zephyr.bin` will be created by west.

### Flashing

#### Windows

Use the winflash tool to program a zephyr application
to the it8xxx2 board flash.

1. Open winflash tool and make sure the order you open the switch is right.
   Fisrt, turn on the Download board switch.
   Second, turn on the it8xxx2\_evb board switch.
   Then, configure your winflash tool like below.

   > ![../../../../_images/WinFlashTool_P21.jpg](../../../../_images/WinFlashTool_P21.jpg)
   >
   > ![../../../../_images/WinFlashTool_P41.jpg](../../../../_images/WinFlashTool_P41.jpg)
2. Using winflash tool flash zephyr.bin into your ITE board.
   First, click `Load` button and select your zephyr.bin file.
   Second, click `run` to flash the iamge into board.

   > ![../../../../_images/WinFlashTool_P31.jpg](../../../../_images/WinFlashTool_P31.jpg)
3. At this point, you have flashed your image into ITE board and
   it will work if you turn on ITE board. You can use a terminal program
   to verify flashing worked correctly.

   For example, open device manager to find the USB Serial Port(COM4) and use your
   terminal program to connect it(Speed: 115200).

   > ![../../../../_images/WinFlashTool_P11.jpg](../../../../_images/WinFlashTool_P11.jpg)
4. Turn on the it8xxx2\_evb board switch, you should see `"Hello World! it8xxx2_evb"`
   sent by the board. If you don’t see this message, press the Reset button and the
   message should appear.

#### Ubuntu

1. Run your favorite terminal program to listen for output.
   Under Linux the terminal should be `/dev/ttyUSB0`. Do not close it.

   For example:

   ```shell
   $ minicom -D /dev/ttyUSB0 -b 115200
   ```
2. Open a second terminal window and use linux flash tool to flash your board.

   ```shell
   $ sudo ~/itetool/ite -f build/zephyr/zephyr.bin
   ```

   Note

   The source code of ITE tool can be downloaded here:
   [https://www.ite.com.tw/upload/2024\_01\_23/6\_20240123162336wu55j1Rjm4.bz2](https://www.ite.com.tw/upload/2024_01_23/6_20240123162336wu55j1Rjm4.bz2)
3. Split first and second terminal windows to view both of them.
   You should see `"Hello World! it8xxx2_evb"` in the first terminal window.
   If you don’t see this message, press the Reset button and the message should appear.

### Debugging

Supporting uart debug, currently.

### Troubleshooting

1. If the flash tool reports a failure, re-plug the 8390 Download board or
   power cycle the it8xxx2\_evb board and try again.

### References

[1]
([1](#id3),[2](#id4))

[https://www.ite.com.tw/en/product/cate2/IT81202](https://www.ite.com.tw/en/product/cate2/IT81202)

[[2](#id6)]

[https://docs.zephyrproject.org/latest/getting\_started/index.html](https://docs.zephyrproject.org/latest/getting_started/index.html)
