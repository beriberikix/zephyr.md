---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rza3ul_smarc/doc/index.html
original_path: boards/renesas/rza3ul_smarc/doc/index.html
---

# RZ/A3UL SMARC Evaluation Board Kit

Board Overview

[![../../../../_images/rza3ul_smarc.webp](https://docs.zephyrproject.org/4.2.0/_images/rza3ul_smarc.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rza3ul_smarc.webp)

RZ/A3UL SMARC Evaluation Board Kit

Name:
:   `rza3ul_smarc`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm64

SoC:
:   r9a07g063u02gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rza3ul_smarc/doc/index.rst/../..)

## Overview

The Renesas RZ/A3UL SMARC Evaluation Board Kit (RZ/A3UL-EVKIT) consists of a SMARC v2.1 module board and a carrier board.
Two types of evaluation boards are available: QSPI version and Octal-SPI version. The QSPI version is supported.

- Device: RZ/A3UL R9A07G063U02GBG

  - Cortex-A55 Single
  - BGA361pin, 13mmSq body, 0.5mm pitch
  - Certified device in [Azure Certified Device Catalog](https://devicecatalog.azure.com/devices/5848d87b-5d3e-4c11-ad76-90612639b025)
- SMARC v2.1 Module Board Functions

  - Two types of evaluation boards are available:

    - QSPI version: QSPI Serial Flash (Boot) + DDR4
    - Octal-SPI version: Octa Flash (Boot) + OctaRAM + DDR4
  - DDR4 SDRAM: 1GB x 1pc
  - QSPI flash memory: 128Mb x 1pc [AT25QL128A](https://www.renesas.com/en/products/memory-logic/non-volatile-memory/spi-nor-flash/at25ql128a-128mbit-17v-minimum-spi-serial-flash-memory-dual-io-quad-io-and-qpi-support) (QSPI version)
  - Octa RAM memory: 512Mb x 1pc / Octa flash memory: 1Gb x 1pc (Octal-SPI version)
  - eMMC memory: 64GB x 1pc
  - The microSD card slot is implemented and used as an eSD for boot.
  - 5-output clock oscillator [5P35023](https://www.renesas.com/en/products/clocks-timing/clock-generation/programmable-clocks/5p35023-versaclock-3s-programmable-clock-generator) implemented
  - PMIC power supply [DA9062](https://www.renesas.com/en/products/power-management/multi-channel-power-management-ics-pmics/da9062-pmic-designed-applications-requiring-85a) implemented
- Carrier Board Functions

  - The FFC/FPC connector is mounted as standard for connection to high-speed serial interface for camera module.
  - The Micro-HDMI connector via DSI/HDMI conversion module is mounted as standard for connection to high-speed serial interface for digital video module.
  - The Micro-AB receptacle (ch0: USB2.0 OTG) and A receptacle (ch1: USB2.0 Host) are respectively mounted as standard for connection to USB interface.
  - The RJ45 connector is mounted as standard for software development and evaluation using Ethernet.
  - The audio codec is mounted as standard for advance development of audio system. The audio jack is implemented for connection to audio interface.
  - The Micro-AB receptacles are implemented for connection to asynchronous serial port interface.
  - The microSD card slot and two sockets for PMOD are implemented as an interface for RZ/A3UL peripheral functions.
  - For power supply, a mounted USB Type-C receptacle supports the USB PD standard.

## Hardware

The Renesas RZ/A3UL MPU documentation can be found at [RZ/A3UL Group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-powerful-1ghz-64-bit-mpus-rtos-support-enables-high-definition-hmi-and-quick-startup?) [[1]](#id3)

[![RZ/A3UL group feature](https://docs.zephyrproject.org/4.2.0/_images/rza3ul_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rza3ul_block_diagram.webp)

RZ/A3UL block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZA3UL-EVKIT Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-evkit-rza3ul-evaluation-board-kit) [[2]](#id5)

### Supported Features

The `rza3ul_smarc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rza3ul_smarc/r9a07g063u02gbg` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L22) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm,cortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| GPIO & Headers | on-chip | Renesas RZ GPIO Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L56) | [`renesas,rz-gpio-int`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio-int.md#std-dtcompatible-renesas-rz-gpio-int) |
| on-chip | Renesas RZ GPIO controller[19 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L95) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L42) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| MTD | on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rza3ul_smarc/rza3ul_smarc.dts?plain=1#L43) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Below generic example shows of supported pinctrl definitions:[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L51) | [`renesas,rza-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas,rza-pinctrl.md#std-dtcompatible-renesas-rza-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCIF UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L268)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L281) | [`renesas,rz-scif-uart`](../../../../build/dts/api/bindings/serial/renesas,rz-scif-uart.md#std-dtcompatible-renesas-rz-scif-uart) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rza3ul_smarc/rza3ul_smarc.dts?plain=1#L39) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/renesas/rz/rza/r9a07g063.dtsi?plain=1#L30) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

## Programming and Debugging

The `rza3ul_smarc` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

RZ/A3UL-EVKIT uses Initial Program Loader (IPL) to perform initial settings and copy the Zephyr image from flash to DDR SRAM for execution. It only needs to be written to flash once.

There are two options to write IPL:

1. (Recommended) Follow ‘’4. Tutorial: Your First RZ MPU Project - Blinky’’ of [Getting Started with RZ/A Flexible Software Package](https://www.renesas.com/en/document/apn/rza-getting-started-flexible-software-package) [[4]](#id9)
   to start writing a blinky sample with FSP. The IPL will be written to flash by default in debugging time.
2. Follow the [Initial Program Loader Application Note](https://github.com/renesas/rza-initial-program-loader/tree/main/application_note) [[3]](#id7) to write the IPL separately. The minimal steps are described below.

   1. Follow ‘’6. IPL development environment construction procedure’’ to prepare the build environment.
   2. Follow ‘’7. IPL build environment construction procedure’’ to build Initial Program Loader.
      If the build is successful, Initial Program Loader file will be generated in /build/a3ul/release/rza3ul\_smarc\_qspi\_ipl.srec
   3. Follow ‘’8.1 Create Debug Configuration’’ to create a Debug configuration to run Initial Program Loader on the target board.
   4. Follow ‘’8.2 Connection to SMARC EVK Board’’ to setup target board with SW1 Debugger Enable (SW1-1 OFF) and Boot (1.8V) Mode (SW11[1:4]=OFF OFF OFF ON).
   5. Follow ‘’8.4 Execution procedure of IPL’’ to write Initial Program Loader to the target board.

Applications for the `rza3ul_smarc` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

### Console

The UART port is accessed by USB Type-mircoB port (CN14).

### Debugging

It is possible to load and execute a Zephyr application binary on this board on the Cortex-A55 System Core
from the DDR SDRAM, using `JLink` debugger ([J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools)).

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rza3ul_smarc samples/hello_world
west debug
```

### Flashing

Zephyr application can be flashed to QSPI/Octal-SPI storage and then loaded by Initial Program Loader.

```shell
# From the root of the zephyr repository
west build -b rza3ul_smarc samples/hello_world
west flash
```

## References

[[1](#id4)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-powerful-1ghz-64-bit-mpus-rtos-support-enables-high-definition-hmi-and-quick-startup?](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-powerful-1ghz-64-bit-mpus-rtos-support-enables-high-definition-hmi-and-quick-startup?)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-evkit-rza3ul-evaluation-board-kit](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rza3ul-evkit-rza3ul-evaluation-board-kit)

[[3](#id8)]

[https://github.com/renesas/rza-initial-program-loader/tree/main/application\_note](https://github.com/renesas/rza-initial-program-loader/tree/main/application_note)

[[4](#id10)]

[https://www.renesas.com/en/document/apn/rza-getting-started-flexible-software-package](https://www.renesas.com/en/document/apn/rza-getting-started-flexible-software-package)
