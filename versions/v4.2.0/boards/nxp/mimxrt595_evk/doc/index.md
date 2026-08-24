---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt595_evk/doc/index.html
original_path: boards/nxp/mimxrt595_evk/doc/index.html
---

# MIMXRT595-EVK

Board Overview

[![../../../../_images/mimxrt595_evk.jpg](https://docs.zephyrproject.org/4.2.0/_images/mimxrt595_evk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt595_evk.jpg)

MIMXRT595-EVK

Name:
:   `mimxrt595_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   xtensa, arm

SoC:
:   mimxrt595s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt595_evk/doc/index.rst/../..)

## Overview

i.MX RT500 crossover MCUs are part of the edge computing family and are optimized
for low-power HMI applications by combining a graphics engine and a streamlined
Cadence Tensilica Fusion F1 DSP core with a next-generation Arm Cortex-M33
core. These devices are designed to unlock the potential of display-based applications
with a secure, power-optimized embedded processor.

i.MX RT500 MCUs provides up to 5MB of on-chip SRAM and several high-bandwidth interfaces
to access off-chip flash, including an Octal/Quad SPI interface with an on-the-fly
decryption engine.

## Hardware

- MIMXRT595SFFOC Cortex-M33 (275 MHz) core processor with Cadence Tensilica Fusion F1 DSP
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP protocol (supporting Cortex M33 debug only)
- USB2.0 high-speed host and device with micro USB connector and external crystal
- Octal/Quad/pSRAM external memories via FlexSPI
- 5 MB system SRAM
- Full size SD card slot (SDIO)
- On-board eMMC chip
- On-board 5 V inputs NXP PCA9420UK PMIC providing 1.2 V, 1.8 V, 3.3 V
- User LEDs
- Reset and User buttons
- MIPI-DSI connector
- Single row headers for ARDUINO signals and MikroBus connector
- FlexIO connector for MikroElektronica TFT Proto 5 inch capacitive touch display
- One motion sensor combo accelero-/magneto-meter NXP FXOS8700CQ
- Stereo audio codec with line-In/ line-Out/ and Microphone
- Pmod/host expansion connector
- NXP TFA9896 audio digital amplifier
- Support for up to eight off-board digital microphones via 12-pin header
- Two on-board digital microphones

For more information about the MIMXRT595 SoC and MIMXRT595-EVK board, see
these references:

- [i.MX RT595 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt500-crossover-mcu-with-arm-cortex-m33-dsp-and-gpu-cores:i.MX-RT500)
- [i.MX RT595 Datasheet](https://www.nxp.com/docs/en/data-sheet/IMXRT500EC.pdf)
- [i.MX RT595 Reference Manual](https://www.nxp.com/webapp/Download?colCode=IMXRT500RM)
- [MIMXRT595-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt595-evaluation-kit:MIMXRT595-EVK)
- [MIMXRT595-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=MIMXRT595EVKHUG)
- [MIMXRT595-EVK Schematics](https://www.nxp.com/downloads/en/schematics/MIMXRT595-EVK-DESIGN-FILES.zip)
- [MIMXRT595-EVK Debug Firmware](https://www.nxp.com/docs/en/application-note/AN13206.pdf)

### Supported Features

NXP considers the MIMXRT595-EVK as a superset board for the i.MX RT5xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT5xx family. NXP prioritizes enabling
this board with new support for Zephyr features. Another very similar
board is the [MIMXRT685-EVK](../../mimxrt685_evk/doc/index.md#mimxrt685_evk), and that board may have additional features
already supported, which can also be re-used on this mimxrt595\_evk board.

The `mimxrt595_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt595_evk/mimxrt595s/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L27) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L564) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | LPC Flexcomm node[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L253) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L431) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp%2Cdmic.md#std-dtcompatible-nxp-dmic) |
| on-board | WM8904 audio codec[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L472) | [`wolfson,wm8904`](../../../../build/dts/api/bindings/audio/wolfson%2Cwm8904.md#std-dtcompatible-wolfson-wm8904) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L126) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L501) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L587) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L682) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L693)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L698) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| Display | on-chip | NXP DCNano LCDIF (LCD Interface) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L370) | [`nxp,dcnano-lcdif`](../../../../build/dts/api/bindings/display/nxp%2Cdcnano-lcdif.md#std-dtcompatible-nxp-dcnano-lcdif) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L407)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L419) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| on-chip | NXP SmartDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L578) | [`nxp,smartdma`](../../../../build/dts/api/bindings/dma/nxp%2Csmartdma.md#std-dtcompatible-nxp-smartdma) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L165) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L171) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L76) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L160) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | LPC I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L271) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| I2S | on-chip | LPC I2S node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L244) | [`nxp,lpc-i2s`](../../../../build/dts/api/bindings/i2s/nxp%2Clpc-i2s.md#std-dtcompatible-nxp-lpc-i2s) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L660) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L46) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L223) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L60) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L673) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| MIPI-DSI | on-chip | NXP MCUX MIPI DSI 2L[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L647) | [`nxp,mipi-dsi-2l`](../../../../build/dts/api/bindings/mipi-dsi/nxp%2Cmipi-dsi-2l.md#std-dtcompatible-nxp-mipi-dsi-2l) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L34) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI MX25UM51345G[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L393) | [`nxp,imx-flexspi-mx25um51345g`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L404) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | AP Memory APS6408L pSRAM on NXP FlexSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L442) | [`nxp,imx-flexspi-aps6408l`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-aps6408l.md#std-dtcompatible-nxp-imx-flexspi-aps6408l) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L133) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | RT600/RT500 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L136) | [`nxp,rt-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Crt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl) |
| Power management | on-chip | Properties for NXP power management through the PDCFG register[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L49) | [`nxp,pdcfg-power`](../../../../build/dts/api/bindings/power/nxp%2Cpdcfg-power.md#std-dtcompatible-nxp-pdcfg-power) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L514) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-board | NXP PCA9420 PMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L235) | [`nxp,pca9420`](../../../../build/dts/api/bindings/regulator/nxp%2Cpca9420.md#std-dtcompatible-nxp-pca9420) |
| on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L127) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L148) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp%2Crstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L507) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L496) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L540)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L552) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt595_evk/mimxrt595_evk_mimxrt595s_cm33.dts?plain=1#L168) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | LPC USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L235) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L118) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L396)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L385) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L82) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L489) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer) |
| on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | NXP LPCIP3511 USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L377) | [`nxp,lpcip3511`](../../../../build/dts/api/bindings/usb/nxp%2Clpcip3511.md#std-dtcompatible-nxp-lpcip3511) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L524)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt5xx_common.dtsi?plain=1#L532) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

### Connections and IOs

The MIMXRT595 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | USART0 | USART RX |
| PIO0\_1 | USART0 | USART TX |
| PIO0\_14 | GPIO | GREEN LED |
| PIO0\_25 | GPIO | SW0 |
| PIO0\_10 | GPIO | SW1 |
| PIO4\_30 | USART12 | USART TX |
| PIO4\_31 | USART12 | USART RX |
| PIO0\_29 | I2C | I2C SCL |
| PIO0\_30 | I2C | I2C SDA |
| PIO0\_22 | GPIO | FXOS8700 TRIGGER |
| PIO1\_5 | SPI | SPI MOSI |
| PIO1\_4 | SPI | SPI MISO |
| PIO1\_3 | SPI | SPI SCK |
| PIO1\_6 | SPI | SPI SSEL |
| PIO0\_5 | SCT0 | SCT0 GPI0 |
| PIO0\_6 | SCT0 | SCT0 GPI1 |

### System Clock

The MIMXRT595 EVK is configured to use the OS Event timer
as a source for the system clock.

### Serial Port

The MIMXRT595 SoC has 13 FLEXCOMM interfaces for serial communication. One is
configured as USART for the console and the remaining are not used.

### Fusion F1 DSP Core

You can build a Zephyr application for the RT500 DSP core by targeting the F1
SOC. Xtensa toolchain supporting RT500 DSP core is included in Zephyr SDK.
To build the hello\_world sample for the RT500 DSP core:

```shell
$ west build -b mimxrt595_evk/mimxrt595s/f1 samples/hello_world
```

For detailed instructions on how to debug DSP firmware, please refer to
this document: [Getting Started with Xplorer for EVK-MIMXRT595](https://www.nxp.com/docs/en/supporting-information/GSXEVKMIMXRT595.pdf)

## Programming and Debugging

The `mimxrt595_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ | ✅ | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the LPC-Link2.

LPCLink2 JLink OnboardJLink ExternalLinkserver

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To connect the SWD signals to onboard debug circuit, install jumpers JP17, JP18 and JP19,
   if not already done (these jumpers are installed by default).
3. Follow the instructions in [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to program the
   J-Link firmware. Please make sure you have the latest firmware for this board.

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To disconnect the SWD signals from onboard debug circuit, **remove** jumpers J17, J18,
   and J19 (these are installed by default).
3. Connect the J-Link probe to J2 10-pin header.

See [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) for more information.

1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your search path.
2. To update the debug firmware, please follow the instructions on MIMXRT595-EVK Debug Firmware

### Configuring a Console

Connect a USB cable from your PC to J40, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS v2.7 ***
Hello World! mimxrt595_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt595_evk/mimxrt595s/cm33 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS v2.7 ***
Hello World! mimxrt595_evk
```

### Troubleshooting

If the debug probe fails to connect with the following error, it’s possible
that the image in flash is interfering and causing this issue.

```shell
Remote debugging using :2331
Remote communication error.  Target disconnected.: Connection reset by peer.
"monitor" command not supported by this target.
"monitor" command not supported by this target.
You can't do that when your target is `exec'
(gdb) Could not connect to target.
Please check power, connection and settings.
```

You can fix it by erasing and reprogramming the flash with the following
steps:

1. Set the SW7 DIP switches to ON-ON-ON to prevent booting from flash.
2. Reset by pressing SW3
3. Run `west debug` or `west flash` again with a known working Zephyr
   application (example “Hello World”).
4. Set the SW5 DIP switches to OFF-OFF-ON to boot from flash.
5. Reset by pressing SW3

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
