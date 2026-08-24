---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/openhwgroup/cv32a6_genesys_2/doc/index.html
original_path: boards/openhwgroup/cv32a6_genesys_2/doc/index.html
---

# cv32a6\_genesys\_2

Board Overview

[![../../../../_images/cv32a6_genesys_2.webp](https://docs.zephyrproject.org/4.2.0/_images/cv32a6_genesys_2.webp)
](https://docs.zephyrproject.org/4.2.0/_images/cv32a6_genesys_2.webp)

cv32a6\_genesys\_2

Name:
:   `cv32a6_genesys_2`

Vendor:
:   OpenHW Group

Architecture:
:   riscv

SoC:
:   cv32a6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/openhwgroup/cv32a6_genesys_2/doc/index.rst/../..)

## Overview

The Digilent Genesys 2 board features a Xilinx Kintex-7 FPGA which can run various softcore CPUs.
In this configuration, the Genesys 2 is configured with a 32-bit version of the CVA6 RISC-V CPU.
The SoC is configured with a memory controller interfacing with the Genesys’ DRAM, PLIC and CLINT
interrupt controllers, a UART device interfacing with the Genesys’ USB UART, a RISC-V compatible
debug module that interfaces with the Genesys’ FTDI (USB JTAG) chip, a Xilinx SPI interface
interfacing with the Genesys’ SD card slot and a Xilinx GPIO interfacing with the Genesys’ LEDs
and switches.
The complete hardware sources (see first reference) in conjunction with
instructions for compiling and loading the configuration onto the Genesys 2 are available.

See the following references for more information:

- [CVA6 documentation](https://github.com/openhwgroup/cva6)
- [Genesys 2 Reference Manual](https://digilent.com/reference/programmable-logic/genesys-2/reference-manual)
- [Genesys 2 Schematic](https://digilent.com/reference/_media/reference/programmable-logic/genesys-2/genesys-2_sch.pdf)

## Hardware

- CVA6 CPU with RV32imac instruction sets with PLIC, CLINT interrupt controllers.
- 1 GB DDR3 DRAM
- 10/100/1000 Ethernet with copper interface, lowRISC Ethernet MAC
- ns16550a-compatible USB UART, 115200 baud
- RISCV debug module, connected via on-board FTDI (USB JTAG)
- Xilinx SPI controller, connected to microSD slot
- Xilinx GPIO, connected to 7 switches and LEDs

### Supported Features

The `cv32a6_genesys_2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cv32a6_genesys_2/cv32a6` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | OpenHW Group CVA6 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cv32a6.dtsi?plain=1#L20) | [`openhwgroup,cva6`](../../../../build/dts/api/bindings/cpu/openhwgroup%2Ccva6.md#std-dtcompatible-openhwgroup-cva6) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L17) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| DMA | on-chip | Xilinx AXI DMA LogiCORE IP controller with compatibility string generated in use with the AXI Ethernet subsystem[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L109) | [`xlnx,eth-dma`](../../../../build/dts/api/bindings/dma/xlnx%2Ceth-dma.md#std-dtcompatible-xlnx-eth-dma) |
| GPIO & Headers | on-chip | Xilinx AXI GPIO IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L142) | [`xlnx,xps-gpio-1.00.a`](../../../../build/dts/api/bindings/gpio/xlnx%2Cxps-gpio-1.00.a.md#std-dtcompatible-xlnx-xps-gpio-1.00.a) |
| Interrupt controller | on-chip | SiFive RISCV-V platform-local interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L43) | [`sifive,plic-1.0.0`](../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cplic-1.0.0.md#std-dtcompatible-sifive-plic-1.0.0) |
| on-chip | SiFive RISC-V Core-Local Interruptor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L89) | [`sifive,clint0`](../../../../build/dts/api/bindings/interrupt-controller/sifive%2Cclint0.md#std-dtcompatible-sifive-clint0) |
| on-chip | RISC-V CPU interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cv32a6.dtsi?plain=1#L32) | [`riscv,cpu-intc`](../../../../build/dts/api/bindings/interrupt-controller/riscv%2Ccpu-intc.md#std-dtcompatible-riscv-cpu-intc) |
| Serial controller | on-chip | ns16550 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L56) | [`ns16550`](../../../../build/dts/api/bindings/serial/ns16550.md#std-dtcompatible-ns16550) |
| SPI | on-chip | Xilinx AXI Quad SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L73) | [`xlnx,xps-spi-2.00.a`](../../../../build/dts/api/bindings/spi/xlnx%2Cxps-spi-2.00.a.md#std-dtcompatible-xlnx-xps-spi-2.00.a) |
| Timer | on-chip | RISC-V Machine Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/riscv/openhwgroup/cva6.dtsi?plain=1#L96) | [`riscv,machine-timer`](../../../../build/dts/api/bindings/timer/riscv%2Cmachine-timer.md#std-dtcompatible-riscv-machine-timer) |

## Programming and Debugging

### Loading the FPGA configuration

You need to build a bitstream with Xilinx Vivado and load it into the FPGA
before you can load zephyr onto the board.
Please refer to the CVA6 documentation for the required steps.
This configuration is compatible with the following build targets:
cv32a6\_imac\_sv0, cv32a6\_imac\_sv32, cv32a6\_imafc\_sv32, cv32a6\_ima\_sv32\_fpga.

### Flashing

west flash is supported via the openocd runner.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cv32a6_genesys_2 samples/hello_world
west flash
```

### Debugging

west debug, attach and debugserver commands are supported via the openocd runner.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cv32a6_genesys_2 samples/hello_world
west debug
```

## References
