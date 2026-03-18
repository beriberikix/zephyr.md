---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_l031k6/doc/index.html
original_path: boards/st/nucleo_l031k6/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo L031K6

## Overview

The STM32 Nucleo-32 development board with STM32L031K6 MCU, supports Arduino Nano V3 connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption, and features.

The Arduino\* Nano V3 connectivity support allow easy functionality
expansion of the STM32 Nucleo open development platform with a wide choice of
specialized shields.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

![Nucleo L031K6](../../../../_images/nucleo_l031k6.jpg)

More information about the board can be found at the [Nucleo L031K6 website](https://www.st.com/en/evaluation-tools/nucleo-l031k6.html) [[1]](#id1).

## Hardware

Nucleo L031K6 provides the following hardware components:

- STM32 microcontroller in LQFP32 package
- Extension resource:

  - Arduino\* Nano V3 connectivity
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector:

  - Selection-mode switch to use the kit as a standalone ST-LINK/V2-1
- Flexible board power supply:

  - USB VBUS or external source (3.3V, 5V, 7 - 12V)
  - Power management access point
- Three LEDs:

  - USB communication (LD1), user LED (LD2), power LED (LD3)
- One push-button: RESET
- USB re-enumeration capability. Three different interfaces supported on USB:

  - Virtual COM port
  - Mass storage
  - Debug port

More information about STM32L031K6 can be found in the
[STM32L0x1 reference manual](https://www.st.com/resource/en/reference_manual/dm00108282-ultralowpower-stm32l0x1-advanced-armbased-32bit-mcus-stmicroelectronics.pdf) [[2]](#id3)

### Supported Features

The Zephyr nucleo\_l031k6 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| I2C | on-chip | i2c controller |
| SPI | on-chip | spi controller |
| EEPROM | on-chip | eeprom |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_l031k6/nucleo\_l031k6\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l031k6/nucleo_l031k6_defconfig)

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA15 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PA9/PA10 (Arduino I2C)
- SPI1 SCK/MISO/MOSI : PA5/PA6/PA7 (Arduino SPI)
- LD2 : PB3

For more details please refer to [STM32 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf) [[3]](#id5).

## Programming and Debugging

Applications for the `nucleo_l031k6` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo L031K6 board includes an ST-LINK/V2-1 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to Nucleo L031K6

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l031k6 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l031k6 samples/hello_world
west debug
```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/nucleo-l031k6.html](https://www.st.com/en/evaluation-tools/nucleo-l031k6.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/dm00108282-ultralowpower-stm32l0x1-advanced-armbased-32bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/dm00108282-ultralowpower-stm32l0x1-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/user\_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf)
