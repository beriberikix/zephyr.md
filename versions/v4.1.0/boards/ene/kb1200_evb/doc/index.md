---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/ene/kb1200_evb/doc/index.html
original_path: boards/ene/kb1200_evb/doc/index.html
---

# ENE KB1200\_EVB

Board Overview

Name:
:   `kb1200_evb`

Vendor:
:   ENE Technology, Inc.

Architecture:
:   arm

SoC:
:   kb1200

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1200_evb/doc/index.rst/../..)

## Overview

The KB1200\_EVB kit is a development platform to evaluate the
ENE KB1200 series microcontrollers. This board needs to be mated with
part number KB1200.

## Hardware

- ARM Cortex-M4F Processor
- 512KB Flash and 320KB RAM
- ADC & GPIO headers
- SER1, SER2 and SER3
- FAN PWM interface
- ENE Debug interface

### Supported Features

The `kb1200_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `kb1200_evb/kb1200` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L20) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | ENE KB1200 ADC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L127) | [`ene,kb1200-adc`](../../../../build/dts/api/bindings/adc/ene%2Ckb1200-adc.md#std-dtcompatible-ene-kb1200-adc) |
| GPIO & Headers | on-chip | ENE KB1200 GPIO(General purpose IO) Port node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L62)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L72) | [`ene,kb1200-gpio`](../../../../build/dts/api/bindings/gpio/ene%2Ckb1200-gpio.md#std-dtcompatible-ene-kb1200-gpio) |
| I2C | on-chip | ENE I2C/SMB controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L249)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L258) | [`ene,kb1200-i2c`](../../../../build/dts/api/bindings/i2c/ene%2Ckb1200-i2c.md#std-dtcompatible-ene-kb1200-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/kb1200_evb.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1200_evb/kb1200_evb.dts?plain=1#L39) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | ENE, Power Manager[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L46) | [`ene,kb1200-pmu`](../../../../build/dts/api/bindings/misc/ene%2Ckb1200-pmu.md#std-dtcompatible-ene-kb1200-pmu) |
| on-chip | ENE, General Configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L51) | [`ene,kb1200-gcfg`](../../../../build/dts/api/bindings/misc/ene%2Ckb1200-gcfg.md#std-dtcompatible-ene-kb1200-gcfg) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L40) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | The ENE KB1200 pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L56) | [`ene,kb1200-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ene%2Ckb1200-pinctrl.md#std-dtcompatible-ene-kb1200-pinctrl) |
| PWM | on-chip | ENE, Pulse Width Modulator (PWM) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L134)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L141) | [`ene,kb1200-pwm`](../../../../build/dts/api/bindings/pwm/ene%2Ckb1200-pwm.md#std-dtcompatible-ene-kb1200-pwm) |
| Serial controller | on-chip | ENE KB1200 UART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L103) | [`ene,kb1200-uart`](../../../../build/dts/api/bindings/serial/ene%2Ckb1200-uart.md#std-dtcompatible-ene-kb1200-uart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Tachometer | on-chip | ENE, KB1200-Tachometer node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L218) | [`ene,kb1200-tach`](../../../../build/dts/api/bindings/tach/ene%2Ckb1200-tach.md#std-dtcompatible-ene-kb1200-tach) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | ENE watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb1200.dtsi?plain=1#L242) | [`ene,kb1200-watchdog`](../../../../build/dts/api/bindings/watchdog/ene%2Ckb1200-watchdog.md#std-dtcompatible-ene-kb1200-watchdog) |

### System Clock

The KB1200 MCU is configured to use the 96Mhz internal oscillator with the
on-chip DPLL to generate a resulting EC clock rate of 96MHz/48MHz/24MHz/12MHz.
See Processor clock control register (refer 5.1 General Configuration)

## Programming and Debugging

### Flashing

If the correct headers are installed, this board supports SWD Debug Interface.

To flash with SWD, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

### Debugging

Use SWD with a J-Link

### References
