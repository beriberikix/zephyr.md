---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/nucleo_h7a3zi_q/doc/index.html
original_path: boards/arm/nucleo_h7a3zi_q/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ST Nucleo H7A3ZI-Q

## Overview

The STM32 Nucleo-144 boards offer combinations of performance and power that
provide an affordable and flexible way for users to build prototypes and try
out new concepts. For compatible boards, the SMPS (Switched-Mode Power Supply)
significantly reduces power consumption in Run mode.

The Arduino-compatible ST Zio connector expands functionality of the Nucleo
open development platform, with a wide choice of specialized Arduino\* Uno V3
shields.

The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK/V3E debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software
libraries and examples available with the STM32Cube MCU Package.

Key Features

- STM32 microcontroller in LQFP144 package
- USB OTG or full-speed device (depending on STM32 support)
- 3 user LEDs
- 2 user and reset push-buttons
- 32.768 kHz crystal oscillator
- Board connectors:

> - USB with Micro-AB
> - SWD
> - ST Zio connector including Arduino\* Uno V3
> - ST morpho

- Flexible power-supply options: ST-LINK USB VBUS or external sources.
- On-board ST-LINK/V3E debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port.
- Comprehensive free software libraries and examples available with the
  STM32Cube MCU package.
- Arm\* Mbed Enabled\* compliant (only for some Nucleo part numbers)

![Nucleo H7A3ZI-Q](../../../../_images/nucleo_h7a3zi_q.jpg)

More information about the board can be found at the [Nucleo H7A3ZI-Q website](https://www.st.com/en/evaluation-tools/nucleo-h7a3zi-q.html#overview).

## Hardware

Nucleo H7A3ZI-Q provides the following hardware components:

- STM32H7A3ZI in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- Chrom-ART Accelerator
- Hardware JPEG Codec
- 280 MHz max CPU frequency
- VDD from 1.62 V to 3.6 V
- 2 MB Flash
- ~1.4 Mbytes SRAM
- 32-bit timers(2)
- 16-bit timers(15)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(5)
- UART(5)
- USB OTG Full Speed and High Speed(1)
- CAN FD(2)
- SAI(2)
- SPDIF\_Rx(4)
- HDMI\_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO (up to 114) with external interrupt capability
- 16-bit ADC(2) with 24 channels / 3.6 MSPS
- 12-bit DAC with 1/2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution

### Supported Features

The Zephyr nucleo\_h7a3zi\_q board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| Backup SRAM | on-chip | Backup SRAM |
| USB OTG HS | on-chip | USB device |
| RNG | on-chip | True Random number generator |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
`boards/arm/nucleo_h7a3zi_q/nucleo_h7a3zi_q_defconfig`

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/um2408-stm32h7-nucleo144-boards-mb1363-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo H7A3ZI-Q board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- USART3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PE1
- LD3 : PB14
- ADC1\_INP15 : PA3 (Arduino analog, A0)

#### System Clock

Nucleo H7A3ZI-Q System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 96MHz, driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo H7A3ZI-Q board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to USART3. Default settings are 115200 8N1.

## Programming and Debugging

Applications for the `nucleo_h7a3zi_q` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

Nucleo H7A3ZI-Q board includes an ST-LINK/V3E embedded debug tool interface.

#### Flashing an application to Nucleo H7A3ZI-Q

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_h7a3zi_q samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_h7a3zi_q
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h7a3zi_q samples/hello_world
west debug
```
