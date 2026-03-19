---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f334r8/doc/index.html
original_path: boards/st/nucleo_f334r8/doc/index.html
---

# Nucleo F334R8

Board Overview

[![../../../../_images/nucleo_f334r8.jpg](../../../../_images/nucleo_f334r8.jpg)
](../../../../_images/nucleo_f334r8.jpg)

Nucleo F334R8

Name:
:   `nucleo_f334r8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f334x8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f334r8/doc/index.rst/../..)

## Overview

STM32 Nucleo-64 development board with STM32F334R8 MCU, supports Arduino and ST morpho connectivity.

The STM32 Nucleo board provides an affordable and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption and features.

The Arduino\* Uno V3 connectivity support and the ST morpho headers allow easy functionality
expansion of the STM32 Nucleo open development platform with a wide choice of
specialized shields.

The STM32 Nucleo board does not require any separate probe as it integrates the ST-LINK/V2-1
debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

More information about the board can be found at the [Nucleo F334R8 website](https://www.st.com/en/evaluation-tools/nucleo-f334r8.html) [[1]](#id2).

## Hardware

Nucleo F334R8 provides the following hardware components:

- STM32 microcontroller in QFP64 package
- Two types of extension resources:

  - Arduino\* Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:

  - Selection-mode switch to use the kit as a standalone ST-LINK/V2-1
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs:

  - USB communication (LD1), user LED (LD2), power LED (LD3)
- Two push-buttons: USER and RESET
- USB re-enumeration capability. Three different interfaces supported on USB:

  - Virtual COM port
  - Mass storage
  - Debug port

More information about STM32F334R8 can be found in the
[STM32F334 reference manual](https://www.st.com/resource/en/reference_manual/dm00093941.pdf) [[2]](#id4)

### Supported Features

The `nucleo_f334r8` board supports the hardware features listed below.

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
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![Nucleo F334R8 connectors](../../../../_images/nucleo_f334r8_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- UART\_3 TX/RX : PB10/PB11
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 CS/SCK/MISO/MOSI : PB6/PA5/PA6/PA7 (Arduino SPI)
- PWM\_1\_CH1 : PA8
- USER\_PB : PC13
- LD2 : PA5

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf) [[3]](#id6).

## Programming and Debugging

Nucleo F334R8 board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f334r8` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

#### Flashing an application to Nucleo F334R8

Connect the Nucleo F334R8 to your host computer using the USB port,
then build and flash an application. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f334r8 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for
the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f334r8 samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-f334r8.html](https://www.st.com/en/evaluation-tools/nucleo-f334r8.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00093941.pdf](https://www.st.com/resource/en/reference_manual/dm00093941.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/dm00105823.pdf](https://www.st.com/resource/en/user_manual/dm00105823.pdf)

[[4](#id9)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
