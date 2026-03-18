---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_f031k6/doc/index.html
original_path: boards/st/nucleo_f031k6/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo F031K6

## Overview

The STM32 Nucleo-32 development board with STM32F031K6 MCU, supports Arduino nano connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption and features.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

![Nucleo F031k6](../../../../_images/nucleo_f031k6.jpg)

More information about the board can be found at the [Nucleo F031K6 website](https://www.st.com/en/evaluation-tools/nucleo-f031k6.html) [[1]](#id1).

## Hardware

Nucleo F031K6 provides the following hardware components:

- STM32 microcontroller in LQFP32 package
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
- Three LEDs:

  - USB communication (LD1), user LED (LD2), power LED (LD3)
- reset push button

More information about STM32F031K6 can be found here:

- [STM32F031 reference manual](https://www.st.com/resource/en/reference_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[2]](#id3)
- [STM32F031 data sheet](https://www.st.com/resource/en/datasheet/stm32f031k6.pdf) [[3]](#id5)

### Supported Features

The Zephyr nucleo\_f031k6 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| I2C | on-chip | i2c controller |
| SPI | on-chip | spi controller |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in
[boards/st/nucleo\_f031k6/nucleo\_f031k6\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f031k6/nucleo_f031k6_defconfig)

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions.

#### Board connectors:

![Nucleo F031K6 connectors](../../../../_images/nucleo_f031k6_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA2/PA15 (ST-Link Virtual COM Port)
- I2C1 SCL/SDA : PB6/PB7 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PA4/PA5/PA6/PA7 (Arduino SPI)
- LD2 : PB3

For more details please refer to [STM32 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf) [[4]](#id7).

## Programming and Debugging

Applications for the `nucleo_f031k6` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo F031K6 board includes an ST-LINK/V2-1 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to Nucleo F030R8

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f031k6 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f031k6 samples/basic/blinky
west debug
```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/nucleo-f031k6.html](https://www.st.com/en/evaluation-tools/nucleo-f031k6.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/dm00031936-stm32f0x1stm32f0x2stm32f0x8-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/datasheet/stm32f031k6.pdf](https://www.st.com/resource/en/datasheet/stm32f031k6.pdf)

[[4](#id8)]

[https://www.st.com/resource/en/user\_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf)
