---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzg2l_smarc/doc/index.html
original_path: boards/renesas/rzg2l_smarc/doc/index.html
---

# RZ/G2L SMARC Evaluation Board Kit

Board Overview

[![../../../../_images/rzg2l_smarc.webp](https://docs.zephyrproject.org/4.2.0/_images/rzg2l_smarc.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzg2l_smarc.webp)

RZ/G2L SMARC Evaluation Board Kit

Name:
:   `rzg2l_smarc`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a07g044l23gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzg2l_smarc/doc/index.rst/../..)

## Overview

The Renesas RZ/G2L SMARC Evaluation Board Kit (RZ/G2L-EVKIT) consists of a SMARC v2.1 module board and a carrier board.

- Device: RZ/G2L R9A07G044L23GBG

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
  - The Micro-AB receptacles are implemented for connection to asynchronous serial port interface.
  - The microSD card slot and two sockets for PMOD are implemented as an interface for peripheral functions.
  - For power supply, a mounted USB Type-C receptacle supports the USB PD standard.

## Hardware

The Renesas RZ/G2L MPU documentation can be found at [RZ/G2L Group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzg2l-general-purpose-mpu-dual-core-arm-cortex-a55-cpus-and-single-core-cortex-m33-cpu-3d-graphics-and) [[1]](#id3)

[![RZ/G2L group feature](https://docs.zephyrproject.org/4.2.0/_images/rzg2l_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzg2l_block_diagram.webp)

RZ/G2L block diagram (Credit: Renesas Electronics Corporation)

### Supported Features

The `rzg2l_smarc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzg2l_smarc/r9a07g044l23gbg/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L19) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| GPIO & Headers | on-chip | Renesas RZ GPIO Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L40) | [`renesas,rz-gpio-int`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio-int.md#std-dtcompatible-renesas-rz-gpio-int) |
| on-chip | Renesas RZ GPIO controller[49 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L55) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L27) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | Renesas RZ/G pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L35) | [`renesas,rzg-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas,rzg-pinctrl.md#std-dtcompatible-renesas-rzg-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCIF UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L514)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzg/r9a07g044.dtsi?plain=1#L496) | [`renesas,rz-scif-uart`](../../../../build/dts/api/bindings/serial/renesas,rz-scif-uart.md#std-dtcompatible-renesas-rz-scif-uart) |
| SRAM | on-board | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzg2l_smarc/rzg2l_smarc_r9a07g044l23gbg_cm33.dts?plain=1#L23) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

## Programming and Debugging

Applications for the `rzg2l_smarc` board can be built in the usual way as
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
west build -b rzg2l_smarc/r9a07g044l23gbg/cm33 samples/hello_world
west debug
```

### Flashing

RZ/G2L-EVKIT is designed to start different systems on different cores.
It uses Yocto as the build system to build Linux system and boot loaders
to run Zephyr on Cortex-M33 with u-boot. The minimal steps are described below.

1. Follow “2.2 Building Images” of [SMARC EVK of RZ/G2L, RZ/G2LC, RZ/G2UL Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105) [[2]](#id5) to prepare the build environment.
2. At step (4), follow step “2. Download Multi-OS Package” and “3. Add the layer for Multi-OS Package”
   of “3.2 OpenAMP related stuff Integration for RZ/G2L, RZ/G2LC and RZ/G2UL” of [Release Note for RZ/G Multi-OS Package V2.0.2](https://www.renesas.com/us/en/document/rln/release-note-rzg-multi-os-package-v202) [[3]](#id11)
   to add the layer for Multi-OS Package.

   ```shell
   $ cd ~/rzg_vlp_<pkg ver>
   $ unzip <Multi-OS Dir>/r01an5869ej0202-rzg-multi-os-pkg.zip
   $ tar zxvf r01an5869ej0202-rzg-multi-os-pkg/meta-rz-features_multi-os_v2.0.2.tar.gz
   $ bitbake-layers add-layer ../meta-rz-features/meta-rz-multi-os/meta-rzg2l
   ```
3. Start the build:

   ```shell
   $ MACHINE=smarc-rzg2l bitbake core-image-minimal
   ```

   The below necessary artifacts will be located in the build/tmp/deploy/images

   | Artifacts | File name |
   | --- | --- |
   | Boot loader | bl2\_bp-smarc-rzg2l\_pmic.srec  fip-smarc-rzg2l\_pmic.srec |
   | Flash Writer | Flash\_Writer\_SCIF\_RZG2L\_SMARC\_PMIC\_DDR4\_2GB\_1PCS.mot |
4. Follow “4.2 Startup Procedure” of [SMARC EVK of RZ/G2L, RZ/G2LC, RZ/G2UL Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105) [[2]](#id5) for power supply and board setting
   at SCIF download (SW11[1:4] = OFF, ON, OFF, ON) and (SW1[1:2] = ON, OFF)
5. Follow “4.3 Download Flash Writer to RAM” of [SMARC EVK of RZ/G2L, RZ/G2LC, RZ/G2UL Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105) [[2]](#id5) to download Flash Writer to RAM
6. Follow “4.4 Write the Bootloader” of [SMARC EVK of RZ/G2L, RZ/G2LC, RZ/G2UL Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105) [[2]](#id5) to write the boot loader
   to the target board by using Flash Writer.
7. Follow “4.5 Change Back to Normal Boot Mode” with switch setting (SW11[1:4] = OFF, OFF, OFF, ON) and (SW1[1:2] = ON, OFF)
8. Follow “3. Preparing the SD Card” of [SMARC EVK of RZ/G2L, RZ/G2LC, RZ/G2UL Linux Start-up Guide](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105) [[2]](#id5) to write files to the microSD Card
9. Copy zephyr.bin file to microSD card
10. Follow “4.4.2 CM33 Sample Program Invocation with u-boot” from the beginning to step 4 of [Release Note for RZ/G Multi-OS Package V2.0.2](https://www.renesas.com/us/en/document/rln/release-note-rzg-multi-os-package-v202) [[3]](#id11)
11. Execute the commands stated below on the console to start zephyr application with CM33 core.
    Here, ‘’N’’ stands for the partition number in which you stored zephyr.bin file.

> ```shell
> Hit any key to stop autoboot: 2
> => dcache off
> => mmc dev 1
> => fatload mmc 1:N 0x00010000 zephyr.bin
> => fatload mmc 1:N 0x40010000 zephyr.bin
> => cm33 start_normal 0x00010000 0x40010000
> => dcache on
> ```

## References

[[1](#id4)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzg2l-general-purpose-mpu-dual-core-arm-cortex-a55-cpus-and-single-core-cortex-m33-cpu-3d-graphics-and](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzg2l-general-purpose-mpu-dual-core-arm-cortex-a55-cpus-and-single-core-cortex-m33-cpu-3d-graphics-and)

[2]
([1](#id6),[2](#id7),[3](#id8),[4](#id9),[5](#id10))

[https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105](https://www.renesas.com/en/document/gde/smarc-evk-rzg2l-rzg2lc-rzg2ul-linux-start-guide-rev105)

[3]
([1](#id12),[2](#id13))

[https://www.renesas.com/us/en/document/rln/release-note-rzg-multi-os-package-v202](https://www.renesas.com/us/en/document/rln/release-note-rzg-multi-os-package-v202)
