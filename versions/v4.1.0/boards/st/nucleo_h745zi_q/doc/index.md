---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_h745zi_q/doc/index.html
original_path: boards/st/nucleo_h745zi_q/doc/index.html
---

# Nucleo H745ZI-Q

Board Overview

[![../../../../_images/nucleo_h745zi_q.jpg](https://docs.zephyrproject.org/4.1.0/_images/nucleo_h745zi_q.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/nucleo_h745zi_q.jpg)

Nucleo H745ZI-Q

Name:
:   `nucleo_h745zi_q`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h745xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_h745zi_q/doc/index.rst/../..)

## Overview

The STM32 Nucleo-144 board provides an affordable and flexible way for users
to try out new concepts and build prototypes by choosing from the various combinations
of performance and power consumption features, provided by the STM32 microcontroller.
For the compatible boards, the internal or external SMPS significantly reduces power
consumption in Run mode.

The ST Zio connector, which extends the ARDUINO® Uno V3 connectivity, and
the ST morpho headers provide an easy means of expanding the functionality of the Nucleo
open development platform with a wide choice of specialized shields.
The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK V3 debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software
libraries and examples available with the STM32Cube MCU Package.

Key Features

- STM32 microcontroller in LQFP144 package
- Ethernet compliant with IEEE-802.3-2002 (depending on STM32 support)
- USB OTG or full-speed device (depending on STM32 support)
- 3 user LEDs
- 2 user and reset push-buttons
- 32.768 kHz crystal oscillator
- Board connectors:

> - USB with Micro-AB
> - Ethernet RJ45 (depending on STM32 support)
> - SWDST Zio connector including Arduino\* Uno V3ST
> - ST morpho expansion

- Flexible power-supply options: ST-LINK USB VBUS or external sources
- External or internal SMPS to generate Vcore logic supply
- On-board ST-LINK/V3 debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port
- USB OTG full speed or device only
- Comprehensive free software libraries and examples available with the
  STM32Cube MCU package.
- Arm\* Mbed Enabled\* compliant (only for some Nucleo part numbers)

More information about the board can be found at the [Nucleo H745ZI-Q website](https://www.st.com/en/evaluation-tools/nucleo-h745zi-q.html).

## Hardware

Nucleo H745ZI-Q provides the following hardware components:

- STM32H745ZI in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- ARM 32-bit Cortex-M4 CPU with FPU
- Chrom-ART Accelerator
- Hardware JPEG Codec
- 480 MHz max CPU frequency
- VDD from 1.62 V to 3.6 V
- 2 MB Flash
- 1 MB SRAM
- High-resolution timer (2.1 ns)
- 32-bit timers(2)
- 16-bit timers(12)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(4)
- UART(4)
- USB OTG Full Speed and High Speed(1)
- USB OTG Full Speed(1)
- CAN FD(2)
- SAI(2)
- SPDIF\_Rx(4)
- HDMI\_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO (up to 114) with external interrupt capability
- 16-bit ADC(3) with 36 channels / 3.6 MSPS
- 12-bit DAC with 2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution

### Supported Features

The `nucleo_h745zi_q` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_h745zi_q/stm32h745xx/m4` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7_dualcore.dtsi?plain=1#L11) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L852) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32H7 series FDCAN CAN FD controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L526) | [`st,stm32h7-fdcan`](../../../../build/dts/api/bindings/can/st,stm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) |
| Clock control | on-chip | STM32H7 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L153) | [`st,stm32h7-rcc`](../../../../build/dts/api/bindings/clock/st,stm32h7-rcc.md#std-dtcompatible-st-stm32h7-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L66) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L74) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L88) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7 main PLL[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L103) | [`st,stm32h7-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-pll-clock.md#std-dtcompatible-st-stm32h7-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L124) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L132) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L581) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L921) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L39) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L929) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| on-chip | STM32 BDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L955) | [`st,stm32-bdma`](../../../../build/dts/api/bindings/dma/st,stm32-bdma.md#std-dtcompatible-st-stm32-bdma) |
| on-chip | STM32 DMAMUX controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L968) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Ethernet | on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1028) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L144) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L373) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L484) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q.dtsi?plain=1#L24) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L164) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| IPM | on-chip | STM32 HSEM MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7_dualcore.dtsi?plain=1#L19) | [`st,stm32-hsem-mailbox`](../../../../build/dts/api/bindings/ipm/st,stm32-hsem-mailbox.md#std-dtcompatible-st-stm32-hsem-mailbox) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q.dtsi?plain=1#L12) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1038) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L78) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-chip | STM32H7 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1046) | [`st,stm32h7-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32h7-fmc.md#std-dtcompatible-st-stm32h7-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1052) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| MMC | on-chip | STM32 SDMMC Disk Access[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1008) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L22) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L125) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L558) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1068) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L158) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1000) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L362) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1088) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1100) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1106) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L288) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L344)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L312) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L353) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1114) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L421)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L432) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L92) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[14 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L548) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L834) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L49) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L63) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1078) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st,stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L274) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L280) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

