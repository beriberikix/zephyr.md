---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_f439zi/doc/index.html
original_path: boards/st/nucleo_f439zi/doc/index.html
---

# Nucleo F439ZI

Board Overview

Name:
:   `nucleo_f439zi`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f439xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f439zi/doc/index.rst/../..)

## Overview

The Nucleo F439ZI board features an ARM Cortex-M4 based STM32F439ZI MCU
with a wide range of connectivity support and configurations. This SoC
is basically a clone of the STM32F429ZI with a supplementary hardware
cryptographic accelerator.

More information about STM32F439ZI can be found here:

- [STM32F439ZI on www.st.com](https://www.st.com/en/microcontrollers/stm32f439zi.html) [[1]](#id1)
- [STM32F439 reference manual](https://www.st.com/resource/en/reference_manual/dm00031020.pdf) [[2]](#id3)
- [STM32F439 datasheet](https://www.st.com/resource/en/datasheet/stm32f439zi.pdf) [[3]](#id5)

### Supported Features

The `nucleo_f439zi` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

## Programming and Debugging

The `nucleo_f439zi` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The Nucleo F439ZI board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) [[4]](#id7) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to the Nucleo F439ZI

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_f439zi samples/basic/blinky
west flash
```

You should see user led “LD1” blinking.

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f439zi samples/hello_world
west debug
```

[[1](#id2)]

[https://www.st.com/en/microcontrollers/stm32f439zi.html](https://www.st.com/en/microcontrollers/stm32f439zi.html)

[[2](#id4)]

[https://www.st.com/resource/en/reference\_manual/dm00031020.pdf](https://www.st.com/resource/en/reference_manual/dm00031020.pdf)

[[3](#id6)]

[https://www.st.com/resource/en/datasheet/stm32f439zi.pdf](https://www.st.com/resource/en/datasheet/stm32f439zi.pdf)

[[4](#id8)]

[https://www.st.com/en/development-tools/stm32cubeprog.html](https://www.st.com/en/development-tools/stm32cubeprog.html)
