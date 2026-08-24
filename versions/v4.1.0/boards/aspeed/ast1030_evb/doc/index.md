---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/aspeed/ast1030_evb/doc/index.html
original_path: boards/aspeed/ast1030_evb/doc/index.html
---

# AST1030\_EVB

Board Overview

[![../../../../_images/ast1030_evb.jpg](https://docs.zephyrproject.org/4.1.0/_images/ast1030_evb.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/ast1030_evb.jpg)

AST1030\_EVB

Name:
:   `ast1030_evb`

Vendor:
:   ASPEED Technology Inc.

Architecture:
:   arm

SoC:
:   ast1030

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/aspeed/ast1030_evb/doc/index.rst/../..)

## Overview

The AST1030\_EVB kit is a development platform to evaluate the
Aspeed AST10x0 series SOCs. This board needs to be mated with
part number AST1030.

## Hardware

- ARM Cortex-M4F Processor
- 768 KB on-chip SRAM for instruction and data memory
- 1 MB on-chip Flash memory for boot ROM and data storage
- SPI interface
- UART interface
- I2C/I3C interface
- FAN PWM interface
- ADC interface
- JTAG interface
- USB interface
- LPC interface
- eSPI interface

### Supported Features

The `ast1030_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ast1030_evb/ast1030` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L16) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| Clock control | on-chip | Aspeed AST10X0 Clock Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L31) | [`aspeed,ast10x0-clock`](../../../../build/dts/api/bindings/clock/aspeed%2Cast10x0-clock.md#std-dtcompatible-aspeed-ast10x0-clock) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| Reset controller | on-chip | Aspeed AST10X0 Reset Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L36) | [`aspeed,ast10x0-reset`](../../../../build/dts/api/bindings/reset/aspeed%2Cast10x0-reset.md#std-dtcompatible-aspeed-ast10x0-reset) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L42) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L23) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| System controller | on-chip | System Controller Registers R/W[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/aspeed/ast10x0.dtsi?plain=1#L28) | [`syscon`](../../../../build/dts/api/bindings/syscon/syscon.md#std-dtcompatible-syscon) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Connections and IOs

Aspeed to provide the schematic for this board.

### System Clock

The AST1030 SOC is configured to use external 25MHz clock input to generate 200Mhz system clock by
the on-chip PLL.

### Serial Port

UART5 is configured for serial logs. The default serial setup is 115200 8N1.

## Programming and Debugging

This board comes with a JTAG port which facilitates debugging using a single physical connection.

### Flashing

Build application as usual for the `ast1030_evb` board, and flash
using SF100 SPI Flash programmer. See the
[Aspeed Zephyr SDK User Guide](https://github.com/AspeedTech-BMC/zephyr/releases/download/v00.01.03/Aspeed_Zephy_SDK_User_Guide_v00.01.03.pdf) [[1]](#id2) for more information.

### Debugging

Use JTAG or SWD with a J-Link

## References

[[1](#id3)]

[https://github.com/AspeedTech-BMC/zephyr/releases/download/v00.01.03/Aspeed\_Zephy\_SDK\_User\_Guide\_v00.01.03.pdf](https://github.com/AspeedTech-BMC/zephyr/releases/download/v00.01.03/Aspeed_Zephy_SDK_User_Guide_v00.01.03.pdf)
