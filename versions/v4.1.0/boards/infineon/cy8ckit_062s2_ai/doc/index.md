---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/infineon/cy8ckit_062s2_ai/doc/index.html
original_path: boards/infineon/cy8ckit_062s2_ai/doc/index.html
---

# PSOC 6 AI Evaluation Kit

Board Overview

[![../../../../_images/cy8ckit_062s2_ai.webp](../../../../_images/cy8ckit_062s2_ai.webp)
](../../../../_images/cy8ckit_062s2_ai.webp)

PSOC 6 AI Evaluation Kit

Name:
:   `cy8ckit_062s2_ai`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cy8c624abzi\_s2d44

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8ckit_062s2_ai/doc/index.rst/../..)

## Overview

The PSOC 6 AI Evaluation Kit (CY8CKIT-062S2-AI) is a cost effective and small development kit that
enables design and debug of PSOC 6 MCUs.
It includes a CY8C624ABZI-S2D44 MCU which is based on a 150-MHz Arm® Cortex®-M4 and
a 100-MHz Arm® Cortex®-M0+, with 2048 KB of on-chip Flash, 1024 KB of SRAM,
a Quad-SPI external memory interface, built-in hardware and software security features,
rich analog, digital, and communication peripherals.

The board features an AIROC® CYW43439 Wi-Fi & Bluetooth® combo device,
a 512 MB NOR flash, an onboard programmer/debugger (KitProg3), USB host and device features,
two user LEDs, and one push button.

## Hardware

For more information about the CY8C624ABZI-S2D44 MCU SoC and CY8CKIT-062S2-AI board:

