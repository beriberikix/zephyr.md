---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/ek_ra4l1/doc/index.html
original_path: boards/renesas/ek_ra4l1/doc/index.html
---

# RA4L1 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra4l1.webp](../../../../_images/ek_ra4l1.webp)
](../../../../_images/ek_ra4l1.webp)

RA4L1 Evaluation Kit

Name:
:   `ek_ra4l1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa4l1bd4cfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra4l1/doc/index.rst/../..)

## Overview

The Renesas RA4L1 group of 32-bit microcontrollers (MCUs) uses the high-performance Arm
Cortex®-M33 core. Share a common set of Renesas peripherals to facilitate design scalability
and efficient platform-based product development.

The MCU in this series incorporates a high-performance Arm Cortex®-M33 core running up to
80 MHz with the following features:

**MCU Native Pin Access**

- R7FA4L1BD4CFP MCU (referred to as RA MCU)
- 80 MHz, Arm® Cortex®-M33 core
- 512 KB Code Flash, 64 KB SRAM
- 100-pin LQFP package

**System Control and Ecosystem Access**

- USB Full Speed Host and Device (USB-C connector)
- Three 5 V input sources

  - USB (Debug, Full Speed)
  - External power supply (using surface mount clamp test points and power input vias)
- Three Debug modes

  - Debug on-board (SWD)
  - Debug in (SWD)
  - Debug out (SWD, SW0 and JTAG)
- User LEDs and buttons

  - Three User LEDs (red, blue, green)
  - Power LED (white) indicating availability of regulated power
  - Debug LED (yellow) indicating the debug connection
  - Two User buttons
  - One Reset button
- Five most popular ecosystems expansions

  > - 1 Seeed Grove® system (I3C) connector
  > - 1 Seeed Grove® system (I2C/Analog) connector
  > - 2 Digilent PmodTM (SPI, UART and I2C) connectors
  > - ArduinoTM (Uno R3) connector
  > - MikroElektronikaTM mikroBUS connector
- MCU boot configuration jumper

**Special Feature Access**

- 256 Mb (32 MB) External QUAD-SPI Flash
- CAN FD (3-pin header)
- Segment LCD Board Interface (50-pin header)

## Hardware

Detailed hardware features can be found at:

- RA4L1 MCU: [RA4L1 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/ra4l1-group-users-manual-hardware?r=25568281)
- EK-RA4L1 board: [EK-RA4L1 - User’s Manual](https://www.renesas.com/en/document/mat/ek-ra4l1-v1-users-manual?r=25570359)

Debug on-board:

> - Connector Used: USB-C (J10)

| Debug Modes | J6 | J6-A | J8 | J9 | J29 |
| --- | --- | --- | --- | --- | --- |
| Debug on-board | Open | Open | Jumper on pins 1-2 | Open | Jumpers on pins 1-2, 3-4, 5-6, 7-8 |

### Supported Features

The `ek_ra4l1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ek_ra4l1/r7fa4l1bd4cfp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L20) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L256) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas%2Cra-adc.md#std-dtcompatible-renesas-ra-adc) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L349) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L358) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L588) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L595) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L613) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L620) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L631) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L641)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L684) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L550) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas%2Cra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L267) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L274) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bd4cfp.dtsi?plain=1#L11) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas%2Cra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L56)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L76) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L282) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic) |
| I2S | on-chip | Renesas RA I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L571) | [`renesas,ra-i2s-ssie`](../../../../build/dts/api/bindings/i2s/renesas%2Cra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie) |
| I3C | on-chip | Renesas RA I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L245) | [`renesas,ra-i3c`](../../../../build/dts/api/bindings/i3c/renesas%2Cra-i3c.md#std-dtcompatible-renesas-ra-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra4l1/ek_ra4l1.dts?plain=1#L46) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra4l1/ek_ra4l1.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L43) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas%2Cra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L204)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L152) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L444)[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L390) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L541) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L27) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash memory binding for Renesas RA Code flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bd4cfp.dtsi?plain=1#L21) | [`renesas,ra-nv-code-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash) |
| on-chip | Flash memory binding for Renesas RA Data flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bd4cfp.dtsi?plain=1#L30) | [`renesas,ra-nv-data-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra4l1/ek_ra4l1.dts?plain=1#L217) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra4l1/ek_ra4l1.dts?plain=1#L69) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L146) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L299)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L289) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L212)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L158) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas%2Cra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SPI | on-chip | Renesas RA SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L234) | [`renesas,ra-spi`](../../../../build/dts/api/bindings/spi/renesas%2Cra-spi.md#std-dtcompatible-renesas-ra-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L51) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4l1bx.dtsi?plain=1#L534) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas%2Cra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

## Programming and Debugging

The `ek_ra4l1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `ek_ra4l1` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

### Flashing

Program can be flashed to EK-RA4L1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [EK-RA4L1 - User’s Manual](https://www.renesas.com/en/document/mat/ek-ra4l1-v1-users-manual?r=25570359)
3. Execute west command

> ```shell
> west flash -r jlink
> ```

## References

- [EK-RA4L1 Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ek-ra4l1-evaluation-kit-ra4l1-mcu-group)
- [RA4L1 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra4l1-80mhz-arm-cortex-m33-based-low-power-mcu-trustzone-segment-lcd-controller-and-advanced-security)
