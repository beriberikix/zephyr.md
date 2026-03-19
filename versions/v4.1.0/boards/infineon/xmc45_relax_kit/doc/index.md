---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/infineon/xmc45_relax_kit/doc/index.html
original_path: boards/infineon/xmc45_relax_kit/doc/index.html
---

# XMC45-RELAX-KIT

Board Overview

[![../../../../_images/xmc45_relax_kit.jpg](../../../../_images/xmc45_relax_kit.jpg)
](../../../../_images/xmc45_relax_kit.jpg)

XMC45-RELAX-KIT

Name:
:   `xmc45_relax_kit`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   xmc4500

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/xmc45_relax_kit/doc/index.rst/../..)

## Overview

The XMC4500 Relax Kit is designed to evaluate the capabilities of the XMC4500
Microcontroller. It is based on High performance ARM Cortex-M4F which can run
up to 120MHz.

### Features:

- ARM Cortex-M4F XMC4500
- 32 Mbit Quad-SPI Flash
- 4 x SPI-Master, 3x I2C, 3 x I2S, 3 x UART, 2 x CAN, 17 x ADC
- 2 pin header x1 and x2 with 80 pins
- Two buttons and two LEDs for user interaction
- Detachable on-board debugger (second XMC4500) with Segger J-Link

Details on the Relax Kit development board can be found in the [Relax Kit User Manual](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9) [[1]](#id2).

### Supported Features

The `xmc45_relax_kit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

The on-board 12-MHz crystal allows the device to run at its maximum operating speed of 120MHz.

## Build hello world sample

Here is an example for building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample application.

```shell
# From the root of the zephyr repository
west build -b xmc45_relax_kit samples/hello_world
```

## Programming and Debugging

### West Commands

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

> WindowsLinux
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```
>
> ```shell
> # Do a pristine build
> west build -b xmc45_relax_kit -p always samples/hello_world
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Board\_Users\_Manual\_XMC4500\_Relax\_Kit-V1\_R1.2\_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9](https://www.infineon.com/dgdl/Board_Users_Manual_XMC4500_Relax_Kit-V1_R1.2_released.pdf?fileId=db3a30433acf32c9013adf6b97b112f9)
