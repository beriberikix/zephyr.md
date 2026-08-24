---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_f746zg/doc/index.html
original_path: boards/st/nucleo_f746zg/doc/index.html
---

# Nucleo F746ZG

Board Overview

[![../../../../_images/nucleo_f746zg.jpg](https://docs.zephyrproject.org/4.1.0/_images/nucleo_f746zg.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/nucleo_f746zg.jpg)

Nucleo F746ZG

Name:
:   `nucleo_f746zg`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32f746xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_f746zg/doc/index.rst/../..)

## Overview

The STM32 Nucleo-144 boards offer combinations of performance and power that
provide an affordable and flexible way for users to build prototypes and try
out new concepts. For compatible boards, the SMPS significantly reduces power
consumption in Run mode.

The Arduino-compatible ST Zio connector expands functionality of the Nucleo
open development platform, with a wide choice of specialized Arduino\* Uno V3
shields.

The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK/V2-1 debugger/programmer.

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
> - SWD
> - Ethernet RJ45 (depending on STM32 support)
> - ST Zio connector including Arduino\* Uno V3
> - ST morpho

- Flexible power-supply options: ST-LINK USB VBUS or external sources.
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port.
- Comprehensive free software libraries and examples available with the
  STM32Cube MCU package.
- Arm\* Mbed Enabled\* compliant (only for some Nucleo part numbers)

More information about the board can be found at the [Nucleo F746ZG website](https://www.st.com/en/evaluation-tools/nucleo-f746zg.html).

## Hardware

Nucleo F746ZG provides the following hardware components:

- STM32F746ZG in LQFP144 package
- ARM 32-bit Cortex-M7 CPU with FPU
- Chrom-ART Accelerator
- ART Accelerator
- 216 MHz max CPU frequency
- VDD from 1.7 V to 3.6 V
- 1 MB Flash
- 320 KB SRAM
- 16-bit timers(10)
- 32-bit timers(2)
- SPI(6)
- I2C(4)
- I2S (3)
- USART(4)
- UART(4)
- USB OTG Full Speed and High Speed(1)
- USB OTG Full Speed(1)
- CAN(2)
- SAI(2)
- SPDIF\_Rx(4)
- HDMI\_CEC(1)
- Dual Mode Quad SPI(1)
- Camera Interface
- GPIO(up to 168) with external interrupt capability
- 12-bit ADC(3) with 24 channels / 2.4 MSPS
- 12-bit DAC with 2 channels(2)
- True Random Number Generator (RNG)
- 16-channel DMA
- LCD-TFT Controller with XGA resolution

### Supported Features

The `nucleo_f746zg` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_f746zg/stm32f746xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L34) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32F4 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L752)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L769) | [`st,stm32f4-adc`](../../../../build/dts/api/bindings/adc/st,stm32f4-adc.md#std-dtcompatible-st-stm32f4-adc) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L412)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f745.dtsi?plain=1#L69) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L135) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L56) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L77)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L62) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L69) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32F7 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L84) | [`st,stm32f7-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32f7-pll-clock.md#std-dtcompatible-st-stm32f7-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L92) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L454) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L803) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-chip | STM32 LCD-TFT display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f746.dtsi?plain=1#L14) | [`st,stm32-ltdc`](../../../../build/dts/api/bindings/display/st,stm32-ltdc.md#std-dtcompatible-st-stm32-ltdc) |
| DMA | on-chip | STM32 DMA controller (V1)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L820)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L811) | [`st,stm32-dma-v1`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v1.md#std-dtcompatible-st-stm32-dma-v1) |
| Ethernet | on-chip | ST STM32 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f745.dtsi?plain=1#L78) | [`st,stm32-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet.md#std-dtcompatible-st-stm32-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L118) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L167) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f746zg/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L326)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L350) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f746zg/nucleo_f746zg.dts?plain=1#L49) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L146) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_f746zg/nucleo_f746zg.dts?plain=1#L33) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L104) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (SDRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L110) | [`st,stm32-fmc-sdram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-sdram.md#std-dtcompatible-st-stm32-fmc-sdram) |
| on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L745) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L839) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L41) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L894) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L161) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L431)[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L448) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L857) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L140) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L830) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L735) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L868) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L879) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L887) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L272)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L254) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L281) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L904) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L362)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L372) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L421)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L438) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L707) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L721) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st,stm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L240) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/f7/stm32f7.dtsi?plain=1#L246) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00244518.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo F746ZG board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART\_2 TX/RX/RTS/CTS : PD5/PD6/PD4/PD3
- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- UART\_6 TX/RX : PG14/PG9 (Arduino UART)
- USER\_PB : PC13
- LD1 : PB0
- LD2 : PB7
- LD3 : PB14
- ETH : PA1, PA2, PA7, PB13, PC1, PC4, PC5, PG11, PG13
- USB DM : PA11
- USB DP : PA12
- I2C : PB8, PB9
- PWM : PE13
- SPI : PD14, PA5, PA6, PA7
- ADC1\_IN0 : PA0
- DAC1\_OUT1 : PA4

Note. The Arduino Uno v3 specified SPI device conflicts with the on-board ETH
device on pin PA7.

#### System Clock

Nucleo F746ZG System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 72MHz, driven by an 8MHz high-speed external clock.

#### Serial Port

Nucleo F746ZG board has 4 UARTs and 4 USARTs. The Zephyr console output is
assigned to UART3. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB156` jumper on the back side of the board.

## Programming and Debugging

Nucleo F746ZG board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_f746zg` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to Nucleo F746ZG

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_f746zg samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_f746zg
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_f746zg samples/hello_world
west debug
```
