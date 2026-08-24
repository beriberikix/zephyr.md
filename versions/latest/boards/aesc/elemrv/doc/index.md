---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/aesc/elemrv/doc/index.html
original_path: boards/aesc/elemrv/doc/index.html
---

# ElemRV-N

Board Overview

Name:
:   `elemrv`

Vendor:
:   Aesc Silicon

Architecture:
:   riscv

SoC:
:   elemrv\_n

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/aesc/elemrv/doc/index.rst/../..)

## Overview

ElemRV-N is an end-to-end open-source RISC-V microcontroller designed using SpinalHDL.

Version 0.2 of ElemRV-N was successfully fabricated using [IHP’s Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK), a 130nm open semiconductor process, with support from [FMD-QNC](https://www.elektronikforschung.de/projekte/fmd-qnc).

For more details, refer to the official [GitHub Project](https://github.com/aesc-silicon/elemrv).

Note

The currently supported silicon version is ElemRV-N 0.2.

## Supported Features

The `elemrv` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### `elemrv/elemrv_n` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | VexRiscv core with the standard configuration as used by LiteX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L19) | [`litex,vexriscv-standard`](../../../../build/dts/api/bindings/cpu/litex,vexriscv-standard.md#std-dtcompatible-litex-vexriscv-standard) |
| Interrupt controller | on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L26) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv,cpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| MTD | on-board | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv/elemrv_elemrv_n.dts?plain=1#L35) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Serial controller | on-chip | Aesc Silicon UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/elemrv-n.dtsi?plain=1#L19) | [`aesc,uart`](../../../../build/dts/api/bindings/serial/aesc,uart.md#std-dtcompatible-aesc-uart) |
| SRAM | on-board | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/aesc/elemrv/elemrv_elemrv_n.dts?plain=1#L23) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/aesc/nitrogen.dtsi?plain=1#L41) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv,machine-timer.md#std-dtcompatible-riscv-machine-timer) |

### System Clock

The system clock for the RISC-V core is set to 20 MHz. This value is specified in the `cpu0` devicetree node using the `clock-frequency` property.

### CPU

ElemRV-N integrates a VexRiscv RISC-V core featuring a 5-stage pipeline and the following ISA extensions:

- M (Integer Multiply/Divide)
- C (Compressed Instructions)

It also includes the following general-purpose `Z` extensions:

- Zicntr – Base Counter and Timer extensions
- Zicsr – Control and Status Register operations
- Zifencei – Instruction-fetch fence

The complete ISA string for this CPU is: `RV32IMC_Zicntr_Zicsr_Zifencei`

### Hart-Level Interrupt Controller (HLIC)

Each CPU core is equipped with a Hart-Level Interrupt Controller, configurable through Control and Status Registers (CSRs).

### Machine Timer

A RISC-V compliant machine timer is enabled by default.

### Serial

The UART (Universal Asynchronous Receiver-Transmitter) interface is a configurable serial communication peripheral used for transmitting and receiving data.

By default, `uart0` operates at a baud rate of `115200`, which can be adjusted via the elemrv device tree.

To evaluate the UART interface, build and run the following sample:

```shell
# From the root of the zephyr repository
west build -b elemrv/elemrv_n samples/hello_world
```
