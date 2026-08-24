---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/realtek/rts5912_evb/doc/index.html
original_path: boards/realtek/rts5912_evb/doc/index.html
---

# RTS5912 Evaluation Board

Board Overview

[![../../../../_images/rts5912evb.webp](https://docs.zephyrproject.org/4.1.0/_images/rts5912evb.webp)
](https://docs.zephyrproject.org/4.1.0/_images/rts5912evb.webp)

RTS5912 Evaluation Board

Name:
:   `rts5912_evb`

Vendor:
:   Realtek Semiconductor Corp.

Architecture:
:   arm

SoC:
:   rts5912

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/realtek/rts5912_evb/doc/index.rst/../..)

## Overview

The RTS5912 EVB is a development platform to evaluate the Realtek RTS5912 embedded controller.

## Hardware

- Realtek-M300 Processor (compatible to Cortex-M33)
- Memory:

  > - 384 KB SRAM
  > - 64 KB ROM
  > - 512 KB Flash(MCM)
  > - 256 B Battery SRAM
- PECI interface 3.1
- FAN, PWM and TACHO pins
- 6x I2C instances
- eSPI header
- 1x PS/2 ports
- Keyboard interface headers

For more information about the evb board please see [RTS5912\_EVB\_Schematics](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf) [[1]](#id2) and [RTS5912\_DATASHEET](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf) [[2]](#id4)

The board is powered through the +5V USB Type-C connector or adaptor.

### Supported Features

The `rts5912_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rts5912_evb/rts5912` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L17) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| Clock control | on-chip | Realtek RTS5912 System Clock Controller (SCCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L68) | [`realtek,rts5912-sccon`](../../../../build/dts/api/bindings/clock/realtek,rts5912-sccon.md#std-dtcompatible-realtek-rts5912-sccon) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L48) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| GPIO & Headers | on-chip | Realtek RTS5912 GPIO[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L120) | [`realtek,rts5912-gpio`](../../../../build/dts/api/bindings/gpio/realtek,rts5912-gpio.md#std-dtcompatible-realtek-rts5912-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L238) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Pin control | on-chip | This binding gives a base representation of the pins configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L113) | [`realtek,rts5912-pinctrl`](../../../../build/dts/api/bindings/pinctrl/realtek,rts5912-pinctrl.md#std-dtcompatible-realtek-rts5912-pinctrl) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L95) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| on-chip | Realtek RTS5912 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L104) | [`realtek,rts5912-uart`](../../../../build/dts/api/bindings/serial/realtek,rts5912-uart.md#std-dtcompatible-realtek-rts5912-uart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L42) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Realtek RTS5912 32-bit slow timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L76) | [`realtek,rts5912-slwtimer`](../../../../build/dts/api/bindings/timer/realtek,rts5912-slwtimer.md#std-dtcompatible-realtek-rts5912-slwtimer) |
| on-chip | RTOS Timer on Realtek RTS5912 EC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/realtek/ec/rts5912.dtsi?plain=1#L88) | [`realtek,rts5912-rtmr`](../../../../build/dts/api/bindings/timer/realtek,rts5912-rtmr.md#std-dtcompatible-realtek-rts5912-rtmr) |

## Programming and Debugging

### Building

1. Build [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application as you would normally do.
2. The file `zephyr.rts5912.bin` will be created if the build system can build successfully.
   This binary image can be found under file “build/zephyr/”.

### Flashing

1. Connect Dediprog into header `J81` and `J82`.
2. Use Dediprog SF600 programmer to write the binary into the external flash `U10` at the address 0x0.
3. Power off the board.
4. Set the strap pin `GPIO108` to high and power on the board.

### Debugging

Using SWD or JTAG with ULINPRO.

## References

[[1](#id3)]

[https://github.com/JasonLin-RealTek/Realtek\_EC/blob/main/RTS5912\_EVB\_Schematic\_Ver%201.1\_20240701\_1407.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_EVB_Schematic_Ver%201.1_20240701_1407.pdf)

[[2](#id5)]

[https://github.com/JasonLin-RealTek/Realtek\_EC/blob/main/RTS5912\_datasheet\_brief.pdf](https://github.com/JasonLin-RealTek/Realtek_EC/blob/main/RTS5912_datasheet_brief.pdf)
