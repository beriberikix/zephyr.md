---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/mikroe/stm32_m4_clicker/doc/index.html
original_path: boards/mikroe/stm32_m4_clicker/doc/index.html
---

# STM32 M4 Clicker

Board Overview

[![../../../../_images/stm32_m4_clicker.webp](../../../../_images/stm32_m4_clicker.webp)
](../../../../_images/stm32_m4_clicker.webp)

STM32 M4 Clicker

Vendor:
:   MikroElektronika d.o.o.

Architecture:
:   arm

SoC:
:   stm32f415xx

## Overview

The Mikroe STM32 M4 Clicker development board contains a STMicroelectronics
Cortex-M4 based STM32F415RG Microcontroller operating at up to 168 MHz with
1 MB of Flash memory and 192 KB of SRAM.

## Hardware

The STM32 M4 Clicker board contains a USB connector, two LEDs, two push
buttons, and a reset button. It features a mikroBUS socket for interfacing
with external electronics. For more information about the development
board see the [STM32 M4 Clicker website](https://www.mikroe.com/clicker-stm32f4) [[1]](#id2).

### Supported Features

The `mikroe_stm32_m4_clicker` board target supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| GPIO | on-chip | GPIO output GPIO input |
| USB | on-chip | USB |

Other hardware features have not yet been enabled for this board.

The default configuration can be found in the defconfig file:
[boards/mikroe/stm32\_m4\_clicker/mikroe\_stm32\_m4\_clicker\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/stm32_m4_clicker/mikroe_stm32_m4_clicker_defconfig).

## Programming and debugging

### Building & Flashing

You can build and flash an application in the usual way (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_stm32_m4_clicker samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b mikroe_stm32_m4_clicker samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.mikroe.com/clicker-stm32f4](https://www.mikroe.com/clicker-stm32f4)
