---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32l4r9i_disco/doc/index.html
original_path: boards/st/stm32l4r9i_disco/doc/index.html
---

# STM32L4R9I Discovery

Board Overview

[![../../../../_images/stm32l4r9i_disco.jpg](../../../../_images/stm32l4r9i_disco.jpg)
](../../../../_images/stm32l4r9i_disco.jpg)

STM32L4R9I Discovery

Name:
:   `stm32l4r9i_disco`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l4r9xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32l4r9i_disco/doc/index.rst/../..)

## Overview

The 32L4R9IDISCOVERY Discovery kit is a complete demonstration and development platform
for STMicroelectronics Arm® Cortex®-M4 core-based STM32L4R9AI microcontroller.

Leveraging the innovative ultra-low-power oriented features, 640 Kbytes of embedded RAM,
graphics performance (Chrom-ART Accelerator), and DSI controller offered by the STM32L4R9AI,
the 32L4R9IDISCOVERY Discovery kit enables users to easily prototype applications with
state-of-the-art energy efficiency, as well as stunning audio and graphics rendering with direct
support for AMOLED DSI round LCD display.

For even more user-friendliness, the on-board ST-LINK/V2-1 debugger provides out-of-the-box
programming and debugging capabilities.

More information about the board can be found at the [STM32L4R9I-DISCOVERY website](https://www.st.com/en/evaluation-tools/32l4r9idiscovery.html).
More information about STM32L4R9 can be found here:

- [STM32L4R9/S9 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l4r9-s9.html)
- [STM32L4+ Series reference manual](https://www.st.com/resource/en/reference_manual/rm0432-stm32l4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)
- [STM32L4R5xx/R7xx/R9xx datasheet](https://www.st.com/resource/en/datasheet/stm32l4r5vi.pdf)

### Supported Features

The `stm32l4r9i_disco` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Pin Mapping

For more details, please refer to [STM32L4R9I-DISCOVERY website](https://www.st.com/en/evaluation-tools/32l4r9idiscovery.html).

### System Clock

The STM32L4R9AI System Clock can be driven by an internal or external oscillator,
as well as by the main PLL clock. By default, the System clock is driven by
the PLL clock at 120MHz. PLL clock is driven by a 4MHz medium speed internal clock.

### Serial Port

The STM32L4R9I Discovery board has up to 6 U(S)ARTs.
The Zephyr console output is assigned to UART2, which is connected to the onboard
ST-LINK Virtual COM port interface. Default communication settings are 115200 8N1.

## Programming and Debugging

The STM32L4R9I Discovery board includes an ST-LINK/V2-1 debug tool.

Applications for the `stm32l4r9i_disco` board configuration can be
built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to STM32L4R9I Discovery

Connect the STM32L4R9I Discovery to your host computer using the ST-LINK
USB port, then run a serial host program to connect with the board. For example:

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

You can then build and flash applications in the usual way.
Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32l4r9i_disco samples/hello_world
west flash
```

You should see the following message in the serial host program:

```shell
$ Hello World! stm32l4r9i_disco
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32l4r9i_disco samples/hello_world
west debug
```
