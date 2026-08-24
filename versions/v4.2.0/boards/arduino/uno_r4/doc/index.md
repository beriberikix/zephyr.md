---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/arduino/uno_r4/doc/index.html
original_path: boards/arduino/uno_r4/doc/index.html
---

# Arduino UNO R4 Minima/WiFi

Board Overview

[![../../../../_images/arduino_uno_r4_minima.webp](https://docs.zephyrproject.org/4.2.0/_images/arduino_uno_r4_minima.webp)
](https://docs.zephyrproject.org/4.2.0/_images/arduino_uno_r4_minima.webp)

Arduino UNO R4 Minima/WiFi

Name:
:   `arduino_uno_r4`

Vendor:
:   Arduino

Architecture:
:   arm

SoC:
:   r7fa4m1ab3cfm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/arduino/uno_r4/doc/index.rst/../..)

## Overview

The Arduino UNO R4 Minima/WiFi is a development board featuring the Renesas RA4M1 SoC
in the Arduino form factor and is compatible with traditional Arduino.

## Hardware

- Renesas RA4MA1 Processor (ARM Cortex-M4 at 48 MHz)
- 256 KiB flash memory and 32 KiB of RAM
- One user LEDs
- One reset button
- One WiFi Transceiver (Arduino UNO R4 WiFi only)
- One 12x8 LED Matrix (Arduino UNO R4 WiFi only)
- Built-in CMSIS-DAP debug adapter (Arduino UNO R4 WiFi only)

### Supported Features

The `arduino_uno_r4` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `arduino_uno_r4@minima/r7fa4m1ab3cfm` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L18) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L220) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas,ra-adc.md#std-dtcompatible-renesas-ra-adc) |
| on-board | ADC channels exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_minima.overlay?plain=1#L66) | [`arduino,uno-adc`](../../../../build/dts/api/bindings/adc/arduino,uno-adc.md#std-dtcompatible-arduino-uno-adc) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L134) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L141) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L159) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L166) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L176) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L186)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L229) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L199) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas,ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L229) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas,ra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L236) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas,ra-dac.md#std-dtcompatible-renesas-ra-dac) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L54)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L74) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_minima.overlay?plain=1#L37) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Renesas RA I2C Master controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L251)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L244) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas,ra-iic.md#std-dtcompatible-renesas-ra-iic) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_minima.overlay?plain=1#L16) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_minima.overlay?plain=1#L23) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L40) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas,ra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L48)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L130) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L190) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas,ra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L281)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L299) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas,ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L25) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ab3cfm.dtsi?plain=1#L18) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4.dts?plain=1#L94) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L446) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L124) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L119)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L380) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas,ra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| on-board | PWM channels exposed on Arduino headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_minima.overlay?plain=1#L77) | [`arduino-header-pwm`](../../../../build/dts/api/bindings/pwm/arduino-header-pwm.md#std-dtcompatible-arduino-header-pwm) |
| RNG | on-chip | Renesas RA SCE5 TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L104) | [`renesas,ra-sce5-rng`](../../../../build/dts/api/bindings/rng/renesas,ra-sce5-rng.md#std-dtcompatible-renesas-ra-sce5-rng) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L56)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L137) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SPI | on-chip | Renesas RA SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L179)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L170) | [`renesas,ra-spi`](../../../../build/dts/api/bindings/spi/renesas,ra-spi.md#std-dtcompatible-renesas-ra-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L13) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L258) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L268) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-udc.md#std-dtcompatible-renesas-ra-udc) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L438) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas,ra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

#### `arduino_uno_r4@wifi/r7fa4m1ab3cfm` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L18) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | Renesas RA ADC node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L220) | [`renesas,ra-adc`](../../../../build/dts/api/bindings/adc/renesas,ra-adc.md#std-dtcompatible-renesas-ra-adc) |
| on-board | ADC channels exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_wifi.overlay?plain=1#L66) | [`arduino,uno-adc`](../../../../build/dts/api/bindings/adc/arduino,uno-adc.md#std-dtcompatible-arduino-uno-adc) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L134) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L141) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L159) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L166) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L176) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L186)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L229) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| Counter | on-chip | Renesas RA AGT as Counter[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L199) | [`renesas,ra-agt-counter`](../../../../build/dts/api/bindings/counter/renesas,ra-agt-counter.md#std-dtcompatible-renesas-ra-agt-counter) |
| DAC | on-chip | Renesas RA DAC Controller Global[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L229) | [`renesas,ra-dac-global`](../../../../build/dts/api/bindings/dac/renesas,ra-dac-global.md#std-dtcompatible-renesas-ra-dac-global) |
| on-chip | Renesas RA DAC Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L236) | [`renesas,ra-dac`](../../../../build/dts/api/bindings/dac/renesas,ra-dac.md#std-dtcompatible-renesas-ra-dac) |
| GPIO & Headers | on-chip | Renesas RA GPIO I/O Port[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L54)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L74) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_wifi.overlay?plain=1#L37) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | Renesas RA I2C Master controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L244) | [`renesas,ra-iic`](../../../../build/dts/api/bindings/i2c/renesas,ra-iic.md#std-dtcompatible-renesas-ra-iic) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_wifi.overlay?plain=1#L16) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_wifi.overlay?plain=1#L23) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Miscellaneous | on-chip | Renesas RA Event Link Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L40) | [`renesas,ra-elc`](../../../../build/dts/api/bindings/misc/renesas,ra-elc.md#std-dtcompatible-renesas-ra-elc) |
| on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L48)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L130) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| on-chip | Renesas RA AGT[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L190) | [`renesas,ra-agt`](../../../../build/dts/api/bindings/misc/renesas,ra-agt.md#std-dtcompatible-renesas-ra-agt) |
| on-chip | Renesas RA External Interrupt[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L281)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L299) | [`renesas,ra-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas,ra-external-interrupt.md#std-dtcompatible-renesas-ra-external-interrupt) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L25) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ab3cfm.dtsi?plain=1#L18) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4.dts?plain=1#L94) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L446) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | Renesas RA Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L124) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| PWM | on-chip | Renesas RA Pulse Width Modulation[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L119)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L380) | [`renesas,ra-pwm`](../../../../build/dts/api/bindings/pwm/renesas,ra-pwm.md#std-dtcompatible-renesas-ra-pwm) |
| on-board | PWM channels exposed on Arduino headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/arduino/uno_r4/arduino_uno_r4_wifi.overlay?plain=1#L77) | [`arduino-header-pwm`](../../../../build/dts/api/bindings/pwm/arduino-header-pwm.md#std-dtcompatible-arduino-header-pwm) |
| RNG | on-chip | Renesas RA SCE5 TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L104) | [`renesas,ra-sce5-rng`](../../../../build/dts/api/bindings/rng/renesas,ra-sce5-rng.md#std-dtcompatible-renesas-ra-sce5-rng) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L56)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L137) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SPI | on-chip | Renesas RA SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L170)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L179) | [`renesas,ra-spi`](../../../../build/dts/api/bindings/spi/renesas,ra-spi.md#std-dtcompatible-renesas-ra-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/r7fa4m1ax.dtsi?plain=1#L13) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| USB | on-chip | Renesas RA USB full-speed controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L258) | [`renesas,ra-usbfs`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-usbfs.md#std-dtcompatible-renesas-ra-usbfs) |
| on-chip | Renesas RA USB device controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L268) | [`renesas,ra-udc`](../../../../build/dts/api/bindings/usb/renesas/renesas,ra-udc.md#std-dtcompatible-renesas-ra-udc) |
| Watchdog | on-chip | Renesas RA Watchdog (wdt)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra4/ra4-cm4-common.dtsi?plain=1#L438) | [`renesas,ra-wdt`](../../../../build/dts/api/bindings/watchdog/renesas,ra-wdt.md#std-dtcompatible-renesas-ra-wdt) |

## Programming and debugging

The `arduino_uno_r4` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Debug adapter

A debug adapter is required to flash and debug programs.
Arduino UNO R4 WiFi has a built-in debug adapter that
you can use for flashing and debugging.

In the Arduino UNO R4 Minima case, You need to prepare
debug adapter separately. A 5V-compatible CMSIS-DAP adapter
adapts to this board.

### Building & Flashing

You can build and flash with `west flash` command (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@minima samples/basic/blinky
west flash
```

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi samples/basic/blinky
west flash
```

### Debugging

Debugging can be done with `west debug` command.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@minima samples/basic/blinky
west debug
```

```shell
# From the root of the zephyr repository
west build -b arduino_uno_r4@wifi samples/basic/blinky
west debug
```

#### Using pyOCD

Various debug adapters, including cmsis-dap probes, can debug the Arduino UNO R4 with pyOCD.
The default configuration uses the pyOCD for debugging.
You must install CMSIS-Pack when flashing or debugging Arduino UNO R4 Minima with pyOCD.
If not installed yet, execute the following command to install CMSIS-Pack for Arduino UNO R4.

```shell
pyocd pack install r7fa4m1ab
```

### Restoring Arduino Bootloader

If you corrupt the Arduino bootloader, you can restore it with the following command.

```shell
wget https://raw.githubusercontent.com/arduino/ArduinoCore-renesas/main/bootloaders/UNO_R4/dfu_minima.hex
pyocd flash -e sector -a 0x0 -t r7fa4m1ab dfu_minima.hex
```

```shell
wget https://raw.githubusercontent.com/arduino/ArduinoCore-renesas/main/bootloaders/UNO_R4/dfu_wifi.hex
pyocd flash -e sector -a 0x0 -t r7fa4m1ab dfu_wifi.hex
```
