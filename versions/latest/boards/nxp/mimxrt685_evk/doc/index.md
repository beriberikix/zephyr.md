---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/mimxrt685_evk/doc/index.html
original_path: boards/nxp/mimxrt685_evk/doc/index.html
---

# MIMXRT685-EVK

Board Overview

[![../../../../_images/mimxrt685_evk.jpg](https://docs.zephyrproject.org/4.2.0/_images/mimxrt685_evk.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/mimxrt685_evk.jpg)

MIMXRT685-EVK

Name:
:   `mimxrt685_evk`

Vendor:
:   NXP Semiconductors

Architecture:
:   xtensa, arm

SoC:
:   mimxrt685s

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/mimxrt685_evk/doc/index.rst/../..)

## Overview

The i.MX RT600 is a crossover MCU family optimized for 32-bit immersive audio
playback and voice user interface applications combining a high-performance
Cadence Tensilica HiFi 4 audio DSP core with a next-generation Cortex-M33
core. The i.MX RT600 family of crossover MCUs is designed to unlock the
potential of voice-assisted end nodes with a secure, power-optimized embedded
processor.

The i.MX RT600 family provides up to 4.5MB of on-chip SRAM and several
high-bandwidth interfaces to access off-chip flash, including an Octal/Quad SPI
interface with an on-the-fly decryption engine.

## Hardware

- MIMXRT685SFVKB Cortex-M33 (300 MHz, 128 KB TCM) core processor with Cadence Xtensa HiFi4 DSP
- Onboard, high-speed USB, Link2 debug probe with CMSIS-DAP protocol (supporting Cortex M33 debug only)
- High speed USB port with micro A/B connector for the host or device functionality
- UART, I2C and SPI port bridging from i.MX RT685 target to USB via the on-board debug probe
- 512 MB Macronix Octal SPI Flash operating at 1.8 V
- 4.5 MB Apmemory PSRAM
- Full size SD card slot (SDIO)
- NXP PCA9420UK PMIC
- User LEDs
- Reset and User buttons
- Arduino and PMod/Host expansion connectors
- NXP FXOS8700CQ accelerometer
- Stereo audio codec with line in/out and electret microphone
- Stereo NXP TFA9894 digital amplifiers, with option for external +5V power for higher performance speakers
- Support for up to eight off-board digital microphones via 12-pin header
- Two on-board DMICS

For more information about the MIMXRT685 SoC and MIMXRT685-EVK board, see
these references:

- [i.MX RT685 Website](https://www.nxp.com/products/processors-and-microcontrollers/arm-microcontrollers/i-mx-rt-crossover-mcus/i-mx-rt600-crossover-mcu-with-arm-cortex-m33-and-dsp-cores:i.MX-RT600)
- [i.MX RT685 Datasheet](https://www.nxp.com/docs/en/data-sheet/RT600.pdf)
- [i.MX RT685 Reference Manual](https://www.nxp.com/webapp/Download?colCode=UM11147)
- [MIMXRT685-EVK Website](https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt600-evaluation-kit:MIMXRT685-EVK)
- [MIMXRT685-EVK User Guide](https://www.nxp.com/webapp/Download?colCode=UM11159)
- [MIMXRT685-EVK Schematics](https://www.nxp.com/downloads/en/design-support/RT685-DESIGNFILES.zip)

### Supported Features

NXP considers the MIMXRT685-EVK as a superset board for the i.MX RT6xx
family of MCUs. This board is a focus for NXP’s Full Platform Support for
Zephyr, to better enable the entire RT6xx family. NXP prioritizes enabling
this board with new support for Zephyr features. Another very similar
board is the [MIMXRT595-EVK](../../mimxrt595_evk/doc/index.md#mimxrt595_evk), and that board may have additional features
already supported, which can also be re-used on this mimxrt685\_evk board.

The `mimxrt685_evk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mimxrt685_evk/mimxrt685s/cm33` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L26) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | LPC LPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L506) | [`nxp,lpc-lpadc`](../../../../build/dts/api/bindings/adc/nxp%2Clpc-lpadc.md#std-dtcompatible-nxp-lpc-lpadc) |
| ARM architecture | on-chip | LPC Flexcomm node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L297) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L373) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp%2Cdmic.md#std-dtcompatible-nxp-dmic) |
| on-board | WM8904 audio codec[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L400) | [`wolfson,wm8904`](../../../../build/dts/api/bindings/audio/wolfson%2Cwm8904.md#std-dtcompatible-wolfson-wm8904) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L132) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L443) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L522) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L595) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L606) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L355)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L364) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L180) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L186) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L100) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| Hardware information | on-chip | NXP LPC 128-bit Unique identifier[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L175) | [`nxp,lpc-uid`](../../../../build/dts/api/bindings/hwinfo/nxp%2Clpc-uid.md#std-dtcompatible-nxp-lpc-uid) |
| I2C | on-chip | LPC I2C[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L261) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| I2S | on-chip | LPC I2S node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L252) | [`nxp,lpc-i2s`](../../../../build/dts/api/bindings/i2s/nxp%2Clpc-i2s.md#std-dtcompatible-nxp-lpc-i2s) |
| I3C | on-chip | NXP MCUX I3C controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L582) | [`nxp,mcux-i3c`](../../../../build/dts/api/bindings/i3c/nxp%2Cmcux-i3c.md#std-dtcompatible-nxp-mcux-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L51) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L231) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L65) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L81) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Mailbox | on-chip | NXP i.MX Message Unit as Zephyr MBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L628) | [`nxp,mbox-imx-mu`](../../../../build/dts/api/bindings/mbox/nxp%2Cmbox-imx-mu.md#std-dtcompatible-nxp-mbox-imx-mu) |
| Miscellaneous | on-chip | NXP i.MX RTxxx DSP control driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L53) | [`nxp,rtxxx-dsp-ctrl`](../../../../build/dts/api/bindings/misc/nxp%2Crtxxx-dsp-ctrl.md#std-dtcompatible-nxp-rtxxx-dsp-ctrl) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L33) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI MX25UM51345G[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L255) | [`nxp,imx-flexspi-mx25um51345g`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-mx25um51345g.md#std-dtcompatible-nxp-imx-flexspi-mx25um51345g) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L266) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | LPC I/O Pin Configuration (IOCON)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L148) | [`nxp,lpc-iocon`](../../../../build/dts/api/bindings/pinctrl/nxp%2Clpc-iocon.md#std-dtcompatible-nxp-lpc-iocon) |
| on-chip | RT600/RT500 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L151) | [`nxp,rt-iocon-pinctrl`](../../../../build/dts/api/bindings/pinctrl/nxp%2Crt-iocon-pinctrl.md#std-dtcompatible-nxp-rt-iocon-pinctrl) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L456) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Regulator | on-board | NXP PCA9420 PMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L226) | [`nxp,pca9420`](../../../../build/dts/api/bindings/regulator/nxp%2Cpca9420.md#std-dtcompatible-nxp-pca9420) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L163) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp%2Crstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L449) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L438) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| SDHC | on-chip | NXP imx USDHC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L482)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L494) | [`nxp,imx-usdhc`](../../../../build/dts/api/bindings/sdhc/nxp%2Cimx-usdhc.md#std-dtcompatible-nxp-imx-usdhc) |
| Sensors | on-board | FXOS8700 6-axis accelerometer/magnetometer sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/mimxrt685_evk/mimxrt685_evk_mimxrt685s_cm33.dts?plain=1#L163) | [`nxp,fxos8700`](../../../../build/dts/api/compatibles/nxp%2Cfxos8700.md#std-dtcompatible-nxp-fxos8700) |
| Serial controller | on-chip | LPC USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L243) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L128) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L288)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L338) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L92) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L431) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer) |
| on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| USB | on-chip | NXP LPCIP3511 USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L324) | [`nxp,lpcip3511`](../../../../build/dts/api/bindings/usb/nxp%2Clpcip3511.md#std-dtcompatible-nxp-lpcip3511) |
| on-chip | NXP USB High Speed PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L332) | [`nxp,usbphy`](../../../../build/dts/api/bindings/usb/nxp%2Cusbphy.md#std-dtcompatible-nxp-usbphy) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L466)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rt6xx_common.dtsi?plain=1#L474) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |

### Connections and IOs

The MIMXRT685 SoC has IOCON registers, which can be used to configure the
functionality of a pin.

| Name | Function | Usage |
| --- | --- | --- |
| PIO0\_2 | USART | USART RX |
| PIO0\_1 | USART | USART TX |
| PIO0\_14 | GPIO | GREEN LED |
| PIO1\_1 | GPIO | SW0 |
| PIO0\_17 | I2C | I2C SDA |
| PIO0\_18 | I2C | I2C SCL |
| PIO1\_5 | GPIO | FXOS8700 TRIGGER |
| PIO1\_5 | SPI | SPI MOSI |
| PIO1\_4 | SPI | SPI MISO |
| PIO1\_3 | SPI | SPI SCK |
| PIO1\_6 | SPI | SPI SSEL |
| PIO0\_23 | I2S | I2S DATAOUT |
| PIO0\_22 | I2S | I2S TX WS |
| PIO0\_21 | I2S | I2S TX SCK |
| PIO0\_9 | I2S | I2S DATAIN |
| PIO0\_29 | USART | USART TX |
| PIO0\_30 | USART | USART RX |
| PIO1\_11 | FLEXSPI0B\_DATA0 | OctalSPI Flash |
| PIO1\_12 | FLEXSPI0B\_DATA1 | OctalSPI Flash |
| PIO1\_13 | FLEXSPI0B\_DATA2 | OctalSPI Flash |
| PIO1\_14 | FLEXSPI0B\_DATA3 | OctalSPI Flash |
| PIO1\_29 | FLEXSPI0B\_SCLK | OctalSPI Flash |
| PIO2\_12 | PIO2\_12 | OctalSPI Flash |
| PIO2\_17 | FLEXSPI0B\_DATA4 | OctalSPI Flash |
| PIO2\_18 | FLEXSPI0B\_DATA5 | OctalSPI Flash |
| PIO2\_19 | FLEXSPI0B\_SS0\_N | OctalSPI Flash |
| PIO2\_22 | FLEXSPI0B\_DATA6 | OctalSPI Flash |
| PIO2\_23 | FLEXSPI0B\_DATA7 | OctalSPI Flash |
| PIO0\_27 | SCT0\_OUT7 | PWM |
| PIO1\_30 | SD0\_CLK | SD card |
| PIO1\_31 | SD0\_CMD | SD card |
| PIO2\_0 | SD0\_D0 | SD card |
| PIO2\_1 | SD0\_D1 | SD card |
| PIO2\_2 | SD0\_D2 | SD card |
| PIO2\_3 | SD0\_D3 | SD card |
| PIO2\_4 | SD0\_WR\_PRT | SD card |
| PIO2\_9 | SD0\_CD | SD card |
| PIO2\_10 | SD0\_RST | SD card |

### System Clock

The MIMXRT685 EVK is configured to use the OS Event timer
as a source for the system clock.

### Serial Port

The MIMXRT685 SoC has 8 FLEXCOMM interfaces for serial communication. One is
configured as USART for the console and the remaining are not used.

## Programming and Debugging

The `mimxrt685_evk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ (default) | ✅ (default) | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the LPC-Link2.

LinkServer CMSIS-DAPLPCLink2 JLink OnboardJLink External

1. Install the [LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) and make sure they are in your
   search path. LinkServer works with the default CMSIS-DAP firmware included in
   the on-board debugger.
2. Make sure the jumpers JP17, JP18 and JP19 are installed.

linkserver is the default runner for this board

```shell
west flash
west debug
```

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To connect the SWD signals to onboard debug circuit, install jumpers JP17, JP18 and JP19,
   if not already done (these jumpers are installed by default).
3. Follow the instructions in [LPC-Link2 J-Link Onboard Debug Probe](../../../../develop/flash_debug/probes.md#lpclink2-jlink-onboard-debug-probe) to program the
   J-Link firmware. Please make sure you have the latest firmware for this board.

```shell
west flash -r jlink
west debug -r jlink
```

1. Install the [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) and make sure they are in your search path.
2. To disconnect the SWD signals from onboard debug circuit, **remove** jumpers J17, J18,
   and J19 (these are installed by default).
3. Connect the J-Link probe to J2 10-pin header.

See [J-Link External Debug Probe](../../../../develop/flash_debug/probes.md#jlink-external-debug-probe) for more information.

```shell
west flash -r jlink
west debug -r jlink
```

### Configuring a Console

Connect a USB cable from your PC to J16, and use the serial terminal of your choice
(minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt685_evk/mimxrt685s/cm33 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v1.14.0 *****
Hello World! mimxrt685_evk
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[LinkServer Debug Host Tools](../../../../develop/flash_debug/host-tools.md#linkserver-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b mimxrt685_evk/mimxrt685s/cm33 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v2.3.0 *****
Hello World! mimxrt685_evk
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

1. Set the SW5 DIP switches to ON-ON-ON to prevent booting from flash.
2. Reset by pressing SW3
3. Run `west debug` or `west flash` again with a known working Zephyr
   application (example “Hello World”).
4. Set the SW5 DIP switches to ON-OFF-ON to boot from flash.
5. Reset by pressing SW3

### HiFi 4 DSP core

The Cadence HiFi 4 DSP core instantiated in the i.MX RT685 microcontroller is
supported and works with both the proprietary Xtensa toolchains (`xcc` in
earlier packages and `xt-lang` newer ones) and the
`xtensa-nxp_rt600_adsp_zephyr-elf` GCC variant distributed in the Zephyr SDK.

To build a project:

- Set up toolchain environment
  :   - No special configuration needed for the GCC variant in the Zephyr SDK.
      - For the proprietary Xtensa toolchain, set `XTENSA_CORE`,
        `XTENSA_TOOLCHAIN_PATH` and `TOOLCHAIN_VER` according to your
        installed version. `ZEPHYR_TOOLCHAIN_VARIANT` should be either `xcc`
        or `xt-clang`.
- Build the project with:

```shell
# From the root of the zephyr repository
west build -b mimxrt685_evk/mimxrt685s/hifi4 samples/hello_world
```

Debugging can be directly carried out using the J-Link GDB server with
`xt-gdb` (Xtensa proprietary) or `gdb` (Zephyr SDK) connected. It’s
also possible to debug the HiFi 4 DSP in tandem with the CM33 core using the
`xt-ocd` daemon. See [RT600 Dual-Core Communication and Debugging](https://www.nxp.com/docs/en/application-note/AN12789.pdf)
for details.

As the HiFi 4 DSP is positioned as a secondary core, explicit initialisation
must be done in order for it to be functional. The `nxp_rtxxx_adsp_ctrl`,
instantiated in the RT685’s CM33 domain, takes care of this. Power domains
and clocks are set up upon it initialising. This is sufficient for
attaching a debugger to the core. For the use in an AMP system, this driver
handles code loading and run control.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)