- [CY8C624ABZI-S2D44 MCU SoC Website](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu/psoc-62/psoc-62x8-62xa/cy8c624abzi-s2d44/) [[1]](#id2)
- [CY8C624ABZI-S2D44 MCU Datasheet](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C62X8_CY8C62XA-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee7d03a70b1) [[2]](#id4)
- [CY8CKIT-062S2-AI Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-ai/?redirId=273839) [[3]](#id6)
- [CY8CKIT-062S2-AI User Guide](https://www.infineon.com/dgdl/Infineon-CY8CKIT_062S2_AI_KIT_GUIDE-UserManual-v01_00-EN.pdf?fileId=8ac78c8c90530b3a01906d4608842668) [[4]](#id8)
- [CY8CKIT-062S2-AI Schematics](https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S2-AI_PSoC_6_AI_Evaluation_Board_Schematic-PCBDesignData-v01_00-EN.pdf?fileId=8ac78c8c8eeb092c018f0af9e109106f) [[5]](#id10)

### Supported Features

The `cy8ckit_062s2_ai` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cy8ckit_062s2_ai/cy8c624abzi_s2d44` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L15) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon Cat1 ADC Each ADC group Cat1 is assigned to a Zephyr device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L306) | [`infineon,cat1-adc`](../../../../build/dts/api/bindings/adc/infineon%2Ccat1-adc.md#std-dtcompatible-infineon-cat1-adc) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L202) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon%2Ccat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Clock control | on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L13)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L69) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Generic fixed factor clock provider[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L21)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/system_clocks.dtsi?plain=1#L37) | [`fixed-factor-clock`](../../../../build/dts/api/bindings/clock/fixed-factor-clock.md#std-dtcompatible-fixed-factor-clock) |
| Counter | on-chip | Infineon counters[32 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L320) | [`infineon,cat1-counter`](../../../../build/dts/api/bindings/counter/infineon%2Ccat1-counter.md#std-dtcompatible-infineon-cat1-counter) |
| DMA | on-chip | Infineon CAT1 DMA node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L552) | [`infineon,cat1-dma`](../../../../build/dts/api/bindings/dma/infineon%2Ccat1-dma.md#std-dtcompatible-infineon-cat1-dma) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L27) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon%2Ccat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L111)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L66) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon%2Ccat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s2_ai/cy8ckit_062s2_ai.dts?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s2_ai/cy8ckit_062s2_ai.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl container node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L53) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon%2Ccat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L545) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon%2Ccat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L210) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon%2Ccat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | Infineon CAT1 Watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_02/psoc6_02.dtsi?plain=1#L314) | [`infineon,cat1-watchdog`](../../../../build/dts/api/bindings/watchdog/infineon%2Ccat1-watchdog.md#std-dtcompatible-infineon-cat1-watchdog) |

### System Clock

The PCY8C624ABZI-S2D44 MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. CM0+ works at 50MHz, CM4 - at 100MHz. Other sources for the
system clock are provided in the SoC, depending on your system requirements.

## Fetch Binary Blobs

The CY8CKIT-062S2-AI board requires fetch binary files (e.g CM0+ prebuilt images).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8ckit_062s2_ai/cy8c624abzi_s2d44 samples/basic/blinky
```

## Programming and Debugging

The CY8CKIT-062S2-AI board includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3) [[9]](#id18))
to provide debugging, flash programming, and serial communication over USB.
Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version,
that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [[6]](#id12) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [[7]](#id14) packages include Infineon OpenOCD.
Installing either of these packages will also install Infineon OpenOCD.
If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) [[8]](#id16) release
for your system and manually extract the files to a location of your choice.

Note

Linux requires device access rights to be set up for KitProg3.
This is handled automatically by the ModusToolbox and ModusToolbox Programming Tools installations.
When doing a minimal installation, this can be done manually by executing the script
`openocd/udev_rules/install_rules.sh`.

### West Commands

The path to the installed Infineon OpenOCD executable must be available to the `west` tool commands.
There are multiple ways of doing this.
The example below uses a permanent CMake argument to set the CMake variable `OPENOCD`.

> WindowsLinux
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd.exe
>
> # Do a pristine build once after setting CMake argument
> west build -b cy8ckit_062s2_ai/cy8c624abzi_s2d44 -p always samples/basic/blinky
>
> west flash
> west debug
> ```
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd
>
> # Do a pristine build once after setting CMake argument
> west build -b cy8ckit_062s2_ai/cy8c624abzi_s2d44 -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Alternatively, pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner pyocd
```

## References

[[1](#id3)]

[https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu/psoc-62/psoc-62x8-62xa/cy8c624abzi-s2d44/](https://www.infineon.com/cms/en/product/microcontroller/32-bit-psoc-arm-cortex-microcontroller/psoc-6-32-bit-arm-cortex-m4-mcu/psoc-62/psoc-62x8-62xa/cy8c624abzi-s2d44/)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-PSOC\_6\_MCU\_CY8C62X8\_CY8C62XA-DataSheet-v16\_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee7d03a70b1](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C62X8_CY8C62XA-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee7d03a70b1)

[[3](#id7)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-ai/?redirId=273839](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s2-ai/?redirId=273839)

[[4](#id9)]

[https://www.infineon.com/dgdl/Infineon-CY8CKIT\_062S2\_AI\_KIT\_GUIDE-UserManual-v01\_00-EN.pdf?fileId=8ac78c8c90530b3a01906d4608842668](https://www.infineon.com/dgdl/Infineon-CY8CKIT_062S2_AI_KIT_GUIDE-UserManual-v01_00-EN.pdf?fileId=8ac78c8c90530b3a01906d4608842668)

[[5](#id11)]

[https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S2-AI\_PSoC\_6\_AI\_Evaluation\_Board\_Schematic-PCBDesignData-v01\_00-EN.pdf?fileId=8ac78c8c8eeb092c018f0af9e109106f](https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S2-AI_PSoC_6_AI_Evaluation_Board_Schematic-PCBDesignData-v01_00-EN.pdf?fileId=8ac78c8c8eeb092c018f0af9e109106f)

[[6](#id13)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

[[7](#id15)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

[[8](#id17)]

[https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

[[9](#id19)]

[https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)
