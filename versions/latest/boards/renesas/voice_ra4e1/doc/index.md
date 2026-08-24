---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/voice_ra4e1/doc/index.html
original_path: boards/renesas/voice_ra4e1/doc/index.html
---

# RA4E1 Voice User Reference Kit

Board Overview

[![../../../../_images/voice_ra4e1.webp](https://docs.zephyrproject.org/4.2.0/_images/voice_ra4e1.webp)
](https://docs.zephyrproject.org/4.2.0/_images/voice_ra4e1.webp)

RA4E1 Voice User Reference Kit

Name:
:   `voice_ra4e1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa4e10d2cne

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/voice_ra4e1/doc/index.rst/../..)

## Overview

VOICE-RA4E1 is an edge voice recognition evaluation kit designed to be used by Ecosystem Partners,
Application Engineers, Field Application Engineers, and for Business Development opportunities. The
primary purpose is to evaluate the functionality of projects developed by Ecosystem Partners, and to
facilitate the development of additional partner projects. The kit design to use the RA4E1 MCU with QFN
48pin package as the core logic device, with QSPI flash, OPAMP and power devices chosen from the
Renesas product portfolio.

The MCU in this series incorporates a high-performance Arm Cortex®-M33 core running up to
100 MHz with the following features:

**MCU Native Pin Access**

- R7FA4E10D2CNE MCU (referred to as RA MCU)
- 100 MHz, Arm® Cortex®-M33 core
- 512 KB Code Flash, 8 KB Data Flash, 128 KB SRAM
- 48 pins, LQFP package
- MCU current measurement point for precision current consumption measurement
- Multiple clock sources - Low-precision (~1%) clocks are available internal to the RA MCU.

**Kit Peripheral Features**

Following is a list of the specific features that have been implemented:

- QSPI: One QSPI flash memory device, Dialog AT25SF641B-MHB-T, 64M-bit (8MB).
- PMOD: 1 Digilent PMOD connectors, supporting UART, SPI and I2C configurations.
- Microphones: 1 I2S MEMS digital microphones and 2 MEMS analog microphones, distance between
  each pair of microphones is 50mm which is suitable for beamforming applications.
- Audio out: One stereo audio headphone jack supporting mono output on both channels.
- LEDs: Five LEDs, D2 (Red), D3 (Green) and D4 (Blue) configurable by user, D5 (Blue) as a 3.3V power
  indicator, D8(Green) as a JLOB (J-LINK on board) indicator.
- Buttons: One RESET button (S2), and one USER button (S1).
- Debug: J-Link On-Board debug interface, supporting JTAG or SWD debug port.
- USB: Micro USB-B (J6) for power input and J-Link On-Board function, USB-C (J1) for power input and
  RA4E1 USB Full Speed port as a USB device.
- Form Factor: 7.5 x 6 cm

## Hardware

Detailed hardware features can be found at:

- RA4E1 MCU: [RA4E1 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/ra4e1-group-users-manual-hardware)
- VOICE-RA4E1 board: [VOICE-RA4E1 - Engineering Manual](https://www.renesas.com/en/document/mat/voice-ra4e1-engineering-manual)

### Supported Features

The `voice_ra4e1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `voice_ra4e1/r7fa4e10d2cne` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L18) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L273) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas,ra-adc.md#std-dtcompatible-renesas-ra-adc) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L77) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L84) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L102) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L109) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L130) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L140)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L183) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| Counter | on-chip | Renesas RA AGT as Counter[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L192) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas,ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L293) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas,ra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L299) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas,ra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L49) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas,ra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L68)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L58) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L314) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas,ra-iic.md#std-dtcompatible-renesas-ra-iic) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/voice_ra4e1/voice_ra4e1.dts?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/voice_ra4e1/voice_ra4e1.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L41) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas,ra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L27)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L124) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L183) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas,ra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L401)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L365) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas,ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L25) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash memory binding for Renesas RA Code flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10d2cne.dtsi?plain=1#L16) | [`renesas,ra-nv-code-flash`](../../../../build/dts/api/bindings/mtd/renesas,ra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash) |
| on-chip | Flash memory binding for Renesas RA Data flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10d2cne.dtsi?plain=1#L25) | [`renesas,ra-nv-data-flash`](../../../../build/dts/api/bindings/mtd/renesas,ra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/voice_ra4e1/voice_ra4e1.dts?plain=1#L116) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L557) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L118) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L519) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas,ra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| RNG | on-chip | Renesas RA SCE9 TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L67) | [`renesas,ra-sce9-rng`](../../../../build/dts/api/bindings/rng/renesas,ra-sce9-rng.md#std-dtcompatible-renesas-ra-sce9-rng) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L33)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L131) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SPI | on-chip | Renesas RA SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L152) | [`renesas,ra-spi`](../../../../build/dts/api/bindings/spi/renesas,ra-spi.md#std-dtcompatible-renesas-ra-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4e10x.dtsi?plain=1#L22) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L328) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L338) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-udc.md#std-dtcompatible-renesas-ra-udc) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm33-common.dtsi?plain=1#L549) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas,ra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

## Programming and Debugging

The `voice_ra4e1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `voice_ra4e1` board can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

Program can be flashed to VOICE-RA4E1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [VOICE-RA4E1 - Engineering Manual](https://www.renesas.com/en/document/mat/voice-ra4e1-engineering-manual)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA4E10D
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that we can debug OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [VOICE-RA4E1 Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/tw001-vuia4e1pocz-ra4e1-voice-user-reference-kit)
- [RA4E1 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra4e1-100mhz-arm-cortex-m33-entry-line-balanced-low-power-consumption-optimized-feature-integration)
