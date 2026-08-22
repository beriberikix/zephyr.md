---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx95_evk/doc/index.html
original_path: boards/nxp/imx95_evk/doc/index.html
---

# i.MX95 EVK

Board Overview

Name:
:   `imx95_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64, arm

SoC:
:   mimx9596

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx95_evk/doc/index.rst/../..)

## Overview

The i.MX95 EVK (IMX95LPD5EVK-19) board is a platform designed to show the
most commonly used features of the i.MX 95 automotive applications processor.
It is an entry-level development board, which helps developers to get familiar
with the processor before investing a large amount of resources in more
specific designs. The i.MX95 device on the board comes in a compact
19 x 19 mm package.

## Hardware

- i.MX 95 automotive applications processor

  - The processor integrates up to six Arm Cortex-A55 cores, and supports
    functional safety with built-in Arm Cortex-M33 and -M7 cores
- DRAM memory: 128-Gbit LPDDR5 DRAM
- eMMC: 64 GB Micron eMMC
- SPI NOR flash memory: 1 Gbit octal flash memory
- USB interface: Two USB ports: Type-A and Type-C
- Audio codec interface

  - One audio codec WM8962BECSN/R with one TX and RX lane
  - One 3.5 mm 4-pole CTIA standard audio jack
  - One 4-pin connector to connect speaker
- Ethernet interface

  - ENET2 controller

    - Connects to a 60-pin Ethernet connector
    - Supports Ethernet PHY daughter cards that can be configured to operate
      at 100 Mbit/s or 1000 Mbit/s
  - ENET1 controller

    - Supports 100 Mbit/s or 1000 Mbit/s RGMII Ethernet with one RJ45
      connector connected with an external PHY, RTL8211
  - 10 Gbit Ethernet controller

    - Supports XFI and USXGMII interfaces with one 10 Gbit RJ45 ICM connected
      with an external PHY, Marvell AQR113C
- M.2 interface: One Wi-Fi/Bluetooth Murata Type-2EL module based on NXP AW693
  chip supporting 2x2 Wi-Fi 6 and Bluetooth 5.2
- MIPI CSI interface: Connects to one 36-pin miniSAS connector using x4 lane
  configuration
- MIPI CSIDSI interface: Connects to one 36-pin miniSAS connector using x4 lane
  configuration
- LVDS interface: two mini-SAS connectors each with x4-lane configuration
- CAN interface: Two 4-pin CAN headers for external connection
- SD card interface: one 4-bit SD3.0 microSD card
- I2C interface: I2C1 to I2C7 controllers
- FT4232H I2C interface: PCT2075 temperature sensor and current monitoring devices
- DMIC interface: two digital microphones (DMIC) providing a single-bit PDM output
- ADC interface: two 4-channel ADC header
- Audio board interface

  - Supports PCIe x4 slot for Quantum board connection
  - Supports PCIe x8 slot for Audio I/O board connection
- Debug interface

  - One USB-to-UART/MPSSE device, FT4232H
  - One USB 2.0 Type-C connector (J31) for FT4232H provides quad serial ports

### Supported Features

The `imx95_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx95_evk/mimx9596/a55` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L53)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L23) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| Counter | on-chip | NXP Timer/PWM Module (TPM) used as timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L393) | [`nxp,tpm-timer`](../../../../build/dts/api/bindings/counter/nxp%2Ctpm-timer.md#std-dtcompatible-nxp-tpm-timer) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L86) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L93) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L102) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L108) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| GPIO & Headers | on-chip | i.MX RGPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L269) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L167)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L119) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L73) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L349)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L321) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L112) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L330)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L215) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L61) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx95_evk/mimx9596/a55/smp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L23) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| Counter | on-chip | NXP Timer/PWM Module (TPM) used as timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L393) | [`nxp,tpm-timer`](../../../../build/dts/api/bindings/counter/nxp%2Ctpm-timer.md#std-dtcompatible-nxp-tpm-timer) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L86) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L93) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L102) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L108) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| GPIO & Headers | on-chip | i.MX RGPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L269) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L167)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L119) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L73) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L349)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L321) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L112) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Power management CPU operations | on-board | Power State Coordination Interface (PSCI) version 1.1[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_a55_smp.dts?plain=1#L22) | [`arm,psci-1.1`](../../../../build/dts/api/bindings/pm_cpu_ops/arm%2Cpsci-1.1.md#std-dtcompatible-arm-psci-1.1) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L330)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L215) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx95_a55.dtsi?plain=1#L61) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx95_evk/mimx9596/m7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L18) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L82) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L87) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L486) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DAI | on-chip | NXP Synchronous Audio Interface (SAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L283) | [`nxp,dai-sai`](../../../../build/dts/api/bindings/dai/nxp%2Cdai-sai.md#std-dtcompatible-nxp-dai-sai) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L147) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L31) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek%2Crtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP i.MX NETC Physical Station Interface (PSI)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L546) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cimx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-chip | NXP NETC PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L570) | [`nxp,netc-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cnetc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L37) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L44) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) power domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L53) | [`arm,scmi-power`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-power.md#std-dtcompatible-arm-scmi-power) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L59) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L65) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| on-chip | System Control and Management Interface (SCMI) cpu domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L74) | [`nxp,scmi-cpu`](../../../../build/dts/api/bindings/firmware/nxp%2Cscmi-cpu.md#std-dtcompatible-nxp-scmi-cpu) |
| GPIO & Headers | on-chip | i.MX RGPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L102) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L312)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L201) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | i.MX DSP interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L513) | [`nxp,irqsteer-intc`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cirqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc) |
| on-chip | i.MX IRQ\_STEER master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L520) | [`nxp,irqsteer-master`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cirqsteer-master.md#std-dtcompatible-nxp-irqsteer-master) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L498)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L505) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L537) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cimx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L26) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L54) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L64) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L69) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| PWM | on-chip | MCUX Timer/PWM Module (TPM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L414)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L161) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L247)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L257) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L92) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L446)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L223) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

#### `imx95_evk/mimx9596/m7/ddr` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L18) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L82) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L87) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Counter | on-chip | NXP LPTMR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L486) | [`nxp,lptmr`](../../../../build/dts/api/bindings/counter/nxp%2Clptmr.md#std-dtcompatible-nxp-lptmr) |
| DAI | on-chip | NXP Synchronous Audio Interface (SAI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L283) | [`nxp,dai-sai`](../../../../build/dts/api/bindings/dai/nxp%2Cdai-sai.md#std-dtcompatible-nxp-dai-sai) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L147) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp%2Cmcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| Ethernet | on-board | Realtek RTL8211F Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L31) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek%2Crtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP i.MX NETC Physical Station Interface (PSI)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L546) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp%2Cimx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-chip | NXP NETC PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L570) | [`nxp,netc-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cnetc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L37) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L44) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) power domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L53) | [`arm,scmi-power`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-power.md#std-dtcompatible-arm-scmi-power) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L59) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L65) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm%2Cscmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| on-chip | System Control and Management Interface (SCMI) cpu domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L74) | [`nxp,scmi-cpu`](../../../../build/dts/api/bindings/firmware/nxp%2Cscmi-cpu.md#std-dtcompatible-nxp-scmi-cpu) |
| GPIO & Headers | on-chip | i.MX RGPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L102) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| I2C | on-chip | NXP LPI2C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L312)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L201) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpi2c.md#std-dtcompatible-nxp-lpi2c) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | i.MX DSP interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L513) | [`nxp,irqsteer-intc`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cirqsteer-intc.md#std-dtcompatible-nxp-irqsteer-intc) |
| on-chip | i.MX IRQ\_STEER master[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L520) | [`nxp,irqsteer-master`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cirqsteer-master.md#std-dtcompatible-nxp-irqsteer-master) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L498)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L505) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L537) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cimx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L26) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L54) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx95_evk/imx95_evk_mimx9596_m7.dts?plain=1#L64) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L69) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| PWM | on-chip | MCUX Timer/PWM Module (TPM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L414)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L161) | [`nxp,kinetis-tpm`](../../../../build/dts/api/bindings/pwm/nxp%2Ckinetis-tpm.md#std-dtcompatible-nxp-kinetis-tpm) |
| Serial controller | on-chip | NXP LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L247)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L257) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp%2Clpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L92) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L446)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx95_m7.dtsi?plain=1#L223) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp%2Clpspi.md#std-dtcompatible-nxp-lpspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

