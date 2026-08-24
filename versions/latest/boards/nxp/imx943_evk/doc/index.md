---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/imx943_evk/doc/index.html
original_path: boards/nxp/imx943_evk/doc/index.html
---

# i.MX943 EVK

Board Overview

Name:
:   `imx943_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm64, arm

SoC:
:   mimx94398

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/imx943_evk/doc/index.rst/../..)

## Overview

The IMX943LP5EVK-19 board is a design and evaluation platform based on the
NXP i.MX 943 processor. The i.MX 943 processor integrates up to four Arm
Cortex-A55 cores, along with two Arm Cortex-M33 cores and two Arm Cortex-M7
cores for functional safety. With PLCs, I/O controllers, V2X accelerators,
ML acceleration, energy management, and advanced security, the i.MX 943
processor provides optimized performance and power efficiency for industrial,
IoT, and automotive devices. The i.MX943 device on the board comes in a
compact 19 x 19 mm package.

## Hardware

- i.MX 943 automotive applications processor

  - The processor integrates up to four Arm Cortex-A55 cores, and supports
    functional safety with built-in Arm Cortex-M33 and -M7 cores
- DRAM memory: 8-Gbit LPDDR5 DRAM
- XSPI interface: 64 MB octal SPI NOR flash memory
- eMMC: 32 GB eMMC NAND flash memory
- uSDHC interface: an SD card slot
- USB interface: Two USB Type-C ports
- Ethernet interface: seven Ethernet ports
- PCIe interface: one M.2 slot and one PCIe x4 slot.
- FlexCAN interface: four CAN controller with four CAN connector.
- LPUART interface
- LPSPI interface
- LPI2C interface
- SAI interface
- MQS interface
- MICFIL interface
- LVDS interface
- ADC interface
- SINC interface
- Debug interface

  - One USB-to-UART/MPSSE device, FT4232H
  - One USB 3.2 Type-C connector (J15) for FT4232H provides quad serial ports
  - JTAG header J16

### Supported Features

The `imx943_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `imx943_evk/mimx94398/a55` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A55 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L40)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L22) | [`arm,cortex-a55`](../../../../build/dts/api/bindings/cpu/arm,cortex-a55.md#std-dtcompatible-arm-cortex-a55) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L72) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm,scmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L79) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm,scmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L88) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm,scmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L94) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm,scmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| GPIO & Headers | on-chip | i.MX RGPIO[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L195) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L59) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L301)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L274) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp,mbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L98) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L283)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L105) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx943_a55.dtsi?plain=1#L47) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

#### `imx943_evk/mimx94398/m33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L17) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L82) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L87) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Ethernet | on-board | Generic MII PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx943_evk/imx943_evk_mimx94398_m33.dts?plain=1#L31) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-board | Realtek RTL8211F Ethernet PHY device[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx943_evk/imx943_evk_mimx94398_m33.dts?plain=1#L43) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP i.MX NETC Physical Station Interface (PSI)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L282) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp,imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-chip | NXP NETC PTP (Precision Time Protocol) Clock[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L306) | [`nxp,netc-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L37) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm,scmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L44) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm,scmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) power domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L53) | [`arm,scmi-power`](../../../../build/dts/api/bindings/firmware/arm,scmi-power.md#std-dtcompatible-arm-scmi-power) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L59) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm,scmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L65) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm,scmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| on-chip | System Control and Management Interface (SCMI) cpu domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L74) | [`nxp,scmi-cpu`](../../../../build/dts/api/bindings/firmware/nxp,scmi-cpu.md#std-dtcompatible-nxp-scmi-cpu) |
| GPIO & Headers | on-chip | i.MX RGPIO[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L172) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L249) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp,mbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L273) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp,imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L26) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L69) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L132)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L92) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

