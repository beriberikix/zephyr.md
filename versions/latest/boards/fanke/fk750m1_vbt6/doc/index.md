---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/fanke/fk750m1_vbt6/doc/index.html
original_path: boards/fanke/fk750m1_vbt6/doc/index.html
---

# FK750M1-VBT6

Board Overview

[![../../../../_images/fk750m1_vbt6.webp](../../../../_images/fk750m1_vbt6.webp)
](../../../../_images/fk750m1_vbt6.webp)

FK750M1-VBT6

Name:
:   `fk750m1_vbt6`

Vendor:
:   FANKE Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32h750xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/fanke/fk750m1_vbt6/doc/index.rst/../..)

## Overview

The FK750M1-VBT6 core board by FANKE Technology Co., Ltd. is an advanced microcontroller
platform based on the STMicroelectronics Arm® Cortex®-M7 core STM32H750VBT6 microcontroller.
This board is an ideal solution for developers looking to create high-performance
applications, leveraging its robust capabilities and support for sophisticated display
and image processing technologies.

The FK750M1-VBT6 is designed as a reference design for user application development before
transitioning to the final product, significantly simplifying the development process.
Its wide range of hardware features, including advanced display and image processing capabilities,
allowing for comprehensive evaluation and testing of peripherals and functionalities.

## Hardware

FK750M1-VBT6 provides the following hardware components:

- STM32H750VB in LQFP100 package
- ARM 32-bit Cortex-M7 CPU with FPU
- 480 MHz max CPU frequency
- 128 KB Flash
- 1 MB SRAM: 192 Kbytes TCM RAM (64 Kbytes ITCM RAM + 128 Kbytes DTCM RAM), 864 Kbytes user SRAM, and 4 Kbytes SRAM in Backup domain
- Main clock: External 25MHz crystal oscillator.
- RTC: 32.768kHz crystal oscillator.
- high-resolution timers(2.1 ns max resolution, 1)
- 32-bit timers(2)
- 16-bit timers(17)
- 1 reset button, and 1 BOOT button
- 1 user LED
- External 64-Mbit QSPI (W25Q64) NOR Flash memory.
- USB OTG Full Speed and High Speed(1)
- 1 micro SD card
- 1 DCMI camera interface
- 1 SPI LCD interface
- SWD and serial port accessibility through a pin header
- Bring out 73 IO ports

More information about STM32H750VB can be found here:

- [STM32H750VB on www.st.com](https://www.st.com/en/microcontrollers/stm32h750vb.html) [[1]](#id2)

### Supported Features

The `fk750m1_vbt6` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

FK750M1-VBT6 board has 5 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Default Zephyr Peripheral Mapping:

The FK750M1-VBT6 board is configured as follows

- UART\_1 TX/RX : PA9/PA10 (available on the header pins)
- User LED (blue) : PC13
- SPI4 NCS/CLK/MOSI : PE11/PE12/PE14 (SPI LCD)
- QuadSPI NCS/CLK/IO0/IO1/IO2/IO3 : PB6/PB2/PD11/PD12/PE2/PD13 (NOR Flash)
- USB DM/DP : PA11/PA12

### System Clock

The FK750M1-VBT6 System Clock could be driven by an internal or external oscillator,
as well as by the main PLL clock. By default the system clock is driven by the PLL clock at 480MHz,
driven by an 25MHz external crystal oscillator.

### Serial Port

The Zephyr console output is assigned to UART1. The default communication settings are 115200 8N1.

## Programming and Debugging

Applications for the `fk750m1_vbt6` board target can be built and flashed in the usual
way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The FK750M1-VBT6 board does not include an on-board debugger. As a result, it requires
an external debugger, such as ST-Link, for programming and debugging purposes.

The board provides header pins for the Serial Wire Debug (SWD) interface.

#### Flashing an application to FK750M1-VBT6

To begin, connect the ST-Link Debug Programmer to the FK750M1-VBT6 board using the SWD
interface. Next, connect the ST-Link to your host computer via a USB port.
Once this setup is complete, you can proceed to build and flash your application to the board

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b fk750m1_vbt6 samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0 -b 115200
```

Then, press the RESET button, you should see the following message:

```shell
Hello World! fk750m1_vbt6
```

### Debugging

This current Zephyr port does not support debugging.

## References

[[1](#id3)]

[https://www.st.com/en/microcontrollers/stm32h750vb.html](https://www.st.com/en/microcontrollers/stm32h750vb.html)