#### System Clock

This board configuration uses a system clock frequency of 24 MHz for Cortex-A55.
Cortex-A55 Core runs up to 1.8 GHz.
Cortex-M7 Core runs up to 800MHz in which SYSTICK runs on same frequency.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART1 for Cortex-A55, UART3 for Cortex-M7.

#### TPM

Two channels are enabled on TPM2 for PWM for M7. Signals can be observerd with
oscilloscope.
Channel 2 signal routed to resistance R881.
Channel 3 signal routed to resistance R882.

#### SPI

The EVK board need to be reworked to solder R1217/R1218/R1219/R1220 with 0R resistances.
SPI1 on J35 is enabled for M7.

#### Ethernet

NETC driver supports to manage the Physical Station Interface (PSI).
The first ENET1 port could be enabled for M7 by west build option
`-DEXTRA_DTC_OVERLAY_FILE=enetc_psi0.overlay`.

## Programming and Debugging (A55)

The `imx95_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

There are multiple methods to program and run Zephyr on the A55 core:

### Option 1. Boot Zephyr by Using SPSDK Runner

SPSDK runner leverages SPSDK tools ([https://spsdk.readthedocs.io](https://spsdk.readthedocs.io)), it builds an
bootable flash image `flash.bin` which includes all necessary firmware components,
such as ELE+V2X firmware, System Manager, TCM OEI, TF-A images etc. Using west flash
command will download the boot image flash.bin to DDR memory, SD card or eMMC flash.
By using flash.bin, as no U-Boot image is available, so TF-A will boot up Zephyr on
the first Cortex-A55 Core directly.

In order to use SPSDK runner, it requires fetching binary blobs, which can be achieved
by running the following command:

```shell
west blobs fetch hal_nxp
```

Note

It is recommended running the command above after `west update`.

SPSDK runner is enabled by configure item `CONFIG_BOARD_NXP_SPSDK_IMAGE`, currently
it is not enabled by default for i.MX95 EVK board, so use this configuration to enable
it, for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/a55 samples/synchronization -- -DCONFIG_BOARD_NXP_SPSDK_IMAGE=y
```

