---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_f091rc/doc/index.html
original_path: boards/st/nucleo_f091rc/doc/index.html
---

# Nucleo F091RC

Board Overview

[![../../../../_images/nucleo_f091rc.jpg](../../../../_images/nucleo_f091rc.jpg)
](../../../../_images/nucleo_f091rc.jpg)

Nucleo F091RC

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f091xc

## Overview

The STM32 Nucleo-64 development board with STM32F091RC MCU, supports Arduino and ST morpho connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption, and features.

The Arduino\* Uno V3 connectivity support and the ST morpho headers allow easy functionality
expansion of the STM32 Nucleo open development platform with a wide choice of
specialized shields.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

More information about the board can be found at the [Nucleo F091RC website](https://www.st.com/en/evaluation-tools/nucleo-f091rc.html) [[1]](#id2).

## Hardware

Nucleo F091RC provides the following hardware components:

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

More information about STM32F091RC can be found in the
[STM32F091 reference manual](https://www.st.com/resource/en/reference_manual/dm00031936.pdf) [[2]](#id4)

### Supported Features

The Zephyr nucleo\_f091rc board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| FLASH | on-chip | flash memory |
| WATCHDOG | on-chip | independent watchdog |
| PWM | on-chip | pwm |
| COUNTER | on-chip | rtc |
| I2C | on-chip | i2c controller |
| SPI | on-chip | SPI controller |
| CAN | on-chip | CAN controller |
| ADC | on-chip | ADC controller |
| DAC | on-chip | DAC controller |
| DMA | on-chip | Direct Memory Access |
| die-temp | on-chip | die temperature sensor |
| RTC | on-chip | rtc |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in
[boards/st/nucleo\_f091rc/nucleo\_f091rc\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f091rc/nucleo_f091rc_defconfig)

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Board connectors:

![Nucleo F091RC connectors](../../../../_images/nucleo_f091rc_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PB6/PB7
- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual COM Port)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C2 SCL/SDA : PA11/PA12 (disabled by default, uses same pins as CAN)
- CAN RX/TX : PA11/PA12
- SPI1 SCK/MISO/MOSI : PA5/PA6/PA7 (Arduino SPI)
- SPI2 SCK/MISO/MOSI : PB13/PB14/PB15
- USER\_PB : PC13
- LD2 : PA5
- DAC\_OUT1 : PA4
- PWM\_2\_CH1 : PA5 (might conflict with SPI1)

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf) [[3]](#id6).

## Programming and Debugging

Nucleo F091RC board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f091rc` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id8) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F091RC

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f091rc samples/basic/blinky
west flash
```

You will see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f091rc samples/hello_world
west debug
```

## References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/nucleo-f091rc.html](https://www.st.com/en/evaluation-tools/nucleo-f091rc.html)

[[2](#id5)]

[https://www.st.com/resource/en/reference\_manual/dm00031936.pdf](https://www.st.com/resource/en/reference_manual/dm00031936.pdf)

[[3](#id7)]

[https://www.st.com/resource/en/user\_manual/dm00105823.pdf](https://www.st.com/resource/en/user_manual/dm00105823.pdf)

[[4](#id9)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
