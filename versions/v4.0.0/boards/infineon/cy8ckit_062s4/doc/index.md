---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/infineon/cy8ckit_062s4/doc/index.html
original_path: boards/infineon/cy8ckit_062s4/doc/index.html
---

# PSOC 62S4 Pioneer Kit

Board Overview

[![../../../../_images/cy8ckit_062s4.png](../../../../_images/cy8ckit_062s4.png)
](../../../../_images/cy8ckit_062s4.png)

PSOC 62S4 Pioneer Kit

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cy8c6244lqi\_s4d92

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

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| PINCTRL | on-chip | pin control |
| UART | on-chip | serial port-polling; |

The default configuration can be found in the Kconfig

[boards/infineon/cy8ckit\_062s4/cy8ckit\_062s4\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8ckit_062s4/cy8ckit_062s4_defconfig)

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
