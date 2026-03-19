---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/infineon/xmc47_relax_kit/doc/index.html
original_path: boards/infineon/xmc47_relax_kit/doc/index.html
---

# XMC47-RELAX-KIT

Board Overview

[![../../../../_images/xmc47_relax_kit.jpg](../../../../_images/xmc47_relax_kit.jpg)
](../../../../_images/xmc47_relax_kit.jpg)

XMC47-RELAX-KIT

Name:
:   `xmc47_relax_kit`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc4700

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/xmc47_relax_kit/doc/index.rst/../..)

## Overview

The XMC4700 Relax Kit is designed to evaluate the capabilities of the XMC4700
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 144MHz.

### Features:

- ARM Cortex-M4F XMC4700
- On-board Debug Probe with USB interface supporting SWD + SWO
- Virtual COM Port via Debug Probe
- USB (Micro USB Plug)
- 32 Mbit Quad-SPI Flash
- Ethernet PHY and RJ45 Jack
- 32.768 kHz RTC Crystal
- microSD Card Slot
- CAN Transceiver
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Infineon-Board_User_Manual_XMC4700_XMC4800_Relax_Kit_Series-UserManual-v01_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc) [[1]](#id2).

### Supported Features

The `xmc47_relax_kit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

More details about the supported peripherals are available in [XMC4700 TRM](https://www.infineon.com/dgdl/Infineon-ReferenceManual_XMC4700_XMC4800-UM-v01_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044) [[2]](#id4)

## Build hello world sample

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

```shell
# From the root of the zephyr repository
west build -b xmc47_relax_kit samples/hello_world
```

## Programming and Debugging

### West Commands

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> WindowsLinux
>
> ```shell
> # Do a pristine build
> west build -b xmc47_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```
>
> ```shell
> # Do a pristine build
> west build -b xmc47_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Infineon-Board\_User\_Manual\_XMC4700\_XMC4800\_Relax\_Kit\_Series-UserManual-v01\_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc](https://www.infineon.com/dgdl/Infineon-Board_User_Manual_XMC4700_XMC4800_Relax_Kit_Series-UserManual-v01_04-EN.pdf?fileId=5546d46250cc1fdf01513f8e052d07fc)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-ReferenceManual\_XMC4700\_XMC4800-UM-v01\_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044](https://www.infineon.com/dgdl/Infineon-ReferenceManual_XMC4700_XMC4800-UM-v01_03-EN.pdf?fileId=5546d462518ffd850151904eb90c0044)
