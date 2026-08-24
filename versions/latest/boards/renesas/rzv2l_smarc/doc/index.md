---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzv2l_smarc/doc/index.html
original_path: boards/renesas/rzv2l_smarc/doc/index.html
---

# RZ/V2L SMARC Evaluation Board Kit

Board Overview

[![../../../../_images/rzv2l_smarc.webp](https://docs.zephyrproject.org/4.2.0/_images/rzv2l_smarc.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzv2l_smarc.webp)

RZ/V2L SMARC Evaluation Board Kit

Name:
:   `rzv2l_smarc`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a07g054l23gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzv2l_smarc/doc/index.rst/../..)

## Overview

The Renesas RZ/V2L SMARC Evaluation Board Kit (RZ/V2L-EVKIT) consists of a SMARC v2.1 module board and a carrier board.

- Device: RZ/V2L R9A07G054L23GBG

  - Cortex-A55 Dual, Cortex-M33
  - BGA551pin, 15mmSq body, 0.5mm pitch
- SMARC v2.1 Module Board Functions

  - DDR4 SDRAM: 2GB x 1pc
  - QSPI flash memory: 512Mb x 1pc
  - eMMC memory: 64GB x 1pc
  - The microSD card slot is implemented and used as an eSD for boot
  - 5-output clock oscillator [5P35023](https://www.renesas.com/en/products/clocks-timing/clock-generation/programmable-clocks/5p35023-versaclock-3s-programmable-clock-generator) implemented
  - PMIC power supply [RAA215300](https://www.renesas.com/en/products/power-management/multi-channel-power-management-ics-pmics/raa215300-high-performance-9-channel-pmic-supporting-ddr-memory-built-charger-and-rtc) implemented
- Carrier Board Functions

  - The FFC/FPC connector is mounted as standard for connection to high-speed serial interface for camera module.
  - The Micro-HDMI connector via DSI/HDMI conversion module is mounted as standard for connection to high-speed serial interface for digital video module.
  - The Micro-AB receptacle (ch0: USB2.0 OTG) and A receptacle (ch1: USB2.0 Host) are respectively mounted as standard for connection to USB interface.
  - The RJ45 connector is mounted as standard for software development and evaluation using Ethernet.
  - The audio codec is mounted as standard for advance development of audio system. The audio jack is implemented for connection to audio interface.
  - The CAN connector is implemented for connection to CAN-Bus interface.
  - The Micro-AB receptacles are implemented for connection to asynchronous serial port interface.
  - The microSD card slot and two sockets for PMOD are implemented as an interface for RZ/V2L peripheral functions.
  - For power supply, a mounted USB Type-C receptacle supports the USB PD standard.
- MIPI Camera Module

  - MIPI Camera Module (MIPI CSI) is included. Image recognition processing can be used with images input with MIPI camera.

## Hardware

The Renesas RZ/V2L MPU documentation can be found at [RZ/V2L Group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-general-purpose-microprocessor-equipped-renesas-original-ai-accelerator-drp-ai-12ghz-dual-core-arm) [[1]](#id3)

[![RZ/V2L group feature](https://docs.zephyrproject.org/4.2.0/_images/rzv2l_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzv2l_block_diagram.webp)

RZ/V2L block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZV2L-EVKIT Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-evkit-smarc-som-evaluation-kit-rzv2l-mpu-ai-accelerator) [[2]](#id5)

### Supported Features

The `rzv2l_smarc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzv2l_smarc/r9a07g054l23gbg/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L19) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| GPIO & Headers | on-chip | Renesas RZ GPIO Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L40) | [`renesas,rz-gpio-int`](../../../../build/dts/api/bindings/gpio/renesas%2Crz-gpio-int.md#std-dtcompatible-renesas-rz-gpio-int) |
| on-chip | Renesas RZ GPIO controller[49 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L55) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L27) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | Renesas RZ/V pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L35) | [`renesas,rzv-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crzv-pinctrl.md#std-dtcompatible-renesas-rzv-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCIF UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L516)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzv/r9a07g054.dtsi?plain=1#L498) | [`renesas,rz-scif-uart`](../../../../build/dts/api/bindings/serial/renesas%2Crz-scif-uart.md#std-dtcompatible-renesas-rz-scif-uart) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzv2l_smarc/rzv2l_smarc_r9a07g054l23gbg_cm33.dts?plain=1#L24) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

## Programming and Debugging

The `rzv2l_smarc` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rzv2l_smarc` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

### Console

The UART port for Cortex-M33 System Core can be accessed by connecting [Pmod USBUART](https://store.digilentinc.com/pmod-usbuart-usb-to-uart-interface/)
to the upper side of `PMOD 1`.

### Debugging

It is possible to load and execute a Zephyr application binary on
this board on the Cortex-M33 System Core from
the internal SRAM, using `JLink` debugger ([J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools)).

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rzv2l_smarc/r9a07g054l23gbg/cm33 samples/hello_world
west debug
```

### Flashing

RZ/V2L-EVKIT is designed to start different systems on different cores.
It uses Yocto as the build system to build Linux system and boot loaders
to run Zephyr on Cortex-M33 with u-boot. The minimal steps are described below.

1. Follow ‘’2.2 Building Images’’ of [SMARC EVK of RZ/V2L Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104) [[3]](#id7) to prepare the build environment.
2. At step (4), follow step ‘’2. Download Multi-OS Package’’ and ‘’3. Add the layer for Multi-OS Package’’
   of ‘’3.2 OpenAMP related stuff Integration for RZ/V2L’’ of [RZ/V2L Quick Start Guide for RZ/V Multi-OS Package](https://www.renesas.com/en/document/apn/rzv2l-quick-start-guide-rzv-multi-os-package-v300) [[4]](#id13)
   to add the layer for Multi-OS Package.

```shell
$ cd ~/rzv_vlp_<pkg ver>
$ unzip <Multi-OS Dir>/r01an7254ej0300-rzv-multi-os-pkg.zip
$ tar zxvf r01an7254ej0300-rzv-multi-os-pkg/meta-rz-features_multi-os_v3.0.0.tar.gz
$ bitbake-layers add-layer ../meta-rz-features/meta-rz-multi-os/meta-rzv2l
```

3. Start the build:

```shell
$ MACHINE=smarc-rzv2l bitbake core-image-minimal
```

The below necessary artifacts will be located in the build/tmp/deploy/images

| Artifacts | File name |
| --- | --- |
| Boot loader | bl2\_bp-smarc-rzv2l\_pmic.srec  fip-smarc-rzv2l\_pmic.srec |
| Flash Writer | Flash\_Writer\_SCIF\_RZV2L\_SMARC\_PMIC\_DDR4\_2GB\_1PCS.mot |

4. Follow ‘’4.2 Startup Procedure’’ of [SMARC EVK of RZ/V2L Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104) [[3]](#id7) for power supply and board setting
   at SCIF download (SW11[1:4] = OFF, ON, OFF, ON) and (SW1[1:2] = ON, OFF)
5. Follow ‘’4.3 Download Flash Writer to RAM’’ of [SMARC EVK of RZ/V2L Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104) [[3]](#id7) to download Flash Writer to RAM
6. Follow ‘’4.4 Write the Bootloader’’ of [SMARC EVK of RZ/V2L Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104) [[3]](#id7) to write the boot loader
   to the target board by using Flash Writer.
7. Follow ‘’4.5 Change Back to Normal Boot Mode’’ with switch setting (SW11[1:4] = OFF, OFF, OFF, ON) and (SW1[1:2] = ON, OFF)
8. Follow ‘’3. Preparing the SD Card’’ of [SMARC EVK of RZ/V2L Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104) [[3]](#id7) to write files to the microSD Card
9. Copy zephyr.bin file to microSD card
10. Follow “4.3.2 CM33 Sample Program Invocation with u-boot” from the beginning to step 4 of [RZ/V2L Quick Start Guide for RZ/V Multi-OS Package](https://www.renesas.com/en/document/apn/rzv2l-quick-start-guide-rzv-multi-os-package-v300) [[4]](#id13)
11. Execute the commands stated below on the console to start zephyr application with CM33 core.
    Here, ‘’N’’ stands for the partition number in which you stored zephyr.bin file.

```shell
Hit any key to stop autoboot: 2
=> dcache off
=> mmc dev 1
=> fatload mmc 1:N 0x00010000 zephyr.bin
=> fatload mmc 1:N 0x40010000 zephyr.bin
=> cm33 start_normal 0x00010000 0x40010000
=> dcache on
```

## References

[[1](#id4)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-general-purpose-microprocessor-equipped-renesas-original-ai-accelerator-drp-ai-12ghz-dual-core-arm](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-general-purpose-microprocessor-equipped-renesas-original-ai-accelerator-drp-ai-12ghz-dual-core-arm)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-evkit-smarc-som-evaluation-kit-rzv2l-mpu-ai-accelerator](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzv2l-evkit-smarc-som-evaluation-kit-rzv2l-mpu-ai-accelerator)

[3]
([1](#id8),[2](#id9),[3](#id10),[4](#id11),[5](#id12))

[https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104](https://www.renesas.com/en/document/gde/smarc-evk-rzv2l-linux-start-guide-rev104)

[4]
([1](#id14),[2](#id15))

[https://www.renesas.com/en/document/apn/rzv2l-quick-start-guide-rzv-multi-os-package-v300](https://www.renesas.com/en/document/apn/rzv2l-quick-start-guide-rzv-multi-os-package-v300)
