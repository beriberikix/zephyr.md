---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f302r8/doc/index.html
original_path: boards/st/nucleo_f302r8/doc/index.html
---

# Nucleo F302R8

Board Overview

[![../../../../_images/nucleo_f302r8.jpg](../../../../_images/nucleo_f302r8.jpg)
](../../../../_images/nucleo_f302r8.jpg)

Nucleo F302R8

Name:
:   `nucleo_f302r8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f302x8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f302r8/doc/index.rst/../..)

## Overview

The Nucleo F302R8 board features an ARM Cortex-M4 based STM32F302R8
mixed-signal MCU with FPU and DSP instructions capable of running at 72 MHz.
Here are some highlights of the Nucleo F302R8 board:

- STM32 microcontroller in LQFP64 package
- LSE crystal: 32.768 kHz crystal oscillator
- Two types of extension resources:

  - Arduino\* Uno V3 connectors
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector
- One user LED
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo F302R8 website](https://www.st.com/en/evaluation-tools/nucleo-f302r8.html),
and in the [STM32 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/dm00105823.pdf).

## Hardware

The Nucleo F302R8 provides the following hardware components:

- STM32F302R8T6 in QFP64 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 72 MHz max CPU frequency
- VDD from 2.0 V to 3.6 V
- 64 KB Flash
- 16 KB SRAM
- RTC
- Advanced-control Timer
- General Purpose Timers (4)
- Basic Timer
- Watchdog Timers (2)
- PWM channels (18)
- SPI/I2S (2)
- I2C (3)
- USART/UART (3/3)
- USB 2.0 FS with on-chip PHY
- CAN (2)
- GPIO with external interrupt capability
- DMA channels (7)
- Capacitive sensing channels (18)
- 12-bit ADC with 15 channels
- 12-bit D/A converter
- Analog comparator (3)
- Op amp

More information about the STM32F302R8 can be found here:

- [STM32F302R8 on www.st.com](https://www.st.com/en/microcontrollers/stm32f302r8.html)
- [STM32F302R8 reference manual](https://www.st.com/resource/en/reference_manual/dm00094349.pdf)
- [STM32F302R8 datasheet](https://www.st.com/resource/en/datasheet/stm32f302r8.pdf)

### Supported Features

The `nucleo_f302r8` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

The Nucleo F302R8 Board has 5 GPIO controllers. These controllers are
responsible for pin muxing, input/output, pull-up, etc.

#### Board connectors:

![Nucleo F302R8 connectors](../../../../_images/nucleo_f302r8_connectors.jpg)

#### Default Zephyr Peripheral Mapping:

The Nucleo F302R8 board features an Arduino Uno V3 connector and a ST
morpho connector. Board is configured as follows:

- UART\_2 TX/RX : PA2/PA3 (ST-Link Virtual Port Com)
- UART\_3 TX/RX : PC10/PC11
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI2 CS/SCK/MISO/MOSI : PB6/PB13/PB14/P15 (Arduino SPI)
- PWM\_2\_CH2 : PA0
- USER\_PB : PC13
- LD2 : PB13

#### System Clock

The Nucleo F302R8 System Clock can be driven by an internal or
external oscillator, as well as by the main PLL clock. By default the
System Clock is driven by the PLL clock at 72 MHz. The input to the
PLL is an 8 MHz external clock supplied by the processor of the
on-board ST-LINK/V2-1 debugger/programmer.

#### Serial Port

The Nucleo F302R8 board has 3 UARTs. The Zephyr console output is assigned
to UART2. Default settings are 115200 8N1.

## Programming and Debugging

The Nucleo F302R8 board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```
