---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32u5g9j_dk2/doc/index.html
original_path: boards/st/stm32u5g9j_dk2/doc/index.html
---

# STM32U5G9J Discovery Kit

Board Overview

[![../../../../_images/stm32u5g9j_dk2.webp](../../../../_images/stm32u5g9j_dk2.webp)
](../../../../_images/stm32u5g9j_dk2.webp)

STM32U5G9J Discovery Kit

Name:
:   `stm32u5g9j_dk2`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u5g9xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32u5g9j_dk2/doc/index.rst/../..)

## Overview

The STM32U5G9J-DK2 Discovery kit is a complete demonstration and development
platform for the STM32U5G9ZJT6Q microcontroller, featuring an Arm® Cortex®‑M33
core with Arm® TrustZone®.

Leveraging the innovative ultra-low power-oriented features, 3 Mbytes of
embedded SRAM, 4 Mbytes of embedded flash memory, and rich graphics features,
the STM32U5G9J-DK2 Discovery kit enables users to prototype applications
with state-of-the-art energy efficiency, as well as providing stunning and
optimized graphics rendering with the support of a 2.5D Neo-Chrom accelerator,
chrom-ART Accelerator, and Chrom-GRC™ MMU.

The STM32U5G9J-DK2 Discovery kit integrates a full range of hardware features
that help the user evaluate all the peripherals, such as a 5” RGB 800x480 pixels
TFT colored LCD module with a 24‑bit RGB interface and capacitive touch panel,
USB Type-C® HS, Octo‑SPI flash memory device, ARDUINO®, and STLINK-V3EC
(USART console).

The STM32U5G9J-DK2 Discovery kit integrates an STLINK-V3EC embedded in-circuit
debugger and programmer for the STM32 microcontroller with a USB Virtual COM
port bridge and comes with the STM32CubeU5 MCU Package, which provides an STM32
comprehensive software HAL library as well as various software examples.

More information about the board can be found at the [STM32U5G9J-DK2 website](https://www.st.com/en/evaluation-tools/stm32u5g9j-dk2.html).
More information about STM32U5G9ZJT6Q can be found here:

- [STM32U5G9ZJ on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u5g9zj.html)
- [STM32U5 Series reference manual](https://www.st.com/resource/en/reference_manual/rm0456-stm32u5-series-armbased-32bit-mcus-stmicroelectronics.pdf)
- [STM32U5Gxxx datasheet](https://www.st.com/resource/en/datasheet/stm32u5g7vj.pdf)

### Supported Features

The `stm32u5g9j_dk2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

For more details please refer to [STM32U5G9J-DK2 board User Manual](https://www.st.com/resource/en/user_manual/um3223-discovery-kit-with-stm32u5g9zj-mcu-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX/RX : PA9/PA10 (ST-Link Virtual Port Com)
- USART\_2 TX/RX : PA2/PA3
- LD2 : PD2
- LD3 : PD4
- User Button: PC13
- I2C1 SCL/SDA : PG14/PG13
- I2C2 SCL/SDA : PF1/PF0
- SPI1 SCK/MISO/MOSI/CS : PA5/PA6/PB5/PA3
- ADC1 : channel5 PA0, channel12 PA7
- ADC4 : channel4 PC3
- SDMMC1/LTDC conflicting pins: PC6, PC7, PC8, PC9, PB9
- SDMMC1\_CK : PC12
- SDMMC1\_CMD : PD2
- SDMMC1\_D0 : PC8
- SDMMC1\_D1 : PC9
- SDMMC1\_D2 : PC10
- SDMMC1\_D3 : PC11
- SDMMC1\_D4 : PB8
- SDMMC1\_D5 : PB9
- SDMMC1\_D6 : PC6
- SDMMC1\_D7 : PC7
- LTDC\_R0 : PC6
- LTDC\_R1 : PC7
- LTDC\_R2 : PE15
- LTDC\_R3 : PD8
- LTDC\_R4 : PD9
- LTDC\_R5 : PD10
- LTDC\_R6 : PD11
- LTDC\_R7 : PD12
- LTDC\_G0 : PC8
- LTDC\_G1 : PC9
- LTDC\_G2 : PE9
- LTDC\_G3 : PE10
- LTDC\_G4 : PE11
- LTDC\_G5 : PE12
- LTDC\_G6 : PE13
- LTDC\_G7 : PE14
- LTDC\_B0 : PB9
- LTDC\_B1 : PB2
- LTDC\_B2 : PD14
- LTDC\_B3 : PD15
- LTDC\_B4 : PD0
- LTDC\_B5 : PD1
- LTDC\_B6 : PE7
- LTDC\_B7 : PE8
- LTDC\_DE : PD6
- LTDC\_CLK : PD3
- LTDC\_HSYNC : PE0
- LTDC\_VSYNC : PD13

### System Clock

The STM32U5G9J-DK Discovery 2 kit relies on an HSE oscillator (16 MHz crystal)
and an LSE oscillator (32.768 kHz crystal) as clock references.
Using the HSE (instead of HSI) is mandatory to manage the DSI interface for
the LCD module and the USB high‑speed interface.

### Serial Port

The STM32U5G9J Discovery 2 kit has up to 4 USARTs, 2 UARTs, and 1 LPUART.
The Zephyr console output is assigned to USART1 which connected to the onboard
ST-LINK/V3.0. Virtual COM port interface. Default communication settings are
115200 8N1.

## Programming and Debugging

The `stm32u5g9j_dk2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

STM32U5G9J Discovery 2 kit includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash and debug the board using various tools.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to STM32U5G9J\_DK2

Connect the STM32U5G9J Discovery 2 board to your host computer using the USB
port, then run a serial host program to connect with your Discovery
board. For example:

```shell
$ minicom -D /dev/ttyACM0 -b 115200
```

Then, build and flash in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32u5g9j_dk2 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! stm32u5g9j_dk2
```

### Debugging

Default debugger for this board is openocd. It could be used in the usual way
with “west debug” command.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32u5g9j_dk2 samples/basic/blinky
west debug
```
