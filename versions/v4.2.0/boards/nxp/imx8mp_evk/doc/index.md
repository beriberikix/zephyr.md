---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx8mp_evk/doc/index.html
original_path: boards/nxp/imx8mp_evk/doc/index.html
---

# i.MX8MP EVK

Board Overview

Name:
:   `imx8mp_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64, xtensa, arm

SoC:
:   mimx8ml8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx8mp_evk/doc/index.rst/../..)

## Overview

i.MX8M Plus LPDDR4 EVK board is based on NXP i.MX8M Plus applications
processor, composed of a quad Cortex®-A53 cluster and a single Cortex®-M7 core.
Zephyr OS is ported to run on the Cortex®-A53 core.

- Board features:

  - RAM: 2GB LPDDR4
  - Storage:

    - SanDisk 16GB eMMC5.1
    - Micron 32MB QSPI NOR
    - microSD Socket
  - Wireless:

    - WiFi: 2.4/5GHz IEEE 802.11b/g/n
    - Bluetooth: v4.1
  - USB:

    - OTG - 2x type C
  - Ethernet
  - PCI-E M.2
  - Connectors:

    - 40-Pin Dual Row Header
  - LEDs:

    - 1x Power status LED
    - 1x UART LED
  - Debug

    - JTAG 20-pin connector
    - MicroUSB for UART debug, two COM ports for A53 and M4

More information about the board can be found at the
[NXP website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/evaluation-kit-for-the-i-mx-8m-plus-applications-processor:8MPLUSLPD4-EVK).

### Supported Features

The `imx8mp_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx8mp_evk/mimx8ml8/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L40)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L22) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm,cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| CAN | on-chip | NXP FlexCAN CANFD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L192)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L206) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L75) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L292) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L299) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53.dts?plain=1#L78) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L314) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L81)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L94) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| on-board | PCA6416 I2C-based GPIO expander[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53.dts?plain=1#L113) | [`nxp,pca6416`](../../../../build/dts/api/bindings/gpio/nxp,pca6416.md#std-dtcompatible-nxp-pca6416) |
| I2C | on-chip | NXP II2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L244)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L220) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp,ii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L60) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L308) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L333) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp,rdc.md#std-dtcompatible-nxp-rdc) |
| PHY | on-board | Simple GPIO controlled CAN transceiver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53.dts?plain=1#L42)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53.dts?plain=1#L51) | [`can-transceiver-gpio`](../../../../build/dts/api/bindings/phy/can-transceiver-gpio.md#std-dtcompatible-can-transceiver-gpio) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L323) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L327) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L180)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L168) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp,imx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L146) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L47) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx8mp_evk/mimx8ml8/a53/smp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L34)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L22) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm,cortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| CAN | on-chip | NXP FlexCAN CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L192) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp,flexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L75) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L292) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp,enet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L299) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53_smp.dts?plain=1#L60) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L314) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L81) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L220) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp,ii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L60) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L308) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L333) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp,rdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L323) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L327) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Power management CPU operations | on-board | Power State Coordination Interface (PSCI) version 0.2[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_a53_smp.dts?plain=1#L32) | [`arm,psci-0.2`](../../../../build/dts/api/bindings/pm_cpu_ops/arm,psci-0.2.md#std-dtcompatible-arm-psci-0.2) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L180)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L168) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp,imx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L146) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp,imx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L47) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx8mp_evk/mimx8ml8/adsp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Cadence Tensilica Xtensa LX6 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L16) | [`cdns,tensilica-xtensa-lx6`](../../../../build/dts/api/bindings/cpu/cdns,tensilica-xtensa-lx6.md#std-dtcompatible-cdns-tensilica-xtensa-lx6) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L84) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L45) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| DAI | on-chip | NXP Synchronous Audio Interface (SAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L99) | [`nxp,dai-sai`](../../../../build/dts/api/bindings/dai/nxp,dai-sai.md#std-dtcompatible-nxp-dai-sai) |
| on-chip | NXP PDM MICFIL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L116) | [`nxp,dai-micfil`](../../../../build/dts/api/bindings/dai/nxp,dai-micfil.md#std-dtcompatible-nxp-dai-micfil) |
| DMA | on-chip | NXP SDMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L90) | [`nxp,sdma`](../../../../build/dts/api/bindings/dma/nxp,sdma.md#std-dtcompatible-nxp-sdma) |
| Interrupt controller | on-chip | i.MX DSP interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L52) | [`nxp,irqsteer-intc`](../../../../build/dts/api/bindings/interrupt-controller/nxp,irqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc) |
| on-chip | i.MX IRQ\_STEER master[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L59) | [`nxp,irqsteer-master`](../../../../build/dts/api/bindings/interrupt-controller/nxp,irqsteer-master.md#std-dtcompatible-nxp-irqsteer-master) |
| on-chip | Xtensa Core interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L24) | [`cdns,xtensa-core-intc`](../../../../build/dts/api/bindings/interrupt-controller/cdns,xtensa-core-intc.md#std-dtcompatible-cdns-xtensa-core-intc) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L151) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L125) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L129) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L139) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp,imx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/xtensa/nxp/nxp_imx8m.dtsi?plain=1#L33) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |

#### `imx8mp_evk/mimx8ml8/m7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L17) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L32) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L37) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L76) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L118)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L92) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L173) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp,ii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L257) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L24) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L82) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L86) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L157)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L165) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp,imx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L268) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp,imx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

#### `imx8mp_evk/mimx8ml8/m7/ddr` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L17) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L32) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L37) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L76) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp,imx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L118)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L92) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L173) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp,ii2c.md#std-dtcompatible-nxp-ii2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L257) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp,imx-mu.md#std-dtcompatible-nxp-imx-mu) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L24) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L82) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp,imx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L86) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L157)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L165) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp,imx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L268) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp,imx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### Devices

#### System Clock

This board configuration uses a system clock frequency of 8 MHz.

The M7 Core is configured to run at a 800 MHz clock speed.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART4.

## Programming and Debugging (A53)

The `imx8mp_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

There are multiple methods to program and debug Zephyr on the A53 core:

### Option 1. Boot Zephyr by Using JLink Runner

The default runner for the board is JLink, connect the EVK board’s JTAG connector to
the host computer using a J-Link debugger, power up the board and stop the board at
U-Boot command line.

Then use “west flash” or “west debug” command to load the zephyr.bin
image from the host computer and start the Zephyr application on A53 core0.

#### Flash and Run

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mp_evk/mimx8ml8/a53 samples/hello_world
west flash
```

Then the following log could be found on UART4 console:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
Hello World! imx8mp_evk/mimx8ml8/a53
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mp_evk/mimx8ml8/a53 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “cpu” command is used to load and kick Zephyr to Cortex-A secondary Core, Currently
it is supported in : [Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot) (use the branch “uboot\_vxxxx.xx-y.y.y,
xxxx.xx is uboot version and y.y.y is Real-Time Edge Software version, for example
“uboot\_v2023.04-2.9.0” branch is U-Boot v2023.04 used in Real-Time Edge Software release
v2.9.0), and pre-build images and user guide can be found at [Real-Time Edge Software](https://www.nxp.com/rtedge).

#### Step 1: Download Zephyr Image into DDR Memory

Firstly need to download Zephyr binary image into DDR memory, it can use tftp:

```shell
tftp 0xc0000000 zephyr.bin
```

Or copy the Zephyr image `zephyr.bin` SD card and plug the card into the board, for example
if copy to the FAT partition of the SD card, use the following U-Boot command to load the image
into DDR memory (assuming the SD card is dev 1, fat partition ID is 1, they could be changed
based on actual setup):

```shell
fatload mmc 1:1 0xc0000000 zephyr.bin;
```

#### Step 2: Boot Zephyr

Then use the following command to boot Zephyr on the core0:

```shell
dcache off; icache flush; go 0xc0000000;
```

Or use “cpu” command to boot from secondary Core, for example Core1:

```shell
dcache flush; icache flush; cpu 1 release 0xc0000000
```

### Option 3. Boot Zephyr by Using Remoteproc under Linux

When running Linux on the A55 core, it can use the remoteproc framework to load and boot Zephyr,
refer to Real-Time Edge user guide for more details. Pre-build images and user guide can be found
at [Real-Time Edge Software](https://www.nxp.com/rtedge).

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx8mp_evk/mimx8ml8/a53 samples/synchronization
```

This will build an image with the synchronization sample app, boot it and
display the following console output:

```shell
*** Booting Zephyr OS build v4.1.0-3063-g38519ca2c028 ***
thread_a: Hello World from cpu 0 on mimx8mp_evk!
thread_b: Hello World from cpu 0 on mimx8mp_evk!
thread_a: Hello World from cpu 0 on mimx8mp_evk!
thread_b: Hello World from cpu 0 on mimx8mp_evk!
thread_a: Hello World from cpu 0 on mimx8mp_evk!
```

### CAN bus (FlexCAN) (A53)

The FlexCAN controller is a CAN 2.0B controller that supports both standard
and extended frames. The FlexCAN controller has two independent FlexCAN
modules, FlexCAN1 and FlexCAN2. By default, FlexCAN1 is enabled in the device
tree. To enable FlexCAN2, you need to add the following overlay to the
device tree:
[boards/nxp/imx8mp\_evk/dts/flexcan2.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx8mp_evk/dts/flexcan2.overlay).

For example, building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample with the CAN shell and
CAN statistics enabled, and using the FlexCAN1 controller, you can use the following
configuration:

```shell
# From the root of the zephyr repository
west build -b imx8mp_evk/mimx8ml8/a53 samples/hello_world -- -DCONFIG_SHELL=y -DCONFIG_CAN=y -DCONFIG_CAN_SHELL=y -DCONFIG_STATS=y -DCONFIG_CAN_STATS=y
```

## Programming and Debugging (M7)

The MIMX8MP EVK board doesn’t have QSPI flash for the M7, and it needs
to be started by the A53 core. The A53 core is responsible to load the M7 binary
application into the RAM, put the M7 in reset, set the M7 Program Counter and
Stack Pointer, and get the M7 out of reset. The A53 can perform these steps at
bootloader level or after the Linux system has booted.

The M7 can use up to 3 different RAMs (currently, only two configurations are
supported: ITCM and DDR). These are the memory mapping for A53 and M7:

| Region | Cortex-A53 | Cortex-M7 (System Bus) | Cortex-M7 (Code Bus) | Size |
| --- | --- | --- | --- | --- |
| OCRAM | 0x00900000-0x0098FFFF | 0x20200000-0x2028FFFF | 0x00900000-0x0098FFFF | 576KB |
| DTCM | 0x00800000-0x0081FFFF | 0x20000000-0x2001FFFF |  | 128KB |
| ITCM | 0x007E0000-0x007FFFFF |  | 0x00000000-0x0001FFFF | 128KB |
| OCRAM\_S | 0x00180000-0x00188FFF | 0x20180000-0x20188FFF | 0x00180000-0x00188FFF | 36KB |
| DDR | 0x80000000-0x803FFFFF | 0x80200000-0x803FFFFF | 0x80000000-0x801FFFFF | 2MB |

For more information about memory mapping see the
[i.MX 8M Applications Processor Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMX8MPRM) (section 2.1 to 2.3)

At compilation time you have to choose which RAM will be used. This
configuration is done based on board name (imx8mp\_evk/mimx8ml8/m7 for ITCM and
imx8mp\_evk/mimx8ml8/m7/ddr for DDR).

There are two methods to load M7 Core images: U-Boot command and Linux remoteproc.

### Load and Run M7 Zephyr Image from U-Boot

Load and run Zephyr on M7 from A53 using u-boot by copying the compiled
`zephyr.bin` to the first FAT partition of the SD card and plug the SD
card into the board. Power it up and stop the u-boot execution at prompt.

Load the M7 binary onto the desired memory and start its execution using:

### ITCM

```shell
fatload mmc 0:1 0x48000000 zephyr.bin
cp.b 0x48000000 0x7e0000 20000
bootaux 0x7e0000
```

### DDR

```shell
fatload mmc 0:1 0x80000000 zephyr.bin
dcache flush
bootaux 0x80000000
```

### Load and Run M7 Zephyr Image by using Linux remoteproc

Prepare device tree:

The device tree must inlcude CM7 dts node with compatible string “fsl,imx8mn-cm7”,
and also need to reserve M4 DDR memory if using DDR code and sys address, and also
need to put “m4\_reserved” in the list of memory-region property of the cm7 node.

```shell
reserved-memory {
         #address-cells = <2>;
         #size-cells = <2>;
         ranges;

         m7_reserved: m4@80000000 {
               no-map;
               reg = <0 0x80000000 0 0x1000000>;
         };
         ...
}

imx8mp-cm7 {
         compatible = "fsl,imx8mn-cm7";
         rsc-da = <0x55000000>;
         clocks = <&clk IMX8MP_CLK_M7_DIV>,
                  <&audio_blk_ctrl IMX8MP_CLK_AUDIO_BLK_CTRL_AUDPLL_ROOT>;
         clock-names = "core", "audio";
         mbox-names = "tx", "rx", "rxdb";
         mboxes = <&mu 0 1
                  &mu 1 1
                  &mu 3 1>;
         memory-region = <&vdevbuffer>, <&vdev0vring0>, <&vdev0vring1>, <&rsc_table>, <&m7_reserved>;
         status = "okay";
         fsl,startup-delay-ms = <500>;
};
```

Extra Zephyr Kernel configure item for DDR Image:

If use remotepoc to boot DDR board (imx8mp\_evk/mimx8ml8/m7/ddr), also need to enable
“CONFIG\_ROMSTART\_RELOCATION\_ROM” in order to put romstart memory section into ITCM because
M7 Core will get the first instruction from zero address of ITCM, but romstart relocation
will make the storage size of zephyr.bin too large, so we don’t enable it by default in
board defconfig.

```shell
diff --git a/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_m7_ddr_defconfig b/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_m7_ddr_defconfig
index 17542cb4eec..8c30c5b6fa3 100644
--- a/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_m7_ddr_defconfig
+++ b/boards/nxp/imx8mp_evk/imx8mp_evk_mimx8ml8_m7_ddr_defconfig
@@ -12,3 +12,4 @@ CONFIG_CONSOLE=y
CONFIG_XIP=y
CONFIG_CODE_DDR=y
+CONFIG_ROMSTART_RELOCATION_ROM=y
```

Then use the following steps to boot Zephyr kernel:

1. In U-Boot command line execute prepare script:

```shell
u-boot=> run prepare_mcore
```

2. Boot Linux kernel with specified dtb and then boot Zephyr by using remoteproc:

```shell
root@imx8mp-lpddr4-evk:~# echo zephyr.elf > /sys/devices/platform/imx8mp-cm7/remoteproc/remoteproc0/firmware
root@imx8mp-lpddr4-evk:~# echo start  > /sys/devices/platform/imx8mp-cm7/remoteproc/remoteproc0/state
[   39.195651] remoteproc remoteproc0: powering up imx-rproc
[   39.203345] remoteproc remoteproc0: Booting fw image zephyr.elf, size 503992
[   39.203388] remoteproc remoteproc0: No resource table in elf
root@imx8mp-lpddr4-evk:~# [   39.711380] remoteproc remoteproc0: remote processor imx-rproc is now up

root@imx8mp-lpddr4-evk:~#
```

### Debugging

MIMX8MP EVK board can be debugged by connecting an external JLink
JTAG debugger to the J24 debug connector and to the PC. Then
the application can be debugged using the usual way.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mp_evk/mimx8ml8/m7 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.7.99-1310-g2801bf644a91  ***
Hello World! imx8mp_evk
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
