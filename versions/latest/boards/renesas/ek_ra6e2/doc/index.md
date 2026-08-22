---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/ek_ra6e2/doc/index.html
original_path: boards/renesas/ek_ra6e2/doc/index.html
---

# RA6E2 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra6e2.webp](../../../../_images/ek_ra6e2.webp)
](../../../../_images/ek_ra6e2.webp)

RA6E2 Evaluation Kit

Name:
:   `ek_ra6e2`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa6e2bb3cfm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra6e2/doc/index.rst/../..)

## Overview

The EK-RA6E2, an Evaluation Kit for RA6E2 MCU Group, enables users to
seamlessly evaluate the features of the RA6E2 MCU group and develop
embedded systems applications using Flexible Software Package (FSP)
and e2 studio IDE. The users can use rich on-board features along with
their choice of popular ecosystems add-ons to bring their big ideas to life

The key features of the EK-RA6E2 board are categorized in three groups as follow:

**MCU Native Pin Access**

- 200MHz Arm Cortex-M33 based RA6E2 MCU in 64 pins, LQFP package
- 256 kB Code Flash, 40 kB SRAM
- Native pin access through 2 x 14-pin and 1 x 40-pin male headers
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources - RA6E2 MCU oscillator and sub-clock oscillator crystals,
  providing precision 20.000 MHz and 32,768 Hz reference clock.
  Additional low precision clocks are available internal to the RA6E2 MCU

**System Control and Ecosystem Access**

- USB Full Speed Host and Device (micro-AB connector)
- Three 5V input sources

  - USB (Debug, Full Speed)
  - External power supply (using surface mount clamp test points and J31 through holes)
- Three Debug modes

  - Debug on-board (SWD)
  - Debug in (SWD)
  - Debug out (JTAG, SWD)
- User LEDs and buttons

  - Three User LEDs (red, blue, green)
  - Power LED (white) indicating availability of regulated power
  - Debug LED (yellow) indicating the debug connection
  - Two User buttons
  - One Reset button
- Five most popular ecosystems expansions

  - Two Seeed Grove system (I3C/Analog) connectors
  - One SparkFun Qwiic connector
  - Two Digilent Pmod (SPI and UART) connectors
  - Arduino (Uno R3) connector
  - MikroElektronika mikroBUS connector
- MCU boot configuration jumper

**Special Feature Access**

- 16 Mb (128 Mb) External Quad-SPI Flash
- CAN (3-pin header)

## Hardware

Detailed hardware features for the RA6E2 MCU group can be found at [RA6E2 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/ra6e2-group-users-manual-hardware)

[![RA6E2 MCU group feature](../../../../_images/ra6e2_block_diagram.webp)
](../../../../_images/ra6e2_block_diagram.webp)

RA6E2 Block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the EK-RA6E2 MCU can be found at [EK-RA6E2 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra6e2-v1-users-manual)

### Supported Features

The `ek_ra6e2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ek_ra6e2/r7fa6e2bb3cfm` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L19) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L270) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas%2Cra-adc.md#std-dtcompatible-renesas-ra-adc) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L52) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L62) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L133) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L140) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L158) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L165) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L176) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L186)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L229) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L107) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas%2Cra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L290) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L296)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L303) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L334) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas%2Cra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L50)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L100) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L144) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra6e2/ek_ra6e2.dts?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra6e2/ek_ra6e2.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L42) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas%2Cra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L116)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L130) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L438)[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L357) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L98) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L26) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash memory binding for Renesas RA Code flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bb3cfm.dtsi?plain=1#L15) | [`renesas,ra-nv-code-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash) |
| on-chip | Flash memory binding for Renesas RA Data flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bb3cfm.dtsi?plain=1#L24) | [`renesas,ra-nv-data-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra6e2/ek_ra6e2.dts?plain=1#L177) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L110) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L501)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L511) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| RNG | on-chip | Renesas RA TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L93) | [`renesas,ra-trng`](../../../../build/dts/api/bindings/rng/renesas%2Cra-trng.md#std-dtcompatible-renesas-ra-trng) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L123)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L137) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas%2Cra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SPI | on-chip | Renesas RA SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L158)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L169) | [`renesas,ra-spi`](../../../../build/dts/api/bindings/spi/renesas%2Cra-spi.md#std-dtcompatible-renesas-ra-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/r7fa6e2bx.dtsi?plain=1#L26) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra6/ra6-cm33-common.dtsi?plain=1#L541) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas%2Cra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

## Programming and Debugging

The `ek_ra6e2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `ek_ra6e2` board target configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

Program can be flashed to EK-RA6E2 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [EK-RA6E2 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra6e2-v1-users-manual)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA6E2BB
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that we can debug OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [EK-RA6E2 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ek-ra6e2-evaluation-kit-ra6e2-mcu-group)
- [RA6E2 MCU group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra6e2-entry-line-200mhz-arm-cortex-m33-general-purpose-microcontroller)
