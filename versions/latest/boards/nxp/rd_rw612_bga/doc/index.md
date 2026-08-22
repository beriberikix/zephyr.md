---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/rd_rw612_bga/doc/index.html
original_path: boards/nxp/rd_rw612_bga/doc/index.html
---

# RD-RW612-BGA

Board Overview

Name:
:   `rd_rw612_bga`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   rw612

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/rd_rw612_bga/doc/index.rst/../..)

## Overview

The RW612 is a highly integrated, low-power tri-radio wireless MCU with an
integrated 260 MHz ARM Cortex-M33 MCU and Wi-Fi 6 + Bluetooth Low Energy (LE) 5.3 / 802.15.4
radios designed for a broad array of applications, including connected smart home devices,
gaming controllers, enterprise and industrial automation, smart accessories and smart energy.

The RW612 MCU subsystem includes 1.2 MB of on-chip SRAM and a high-bandwidth Quad SPI interface
with an on-the-fly decryption engine for securely accessing off-chip XIP flash.

The advanced design of the RW612 delivers tight integration, low power and highly secure
operation in a space- and cost-efficient wireless MCU requiring only a single 3.3 V power supply.

## Hardware

- 260 MHz ARM Cortex-M33, tri-radio cores for Wifi 6 + BLE 5.3 + 802.15.4
- 1.2 MB on-chip SRAM

### Supported Features

