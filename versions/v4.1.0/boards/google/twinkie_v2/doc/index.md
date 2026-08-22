---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/google/twinkie_v2/doc/index.html
original_path: boards/google/twinkie_v2/doc/index.html
---

# Twinkie V2

Board Overview

Name:
:   `google_twinkie_v2`

Vendor:
:   Google, Inc.

Architecture:
:   arm

SoC:
:   stm32g0b1xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/google/twinkie_v2/doc/index.rst/../..)

## Overview

Google Twinkie V2 is a reference board for the google power delivery analyzer
(PDA) Twinkie V2.

## Hardware

- STM32G0B1REI6

### Supported Features

The `google_twinkie_v2` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `google_twinkie_v2/stm32g0b1xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L32) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L406) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0b1.dtsi?plain=1#L35) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L116) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32G0 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L66) | [`st,stm32g0-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g0-hsi-clock.md#std-dtcompatible-st-stm32g0-hsi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L74) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L82) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32G0 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L89) | [`st,stm32g0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g0-pll-clock.md#std-dtcompatible-st-stm32g0-pll-clock) |
| on-chip | STM32 HSI48 Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0b1.dtsi?plain=1#L13) | [`st,stm32-hsi48-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hsi48-clock.md#std-dtcompatible-st-stm32-hsi48-clock) |
| Counter | on-chip | STM32 counters[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L268) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g051.dtsi?plain=1#L66) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L429) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L441) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L97) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L145) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L362) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| IIO | on-board | Description for a voltage divider, with optional ability to measure resistance of the upper leg[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/google/twinkie_v2/google_twinkie_v2.dts?plain=1#L46) | [`voltage-divider`](../../../../build/dts/api/bindings/iio/afe/voltage-divider.md#std-dtcompatible-voltage-divider) |
| on-board | When an io-channel measures the voltage over a current sense amplifier, the interesting measurement is almost always the current through the sense resistor, not the voltage over it[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/google/twinkie_v2/google_twinkie_v2.dts?plain=1#L65) | [`current-sense-amplifier`](../../../../build/dts/api/bindings/iio/afe/current-sense-amplifier.md#std-dtcompatible-current-sense-amplifier) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/google/twinkie_v2/google_twinkie_v2.dts?plain=1#L34) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L127) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/google/twinkie_v2/google_twinkie_v2.dts?plain=1#L21) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L202) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L106) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0b1.dtsi?plain=1#L153) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L139) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L262) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L121) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L186) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L453) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L464) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L472) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L223) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g031.dtsi?plain=1#L14) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L479) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L386) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g071.dtsi?plain=1#L37)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g071.dtsi?plain=1#L45) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L241) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L252) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0b1.dtsi?plain=1#L139) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L209) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g0/stm32g0.dtsi?plain=1#L215) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

#### Default Zephyr Peripheral Mapping:

- CC1\_BUF : PA1
- CC2\_BUF : PA3
- VBUS\_READ\_BUF : PB11
- CSA\_VBUS : PC4
- CSA\_CC2 : PC5

## Programming and Debugging

Build application as usual for the `google_twinkie_v2` board, and flash
using dfu-util or J-Link.

### Debugging

Use SWD with a J-Link or ST-Link.
