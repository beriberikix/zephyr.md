---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/microchip/ev11l78a/doc/index.html
original_path: boards/microchip/ev11l78a/doc/index.html
---

# UPD301C Basic Sink Application Example

Board Overview

[![../../../../_images/ev11l78a.jpg](../../../../_images/ev11l78a.jpg)
](../../../../_images/ev11l78a.jpg)

UPD301C Basic Sink Application Example

Name:
:   `ev11l78a`

Vendor:
:   Microchip Technology Inc.

Architecture:
:   arm

SoC:
:   samd20e16

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/microchip/ev11l78a/doc/index.rst/../..)

## Overview

The UPD301C Basic Sink Application Example Evaluation Kit (EV11L78A)
is a low-cost evaluation platform for Microchip’s UPD301C Standalone
Programmable USB Power Delivery (PD) Controller. This RoHS-compliant
evaluation platform comes in a small form factor and adheres to the
USB Type-C™ Connector Specification and USB PD 3.0 specification.

## Hardware

- ATSAMD20E16 ARM Cortex-M0+ processor at 48 MHz
- UPD301C combines a SAMD20 core and a UPD350 USB-PD controller
- Sink PDO Selector Switch
- Onboard LED Voltmeter

### Supported Features

The `ev11l78a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ev11l78a/samd20e16` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L44) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | Atmel SAM0 family ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L202) | [`atmel,sam0-adc`](../../../../build/dts/api/bindings/adc/atmel%2Csam0-adc.md#std-dtcompatible-atmel-sam0-adc) |
| ARM architecture | on-chip | Atmel SAM0 multi-protocol (UART, SPI, I2C) SERCOM unit[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L132) | [`atmel,sam0-sercom`](../../../../build/dts/api/bindings/arm/atmel%2Csam0-sercom.md#std-dtcompatible-atmel-sam0-sercom) |
| on-chip | For locating the Device ID (serial number) on Atmel SAM0 devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L56) | [`atmel,sam0-id`](../../../../build/dts/api/bindings/arm/atmel%2Csam0-id.md#std-dtcompatible-atmel-sam0-id) |
| Clock control | on-chip | Atmel SAM0 Main Clock Controller (MCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L82) | [`atmel,sam0-mclk`](../../../../build/dts/api/bindings/clock/atmel%2Csam0-mclk.md#std-dtcompatible-atmel-sam0-mclk) |
| on-chip | Atmel SAMD0 Generic Clock Controller (GCLK)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L90) | [`atmel,sam0-gclk`](../../../../build/dts/api/bindings/clock/atmel%2Csam0-gclk.md#std-dtcompatible-atmel-sam0-gclk) |
| Counter | on-chip | Atmel SAM0 basic timer counter (TC) operating in 32-bit wide mode[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L156) | [`atmel,sam0-tc32`](../../../../build/dts/api/bindings/counter/atmel%2Csam0-tc32.md#std-dtcompatible-atmel-sam0-tc32) |
| DAC | on-chip | Atmel SAM0 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L212) | [`atmel,sam0-dac`](../../../../build/dts/api/bindings/dac/atmel%2Csam0-dac.md#std-dtcompatible-atmel-sam0-dac) |
| Flash controller | on-chip | Atmel SAM0 NVMC (Non-Volatile Memory Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L65) | [`atmel,sam0-nvmctrl`](../../../../build/dts/api/bindings/flash_controller/atmel%2Csam0-nvmctrl.md#std-dtcompatible-atmel-sam0-nvmctrl) |
| GPIO & Headers | on-chip | SAM0 GPIO PORT node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L169) | [`atmel,sam0-gpio`](../../../../build/dts/api/bindings/gpio/atmel%2Csam0-gpio.md#std-dtcompatible-atmel-sam0-gpio) |
| I2C | on-chip | Atmel SAM0 series SERCOM I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L138) | [`atmel,sam0-i2c`](../../../../build/dts/api/bindings/i2c/atmel%2Csam0-i2c.md#std-dtcompatible-atmel-sam0-i2c) |
| IIO | on-board | When an io-channel measures the voltage over a current sense amplifier, the interesting measurement is almost always the current through the sense resistor, not the voltage over it[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/ev11l78a/ev11l78a.dts?plain=1#L39) | [`current-sense-amplifier`](../../../../build/dts/api/bindings/iio/afe/current-sense-amplifier.md#std-dtcompatible-current-sense-amplifier) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | Atmel SAM0 series External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L98) | [`atmel,sam0-eic`](../../../../build/dts/api/bindings/interrupt-controller/atmel%2Csam0-eic.md#std-dtcompatible-atmel-sam0-eic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/ev11l78a/ev11l78a.dts?plain=1#L31) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L75) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/microchip/ev11l78a/ev11l78a.dts?plain=1#L89) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Atmel SAM0 PINMUX[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L104) | [`atmel,sam0-pinmux`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinmux.md#std-dtcompatible-atmel-sam0-pinmux) |
| on-chip | Atmel SAM0 Pinctrl Container[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L162) | [`atmel,sam0-pinctrl`](../../../../build/dts/api/bindings/pinctrl/atmel%2Csam0-pinctrl.md#std-dtcompatible-atmel-sam0-pinctrl) |
| RTC | on-chip | Atmel SAM0 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L190) | [`atmel,sam0-rtc`](../../../../build/dts/api/bindings/rtc/atmel%2Csam0-rtc.md#std-dtcompatible-atmel-sam0-rtc) |
| Serial controller | on-chip | Atmel SAM0 SERCOM UART driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L126) | [`atmel,sam0-uart`](../../../../build/dts/api/bindings/serial/atmel%2Csam0-uart.md#std-dtcompatible-atmel-sam0-uart) |
| SPI | on-chip | Atmel SAM0 SERCOM SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L120) | [`atmel,sam0-spi`](../../../../build/dts/api/bindings/spi/atmel%2Csam0-spi.md#std-dtcompatible-atmel-sam0-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L52) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| Watchdog | on-chip | Atmel SAM0 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/atmel/samd2x.dtsi?plain=1#L114) | [`atmel,sam0-watchdog`](../../../../build/dts/api/bindings/watchdog/atmel%2Csam0-watchdog.md#std-dtcompatible-atmel-sam0-watchdog) |

Refer to the [EV11L78A Schematics](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF) [[1]](#id2) for a detailed hardware diagram.

### Serial Port

The SAMD20 MCU has 6 SERCOM based USARTs. One of the USARTs
(SERCOM1) is available on the Debug/Status header.

### SPI Port

The SAMD20 MCU has 6 SERCOM based SPIs. One of the SPIs (SERCOM0)
is internally connected between the SAMD20 core and the UPD350.

### I²C Port

The SAMD20 MCU has 6 SERCOM based I2Cs. One of the I2Cs (SERCOM3)
is available on the Debug/Status header.

## References

[[1](#id3)]

[https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF](https://ww1.microchip.com/downloads/aemDocuments/documents/UNG/ProductDocuments/SupportingCollateral/03-00056-R1.0.PDF)
