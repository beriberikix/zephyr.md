---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ite/it82xx2_evb/doc/index.html
original_path: boards/ite/it82xx2_evb/doc/index.html
---

# IT82XX2 series

Board Overview

[![../../../../_images/it82xx2_evb_and_debug_card.jpg](../../../../_images/it82xx2_evb_and_debug_card.jpg)
](../../../../_images/it82xx2_evb_and_debug_card.jpg)

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

![IT82202 EVB](../../../../_images/it82xx2_evb_and_debug_card1.jpg)

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

#### `it82xx2_evb/it82202ax` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ITE IT8XXX2 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L30) | [`ite,riscv-ite`](../../../../build/dts/api/bindings/cpu/ite%2Criscv-ite.md#std-dtcompatible-ite-riscv-ite) |
| ADC | on-chip | ITE it8xxx2 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L461) | [`ite,it8xxx2-adc`](../../../../build/dts/api/bindings/adc/ite%2Cit8xxx2-adc.md#std-dtcompatible-ite-it8xxx2-adc) |
| Counter | on-chip | ITE IT8XXX2 counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L156) | [`ite,it8xxx2-counter`](../../../../build/dts/api/bindings/counter/ite%2Cit8xxx2-counter.md#std-dtcompatible-ite-it8xxx2-counter) |
| Cryptographic accelerator | on-chip | ITE IT8XXX2 Crypto SHA accelerator V2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L1015) | [`ite,it8xxx2-sha-v2`](../../../../build/dts/api/bindings/crypto/ite%2Cit8xxx2-sha-v2.md#std-dtcompatible-ite-it8xxx2-sha-v2) |
| ESPI | on-chip | ITE IT8XXX2 ESPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L427) | [`ite,it8xxx2-espi`](../../../../build/dts/api/bindings/espi/ite%2Cit8xxx2-espi.md#std-dtcompatible-ite-it8xxx2-espi) |
| Flash controller | on-chip | ITE IT8XXX2 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L59) | [`ite,it8xxx2-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ite%2Cit8xxx2-flash-controller.md#std-dtcompatible-ite-it8xxx2-flash-controller) |
| GPIO & Headers | on-chip | ITE IT8xxx2 GPIO V2[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L165) | [`ite,it8xxx2-gpio-v2`](../../../../build/dts/api/bindings/gpio/ite%2Cit8xxx2-gpio-v2.md#std-dtcompatible-ite-it8xxx2-gpio-v2) |
| I2C | on-chip | ITE enhance I2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L903) | [`ite,enhance-i2c`](../../../../build/dts/api/bindings/i2c/ite%2Cenhance-i2c.md#std-dtcompatible-ite-enhance-i2c) |
| Input | on-chip | ITE it8xxx2 keyboard matrix controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L685) | [`ite,it8xxx2-kbd`](../../../../build/dts/api/bindings/input/ite%2Cit8xxx2-kbd.md#std-dtcompatible-ite-it8xxx2-kbd) |
| Interrupt controller | on-chip | ITE Wake-Up Controller (WUC) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2-wuc-map.dtsi?plain=1#L11) | [`ite,it8xxx2-wuc-map`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc-map.md#std-dtcompatible-ite-it8xxx2-wuc-map) |
| on-chip | ITE Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L16) | [`ite,it8xxx2-intc-v2`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-intc-v2.md#std-dtcompatible-ite-it8xxx2-intc-v2) |
| on-chip | ITE Wake-Up Controller (WUC)[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L743) | [`ite,it8xxx2-wuc`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit8xxx2-wuc.md#std-dtcompatible-ite-it8xxx2-wuc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it82xx2_evb/it82xx2_evb.dts?plain=1#L34) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | ITE, IT8XXX2 Battery Backed RAM node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L52) | [`ite,it8xxx2-bbram`](../../../../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-bbram.md#std-dtcompatible-ite-it8xxx2-bbram) |
| on-chip | ITE IT8XXX2 Instruction Local Memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L77) | [`ite,it8xxx2-ilm`](../../../../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-ilm.md#std-dtcompatible-ite-it8xxx2-ilm) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L65) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it82xx2_evb/it82xx2_evb.dts?plain=1#L215) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PECI | on-chip | ITE it8xxx2 PECI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L675) | [`ite,it8xxx2-peci`](../../../../build/dts/api/bindings/peci/ite%2Cit8xxx2-peci.md#std-dtcompatible-ite-it8xxx2-peci) |
| Pin control | on-chip | The ITE IT8XXX2 pin controller is a node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L441) | [`ite,it8xxx2-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl.md#std-dtcompatible-ite-it8xxx2-pinctrl) |
| on-chip | ITE IT8XXX2 Pin Controller[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L448) | [`ite,it8xxx2-pinctrl-func`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl-func.md#std-dtcompatible-ite-it8xxx2-pinctrl-func) |
| PWM | on-chip | ITE, it8xxx2 PWM prescaler node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L559) | [`ite,it8xxx2-pwmprs`](../../../../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwmprs.md#std-dtcompatible-ite-it8xxx2-pwmprs) |
| on-chip | ITE, it8xxx2 Pulse Width Modulator (PWM) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L563)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L574) | [`ite,it8xxx2-pwm`](../../../../build/dts/api/bindings/pwm/ite%2Cit8xxx2-pwm.md#std-dtcompatible-ite-it8xxx2-pwm) |
| Sensors | on-chip | ITE, it8xxx2 Voltage Comparator node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L469)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L483) | [`ite,it8xxx2-vcmp`](../../../../build/dts/api/bindings/sensor/ite%2Cit8xxx2-vcmp.md#std-dtcompatible-ite-it8xxx2-vcmp) |
| Serial controller | on-chip | ns16550 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L105) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| on-chip | ITE, IT8XXX2-UART node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L126) | [`ite,it8xxx2-uart`](../../../../build/dts/api/bindings/serial/ite%2Cit8xxx2-uart.md#std-dtcompatible-ite-it8xxx2-uart) |
| SHI | on-chip | ITE IT8XXX2 Serial Host Interface (SHI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L452) | [`ite,it8xxx2-shi`](../../../../build/dts/api/bindings/shi/ite%2Cit8xxx2-shi.md#std-dtcompatible-ite-it8xxx2-shi) |
| SPI | on-chip | IT8XXX2 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L1021) | [`ite,it8xxx2-spi`](../../../../build/dts/api/bindings/spi/ite%2Cit8xxx2-spi.md#std-dtcompatible-ite-it8xxx2-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L73) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | ITE IT8xxx2 Tachometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L651)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L660) | [`ite,it8xxx2-tach`](../../../../build/dts/api/bindings/tach/ite%2Cit8xxx2-tach.md#std-dtcompatible-ite-it8xxx2-tach) |
| Timer | on-chip | ITE Ext-timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L144) | [`ite,it8xxx2-timer`](../../../../build/dts/api/bindings/timer/ite%2Cit8xxx2-timer.md#std-dtcompatible-ite-it8xxx2-timer) |
| USB | on-chip | ITE IT82XX2 USB in device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L1002) | [`ite,it82xx2-usb`](../../../../build/dts/api/bindings/usb/ite%2Cit82xx2-usb.md#std-dtcompatible-ite-it82xx2-usb) |
| USB Type-C | on-chip | ITE it8xxx2 USB-C Power Delivery port[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it8xxx2.dtsi?plain=1#L703) | [`ite,it8xxx2-usbpd`](../../../../build/dts/api/bindings/usb-c/ite%2Cit8xxx2-usbpd.md#std-dtcompatible-ite-it8xxx2-usbpd) |
| Watchdog | on-chip | ITE watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it82xx2.dtsi?plain=1#L24) | [`ite,it8xxx2-watchdog`](../../../../build/dts/api/bindings/watchdog/ite%2Cit8xxx2-watchdog.md#std-dtcompatible-ite-it8xxx2-watchdog) |

## Programming and debugging on it82202

In order to upload the application to the device,
you’ll need our flash tool and Download board.
You can get them at: [ITE’s website](https://www.ite.com.tw/zh-tw/product/view?mid=169) [[1]](#id2).

### Wiring

1. Connect the Download Board to your host computer using the USB cable.
2. Connect the it82xx2\_evb to the evolution motherboard.
3. Connect the Download Board J5 to J41 on the evolution motherboard.
4. Connect the USB to UART wire to J33 on the evolution motherboard.

   ![it82xx2_evb wiring](../../../../_images/it82xx2_evb_wiring.jpg)

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
