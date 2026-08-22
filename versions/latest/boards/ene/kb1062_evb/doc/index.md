---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/ene/kb1062_evb/doc/index.html
original_path: boards/ene/kb1062_evb/doc/index.html
---

# ENE KB1062\_EVB

Board Overview

Name:
:   `kb1062_evb`

Vendor:
:   ENE Technology, Inc.

Architecture:
:   arm

SoC:
:   kb1062

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/ene/kb1062_evb/doc/index.rst/../..)

## Overview

The KB1062\_EVB kit is a development platform to evaluate the
ENE KB106X series microcontrollers. This board needs to be mated with
part number KB1062.

## Hardware

- ARM Cortex-M3 Processor
- 256KB Flash and 64KB RAM
- ADC & GPIO headers
- SER serial port
- FAN PWM interface
- ENE Debug interface

### Supported Features

The `kb1062_evb` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `kb1062_evb/kb1062` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M3 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L20) | [`arm,cortex-m3`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m3.md#std-dtcompatible-arm-cortex-m3) |
| ADC | on-chip | ENE KB106X ADC controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L122) | [`ene,kb106x-adc`](../../../../build/dts/api/bindings/adc/ene%2Ckb106x-adc.md#std-dtcompatible-ene-kb106x-adc) |
| GPIO & Headers | on-chip | ENE KB106X GPIO(General purpose IO) Port node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L64)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L74) | [`ene,kb106x-gpio`](../../../../build/dts/api/bindings/gpio/ene%2Ckb106x-gpio.md#std-dtcompatible-ene-kb106x-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1062_evb/kb1062_evb.dts?plain=1#L30) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/ene/kb1062_evb/kb1062_evb.dts?plain=1#L40) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | ENE, General Configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L46) | [`ene,kb106x-gcfg`](../../../../build/dts/api/bindings/misc/ene%2Ckb106x-gcfg.md#std-dtcompatible-ene-kb106x-gcfg) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L40) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | The ENE KB106X pin controller is a singleton node responsible for controlling pin function selection and pin properties[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L57) | [`ene,kb106x-pinctrl`](../../../../build/dts/api/bindings/pinctrl/ene%2Ckb106x-pinctrl.md#std-dtcompatible-ene-kb106x-pinctrl) |
| PWM | on-chip | ENE, Pulse Width Modulator (PWM) node[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L129) | [`ene,kb106x-pwm`](../../../../build/dts/api/bindings/pwm/ene%2Ckb106x-pwm.md#std-dtcompatible-ene-kb106x-pwm) |
| Serial controller | on-chip | ENE KB106X UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L115) | [`ene,kb106x-uart`](../../../../build/dts/api/bindings/serial/ene%2Ckb106x-uart.md#std-dtcompatible-ene-kb106x-uart) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L28) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| Watchdog | on-chip | ENE watchdog timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/ene/kb106x/kb106x.dtsi?plain=1#L161) | [`ene,kb106x-watchdog`](../../../../build/dts/api/bindings/watchdog/ene%2Ckb106x-watchdog.md#std-dtcompatible-ene-kb106x-watchdog) |

### System Clock

The KB106x MCU is configured to use the 48Mhz internal oscillator with the
on-chip DPLL to generate a resulting EC clock rate of 48MHz/24MHz
See Processor clock control register (refer 5.1 General Configuration)

## Programming and Debugging

The `kb1062_evb` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

If the correct headers are installed, this board supports SWD Debug Interface.

To flash with SWD, install the drivers for your programmer, for example:
SEGGER J-link’s drivers are at [https://www.segger.com/downloads/jlink/](https://www.segger.com/downloads/jlink/)

### Debugging

Use SWD with a J-Link

### References
