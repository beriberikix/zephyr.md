---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32g0316_disco/doc/index.html
original_path: boards/st/stm32g0316_disco/doc/index.html
---

# STM32G0316 Discovery

Board Overview

[![../../../../_images/stm32g0316_disco.jpg](../../../../_images/stm32g0316_disco.jpg)
](../../../../_images/stm32g0316_disco.jpg)

STM32G0316 Discovery

Name:
:   `stm32g0316_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32g031xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32g0316_disco/doc/index.rst/../..)

## Overview

The STM32G0316-DISCO Discovery kit helps to discover features of STM32G0 in SO8 package.
This discovery kit offers an SO8 to DIL8 module designed with the STM32G031J6 microcontroller
and allows the user to develop applications. It includes an on-board ST-LINK/V2-1 to debug
and program the embedded STM32 microcontroller.

## Hardware

- STM32G031J6 Arm® Cortex®-M0+ core-based microcontroller,
  featuring 32 Kbytes of Flash memory and 8 Kbytes of SRAM, in an SO8 package
- 1 user LED
- 1 reset/user push-button
- Individual and breakable STM32 SO8 to DIL8 module
- ST-LINK Micro-B USB connector
- DIL8 socket to ease programming of the STM32 MCU
- On-board ST-LINK/V2-1 debugger/programmer

For more information about the STM32G03x SoC and the STM32G0316-DISCO board, see these ST reference documents:

- [STM32G031J6 website](https://www.st.com/en/microcontrollers-microprocessors/stm32g031j6.html)
- [STM32G031 datasheet](https://www.st.com/resource/en/datasheet/stm32g031j6.pdf)
- [STM32G0x1 reference manual](https://www.st.com/resource/en/reference_manual/dm00371828.pdf)
- [STM32G0316-DISCO website](https://www.st.com/en/evaluation-tools/stm32g0316-disco.html)

### Supported Features

The `stm32g0316_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

Due to the small number of I/O pins on the SO8 package, multiple die I/Os are bonded
to the same package pins to maximize the number of peripherals which can be used.
Care must be taken not to set two I/Os which are connected together to conflicting
states (e.g. both as outputs, one low, the other high).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PA9/PB7 (pins 5/1)
- USER\_PB : PA0 (pin 4)
- LD2 : PA12 (pin 6)

## Programming and Debugging

The STM32G0316-DISCO board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `stm32g0316_disco` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to the STM32G0316-DISCO

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b stm32g0316_disco samples/basic/blinky
west flash
```

You should see the LED blinking every second.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32g0316_disco samples/hello_world
west debug
```
