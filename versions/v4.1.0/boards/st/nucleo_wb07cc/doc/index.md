---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_wb07cc/doc/index.html
original_path: boards/st/nucleo_wb07cc/doc/index.html
---

# Nucleo WB07CC

Board Overview

[![../../../../_images/nucleo_wb07cc.webp](../../../../_images/nucleo_wb07cc.webp)
](../../../../_images/nucleo_wb07cc.webp)

Nucleo WB07CC

Name:
:   `nucleo_wb07cc`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wb07

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wb07cc/doc/index.rst/../..)

## Overview

The Nucleo WB07CC board is a Bluetooth® Low Energy wireless and ultra-low-power
board featuring an ARM Cortex®-M0+ based STM32WB07CCV MCU, embedding a
powerful and ultra-low-power radio compliant with the Bluetooth® Low Energy
SIG specification v5.4.

More information about the board can be found on the [Nucleo WB07CC webpage](https://www.st.com/en/evaluation-tools/nucleo-wb07cc.html).

## Hardware

Nucleo WB07CC provides the following hardware components:

- STM32WB07CCV in VFQFPN32 package
- ARM® 32-bit Cortex®-M0+ CPU
- 64 MHz maximal CPU frequency
- 256 KB Flash
- 64 KB SRAM

More information about STM32WB07CCV can be found here:

- [WB07CC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wb07cc.html)
- [STM32WB07 reference manual](https://www.st.com/resource/en/reference_manual/rm0530--stm32wb07xc-and-stm32wb06xc-ultralow-power-wireless-32bit-mcus-armbased-cortexm0-with-bluetooth-low-energy-and-24-ghz-radio-solution-stmicroelectronics.pdf)

### Supported Features

The `nucleo_wb07cc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### Bluetooh support

BLE support is enabled; however, to build a Zephyr sample using this board,
you first need to fetch the Bluetooth controller library into Zephyr as a binary BLOB.

To fetch binary BLOBs:

```shell
west blobs fetch hal_stm32
```

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- USART1 TX/RX : PA9/PA8 (ST-Link Virtual COM Port)
- BUTTON (B1) : PA0
- BUTTON (B2) : PB5
- BUTTON (B3) : PB9
- LED (LD1/BLUE) : PB0
- LED (LD2/GREEN) : PB4
- LED (LD3/RED) : PB2

For more details, please refer to the [Nucleo WB07CC board User Manual](https://www.st.com/resource/en/user_manual/um3344-stm32wb07-nucleo64-board-mb1801-and-mb2119-stmicroelectronics.pdf).

## Programming and Debugging

Nucleo WB07CC board includes an ST-LINK-V3EC embedded debug tool interface.

Applications for the `nucleo_wb07cc` board target can be built and flashed
in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run)
for more details).

### Flashing

The board is configured to be flashed using the west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so [it must be installed](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) beforehand.

Alternatively, OpenOCD can also be used to flash the board using the
`--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to Nucleo WB07CC

Connect the Nucleo WB07CC to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_wb07cc samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_wb07cc/stm32wb07
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wb07cc samples/hello_world
west debug
```
