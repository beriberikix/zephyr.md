---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ite/it515xx_evb/doc/index.html
original_path: boards/ite/it515xx_evb/doc/index.html
---

# IT51XXX series

Board Overview

[![../../../../_images/it515xx_evb_wiring.webp](../../../../_images/it515xx_evb_wiring.webp)
](../../../../_images/it515xx_evb_wiring.webp)

IT51XXX series

Name:
:   `it515xx_evb`

Vendor:
:   ITE Tech. Inc.

Architecture:
:   riscv

SoC:
:   it51526aw

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ite/it515xx_evb/doc/index.rst/../..)

## Overview

The IT51XXX is a 32-bit RISC-V microcontroller.
And a highly integrated embedded controller with system functions.
It is suitable for mobile system applications. The picture below is
the IT51526 development board (also known as it515xx\_evb) and its debug card.

![IT51526 EVB](../../../../_images/it515xx_evb_and_debug_card.webp)

To find out more about ITE, visit our World Wide Web at:[ITE’s website](https://www.ite.com.tw/en) [[1]](#id2)

## Hardware

The IT51XXX series contains different chip types(ex, it51526, it51527),
and they support different hardware features.
Listing the IT51526 hardware features as following:

- RISC-V RV32IMC instruction set
- 4KB instruction cache size
- 128KB SRAM in total
- Built-in 32.768 kHz clock generator
- Embedded Flash, 512K/1024K-byte e-flash
- eSPI, SPI, BRAM, KBC, PECI, UART
- GPIO, PWM, ADC, INTC, WUC, Timer, Watchdog, KB scan, JTAG
- Support 3 Voltage Comparator
- Support Cryptographic Engine
- 9 SMBus hosts, 3 targets, with 12 SMBus channels, compatible with I2C
- I3C host: Support two I3C controllers, compliant with the MIPI I3C v1.0 SEPC.
- Two-wire serial interface up to 12.5MHz using Push-Pull.
- Support SDR, IBI, Hot-Join.
- I3C target: Support SDR, FIFO co-use DLM. Support Push-Pull output.

### Supported Features

The `it515xx_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `it515xx_evb/it51526aw` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ITE IT8XXX2 RISC-V CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L31) | [`ite,riscv-ite`](../../../../build/dts/api/bindings/cpu/ite%2Criscv-ite.md#std-dtcompatible-ite-riscv-ite) |
| ADC | on-chip | ITE it51xxx ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L78) | [`ite,it51xxx-adc`](../../../../build/dts/api/bindings/adc/ite%2Cit51xxx-adc.md#std-dtcompatible-ite-it51xxx-adc) |
| Clock control | on-chip | ITE it51xxx ECPM (EC Clock and Power Management Controller) node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1124) | [`ite,it51xxx-ecpm`](../../../../build/dts/api/bindings/clock/ite%2Cit51xxx-ecpm.md#std-dtcompatible-ite-it51xxx-ecpm) |
| Comparator | on-chip | ITE, it51xxx Voltage Comparator node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L98)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L88) | [`ite,it51xxx-vcmp`](../../../../build/dts/api/bindings/comparator/ite%2Cit51xxx-vcmp.md#std-dtcompatible-ite-it51xxx-vcmp) |
| Counter | on-chip | ITE IT51XXX counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1196) | [`ite,it51xxx-counter`](../../../../build/dts/api/bindings/counter/ite%2Cit51xxx-counter.md#std-dtcompatible-ite-it51xxx-counter) |
| Cryptographic accelerator | on-chip | ITE IT51XXX Crypto SHA accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1383) | [`ite,it51xxx-sha`](../../../../build/dts/api/bindings/crypto/ite%2Cit51xxx-sha.md#std-dtcompatible-ite-it51xxx-sha) |
| ESPI | on-chip | ITE IT8XXX2 ESPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1223) | [`ite,it8xxx2-espi`](../../../../build/dts/api/bindings/espi/ite%2Cit8xxx2-espi.md#std-dtcompatible-ite-it8xxx2-espi) |
| Flash controller | on-chip | ITE IT8XXX2 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L54) | [`ite,it8xxx2-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ite%2Cit8xxx2-flash-controller.md#std-dtcompatible-ite-it8xxx2-flash-controller) |
| GPIO & Headers | on-chip | This binding gives a base representation of the it51xxx series gpio[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L123) | [`ite,it51xxx-gpio`](../../../../build/dts/api/bindings/gpio/ite%2Cit51xxx-gpio.md#std-dtcompatible-ite-it51xxx-gpio) |
| I2C | on-chip | ITE it51xxx I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L971)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L988) | [`ite,it51xxx-i2c`](../../../../build/dts/api/bindings/i2c/ite%2Cit51xxx-i2c.md#std-dtcompatible-ite-it51xxx-i2c) |
| I3C | on-chip | IT51XXX I3CM controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1337) | [`ite,it51xxx-i3cm`](../../../../build/dts/api/bindings/i3c/ite%2Cit51xxx-i3cm.md#std-dtcompatible-ite-it51xxx-i3cm) |
| on-chip | IT51XXX I3CS controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1359) | [`ite,it51xxx-i3cs`](../../../../build/dts/api/bindings/i3c/ite%2Cit51xxx-i3cs.md#std-dtcompatible-ite-it51xxx-i3cs) |
| Input | on-chip | ITE it51xxx keyboard matrix controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1205) | [`ite,it51xxx-kbd`](../../../../build/dts/api/bindings/input/ite%2Cit51xxx-kbd.md#std-dtcompatible-ite-it51xxx-kbd) |
| Interrupt controller | on-chip | ITE Wake-Up Controller (WUC) mapping child node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx-wuc-map.dtsi?plain=1#L11) | [`ite,it51xxx-wuc-map`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit51xxx-wuc-map.md#std-dtcompatible-ite-it51xxx-wuc-map) |
| on-chip | ITE Wake-Up Controller (WUC)[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L803) | [`ite,it51xxx-wuc`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit51xxx-wuc.md#std-dtcompatible-ite-it51xxx-wuc) |
| on-chip | ITE Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1178) | [`ite,it51xxx-intc`](../../../../build/dts/api/bindings/interrupt-controller/ite%2Cit51xxx-intc.md#std-dtcompatible-ite-it51xxx-intc) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it515xx_evb/it515xx_evb.dts?plain=1#L33) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | ITE IT8XXX2 Instruction Local Memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L73) | [`ite,it8xxx2-ilm`](../../../../build/dts/api/bindings/memory-controllers/ite%2Cit8xxx2-ilm.md#std-dtcompatible-ite-it8xxx2-ilm) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L60) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ite/it515xx_evb/it515xx_evb.dts?plain=1#L65) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The ITE IT8XXX2 pin controller is a node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L549) | [`ite,it8xxx2-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl.md#std-dtcompatible-ite-it8xxx2-pinctrl) |
| on-chip | ITE IT8XXX2 Pin Controller[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L556) | [`ite,it8xxx2-pinctrl-func`](../../../../build/dts/api/bindings/pinctrl/ite%2Cit8xxx2-pinctrl-func.md#std-dtcompatible-ite-it8xxx2-pinctrl-func) |
| PWM | on-chip | ITE, it51xxx Pulse Width Modulator (PWM) node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1255)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1263) | [`ite,it51xxx-pwm`](../../../../build/dts/api/bindings/pwm/ite%2Cit51xxx-pwm.md#std-dtcompatible-ite-it51xxx-pwm) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1136)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1157) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| on-chip | ITE, IT51XXX-UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1147)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1168) | [`ite,it51xxx-uart`](../../../../build/dts/api/bindings/serial/ite%2Cit51xxx-uart.md#std-dtcompatible-ite-it51xxx-uart) |
| SPI | on-chip | IT51XXX SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1389) | [`ite,it51xxx-spi`](../../../../build/dts/api/bindings/spi/ite%2Cit51xxx-spi.md#std-dtcompatible-ite-it51xxx-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L68) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | ITE, it51xxx Tachometer node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1319)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1325) | [`ite,it51xxx-tach`](../../../../build/dts/api/bindings/tach/ite%2Cit51xxx-tach.md#std-dtcompatible-ite-it51xxx-tach) |
| Timer | on-chip | ITE it51xxx external timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1186) | [`ite,it51xxx-timer`](../../../../build/dts/api/bindings/timer/ite%2Cit51xxx-timer.md#std-dtcompatible-ite-it51xxx-timer) |
| Watchdog | on-chip | ITE watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/ite/it51xxx.dtsi?plain=1#L1248) | [`ite,it51xxx-watchdog`](../../../../build/dts/api/bindings/watchdog/ite%2Cit51xxx-watchdog.md#std-dtcompatible-ite-it51xxx-watchdog) |

## Programming and debugging on it51526

In order to upload the application to the device,
you’ll need our flash tool and Download board.
You can get them at: [ITE’s website](https://www.ite.com.tw/en) [[1]](#id2).

### Wiring

1. Connect the Download Board to your host computer using the USB cable.
2. Connect the it515xx\_evb to the evolution motherboard.
3. Connect the Download Board J5 to J38(GPC1 & GPC2) on the evolution motherboard.
4. Connect the USB to UART wire to UART0 connector on the evolution motherboard.

   ![it515xx_evb wiring](../../../../_images/it515xx_evb_wiring1.webp)

   Note

   Be careful during connection!
   Use separate wires to connect I2C pins with pins on the it515xx\_evb board.
   Wiring connection is described in the table below.

   | J5 Connector | it515xx\_evb J38 Connector |
   | --- | --- |
   | 2 | C1 |
   | 3 | C2 |
   | 4 | GND |

   For USB to UART cable, connect the evolution motherboard as below:

   | USB to UART cable | Evolution motherboard UART0 Connector |
   | --- | --- |
   | USB | UART0 |

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do
   (see :[Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/getting_started/index.html) [[2]](#id5)):.

   ```shell
   # From the root of the zephyr repository
   west build -b it515xx_evb samples/hello_world
   ```
2. The file `zephyr.bin` will be created by west.

### Flashing

#### Windows

Use the winflash tool to program a zephyr application
to the it515xx board flash.

1. Flashing steps as described in the link: [Flashing steps](https://docs.zephyrproject.org/latest/boards/ite/it82xx2_evb/doc/index.html#flashing) [[3]](#id7).
2. Turn on the it515xx\_evb board switch, you should see `"Hello World! it515xx_evb"`
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
   You should see `"Hello World! it515xx_evb"` in the first terminal window.
   If you don’t see this message, press the Reset button and the message should appear.

### Debugging

it515xx\_evb board can be debugged by connecting USB to UART. We can write commands and
read messages through minicom in the Ubuntu terminal.

### Troubleshooting

1. If the flash tool reports a failure, re-plug the 8390 Download board or
   power cycle the it515xx\_evb board and try again.

### References

[1]
([1](#id3),[2](#id4))

[https://www.ite.com.tw/en](https://www.ite.com.tw/en)

[[2](#id6)]

[https://docs.zephyrproject.org/latest/getting\_started/index.html](https://docs.zephyrproject.org/latest/getting_started/index.html)

[[3](#id8)]

[https://docs.zephyrproject.org/latest/boards/ite/it82xx2\_evb/doc/index.html#flashing](https://docs.zephyrproject.org/latest/boards/ite/it82xx2_evb/doc/index.html#flashing)
