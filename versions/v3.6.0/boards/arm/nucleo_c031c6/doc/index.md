---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nucleo_c031c6/doc/index.html
original_path: boards/arm/nucleo_c031c6/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST Nucleo C031C6

## Overview

The STM32 Nucleo-64 development board with STM32C031C6 MCU, supports Arduino and ST morpho connectivity.

The STM32 Nucleo board provides an affordable, and flexible way for users to try out new concepts,
and build prototypes with the STM32 microcontroller, choosing from the various
combinations of performance, power consumption and features.

The STM32 Nucleo board integrates the ST-LINK/V2-1 debugger and programmer.

The STM32 Nucleo board comes with the STM32 comprehensive software HAL library together
with various packaged software examples.

![Nucleo C031C6](../../../../_images/nucleo_c031c6.jpg)

More information about the board can be found at the [Nucleo C031C6 website](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html) [[1]](#id1).

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
[STM32C0x1 reference manual](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf) [[2]](#id3)

### Supported Features

The Zephyr nucleo\_c031c6 board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| CLOCK | on-chip | reset and clock control |
| RTC | on-chip | counter |
| IWDG | on-chip | independent watchdog |
| WWDG | on-chip | window watchdog |
| PWM | on-chip | pwm |
| ADC | on-chip | ADC Controller |
| die-temp | on-chip | die temperature sensor |
| I2C | on-chip | i2c |
| DMA | on-chip | Direct Memory Access |

Other hardware features are not yet supported in this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/nucleo_c031c6/nucleo_c031c6_defconfig`

### Connections and IOs

Each of the GPIO pins can be configured by software as output (push-pull or open-drain), as
input (with or without pull-up or pull-down), or as peripheral alternate function. Most of the
GPIO pins are shared with digital or analog alternate functions. All GPIOs are high current
capable except for analog inputs.

#### Default Zephyr Peripheral Mapping:

- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- LD4 : PA5

For more details please refer to [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf) [[3]](#id5).

## Programming and Debugging

Applications for the `nucleo_c031c6` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo C031C6 board includes an ST-LINK/V2-1 embedded debug tool interface.

#### Flashing an application to Nucleo C031C6

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_c031c6 samples/basic/blinky
west flash
```

You will see the LED blinking every second.

## References

[[1](#id2)]

[https://www.st.com/en/evaluation-tools/nucleo-c031c6.html](https://www.st.com/en/evaluation-tools/nucleo-c031c6.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/user\_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf](https://www.st.com/resource/en/user_manual/um2953-stm32c0-nucleo64-board-mb1717-stmicroelectronics.pdf)
