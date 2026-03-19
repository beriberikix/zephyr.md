---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_c031c6/doc/index.html
original_path: boards/st/nucleo_c031c6/doc/index.html
---

# Nucleo C031C6

Board Overview

[![../../../../_images/nucleo_c031c6.jpg](../../../../_images/nucleo_c031c6.jpg)
](../../../../_images/nucleo_c031c6.jpg)

Nucleo C031C6

Name:
:   `nucleo_c031c6`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32c031xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_c031c6/doc/index.rst/../..)

## Overview

The STM32 Nucleo-64 development board with STM32C031C6 MCU, supports Arduino and ST morpho connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption and features.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

More information about the board can be found at the [Nucleo C031C6 website](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html) [[1]](#id2).

## Hardware

Nucleo C031C6 provides the following hardware components:

- STM32 microcontroller in 48-pin package featuring 32 Kbytes of Flash memory
  and 12 Kbytes of SRAM.
- Extension resource:

  - Arduino\* Uno V3 connectivity
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Current consumption measurement (IDD)
- Four LEDs:

  - USB communication (LD1), USB power fault LED (LD2), power LED (LD3),
    user LED (LD4)
- Two push-button: USER and RESET
- USB re-enumeration capability. Three different interfaces supported on USB:

  - Virtual COM port
  - Mass storage
  - Debug port

More information about STM32C031C6 can be found here:
[STM32C0x1 reference manual](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf) [[2]](#id4)

### Supported Features

The `nucleo_c031c6` board supports the hardware features listed below.

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

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- LD4 : PA5

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf) [[3]](#id6).

## Programming and Debugging

Nucleo C031C6 board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_c031c6` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

#### Flashing an application to Nucleo C031C6

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_c031c6 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-c031c6.html](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf)

[[4](#id9)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