If `CONFIG_BOARD_NXP_SPSDK_IMAGE` is available and enabled for the board variant,
`flash.bin` will be built automatically. The programming could be through below commands.
Before that, switch SW7[1:4] should be configured to 0b1001 for usb download mode
to boot, and USB1 and DBG ports should be connected to PC. There are 4 serial ports
enumerated (115200 8n1), and we use the first for M7 and the fourth for M33 System Manager.
(The flasher is spsdk which already installed via scripts/requirements.txt.
On linux host, usb device permission should be configured per Installation Guide
of [https://spsdk.readthedocs.io](https://spsdk.readthedocs.io))

```text
# load and run without programming. for next flashing, execute 'reset' in the
# fourth serail port
$ west flash

# program to SD card, then set SW7[1:4]=0b1011 to reboot
$ west flash --bootdevice sd

# program to emmc card, then set SW7[1:4]=0b1010 to reboot
$ west flash --bootdevice=emmc
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “go” command can be used to start Zephyr on A55 core0 and U-Boot “cpu” command
is used to load and kick Zephyr to the other A55 secondary Cores. Currently “cpu” command
is supported in : [Real-Time Edge U-Boot](https://github.com/nxp-real-time-edge-sw/real-time-edge-uboot) (use the branch “uboot\_vxxxx.xx-y.y.y,
xxxx.xx is uboot version and y.y.y is Real-Time Edge Software version, for example
“uboot\_v2023.04-2.9.0” branch is U-Boot v2023.04 used in Real-Time Edge Software release
v2.9.0), and pre-build images and user guide can be found at [Real-Time Edge Software](https://www.nxp.com/rtedge).

#### Step 1: Download Zephyr Image into DDR Memory

Firstly need to download Zephyr binary image into DDR memory, it can use tftp:

```shell
tftp 0xd0000000 zephyr.bin
```

Or copy the Zephyr image `zephyr.bin` SD card and plug the card into the board, for example
if copy to the FAT partition of the SD card, use the following U-Boot command to load the image
into DDR memory (assuming the SD card is dev 1, fat partition ID is 1, they could be changed
based on actual setup):

```shell
fatload mmc 1:1 0xd0000000 zephyr.bin;
```

#### Step 2: Boot Zephyr

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Basic Synchronization](../../../../samples/synchronization/README.md#synchronization "Manipulate basic kernel synchronization primitives.") sample:

```shell
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/a55 samples/synchronization
```

This will build an image (zephyr.bin) with the synchronization sample app.

Then use the following command to boot Zephyr on the core0:

```shell
dcache off; icache flush; go 0xd0000000;
```

Or use “cpu” command to boot from secondary Core, for example Core1:

```shell
dcache flush; icache flush; cpu 1 release 0xd0000000
```

It will display the following console output:

```shell
*** Booting Zephyr OS build v3.6.0-4569-g483c01ca11a7 ***
thread_a: Hello World from cpu 0 on imx95_evk!
thread_b: Hello World from cpu 0 on imx95_evk!
thread_a: Hello World from cpu 0 on imx95_evk!
thread_b: Hello World from cpu 0 on imx95_evk!
thread_a: Hello World from cpu 0 on imx95_evk!
```

### Option 3. Boot Zephyr by Using Remoteproc under Linux

When running Linux on the A55 core, it can use the remoteproc framework to load and boot Zephyr,
refer to Real-Time Edge user guide for more details. Pre-build images and user guide can be found
at [Real-Time Edge Software](https://www.nxp.com/rtedge).

## Programming and Debugging (M7)

The i.MX System Manager (SM) is used on i.MX95, which is an application that runs on
Cortex-M33 processor. The Cortex-M33 is the boot core, runs the boot ROM which loads
the SM (and other boot code), and then branches to the SM. The SM then configures some
aspects of the hardware such as isolation mechanisms and then starts other cores in the
system. After starting these cores, it enters a service mode where it provides access
to clocking, power, sensor, and pin control via a client RPC API based on ARM’s
[System Control and Management Interface (SCMI)](https://developer.arm.com/documentation/den0056/latest/).

To program M7, an i.MX container image `flash.bin` must be made, which contains
multiple elements required, like ELE+V2X firmware, System Manager, TCM OEI, Cortex-M7
image and so on.

SPSDK runner is used to build `flash.bin`, and it requires fetching binary blobs, which
can be achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

Note

It is recommended running the command above after `west update`.

Two methods to build and program `flash.bin`.

1. If `CONFIG_BOARD_NXP_SPSDK_IMAGE` is not available for the board variant,
the steps making flash.bin and programming should refer to `Getting Started with
MCUXpresso SDK for IMX95LPD5EVK-19.pdf` in i.MX95 [MCUX SDK release](https://mcuxpresso.nxp.com/). Note that
for the DDR variant, one should use the Makefile targets containing the `ddr` keyword.
See `4.2 Run an example application`, just rename `zephyr.bin` to `m7_image.bin`
to make flash.bin and program to SD/eMMC.

2. If `CONFIG_BOARD_NXP_SPSDK_IMAGE` is available and enabled for the board variant,
`flash.bin` will be built automatically. The programming could be through below commands.
Before that, switch SW7[1:4] should be configured to 0b1001 for usb download mode
to boot, and USB1 and DBG ports should be connected to PC. There are 4 serial ports
enumerated (115200 8n1), and we use the first for M7 and the fourth for M33 System Manager.
(The flasher is spsdk which already installed via scripts/requirements.txt.
On linux host, usb device permission should be configured per Installation Guide
of [https://spsdk.readthedocs.io](https://spsdk.readthedocs.io))

```text
# load and run without programming. for next flashing, execute 'reset' in the
# fourth serail port
$ west flash

# program to SD card, then set SW7[1:4]=0b1011 to reboot
$ west flash --bootdevice sd

# program to emmc card, then set SW7[1:4]=0b1010 to reboot
$ west flash --bootdevice=emmc
```

Zephyr supports two M7-based i.MX95 boards: `imx95_evk/mimx9596/m7` and
`imx95_evk/mimx9596/m7/ddr`. The main difference between them is the memory
used. `imx95_evk/mimx9596/m7` uses TCM (ITCM for code and, generally, read-only
data and DTCM for R/W data), while `imx95_evk/mimx9596/m7/ddr` uses DDR.

1. Building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application for the TCM-based board

```shell
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/m7 samples/hello_world
```

2. Building the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application for the DDR-based board

```shell
# From the root of the zephyr repository
west build -b imx95_evk/mimx9596/m7/ddr samples/hello_world
```

After making flash.bin and program to SD/eMMC, open a serial terminal, and reset the
board. For the `imx95_evk/mimx9596/m7` board you should see something like:

```shell
*** Booting Zephyr OS build v3.6.0-4569-g483c01ca11a7 ***
Hello World! imx95_evk/mimx9596/m7
```

while, for the `imx95_evk/mimx9596/m7/ddr` board, you should get the following output:

```shell
*** Booting Zephyr OS build v3.6.0-4569-g483c01ca11a7 ***
Hello World! imx95_evk/mimx9596/m7/ddr
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
