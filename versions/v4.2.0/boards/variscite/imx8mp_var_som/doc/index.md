---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/variscite/imx8mp_var_som/doc/index.html
original_path: boards/variscite/imx8mp_var_som/doc/index.html
---

# VAR-SOM-MX8M-PLUS

Board Overview

[![../../../../_images/imx8mp_var_som.webp](https://docs.zephyrproject.org/4.2.0/_images/imx8mp_var_som.webp)
](https://docs.zephyrproject.org/4.2.0/_images/imx8mp_var_som.webp)

VAR-SOM-MX8M-PLUS

Name:
:   `imx8mp_var_som`

Vendor:
:   Variscite Ltd.

Architecture:
:   arm64, arm

SoC:
:   mimx8ml8

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/variscite/imx8mp_var_som/doc/index.rst/../..)

## Overview

Variscite’s VAR-SOM-MX8M-PLUS System on Module (SoM) is based on the i.MX 8M Plus family,
which is a set of NXP products built to achieve both high performance and low power
consumption and relies on a powerful, fully coherent core complex based on a quad Cortex®-A53
cluster and Cortex®-M7 low-power coprocessor, audio digital signal processor, machine learning
and graphics accelerators.

Zephyr OS is ported to run on either the Cortex®-A53 or the Cortex®-M7.

## Specs Summary

> - CPU
>
>   - NXP i.MX8M Plus:
>   - Up to 4x Cortex®-A53 @ 1.8GHz
>   - 1x Cortex®-M7 @ 800 MHz
>   - 1x NPU 2.3 TOPS
> - Memory
>
>   - Up to 8GB LPDDR4 RAM @ 2000MHz
>   - 8-bit up to 128GB eMMC boot and storage
> - GPU
>
>   - 3D: Vivante™ GC7000UltraLite (2 shaders) OpenGL ES 3.0, OpenCL1.2, Vulkan
>   - 2D: Vivante™ GC520L
> - NPU (Neural Processing Unit)
>
>   - 2.3 TOPS Neural Network performance
> - Display
>
>   - 2x LVDS interface 4-lane each up to 1080p60
>   - HDMI 2.0a up to 4Kp30
>   - 1x MIPI DSI with up to 4 data lanes 1080p60
> - Network
>
>   - 2x 10/100/1000 Mbit/s Ethernet Interface
>   - Certified Wi-Fi 6 dual-band 802.11ax/ac/a/b/g/n with optional 802.15.4
>   - Bluetooth/BLE 5.4
> - Camera
>
>   - Up to 2x MIPI CSI – CMOS Serial camera Interface 4 lanes
>   - 375 Mpixel/s HDR ISP (Image Sensor Processor)
> - Audio
>
>   - Headphones
>   - Microphone: Digital, Analog (stereo)
>   - 6x I2S(SAI), S/PDIF RX TX, PDM 8CH, Line In/Out
> - USB
>
>   - 2x USB 3.0/2.0 Host/Device
> - Serial interfaces
>
>   - SPI: x3
>   - I2C: x5
>   - UART: x4, up to 5 Mbps
>   - CAN: x2
> - Temperature range
>
>   - -40°C to 85°C

More information about the SoM can be found at the
[Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX8M-PLUS) and
[Variscite website](https://www.variscite.com/product/system-on-module-som/cortex-a53-krait/var-som-mx8m-plus-nxp-i-mx-8m-plus).

## Supported Features

The `imx8mp_var_som` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### `imx8mp_var_som/mimx8ml8/a53` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-A53 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L40)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L22) | [`arm,cortex-a53`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-a53.md#std-dtcompatible-arm-cortex-a53) |
| CAN | on-chip | NXP FlexCAN CANFD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L192) | [`nxp,flexcan-fd`](../../../../build/dts/api/bindings/can/nxp%2Cflexcan-fd.md#std-dtcompatible-nxp-flexcan-fd) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L75) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| Ethernet | on-chip | NXP ENET1G IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L292) | [`nxp,enet1g`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet1g.md#std-dtcompatible-nxp-enet1g) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L299) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L314) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L107)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L81) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L220) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_a53.dts?plain=1#L57) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L60) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_a53.dts?plain=1#L49) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L308) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| Miscellaneous | on-chip | NXP i.MX Resource Domain Controller (RDC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L333) | [`nxp,rdc`](../../../../build/dts/api/bindings/misc/nxp%2Crdc.md#std-dtcompatible-nxp-rdc) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L323) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L327) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L180)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L168) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| Timer | on-chip | NXP MCUX General-Purpose Timer (GPT)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L146) | [`nxp,imx-gpt`](../../../../build/dts/api/bindings/timer/nxp%2Cimx-gpt.md#std-dtcompatible-nxp-imx-gpt) |
| on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm64/nxp/nxp_mimx8mp_a53.dtsi?plain=1#L47) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### `imx8mp_var_som/mimx8ml8/m7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L17) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L32) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L37) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L76) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L118)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L92) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L173) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_m7.dts?plain=1#L41) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L257) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp%2Cimx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_m7.dts?plain=1#L33) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L24) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L82) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L86) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L157)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L165) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L268) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

### `imx8mp_var_som/mimx8ml8/m7/ddr` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L17) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ARM architecture | on-chip | i.MX ITCM (Instruction Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L32) | [`nxp,imx-itcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-itcm.md#std-dtcompatible-nxp-imx-itcm) |
| on-chip | i.MX DTCM (Data Tightly Coupled Memory)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L37) | [`nxp,imx-dtcm`](../../../../build/dts/api/bindings/arm/nxp%2Cimx-dtcm.md#std-dtcompatible-nxp-imx-dtcm) |
| Clock control | on-chip | i.MX CCM (Clock Controller Module) IP node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L76) | [`nxp,imx-ccm`](../../../../build/dts/api/bindings/clock/nxp%2Cimx-ccm.md#std-dtcompatible-nxp-imx-ccm) |
| GPIO & Headers | on-chip | i.MX GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L118)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L92) | [`nxp,imx-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Cimx-gpio.md#std-dtcompatible-nxp-imx-gpio) |
| I2C | on-chip | NXP II2C[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L173) | [`nxp,ii2c`](../../../../build/dts/api/bindings/i2c/nxp%2Cii2c.md#std-dtcompatible-nxp-ii2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_m7_ddr.dts?plain=1#L58) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| IPM | on-chip | i.MX Messaging Unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L257) | [`nxp,imx-mu`](../../../../build/dts/api/bindings/ipm/nxp%2Cimx-mu.md#std-dtcompatible-nxp-imx-mu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/variscite/imx8mp_var_som/imx8mp_var_som_mimx8ml8_m7_ddr.dts?plain=1#L50) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L24) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| Pin control | on-chip | This compatible binding should be applied to the device’s iomuxc DTS node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L82) | [`nxp,imx-iomuxc`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx-iomuxc.md#std-dtcompatible-nxp-imx-iomuxc) |
| on-chip | The node has the ‘pinctrl’ node label set in MCUX SoC’s devicetree[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L86) | [`nxp,imx8mp-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cimx8mp-pinctrl.md#std-dtcompatible-nxp-imx8mp-pinctrl) |
| Serial controller | on-chip | This binding gives a base representation of the NXP iMX IUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L157)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L165) | [`nxp,imx-iuart`](../../../../build/dts/api/bindings/serial/nxp%2Cimx-iuart.md#std-dtcompatible-nxp-imx-iuart) |
| SPI | on-chip | NXP i.MX ECSPI controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_imx8ml_m7.dtsi?plain=1#L268) | [`nxp,imx-ecspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-ecspi.md#std-dtcompatible-nxp-imx-ecspi) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

Note

It is recommended to disable peripherals used by the M7 core on the Linux host.

### Devices

#### System Clock

This board configuration uses a system clock frequency of 8 MHz.

The M7 core is configured to run at an 800 MHz clock speed.

#### Serial Port

This board configuration uses a single serial communication channel with the
CPU’s UART4.

## Programming and Debugging (A53)

Copy the compiled `zephyr.bin` to the boot directory of the SD card and
plug the SD card into the board. Power it up and stop the U-Boot execution at
prompt.

Use U-Boot to load and run zephyr.bin on the Cortex-A53:

```shell
load mmc $mmcdev:$mmcpart $loadaddr /boot/zephyr.bin
dcache flush; icache flush; go $loadaddr
```

Use this configuration to run basic Zephyr applications and kernel tests,
for example, with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") sample:

```shell
# From the root of the zephyr repository
west build -b imx8mp_var_som/mimx8ml8/a53 samples/hello_world
```

This will build an image with the hello\_world sample app. When loaded and executed
it will display the following ram console output:

```shell
*** Booting Zephyr OS build v4.0.0-3113-g5aeda6fe7dfa ***
Hello World! imx8mp_var_som/mimx8ml8/a53
```

## Programming and Debugging (M7)

The `imx8mp_var_som` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The VAR-SOM-MX8M-PLUS don’t have QSPI flash for the M7, and it needs to be
started by the A53 core. The A53 core is responsible to load the M7 binary
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
| DDR | 0x80000000-0x803FFFFF | 0x7B200000-0x7B3FFFFF | 0x7B000000-0x7B1FFFFF | 2MB |

For more information about memory mapping see the
[i.MX 8M Applications Processor Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMX8MPRM) (section 2.1 to 2.3)

At compilation time you have to choose which RAM will be used. This
configuration is done based on board name (e.g. imx8mp\_var\_som/mimx8ml8/m7
for ITCM and imx8mp\_var\_som/mimx8ml8/m7/ddr for DDR).

There are two methods to load M7 Core images: U-Boot command and Linux remoteproc.

### Load and Run M7 Zephyr Image from U-Boot

Load and run Zephyr on M7 from A53 using U-Boot by copying the compiled
`zephyr.bin` to the boot directory of the SD card and plug the SD
card into the board. Power it up and stop the U-Boot execution at prompt.

Load the M7 binary onto the desired memory and start its execution using:

### ITCM

```shell
load mmc 1:1 0x48000000 /boot/zephyr.bin
cp.b 0x48000000 0x7e0000 20000
bootaux 0x7e0000
```

### DDR

```shell
load mmc 1:1 0x7b000000 /boot/zephyr.bin
dcache flush
bootaux 0x7b000000
```

### Load and Run M7 Zephyr Image by using Linux remoteproc

Transfer built binaries `zephyr.bin` and `zephyr.elf` to the SoM’s `/boot` and
`/lib/firmware` respectively using `scp` or through an USB drive.

It is possible to execute Zephyr binaries using Variscite remoteproc scripts made
for MCUXpresso binaries:

```shell
root@imx8mp-var-dart:~# /etc/remoteproc/variscite-rproc-linux -f /lib/firmware/zephyr.elf
[  212.888118] remoteproc remoteproc0: powering up imx-rproc
[  212.899215] remoteproc remoteproc0: Booting fw image zephyr.elf, size 515836
[  212.912070] remoteproc remoteproc0: No resource table in elf
[  213.444675] remoteproc remoteproc0: remote processor imx-rproc is now up
```

Which should yield the following result on the UART4 serial console:

```shell
*** Booting Zephyr OS build v4.0.0-3113-g5aeda6fe7dfa ***
Hello World! imx8mp_var_som/mimx8ml8/m7
```

If the device tree dedicated to be used with Cortex-M7 applications is not being
currently used, the script will give instructions on how to do so:

```shell
Error: /sys/class/remoteproc/remoteproc0 not found.
Please enable remoteproc driver.
Most likely you need to use the correct device tree, for example:
fw_setenv fdt_file imx8mp-var-som-symphony-m7.dtb && reboot
```

You can also configure U-Boot to load firmware on boot:

```shell
root@imx8mp-var-dart:~# /etc/remoteproc/variscite-rproc-u-boot -f /boot/zephyr.bin
Configuring for TCM memory
+ fw_setenv m7_addr 0x7E0000
+ fw_setenv fdt_file imx8mp-var-som-symphony-m7.dtb
+ fw_setenv use_m7 yes
+ fw_setenv m7_bin zephyr.bin

Finished: Please reboot, the m7 firmware will run during U-Boot
```

For more information about Variscite remoteproc scripts and general Cortex-M7
support, visit [Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX8M-PLUS).

### Debugging

VAR-SOM-MX8M-PLUS board can be debugged by connecting an external
JLink JTAG debugger to the 14-pin header on the top left side of
the SoM and to the PC. Then the application can be debugged using
the usual way.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b imx8mp_var_som/mimx8ml8/m7 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v4.0.0-3113-g5aeda6fe7dfa ***
Hello World! imx8mp_var_som/mimx8ml8/m7
```

## References

- [Variscite Wiki](https://variwiki.com/index.php?title=VAR-SOM-MX8M-PLUS)
- [Variscite website](https://www.variscite.com/product/system-on-module-som/cortex-a53-krait/var-som-mx8m-plus-nxp-i-mx-8m-plus)
- [i.MX 8M Applications Processor Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMX8MPRM)
