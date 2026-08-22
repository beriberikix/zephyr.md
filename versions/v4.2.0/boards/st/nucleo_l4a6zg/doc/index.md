---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_l4a6zg/doc/index.html
original_path: boards/st/nucleo_l4a6zg/doc/index.html
---

# Nucleo L4A6ZG

Board Overview

Name:
:   `nucleo_l4a6zg`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l4a6xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_l4a6zg/doc/index.rst/../..)

## Overview

The Nucleo L4A6ZG board features an ARM Cortex-M4 based STM32L4A6ZG MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the Nucleo L4A6ZG board:

- STM32 microcontroller in QFP144 package
- USB OTG FS with Micro-AB connector
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V2-1 debugger/programmer with SWD connector
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - Power management access point
- 8 LEDs: user LEDs (LD1, LD2, LD3), communication LED (LD4), USB
  power fault(LD5), power LED (LD6), USB FS OTG (LD7, LD8)
- 2 push buttons: USER and RESET

More information about the board can be found at the [Nucleo L4A6ZG website](https://www.st.com/en/evaluation-tools/nucleo-l4a6zg.html).

## Hardware

The STM32L4A6ZG SoC provides the following hardware capabilities:

- Ultra-low-power with FlexPowerControl (down to 108 nA Standby mode and 91 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, frequency up to 80 MHz, 100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 3 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- LCD 8 x 40 or 4 x 44 with step-up converter
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 16x timers:

  - 2x 16-bit advanced motor-control
  - 2x 32-bit and 5x 16-bit general purpose
  - 2x 16-bit basic
  - 2x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - SysTick timer
- Up to 136 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Memories

  - Up to 1 MB Flash, 2 banks read-while-write, proprietary code readout protection
  - Up to 320 KB of SRAM including 64 KB with hardware parity check
  - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
  - Quad SPI memory interface
- 4x digital filters for sigma delta modulator
- Rich analog peripherals (independent supply)

  - 3x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200 uA/MSPS
  - 2x 12-bit DAC, low-power sample and hold
  - 2x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
- 20x communication interfaces

  - USB OTG 2.0 full-speed, LPM and BCD
  - 2x SAIs (serial audio interface)
  - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 5x U(S)ARTs (ISO 7816, LIN, IrDA, modem)
  - 1x LPUART
  - 3x SPIs (4x SPIs with the Quad SPI)
  - 2x CAN (2.0B Active) and SDMMC interface
  - SWPMI single wire protocol master I/F
  - IRTIM (Infrared interface)
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- AES and HASH hardware accelerators
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L4A6ZG can be found here:

- [STM32L4A6ZG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l4a6zg.html)
- [STM32L4A6 reference manual](https://www.st.com/resource/en/reference_manual/dm00083560.pdf)

### Supported Features

The `nucleo_l4a6zg` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_l4a6zg/stm32l4a6xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L397) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 CAN controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L228) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L136) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L73)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l496.dtsi?plain=1#L12) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L102) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L110) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L320) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32L4 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4a6.dtsi?plain=1#L13) | [`st,stm32l4-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32l4-aes.md#std-dtcompatible-st-stm32l4-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L247) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L429) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L168) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l4a6zg/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L242)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L254) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l4a6zg/nucleo_l4a6zg.dts?plain=1#L51) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L147) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l4a6zg/nucleo_l4a6zg.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_l4a6zg/nucleo_l4a6zg.dts?plain=1#L43) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L265) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L237) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l475.dtsi?plain=1#L28) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L162) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L483) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L352)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L297) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L266) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st%2Cstm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L471) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L386) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L517) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L528) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L536) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L48)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L215) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L233) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L57) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L543) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L276)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L87) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L342)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L287) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L449) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l475.dtsi?plain=1#L13) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L201) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L207) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo L4A6ZG Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/dm00368330.pdf).

#### Default Zephyr Peripheral Mapping:

- LPUART\_1 TX/RX : PG7/PG8 (ST-Link Virtual COM Port)
- UART\_3 TX/RX : PD8/PD9 (Arduino Serial)
- I2C\_1 SCL/SDA : PB8/PB7 (Arduino I2C)
- SPI\_1 SCK/MISO/MOSI/NSS : PA5/PA6/PA7/PD14 (Arduino SPI)
- USER\_PB : PC13
- PWM\_15\_CH1 : PB14 (Red LED)
- LD1 : PC7 (Green LED)
- LD2 : PB7 (Blue LED)
- LD3 : PB14 (Red LED)

#### System Clock

Nucleo L4A6ZG system clock could be driven by internal or external oscillator,
as well as main PLL clock. By default, system clock is driven by PLL at 80MHz, which is
driven by 16MHz high speed internal oscillator (HSI). High speed external oscillator
(HSE) is not soldered on the board, so it cannot be used to drive the PLL.

#### Serial Port

Nucleo L4A6ZG board has 5 UARTs. The Zephyr console output is assigned to LPUART1,
which is connected to the onboard ST-LINK/V2-1. Virtual COM port interface.
Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_l4a6zg` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo L4A6ZG board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `nucleo_l4a6zg` board configuration can be built and
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

#### Flashing an application to Nucleo L4A6ZG

Connect the Nucleo L4A6ZG to your host computer using the ST-LINK USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyUSB0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l4a6zg samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_l4a6zg
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_l4a6zg samples/hello_world
west debug
```
