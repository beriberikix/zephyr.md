---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/openhwgroup/cv64a6_genesys_2/doc/index.html
original_path: boards/openhwgroup/cv64a6_genesys_2/doc/index.html
---

# cv64a6\_genesys\_2

Board Overview

[![../../../../_images/cv64a6_genesys_2.webp](../../../../_images/cv64a6_genesys_2.webp)
](../../../../_images/cv64a6_genesys_2.webp)

cv64a6\_genesys\_2

Name:
:   `cv64a6_genesys_2`

Vendor:
:   OpenHW Group

Architecture:
:   riscv

SoC:
:   cv64a6\_imafdc

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/openhwgroup/cv64a6_genesys_2/doc/index.rst/../..)

## Overview

The Digilent Genesys 2 board features a Xilinx Kintex-7 FPGA which can run various softcore CPUs.
In this configuration, the Genesys 2 is configured with a 64-bit version of the CVA6 RISC-V CPU.
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

- CVA6 CPU with RV64imafdc instruction sets and an SV39 MMU
- 1 GB DDR3 DRAM
- 10/100/1000 Ethernet with copper interface, lowRISC Ethernet MAC
- ns16550a-compatible USB UART, 115200 baud
- RISCV debug module, connected via on-board FTDI (USB JTAG)
- Xilinx SPI controller, connected to microSD slot
- Xilinx GPIO, connected to 7 switches and LEDs

### Supported Features

The `cv64a6_genesys_2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

### Loading the FPGA configuration

You need to build a bitstream with Xilinx Vivado and load it into the FPGA
before you can load zephyr onto the board.
Please refer to the CVA6 documentation for the required steps.
This configuration is compatible with the following build target: cv64a6\_imafdc\_sv39

### Flashing

west flash is supported via the openocd runner.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cv64a6_genesys_2 samples/hello_world
west flash
```

### Debugging

west debug, attach and debugserver commands are supported via the openocd runner.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b cv64a6_genesys_2 samples/hello_world
west debug
```

## References
