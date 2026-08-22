---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32mp257f_ev1/doc/index.html
original_path: boards/st/stm32mp257f_ev1/doc/index.html
---

# STM32MP257F-EV1 Evaluation Board

Board Overview

[![../../../../_images/stm32mp257f_ev1.webp](../../../../_images/stm32mp257f_ev1.webp)
](../../../../_images/stm32mp257f_ev1.webp)

STM32MP257F-EV1 Evaluation Board

Name:
:   `stm32mp257f_ev1`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32mp257fxx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32mp257f_ev1/doc/index.rst/../..)

## Overview

The STM32MP257F-EV1 Evaluation board is designed as a complete demonstration
and development platform for the STMicroelectronics STM32MP257F microprocessor
based on Arm® dual-core Cortex®-A35 (1.5 GHz) and Cortex®-M33
(400 MHz), and the STPMIC25APQR companion chip.
Zephyr OS is ported to run on the Cortex®-M33 core, as a coprocessor of
the Cortex®-A35 core.

### Features:

- STM32MP257FAI3 microprocessor featuring dual-core Arm® Cortex®-A35,
  a Cortex®-M33 and a Cortex®-M0+ in a TFBGA436 package
- ST power management STPMIC25APQR
- Two 16-Gbit DDR4 DRAMs
- 512-Mbit (64 Mbytes) S-NOR flash memory
- 32-Gbit (4 Gbytes) eMMC v5.0
- Three 1-Gbit/s Ethernet (RGMII) with TSN switch compliant with IEEE-802.3ab
- High-speed USB Host 2-port hub
- High-speed USB Type-C® DRP
- Four user LEDs
- Two user, one tamper, and one reset push-buttons
- One wake-up button
- Four boot pin switches
- Board connectors:

  - Three Ethernet RJ45
  - Two USB Host Type-A
  - USB Type-C®
  - microSD™ card holder
  - Mini PCIe
  - Dual-lane MIPI CSI-2® camera module expansion connector
  - Two CAN FD
  - LVDS
  - MIPI10
  - GPIO expansion connector
  - mikroBUS™ expansion connector
  - VBAT for power backup
- On-board STLINK-V3EC debugger/programmer with USB re-enumeration capability
  Two Virtual COM ports (VCPs), and debug ports (JTAG/SWD)
- Mainlined open-source Linux® STM32 MPU OpenSTLinux Distribution and
  STM32CubeMP2 software with examples
- Linux® Yocto project, Buildroot, and STM32CubeIDE as
  development environments

