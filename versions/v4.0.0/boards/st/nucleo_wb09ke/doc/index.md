---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/st/nucleo_wb09ke/doc/index.html
original_path: boards/st/nucleo_wb09ke/doc/index.html
---

# Nucleo WB09KE

Board Overview

[![../../../../_images/nucleo_wb09ke.webp](../../../../_images/nucleo_wb09ke.webp)
](../../../../_images/nucleo_wb09ke.webp)

Nucleo WB09KE

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wb09

## Overview

The Nucleo WB09KE board is a Bluetooth® Low Energy wireless and ultra-low-power
board featuring an ARM Cortex®-M0+ based STM32WB09KEV MCU, embedding a
powerful and ultra-low-power radio compliant with the Bluetooth® Low Energy
SIG specification v5.4.

More information about the board can be found on the [Nucleo WB09KE webpage](https://www.st.com/en/evaluation-tools/nucleo-wb09ke.html).

## Hardware

Nucleo WB09KE provides the following hardware components:

- STM32WB09KEV in VFQFPN32 package
- ARM® 32-bit Cortex®-M0+ CPU
- 64 MHz maximal CPU frequebct
- 512 KB Flash
- 64 KB SRAM

More information about STM32WB09KEV can be found here:

- [WB09KE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wb09ke.html)
- [STM32WB09 reference manual](https://www.st.com/resource/en/reference_manual/rm0505-stm32wb09xe-ultralow-power-wireless-32bit-mcu-armbased-cortexm0-with-bluetooth-low-energy-and-24-ghz-radio-solution-stmicroelectronics.pdf)

### Supported Features

The Zephyr `nucleo_wb09ke` board target supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| UART | on-chip | serial port-polling; serial port-interrupt |
| PINMUX | on-chip | pinmux |
| GPIO | on-chip | gpio |
| FLASH | on-chip | internal flash memory |

Other hardware features are not yet supported on this Zephyr port.

The default configuration can be found in the defconfig file:
[boards/st/nucleo\_wb09ke/nucleo\_wb09ke\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wb09ke/nucleo_wb09ke_defconfig)

### Connections and IOs

#### Default Zephyr Peripheral Mapping:

- USART1 TX/RX : PA1/PB0 (ST-Link Virtual COM Port)
- BUTTON (B1) : PA0
- BUTTON (B2) : PB5
- BUTTON (B3) : PB14
- LED (LD1/BLUE) : PB1
- LED (LD2/GREEN) : PB4
- LED (LD3/RED) : PB2

For more details, please refer to the [Nucleo WB09KE board User Manual](https://www.st.com/resource/en/user_manual/um3345-stm32wb09-nucleo64-board-mb1801-and-mb2032-stmicroelectronics.pdf).

## Programming and Debugging

Nucleo WB09KE board includes an ST-LINK-V3EC embedded debug tool interface.

Applications for the `nucleo_w09ke` board target can be built and flashed
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

#### Flashing an application to Nucleo WB09KE

Connect the Nucleo WB09KE to your host computer using the USB port,
then run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Now build and flash an application. Here is an example for
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b nucleo_wb09ke samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_wb09ke/stm32wb09
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wb09ke samples/hello_world
west debug
```
