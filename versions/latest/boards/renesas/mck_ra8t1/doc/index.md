---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/mck_ra8t1/doc/index.html
original_path: boards/renesas/mck_ra8t1/doc/index.html
---

# RA8T1 Motor Control Kit

Board Overview

[![../../../../_images/mck_ra8t1.jpg](../../../../_images/mck_ra8t1.jpg)
](../../../../_images/mck_ra8t1.jpg)

RA8T1 Motor Control Kit

Name:
:   `mck_ra8t1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa8t1ahecbd

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/mck_ra8t1/doc/index.rst/../..)

## Overview

The **MCK-RA8T1** is a development kit that enables easy evaluation of motor control using permanent magnet synchronous
motors (brushless DC motors). More detailed information about the features of this toolkit and it’s applications can be
found here: [MCK-RA8T1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0s00020bj-mck-ra8t1-renesas-flexible-motor-control-kit-ra8t1-mcu-group)

MCK-RA8T1 kit includes the items below:

- RA8T1 CPU board ([MCB-RA8T1](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0c00000bj-mcb-ra8t1-cpu-board-ra8t1-mcu-group))
- Inverter board ([MCI-LV-1](https://www.renesas.com/us/en/products/power-power-management/fet-motor-drivers/rtk0em0000s04020bj-mci-lv-1-renesas-flexible-motor-control-inverter-board-low-voltage-48v10a-three-phase-bldcpmsm-motor))
- Communication board ([MC-COM](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rtk0emxc90s00000bj-mc-com-renesas-flexible-motor-control-communication-board))
- Permanent magnet synchronous motors
- Accessories (cables, standoffs, etc.)

![RA8T1 Motor Control Kit](../../../../_images/mck_ra8t1_product_contents.jpg)

MCK-RA8T1 product contents (Credit: Renesas Electronics Corporation)

**MCB-RA8T1** is a CPU board for motor control equipped with RA8T1. Motor control using RA8T1 can be easily realized by
using it in combination with a supported inverter board. The RA8T1 MCU can be evaluated using this board alone.

By using a supported communication board, the CPU board can be electrically isolated from the PC for safe motor control
evaluation and debugging.

The specifications of the CPU board are shown below:

**MCU specifications**

- 480MHz Arm Cortex-M85 based RA8T1 MCU in 224 pins, BGA package
- ROM/RAM size: 2MB/1MB
- MCU input clock: 24MHz (Generate with external crystal oscillator)
- Power supply: DC 5V, select one way automatically from the below:

  - Power is supplied from compatible inverter board
  - Power is supplied from USB connector

**Connector**

- Inverter board connector (2 pair)
- USB connector for J-Link OB
- USB connector for RA8T1
- SCI connector for Renesas Motor Workbench communication
- Through hole for CAN communication
- 20 pin through hole for Arm debugger
- Pmod connectors (Type6A + Type2A/3A)
- Ethrnet connector
- microSD card connector

**Onboard debugger**

This product has the onboard debugger circuit, J-Link On-Board (hereinafter called “J-Link-OB”). You can
write a program (firmware) of RA8T1 with it.

## Hardware

Detailed Hardware features for the RA8T1 MCU group can be found at [RA8T1 Group User’s Manual Hardware](https://www.renesas.com/us/en/document/mah/ra8t1-group-users-manual-hardware?r=25463106)

[![RA8T1 MCU group feature](../../../../_images/ra8t1_block_diagram.png)
](../../../../_images/ra8t1_block_diagram.png)

RA8T1 Block diagram (Credit: Renesas Electronics Corporation)

Detailed Hardware features for the MCB-RA8T1 board can be found at [MCB-RA8T1 - User’s Manual](https://www.renesas.com/us/en/document/mat/mcb-ra8t1-users-manual?r=25466356)

### Supported Features

The `mck_ra8t1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mck_ra8t1/r7fa8t1ahecbd` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M85 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L19) | [`arm,cortex-m85`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m85.md#std-dtcompatible-arm-cortex-m85) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L354)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L365) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas%2Cra-adc.md#std-dtcompatible-renesas-ra-adc) |
| CAN | on-chip | Renesas RA CANFD controller global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L668) | [`renesas,ra-canfd-global`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd-global.md#std-dtcompatible-renesas-ra-canfd-global) |
| on-chip | Renesas RA CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L689)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L679) | [`renesas,ra-canfd`](../../../../build/dts/api/bindings/can/renesas%2Cra-canfd.md#std-dtcompatible-renesas-ra-canfd) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L19) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L26) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L44) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L51)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L84) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock out line[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L58)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L91) | [`renesas,ra-cgc-pll-out`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll-out.md#std-dtcompatible-renesas-ra-cgc-pll-out) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L117) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L127)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L197) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA External Bus Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1xh.dtsi?plain=1#L180) | [`renesas,ra-cgc-busclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-busclk.md#std-dtcompatible-renesas-ra-cgc-busclk) |
| Comparator | on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L911) | [`renesas,ra-acmphs-global`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs-global.md#std-dtcompatible-renesas-ra-acmphs-global) |
| on-chip | Renesas RA ACMPHS (High-Speed Analog COMParator) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L916) | [`renesas,ra-acmphs`](../../../../build/dts/api/bindings/comparator/renesas%2Cra-acmphs.md#std-dtcompatible-renesas-ra-acmphs) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L645) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas%2Cra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L376) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L382)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L389) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas%2Cra-dac.md#std-dtcompatible-renesas-ra-dac) |
| Ethernet | on-chip | Renesas RA Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L700) | [`renesas,ra-ethernet`](../../../../build/dts/api/bindings/ethernet/renesas%2Cra-ethernet.md#std-dtcompatible-renesas-ra-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L209) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | Renesas RA family flash high-performance controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L345) | [`renesas,ra-flash-hp-controller`](../../../../build/dts/api/bindings/flash_controller/renesas%2Cra-flash-hp-controller.md#std-dtcompatible-renesas-ra-flash-hp-controller) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L107)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L77) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| I2C | on-chip | Renesas RA I2C Master controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L198) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-iic.md#std-dtcompatible-renesas-ra-iic) |
| on-chip | Renesas RA SCI-B I2C controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L226) | [`renesas,ra-i2c-sci-b`](../../../../build/dts/api/bindings/i2c/renesas%2Cra-i2c-sci-b.md#std-dtcompatible-renesas-ra-i2c-sci-b) |
| I3C | on-chip | Renesas RA I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L427) | [`renesas,ra-i3c`](../../../../build/dts/api/bindings/i3c/renesas%2Cra-i3c.md#std-dtcompatible-renesas-ra-i3c) |
| Interrupt controller | on-chip | ARMv8.1-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L17) | [`arm,v8.1m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8.1m-nvic.md#std-dtcompatible-arm-v8.1m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | Renesas RA External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L709) | [`renesas,ra-mdio`](../../../../build/dts/api/bindings/mdio/renesas%2Cra-mdio.md#std-dtcompatible-renesas-ra-mdio) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L63) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas%2Cra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L279)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L213) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA ULPT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L578) | [`renesas,ra-ulpt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-ulpt.md#std-dtcompatible-renesas-ra-ulpt) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L634) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[16 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L716) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Cra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv8.1-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L27) | [`arm,armv8.1m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8.1m-mpu.md#std-dtcompatible-arm-armv8.1m-mpu) |
| MTD | on-chip | Flash memory binding for Renesas RA Code flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1ahecbd.dtsi?plain=1#L15) | [`renesas,ra-nv-code-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-code-flash.md#std-dtcompatible-renesas-ra-nv-code-flash) |
| on-chip | Flash memory binding for Renesas RA Data flash region[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/r7fa8t1ahecbd.dtsi?plain=1#L24) | [`renesas,ra-nv-data-flash`](../../../../build/dts/api/bindings/mtd/renesas%2Cra-nv-data-flash.md#std-dtcompatible-renesas-ra-nv-data-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/mck_ra8t1/mck_ra8t1.dts?plain=1#L160) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | Renesas RA OSPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L604) | [`renesas,ra-ospi-b`](../../../../build/dts/api/bindings/ospi/renesas%2Cra-ospi-b.md#std-dtcompatible-renesas-ra-ospi-b) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L954) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L71) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L458)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L438) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Cra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| RNG | on-chip | Renesas RA RSIP-E51A TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L397) | [`renesas,ra-rsip-e51a-trng`](../../../../build/dts/api/bindings/rng/renesas%2Cra-rsip-e51a-trng.md#std-dtcompatible-renesas-ra-rsip-e51a-trng) |
| SDHC | on-chip | Renesas RA SDHC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L860)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L875) | [`renesas,ra-sdhc`](../../../../build/dts/api/bindings/sdhc/renesas%2Cra-sdhc.md#std-dtcompatible-renesas-ra-sdhc) |
| Serial controller | on-chip | Renesas RA SCI\_B UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L286)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L220) | [`renesas,ra8-uart-sci-b`](../../../../build/dts/api/bindings/serial/renesas%2Cra8-uart-sci-b.md#std-dtcompatible-renesas-ra8-uart-sci-b) |
| SPI | on-chip | Renesas RA8 SPI\_B controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L401)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L414) | [`renesas,ra8-spi-b`](../../../../build/dts/api/bindings/spi/renesas%2Cra8-spi-b.md#std-dtcompatible-renesas-ra8-spi-b) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8.1-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8.1-m.dtsi?plain=1#L25) | [`arm,armv8.1m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8.1m-systick.md#std-dtcompatible-arm-armv8.1m-systick) |
| on-chip | Renesas RA ULPT TIMER[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L586) | [`renesas,ra-ulpt-timer`](../../../../build/dts/api/bindings/timer/renesas%2Cra-ulpt-timer.md#std-dtcompatible-renesas-ra-ulpt-timer) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L895) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas%2Cra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L905) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas%2Cra-udc.md#std-dtcompatible-renesas-ra-udc) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra8/ra8x1.dtsi?plain=1#L888) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas%2Cra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

Note

For using SDHC module on EK-RA8M1, Connect microSD Card to microSD Socket (CN12)

## Programming and Debugging

The `mck_ra8t1` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `mcb_ra8t1` board configuration can be
built, flashed, and debugged in the usual way. See
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details on
building and running.

**Note:** Only support from SDK v0.16.6 in which GCC for Cortex Arm-M85 was available.
To build for EK-RA8M1 user need to get and install GNU Arm Embedded toolchain from [https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6](https://github.com/zephyrproject-rtos/sdk-ng/releases/tag/v0.16.6)

### Flashing

Program can be flashed to MCB-RA8T1 via the on-board SEGGER J-Link debugger.
SEGGER J-link’s drivers are available at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

To flash the program to board

1. Connect to J-Link OB via USB port to host PC
2. Make sure J-Link OB jumper is in default configuration as describe in [MCB-RA8T1 - User’s Manual](https://www.renesas.com/us/en/document/mat/mcb-ra8t1-users-manual?r=25466356)
3. Execute west command

   > ```shell
   > west flash -r jlink
   > ```

### Debugging

You can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA8T1AH
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

**Note:** It’s verified that debug is OK on Segger Ozone v3.30d so please use this or later
version of Segger Ozone

## References

- [MCB-RA8T1 Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/rtk0ema5k0c00000bj-mcb-ra8t1-cpu-board-ra8t1-mcu-group)
- [RA8T1 MCU group Website](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/ra-cortex-m-mcus/ra8t1-480-mhz-arm-cortex-m85-based-motor-control-microcontroller-helium-and-trustzone)