More information about the board can be found at the
[STM32MP257F-EV1 website](https://www.st.com/en/evaluation-tools/stm32mp257f-ev1.html#overview) [[1]](#id2).

## Hardware

### Cores:

- 64-bit dual-core Arm® Cortex®-A35 with 1.5 GHz max frequency
  - 32-Kbyte I + 32-Kbyte D level 1 cache for each Cortex®-A35 core
  - 512-Kbyte unified level 2 cache
  - Arm® NEON™ and Arm® TrustZone®
- 32-bit Arm® Cortex®-M33 with FPU/MPU, Arm® TrustZone®,
  and 400 MHz max frequency
  - L1 16-Kbyte ICache / 16-Kbyte DCache for Cortex®-M33
- 32-bit Arm® Cortex®-M0+ in SmartRun domain with 200 MHz max
  frequency (up to 16 MHz in autonomous mode)

### Memories:

- External DDR memory up to 4 Gbytes
  - Up to DDR3L-2133 16/32-bit
  - Up to DDR4-2400 16/32-bit
  - Up to LPDDR4-2400 16/32-bit
- 808-Kbyte internal SRAM: 256-Kbyte AXI SYSRAM, 128-Kbyte AXI video RAM or
  SYSRAM extension, 256-Kbyte AHB SRAM, 128-Kbyte AHB SRAM with ECC in backup
  domain, 8-Kbyte SRAM with ECC in backup domain, 32 Kbytes in SmartRun domain
- Two Octo-SPI memory interfaces
- Flexible external memory controller with up to 16-bit data bus: parallel
  interface to connect external ICs, and SLC NAND memories with up to 8-bit ECC

### Power

- STPMIC25 for voltage regulation (multiple buck/LDO regulators)
- USB-C or 5V DC jack power input
- VBAT backup battery connector (RTC, backup SRAM)

### Clock management

- External oscillators:
  - 32.768 kHz LSE crystal
  - 40 MHz HSE crystal
- Internal oscillators:
  - 64 MHz HSI oscillator
  - 4 MHz CSI oscillator
  - 32 kHz LSI oscillator
  - Five separate PLLs with integer and fractional mode

### Security/Safety

- Secure boot, TrustZone® peripherals, active tamper, environmental
  monitors, display secure layers, hardware accelerators
- Complete resource isolation framework

### Connectivity

- 3x Gigabit Ethernet (RGMII, TSN switch capable)
- 2x CAN FD
- USB 2.0 High-Speed Host (dual-port)
- USB Type-C® DRP
- mikroBUS™ expansion
- GPIO expansion connector

### Display & Camera

- DSI interface (4-lane)
- LVDS interface (4-lane)
- Camera CSI-2 interface (2-lane)

### Debug

- STLINK-V3EC (onboard debugger with VCP, JTAG and SWD)

More information about STM32MP257F can be found here:

- [STM32MP257F on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html) [[3]](#id6)

### Supported Features

The `stm32mp257f_ev1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32mp257f_ev1/stm32mp257fxx/m33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L19) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| Clock control | on-chip | STM32MP2 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L35) | [`st,stm32mp2-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32mp2-rcc.md#std-dtcompatible-st-stm32mp2-rcc) |
| GPIO & Headers | on-chip | STM32MP2 GPIO Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L122)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L74) | [`st,stm32mp2-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32mp2-gpio.md#std-dtcompatible-st-stm32mp2-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp257f_ev1/stm32mp257f_ev1_stm32mp257fxx_m33.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L47) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32mp257f_ev1/stm32mp257f_ev1_stm32mp257fxx_m33.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L68) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L41) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| Serial controller | on-chip | STM32 USART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L163) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L199)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L190) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/mp2/stm32mp2_m33.dtsi?plain=1#L26) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

### Connections and IOs

STM32MP257F-EV1 Evaluation Board schematic is available here:
[STM32MP257F-EV1 Evaluation board schematics](https://www.st.com/resource/en/schematic_pack/mb1936-mp257f-x-d01-schematic.pdf) [[2]](#id4)

### System Clock

#### Cortex®-A35

Not yet supported in Zephyr.

#### Cortex®-M33

The Cortex®-M33 Core is configured to run at a 400 MHz clock speed.

## Programming and Debugging

The `stm32mp257f_ev1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Prerequisite

Before you can run Zephyr on the STM32MP257F-EV1 Evaluation board, you need to
set up the Cortex®-A35 core with a Linux® environment. The Cortex®-M33 core runs Zephyr as a coprocessor, and it requires the Cortex®-A35 to load and start the firmware using remoteproc.

One way to set up the Linux environment is to use the official ST
OpenSTLinux distribution, following the [Starter Package](https://wiki.st.com/stm32mpu/wiki/STM32MP25_Evaluation_boards_-_Starter_Package) [[5]](#id11). (more information
about the procedure can be found in the [STM32MPU Wiki](https://wiki.st.com/stm32mpu/wiki/Main_Page) [[6]](#id13))

### Loading the firmware

Once the OpenSTLinux distribution is installed on the board, the Cortex®
-A35 is responsible (in the current distribution) for loading the Zephyr
firmware image in DDR and/or SRAM and starting the Cortex® -M33 core. The
application can be built using west, taking the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") as
an example.

```shell
# From the root of the zephyr repository
west build -b stm32mp257f_ev1/stm32mp257fxx/m33 samples/basic/blinky
```

The firmware can be copied to the board file system and started with the Linux
remoteproc framework. (more information about the procedure can be found in the
[STM32MP257F boot Cortex-M33 firmware](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs) [[4]](#id8))

### Debugging

Applications can be debugged using OpenOCD and GDB. The OpenOCD files can be
found at [device-stm-openocd](https://github.com/STMicroelectronics/device-stm-openocd/tree/main) [[7]](#id15).
The firmware must first be started by the Cortex®-A35. The debugger can
then be attached to the running Zephyr firmware using OpenOCD.

- Build the sample:

```shell
# From the root of the zephyr repository
west build -b stm32mp257f_ev1/stm32mp257fxx/m33 samples/basic/blinky
```

- Copy the firmware to the board, load it and start it with remoteproc
  ([STM32MP257F boot Cortex-M33 firmware](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs) [[4]](#id8)). The orange LED should be blinking.
- Attach to the target:

```shell
$ west attach
```

### References

[[1](#id3)]

[https://www.st.com/en/evaluation-tools/stm32mp257f-ev1.html#overview](https://www.st.com/en/evaluation-tools/stm32mp257f-ev1.html#overview)

[[2](#id5)]

[https://www.st.com/resource/en/schematic\_pack/mb1936-mp257f-x-d01-schematic.pdf](https://www.st.com/resource/en/schematic_pack/mb1936-mp257f-x-d01-schematic.pdf)

[[3](#id7)]

[https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html](https://www.st.com/en/microcontrollers-microprocessors/stm32mp257f.html)

[4]
([1](#id9),[2](#id10))

[https://wiki.st.com/stm32mpu/wiki/Linux\_remoteproc\_framework\_overview#Remote\_processor\_boot\_through\_sysfs](https://wiki.st.com/stm32mpu/wiki/Linux_remoteproc_framework_overview#Remote_processor_boot_through_sysfs)

[[5](#id12)]

[https://wiki.st.com/stm32mpu/wiki/STM32MP25\_Evaluation\_boards\_-\_Starter\_Package](https://wiki.st.com/stm32mpu/wiki/STM32MP25_Evaluation_boards_-_Starter_Package)

[[6](#id14)]

[https://wiki.st.com/stm32mpu/wiki/Main\_Page](https://wiki.st.com/stm32mpu/wiki/Main_Page)

[[7](#id16)]

[https://github.com/STMicroelectronics/device-stm-openocd/tree/main](https://github.com/STMicroelectronics/device-stm-openocd/tree/main)
