---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f303k8/doc/index.html
original_path: boards/st/nucleo_f303k8/doc/index.html
---

# Nucleo F303K8

Board Overview

[![../../../../_images/nucleo_f303k8.jpg](../../../../_images/nucleo_f303k8.jpg)
](../../../../_images/nucleo_f303k8.jpg)

Nucleo F303K8

Name:
:   `nucleo_f303k8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f303x8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f303k8/doc/index.rst/../..)

## Overview

The Nucleo F303K8 board features an ARM Cortex-M4 based STM32F303K8
mixed-signal MCU with FPU and DSP instructions capable of running at 72 MHz.
Here are some highlights of the Nucleo F303K8 board:

- STM32 microcontroller in LQFP32 package
- one type of extension resources:
- Arduino™ Nano V3 connectivity support
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:
- 5 V from ST-LINK/V2-1 USB VBUS
- External power sources: 3.3 V, 5V and 7 - 12 V
- One user LED
- One push-buttons: RESET

More information about the board can be found at the [Nucleo F303K8 website](https://www.st.com/en/evaluation-tools/nucleo-F303K8.html),
and in the [STM32 Nucleo-32 board User Manual](https://www.st.com/resource/en/user_manual/dm00231744-stm32-nucleo32-boards-mb1180-stmicroelectronics.pdf).

## Hardware

The Nucleo F303K8 provides the following hardware components:

- STM32F303K8T6 in LQFP32 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 72 MHz max CPU frequency
- VDD from 2.0 V to 3.6 V
- 64 KB Flash
- 12 KB SRAM
- RTC
- Advanced-control Timer
- General Purpose Timers (5)
- Basic Timer (2)
- Watchdog Timers (2)
- PWM channels (12)
- SPI/I2S (1)
- I2C (1)
- USART/UART (2)
- CAN (1)
- GPIO with external interrupt capability
- DMA channels (7)
- Capacitive sensing channels (18)
- 12-bit ADC with 21 channels
- 12-bit D/A converter
- Analog comparator (3)
- Op amp

More information about the STM32F303K8 can be found here:

- [STM32F303K8 on www.st.com](https://www.st.com/en/microcontrollers/stm32F303K8.html)
- [STM32F303K8 reference manual](https://www.st.com/resource/en/reference_manual/dm00043574-stm32f303xbcde-stm32f303x68-stm32f328x8-stm32f358xc-stm32f398xe-advanced-armbased-mcus-stmicroelectronics.pdf)
- [STM32F303K8 datasheet](https://www.st.com/resource/en/datasheet/stm32f303k8.pdf)

### Supported Features

The `nucleo_f303k8` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The Nucleo F303K8 Board has 1 GPIO controller. This controllers is responsible
for input/output, pull-up, etc.

#### Board connectors:

![Nucleo F303K8 connectors](../../../../_images/nucleo_f303k8_pinout.jpg)

#### Default Zephyr Peripheral Mapping:

The Nucleo F303K8 board features an Arduino Zero V3 connector. Board is configured as follows:

- UART\_2 TX/RX : PA2/PA15 (ST-Link Virtual Port Com)
- I2C1 SCL/SDA : PB7/PB6
- SPI1 CS/SCK/MISO/MOSI : PA\_4/PA\_5/PA\_6/PA\_7
- LD2 : PB3

#### System Clock

The Nucleo F303K8 System Clock can be driven by an internal or
external oscillator, as well as by the main PLL clock. By default the
System Clock is driven by the PLL clock at 72 MHz. The input to the
PLL is an 8 MHz internal clock supply.

#### Serial Port

The Nucleo F303K8 board has 2 UARTs. The Zephyr console output is assigned
to UART2. Default settings are 115200 8N1.

## Programming and Debugging

The Nucleo F303K8 board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```
