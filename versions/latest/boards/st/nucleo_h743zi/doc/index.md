---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/st/nucleo_h743zi/doc/index.html
original_path: boards/st/nucleo_h743zi/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# ST Nucleo H743ZI

## Overview

The STM32 Nucleo-144 boards offer combinations of performance and power that
provide an affordable and flexible way for users to build prototypes and try
out new concepts. For compatible boards, the SMPS (Switched-Mode Power Supply)
significantly reduces power consumption in Run mode.

The Arduino-compatible ST Zio connector expands functionality of the Nucleo
open development platform, with a wide choice of specialized Arduino\* Uno V3
shields.

The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK/V2-1 debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software
libraries and examples available with the STM32Cube MCU Package.

Key Features

- STM32 microcontroller in LQFP144 package
- Ethernet compliant with IEEE-802.3-2002 (depending on STM32 support)
- USB OTG or full-speed device (depending on STM32 support)
- 3 user LEDs
- 2 user and reset push-buttons
- 32.768 kHz crystal oscillator
- Board connectors:

> - USB with Micro-AB
> - SWD
> - Ethernet RJ45 (depending on STM32 support)
> - ST Zio connector including Arduino\* Uno V3
> - ST morpho

- Flexible power-supply options: ST-LINK USB VBUS or external sources.
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port.
- Comprehensive free software libraries and examples available with the
  STM32Cube MCU package.
- Arm\* Mbed Enabled\* compliant (only for some Nucleo part numbers)

![Nucleo H743ZI](../../../../_images/nucleo_h743zi.jpg)

More information about the board can be found at the [Nucleo H743ZI website](https://www.st.com/en/evaluation-tools/nucleo-h743zi.html).

## Hardware

Nucleo H743ZI provides the following hardware components:

- STM32H743ZI in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- Chrom-ART Accelerator
- Hardware JPEG Codec
- 480 MHz max CPU frequency
- VDD from 1.62 V to 3.6 V
- 2 MB Flash
- 1 MB SRAM
- High-resolution timer (2.1 ns)
- 32-bit timers(2)
- 16-bit timers(12)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(4)
- UART(4)
- USB OTG Full Speed and High Speed(1)
- USB OTG Full Speed(1)
- CAN FD(2)
- SAI(2)
- SPDIF\_Rx(4)
- HDMI\_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO (up to 114) with external interrupt capability
- 16-bit ADC(3) with 36 channels / 3.6 MSPS
- 12-bit DAC with 2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution

### Supported Features

The Zephyr nucleo\_h743zi board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| RTC | on-chip | counter |
| I2C | on-chip | i2c |
| PWM | on-chip | pwm |
| ADC | on-chip | adc |
| DAC | on-chip | DAC Controller |
| RNG | on-chip | True Random number generator |
| ETHERNET | on-chip | ethernet |
| SPI | on-chip | spi |
| Backup SRAM | on-chip | Backup SRAM |
| WATCHDOG | on-chip | independent watchdog |
| USB | on-chip | usb\_device |
| CAN/CANFD | on-chip | canbus |
| die-temp | on-chip | die temperature sensor |
| RTC | on-chip | rtc |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_h743zi/nucleo\_h743zi\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h743zi/nucleo_h743zi_defconfig)

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00244518.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo H743ZI board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- I2C : PB8, PB9
- ADC1\_INP15 : PA3
- DAC1\_OUT1 : PA4
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PB5 (Arduino SPI)
- CAN/CANFD : PD0, PD1

#### System Clock

Nucleo H743ZI System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 96MHz, driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo H743ZI board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to UART3. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB156` jumper on the back side of the board.

#### CAN, CANFD

Requires an external CAN or CANFD transceiver.

## Programming and Debugging

Applications for the `nucleo_h743zi` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Note

If using OpenOCD you will need a recent development version as the last
official release does not support H7 series yet. You can also choose the
`stm32cubeprogrammer` runner.

### Flashing

Nucleo H743ZI board includes an ST-LINK/V2-1 embedded debug tool interface.

#### Flashing an application to Nucleo H743ZI

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_h743zi samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_h743zi
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h743zi samples/hello_world
west debug
```
