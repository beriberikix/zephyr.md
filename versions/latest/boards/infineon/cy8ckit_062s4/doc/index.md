---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/infineon/cy8ckit_062s4/doc/index.html
original_path: boards/infineon/cy8ckit_062s4/doc/index.html
---

# PSOC 62S4 Pioneer Kit

Board Overview

[![../../../../_images/cy8ckit_062s4.png](../../../../_images/cy8ckit_062s4.png)
](../../../../_images/cy8ckit_062s4.png)

PSOC 62S4 Pioneer Kit

Name:
:   `cy8ckit_062s4`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cy8c6244lqi\_s4d92

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cy8ckit_062s4/doc/index.rst/../..)

## Overview

The PSOC 62S4 Pioneer kit has a CY8C62x4 MCU, which is an ultra-low-power PSOC device specifically designed for battery-operated analog
sensing applications. It includes a 150-MHz Arm® Cortex®-M4 CPU as the primary application processor, a 100-MHz Arm® Cortex®-M0+ CPU that
supports low-power operations, up to 256 KB Flash and 128 KB SRAM, programmable analog sensing,
CapSense™ touch-sensing, and programmable digital peripherals.

The board features an onboard
programmer/debugger (KitProg3), a 512-Mbit Quad SPI NOR flash, a micro-B connector for USB device
interface, a thermistor, an ambient light sensor, a 5-segment CapSense™ slider, two CapSense™ buttons, two
user LEDs, and a push button. The board supports operating voltages from 1.8 V to 3.3 V for PSoC™ 6 MCU.

## Hardware

