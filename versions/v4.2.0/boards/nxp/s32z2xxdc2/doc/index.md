---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/s32z2xxdc2/doc/index.html
original_path: boards/nxp/s32z2xxdc2/doc/index.html
---

# X-S32Z27X-DC (DC2)

Board Overview

Name:
:   `s32z2xxdc2`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   s32z270

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/s32z2xxdc2/doc/index.rst/../..)

## Overview

The X-S32Z27X-DC (DC2) board is based on the NXP S32Z2 Real-Time Processor,
which includes two Real-Time Units (RTU) composed of four ARM Cortex-R52 cores
each, with flexible split/lock configurations.

There is one Zephyr board per SoC/RTU:

- `s32z2xxdc2/s32z270/rtu0`, for S32Z270/RTU0
- `s32z2xxdc2/s32z270/rtu1`, for S32Z270/RTU1.

## Hardware

Information about the hardware and design resources can be found at
[NXP S32Z2 Real-Time Processors website](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2) [[8]](#id15).

### Supported Features

The `s32z2xxdc2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `s32z2xxdc2@B/s32z270/rtu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L18) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| ADC | on-chip | NXP S32 ADC SAR controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1106) | [`nxp,s32-adc-sar`](../../../../build/dts/api/bindings/adc/nxp%2Cs32-adc-sar.md#std-dtcompatible-nxp-s32-adc-sar) |
| CAN | on-chip | NXP S32 CANXL controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L718)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L732) | [`nxp,s32-canxl`](../../../../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl) |
| on-chip | NXP FlexCAN CANFD controller[24 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L746) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L85) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| Counter | on-chip | NXP S32 System Timer Module (STM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L25) | [`nxp,s32-sys-timer`](../../../../build/dts/api/bindings/counter/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L102) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L112) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1148) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP S32 NETC Physical Station Interface (PSI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L669) | [`nxp,s32-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi) |
| on-chip | NXP S32 NETC Virtual Station Interface (VSI)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L675) | [`nxp,s32-netc-vsi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi) |
| GPIO & Headers | on-chip | NXP S32 GPIO controller[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L243) | [`nxp,s32-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cs32-gpio.md#std-dtcompatible-nxp-s32-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1126) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L104) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | NXP S32 SIUL2 External Interrupts Request controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L233) | [`nxp,s32-siul2-eirq`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cs32-siul2-eirq.md#std-dtcompatible-nxp-s32-siul2-eirq) |
| Mailbox | on-chip | NXP S32 Message Receive Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L591)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L599) | [`nxp,s32-mru`](../../../../build/dts/api/bindings/mbox/nxp%2Cs32-mru.md#std-dtcompatible-nxp-s32-mru) |
| MDIO | on-chip | NXP S32 NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L661) | [`nxp,s32-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cs32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio) |
| Miscellaneous | on-chip | Enhanced Modular IO SubSystem (eMIOS) for NXP S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1280) | [`nxp,s32-emios`](../../../../build/dts/api/bindings/misc/nxp%2Cs32-emios.md#std-dtcompatible-nxp-s32-emios) |
| MTD | on-board | QSPI hyperflash connected to the NXP S32 QSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102) | [`nxp,s32-qspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp%2Cs32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP S32 Pin Controller for S32Z/E SoCs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L77) | [`nxp,s32ze-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cs32ze-pinctrl.md#std-dtcompatible-nxp-s32ze-pinctrl) |
| PSI5 | on-chip | NXP S32 PSI5 (Peripheral Sensor Interface) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1575) | [`nxp,s32-psi5`](../../../../build/dts/api/bindings/psi5/nxp%2Cs32-psi5.md#std-dtcompatible-nxp-s32-psi5) |
| PWM | on-chip | NXP S32 eMIOS PWM node for S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1360) | [`nxp,s32-emios-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cs32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm) |
| QSPI | on-chip | NXP S32 Quad Serial Peripheral Interface (QSPI) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1453)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1461) | [`nxp,s32-qspi`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi.md#std-dtcompatible-nxp-s32-qspi) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP MDAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82) | [`nxp,s32-qspi-sfp-mdad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP FRAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91) | [`nxp,s32-qspi-sfp-frad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad) |
| SENT | on-chip | NXP S32 SENT (Single Edge Nibble Transmission) Receiver Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1469) | [`nxp,s32-sent`](../../../../build/dts/api/bindings/sent/nxp%2Cs32-sent.md#std-dtcompatible-nxp-s32-sent) |
| Serial controller | on-chip | NXP S32 LINFlexD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L124)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L132) | [`nxp,s32-linflexd`](../../../../build/dts/api/bindings/serial/nxp%2Cs32-linflexd.md#std-dtcompatible-nxp-s32-linflexd) |
| SPI | on-chip | NXP S32 SPI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L471) | [`nxp,s32-spi`](../../../../build/dts/api/bindings/spi/nxp%2Cs32-spi.md#std-dtcompatible-nxp-s32-spi) |
| on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L581) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L114) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Software Watchdog Timer (SWT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L57)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L66) | [`nxp,s32-swt`](../../../../build/dts/api/bindings/watchdog/nxp%2Cs32-swt.md#std-dtcompatible-nxp-s32-swt) |

#### `s32z2xxdc2@B/s32z270/rtu1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L42) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| ADC | on-chip | NXP S32 ADC SAR controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1106) | [`nxp,s32-adc-sar`](../../../../build/dts/api/bindings/adc/nxp%2Cs32-adc-sar.md#std-dtcompatible-nxp-s32-adc-sar) |
| CAN | on-chip | NXP S32 CANXL controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L718) | [`nxp,s32-canxl`](../../../../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L746)[23 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L761) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L85) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| Counter | on-chip | NXP S32 System Timer Module (STM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L25) | [`nxp,s32-sys-timer`](../../../../build/dts/api/bindings/counter/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L102) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L112) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1148) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP S32 NETC Physical Station Interface (PSI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L669) | [`nxp,s32-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi) |
| on-chip | NXP S32 NETC Virtual Station Interface (VSI)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L675) | [`nxp,s32-netc-vsi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi) |
| GPIO & Headers | on-chip | NXP S32 GPIO controller[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L243) | [`nxp,s32-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cs32-gpio.md#std-dtcompatible-nxp-s32-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1126) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L104) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | NXP S32 SIUL2 External Interrupts Request controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L233) | [`nxp,s32-siul2-eirq`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cs32-siul2-eirq.md#std-dtcompatible-nxp-s32-siul2-eirq) |
| Mailbox | on-chip | NXP S32 Message Receive Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L623)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L591) | [`nxp,s32-mru`](../../../../build/dts/api/bindings/mbox/nxp%2Cs32-mru.md#std-dtcompatible-nxp-s32-mru) |
| MDIO | on-chip | NXP S32 NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L661) | [`nxp,s32-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cs32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio) |
| Miscellaneous | on-chip | Enhanced Modular IO SubSystem (eMIOS) for NXP S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1280) | [`nxp,s32-emios`](../../../../build/dts/api/bindings/misc/nxp%2Cs32-emios.md#std-dtcompatible-nxp-s32-emios) |
| MTD | on-board | QSPI hyperflash connected to the NXP S32 QSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102) | [`nxp,s32-qspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp%2Cs32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP S32 Pin Controller for S32Z/E SoCs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L77) | [`nxp,s32ze-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cs32ze-pinctrl.md#std-dtcompatible-nxp-s32ze-pinctrl) |
| PSI5 | on-chip | NXP S32 PSI5 (Peripheral Sensor Interface) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1575) | [`nxp,s32-psi5`](../../../../build/dts/api/bindings/psi5/nxp%2Cs32-psi5.md#std-dtcompatible-nxp-s32-psi5) |
| PWM | on-chip | NXP S32 eMIOS PWM node for S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1360) | [`nxp,s32-emios-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cs32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm) |
| QSPI | on-chip | NXP S32 Quad Serial Peripheral Interface (QSPI) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1453)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1461) | [`nxp,s32-qspi`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi.md#std-dtcompatible-nxp-s32-qspi) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP MDAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82) | [`nxp,s32-qspi-sfp-mdad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP FRAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91) | [`nxp,s32-qspi-sfp-frad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad) |
| SENT | on-chip | NXP S32 SENT (Single Edge Nibble Transmission) Receiver Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1469) | [`nxp,s32-sent`](../../../../build/dts/api/bindings/sent/nxp%2Cs32-sent.md#std-dtcompatible-nxp-s32-sent) |
| Serial controller | on-chip | NXP S32 LINFlexD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L124)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L132) | [`nxp,s32-linflexd`](../../../../build/dts/api/bindings/serial/nxp%2Cs32-linflexd.md#std-dtcompatible-nxp-s32-linflexd) |
| SPI | on-chip | NXP S32 SPI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L471) | [`nxp,s32-spi`](../../../../build/dts/api/bindings/spi/nxp%2Cs32-spi.md#std-dtcompatible-nxp-s32-spi) |
| on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L581) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L114) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Software Watchdog Timer (SWT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L57)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L66) | [`nxp,s32-swt`](../../../../build/dts/api/bindings/watchdog/nxp%2Cs32-swt.md#std-dtcompatible-nxp-s32-swt) |

#### `s32z2xxdc2@D/s32z270/rtu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L18) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| ADC | on-chip | NXP S32 ADC SAR controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1106) | [`nxp,s32-adc-sar`](../../../../build/dts/api/bindings/adc/nxp%2Cs32-adc-sar.md#std-dtcompatible-nxp-s32-adc-sar) |
| CAN | on-chip | NXP S32 CANXL controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L718)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L732) | [`nxp,s32-canxl`](../../../../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl) |
| on-chip | NXP FlexCAN CANFD controller[24 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L746) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L85) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| Counter | on-chip | NXP S32 System Timer Module (STM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L25) | [`nxp,s32-sys-timer`](../../../../build/dts/api/bindings/counter/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L102) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L112) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1148) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP S32 NETC Physical Station Interface (PSI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L669) | [`nxp,s32-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi) |
| on-chip | NXP S32 NETC Virtual Station Interface (VSI)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L675) | [`nxp,s32-netc-vsi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi) |
| GPIO & Headers | on-chip | NXP S32 GPIO controller[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L243) | [`nxp,s32-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cs32-gpio.md#std-dtcompatible-nxp-s32-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1126) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L104) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | NXP S32 SIUL2 External Interrupts Request controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L233) | [`nxp,s32-siul2-eirq`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cs32-siul2-eirq.md#std-dtcompatible-nxp-s32-siul2-eirq) |
| Mailbox | on-chip | NXP S32 Message Receive Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L591)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L599) | [`nxp,s32-mru`](../../../../build/dts/api/bindings/mbox/nxp%2Cs32-mru.md#std-dtcompatible-nxp-s32-mru) |
| MDIO | on-chip | NXP S32 NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L661) | [`nxp,s32-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cs32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio) |
| Miscellaneous | on-chip | Enhanced Modular IO SubSystem (eMIOS) for NXP S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1280) | [`nxp,s32-emios`](../../../../build/dts/api/bindings/misc/nxp%2Cs32-emios.md#std-dtcompatible-nxp-s32-emios) |
| MTD | on-board | QSPI hyperflash connected to the NXP S32 QSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102) | [`nxp,s32-qspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp%2Cs32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP S32 Pin Controller for S32Z/E SoCs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L77) | [`nxp,s32ze-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cs32ze-pinctrl.md#std-dtcompatible-nxp-s32ze-pinctrl) |
| PSI5 | on-chip | NXP S32 PSI5 (Peripheral Sensor Interface) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1575) | [`nxp,s32-psi5`](../../../../build/dts/api/bindings/psi5/nxp%2Cs32-psi5.md#std-dtcompatible-nxp-s32-psi5) |
| PWM | on-chip | NXP S32 eMIOS PWM node for S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1360) | [`nxp,s32-emios-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cs32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm) |
| QSPI | on-chip | NXP S32 Quad Serial Peripheral Interface (QSPI) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1453)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1461) | [`nxp,s32-qspi`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi.md#std-dtcompatible-nxp-s32-qspi) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP MDAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82) | [`nxp,s32-qspi-sfp-mdad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP FRAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91) | [`nxp,s32-qspi-sfp-frad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad) |
| SENT | on-chip | NXP S32 SENT (Single Edge Nibble Transmission) Receiver Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1469) | [`nxp,s32-sent`](../../../../build/dts/api/bindings/sent/nxp%2Cs32-sent.md#std-dtcompatible-nxp-s32-sent) |
| Serial controller | on-chip | NXP S32 LINFlexD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L196)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L124) | [`nxp,s32-linflexd`](../../../../build/dts/api/bindings/serial/nxp%2Cs32-linflexd.md#std-dtcompatible-nxp-s32-linflexd) |
| SPI | on-chip | NXP S32 SPI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L471) | [`nxp,s32-spi`](../../../../build/dts/api/bindings/spi/nxp%2Cs32-spi.md#std-dtcompatible-nxp-s32-spi) |
| on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L581) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L114) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Software Watchdog Timer (SWT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L57)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu0_r52.dtsi?plain=1#L66) | [`nxp,s32-swt`](../../../../build/dts/api/bindings/watchdog/nxp%2Cs32-swt.md#std-dtcompatible-nxp-s32-swt) |

#### `s32z2xxdc2@D/s32z270/rtu1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L42) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| ADC | on-chip | NXP S32 ADC SAR controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1106) | [`nxp,s32-adc-sar`](../../../../build/dts/api/bindings/adc/nxp%2Cs32-adc-sar.md#std-dtcompatible-nxp-s32-adc-sar) |
| CAN | on-chip | NXP S32 CANXL controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L718) | [`nxp,s32-canxl`](../../../../build/dts/api/bindings/can/nxp%2Cs32-canxl.md#std-dtcompatible-nxp-s32-canxl) |
| on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L746)[23 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L761) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | NXP S32 clock generator IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L85) | [`nxp,s32-clock`](../../../../build/dts/api/bindings/clock/nxp%2Cs32-clock.md#std-dtcompatible-nxp-s32-clock) |
| Counter | on-chip | NXP S32 System Timer Module (STM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L25) | [`nxp,s32-sys-timer`](../../../../build/dts/api/bindings/counter/nxp%2Cs32-sys-timer.md#std-dtcompatible-nxp-s32-sys-timer) |
| on-chip | NXP Periodic Interrupt Timer (PIT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L102) | [`nxp,pit`](../../../../build/dts/api/bindings/counter/nxp%2Cpit.md#std-dtcompatible-nxp-pit) |
| on-chip | Child node for the Periodic Interrupt Timer node, intended for an individual timer channel[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L112) | [`nxp,pit-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cpit-channel.md#std-dtcompatible-nxp-pit-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1148) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L19) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-chip | NXP S32 NETC Physical Station Interface (PSI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L669) | [`nxp,s32-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-psi.md#std-dtcompatible-nxp-s32-netc-psi) |
| on-chip | NXP S32 NETC Virtual Station Interface (VSI)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L675) | [`nxp,s32-netc-vsi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cs32-netc-vsi.md#std-dtcompatible-nxp-s32-netc-vsi) |
| GPIO & Headers | on-chip | NXP S32 GPIO controller[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L243) | [`nxp,s32-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cs32-gpio.md#std-dtcompatible-nxp-s32-gpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1126) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L104) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | NXP S32 SIUL2 External Interrupts Request controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L233) | [`nxp,s32-siul2-eirq`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cs32-siul2-eirq.md#std-dtcompatible-nxp-s32-siul2-eirq) |
| Mailbox | on-chip | NXP S32 Message Receive Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L623)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L591) | [`nxp,s32-mru`](../../../../build/dts/api/bindings/mbox/nxp%2Cs32-mru.md#std-dtcompatible-nxp-s32-mru) |
| MDIO | on-chip | NXP S32 NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L661) | [`nxp,s32-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cs32-netc-emdio.md#std-dtcompatible-nxp-s32-netc-emdio) |
| Miscellaneous | on-chip | Enhanced Modular IO SubSystem (eMIOS) for NXP S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1280) | [`nxp,s32-emios`](../../../../build/dts/api/bindings/misc/nxp%2Cs32-emios.md#std-dtcompatible-nxp-s32-emios) |
| MTD | on-board | QSPI hyperflash connected to the NXP S32 QSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L102) | [`nxp,s32-qspi-hyperflash`](../../../../build/dts/api/bindings/mtd/nxp%2Cs32-qspi-hyperflash.md#std-dtcompatible-nxp-s32-qspi-hyperflash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L116) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | NXP S32 Pin Controller for S32Z/E SoCs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L77) | [`nxp,s32ze-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cs32ze-pinctrl.md#std-dtcompatible-nxp-s32ze-pinctrl) |
| PSI5 | on-chip | NXP S32 PSI5 (Peripheral Sensor Interface) Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1575) | [`nxp,s32-psi5`](../../../../build/dts/api/bindings/psi5/nxp%2Cs32-psi5.md#std-dtcompatible-nxp-s32-psi5) |
| PWM | on-chip | NXP S32 eMIOS PWM node for S32 SoCs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1360) | [`nxp,s32-emios-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Cs32-emios-pwm.md#std-dtcompatible-nxp-s32-emios-pwm) |
| QSPI | on-chip | NXP S32 Quad Serial Peripheral Interface (QSPI) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1453)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1461) | [`nxp,s32-qspi`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi.md#std-dtcompatible-nxp-s32-qspi) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP MDAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L82) | [`nxp,s32-qspi-sfp-mdad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-mdad.md#std-dtcompatible-nxp-s32-qspi-sfp-mdad) |
| on-board | NXP S32 Quad Serial Peripheral Interface (QSPI) Secure Flash Protection SFP FRAD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/s32z2xxdc2/s32z2xxdc2_s32z270.dtsi?plain=1#L91) | [`nxp,s32-qspi-sfp-frad`](../../../../build/dts/api/bindings/qspi/nxp%2Cs32-qspi-sfp-frad.md#std-dtcompatible-nxp-s32-qspi-sfp-frad) |
| SENT | on-chip | NXP S32 SENT (Single Edge Nibble Transmission) Receiver Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L1469) | [`nxp,s32-sent`](../../../../build/dts/api/bindings/sent/nxp%2Cs32-sent.md#std-dtcompatible-nxp-s32-sent) |
| Serial controller | on-chip | NXP S32 LINFlexD[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L196)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L124) | [`nxp,s32-linflexd`](../../../../build/dts/api/bindings/serial/nxp%2Cs32-linflexd.md#std-dtcompatible-nxp-s32-linflexd) |
| SPI | on-chip | NXP S32 SPI controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L471) | [`nxp,s32-spi`](../../../../build/dts/api/bindings/spi/nxp%2Cs32-spi.md#std-dtcompatible-nxp-s32-spi) |
| on-chip | NXP DSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L581) | [`nxp,dspi`](../../../../build/dts/api/bindings/spi/nxp%2Cdspi.md#std-dtcompatible-nxp-dspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_r52.dtsi?plain=1#L114) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Watchdog | on-chip | Software Watchdog Timer (SWT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L57)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_s32z27x_rtu1_r52.dtsi?plain=1#L66) | [`nxp,s32-swt`](../../../../build/dts/api/bindings/watchdog/nxp%2Cs32-swt.md#std-dtcompatible-nxp-s32-swt) |

### Connections and IOs

The SoC’s pads are grouped into ports and pins for consistency with GPIO driver
and the HAL drivers used by this Zephyr port. The following table summarizes
the mapping between pads and ports/pins. This must be taken into account when
using GPIO driver or configuring the pinmuxing for the device drivers.

| Pads | Port/Pins |
| --- | --- |
| PAD\_000 - PAD\_015 | PA0 - PA15 |
| PAD\_016 - PAD\_030 | PB0 - PB14 |
| PAD\_031 | PC15 |
| PAD\_032 - PAD\_047 | PD0 - PD15 |
| PAD\_048 - PAD\_063 | PE0 - PE15 |
| PAD\_064 - PAD\_079 | PF0 - PF15 |
| PAD\_080 - PAD\_091 | PG0 - PG11 |
| PAD\_092 - PAD\_095 | PH12 - PH15 |
| PAD\_096 - PAD\_111 | PI0 - PI15 |
| PAD\_112 - PAD\_127 | PJ0 - PJ15 |
| PAD\_128 - PAD\_143 | PK0 - PK15 |
| PAD\_144 - PAD\_145 | PL0 - PL1 |
| PAD\_146 - PAD\_159 | PM2 - PM15 |
| PAD\_160 - PAD\_169 | PN0 - PN9 |
| PAD\_170 - PAD\_173 | PO10 - PO13 |

This board does not include user LED’s or switches, which are needed for some
of the samples such as [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") or [Button](../../../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.").
Follow the steps described in the sample description to enable support for this
board.

### System Clock

The Cortex-R52 cores are configured to run at 1 GHz.

### Serial Port

The SoC has 12 LINFlexD instances that can be used in UART mode. The console can
be accessed by default on the USB micro-B connector J119.

### Watchdog

The watchdog driver only supports triggering an interrupt upon timer expiration.
Zephyr is currently running from SRAM on this board, thus system reset is not
supported.

### Ethernet

NETC driver supports to manage the Physical Station Interface (PSI0) and/or a
single Virtual SI (VSI). The rest of the VSI’s shall be assigned to different
cores of the system. Refer to [S32 Network Controller (NETC)](../../../../samples/boards/nxp/s32/netc/README.md#nxp_s32_netc "Configure NXP S32 Network Controller (NETC)") to learn how to
configure the Ethernet network controller.

### Controller Area Network

#### CANEXCEL

CANEXCEL supports CAN Classic (CAN 2.0) and CAN FD modes. Remote transmission
request is not supported.

Note that this board does not currently come with CAN transceivers installed for
the CANEXCEL ports. To facilitate external traffic, you will need to add a CAN
transceiver. Any transceiver pin-compatible with CAN 2.0 and CAN FD protocols
can be used.

#### FlexCAN

FlexCAN supports CAN Classic (CAN 2.0) and CAN FD modes.

### ADC

ADC is provided through ADC SAR controller with 2 instances. Each ADC SAR instance has
12-bit resolution. ADC channels are divided into 2 groups (precision and internal/standard).

Note

All channels of an instance only run on 1 group channel at the same time.

### EDMA

The EDMA modules feature four EDMA3 instances: Instance 0 with 32 channels,
and instances 1, 4, and 5, each with 16 channels.

### External Flash

The on-board S26HS512T 512M-bit HyperFlash memory is connected to the QSPI controller
port A1. This board configuration selects it as the default flash controller.

## Programming and Debugging

The `s32z2xxdc2` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** |
| --- | --- | --- | --- | --- |
| **[nxp\_s32dbg](../../../../develop/flash_debug/host-tools.md#runner-nxp-s32dbg)** |  | ✅ (default) | ✅ | ✅ |
| **[trace32](../../../../develop/flash_debug/host-tools.md#runner-trace32)** | ✅ | ✅ |  |  |

Applications for the `s32z2xxdc2` boards can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

Currently is only possible to load and execute a Zephyr application binary on
this board from the core internal SRAM.

This board supports West runners for the following debug tools:

- [NXP S32 Debug Probe](../../../../develop/flash_debug/probes.md#nxp-s32-debug-probe) (default)
- [Lauterbach TRACE32](../../../../develop/flash_debug/host-tools.md#lauterbach-trace32-debug-host-tools)

Follow the installation steps of the debug tool you plan to use before loading
your firmware.

### Set-up the Board

Connect the external debugger probe to the board’s JTAG connector (`J134`)
and to the host computer via USB or Ethernet, as supported by the probe.

For visualizing the serial output, connect the board’s USB/UART port (`J119`) to
the host computer and run your favorite terminal program to listen for output.
For example, using the cross-platform [pySerial miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm) [[9]](#id17) terminal:

```shell
python -m serial.tools.miniterm <port> 115200
```

Replace `<port>` with the port where the board can be found. For example,
under Linux, `/dev/ttyUSB0`.

### Debugging

You can build and debug the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample for the board
`s32z2xxdc2/s32z270/rtu0` with:

```shell
# From the root of the zephyr repository
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west debug
```

In case you are using a newer PCB revision, you have to use an adapted board
definition as the default PCB revision is B. For example, if using revision D:

```shell
west build -b s32z2xxdc2@D/s32z270/rtu0 samples/hello_world
west debug
```

At this point you can do your normal debug session. Set breakpoints and then
`c` to continue into the program. You should see the following message in
the terminal:

```shell
Hello World! s32z2xxdc2
```

To debug with Lauterbach TRACE32 software run instead:

```shell
west debug -r trace32
```

### Flashing

Follow these steps if you just want to download the application to the board
SRAM and run.

`flash` command is supported only by the Lauterbach TRACE32 runner:

```shell
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world
west flash -r trace32
```

Note

Currently, the Lauterbach start-up scripts executed with `flash` and
`debug` commands perform the same steps to initialize the SoC and
load the application to SRAM. The difference is that `flash` hides the
Lauterbach TRACE32 interface, executes the application and exits.

To imitate a similar behavior using NXP S32 Debug Probe runner, you can run the
`debug` command with GDB in batch mode:

```shell
west debug --tool-opt='--batch'
```

### RTU and Core Configuration

This Zephyr port can only run single core in any of the Cortex-R52 cores,
either in lock-step or split-lock mode. By default, Zephyr runs on the first
core of the RTU chosen and in lock-step mode (which is the reset
configuration).

To build for split-lock mode, the [`CONFIG_DCLS`](../../../../kconfig.md#CONFIG_DCLS "CONFIG_DCLS") must be
disabled from your application Kconfig file.

By default the board configuration will set the runner arguments according to
the build configuration. To debug for a core different than the default use:

lockstep configurationsplit-lock configuration

```shell
west debug --core-name='R52_<rtu_id>_<core_id>_LS'
```

```shell
west debug --core-name='R52_<rtu_id>_<core_id>'
```

Where:

- `<rtu_id>` is the zero-based RTU index
- `<core_id>` is the zero-based core index relative to the RTU on which to
  run the Zephyr application (0, 1, 2 or 3)

For example, to build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample for the board
`s32z2xxdc2/s32z270/rtu0` with split-lock core configuration:

```shell
west build -b s32z2xxdc2/s32z270/rtu0 samples/hello_world -- -DCONFIG_DCLS=n
```

To execute this sample in the second core of RTU0 in split-lock mode:

```shell
west debug --core-name='R52_0_1'
```

If using Lauterbach TRACE32, all runner parameters must be overridden from command
line:

```shell
west debug -r trace32 --startup-args elfFile=<elf_path> rtu=<rtu_id> core=<core_id> lockstep=<yes/no>
```

Where `<elf_path>` is the path to the Zephyr application ELF in the output
directory.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id1)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id3), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id5) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id7)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id9)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id11) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id13)

## References

[[1](#id2)]

[https://github.com/nxp-zephyr/nxp-zsdk](https://github.com/nxp-zephyr/nxp-zsdk)

[[2](#id4)]

[https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC)

[[3](#id6)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki)

[[4](#id8)]

[https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)

[[5](#id10)]

[https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)

[[6](#id12)]

[https://nxp.com/zephyr](https://nxp.com/zephyr)

[[7](#id14)]

[https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

[[8](#id16)]

[https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2](https://www.nxp.com/products/processors-and-microcontrollers/s32-automotive-platform/s32z-and-s32e-real-time-processors/s32z2-safe-and-secure-high-performance-real-time-processors:S32Z2)

[[9](#id18)]

[https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)
