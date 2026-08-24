---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt700_evk/doc/index.html
original_path: boards/nxp/mimxrt700_evk/doc/index.html
---

# MIMXRT700-EVK

Board Overview

Name:
:   `mimxrt700_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   xtensa, arm

SoC:
:   mimxrt798s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt700_evk/doc/index.rst/../..)

## Overview

The new i.MX RT700 CPU architecture is composed of a high-performance main-compute subsystem,
a secondary “always-on” sense-compute subsystem and specialized coprocessors.

The main-compute subsystem has a primary Arm® Cortex®-M33 running at 325 MHz, with an integrated
Cadence® Tensilica® HiFi 4 DSP for more demanding DSP and audio processing tasks.
The sense-compute subsystem has a second Arm® Cortex®-M33 and an integrated Cadence® Tensilica®
HiFi 1 DSP. This removes the need for an external sensor hub, reducing system design complexity,
footprint and BOM costs.

The HiFi4 is a high performance DSP core based upon a Very Long Instruction Word (VLIW) architecture,
which is capable of processing up to eight 32x16 MACs per instruction cycle. It can be used for offloading
high-performance numerical tasks such as audio and image processing and supports both fixed-point and
floating-point operations.

The i.MX RT700 also features NXP’s eIQ Neutron NPU, enabled with the eIQ machine learning software
development environment.

## Hardware

- Main Compute Subsystem:
  :   - Arm Cortex-M33 up to 325 MHz
      - HiFi 4 DSP up to 325 MHz
      - eIQ Neutron NPU up to 325 MHz
- Sense Compute Subsystem:
  :   - Arm Cortex-M33 up to 250 MHz
      - HiFi 1 DSP up to 250 MHz
- 7.5 MB on-chip SRAM
- Three xSPI interfaces for off-chip memory expansion, supporting up to 16b wide external memories up to 250 MHz DDR
- eUSB support with integrated PHY
- Two SD/eMMC memory card interfaces—one supporting eMMC 5.0 with HS400/DDR operation
- USB high-speed host/device controller with on-chip PHY
- A digital microphone interface supporting up to 8 channels
- Serial peripherals (UART/I²C/I3C/SPI/HSPI/SAI)
- 2.5D GPU with vector graphics acceleration and frame buffer compression
- EZH-V using RISC-V core with additional SIMD/DSP instructions
- Full openVG 1.1 support
- Up to [720p@60FPS](mailto:720p%4060FPS) from on-chip SRAM
- LCD Interface + MIPI DSI
- Integrated JPEG and PNG support
- CSI 8/10/16-bit parallel (via FlexIO)

For more information about the MIMXRT798 SoC and MIMXRT700-EVK board, see
these references:

- [i.MX RT700 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt700-crossover-mcu-with-arm-cortex-m33-npu-dsp-and-gpu-cores:i.MX-RT700)

### Supported Features

NXP considers the MIMXRT700-EVK as a superset board for the i.MX RT7xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT7xx family. NXP prioritizes enabling
this board with new support for Zephyr features.

The `mimxrt700_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt700_evk/mimxrt798s/cm33_cpu0` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L21) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L119) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| Audio | on-board | WM8962 audio codec[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L144) | [`wolfson,wm8962`](../../../../build/dts/api/bindings/audio/wolfson,wm8962.md#std-dtcompatible-wolfson-wm8962) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L159) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L63) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L183)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L195) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1006) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1017)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1023) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DMA | on-chip | NXP MCUX EDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L243)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L258) | [`nxp,mcux-edma`](../../../../build/dts/api/bindings/dma/nxp,mcux-edma.md#std-dtcompatible-nxp-mcux-edma) |
| GPIO & Headers | on-chip | Kinetis GPIO[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L316)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L356) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L503)[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L425) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I2S | on-chip | NXP mcux SAI-I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1073)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1090) | [`nxp,mcux-i2s`](../../../../build/dts/api/bindings/i2s/nxp,mcux-i2s.md#std-dtcompatible-nxp-mcux-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L50) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L38) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Low Power Flexcomm[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L396)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L435) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MIPI-DBI | on-chip | DBI settings for NXP DCnano LCD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1134) | [`nxp,mipi-dbi-dcnano-lcdif`](../../../../build/dts/api/bindings/mipi-dbi/nxp,mipi-dbi-dcnano-lcdif.md#std-dtcompatible-nxp-mipi-dbi-dcnano-lcdif) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI 2L[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1141) | [`nxp,mipi-dsi-2l`](../../../../build/dts/api/bindings/mipi-dsi/nxp,mipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l) |
| Miscellaneous | on-chip | NXP FlexIO controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1042) | [`nxp,flexio`](../../../../build/dts/api/bindings/misc/nxp,flexio.md#std-dtcompatible-nxp-flexio) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L27) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP XSPI MX25UM51345G[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L218) | [`nxp,xspi-mx25um51345g`](../../../../build/dts/api/bindings/mtd/nxp,xspi-mx25um51345g.md#std-dtcompatible-nxp-xspi-mx25um51345g) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L298) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp,lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | RT600/RT500 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L58) | [`nxp,rt-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1124) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu0.dts?plain=1#L86) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L135) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp,rstctl.md#std-dtcompatible-nxp-rstctl) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L407)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L446) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L943)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L414) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| on-chip | NXP XSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L44) | [`nxp,xspi`](../../../../build/dts/api/bindings/spi/nxp,xspi.md#std-dtcompatible-nxp-xspi) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L88) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1050) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L980)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L990) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1000) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp,usbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1057)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu0.dtsi?plain=1#L1065) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

