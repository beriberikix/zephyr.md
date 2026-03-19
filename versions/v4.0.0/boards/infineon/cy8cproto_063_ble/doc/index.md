---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/infineon/cy8cproto_063_ble/doc/index.html
original_path: boards/infineon/cy8cproto_063_ble/doc/index.html
---

# CY8CPROTO-063-BLE

Board Overview

[![../../../../_images/cy8cproto-063-ble.jpg](../../../../_images/cy8cproto-063-ble.jpg)
](../../../../_images/cy8cproto-063-ble.jpg)

CY8CPROTO-063-BLE

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cyble\_416045\_02

## Overview

The PSOC 6 BLE Proto Kit (CY8CPROTO-063-BLE) is a hardware platform that
enables design and debug of the Cypress PSOC 63 BLE MCU.

## Hardware

For more information about the PSOC 63 BLE MCU SoC and CY8CPROTO-063-BLE board:

- [PSOC 63 BLE MCU SoC Website](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6) [[1]](#id2)
- [PSOC 63 BLE MCU Datasheet](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_PSOC_63_with_BLE_Datasheet_Programmable_System-on-Chip_(PSOC)-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm_source=cypress&utm_medium=referral&utm_campaign=202110_globe_en_all_integration-files) [[2]](#id4)
- [PSOC 63 BLE MCU Architecture Reference Manual](https://documentation.infineon.com/html/psoc6/zrs1651212645947.html) [[3]](#id6)
- [PSOC 63 BLE MCU Register Reference Manual](https://documentation.infineon.com/html/psoc6/bnm1651211483724.html) [[4]](#id8)
- [CY8CPROTO-063-BLE Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/) [[5]](#id10)
- [CY8CPROTO-063-BLE User Guide](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812) [[6]](#id12)
- [CY8CPROTO-063-BLE Schematics](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821) [[7]](#id14)

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| GPIO | on-chip | GPIO |
| PINCTRL | on-chip | pin control |
| SPI | on-chip | SPI |
| UART | on-chip | serial port-polling; serial port-interrupt |
| I2C | on-chip | I2C |
| PWM | on-chip | PWM |
| Counter | on-chip | Counter |
| Bluetooth | on-chip | Bluetooth |

The default configuration can be found in the Kconfig

[boards/infineon/cy8cproto\_063\_ble/cy8cproto\_063\_ble\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_063_ble/cy8cproto_063_ble_defconfig)

### System Clock

The PSOC 63 BLE MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. CM0+ works at 50MHz, CM4 - at 100MHz. Other sources for the
system clock are provided in the SOC, depending on your system requirements.

## Fetch Binary Blobs

cy8cproto\_063\_ble board requires fetch binary files
(e.g Bluetooth controller firmware, CM0p prebuilt images, etc).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8cproto_063_ble samples/basic/blinky
```

## Programming and Debugging

The CY8CPROTO-063-BLE includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3) [[11]](#id22)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) [[8]](#id16) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) [[9]](#id18) packages include Infineon OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) [[10]](#id20) release for your system and manually extract the files to a location of your choice.

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
> west build -b cy8cproto_063_ble -p always samples/basic/blinky
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
> west build -b cy8cproto_063_ble -p always samples/basic/blinky
>
> west flash
> west debug
> ```

## References

[[1](#id3)]

[https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6)

[[2](#id5)]

[https://www.infineon.com/dgdl/Infineon-PSOC\_6\_MCU\_PSOC\_63\_with\_BLE\_Datasheet\_Programmable\_System-on-Chip\_(PSOC)-DataSheet-v16\_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm\_source=cypress&utm\_medium=referral&utm\_campaign=202110\_globe\_en\_all\_integration-files](https://www.infineon.com/dgdl/Infineon-PSOC_6_MCU_PSOC_63_with_BLE_Datasheet_Programmable_System-on-Chip_(PSOC)-DataSheet-v16_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0ee4efe46c37&utm_source=cypress&utm_medium=referral&utm_campaign=202110_globe_en_all_integration-files)

[[3](#id7)]

[https://documentation.infineon.com/html/psoc6/zrs1651212645947.html](https://documentation.infineon.com/html/psoc6/zrs1651212645947.html)

[[4](#id9)]

[https://documentation.infineon.com/html/psoc6/bnm1651211483724.html](https://documentation.infineon.com/html/psoc6/bnm1651211483724.html)

[[5](#id11)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/)

[[6](#id13)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00d7eb1812)

[[7](#id15)]

[https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-063-ble/#!?fileId=8ac78c8c7d0d8da4017d0f00ea3c1821)

[[8](#id17)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox)

[[9](#id19)]

[https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools)

[[10](#id21)]

[https://github.com/Infineon/openocd/releases/latest](https://github.com/Infineon/openocd/releases/latest)

[[11](#id23)]

[https://github.com/Infineon/KitProg3](https://github.com/Infineon/KitProg3)
