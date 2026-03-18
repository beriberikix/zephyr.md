---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nucleo_f103rb/doc/index.html
original_path: boards/arm/nucleo_f103rb/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST Nucleo F103RB

## Overview

The STM32 Nucleo-64 development board with STM32F103RB MCU, supports Arduino and ST morpho connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption, and features.

The Arduino\* Uno V3 connectivity support and the ST morpho headers allow easy functionality
expansion of the STM32 Nucleo open development platform with a wide choice of
specialized shields.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

![Nucleo F103RB](../../../../_images/nucleo_f103rb.jpg)

More information about the board can be found at the [Nucleo F103RB website](https://www.st.com/en/evaluation-tools/nucleo-f103rb.html) [[1]](#id1).

## Hardware

Nucleo F103RB provides the following hardware components:

- STM32 microcontroller in QFP64 package
- Two types of extension resources:

  - Arduino\* Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- ARM\* mbed\*
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
- Support of wide choice of Integrated Development Environments (IDEs) including:

  - IAR
  - ARM Keil
  - GCC-based IDEs

More information about STM32F103RB can be found here:

- [STM32F103 reference manual](https://www.st.com/resource/en/reference_manual/cd00171190.pdf) [[2]](#id3)
- [STM32F103 data sheet](https://www.st.com/resource/en/datasheet/stm32f103rb.pdf) [[3]](#id5)

### Supported Features

The Zephyr nucleo\_f103rb board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| WATCHDOG | on-chip | independent watchdog |
| ADC | on-chip | ADC Controller |
| DMA | on-chip | Direct Memory Access |
| die-temp | on-chip | die temperature sensor |
| COUNTER | on-chip | rtc |
| RTC | on-chip | rtc |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/nucleo_f103rb/nucleo_f103rb_defconfig`

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![Nucleo F103RB connectors](../../../../_images/nucleo_f103rb_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PA10
- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual COM Port)
- SPI1 NSS/SCK/MISO/MOSI : PB6/PA5/PA6/PA7 (Arduino SPI)
- SPI2 SCK/MISO/MOSI : PB12/PB13/PB14/PB15
- I2C1 SDA/SCL: PB9/PB8 (Arduino I2C)
- PWM1\_CH1: PA8
- USER\_PB : PC13
- LD1 : PA5

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf) [[4]](#id7).

## Programming and Debugging

Applications for the `nucleo_f103rb` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo F103RB board includes an ST-LINK/V2-1 embedded debug tool interface.
This interface is supported by the openocd version included in the Zephyr SDK.

#### Flashing an application to Nucleo F103RB

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f103rb samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f103rb samples/basic/blinky
west debug
```

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/nucleo-f103rb.html](https://www.st.com/en/evaluation-tools/nucleo-f103rb.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/cd00171190.pdf](https://www.st.com/resource/en/reference_manual/cd00171190.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/datasheet/stm32f103rb.pdf](https://www.st.com/resource/en/datasheet/stm32f103rb.pdf)

[[4](#id8)]

[https://www.st.com/resource/en/user\_manual/dm00105823.pdf](https://www.st.com/resource/en/user_manual/dm00105823.pdf)