- [CY8CKIT 062S4 Pioneer Kit Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/?redirId=VL1508&utm_medium=referral&utm_source=cypress&utm_campaign=202110_globe_en_all_integration-dev_kit) [[2]](#id4)
- [CY8CKIT 062S4 Pioneer Kit Guide](https://www.infineon.com/dgdl/Infineon-CY8CKIT_062S4_PSOC62S4_pioneer_kit_guide-UserManual-v01_00-EN.pdf?fileId=8ac78c8c7e7124d1017e962f98992207) [[1]](#id2)
- [CY8CKIT 062S4 Pioneer Kit Schematic](https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S4_PSOC_62S4_Pioneer_Kit_Schematic-PCBDesignData-v01_00-EN.pdf?fileId=8ac78c8c7d710014017d7153484d2081) [[3]](#id6)
- [CY8CKIT 062S4 Pioneer Kit Technical Reference Manual](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C61X4CY8C62X4_REGISTERS_TECHNICAL_REFERENCE_MANUAL_(TRM)_PSOC_61_PSOC_62_MCU-AdditionalTechnicalInformation-v03_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0fb34f0627a7) [[4]](#id8)
- [CY8CKIT 062S4 Pioneer Kit Datasheet](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C62X4-DataSheet-v12_00-EN.pdf?fileId=8ac78c8c7ddc01d7017ddd026d585901) [[5]](#id10)

### Supported Features

The `cy8ckit_062s4` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `cy8ckit_062s4/cy8c6244lqi_s4d92` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L15) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L20) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | Infineon Cat1 ADC Each ADC group Cat1 is assigned to a Zephyr device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L189) | [`infineon,cat1-adc`](../../../../build/dts/api/bindings/adc/infineon%2Ccat1-adc.md#std-dtcompatible-infineon-cat1-adc) |
| ARM architecture | on-chip | Infineon Serial Communication Blocks (SCB) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L210) | [`infineon,cat1-scb`](../../../../build/dts/api/bindings/arm/infineon%2Ccat1-scb.md#std-dtcompatible-infineon-cat1-scb) |
| Flash controller | on-chip | Infineon CAT1 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L27) | [`infineon,cat1-flash-controller`](../../../../build/dts/api/bindings/flash_controller/infineon%2Ccat1-flash-controller.md#std-dtcompatible-infineon-cat1-flash-controller) |
| GPIO & Headers | on-chip | Infineon CAT1 GPIO Port[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L83)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L66) | [`infineon,cat1-gpio`](../../../../build/dts/api/bindings/gpio/infineon%2Ccat1-gpio.md#std-dtcompatible-infineon-cat1-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s4/cy8ckit_062s4.dts?plain=1#L32) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s4/cy8ckit_062s4.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L33) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Infineon CAT1 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L53) | [`infineon,cat1-pinctrl`](../../../../build/dts/api/bindings/pinctrl/infineon%2Ccat1-pinctrl.md#std-dtcompatible-infineon-cat1-pinctrl) |
| SDHC | on-chip | Infineon CAT1 SDHC/SDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L250) | [`infineon,cat1-sdhc-sdio`](../../../../build/dts/api/bindings/sdhc/infineon%2Ccat1-sdhc-sdio.md#std-dtcompatible-infineon-cat1-sdhc-sdio) |
| Serial controller | on-chip | Infineon CAT1 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L218)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L202) | [`infineon,cat1-uart`](../../../../build/dts/api/bindings/serial/infineon%2Ccat1-uart.md#std-dtcompatible-infineon-cat1-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/infineon/cat1a/psoc6_04/psoc6_04.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Clock Configuration

| Clock | Source | Output Frequency |
| --- | --- | --- |
| FLL | IMO | 100.0 MHz |
| PLL | IMO | 48.0 MHz |
| CLK\_HF0 | CLK\_PATH0 | 100.0 MHz |

## Fetch Binary Blobs

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8ckit_062s4 samples/basic/blinky
```

## Programming and Debugging

The `cy8ckit_062s4` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The CY8CKIT-062S4 includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3) [[9]](#id18)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [[6]](#id12) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [[7]](#id14) packages include Infineon OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) [[8]](#id16) release for your system and manually extract the files to a location of your choice.

Note

Linux requires device access rights to be set up for KitProg3. This is handled automatically by the ModusToolbox and ModusToolbox Programming Tools installations. When doing a minimal installation, this can be done manually by executing the script `openocd/udev_rules/install_rules.sh`.

### West Commands

The path to the installed Infineon OpenOCD executable must be available to the `west` tool commands. There are multiple ways of doing this. The example below uses a permanent CMake argument to set the CMake variable `OPENOCD`.

> WindowsLinux
>
> ```shell
> # Run west config once to set permanent CMake argument
> west config build.cmake-args -- -DOPENOCD=path/to/infineon/openocd/bin/openocd.exe
>
> # Do a pristine build once after setting CMake argument
> west build -b cy8ckit_062s4 -p always samples/basic/blinky
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
> west build -b cy8ckit_062s4 -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging on the PSOC 6 CM4 core.

## References

[[1](#id3)]

[https://www.infineon.com/dgdl/Infineon-CY8CKIT\_062S4\_PSOC62S4\_pioneer\_kit\_guide-UserManual-v01\_00-EN.pdf?fileId=8ac78c8c7e7124d1017e962f98992207](https://www.infineon.com/dgdl/Infineon-CY8CKIT_062S4_PSOC62S4_pioneer_kit_guide-UserManual-v01_00-EN.pdf?fileId=8ac78c8c7e7124d1017e962f98992207)

[[2](#id5)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/?redirId=VL1508&utm\_medium=referral&utm\_source=cypress&utm\_campaign=202110\_globe\_en\_all\_integration-dev\_kit](https://www.infineon.com/cms/en/product/evaluation-boards/cy8ckit-062s4/?redirId=VL1508&utm_medium=referral&utm_source=cypress&utm_campaign=202110_globe_en_all_integration-dev_kit)

[[3](#id7)]

[https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S4\_PSOC\_62S4\_Pioneer\_Kit\_Schematic-PCBDesignData-v01\_00-EN.pdf?fileId=8ac78c8c7d710014017d7153484d2081](https://www.infineon.com/dgdl/Infineon-CY8CKIT-062S4_PSOC_62S4_Pioneer_Kit_Schematic-PCBDesignData-v01_00-EN.pdf?fileId=8ac78c8c7d710014017d7153484d2081)

[[4](#id9)]

[https://www.infineon.com/dgdl/Infineon-PSOC\_6\_MCU\_CY8C61X4CY8C62X4\_REGISTERS\_TECHNICAL\_REFERENCE\_MANUAL\_(TRM)\_PSOC\_61\_PSOC\_62\_MCU-AdditionalTechnicalInformation-v03\_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0fb34f0627a7](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C61X4CY8C62X4_REGISTERS_TECHNICAL_REFERENCE_MANUAL_(TRM)_PSOC_61_PSOC_62_MCU-AdditionalTechnicalInformation-v03_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0fb34f0627a7)

[[5](#id11)]

[https://www.infineon.com/dgdl/Infineon-PSOC\_6\_MCU\_CY8C62X4-DataSheet-v12\_00-EN.pdf?fileId=8ac78c8c7ddc01d7017ddd026d585901](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_CY8C62X4-DataSheet-v12_00-EN.pdf?fileId=8ac78c8c7ddc01d7017ddd026d585901)

[[6](#id13)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

[[7](#id15)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

[[8](#id17)]

[https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

[[9](#id19)]

[https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)
