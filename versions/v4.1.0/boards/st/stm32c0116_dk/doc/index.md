---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32c0116_dk/doc/index.html
original_path: boards/st/stm32c0116_dk/doc/index.html
---

# STM32C0116-DK Discovery Kit

Board Overview

[![../../../../_images/stm32c0116_dk.jpg](../../../../_images/stm32c0116_dk.jpg)
](../../../../_images/stm32c0116_dk.jpg)

STM32C0116-DK Discovery Kit

Name:
:   `stm32c0116_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32c011xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32c0116_dk/doc/index.rst/../..)

## Overview

The STM32C0116-DK Discovery kit helps to discover features of the STM32C0 Series
microcontroller in a UFQFPN20 package. This Discovery kit features one UFQFPN20
to DIL20 module designed with the STM32C011F6 microcontroller and allows the user to develop
and share applications. It includes an on-board ST-LINK/V2-1 to debug and program the embedded
STM32 microcontroller. Important board features include:

More information about the board can be found at the [STM32C0116-DK website](https://www.st.com/en/evaluation-tools/stm32c0116-dk.html).

## Hardware

The STM32C0116-DK Discovery kit provides the following hardware components:

- STM32C011F6 microcontroller with 32 Kbytes of Flash memory and 6 Kbytes of RAM, in a UFQFPN20 package
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration capability: mass storage and debug port
- User LED
- Reset push-button
- 5 way joystick using a single ADC input pin
- Individual STM32 UFQFPN20 to DIL20 module
- Board connectors:

  - USB Micro-B
  - DIL20 socket
  - Dedicated LCD footprint
  - Grove (UART)
  - 2 x 10 pin headers for MCU daughterboard
  - Extension connectors

More information about STM32C011F6 can be found here:

- [STM32C011F6 on www.st.com](https://www.st.com/resource/en/datasheet/stm32c011f6.pdf)
- [STM32C0x1 reference manual](https://www.st.com/resource/en/reference_manual/rm0490-stm32c0x1-advanced-armbased-64bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32c0116_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

STM32C0116-DK Discovery kit has 4 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32C0116-DK board User Manual](https://www.st.com/resource/en/user_manual/um2970-discovery-kit-with-stm32c011f6-mcu-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

The STM32C0116 Discovery board is configured as follows:

- UART\_2 TX/RX : PA2/PA3
- UART\_1 TX/RX : PA9/PA10 (ST-Link Virtual Port Com)
- PWM\_1\_CH3 : PB6
- ADC1\_CH8 : PA8
- LD3 : PB6

## Programming and Debugging

STM32C0116-DK Discovery kit includes an ST-LINK/V2 embedded debug tool interface.

Applications for the `stm32c0116_dk` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner jlink
```

#### Flashing an application to STM32C0116-DK

First, connect the STM32C0116 Discovery kit to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32c0116_dk samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

You should see the following message on the console:

```shell
Hello World! arm
```
