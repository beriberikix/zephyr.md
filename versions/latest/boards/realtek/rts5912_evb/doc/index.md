---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/realtek/rts5912_evb/doc/index.html
original_path: boards/realtek/rts5912_evb/doc/index.html
---

# RTS5912 Evaluation Board

Board Overview

[![../../../../_images/rts5912evb.webp](../../../../_images/rts5912evb.webp)
](../../../../_images/rts5912evb.webp)

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
