---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/infineon/cy8cproto_062_4343w/doc/index.html
original_path: boards/infineon/cy8cproto_062_4343w/doc/index.html
---

# CY8CPROTO-062-4343W

Board Overview

[![../../../../_images/board.jpg](../../../../_images/board.jpg)
](../../../../_images/board.jpg)

CY8CPROTO-062-4343W

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cy8c624abzi\_s2d44

## Overview

The CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Prototyping Kit is a low-cost hardware
platform that enables design and debug of PSOC 6 MCUs. It comes with a Murata
LBEE5KL1DX module, based on the CYW4343W combo device, industry-leading CAPSENSE
for touch buttons and slider, on-board debugger/programmer with KitProg3, microSD
card interface, 512-Mb Quad-SPI NOR flash, PDM-PCM microphone, and a thermistor.

This kit is designed with a snap-away form-factor, allowing the user to separate
the different components and features that come with this kit and use independently.
In addition, support for Digilent’s Pmod interface is also provided with this kit.

## Hardware

For more information about the PSOC 62 MCU SoC and CY8CPROTO-062-4343W board:

- [PSOC 62 MCU SoC Website](https://www.cypress.com/products/32-bit-arm-cortex-m4-psoc-6)
- [PSOC 62 MCU Datasheet](https://www.cypress.com/documentation/datasheets/psoc-6-mcu-psoc-62-datasheet-programmable-system-chip-psoc-preliminary)
- [PSOC 62 MCU Architecture Reference Manual](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-architecture-technical-reference-manual)
- [PSOC 62 MCU Register Reference Manual](https://www.cypress.com/documentation/technical-reference-manuals/psoc-6-mcu-psoc-62-register-technical-reference-manual-trm)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Website](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT User Guide](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/#!?fileId=8ac78c8c7d0d8da4017d0f0118571844)
- [CY8CPROTO-062-4343W PSOC 6 Wi-Fi BT Schematics](https://www.infineon.com/cms/en/product/evaluation-boards/cy8cproto-062-4343w/#!?fileId=8ac78c8c7d0d8da4017d0f01126b183f)

### Kit Features:

- Support of up to 2MB Flash and 1MB SRAM
- Dedicated SDHC to interface with WICED wireless devices.
- Delivers dual-cores, with a 150-MHz Arm Cortex-M4 as the primary
  application processor and a 100-MHz Arm Cortex-M0+ as the secondary
  processor for low-power operations.
- Supports Full-Speed USB, capacitive-sensing with CAPSENSE, a PDM-PCM
  digital microphone interface, a Quad-SPI interface, 13 serial communication
  blocks, 7 programmable analog blocks, and 56 programmable digital blocks.

### Kit Contents:

- PSOC 6 Wi-Fi BT Prototyping Board
- USB Type-A to Micro-B cable
- Quick start guide

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vectored interrupt controller |
| SYSTICK | on-chip | system clock |
| GPIO | on-chip | GPIO |
| UART | on-chip | serial port-polling; serial port-interrupt |

The default configuration can be found in the Kconfig

[boards/infineon/cy8cproto\_062\_4343w/cy8cproto\_062\_4343w\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/infineon/cy8cproto_062_4343w/cy8cproto_062_4343w_defconfig)

### System Clock

The PSOC 62 MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. CM0+ works at 50MHz, CM4 - at 100MHz. Other sources for the
system clock are provided in the SOC, depending on your system requirements.

## Fetch Binary Blobs

cy8cproto\_062\_4343w board optionally uses binary blobs for features
(e.g WIFI/Bluetooth chip firmware, CM0p prebuilt images, etc).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cy8cproto_062_4343w samples/basic/blinky
```

## Programming and Debugging

The CY8CPROTO-062-4343W includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

### Infineon OpenOCD Installation

Both the full [ModusToolbox](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolbox) and the [ModusToolbox Programming Tools](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.modustoolboxprogtools) packages include Infineon OpenOCD. Installing either of these packages will also install Infineon OpenOCD. If neither package is installed, a minimal installation can be done by downloading the [Infineon OpenOCD](https://github.com/Infineon/openocd/releases/latest) release for your system and manually extract the files to a location of your choice.

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
> west build -b cy8cproto_062_4343w -p always samples/basic/blinky
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
> west build -b cy8cproto_062_4343w -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging on the PSOC 6 CM4 core.

### Errata

| Problem | Solution |
| --- | --- |
| The GPIO\_INT\_TRIG\_BOTH interrupt is not raised when the associated GPIO is asserted. | This will be fixed in a future release. |
| GDB experiences a timeout error connecting to a server instance started by west debugserver. | This will be fixed in a future release. |
