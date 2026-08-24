---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/nxp/frdm_rw612/doc/index.html
original_path: boards/nxp/frdm_rw612/doc/index.html
---

# FRDM\_RW612

Board Overview

[![../../../../_images/frdm_rw612.webp](https://docs.zephyrproject.org/4.2.0/_images/frdm_rw612.webp)
](https://docs.zephyrproject.org/4.2.0/_images/frdm_rw612.webp)

FRDM\_RW612

Name:
:   `frdm_rw612`

Vendor:
:   NXP Semiconductors

Architecture:
:   arm

SoC:
:   rw612

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/nxp/frdm_rw612/doc/index.rst/../..)

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

The `frdm_rw612` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `frdm_rw612/rw612` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L28) | [`arm,cortex-m33f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33f.md#std-dtcompatible-arm-cortex-m33f) |
| ADC | on-chip | NXP GAU GPADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L550)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L559) | [`nxp,gau-adc`](../../../../build/dts/api/bindings/adc/nxp,gau-adc.md#std-dtcompatible-nxp-gau-adc) |
| ARM architecture | on-chip | LPC Flexcomm node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L300) | [`nxp,lpc-flexcomm`](../../../../build/dts/api/bindings/arm/nxp,lpc-flexcomm.md#std-dtcompatible-nxp-lpc-flexcomm) |
| on-chip | RW SOC controller node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L313) | [`nxp,rw-soc-ctrl`](../../../../build/dts/api/bindings/arm/nxp,rw-soc-ctrl.md#std-dtcompatible-nxp-rw-soc-ctrl) |
| on-chip | NXP NBU interruption information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L585) | [`nxp,nbu`](../../../../build/dts/api/bindings/arm/nxp,nbu.md#std-dtcompatible-nxp-nbu) |
| Audio | on-chip | NXP DMIC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L510) | [`nxp,dmic`](../../../../build/dts/api/bindings/audio/nxp,dmic.md#std-dtcompatible-nxp-dmic) |
| Bluetooth | on-chip | NXP BLE HCI information[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L591) | [`nxp,hci-ble`](../../../../build/dts/api/bindings/bluetooth/nxp,hci-ble.md#std-dtcompatible-nxp-hci-ble) |
| Clock control | on-chip | LPC SYSCON & CLKCTL IP node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L145) | [`nxp,lpc-syscon`](../../../../build/dts/api/bindings/clock/nxp,lpc-syscon.md#std-dtcompatible-nxp-lpc-syscon) |
| Counter | on-chip | Driver that uses the NXP LPC RTC High resolution counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L373) | [`nxp,lpc-rtc-highres`](../../../../build/dts/api/bindings/counter/nxp,lpc-rtc-highres.md#std-dtcompatible-nxp-lpc-rtc-highres) |
| on-chip | NXP MCUX Standard Timer/Counter[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L379)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L392) | [`nxp,lpc-ctimer`](../../../../build/dts/api/bindings/counter/nxp,lpc-ctimer.md#std-dtcompatible-nxp-lpc-ctimer) |
| on-chip | NXP Multirate Timer[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L442) | [`nxp,mrt`](../../../../build/dts/api/bindings/counter/nxp,mrt.md#std-dtcompatible-nxp-mrt) |
| on-chip | NXP Multirate Timer Channel[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L454)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L459) | [`nxp,mrt-channel`](../../../../build/dts/api/bindings/counter/nxp,mrt-channel.md#std-dtcompatible-nxp-mrt-channel) |
| DAC | on-chip | NXP GAU DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L568) | [`nxp,gau-dac`](../../../../build/dts/api/bindings/dac/nxp,gau-dac.md#std-dtcompatible-nxp-gau-dac) |
| DMA | on-chip | NXP LPC DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L345) | [`nxp,lpc-dma`](../../../../build/dts/api/bindings/dma/nxp,lpc-dma.md#std-dtcompatible-nxp-lpc-dma) |
| Ethernet | on-chip | NXP ENET IP Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L603) | [`nxp,enet`](../../../../build/dts/api/bindings/ethernet/nxp,enet.md#std-dtcompatible-nxp-enet) |
| on-chip | NXP ENET MAC/L2 Device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L607) | [`nxp,enet-mac`](../../../../build/dts/api/bindings/ethernet/nxp,enet-mac.md#std-dtcompatible-nxp-enet-mac) |
| on-board | Microchip KSZ8081 Ethernet PHY device[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L175) | [`microchip,ksz8081`](../../../../build/dts/api/bindings/ethernet/phy/microchip,ksz8081.md#std-dtcompatible-microchip-ksz8081) |
| on-chip | NXP ENET PTP (Precision Time Protocol) Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L623) | [`nxp,enet-ptp-clock`](../../../../build/dts/api/bindings/ethernet/nxp,enet-ptp-clock.md#std-dtcompatible-nxp-enet-ptp-clock) |
| GPIO & Headers | on-chip | LPC GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L209) | [`nxp,lpc-gpio`](../../../../build/dts/api/bindings/gpio/nxp,lpc-gpio.md#std-dtcompatible-nxp-lpc-gpio) |
| on-chip | LPC GPIO port device[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L215) | [`nxp,lpc-gpio-port`](../../../../build/dts/api/bindings/gpio/nxp,lpc-gpio-port.md#std-dtcompatible-nxp-lpc-gpio-port) |
| on-board | GPIO pins exposed on NXP LCD pmod interface (e.g., used on LCD-PAR-035 panel)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L50) | [`nxp,lcd-pmod`](../../../../build/dts/api/bindings/gpio/nxp,lcd-pmod.md#std-dtcompatible-nxp-lcd-pmod) |
| IEEE 802.15.4 HDLC RCP interface | on-chip | NXP HDLC RCP interface node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L596) | [`nxp,hdlc-rcp-if`](../../../../build/dts/api/bindings/hdlc_rcp_if/nxp,hdlc-rcp-if.md#std-dtcompatible-nxp-hdlc-rcp-if) |
| I2C | on-chip | LPC I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L272) | [`nxp,lpc-i2c`](../../../../build/dts/api/bindings/i2c/nxp,lpc-i2c.md#std-dtcompatible-nxp-lpc-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | NXP Pin interrupt and pattern match engine (PINT)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L325) | [`nxp,pint`](../../../../build/dts/api/bindings/interrupt-controller/nxp,pint.md#std-dtcompatible-nxp-pint) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L33) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | NXP ENET MDIO Features[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L616) | [`nxp,enet-mdio`](../../../../build/dts/api/bindings/mdio/nxp,enet-mdio.md#std-dtcompatible-nxp-enet-mdio) |
| MIPI-DBI | on-chip | NXP LCDIC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L355) | [`nxp,lcdic`](../../../../build/dts/api/bindings/mipi-dbi/nxp,lcdic.md#std-dtcompatible-nxp-lcdic) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L35) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-board | NXP FlexSPI NOR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L99) | [`nxp,imx-flexspi-nor`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-nor.md#std-dtcompatible-nxp-imx-flexspi-nor) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L109) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-board | AP Memory APS6404L pSRAM on NXP FlexSPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L136) | [`nxp,imx-flexspi-aps6404l`](../../../../build/dts/api/bindings/mtd/nxp,imx-flexspi-aps6404l.md#std-dtcompatible-nxp-imx-flexspi-aps6404l) |
| Pin control | on-chip | MCI IO MUX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L152) | [`nxp,mci-io-mux`](../../../../build/dts/api/bindings/pinctrl/nxp,mci-io-mux.md#std-dtcompatible-nxp-mci-io-mux) |
| Power management | on-chip | NXP RW PMU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L177) | [`nxp,rw-pmu`](../../../../build/dts/api/bindings/power/nxp,rw-pmu.md#std-dtcompatible-nxp-rw-pmu) |
| on-chip | Some NXP SoC’s have pins dedicated to generate a wakeup interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L180) | [`nxp,aon-wakeup-pin`](../../../../build/dts/api/bindings/power/nxp,aon-wakeup-pin.md#std-dtcompatible-nxp-aon-wakeup-pin) |
| on-chip | Properties for NXP power management through the PDCFG register[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L50)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L62) | [`nxp,pdcfg-power`](../../../../build/dts/api/bindings/power/nxp,pdcfg-power.md#std-dtcompatible-nxp-pdcfg-power) |
| Power domain | on-chip | This power domain will Turn On and Off devices when transitioning in and out a specified Power State[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L86) | [`power-domain-soc-state-change`](../../../../build/dts/api/bindings/power-domain/power-domain-soc-state-change.md#std-dtcompatible-power-domain-soc-state-change) |
| PWM | on-chip | NXP SCTimer PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L431) | [`nxp,sctimer-pwm`](../../../../build/dts/api/bindings/pwm/nxp,sctimer-pwm.md#std-dtcompatible-nxp-sctimer-pwm) |
| Reset controller | on-chip | NXP RSTCTL Peripheral reset controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L165) | [`nxp,rstctl`](../../../../build/dts/api/bindings/reset/nxp,rstctl.md#std-dtcompatible-nxp-rstctl) |
| RNG | on-chip | Kinetis TRNG (True Random Number Generator)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L192) | [`nxp,kinetis-trng`](../../../../build/dts/api/bindings/rng/nxp,kinetis-trng.md#std-dtcompatible-nxp-kinetis-trng) |
| RTC | on-chip | NXP LPC RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L368) | [`nxp,lpc-rtc`](../../../../build/dts/api/bindings/rtc/nxp,lpc-rtc.md#std-dtcompatible-nxp-lpc-rtc) |
| Sensors | on-board | NXP P3T1755 digital temperature sensor connected to I3C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/nxp/frdm_rw612/frdm_rw612_common.dtsi?plain=1#L276) | [`nxp,p3t1755`](../../../../build/dts/api/compatibles/nxp,p3t1755.md#std-dtcompatible-nxp-p3t1755) |
| Serial controller | on-chip | LPC USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L286)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L244) | [`nxp,lpc-usart`](../../../../build/dts/api/bindings/serial/nxp,lpc-usart.md#std-dtcompatible-nxp-lpc-usart) |
| SPI | on-chip | NXP FlexSPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L141) | [`nxp,imx-flexspi`](../../../../build/dts/api/bindings/spi/nxp,imx-flexspi.md#std-dtcompatible-nxp-imx-flexspi) |
| on-chip | NXP LPC SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L258) | [`nxp,lpc-spi`](../../../../build/dts/api/bindings/spi/nxp,lpc-spi.md#std-dtcompatible-nxp-lpc-spi) |
| SRAM | on-chip | Generic on-chip SRAM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L102) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | NXP OS Timer on i.MX-RT5xx/6xx[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L578) | [`nxp,os-timer`](../../../../build/dts/api/bindings/timer/nxp,os-timer.md#std-dtcompatible-nxp-os-timer) |
| USB | on-chip | NXP EHCI USB device mode[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L234) | [`nxp,ehci`](../../../../build/dts/api/bindings/usb/nxp,ehci.md#std-dtcompatible-nxp-ehci) |
| Watchdog | on-chip | LPC Windowed Watchdog Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L200) | [`nxp,lpc-wwdt`](../../../../build/dts/api/bindings/watchdog/nxp,lpc-wwdt.md#std-dtcompatible-nxp-lpc-wwdt) |
| Wi-Fi | on-chip | NXP Wi-Fi Module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/nxp/nxp_rw6xx_common.dtsi?plain=1#L338) | [`nxp,wifi`](../../../../build/dts/api/bindings/wifi/nxp,wifi.md#std-dtcompatible-nxp-wifi) |

Note

Power modes 1, 2 and 3 are supported when using System Power Management.

## Programming and Debugging

The `frdm_rw612` board supports the runners and associated west commands listed below.

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

Connect a USB cable from your PC to J10, and use the serial terminal of your choice
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
west build -b frdm_rw612 samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the RESET button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v3.6.0 *****
Hello World! frdm_rw612
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application. This example uses the
[J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools) as default.

```shell
# From the root of the zephyr repository
west build -b frdm_rw612 samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
***** Booting Zephyr OS zephyr-v3.6.0 *****
Hello World! frdm_rw612
```

## SRAM Bus Access Partitioning

RW612 supports shared access of the SRAM from both the code bus and data bus.
The bus used to access the SRAM is determined using two separate memory mapped address spaces.
The application can configure the partitioning of the SRAM access regions by a devicetree overlay.
For example, below is part of an overlay to change the whole SRAM to be used for data.

```devicetree
&sram_data {
     reg = <0x0 DT_SIZE_K(1216)>;
};
```

## Wireless Connectivity Support

### Fetch Binary Blobs

To support Bluetooth or Wi-Fi, frdm\_rw612 requires fetching binary blobs, which can be
achieved by running the following command:

```shell
west blobs fetch hal_nxp
```

### Bluetooth

BLE functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

frdm\_rw612 platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_ble_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

### Wi-Fi

Wi-Fi functionality requires to fetch binary blobs, so make sure to follow
the `Fetch Binary Blobs` section first.

frdm\_rw612 platform supports the monolithic feature. The required binary blob
`<zephyr workspace>/modules/hal/nxp/zephyr/blobs/rw61x_sb_wifi_a2.bin` will be linked
with the application image directly, forming one single monolithic image.

### RTC Sub-Second Counter

To use the RTC sub-second counter which is clocked at a 32kHZ rate, make the
following modifications to the board hardware:

1. Move the short on SJ21 from 1 and 2 to short 2 and 3.
2. Move the short on SJ22 from 1 and 2 to short 2 and 3.

After this change, the ENET will stop functioning on the board.

### Support Resources for Zephyr

- [NXP Zephyr Downstream Software Development Kit](https://github.com/nxp-zephyr/nxp-zsdk)
- [MCUXpresso for VS Code](https://www.nxp.com/design/design-center/software/embedded-software/mcuxpresso-for-visual-studio-code:MCUXPRESSO-VSC?tid=vanMCUXPRESSO-VSC), [wiki](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki) documentation and [Zephyr lab guides](https://github.com/nxp-mcuxpresso/vscode-for-mcux/wiki/Training-Zephyr-Getting-Started)
- [NXP Zephyr Knowledge Hub](https://community.nxp.com/t5/Zephyr-Project-Knowledge-Base/Zephyr-Knowledge-Hub/ta-p/2008548)
- [NXP’s Zephyr landing page](https://nxp.com/zephyr) (including training resources)
- [NXP Support Community forum for Zephyr](https://community.nxp.com/t5/Zephyr-Project/bd-p/Zephyr-Project)

## Resources
