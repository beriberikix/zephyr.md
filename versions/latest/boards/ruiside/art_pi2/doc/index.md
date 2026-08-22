---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ruiside/art_pi2/doc/index.html
original_path: boards/ruiside/art_pi2/doc/index.html
---

# ART-Pi2

Board Overview

[![../../../../_images/art_pi2.webp](../../../../_images/art_pi2.webp)
](../../../../_images/art_pi2.webp)

ART-Pi2

Name:
:   `art_pi2`

Vendor:
:   Shanghai Ruiside Electronic Technology Co., Ltd.

Architecture:
:   arm

SoC:
:   stm32h7r7xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ruiside/art_pi2/doc/index.rst/../..)

## Overview

The ART-Pi2 is an open-source hardware platform designed by the
RT-Thread team specifically for embedded software engineers
and open-source makers, offering extensive expandability for DIY projects.

Key Features

- STM32H7R7L8HxH microcontroller featuring 64 Kbytes of Flash and 620 Kbytes of SRAM in an TFBGA225 package
- On-board ST-LINK/V2.1 debugger/programmer
- SDIO TF Card slot
- SDIO WIFI:CYWL6208
- HDC UART BuleTooth:CYWL6208
- 32-MB HyperRAM
- 64-MB HyperFlash
- One Power LED (blue) for 3.3 V power-on
- Two user LEDs blue and red
- Two ST-LINK LEDs: blue and red
- Two push-buttons (user and reset)
- Board connectors:

  - USB OTG with Type-C connector
  - RGB888 FPC connector

More information about the board can be found at the [ART-Pi2 website](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2) [[1]](#id2).

## Hardware

ART-Pi2 provides the following hardware components:

The STM32H7R7xx devices are a high-performance microcontrollers family (STM32H7
Series) based on the high-performance Arm® Cortex®-M7 32-bit RISC core.
They operate at a frequency of up to 600 MHz.

More information about STM32H7R7 can be found here:

- [STM32H7R7L8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html) [[2]](#id4)
- [STM32H7Rx reference manual](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf) [[3]](#id6)

### Supported Features

The `art_pi2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### Default Zephyr Peripheral Mapping:

The ART-Pi2 board features a On-board ST-LINK/V2.1 debugger/programmer. Board is configured as follows:

- UART4 TX/RX : PD1/PD0 (ST-Link Virtual Port Com)
- LED1 (red) : PO1
- LED2 (blue) : PO5
- USER PUSH-BUTTON : PC13

#### System Clock

ART-Pi2 System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 250MHz, driven by an 24MHz high-speed external clock.

#### Serial Port

ART-Pi2 board has 4 UARTs and 3 USARTs plus one LowPower UART. The Zephyr console
output is assigned to UART4. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB13` jumper on the back side of the board.

## Programming and Debugging

The `art_pi2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

ART-Pi2 board includes an ST-LINK/V2.1 embedded debug tool interface.

Note

Check if your ST-LINK V2.1 has newest FW version. It can be done with [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8)

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

#### Flashing an application to ART-Pi2

First, connect the art\_pi2 to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your art\_pi2 board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

or use screen:

```shell
$ screen /dev/ttyACM0 115200
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
*** Booting Zephyr OS build v4.1.0-1907-g415ab379a8af ***
Hello World! art_pi2/stm32h7r7xx
```

Blinky example can also be used:

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b art_pi2 samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2](https://github.com/RT-Thread-Studio/sdk-bsp-stm32h7r-realthread-artpi2)

[[2](#id5)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html](https://www.st.com/en/microcontrollers-microprocessors/stm32h7r7l8.html)

[[3](#id7)]

[https://www.st.com/resource/en/reference\_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf)

[4]
([1](#id9),[2](#id10))

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
