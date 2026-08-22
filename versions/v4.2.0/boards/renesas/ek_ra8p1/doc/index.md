---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/ek_ra8p1/doc/index.html
original_path: boards/renesas/ek_ra8p1/doc/index.html
---

# RA8P1 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra8p1.webp](../../../../_images/ek_ra8p1.webp)
](../../../../_images/ek_ra8p1.webp)

RA8P1 Evaluation Kit

Name:
:   `ek_ra8p1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7ka8p1kflcac

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra8p1/doc/index.rst/../..)

## Overview

The EK-RA8P1 is an Evaluation Kit for Renesas RA8P1 MCU Group which integrates multiple series of software-compatible
Arm®-based 32-bit cores that share a common set of Renesas peripherals to facilitate design scalability and efficient
platform-based product development.

The MCU in this series incorporates a high-performance Arm® Cortex®-M85 core running up to 1 GHz and Arm®
Cortex®-M33 core running up to 250 MHz with the following features:

- Up to 1 MB MRAM
- 2 MB SRAM (256 KB of CM85 TCM RAM, 128 KB CM33 TCM RAM, 1664 KB of user SRAM)
- Arm® Ethos™-U55 NPU
- Octal Serial Peripheral Interface (OSPI)
- Layer 3 Ethernet Switch Module (ESWM), USBFS, USBHS, SD/MMC Host Interface
- Graphics LCD Controller (GLCDC)
- 2D Drawing Engine (DRW)
- MIPI DSI/CSI interface
- Analog peripherals
- Security and safety features

**MCU Native Pin Access**

- 1 GHz Arm Cortex-M85 and 250 MHz Arm Cortex-M33 based RA8P1 MCU in 289 pins, BGA package
- Native pin access through 2 x 20-pin, and 2 x 40-pin headers (no populated)
- Camera Expansion connector (present on the underside of the EK-RA8P1 board)
- 2-Lane MIPI Display connector (present on the underside of the EK-RA8P1 board)
- Parallel graphics display interface connector
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources - RA8P1 MCU oscillator and sub-clock oscillator crystals,
  providing precision 24.000 MHz and 32,768 Hz reference clocks.
  Additional low precision clocks are available internal to the RA8P1 MCU

**System Control and Ecosystem Access**

- USB Full Speed Host and Device (USB-C connector)
- Four 5V input sources

  - USB (Debug, Full Speed, High Speed)
  - External power supply (using surface mount clamp test points and power input vias)
- Three Debug modes

  - Debug on-board (SWD and JTAG)
  - Debug in (ETM, SWD, SWO and JTAG)
  - Debug out (SWD, SWO, and JTAG)
- User LEDs and buttons

  - Three User LEDs (red, blue, green)
  - Power LED (white) indicating availability of regulated power
  - Debug LED (yellow) indicating the debug connection
  - Ethernet LEDs (amber, yellow, green)
  - Two User buttons
  - One Reset button
- Five most popular ecosystems expansions

  - Two Seeed Grove system (I2C/I3C/Analog) connectors (not populated)
  - One SparkFun Qwiic connector (not populated)
  - Two Digilent Pmod (SPI, UART and I2C) connectors
  - Arduino (Uno R3) connector
  - MikroElektronika mikroBUS connector (not populated)
- MCU boot configuration jumper

**Special Feature Access**

- Ethernet (RJ45 RGMII interface)
- USB High Speed Host and Device (USB-C connector)
- 512 Mb (64 MB) External Octo-SPI Flash (present in the MCU Native Pin Access area of the EK-RA8P1 board)

## Hardware

Detailed hardware features can be found at:

- RA8P1 MCU: [RA8P1 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/ra8p1-group-users-manual-hardware)
- EK-RA8P1 board: [EK-RA8P1 - User’s Manual](https://www.renesas.com/en/document/mat/ek-ra8p1-v1-users-manual)

### Supported Features

The `ek_ra8p1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ek_ra8p1/r7ka8p1kflcac/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L32) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L651) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L660) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L15) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L22) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L40) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L47)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L82) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock out line[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L57)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L89) | [`renesas,ra-cgc-pll-out`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L108) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L118)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L212) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA External Bus Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L196) | [`renesas,ra-cgc-busclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk) |
| Comparator | on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L701) | [`renesas,ra-acmphs-global`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs-global.md#std-dtcompatible-renesas-ra-acmphs-global) |
| on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L706) | [`renesas,ra-acmphs`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs.md#std-dtcompatible-renesas-ra-acmphs) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L630) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas%2Cra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| Display | on-chip | Renesas Graphic LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L27) | [`renesas,ra-glcdc`](../../../../build/dts/api/bindings/display/renesas%2Cra-glcdc.md#std-dtcompatible-renesas-ra-glcdc) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L87) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L228) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic) |
| on-chip | Renesas RA SCI-B I2C controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L261) | [`renesas,ra-i2c-sci-b`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Memory controller | on-chip | Renesas RA SDRAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L19) | [`renesas,ra-sdram`](../../../../build/dts/api/bindings/memory-controllers/renesas%2Cra-sdram.md#std-dtcompatible-renesas-ra-sdram) |
| MIPI-DSI | on-chip | Renesas RA MIPI DSI host[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L34) | [`renesas,ra-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/renesas%2Cra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi) |
| Miscellaneous | on-chip | Renesas RA SCI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L249) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L621) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA ULPT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L677) | [`renesas,ra-ulpt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-ulpt.md#std-dtcompatible-renesas-ra-ulpt) |
| on-chip | Renesas RA External Interrupt[32 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L731) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L39) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L13) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L75) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L481) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| SDHC | on-chip | Renesas RA SDHC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1019) | [`renesas,ra-sdhc`](../../../../build/dts/api/bindings/sdhc/renesas%2Cra-sdhc.md#std-dtcompatible-renesas-ra-sdhc) |
| Serial controller | on-chip | Renesas RA SCI\_B UART controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L255) | [`renesas,ra8-uart-sci-b`](../../../../build/dts/api/bindings/serial/renesas%2Cra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b) |
| SPI | on-chip | Renesas RA8 SPI\_B controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L459) | [`renesas,ra8-spi-b`](../../../../build/dts/api/bindings/spi/renesas%2Cra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L64) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | Renesas RA ULPT TIMER[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L683) | [`renesas,ra-ulpt-timer`](../../../../build/dts/api/bindings/timer/renesas%2Cra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer) |

#### `ek_ra8p1/r7ka8p1kflcac/cm85` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L18) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L651) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L660) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L15) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L22) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L40) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L47) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock out line[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L57) | [`renesas,ra-cgc-pll-out`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L108) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L118)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L212) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA External Bus Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1xf.dtsi?plain=1#L196) | [`renesas,ra-cgc-busclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk) |
| Comparator | on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L701) | [`renesas,ra-acmphs-global`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs-global.md#std-dtcompatible-renesas-ra-acmphs-global) |
| on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L706) | [`renesas,ra-acmphs`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs.md#std-dtcompatible-renesas-ra-acmphs) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L630) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas%2Cra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| Display | on-chip | Renesas Graphic LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L27) | [`renesas,ra-glcdc`](../../../../build/dts/api/bindings/display/renesas%2Cra-glcdc.md#std-dtcompatible-renesas-ra-glcdc) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L87)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L178) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L235)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L228) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic) |
| on-chip | Renesas RA SCI-B I2C controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L261) | [`renesas,ra-i2c-sci-b`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8p1/ek_ra8p1_r7ka8p1kflcac_cm85.dts?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8p1/ek_ra8p1_r7ka8p1kflcac_cm85.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | Renesas RA SDRAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L19) | [`renesas,ra-sdram`](../../../../build/dts/api/bindings/memory-controllers/renesas%2Cra-sdram.md#std-dtcompatible-renesas-ra-sdram) |
| MIPI-DSI | on-chip | Renesas RA MIPI DSI host[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L34) | [`renesas,ra-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/renesas%2Cra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi) |
| Miscellaneous | on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L417)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L249) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L621) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA ULPT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L677) | [`renesas,ra-ulpt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-ulpt.md#std-dtcompatible-renesas-ra-ulpt) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L839)[30 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L731) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L26) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7ka8p1kflcac.dtsi?plain=1#L13) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L75) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L491)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L481) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| SDHC | on-chip | Renesas RA SDHC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L1019) | [`renesas,ra-sdhc`](../../../../build/dts/api/bindings/sdhc/renesas%2Cra-sdhc.md#std-dtcompatible-renesas-ra-sdhc) |
| Serial controller | on-chip | Renesas RA SCI\_B UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L423)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L255) | [`renesas,ra8-uart-sci-b`](../../../../build/dts/api/bindings/serial/renesas%2Cra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b) |
| SPI | on-chip | Renesas RA8 SPI\_B controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L470)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L459) | [`renesas,ra8-spi-b`](../../../../build/dts/api/bindings/spi/renesas%2Cra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L64) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| on-chip | Renesas RA ULPT TIMER[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x2.dtsi?plain=1#L683) | [`renesas,ra-ulpt-timer`](../../../../build/dts/api/bindings/timer/renesas%2Cra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer) |

Note

- Other hardware features are currently not supported by the port.

## Programming and Debugging

Applications for the `ek_ra8p1` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application on CM85 core.

```shell
# From the root of the zephyr repository
west build -b ek_ra8p1/r7ka8p1kflcac/cm85 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the S3 button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v4.2.0-xxx-xxxxxxxxxxxxx *****
Hello World! ek_ra8p1/r7ka8p1kflcac/cm85
```

### Flashing

Program can be flashed to EK-RA8P1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as described in [EK-RA8P1 - User’s Manual](https://www.renesas.com/en/document/mat/ek-ra8p1-v1-users-manual)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

## References

- [EK-RA8P1 Website](https://www.renesas.com/en/design-resources/boards-kits/ek-ra8p1)
- [RA8P1 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8p1-1ghz-arm-cortex-m85-and-ethos-u55-npu-based-ai-microcontroller)
