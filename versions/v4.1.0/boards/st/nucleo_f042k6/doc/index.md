---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f042k6/doc/index.html
original_path: boards/st/nucleo_f042k6/doc/index.html
---

# Nucleo F042K6

Board Overview

[![../../../../_images/nucleo_f042k6.jpg](../../../../_images/nucleo_f042k6.jpg)
](../../../../_images/nucleo_f042k6.jpg)

Nucleo F042K6

Name:
:   `nucleo_f042k6`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f042x6

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f042k6/doc/index.rst/../..)

## Overview

The STM32 Nucleo-32 development board with STM32F042K6 MCU, supports Arduino nano connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption and features.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

More information about the board can be found at the [Nucleo F042K6 website](https://www.st.com/en/evaluation-tools/nucleo-f042k6.html) [[1]](#id2).

## Hardware

Nucleo F042K6 provides the following hardware components:

- STM32 microcontroller in LQFP32 package
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
- Three LEDs:

  - USB communication (LD1), user LED (LD2), power LED (LD3)
- reset push button

More information about STM32F042K6 can be found here:

- [STM32F042 reference manual](https://www.st.com/resource/en/reference_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[2]](#id4)
- [STM32F042 data sheet](https://www.st.com/resource/en/datasheet/stm32f042k6.pdf) [[3]](#id6)

### Supported Features

The `nucleo_f042k6` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions.

#### Board connectors:

![Nucleo F042K6 connectors](../../../../_images/nucleo_f042k6_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA2/PA15 (ST-Link Virtual COM Port)
- I2C1 SCL/SDA : PB6/PB7 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PA4/PA5/PA6/PA7 (Arduino SPI)
- LD2 : PB3

For more details please refer to [STM32 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf) [[4]](#id8).

## Programming and Debugging

Nucleo F042K6 board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f042k6` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[5]](#id10) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F042K6

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f042k6 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f042k6 samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-f042k6.html](https://www.st.com/en/evaluation-tools/nucleo-f042k6.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/datasheet/stm32f042k6.pdf](https://www.st.com/resource/en/datasheet/stm32f042k6.pdf)

[[4](#id9)]

[https://www.st.com/resource/en/user\_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf)

[[5](#id11)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
