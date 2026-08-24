---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/ek_ra8d1/doc/index.html
original_path: boards/renesas/ek_ra8d1/doc/index.html
---

# RA8D1 Evaluation Kit

Board Overview

[![../../../../_images/ek_ra8d1.jpg](https://docs.zephyrproject.org/4.2.0/_images/ek_ra8d1.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/ek_ra8d1.jpg)

RA8D1 Evaluation Kit

Name:
:   `ek_ra8d1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa8d1bhecbd

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra8d1/doc/index.rst/../..)

## Overview

The EK-RA8D1 is an Evaluation Kit for Renesas RA8D1 MCU Group which are the industry’s first 32-bit
graphics-enabled MCUs based on the Arm Cortex-M85 (CM85) core, delivering breakthrough performance
of over 3000 Coremark points at 480 MHz and superior graphics capabilities that enable high-resolution
displays and Vision AI applications.

The key features of the EK-RA8D1 board are categorized in three groups as follow:

**MCU Native Pin Access**

- 480MHz Arm Cortex-M85 based RA8D1 MCU in 224 pins, BGA package
- Native pin acces througgh 2 x 50-pin, and 2 x 40-pin male headers
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources - RA8D1 MCU oscillator and sub-clock oscillator crystals,
  providing precision 20.000MHz and 32,768 Hz refeence clocks.
  Additional low precision clocks are available internal to the RA8D1 MCU

**System Control and Ecosystem Access**

- USB Full Speed Host and Device (micro-AB connector)
- Four 5V input sources

  - USB (Debug, Full Speed, High Speed)
  - External power supply (using surface mount clamp test points and power input vias)
- Three Debug modes

  - Debug on-board (SWD)
  - Debug in (ETM, SWD and JTAG)
  - Debug out (SWD)
- User LEDs and buttons

  - Three User LEDs (red, blue, green)
  - Power LED (white) indicating availability of regulated power
  - Debug LED (yellow) indicating the debug connection
  - Two User buttons
  - One Reset button
- Five most popular ecosystems expansions

  - Two Seeed Grove system (I2C/I3C) connectors
  - One SparkFun Qwiic connector
  - Two Digilent Pmod (SPI, UART and I2C/I3C) connectors
  - Arduino (Uno R3) connector
  - MikroElektronika mikroBUS connector
- MCU boot configuration jumper

**Special Feature Access**

- Ethernet (RJ45 RMII interface)
- USB High Speed Host and Device (micro-AB connector)
- 512 Mb (64 MB) External Octo-SPI Flash (present in the MCU Native Pin Access area of the EK-RA8D1 board)
- CAN FD (3-pin header)

## Hardware

Detailed Hardware features for the RA8D1 MCU group can be found at [RA8D1 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/ra8d1-group-users-manual-hardware)

[![RA8D1 MCU group feature](https://docs.zephyrproject.org/4.2.0/_images/ra8d1_block_diagram.png)
](https://docs.zephyrproject.org/4.2.0/_images/ra8d1_block_diagram.png)

RA8D1 Block diagram (Credit: Renesas Electronics Corporation)

Detailed Hardware features for the EK-RA8D1 MCU can be found at [EK-RA8D1 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra8d1-v1-user-manual)

### Supported Features

The `ek_ra8d1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ek_ra8d1/r7fa8d1bhecbd` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L19) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm,cortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L354)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L365) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas,ra-adc.md#std-dtcompatible-renesas-ra-adc) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L668) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas,ra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L679)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L689) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas,ra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L46) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L53) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L71) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L78) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock out line[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L87)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L129) | [`renesas,ra-cgc-pll-out`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L147) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L157)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L227) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA External Bus Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L210) | [`renesas,ra-cgc-busclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk) |
| Comparator | on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L911) | [`renesas,ra-acmphs-global`](../../../../build/dts/api/bindings/comparator/renesas,ra-acmphs-global.md#std-dtcompatible-renesas-ra-acmphs-global) |
| on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L916) | [`renesas,ra-acmphs`](../../../../build/dts/api/bindings/comparator/renesas,ra-acmphs.md#std-dtcompatible-renesas-ra-acmphs) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L645) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas,ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L376) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas,ra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L382)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L389) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas,ra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Display | on-chip | Renesas Graphic LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L21) | [`renesas,ra-glcdc`](../../../../build/dts/api/bindings/display/renesas,ra-glcdc.md#std-dtcompatible-renesas-ra-glcdc) |
| Ethernet | on-chip | Renesas RA Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L700) | [`renesas,ra-ethernet`](../../../../build/dts/api/bindings/ethernet/renesas,ra-ethernet.md#std-dtcompatible-renesas-ra-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L295) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L345) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas,ra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| on-board | Renesas RA OSPI FLASH[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L400) | [`renesas,ra-ospi-b-nor`](../../../../build/dts/api/bindings/flash_controller/renesas,ra-ospi-b-nor.md#std-dtcompatible-renesas-ra-ospi-b-nor) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L77)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L97) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| on-board | GPIO pins exposed on Renesas MIPI lcd display headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L69) | [`renesas,ra-gpio-mipi-header`](../../../../build/dts/api/bindings/gpio/renesas,mipi-header.md#std-dtcompatible-renesas-ra-gpio-mipi-header) |
| I2C | on-chip | Renesas RA I2C Master controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L198) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas,ra-iic.md#std-dtcompatible-renesas-ra-iic) |
| on-chip | Renesas RA SCI-B I2C controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L226) | [`renesas,ra-i2c-sci-b`](../../../../build/dts/api/bindings/i2c/renesas,ra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b) |
| I2S | on-chip | Renesas RA I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L929) | [`renesas,ra-i2s-ssie`](../../../../build/dts/api/bindings/i2s/renesas,ra-i2s-ssie.md#std-dtcompatible-renesas-ra-i2s-ssie) |
| I3C | on-chip | Renesas RA I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L427) | [`renesas,ra-i3c`](../../../../build/dts/api/bindings/i3c/renesas,ra-i3c.md#std-dtcompatible-renesas-ra-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L47) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Renesas RA External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L709) | [`renesas,ra-mdio`](../../../../build/dts/api/bindings/mdio/renesas,ra-mdio.md#std-dtcompatible-renesas-ra-mdio) |
| Memory controller | on-chip | Renesas RA SDRAM controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L13) | [`renesas,ra-sdram`](../../../../build/dts/api/bindings/memory-controllers/renesas,ra-sdram.md#std-dtcompatible-renesas-ra-sdram) |
| MIPI-DSI | on-chip | Renesas RA MIPI DSI host[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L30) | [`renesas,ra-mipi-dsi`](../../../../build/dts/api/bindings/mipi-dsi/renesas,ra-mipi-dsi.md#std-dtcompatible-renesas-ra-mipi-dsi) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L63) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas,ra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L323)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L213) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA ULPT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L578) | [`renesas,ra-ulpt`](../../../../build/dts/api/bindings/misc/renesas,ra-ulpt.md#std-dtcompatible-renesas-ra-ulpt) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L634) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas,ra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L824)[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L716) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas,ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L27) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| MTD | on-chip | Flash memory binding for Renesas RA Code flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1bhecbd.dtsi?plain=1#L16) | [`renesas,ra-nv-code-flash`](../../../../build/dts/api/bindings/mtd/renesas,ra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash) |
| on-chip | Flash memory binding for Renesas RA Data flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1bhecbd.dtsi?plain=1#L25) | [`renesas,ra-nv-data-flash`](../../../../build/dts/api/bindings/mtd/renesas,ra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra8d1/ek_ra8d1.dts?plain=1#L246) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | Renesas RA OSPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L604) | [`renesas,ra-ospi-b`](../../../../build/dts/api/bindings/ospi/renesas,ra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L954) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| on-chip | Renesas RA USBHS internal PHY controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L300) | [`renesas,ra-usbphyc`](../../../../build/dts/api/bindings/phy/renesas,ra-usbphyc.md#std-dtcompatible-renesas-ra-usbphyc) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L71) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L508)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L438) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas,ra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| RNG | on-chip | Renesas RA RSIP-E51A TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L397) | [`renesas,ra-rsip-e51a-trng`](../../../../build/dts/api/bindings/rng/renesas,ra-rsip-e51a-trng.md#std-dtcompatible-renesas-ra-rsip-e51a-trng) |
| SDHC | on-chip | Renesas RA SDHC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L860) | [`renesas,ra-sdhc`](../../../../build/dts/api/bindings/sdhc/renesas,ra-sdhc.md#std-dtcompatible-renesas-ra-sdhc) |
| Serial controller | on-chip | Renesas RA SCI\_B UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L330)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L220) | [`renesas,ra8-uart-sci-b`](../../../../build/dts/api/bindings/serial/renesas,ra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b) |
| SPI | on-chip | Renesas RA8 SPI\_B controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L414)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L401) | [`renesas,ra8-spi-b`](../../../../build/dts/api/bindings/spi/renesas,ra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| on-chip | Renesas RA ULPT TIMER[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L586) | [`renesas,ra-ulpt-timer`](../../../../build/dts/api/bindings/timer/renesas,ra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L895) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L293)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L905) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-udc.md#std-dtcompatible-renesas-ra-udc) |
| on-chip | Renesas RA USB high-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8d1xh.dtsi?plain=1#L284) | [`renesas,ra-usbhs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbhs.md#std-dtcompatible-renesas-ra-usbhs) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L888) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas,ra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

