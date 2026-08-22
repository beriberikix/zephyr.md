---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/olimex/lora_stm32wl_devkit/doc/olimex_lora_stm32wl_devkit.html
original_path: boards/olimex/lora_stm32wl_devkit/doc/olimex_lora_stm32wl_devkit.html
---

# LoRa STM32WL DevKit

Board Overview

[![../../../../_images/olimex-stm32wl-devkit.jpg](../../../../_images/olimex-stm32wl-devkit.jpg)
](../../../../_images/olimex-stm32wl-devkit.jpg)

LoRa STM32WL DevKit

Name:
:   `olimex_lora_stm32wl_devkit`

Vendor:
:   OLIMEX Ltd.

Architecture:
:   arm

SoC:
:   stm32wle5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/olimex/lora_stm32wl_devkit/doc/olimex_lora_stm32wl_devkit.rst/../..)

## Overview

LoRaWAN development kit based on Olimex BB-STM32WL module using the
STM32WLE5CCU6 MCU.

## Hardware

The board has below hardware features:

- BB-STM32WL, 256KB Flash, 64KB RAM with external antenna
- Lithium battery connector 3V (does not include battery)
- UEXT connector for external sensors
- BME280 temperature, humidity, pressure sensor
- LDR resistor for lighting measurement
- IIS2MDCTR 3-axis magnetometer for smart parking
- GPIO connector for prototyping
- Low power design
- 1 User LED
- 1 user, 1 boot, and 1 reset push-button
- 32.768 kHz LSE crystal oscillator

More information about the board and the module can be found here:

- [LoRa-STM32WL-DevKit Repository](https://github.com/OLIMEX/LoRa-STM32WL-DevKIT)
- [LoRa-STM32WL-DevKit page on OLIMEX website](https://www.olimex.com/Products/IoT/LoRa/LoRa-STM32WL-DevKit/open-source-hardware)
- [BB-STM32WL Module website](https://www.olimex.com/Products/IoT/LoRa/BB-STM32WL/)
- [STM32WLE5CC reference manual](https://www.st.com/resource/en/reference_manual/dm00530369-stm32wlex-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf)
- [STM32WLE5CC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wle5cc.html)

### Supported Features

The `olimex_lora_stm32wl_devkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `olimex_lora_stm32wl_devkit/stm32wle5xx@C` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L31) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L344) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32WL RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L128) | [`st,stm32wl-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-rcc.md#std-dtcompatible-st-stm32wl-rcc) |
| on-chip | STM32WL HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L65) | [`st,stm32wl-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-hse-clock.md#std-dtcompatible-st-stm32wl-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L102) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L402) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L452) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L361) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L471) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L493) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L110) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L160) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L269)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L281) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L139) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-chip | STM32WL Sub-GHz Radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L335) | [`st,stm32wl-subghz-radio`](../../../../build/dts/api/bindings/lora/st%2Cstm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L220) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L118) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L135) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L154) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L505) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L379) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Regulator | on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit_C.overlay?plain=1#L9) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L133) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L461) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L204) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | BME280 integrated environmental sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L96) | [`bosch,bme280`](../../../../build/dts/api/compatibles/bosch%2Cbme280.md#std-dtcompatible-bosch-bme280) |
| on-board | STMicroelectronics IIS2MDC magnetometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L102) | [`st,iis2mdc`](../../../../build/dts/api/compatibles/st%2Ciis2mdc.md#std-dtcompatible-st-iis2mdc) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L534) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L545) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L553) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L241)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L250) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L259) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L560) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L305)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L315) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| on-chip | STM32 SUBGHZ SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L325) | [`st,stm32-spi-subghz`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L60) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L193) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L369) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L227) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L233) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

#### `olimex_lora_stm32wl_devkit/stm32wle5xx@D` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L31) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L344) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32WL RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L128) | [`st,stm32wl-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-rcc.md#std-dtcompatible-st-stm32wl-rcc) |
| on-chip | STM32WL HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L65) | [`st,stm32wl-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wl-hse-clock.md#std-dtcompatible-st-stm32wl-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L102) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L402) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L452) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L361) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L471) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L493) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L110) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L160) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L269)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L281) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L31) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L139) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L23) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-chip | STM32WL Sub-GHz Radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L335) | [`st,stm32wl-subghz-radio`](../../../../build/dts/api/bindings/lora/st%2Cstm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L220) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L118) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L135) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L154) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L505) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L379) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Regulator | on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit_C.overlay?plain=1#L9) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L133) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L461) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L204) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | BME280 integrated environmental sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L96) | [`bosch,bme280`](../../../../build/dts/api/compatibles/bosch%2Cbme280.md#std-dtcompatible-bosch-bme280) |
| on-board | STMicroelectronics IIS2MDC magnetometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/lora_stm32wl_devkit/olimex_lora_stm32wl_devkit.dts?plain=1#L102) | [`st,iis2mdc`](../../../../build/dts/api/compatibles/st%2Ciis2mdc.md#std-dtcompatible-st-iis2mdc) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L534) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L545) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L553) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L241)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L250) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L259) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L560) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L305)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L315) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| on-chip | STM32 SUBGHZ SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L325) | [`st,stm32-spi-subghz`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L60) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L193) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L369) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L227) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L233) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

## Programming and Debugging

Applications for the `olimex_lora_stm32wl_devkit` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

The board contains an on-board debug probe which implements the CMSIS-DAP
interface.

It can also be debugged and flashed with an external debug probe connected
to the SWD pins.

The built-in debug probe works with pyOCD, but requires installing an additional
pack to support the STM32WL:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32wl
```

### Flashing an application

Connect the board to your host computer and build and flash an application.

```shell
# From the root of the zephyr repository
west build -b olimex_lora_stm32wl_devkit samples/hello_world
west flash
```

If you’re using devkit revision C or higher, you’ll need to specify the
appropriate revision letter to enable the VDDIO supply to the UEXT1 connector and
CON1 pin header.

```shell
# From the root of the zephyr repository
west build -b olimex_lora_stm32wl_devkit@D samples/hello_world
west flash
```

Run a serial terminal to connect with your board. By default, `usart1` is
accessible via the built-in USB to UART converter.

```shell
$ picocom --baud 115200 /dev/ttyACM0
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_lora_stm32wl_devkit samples/basic/blinky
west debug
```

On board revisions C or newer:

```shell
# From the root of the zephyr repository
west build -b olimex_lora_stm32wl_devkit@D samples/basic/blinky
west debug
```