#### `mimxrt700_evk/mimxrt798s/cm33_cpu1` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L20) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L94) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp,lpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L134) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L158)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L170) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| GPIO & Headers | on-chip | Kinetis GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L256)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L267) | [`nxp,kinetis-gpio`](../../../../build/dts/api/bindings/gpio/nxp,kinetis-gpio.md#std-dtcompatible-nxp-kinetis-gpio) |
| I2C | on-chip | NXP LPI2C controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L316) | [`nxp,lpi2c`](../../../../build/dts/api/bindings/i2c/nxp,lpi2c.md#std-dtcompatible-nxp-lpi2c) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L243)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L230) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp,mcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Multi-Function Device | on-chip | Low Power Flexcomm[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L363)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L289) | [`nxp,lp-flexcomm`](../../../../build/dts/api/bindings/mfd/nxp,lp-flexcomm.md#std-dtcompatible-nxp-lp-flexcomm) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L26) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L218) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp,lpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | RT600/RT500 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L49) | [`nxp,rt-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp,rt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L110) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp,rstctl.md#std-dtcompatible-nxp-rstctl) |
| Sensors | on-board | NXP P3T1755 digital temperature sensor connected to I3C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt700_evk/mimxrt700_evk_mimxrt798s_cm33_cpu1.dts?plain=1#L94) | [`nxp,p3t1755`](../../../../build/dts/api/compatibles/nxp,p3t1755.md#std-dtcompatible-nxp-p3t1755) |
| Serial controller | on-chip | NXP LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L374)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L300) | [`nxp,lpuart`](../../../../build/dts/api/bindings/serial/nxp,lpuart.md#std-dtcompatible-nxp-lpuart) |
| SPI | on-chip | NXP LPSPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L306) | [`nxp,lpspi`](../../../../build/dts/api/bindings/spi/nxp,lpspi.md#std-dtcompatible-nxp-lpspi) |
| SRAM | on-chip | Generic on-chip SRAM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L67) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt7xx_cm33_cpu1.dtsi?plain=1#L448) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |

### Connections and IOs

The MIMXRT798 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_6 | I2C | I2C SDA |
| PIO0\_7 | I2C | I2C SCL |
| PIO0\_31 | UART0 | UART RX |
| PIO1\_0 | UART0 | UART TX |
| PIO0\_18 | GPIO | GREEN LED |
| PIO0\_9 | GPIO | SW5 |
| PIO8\_14 | UART19 | UART TX |
| PIO8\_15 | UART19 | UART RX |
| PIO3\_0 | SPI | SPI MOSI |
| PIO3\_1 | SPI | SPI SCK |
| PIO3\_2 | SPI | SPI MISO |
| PIO3\_3 | SPI | SPI SSEL |

### System Clock

The MIMXRT700 EVK is configured to use the Systick
as a source for the system clock.

### HiFi1 DSP Core

One can build a Zephyr application for the i.MX RT700 HiFi 1 DSP core by targeting the HiFi 1
SOC. Xtensa toolchain supporting RT700 DSP cores is included in Zephyr SDK.

To build the hello\_world sample for the i.MX RT700 HiFi 1 DSP core:

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/hifi1 samples/hello_world
```

### HiFi4 DSP Core

One can build a Zephyr application for the i.MX RT700 HiFi 4 DSP core by targeting the HiFi 4
SOC. Xtensa toolchain supporting RT700 DSP cores is included in Zephyr SDK.

To build the hello\_world sample for the i.MX RT700 HiFi 4 DSP core:

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/hifi4 samples/hello_world
```

## Programming and Debugging

The `mimxrt700_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ | ✅ | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the MCU-Link CMSIS-DAP Onboard Debug Probe.

LinkServerJLink External

1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
2. To put the board in `DFU mode` to program the firmware, short jumper J20.
3. To update the debug firmware, please follow the instructions on MIMXRT700-EVK Debug Firmware

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To disconnect the SWD signals from onboard debug circuit, **short** jumpers JP18.
3. Connect the J-Link probe to J18 20-pin header.

See [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) for more information.

### Configuring a Console

Connect a USB cable from your PC to J54, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

The DIP switch SW10 selects the boot options. Set SW10 to Off-On (01) to boot from the default
external flash on XSPI0.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt700_evk/mimxrt798s/cm33_cpu0 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS v3.7.0 ***
Hello World! mimxrt700_evk/mimxrt798s/cm33_cpu0
```

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## Display Support

The mimxrt700\_evk board supports following in-tree display module(s). Setup for
each module is described below:

### NXP G1120B0MIPI MIPI Display

The [NXP G1120B0MIPI MIPI Display](../../../shields/g1120b0mipi/doc/index.md#g1120b0mipi) connects to the board’s MIPI connector J52
directly, but some modifications are required (see
[boards/shields/g1120b0mipi/boards/mimxrt700\_evk\_mimxrt798s\_cm33\_cpu0.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/g1120b0mipi/boards/mimxrt700_evk_mimxrt798s_cm33_cpu0.overlay)
for a list). The display sample can be built for this module like so:

```shell
west build -b mimxrt700_evk --shield g1120b0mipi samples/drivers/display
```
