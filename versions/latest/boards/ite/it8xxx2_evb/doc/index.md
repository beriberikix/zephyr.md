---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ite/it8xxx2_evb/doc/index.html
original_path: boards/ite/it8xxx2_evb/doc/index.html
---

# IT8XXX2 series

Board Overview

[![../../../../_images/it8xxx2_evb_and_debug_card.jpg](https://docs.zephyrproject.org/4.2.0/_images/it8xxx2_evb_and_debug_card.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/it8xxx2_evb_and_debug_card.jpg)

IT8XXX2 series

Name:
:   `it8xxx2_evb`

Vendor:
:   ITE Tech. Inc.

Architecture:
:   riscv

SoC:
:   it81302bx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ite/it8xxx2_evb/doc/index.rst/../..)

## Overview

The IT8XXX2 is a 32-bit RISC-V Micro-controller.
And a highly integrated embedded controller with system functions.
It is suitable for mobile system applications. The picture below is
the IT81302 MECC board (also known as it8xxx2\_evb) and its debug card.

![IT81302 EVB](https://docs.zephyrproject.org/4.2.0/_images/it8xxx2_evb_and_debug_card1.jpg)

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

The `it8xxx2_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `it8xxx2_evb/it81302bx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ITE IT8XXX2 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L30) | [`ite,riscv-ite`](../../../../build/dts/api/bindings/cpu/ite%2Criscv-ite.md#std-dtcompatible-ite-riscv-ite) |
| ADC | on-chip | ITE it8xxx2 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L461) | [`ite,it8xxx2-adc`](../../../../build/dts/api/bindings/adc/ite%2Cit8xxx2-adc.md#std-dtcompatible-ite-it8xxx2-adc) |
| Counter | on-chip | ITE IT8XXX2 counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L156) | [`ite,it8xxx2-counter`](../../../../build/dts/api/bindings/counter/ite%2Cit8xxx2-counter.md#std-dtcompatible-ite-it8xxx2-counter) |
| Cryptographic accelerator | on-chip | ITE IT8XXX2 Crypto SHA accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L625) | [`ite,it8xxx2-sha`](../../../../build/dts/api/bindings/crypto/ite%2Cit8xxx2-sha.md#std-dtcompatible-ite-it8xxx2-sha) |
| ESPI | on-chip | ITE IT8XXX2 ESPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L427) | [`ite,it8xxx2-espi`](../../../../build/dts/api/bindings/espi/ite%2Cit8xxx2-espi.md#std-dtcompatible-ite-it8xxx2-espi) |
| Flash controller | on-chip | ITE IT8XXX2 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L59) | [`ite,it8xxx2-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ite%2Cit8xxx2-flash-controller.md#std-dtcompatible-ite-it8xxx2-flash-controller) |
| GPIO & Headers | on-chip | ITE IT8xxx2 GPIO[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L165) | [`ite,it8xxx2-gpio`](../../../../build/dts/api/bindings/gpio/ite%2Cit8xxx2-gpio.md#std-dtcompatible-ite-it8xxx2-gpio) |
| on-chip | ITE IT8xxx2 Kscan Pins as GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L16) | [`ite,it8xxx2-gpiokscan`](../../../../build/dts/api/bindings/gpio/ite%2Cit8xxx2-gpiokscan.md#std-dtcompatible-ite-it8xxx2-gpiokscan) |
| I2C | on-chip | ITE it8xxx2 I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L353) | [`ite,it8xxx2-i2c`](../../../../build/dts/api/bindings/i2c/ite%2Cit8xxx2-i2c.md#std-dtcompatible-ite-it8xxx2-i2c) |
| on-chip | ITE enhance I2C[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L404) | [`ite,enhance-i2c`](../../../../build/dts/api/bindings/i2c/ite%2Cenhance-i2c.md#std-dtcompatible-ite-enhance-i2c) |
| Input | on-chip | ITE it8xxx2 keyboard matrix controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L685) | [`ite,it8xxx2-kbd`](../../../../build/dts/api/bindings/input/ite%2Cit8xxx2-kbd.md#std-dtcompatible-ite-it8xxx2-kbd) |
| Interrupt controller | on-chip | ITE Wake-Up Controller (WUC) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2-wuc-map.dtsi?plain=1#L11) | [`ite,it8xxx2-wuc-map`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc-map.md#std-dtcompatible-ite-it8xxx2-wuc-map) |
| on-chip | ITE Wake-Up Controller (WUC)[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L449) | [`ite,it8xxx2-wuc`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc.md#std-dtcompatible-ite-it8xxx2-wuc) |
| on-chip | ITE Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L609) | [`ite,it8xxx2-intc`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-intc.md#std-dtcompatible-ite-it8xxx2-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it8xxx2_evb/it8xxx2_evb.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | ITE, IT8XXX2 Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L52) | [`ite,it8xxx2-bbram`](../../../../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-bbram.md#std-dtcompatible-ite-it8xxx2-bbram) |
| on-chip | ITE IT8XXX2 Instruction Local Memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L77) | [`ite,it8xxx2-ilm`](../../../../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-ilm.md#std-dtcompatible-ite-it8xxx2-ilm) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L65) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it8xxx2_evb/it8xxx2_evb.dts?plain=1#L189) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PECI | on-chip | ITE it8xxx2 PECI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L675) | [`ite,it8xxx2-peci`](../../../../build/dts/api/bindings/peci/ite%2Cit8xxx2-peci.md#std-dtcompatible-ite-it8xxx2-peci) |
| Pin control | on-chip | The ITE IT8XXX2 pin controller is a node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L55) | [`ite,it8xxx2-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl.md#std-dtcompatible-ite-it8xxx2-pinctrl) |
| on-chip | ITE IT8XXX2 Pin Controller[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L62) | [`ite,it8xxx2-pinctrl-func`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl-func.md#std-dtcompatible-ite-it8xxx2-pinctrl-func) |
| PWM | on-chip | ITE, it8xxx2 PWM prescaler node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L559) | [`ite,it8xxx2-pwmprs`](../../../../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwmprs.md#std-dtcompatible-ite-it8xxx2-pwmprs) |
| on-chip | ITE, it8xxx2 Pulse Width Modulator (PWM) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L563)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L574) | [`ite,it8xxx2-pwm`](../../../../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwm.md#std-dtcompatible-ite-it8xxx2-pwm) |
| Sensors | on-chip | ITE, it8xxx2 Voltage Comparator node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L469)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L483) | [`ite,it8xxx2-vcmp`](../../../../build/dts/api/bindings/sensor/ite%2Cit8xxx2-vcmp.md#std-dtcompatible-ite-it8xxx2-vcmp) |
| Serial controller | on-chip | ns16550 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L105) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| on-chip | ITE, IT8XXX2-UART node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L126) | [`ite,it8xxx2-uart`](../../../../build/dts/api/bindings/serial/ite%2Cit8xxx2-uart.md#std-dtcompatible-ite-it8xxx2-uart) |
| SHI | on-chip | ITE IT8XXX2 Serial Host Interface (SHI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L452) | [`ite,it8xxx2-shi`](../../../../build/dts/api/bindings/shi/ite%2Cit8xxx2-shi.md#std-dtcompatible-ite-it8xxx2-shi) |
| SPI | on-chip | IT8XXX2 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L631) | [`ite,it8xxx2-spi`](../../../../build/dts/api/bindings/spi/ite%2Cit8xxx2-spi.md#std-dtcompatible-ite-it8xxx2-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L73) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | ITE IT8xxx2 Tachometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L651)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L660) | [`ite,it8xxx2-tach`](../../../../build/dts/api/bindings/tach/ite%2Cit8xxx2-tach.md#std-dtcompatible-ite-it8xxx2-tach) |
| Timer | on-chip | ITE Ext-timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L144) | [`ite,it8xxx2-timer`](../../../../build/dts/api/bindings/timer/ite%2Cit8xxx2-timer.md#std-dtcompatible-ite-it8xxx2-timer) |
| USB Type-C | on-chip | ITE it8xxx2 USB-C Power Delivery port[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L703) | [`ite,it8xxx2-usbpd`](../../../../build/dts/api/bindings/usb-c/ite%2Cit8xxx2-usbpd.md#std-dtcompatible-ite-it8xxx2-usbpd) |
| Watchdog | on-chip | ITE watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it81xx2.dtsi?plain=1#L617) | [`ite,it8xxx2-watchdog`](../../../../build/dts/api/bindings/watchdog/ite%2Cit8xxx2-watchdog.md#std-dtcompatible-ite-it8xxx2-watchdog) |

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

   ![it8xxx2_evb wiring](https://docs.zephyrproject.org/4.2.0/_images/it8xxx2_evb_wiring.jpg)

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

   > ![../../../../_images/WinFlashTool_P21.jpg](https://docs.zephyrproject.org/4.2.0/_images/WinFlashTool_P21.jpg)
   >
   > ![../../../../_images/WinFlashTool_P41.jpg](https://docs.zephyrproject.org/4.2.0/_images/WinFlashTool_P41.jpg)
2. Using winflash tool flash zephyr.bin into your ITE board.
   First, click `Load` button and select your zephyr.bin file.
   Second, click `run` to flash the iamge into board.

   > ![../../../../_images/WinFlashTool_P31.jpg](https://docs.zephyrproject.org/4.2.0/_images/WinFlashTool_P31.jpg)
3. At this point, you have flashed your image into ITE board and
   it will work if you turn on ITE board. You can use a terminal program
   to verify flashing worked correctly.

   For example, open device manager to find the USB Serial Port(COM4) and use your
   terminal program to connect it(Speed: 115200).

   > ![../../../../_images/WinFlashTool_P11.jpg](https://docs.zephyrproject.org/4.2.0/_images/WinFlashTool_P11.jpg)
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
