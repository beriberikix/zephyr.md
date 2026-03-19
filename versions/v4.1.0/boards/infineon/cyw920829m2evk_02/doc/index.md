---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/infineon/cyw920829m2evk_02/doc/index.html
original_path: boards/infineon/cyw920829m2evk_02/doc/index.html
---

# CYW920829M2EVK-02

Board Overview

[![../../../../_images/cyw920829m2evk_02.webp](../../../../_images/cyw920829m2evk_02.webp)
](../../../../_images/cyw920829m2evk_02.webp)

CYW920829M2EVK-02

Name:
:   `cyw920829m2evk_02`

Vendor:
:   Infineon Technologies

Architecture:
:   arm

SoC:
:   cyw20829b0lkml

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/infineon/cyw920829m2evk_02/doc/index.rst/../..)

## Overview

The AIROC™ CYW20829 Bluetooth® LE MCU Evaluation Kit (CYW920829M2EVK-02) with its included on-board peripherals enables evaluation, prototyping, and development of a wide array of Bluetooth® Low Energy applications, all on Infineon’s low power, high performance AIROC™ CYW20829. The AIROC™ CYW20829’s robust RF performance and 10 dBm TX output power without an external power amplifier (PA). This provides enough link budget for the entire spectrum of Bluetooth® LE use cases including industrial IoT applications, smart home, asset tracking, beacons and sensors, and medical devices.

The system features Dual Arm® Cortex® - M33s for powering the MCU and Bluetooth subsystem with programmable and reconfigurable analog and digital blocks. In addition, on the kit, there is a suite of on-board peripherals including six-axis inertial measurement unit (IMU), thermistor, analog mic, user programmable buttons (2), LEDs (2), and RGB LED. There is also extensive GPIO support with extended headers and Arduino Uno R3 compatibility for third-party shields.

## Hardware

For more information about the CYW20829 SoC and CYW920829M2EVK-02 board:

- [CYW20829 SoC Website](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-le/cyw20829/)
- [CYW920829M2EVK-02 Board Website](https://www.infineon.com/cms/en/product/evaluation-boards/cyw920829m2evk-02/)

### Kit Features:

- AIROC™ CYW20829 Bluetooth® LE MCU in 56 pin QFN package
- Arduino compatible headers for hardware expansion
- On-board sensors - 6-axis IMU, Thermistor, Infineon analog microphone, and Infineon digital microphone
- User switches, RGB LED and user LEDs
- USB connector for power, programming and USB-UART bridge

### Kit Contents:

- CYW20829 evaluation board (CYW9BTM2BASE3+CYW920829M2IPA2)
- USB Type-A to Micro-B cable
- Six jumper wires (five inches each)
- Quick start guide

### Supported Features

The `cyw920829m2evk_02` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The AIROC™ CYW20829 Bluetooth® MCU SoC is configured to use the internal IMO+FLL as a source for
the system clock. Other sources for the system clock are provided in the SOC, depending on your
system requirements.

## Fetch Binary Blobs

cyw920829m2evk\_02 board requires fetch binary files (e.g Bluetooth controller firmware).

To fetch Binary Blobs:

```shell
west blobs fetch hal_infineon
```

## Build blinking led sample

Here is an example for building the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample application.

```shell
# From the root of the zephyr repository
west build -b cyw920829m2evk_02 samples/basic/blinky
```

## Programming and Debugging

The CYW920829M2EVK-02 includes an onboard programmer/debugger ([KitProg3](https://github.com/Infineon/KitProg3)) to provide debugging, flash programming, and serial communication over USB. Flash and debug commands use OpenOCD and require a custom Infineon OpenOCD version, that supports KitProg3, to be installed.

The CYW920829M2EVK-02 supports RTT via a SEGGER JLink device, under the target name cyw20829\_tm. This can be enabled for an application by building with the rtt-console snippet or setting the following config values: CONFIG\_UART\_CONSOLE=n, CONFIG\_RTT\_CONSOLE=y, and CONFIG\_USE\_SEGGER\_RTT=y.
e.g. west build -p always -b cyw920829m2evk\_02 samples/basic/blinky -S rtt-console

As an additional note there is currently a discrepancy in RAM address between SEGGER and the CYW920829M2EVK-02 device. So, for RTT control block, do not use “Auto Detection”. Instead, set the search range to something reflecting: RAM RangeStart at 0x20000000 and RAM RangeSize of 0x3d000.

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
> west build -b cyw920829m2evk_02 -p always samples/basic/blinky
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
> west build -b cyw920829m2evk_02 -p always samples/basic/blinky
>
> west flash
> west debug
> ```

Once the gdb console starts after executing the west debug command, you may now set breakpoints and perform other standard GDB debugging on the CYW20829 CM33 core.
