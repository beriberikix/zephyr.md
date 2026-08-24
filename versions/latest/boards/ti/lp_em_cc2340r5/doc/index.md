---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ti/lp_em_cc2340r5/doc/index.html
original_path: boards/ti/lp_em_cc2340r5/doc/index.html
---

# CC2340R5 LaunchPad

Board Overview

[![../../../../_images/lp_em_cc2340r5.webp](https://docs.zephyrproject.org/4.2.0/_images/lp_em_cc2340r5.webp)
](https://docs.zephyrproject.org/4.2.0/_images/lp_em_cc2340r5.webp)

CC2340R5 LaunchPad

Name:
:   `lp_em_cc2340r5`

Vendor:
:   Texas Instruments

Architecture:
:   arm

SoC:
:   cc2340r5

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ti/lp_em_cc2340r5/doc/index.rst/../..)

## Overview

The Texas Instruments CC2340R5 LaunchPad™ (LP\_EM\_CC2340R5) is a
development kit for the SimpleLink™ multi-Standard CC2340R5 wireless MCU.

See the [TI CC2340R5 LaunchPad Product Page](https://www.ti.com/tool/LP-EM-CC2340R5) for details.

## Hardware

The CC2340R5 LaunchPad™ development kit features the CC2340R5 wireless MCU.
The board is equipped with two LEDs, two push buttons and BoosterPack connectors
for expansion.

The CC2340R5 wireless MCU has a 48 MHz Arm® Cortex®-M0+ SoC and an
integrated 2.4 GHz transceiver supporting multiple protocols including Bluetooth® Low Energy and IEEE® 802.15.4.

See the [TI CC2340R5 Product Page](https://www.ti.com/product/CC2340R5) for additional details.

### Supported Features

The `lp_em_cc2340r5` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `lp_em_cc2340r5/cc2340r5` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L20) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | TI CC23X0 16-channel ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L162) | [`ti,cc23x0-adc`](../../../../build/dts/api/bindings/adc/ti%2Ccc23x0-adc.md#std-dtcompatible-ti-cc23x0-adc) |
| Clock control | on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L32) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | CC23x0 RTC counter driver Any reset/sleep mode, except for the power-up reset, will not stop or reset the RTC Timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L119) | [`ti,cc23x0-rtc`](../../../../build/dts/api/bindings/counter/ti%2Ccc23x0-rtc.md#std-dtcompatible-ti-cc23x0-rtc) |
| on-chip | CC23x0 LGPT counter driver[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L126) | [`ti,cc23x0-lgpt`](../../../../build/dts/api/bindings/counter/ti%2Ccc23x0-lgpt.md#std-dtcompatible-ti-cc23x0-lgpt) |
| Cryptographic accelerator | on-chip | TI CC23X0 AES accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L85) | [`ti,cc23x0-aes`](../../../../build/dts/api/bindings/crypto/ti%2Ccc23x0-aes.md#std-dtcompatible-ti-cc23x0-aes) |
| DMA | on-chip | TI CC23X0 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L94) | [`ti,cc23x0-dma`](../../../../build/dts/api/bindings/dma/ti%2Ccc23x0-dma.md#std-dtcompatible-ti-cc23x0-dma) |
| Flash controller | on-chip | Texas Instruments CC23X0 flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L39) | [`ti,cc23x0-flash-controller`](../../../../build/dts/api/bindings/flash_controller/ti%2Ccc23x0-flash-controller.md#std-dtcompatible-ti-cc23x0-flash-controller) |
| GPIO & Headers | on-chip | TI SimpleLink CC23X0 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L65) | [`ti,cc23x0-gpio`](../../../../build/dts/api/bindings/gpio/ti%2Ccc23x0-gpio.md#std-dtcompatible-ti-cc23x0-gpio) |
| on-board | TI BoosterPack GPIO header[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/lp_em_cc2340r5/boosterpack_connector.dtsi?plain=1#L9) | [`ti,boosterpack-header`](../../../../build/dts/api/bindings/gpio/ti%2Cboosterpack-header.md#std-dtcompatible-ti-boosterpack-header) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/lp_em_cc2340r5/lp_em_cc2340r5.dts?plain=1#L50) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ti/lp_em_cc2340r5/lp_em_cc2340r5.dts?plain=1#L36) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L46) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-chip | This binding describes the TI CC23X0 flash CCFG (custom configuration) area content[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L53) | [`ti,cc23x0-ccfg-flash`](../../../../build/dts/api/bindings/mtd/ti%2Ccc23x0-ccfg-flash.md#std-dtcompatible-ti-cc23x0-ccfg-flash) |
| on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc2340r5.dtsi?plain=1#L48) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | TI SimpleLink CC23X0 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L60) | [`ti,cc23x0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ti%2Ccc23x0-pinctrl.md#std-dtcompatible-ti-cc23x0-pinctrl) |
| Serial controller | on-chip | TI SimpleLink CC23X0 UART node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L75) | [`ti,cc23x0-uart`](../../../../build/dts/api/bindings/serial/ti%2Ccc23x0-uart.md#std-dtcompatible-ti-cc23x0-uart) |
| SPI | on-chip | TI SimpleLink CC23x0 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L102) | [`ti,cc23x0-spi`](../../../../build/dts/api/bindings/spi/ti%2Ccc23x0-spi.md#std-dtcompatible-ti-cc23x0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| Watchdog | on-chip | TI CC23x0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ti/cc23x0.dtsi?plain=1#L113) | [`ti,cc23x0-wdt`](../../../../build/dts/api/bindings/watchdog/ti%2Ccc23x0-watchdog.md#std-dtcompatible-ti-cc23x0-wdt) |

### Connections and IOs

All I/O signals are accessible from the BoosterPack connectors. Pin function
aligns with the LaunchPad standard.

| Pin | Function | Usage |
| --- | --- | --- |
| DIO0 | GPIO |  |
| DIO1 | ANALOG\_IO | A4 |
| DIO2 | ANALOG\_IO | A3 |
| DIO5 | ANALOG\_IO | A5 |
| DIO6 | SPI\_CSN | SPI CS |
| DIO7 | ANALOG\_IO | A0 |
| DIO8 | GPIO |  |
| DIO9 | GPIO | Button 2 |
| DIO10 | GPIO | Button 1 |
| DIO11 | SPI\_CSN | SPI CS |
| DIO12 | SPI\_POCI | SPI POCI |
| DIO13 | SPI\_PICO | SPI\_PICO |
| DIO14 | GPIO | Red LED |
| DIO15 | GPIO | Green LED |
| DIO18 | SPI\_CLK | SPI CLK |
| DIO19 | GPIO |  |
| DIO20 | UART0\_TX | UART TX |
| DIO21 | GPIO |  |
| DIO22 | UART0\_RX | UART RX |
| DIO23 | ANALOG\_IO | A8 |
| DIO24 | ANALOG\_IO | A7 |

## Programming and Debugging

The `lp_em_cc2340r5` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

The LP\_EM\_CC2340R5 requires an external debug probe such as the LP-XDS110 or
LP-XDS110ET.

Currently there is no debug support in Zephyr for the LP\_EM\_CC2340R5, and the
built binaries for this target must be flashed/debugged using either Uniflash
or Code Composer Studio.

## References

CC2340R5 LaunchPad Quick Start Guide:
:   [https://www.ti.com/lit/pdf/swru588](https://www.ti.com/lit/pdf/swru588)
