---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/olimex/stm32_h407/doc/index.html
original_path: boards/olimex/stm32_h407/doc/index.html
---

# OLIMEX-STM32-H407

Board Overview

[![../../../../_images/olimex_stm32_h407.jpg](https://docs.zephyrproject.org/4.2.0/_images/olimex_stm32_h407.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/olimex_stm32_h407.jpg)

OLIMEX-STM32-H407

Name:
:   `olimex_stm32_h407`

Vendor:
:   OLIMEX Ltd.

Architecture:
:   arm

SoC:
:   stm32f407xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/olimex/stm32_h407/doc/index.rst/../..)

## Overview

The OLIMEX-STM32-H407 is open source hardware and is based on
the STMicroelectronics STM32F407ZG ARM Cortex-M4 CPU.

![OLIMEX-STM32-H407](https://docs.zephyrproject.org/4.2.0/_images/olimex_stm32_h4071.jpg)

OLIMEX-STM32-H407

## Hardware

Information about the board can be found at the
[OLIMEX-STM32-H407 website](https://www.olimex.com/Products/ARM/ST/STM32-H407/open-source-hardware) and [OLIMEX-STM32-H407 user manual](https://www.olimex.com/Products/ARM/ST/STM32-H407/resources/STM32-H407.pdf).
The [ST STM32F407ZG Datasheet](https://www.st.com/resource/en/reference_manual/dm00031020.pdf) contains the processor’s
information and the datasheet.

### Supported Features

The `olimex_stm32_h407` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `olimex_stm32_h407/stm32f407xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L34) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32F4 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L543) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st,stm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L244) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L208) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L127) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L62) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L82)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F4 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L89) | [`st,stm32f4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f4-pll-clock.md#std-dtcompatible-st-stm32f4-pll-clock) |
| on-chip | STM32F4 PLL I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L11) | [`st,stm32f4-plli2s-clock`](../../../../build/dts/api/bindings/clock/st,stm32f4-plli2s-clock.md#std-dtcompatible-st-stm32f4-plli2s-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L97) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L364) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L278) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L560) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L13) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | ST STM32 Ethernet MAC, a child node of the Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L19) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L109) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L159) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V1 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L265) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| I2S | on-chip | STM32 I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L51) | [`st,stm32-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32-i2s.md#std-dtcompatible-st-stm32-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/stm32_h407/olimex_stm32_h407.dts?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L138) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/olimex/stm32_h407/olimex_stm32_h407.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L30) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L536) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L579) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32F4 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L117) | [`st,stm32f4-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32f4-nv-flash.md#std-dtcompatible-st-stm32f4-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L632) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L153) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L590) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L335) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L132) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L228) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L526) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 quadrature decoder[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L341) | [`st,stm32-qdec`](../../../../build/dts/api/bindings/sensor/st,stm32-qdec.md#std-dtcompatible-st-stm32-qdec) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L606) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L617) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L625) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L247)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L238) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L55) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L637) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L301) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st,stm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L325) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L311) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L194) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L224) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L230) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Pin Mapping

![OLIMEX-STM32-H407 connectors](https://docs.zephyrproject.org/4.2.0/_images/olimex-stm32-h407-front.jpg)

OLIMEX-STM32-H407 connectors

#### LED

- LED (green) = PC13
- PWR\_LED (red) = power

#### Push buttons

- BUT = PA0
- RST = NRST

#### External Connectors

JTAG/SWD debug

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 |  |
| 2 | +3.3V | 12 | GND |
| 3 | PB4 / TRST | 13 | PB3 / TDO |
| 4 | GND | 14 | GND |
| 5 | PA15 / TDI | 15 | PB4 / TRST |
| 6 | GND | 16 | GND |
| 7 | PA13 / TMS | 17 |  |
| 8 | GND | 18 | GND |
| 9 | PA14 / TCK | 19 | +5V\_JTAG |
| 10 | GND | 20 | GND |

UEXT

| PIN # | Wire Name | STM32F407 port |
| --- | --- | --- |
| 1 | +3.3V |  |
| 2 | GND |  |
| 3 | PC6/USART6\_TX | PC6 |
| 4 | PC7/USART6\_RX | PC7 |
| 5 | PB8/I2C1\_SCL | PB8 |
| 6 | PB9/I2C1\_SDA | PB9 |
| 7 | PC2/SPI2\_MISO | PC2 |
| 8 | PC3/SPI2\_MOSI | PC3 |
| 9 | PB10/SPI\_SCK/UART3\_TX | PB10 |
| 10 | RB7/UEXT\_CS | PB7 |

#### Arduino Headers

CON1 power

| Pin | Signal Name | STM32F407 Pin# |
| --- | --- | --- |
| RST | RESET | 25 |
| 3V3 | VCC (3V3) | N/A |
| 5V | VDD (5V) | N/A |
| GND | GND | N/A |
| GND | GND | N/A |
| VIN | VIN | N/A |

CON2 analog

| Pin | Signal Name | STM32F407 Pin# |
| --- | --- | --- |
| A0 | PC0 | 26 |
| A1 | PC1 | 27 |
| A2 | PB0 | 46 |
| A3 | PB1 | 47 |
| A4 | PC4 | 44 |
| A5 | PC5 | 45 |

CON3 digital

| Pin | Signal Name | STM32F407 Pin# |
| --- | --- | --- |
| D0 | PA3/USART2\_RX | 37 |
| D1 | PA2/USART2\_TX | 36 |
| D2 | PG7 | 92 |
| D3 | PG8 | 93 |
| D4 | PG12 | 127 |
| D5 | PG13 | 128 |
| D6 | PG14 | 129 |
| D7 | PG15 | 132 |

CON4 digital

| Pin | Signal Name | STM32F407 Pin# |
| --- | --- | --- |
| D8 | PA1 | 35 |
| D9 | PB11 | 70 |
| D10 | PA4 | 40 |
| D11 | PA7 | 43 |
| D12 | PA6 | 42 |
| D13 | PA5 | 41 |
| GND | AGND | 31 |
| AREF | AREF | 32 |

PD

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 | PD8 |
| 2 | GND | 12 | PD9 |
| 3 | PD0 | 13 | PD10 |
| 4 | PD1 | 14 | PD11 |
| 5 | PD2/SD\_CMD | 15 | PD12 |
| 6 | PD3 | 16 | PD13 |
| 7 | PD4 | 17 | PD14 |
| 8 | PD5 | 18 | PD15 |
| 9 | PD6 | 19 | +5V |
| 10 | PD7 | 20 | GND |

PE

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 | PE8 |
| 2 | GND | 12 | PE9 |
| 3 | PE0 | 13 | PE10 |
| 4 | PE1 | 14 | PE11 |
| 5 | PE2 | 15 | PE12 |
| 6 | PE3 | 16 | PE13 |
| 7 | PE4 | 17 | PE14 |
| 8 | PE5 | 18 | PE15 |
| 9 | PE6 | 19 | +5V |
| 10 | PE7 | 20 | GND |

PF

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 | PF8 |
| 2 | GND | 12 | PF9 |
| 3 | PF0 | 13 | PF10 |
| 4 | PF1 | 14 | PF11 |
| 5 | PF2 | 15 | PF12 |
| 6 | PF3 | 16 | PF13 |
| 7 | PF4 | 17 | PF14 |
| 8 | PF5 | 18 | PF15 |
| 9 | PF6 | 19 | +5V |
| 10 | PF7 | 20 | GND |

PG

| PIN # | Signal Name | Pin # | Signal Name |
| --- | --- | --- | --- |
| 1 | +3.3V | 11 | PG8/D3 |
| 2 | GND | 12 | PG9 |
| 3 | PG0 | 13 | PG10 |
| 4 | PG1 | 14 | PG11 |
| 5 | PG2 | 15 | PG12/D4 |
| 6 | PG3 | 16 | PG13/D5 |
| 7 | PG4 | 17 | PG14/D6 |
| 8 | PG5 | 18 | PG15/D7 |
| 9 | PG6 | 19 | +5V |
| 10 | PG7/D2 | 20 | GND |

### System Clock

OLIMEX-STM32-H407 has two external oscillators. The frequency of
the slow clock is 32.768 kHz. The frequency of the main clock
is 12 MHz. The processor can setup HSE to drive the master clock,
which can be set as high as 168 MHz.

## Programming and Debugging

The `olimex_stm32_h407` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

The OLIMEX-STM32-H407 board does not include an embedded debug tool
interface. You will need to use ST tools or an external JTAG probe.
In the following examples the Olimex ARM-USB-OCD-H is used.

If you have an external JTAG probe compliant with the default Zephyr OpenOCD
configuration, however, then applications for the `olimex_stm32_h407` board
configuration can be built and flashed in the usual way (see
[Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing an application to the Olimex-STM32-H407

Connect the ARM-USB-OCD-H debugger to your host computer and to the JTAG port
of the OLIMEX-STM32-H407 board. Then build and flash an application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_h407 samples/hello_world
west flash
```

Run a serial host program to connect with your board:

```shell
$ minicom -D /dev/ttyUSB0
```

After resetting the board, you should see the following message:

```shell
***** BOOTING ZEPHYR OS v1.11.0 - BUILD: Mar 12 2018 03:12:40 *****
Hello World! arm
```

### Debugging

Provided that you have a JTAG probe, you can debug an application in the usual
way. Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b olimex_stm32_h407 samples/hello_world
west debug
```