#### `nucleo_h745zi_q/stm32h745xx/m7` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L35) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32 ADC[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L852) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32H7 series FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L526)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L537) | [`st,stm32h7-fdcan`](../../../../build/dts/api/bindings/can/st,stm32h7-fdcan.md#std-dtcompatible-st-stm32h7-fdcan) |
| Clock control | on-chip | STM32H7 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L153) | [`st,stm32h7-rcc`](../../../../build/dts/api/bindings/clock/st,stm32h7-rcc.md#std-dtcompatible-st-stm32h7-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L66) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L74)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L81) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L88) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L103)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L110) | [`st,stm32h7-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-pll-clock.md#std-dtcompatible-st-stm32h7-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L124) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L132) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L581) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L921) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L39) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L929) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| on-chip | STM32 BDMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L955) | [`st,stm32-bdma`](../../../../build/dts/api/bindings/dma/st,stm32-bdma.md#std-dtcompatible-st-stm32-bdma) |
| on-chip | STM32 DMAMUX controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L968) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Ethernet | on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1028) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q_stm32h745xx_m7.dts?plain=1#L125) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L144) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L373)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L385) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L484) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q.dtsi?plain=1#L24) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L164) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| IPM | on-chip | STM32 HSEM MAILBOX[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7_dualcore.dtsi?plain=1#L19) | [`st,stm32-hsem-mailbox`](../../../../build/dts/api/bindings/ipm/st,stm32-hsem-mailbox.md#std-dtcompatible-st-stm32-hsem-mailbox) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q.dtsi?plain=1#L12) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h745zi_q/nucleo_h745zi_q_stm32h745xx_m7.dts?plain=1#L32) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1038) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L78) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| on-chip | STM32H7 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1046) | [`st,stm32h7-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32h7-fmc.md#std-dtcompatible-st-stm32h7-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1052) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| MMC | on-chip | STM32 SDMMC Disk Access[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1008) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L42) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L15) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L125) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L712)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L558) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1068) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L158) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1000) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L362) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1088) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1100) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1106) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L304)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L288) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L312) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L353) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1114) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L421)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L432) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L92) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L702)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L548) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L834) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L49) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h745.dtsi?plain=1#L63) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L1078) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st,stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L274) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7/stm32h7.dtsi?plain=1#L280) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00499171-stm32h7-nucleo144-boards-mb1363-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo H745ZI board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PE1
- LD3 : PB14
- I2C : PB8, PB9
- SPI : PA5, PA6, PB5, PD14

#### System Clock

Nucleo H745ZI-Q System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 480MHz, driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo H745ZI-Q board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to UART3. Default settings are 115200 8N1.

#### Resources sharing

The dual core nature of STM32H745 SoC requires sharing HW resources between the
two cores. This is done in 3 ways:

- **Compilation**: Clock configuration is only accessible to M7 core. M4 core only
  has access to bus clock activation and deactivation.
- **Static pre-compilation assignment**: Peripherals such as a UART are assigned in
  devicetree before compilation. The user must ensure peripherals are not assigned
  to both cores at the same time.
- **Run time protection**: Interrupt-controller and GPIO configurations could be
  accessed by both cores at run time. Accesses are protected by a hardware semaphore
  to avoid potential concurrent access issues.

## Programming and Debugging

Nucleo H745ZI-Q board includes an ST-LINK/V3 embedded debug tool interface.

Applications for the `nucleo_h745zi_q` board should be built per core target,
using either `nucleo_h745zi_q/stm32h745xx/m7` or `nucleo_h745zi_q/stm32h745xx/m4`
as the target (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

Note

Check if the board’s ST-LINK V3 has the newest FW version. It can be updated
using [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html).

### Flashing

Flashing operation will depend on the target to be flashed and the SoC
option bytes configuration.

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner
for both cores, so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.
The target core is detected automatically.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

It is advised to use [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) to check and update option bytes
configuration.

By default:

> - CPU0 (Cortex-M7) boot address is set to 0x80000000 (OB: BOOT\_CM7\_ADD0)
> - CPU1 (Cortex-M4) boot address is set to 0x81000000 (OB: BOOT\_CM4\_ADD0)

Also, default out of the box board configuration enables CM7 and CM4 boot when
board is powered (Option bytes BCM7 and BCM4 are checked).
In that configuration, Kconfig boot option `STM32H7_BOOT_CM4_CM7` should be selected.
Zephyr flash configuration has been set to meet these default settings.

#### Flashing an application to STM32H745ZI M7 Core

First, connect the NUCLEO-H745ZI-Q to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your NUCLEO-H745ZI-Q board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

or use screen:

```shell
$ screen /dev/ttyACM0 115200
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_h745zi_q/stm32h745xx/m7 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_h745zi_q_m7
```

Note

Sometimes, flashing is not working. It is necessary to erase the flash
(with STM32CubeProgrammer for example) to make it work again.

Similarly, you can build and flash samples on the M4 target. For this, please
take care of the resource sharing (UART port used for console for instance).

Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application on M4 core.

```shell
# From the root of the zephyr repository
west build -b nucleo_h745zi_q/stm32h745xx/m4 samples/basic/blinky
west flash
```

Note

Flashing both M4 and M7 and pushing RESTART button on the board leads
to LD1 and LD2 flashing simultaneously.

### Debugging

You can debug an application on Cortex M7 side in the usual way. Here is an example
for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h745zi_q/stm32h745xx/m7 samples/hello_world
west debug
```

Debugging a Zephyr application on Cortex M4 side with west is currently not available.
As a workaround, you can use [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html).
