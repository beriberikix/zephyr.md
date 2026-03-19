---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32h750b_dk/doc/index.html
original_path: boards/st/stm32h750b_dk/doc/index.html
---

# STM32H750B Discovery Kit

Board Overview

[![../../../../_images/stm32h750b_dk.png](../../../../_images/stm32h750b_dk.png)
](../../../../_images/stm32h750b_dk.png)

STM32H750B Discovery Kit

Name:
:   `stm32h750b_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h750xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32h750b_dk/doc/index.rst/../..)

## Overview

The STM32H750B-DK Discovery kit is a complete demonstration and development
platform for Arm® Cortex®-M7 core-based STM32H750XBH6 microcontroller, with
128Kbytes of Flash memory and 1 Mbytes of SRAM.

The STM32H750B-DK Discovery kit is used as a reference design for user
application development before porting to the final product, thus simplifying
the application development.

The full range of hardware features available on the board helps users to enhance
their application development by an evaluation of all the peripherals (such as
USB OTG FS, Ethernet, microSD™ card, USART, CAN FD, SAI audio DAC stereo with
audio jack input and output, MEMS digital microphone, HyperRAM™,
Octo-SPI Flash memory, RGB interface LCD with capacitive touch panel, and others).
ARDUINO® Uno V3, Pmod™ and STMod+ connectors provide easy connection to extension
shields or daughterboards for specific applications.

STLINK-V3E is integrated into the board, as the embedded in-circuit debugger and
programmer for the STM32 MCU and USB Virtual COM port bridge. STM32H750B-DK board
comes with the STM32CubeH7 MCU Package, which provides an STM32 comprehensive
software HAL library as well as various software examples.

More information about the board can be found at the [STM32H750B-DK website](https://www.st.com/en/evaluation-tools/stm32h750b-dk.html).
More information about STM32H750 can be found here:

- [STM32H750 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h750-value-line.html)
- [STM32H750xx reference manual](https://www.st.com/resource/en/reference_manual/rm0433-stm32h742-stm32h743753-and-stm32h750-value-line-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)
- [STM32H750xx datasheet](https://www.st.com/resource/en/datasheet/stm32h750ib.pdf)

### Supported Features

The `stm32h750b_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

For more details please refer to [STM32H750B-DK website](https://www.st.com/en/evaluation-tools/stm32h750b-dk.html).

#### Default Zephyr Peripheral Mapping:

- UART\_3 TX/RX : PB10/PB11 (ST-Link Virtual Port Com)
- LD1 : PJ2
- LD2 : PI13
- USART1 TX/RX : PB6/PB7 (Arduino D1/D0)

### System Clock

The STM32H750B System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock
is driven by the PLL clock at 480MHz. PLL clock is feed by a 25MHz high speed external clock.

### Serial Port

The STM32H750B Discovery kit has up to 6 UARTs.
The Zephyr console output is assigned to UART3 which connected to the onboard ST-LINK/V3.0. Virtual
COM port interface. Default communication settings are 115200 8N1.

## Programming and Debugging

STM32H750B Discovery kit includes an ST-LINK-V3E embedded debug tool interface.
This probe allows flashing and debugging the board using various tools.

See [Building an Application](../../../../develop/application/index.md#build-an-application) for more information about application builds.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32H750B\_DK

Connect the STM32H750B-DK to your host computer using the ST-LINK
USB port, then run a serial host program to connect with the board. For example:

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

You can then build and flash applications in the usual way.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32h750b_dk samples/hello_world
west flash
```

You should see the following message in the serial host program:

```shell
$ Hello World! stm32h750b_dk
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32h750b_dk samples/hello_world
west debug
```