#### `imx943_evk/mimx94398/m33/ddr` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L17) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L82) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp,imx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L87) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp,imx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Ethernet | on-board | Generic MII PHY[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx943_evk/imx943_evk_mimx94398_m33.dts?plain=1#L31) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| on-board | Realtek RTL8211F Ethernet PHY device[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/imx943_evk/imx943_evk_mimx94398_m33.dts?plain=1#L43) | [`realtek,rtl8211f`](../../../../build/dts/api/bindings/ethernet/phy/realtek,rtl8211f.md#std-dtcompatible-realtek-rtl8211f) |
| on-chip | NXP i.MX NETC Physical Station Interface (PSI)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L282) | [`nxp,imx-netc-psi`](../../../../build/dts/api/bindings/ethernet/nxp,imx-netc-psi.md#std-dtcompatible-nxp-imx-netc-psi) |
| on-chip | NXP NETC PTP (Precision Time Protocol) Clock[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L306) | [`nxp,netc-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,netc-ptp-clock.md#std-dtcompatible-nxp-netc-ptp-clock) |
| Firmware | on-chip | System Control and Management Interface (SCMI) shared memory (SHMEM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L37) | [`arm,scmi-shmem`](../../../../build/dts/api/bindings/firmware/arm,scmi-shmem.md#std-dtcompatible-arm-scmi-shmem) |
| on-chip | System Control and Management Interface (SCMI) with doorbell and shared memory (SHMEM) transport[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L44) | [`arm,scmi`](../../../../build/dts/api/bindings/firmware/arm,scmi.md#std-dtcompatible-arm-scmi) |
| on-chip | System Control and Management Interface (SCMI) power domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L53) | [`arm,scmi-power`](../../../../build/dts/api/bindings/firmware/arm,scmi-power.md#std-dtcompatible-arm-scmi-power) |
| on-chip | System Control and Management Interface (SCMI) clock protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L59) | [`arm,scmi-clock`](../../../../build/dts/api/bindings/firmware/arm,scmi-clock.md#std-dtcompatible-arm-scmi-clock) |
| on-chip | System Control and Management Interface (SCMI) pinctrl protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L65) | [`arm,scmi-pinctrl`](../../../../build/dts/api/bindings/firmware/arm,scmi-pinctrl.md#std-dtcompatible-arm-scmi-pinctrl) |
| on-chip | System Control and Management Interface (SCMI) cpu domain protocol[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L74) | [`nxp,scmi-cpu`](../../../../build/dts/api/bindings/firmware/nxp,scmi-cpu.md#std-dtcompatible-nxp-scmi-cpu) |
| GPIO & Headers | on-chip | i.MX RGPIO[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L172) | [`nxp,imx-rgpio`](../../../../build/dts/api/bindings/gpio/nxp,imx-rgpio.md#std-dtcompatible-nxp-imx-rgpio) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L249) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp,mbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MDIO | on-chip | NXP i.MX NETC External MDIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L273) | [`nxp,imx-netc-emdio`](../../../../build/dts/api/bindings/mdio/nxp,imx-netc-emdio.md#std-dtcompatible-nxp-imx-netc-emdio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L26) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L69) | [`nxp,imx93-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,imx93-pinctrl.md#std-dtcompatible-nxp-imx93-pinctrl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L132)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx943_m33.dtsi?plain=1#L92) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

#### System Clock

This board configuration uses a system clock frequency of 24 MHz for Cortex-A55.
Cortex-A55 Core runs up to 1.7 GHz.
Cortex-M33 Core runs up to 333MHz in which SYSTICK runs on same frequency.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART1 for Cortex-A55, and UART8 for Cortex-M33.

#### Ethernet

NETC driver supports to manage the Physical Station Interface (PSI).
The ENET0, ENETC1, ENETC2 ports could be enabled for M33 by west build option
`-DEXTRA_DTC_OVERLAY_FILE=enetc.overlay`.

## Programming and Debugging (A55)

The `imx943_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

There are multiple methods to program and debug Zephyr on the A55 core:

### Option 1. Boot Zephyr by Using JLink Runner

#### Dependency

Need to disable all watchdog in U-Boot, otherwise, watchdog will reset the board
after Zephyr start up from the same A55 Core.

#### Setup

The default runner for the board is JLink, connect the EVK board’s JTAG connector to
the host computer using a J-Link debugger, power up the board and stop the board at
U-Boot command line.

Then use “west flash” or “west debug” command to load the zephyr.bin
image from the host computer and start the Zephyr application on A55 core0.

#### Flash and Run

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx943_evk/mimx94398/a55 samples/hello_world
west flash
```

Then the following log could be found on UART1 console:

```shell
*** Booting Zephyr OS build v4.1.0-3650-gdb71736adb68 ***
Hello World! imx943_evk/mimx94398/a55
```

#### Debug

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx943_evk/mimx94398/a55 samples/hello_world
west debug
```

### Option 2. Boot Zephyr by Using U-Boot Command

U-Boot “go” command can be used to start Zephyr on A55 Core0.

#### Dependency

Need to disable all watchdog in U-Boot, otherwise, watchdog will reset the board
after Zephyr start up from the same A55 Core.

#### Step 1: Build Zephyr application

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx943_evk/mimx94398/a55 samples/hello_world
```

#### Step 2: Download Zephyr Image into DDR Memory

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

#### Step 3: Boot Zephyr

Use the following command to boot Zephyr on the core0:

```shell
dcache flush; icache flush; go 0xd0000000;
```

Then the following log could be found on UART1 console:

```shell
*** Booting Zephyr OS build v4.1.0-3650-gdb71736adb68 ***
Hello World! imx943_evk/mimx94398/a55
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## Programming and Debugging (M33)

### Step 1. Build Zephyr application

Here is an example to build the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

For TCM target

```shell
# From the root of the zephyr repository
west build -b imx943_evk/mimx94398/m33 samples/hello_world
```

For DDR target

```shell
# From the root of the zephyr repository
west build -b imx943_evk/mimx94398/m33/ddr samples/hello_world
```

### Step 2. Build bootable firmware

The imx-mkimage tool and some other firmware files from [i.MX Linux BSP release](https://www.nxp.com/design/design-center/software/embedded-software/i-mx-software/embedded-linux-for-i-mx-applications-processors:IMXLINUX)
are required to make a bootable firmware to program to SD/eMMC.

Below is an operations example on Linux host. (For more detail, refer to
[i.MX Linux BSP release](https://www.nxp.com/design/design-center/software/embedded-software/i-mx-software/embedded-linux-for-i-mx-applications-processors:IMXLINUX) 6.12.3\_1.0.0)

```shell
# download

git clone https://github.com/nxp-imx/imx-mkimage.git -b lf-6.12.3_1.0.0
git clone https://github.com/nxp-imx/imx-sm.git      -b lf-6.12.3-imx943-er1
git clone https://github.com/nxp-imx/imx-oei.git     -b lf-6.12.3-imx943-er1

wget https://www.nxp.com/lgfiles/NMG/MAD/YOCTO/firmware-imx-8.27-5af0ceb.bin
wget https://www.nxp.com/lgfiles/NMG/MAD/YOCTO/firmware-ele-imx-2.0.1-0a66c34.bin

# some firmware files need to be unpacked

chmod 777 firmware-imx-8.27-5af0ceb.bin
chmod 777 firmware-ele-imx-2.0.1-0a66c34.bin
./firmware-imx-8.27-5af0ceb.bin --auto-accept
./firmware-ele-imx-2.0.1-0a66c34.bin --auto-accept

# some firmware files need to be built from source

export TOOLS=$ARMGCC_DIR
export SM_CROSS_COMPILE=${TOOLS}/bin/arm-none-eabi-
export OEI_CROSS_COMPILE=${TOOLS}/bin/arm-none-eabi-

make -C imx-oei board=mx943lp5-19 oei=ddr d=1 all
make -C imx-sm config=mx94alt cfg
make -C imx-sm config=mx94alt all

# make bootable firmware flash.bin

cp firmware-imx-8.27-5af0ceb/firmware/ddr/synopsys/lpddr5*v202409.bin imx-mkimage/iMX94/
cp firmware-ele-imx-2.0.1-0a66c34/mx943a0-ahab-container.img          imx-mkimage/iMX94/
cp imx-sm/build/mx94alt/m33_image.bin                                 imx-mkimage/iMX94/
cp imx-oei/build/mx943lp5-19/ddr/oei-m33-ddr.bin                      imx-mkimage/iMX94/
cp zephyr/build/zephyr/zephyr.bin                                     imx-mkimage/iMX94/m33s_image.bin

cd imx-mkimage
make SOC=iMX94 OEI=YES flash_m33s     # for TCM target
make SOC=iMX94 OEI=YES flash_m33s_ddr # for DDR target

# Program to SD card

dd if=iMX94/flash.bin of=/dev/sdb bs=1k seek=32 && sync
```

Note: for this Linux BSP release version, we need to do some changes in imx-sm and imx-mkimage
to support M33 boot and DDR target.

imx-sm changes:

```shell
diff --git a/configs/mx94alt.cfg b/configs/mx94alt.cfg
index 4613900..069992a 100755
--- a/configs/mx94alt.cfg
+++ b/configs/mx94alt.cfg
@@ -308,7 +308,7 @@ FAULT_SWNCF04       OWNER, reaction=sys_shutdown
 # Boot EENV                                                                #
 #==========================================================================#

-LM1                 name="Boot", rpc=scmi, boot=2, skip=1, did=3, default
+LM1                 name="Boot", rpc=scmi, boot=2, skip=1, did=13, default

 DFMT0:              sa=secure
 DFMT1:              sa=secure, pa=privileged
@@ -322,10 +322,6 @@ DATA:               perm=rw

 PD_NETC             stop=6
 CPU_M33S            start=1, stop=5
-PD_M70              stop=4
-CPU_M7P0            start=2, stop=3
-PD_M71              stop=2
-CPU_M7P1            start=3, stop=1

 # Start/Stop (mSel=1)
```

imx-mkimage changes:

```shell
diff --git a/iMX94/soc.mak b/iMX94/soc.mak
index 838d2a2..bc756f9 100644
--- a/iMX94/soc.mak
+++ b/iMX94/soc.mak
@@ -392,6 +392,11 @@ flash_m33s: $(MKIMG) $(AHAB_IMG) $(MCU_IMG) $(M33S_IMG) $(OEI_IMG_M33)
                   -m33 $(MCU_IMG) 0 $(MCU_TCM_ADDR) \
                   -m33 $(M33S_IMG) 1 $(M33S_TCM_ADDR) $(M33S_TCM_ADDR_ALIAS) -out flash.bin

+flash_m33s_ddr: $(MKIMG) $(AHAB_IMG) $(MCU_IMG) $(M33S_IMG) $(OEI_IMG_M33)
+       ./$(MKIMG) -soc IMX9 -cntr_version 2 -u 1 -append $(AHAB_IMG) -c $(OEI_OPT_M33) -msel $(MSEL) \
+                  -m33 $(MCU_IMG) 0 $(MCU_TCM_ADDR) \
+                  -m33 $(M33S_IMG) 1 0x86000000 0x86000000 -out flash.bin
+
 flash_m33s_xspi: $(MKIMG) $(AHAB_IMG) $(MCU_IMG) $(M33S_IMG) $(OEI_IMG_M33)
        ./$(MKIMG) -soc IMX9 -cntr_version 2 -u 1 -append $(AHAB_IMG) -dev flexspi -c $(OEI_OPT_M33) -msel $(MSEL) \
                   -m33 $(MCU_IMG) 0 $(MCU_TCM_ADDR) \
```

### Step 3. Boot Zephyr

Boot board from SD card. It will display the following console output.

For TCM target

```shell
*** Booting Zephyr OS build v4.1.0-5264-g8654b4029d16 ***
Hello World! imx943_evk/mimx94398/m33
```

For DDR target

```shell
*** Booting Zephyr OS build v4.1.0-5264-g8654b4029d16 ***
Hello World! imx943_evk/mimx94398/m33/ddr
```

Note: there will be 4 serial ports identified when connect USB cable to debug port.
The first serial port will be UART8 for M33. As there is multiplexing between JTAG
and UART8, below bcu ([bcu 1.1.113 download](https://github.com/nxp-imx/bcu/releases/tag/bcu_1.1.113)) configuration is needed to use UART8.

```shell
bcu lsftdi
bcu set_gpio fta_jtag_host_en 0 -board=imx943evk19b1 -id=1-1
```
