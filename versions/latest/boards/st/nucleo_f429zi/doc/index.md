---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_f429zi/doc/index.html
original_path: boards/st/nucleo_f429zi/doc/index.html
---

# Nucleo F429ZI

Board Overview

[![../../../../_images/nucleo_f429zi.jpg](../../../../_images/nucleo_f429zi.jpg)
](../../../../_images/nucleo_f429zi.jpg)

Nucleo F429ZI

Name:
:   `nucleo_f429zi`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f429xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f429zi/doc/index.rst/../..)

## Overview

The Nucleo F429ZI board features an ARM Cortex-M4 based STM32F429ZI MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo F429ZI board:

- STM32 microcontroller in LQFP144 package
- LSE crystal: 32.768 kHz crystal oscillator
- USB OTG
- Ethernet compliant with IEEE-802.3-2002
- Two types of extension resources:

  - ST Zio connector including: support for Arduino\* Uno V3 connectivity
    (A0 to A5, D0 to D15) and additional signals exposing a wide range of
    peripherals
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - 5 V from ST-LINK/V2-1 USB VBUS
  - External power sources: 3.3 V and 7 - 12 V on ST Zio or ST morpho
    connectors, 5 V on ST morpho connector
- Three user LEDs
- Two push-buttons: USER and RESET

More information about the board can be found at the [Nucleo F429ZI website](https://www.st.com/en/evaluation-tools/nucleo-f429zi.html).

## Hardware

The Nucleo F429ZI provides the following hardware components:

- STM32F429ZIT6 in LQFP144 package
- ARM® 32-bit Cortex® -M4 CPU with FPU
- 180 MHz max CPU frequency
- VDD from 1.8 V to 3.6 V
- 2 MB Flash
- 256+4 KB SRAM including 64-Kbyte of core coupled memory
- GPIO with external interrupt capability
- 3x12-bit ADC with 24 channels
- 2x12-bit D/A converters
- RTC
- Advanced-control Timer
- General Purpose Timers (17)
- Watchdog Timers (2)
- USART/UART (4/4)
- I2C (3)
- SPI (6)
- SDIO
- 2xCAN
- USB 2.0 OTG FS with on-chip PHY
- USB 2.0 OTG HS/FS with dedicated DMA, on-chip full-speed PHY and ULPI
- 10/100 Ethernet MAC with dedicated DMA
- 8- to 14-bit parallel camera
- CRC calculation unit
- True random number generator
- DMA Controller

More information about STM32F429ZI can be found here:

- [STM32F429ZI on www.st.com](https://www.st.com/en/microcontrollers/stm32f429zi.html)
- [STM32F429 reference manual](https://www.st.com/resource/en/reference_manual/dm00031020.pdf)
- [STM32F429 datasheet](https://www.st.com/resource/en/datasheet/DM00071990.pdf)

### Supported Features

The `nucleo_f429zi` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_f429zi/stm32f429xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L34) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32F4 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L543) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L244) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L208) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L127) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L62) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L82)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L68) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32F4 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L89) | [`st,stm32f4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f4-pll-clock.md#std-dtcompatible-st-stm32f4-pll-clock) |
| on-chip | STM32F4 PLL I2S[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L11) | [`st,stm32f4-plli2s-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32f4-plli2s-clock.md#std-dtcompatible-st-stm32f4-plli2s-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L97) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L364) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L278) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f429.dtsi?plain=1#L22) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st%2Cstm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L569)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L560) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L13) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | ST STM32 Ethernet MAC, a child node of the Ethernet controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L19) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f429zi/nucleo_f429zi.dts?plain=1#L200) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L109) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L159) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f429zi/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V1 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L265)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L289) | [`st,stm32-i2c-v1`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v1.md#std-dtcompatible-st-stm32-i2c-v1) |
| I2S | on-chip | STM32 I2S controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L51) | [`st,stm32-i2s`](../../../../build/dts/api/bindings/i2s/st%2Cstm32-i2s.md#std-dtcompatible-st-stm32-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f429zi/nucleo_f429zi.dts?plain=1#L45) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L138) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f429zi/nucleo_f429zi.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f407.dtsi?plain=1#L30) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st%2Cstm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L536) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f427.dtsi?plain=1#L89) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f427.dtsi?plain=1#L95) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L579) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32F4 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L117) | [`st,stm32f4-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32f4-nv-flash.md#std-dtcompatible-st-stm32f4-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f429zi/nucleo_f429zi.dts?plain=1#L207) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L632) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L153) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L590) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L335)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L358) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L132) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L228) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L526) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 quadrature decoder[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L341) | [`st,stm32-qdec`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-qdec.md#std-dtcompatible-st-stm32-qdec) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L606) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L617) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L625) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L256)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L238) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L55) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L637) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L301)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f401.dtsi?plain=1#L21) | [`st,stm32-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi.md#std-dtcompatible-st-stm32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L57) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L325)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L348) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L311) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f405.dtsi?plain=1#L194) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L224) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f4/stm32f4.dtsi?plain=1#L230) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

The Nucleo F429ZI Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

#### Available pins:

![Nucleo F429ZI ZIO connectors (left)](../../../../_images/nucleo_f429zi_cn8.jpg)
![Nucleo F429ZI ZIO connectors (right)](../../../../_images/nucleo_f429zi_cn7.jpg)
![Nucleo F429ZI Morpho connectors (left)](../../../../_images/nucleo_f429zi_cn11.jpg)
![Nucleo F429ZI Morpho connectors (right)](../../../../_images/nucleo_f429zi_cn12.jpg)

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00244518.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo F429ZI board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART\_6 TX/RX : PG14/PG9 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- SPI1 NSS/SCK/MISO/MOSI : PD14/PA5/PA6/PA7 (Arduino SPI)
- PWM\_2\_CH1 : PE13
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- USB DM : PA11
- USB DP : PA12
- ADC1 : PA0

#### System Clock

The Nucleo F429ZI System Clock could be driven by an internal or external oscillator,
as well as by the main PLL clock. By default System clock is driven by PLL clock at 180MHz,
driven by an 8MHz high speed external clock.

#### Serial Port

The Nucleo F429ZI board has 8 UARTs. The Zephyr console output is assigned to UART3.
Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_f429zi` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

The Nucleo F429ZI board includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

## Flash partitions for MCUBoot bootloader

The on-board STM32F429ZI MCU has 2MBs of internal flash memory. To use [MCUboot](https://github.com/JuulLabs-OSS/mcuboot/blob/master/README.md),
define a [Zephyr partition table](../../../../services/storage/flash_map/flash_map.md#flash-map-api) for the flash memory in
its devicetree file `nucleo_f429zi.dts`. As a reference, a partition table for
MCUBoot is already defined in the devicetree file, with these settings:

- [MCUBoot](https://github.com/JuulLabs-OSS/mcuboot/blob/master/README.md) bootloader partition takes 64K bytes.
- Zephyr settings partition takes 64K bytes.
- Application image takes 256K bytes in Slot 0 partition.
- Updating image takes another 256K bytes in Slot 1 partition.
- A scratch partition with 128K is required for image swap.

A specific application can adjust each partition size based on its needs.