The `rd_rw612_bga` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rd_rw612_bga/rw612` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | NXP GAU GPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L550)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L559) | [`nxp,gau-adc`](../../../../build/dts/api/bindings/adc/nxp%2Cgau-adc.md#std-dtcompatible-nxp-gau-adc) |
| ARM architecture | on-chip | LPC Flexcomm node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L258) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| on-chip | RW SOC controller node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L313) | [`nxp,rw-soc-ctrl`](../../../../build/dts/api/bindings/arm/nxp%2Crw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl) |
| on-chip | NXP NBU interruption information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L585) | [`nxp,nbu`](../../../../build/dts/api/bindings/arm/nxp%2Cnbu.md#std-dtcompatible-nxp-nbu) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L510) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp%2Cdmic.md#std-dtcompatible-nxp-dmic) |
| Bluetooth | on-chip | NXP BLE HCI information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L591) | [`nxp,hci-ble`](../../../../build/dts/api/bindings/bluetooth/nxp%2Chci-ble.md#std-dtcompatible-nxp-hci-ble) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L145) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L373) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L379)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L392) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L442) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L454)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L459) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP GAU DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L568) | [`nxp,gau-dac`](../../../../build/dts/api/bindings/dac/nxp%2Cgau-dac.md#std-dtcompatible-nxp-gau-dac) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L345) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L603) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L607) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L623) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L209) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L215) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L44) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L79) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp%2Clcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| IEEE 802.15.4 HDLC RCP interface | on-chip | NXP HDLC RCP interface node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L596) | [`nxp,hdlc-rcp-if`](../../../../build/dts/api/bindings/hdlc_rcp_if/nxp%2Chdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if) |
| I2C | on-chip | LPC I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L272) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L35) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L325) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L616) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MIPI-DBI | on-chip | NXP LCDIC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L355) | [`nxp,lcdic`](../../../../build/dts/api/bindings/mipi-dbi/nxp%2Clcdic.md#std-dtcompatible-nxp-lcdic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L35) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L136) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L147) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | ISSI IS66WVQ8M4 pSRAM on NXP FlexSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L174) | [`nxp,imx-flexspi-is66wvq8m4`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-is66wvq8m4.md#std-dtcompatible-nxp-imx-flexspi-is66wvq8m4) |
| Pin control | on-chip | MCI IO MUX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L152) | [`nxp,mci-io-mux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmci-io-mux.md#std-dtcompatible-nxp-mci-io-mux) |
| Power management | on-chip | NXP RW PMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L177) | [`nxp,rw-pmu`](../../../../build/dts/api/bindings/power/nxp%2Crw-pmu.md#std-dtcompatible-nxp-rw-pmu) |
| on-chip | Some NXP SoC’s have pins dedicated to generate a wakeup interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L185)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L180) | [`nxp,aon-wakeup-pin`](../../../../build/dts/api/bindings/power/nxp%2Caon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin) |
| on-chip | Properties for NXP power management through the PDCFG register[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L50)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L62) | [`nxp,pdcfg-power`](../../../../build/dts/api/bindings/power/nxp%2Cpdcfg-power.md#std-dtcompatible-nxp-pdcfg-power) |
| Power domain | on-chip | This power domain will Turn On and Off devices when transitioning in and out a specified Power State[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L86) | [`power-domain-soc-state-change`](../../../../build/dts/api/bindings/power-domain/power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L431) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L165) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp%2Crstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L192) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L368) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L286) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L141) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L244) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L102) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L578) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L234) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L200) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |
| Wi-Fi | on-chip | NXP Wi-Fi Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L338) | [`nxp,wifi`](../../../../build/dts/api/bindings/wifi/nxp%2Cwifi.md#std-dtcompatible-nxp-wifi) |

#### `rd_rw612_bga/rw612/ethernet` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | NXP GAU GPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L550)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L559) | [`nxp,gau-adc`](../../../../build/dts/api/bindings/adc/nxp%2Cgau-adc.md#std-dtcompatible-nxp-gau-adc) |
| ARM architecture | on-chip | LPC Flexcomm node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L258) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp%2Clpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| on-chip | RW SOC controller node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L313) | [`nxp,rw-soc-ctrl`](../../../../build/dts/api/bindings/arm/nxp%2Crw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl) |
| on-chip | NXP NBU interruption information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L585) | [`nxp,nbu`](../../../../build/dts/api/bindings/arm/nxp%2Cnbu.md#std-dtcompatible-nxp-nbu) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L510) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp%2Cdmic.md#std-dtcompatible-nxp-dmic) |
| Bluetooth | on-chip | NXP BLE HCI information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L591) | [`nxp,hci-ble`](../../../../build/dts/api/bindings/bluetooth/nxp%2Chci-ble.md#std-dtcompatible-nxp-hci-ble) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L145) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp%2Clpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L373) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L379)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L392) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp%2Clpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L442) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L454)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L459) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp%2Cmrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP GAU DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L568) | [`nxp,gau-dac`](../../../../build/dts/api/bindings/dac/nxp%2Cgau-dac.md#std-dtcompatible-nxp-gau-dac) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L345) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp%2Clpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L603) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L607) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga_rw612_ethernet.dts?plain=1#L31) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip%2Cksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L623) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp%2Cenet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L209) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L215) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp%2Clpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L44) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on NXP LCD 8080 interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L79) | [`nxp,lcd-8080`](../../../../build/dts/api/bindings/gpio/nxp%2Clcd-8080.md#std-dtcompatible-nxp-lcd-8080) |
| IEEE 802.15.4 HDLC RCP interface | on-chip | NXP HDLC RCP interface node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L596) | [`nxp,hdlc-rcp-if`](../../../../build/dts/api/bindings/hdlc_rcp_if/nxp%2Chdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if) |
| I2C | on-chip | LPC I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L272) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp%2Clpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L35) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L325) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp%2Cpint.md#std-dtcompatible-nxp-pint) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L616) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp%2Cenet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MIPI-DBI | on-chip | NXP LCDIC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L355) | [`nxp,lcdic`](../../../../build/dts/api/bindings/mipi-dbi/nxp%2Clcdic.md#std-dtcompatible-nxp-lcdic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L35) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L136) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L147) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | ISSI IS66WVQ8M4 pSRAM on NXP FlexSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/rd_rw612_bga.dtsi?plain=1#L174) | [`nxp,imx-flexspi-is66wvq8m4`](../../../../build/dts/api/bindings/mtd/nxp%2Cimx-flexspi-is66wvq8m4.md#std-dtcompatible-nxp-imx-flexspi-is66wvq8m4) |
| Pin control | on-chip | MCI IO MUX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L152) | [`nxp,mci-io-mux`](../../../../build/dts/api/bindings/pinctrl/nxp%2Cmci-io-mux.md#std-dtcompatible-nxp-mci-io-mux) |
| Power management | on-chip | NXP RW PMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L177) | [`nxp,rw-pmu`](../../../../build/dts/api/bindings/power/nxp%2Crw-pmu.md#std-dtcompatible-nxp-rw-pmu) |
| on-chip | Some NXP SoC’s have pins dedicated to generate a wakeup interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L185)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L180) | [`nxp,aon-wakeup-pin`](../../../../build/dts/api/bindings/power/nxp%2Caon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin) |
| on-chip | Properties for NXP power management through the PDCFG register[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L50)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L62) | [`nxp,pdcfg-power`](../../../../build/dts/api/bindings/power/nxp%2Cpdcfg-power.md#std-dtcompatible-nxp-pdcfg-power) |
| Power domain | on-chip | This power domain will Turn On and Off devices when transitioning in and out a specified Power State[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L86) | [`power-domain-soc-state-change`](../../../../build/dts/api/bindings/power-domain/power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L431) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp%2Csctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L165) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp%2Crstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L192) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp%2Ckinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L368) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp%2Clpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L286) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp%2Clpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L141) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp%2Cimx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L244) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp%2Clpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L102) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L578) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp%2Cos-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L234) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp%2Cehci.md#std-dtcompatible-nxp-ehci) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L200) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp%2Clpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |
| Wi-Fi | on-chip | NXP Wi-Fi Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L338) | [`nxp,wifi`](../../../../build/dts/api/bindings/wifi/nxp%2Cwifi.md#std-dtcompatible-nxp-wifi) |

Note

Power modes 1, 2 and 3 are supported when using System Power Management.

## Display Support

The rd\_rw612\_bga board supports several in-tree display modules. Setup for
each module is described below:

### GoWorld 16880 LCM

This module does not connect directly to the board, and must be connected
via an adapter board and jumper wires. Connections are described in
[boards/nxp/rd\_rw612\_bga/dts/goworld\_16880\_lcm.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/rd_rw612_bga/dts/goworld_16880_lcm.overlay). The
display sample can be built for this board like so:

```shell
west build -b rd_rw612_bga samples/drivers/display -- -DDTC_OVERLAY_FILE=goworld_16880_lcm.overlay
```

### Adafruit 2.8 TFT

The [Adafruit 2.8” TFT Touch Shield v2](../../../shields/adafruit_2_8_tft_touch_v2/doc/index.md#adafruit-2-8-tft-touch-v2) connects to the board’s Arduino headers
directly, but some modifications are required (see
[boards/shields/adafruit\_2\_8\_tft\_touch\_v2/boards/rd\_rw612\_bga.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/adafruit_2_8_tft_touch_v2/boards/rd_rw612_bga.overlay)
for a list). The display sample can be built for this module like so:

```shell
west build -b rd_rw612_bga --shield adafruit_2_8_tft_touch_v2 samples/drivers/display
```

### NXP LCD\_PAR\_S035

The [NXP LCD\_PAR\_S035 TFT LCD Module](../../../shields/lcd_par_s035/doc/index.md#lcd-par-s035) does not connect directly to the board, and must be
connected via jumper wires. Connections and required board changes are
described in
[boards/shields/lcd\_par\_s035/boards/rd\_rw612\_bga.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/lcd_par_s035/boards/rd_rw612_bga.overlay). The
display sample can be built for the module like so:

```shell
west build -b rd_rw612_bga --shield lcd_par_s035_8080 samples/drivers/display
```

## Fetch Binary Blobs

To support Bluetooth or Wi-Fi, rd\_rw612\_bga requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

## Programming and Debugging

The `rd_rw612_bga` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **debugserver** | **rtt** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |
| **[linkserver](../../../../develop/flash_debug/host-tools.md#runner-linkserver)** | ✅ | ✅ | ✅ | ✅ |  |

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Debug Probe

A debug probe is used for both flashing and debugging the board. This board is
configured by default to use the JLink Firmware.

### Configuring a Console

Connect a USB cable from your PC to J7, and use the serial terminal of your choice
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
west build -b rd_rw612_bga samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.4.0 *****
Hello World! rd_rw612_bga
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b rd_rw612_bga samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v3.6.0 *****
Hello World! rd_rw612_bga
```

## Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

rd\_rw612\_bga platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_ble_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

## Wi-Fi

Wi-Fi functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

rd\_rw612\_bga platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_wifi_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

## Board variants

### Ethernet

To use ethernet on the RD\_RW612\_BGA board, you first need to make the following
modifications to the board hardware:

Add resistors:

- R485
- R486
- R487
- R488
- R489
- R491
- R490

Remove resistors:

- R522
- R521
- R520
- R524
- R523
- R508
- R505

Then, build for the board target `rd_rw612_bga//ethernet`.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk) [[1]](#id1)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC) [[2]](#id3), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) [[3]](#id5) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started) [[4]](#id7)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548) [[5]](#id9)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) [[6]](#id11) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project) [[7]](#id13)

## Resources

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