Note

- For using Ethernet on RA8D1 board please set switch SW1 as following configuration:

  | SW1-1 PMOD1 | SW1-2 TRACE | SW1-3 CAMERA | SW1-4 ETHA | SW1-5 ETHB | SW1-6 GLCD | SW1-7 SDRAM | SW1-8 I3C |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF | ON | OFF | OFF | OFF |
- For using SDHC channel 1 on RA8D1 board please set switch SW1 as following configuration:

  | SW1-1 PMOD1 | SW1-2 TRACE | SW1-3 CAMERA | SW1-4 ETHA | SW1-5 ETHB | SW1-6 GLCD | SW1-7 SDRAM | SW1-8 I3C |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF | OFF | OFF | OFF | OFF |
- For using MIPI Graphics Expansion Port (J58) on RA8D1 board please set switch SW1 as following configuration:

  | SW1-1 PMOD1 | SW1-2 TRACE | SW1-3 CAMERA | SW1-4 ETHA | SW1-5 ETHB | SW1-6 GLCD | SW1-7 SDRAM | SW1-8 I3C |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF | OFF | ON | ON | OFF |
- For using the Parallel Graphics Expansion Port (J57) with the Graphics Expansion Board supplied as part of the kit,
  please set switch SW1 as following configuration:

  | SW1-1 PMOD1 | SW1-2 TRACE | SW1-3 CAMERA | SW1-4 ETHA | SW1-5 ETHB | SW1-6 GLCD | SW1-7 SDRAM | SW1-8 I3C |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF | OFF | ON | ON | OFF |
- For using I3C on RA8D1 board please set switch SW1 as following configuration:

  | SW1-1 PMOD1 | SW1-2 TRACE | SW1-3 CAMERA | SW1-4 ETHA | SW1-5 ETHB | SW1-6 GLCD | SW1-7 SDRAM | SW1-8 I3C |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | OFF | OFF | OFF | OFF | OFF | OFF | OFF | ON |

Warning

Do not enable SW1-4 and SW1-5 together

## Programming and Debugging

The `ek_ra8d1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `ek_ra8d1` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

**Note:** Only support from SDK v0.16.6 in which GCC for Cortex Arm-M85 was available.
To build for EK-RA8M1 user need to get and install GNU Arm Embedded toolchain from [https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6)

### Flashing

Program can be flashed to EK-RA8D1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [EK-RA8D1 - User’s Manual](https://www.renesas.com/us/en/document/mat/ek-ra8d1-v1-user-manual)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA8D1BH
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that debug is OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [EK-RA8D1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ek-ra8d1-evaluation-kit-ra8d1-mcu-group)
- [RA8D1 MCU group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8d1-480-mhz-arm-cortex-m85-based-graphics-microcontroller-helium-and-trustzone)
