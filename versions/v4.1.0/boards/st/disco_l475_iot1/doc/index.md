---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/disco_l475_iot1/doc/index.html
original_path: boards/st/disco_l475_iot1/doc/index.html
---

# Disco L475 IOT01 (B-L475E-IOT01A)

Board Overview

[![../../../../_images/disco_l475_iot1.jpg](https://docs.zephyrproject.org/4.1.0/_images/disco_l475_iot1.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/disco_l475_iot1.jpg)

Disco L475 IOT01 (B-L475E-IOT01A)

Name:
:   `disco_l475_iot1`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l475xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/disco_l475_iot1/doc/index.rst/../..)

## Overview

The B-L475E-IOT01A Discovery kit for IoT node allows users to develop
applications with direct connection to cloud servers.
The Discovery kit enables a wide diversity of applications by exploiting
low-power communication, multiway sensing and ARM® Cortex®-M4 core-based
STM32L4 Series features.

This kit provides:

- 64-Mbit Quad-SPI (Macronix) Flash memory
- Bluetooth® V4.1 module (SPBTLE-RF)
- Sub-GHz (868 or 915 MHz) low-power-programmable RF module (SPSGRF-868 or SPSGRF-915)
- Wi-Fi® module Inventek ISM43362-M3G-L44 (802.11 b/g/n compliant)
- Dynamic NFC tag based on M24SR with its printed NFC antenna
- 2 digital omni-directional microphones (MP34DT01)
- Capacitive digital sensor for relative humidity and temperature (HTS221)
- High-performance 3-axis magnetometer (LIS3MDL)
- 3D accelerometer and 3D gyroscope (LSM6DSL)
- 260-1260 hPa absolute digital output barometer (LPS22HB)
- Time-of-Flight and gesture-detection sensor (VL53L0X)
- 2 push-buttons (user and reset)
- USB OTG FS with Micro-AB connector
- Expansion connectors:
  :   - Arduino™ Uno V3
      - PMOD
- Flexible power-supply options:
  :   - ST LINK USB VBUS or external sources
- On-board ST-LINK/V2-1 debugger/programmer with USB re-enumeration capability:
  :   - mass storage, virtual COM port and debug port

More information about the board can be found at the [Disco L475 IoT1 website](https://www.st.com/content/st_com/en/products/evaluation-tools/product-evaluation-tools/mcu-eval-tools/stm32-mcu-eval-tools/stm32-mcu-discovery-kits/b-l475e-iot01a.html).

## Hardware

The STM32L475VG SoC provides the following hardware IPs:

- Ultra-low-power with FlexPowerControl (down to 120 nA Standby mode and 100 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, frequency up to 80 MHz, 100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:
  :   - 4 to 48 MHz crystal oscillator
      - 32 kHz crystal oscillator for RTC (LSE)
      - Internal 16 MHz factory-trimmed RC ( ±1%)
      - Internal low-power 32 kHz RC ( ±5%)
      - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
        LSE (better than ±0.25 % accuracy)
      - 3 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- Up to 24 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 16x timers:
  :   - 2x 16-bit advanced motor-control
      - 2x 32-bit and 5x 16-bit general purpose
      - 2x 16-bit basic
      - 2x low-power 16-bit timers (available in Stop mode)
      - 2x watchdogs
      - SysTick timer
- Up to 114 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Memories
  :   - Up to 1 MB Flash, 2 banks read-while-write, proprietary code readout protection
      - Up to 128 KB of SRAM including 32 KB with hardware parity check
      - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
      - Quad SPI memory interface
- 4x digital filters for sigma delta modulator
- Rich analog peripherals (independent supply)
  :   - 2x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200 uA/MSPS
      - 2x 12-bit DAC, low-power sample and hold
      - 2x operational amplifiers with built-in PGA
      - 2x ultra-low-power comparators
- 18x communication interfaces
  :   - USB OTG 2.0 full-speed, LPM and BCD
      - 2x SAIs (serial audio interface)
      - 3x I2C FM+(1 Mbit/s), SMBus/PMBus
      - 6x USARTs (ISO 7816, LIN, IrDA, modem)
      - 3x SPIs (4x SPIs with the Quad SPI)
      - CAN (2.0B Active) and SDMMC interface
      - SWPMI single wire protocol master I/F
- 14-channel DMA controller
- True random number generator
- CRC calculation unit, 96-bit unique ID
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L475VG can be found here:
:   - [STM32L475VG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l475vg.html)
    - [STM32L475 reference manual](https://www.st.com/resource/en/reference_manual/dm00083560.pdf)

### Supported Features

The `disco_l475_iot1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `disco_l475_iot1/stm32l475xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L397)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L413) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V1 compatible with BlueNRG-MS devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L199) | [`st,hci-spi-v1`](../../../../build/dts/api/bindings/bluetooth/st,hci-spi-v1.md#std-dtcompatible-st-hci-spi-v1) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L228) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L136) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L102) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L110) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L320) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L247) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L429)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L439) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 QSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L325) | [`st,stm32-qspi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-qspi-nor.md#std-dtcompatible-st-stm32-qspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L168) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L242) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L147) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L49) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L265) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L237) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L220) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l475.dtsi?plain=1#L28) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L162) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L483) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L314)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L297) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| QSPI | on-chip | STM32 QSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L266) | [`st,stm32-qspi`](../../../../build/dts/api/bindings/qspi/st,stm32-qspi.md#std-dtcompatible-st-stm32-qspi) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L471) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L386) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics LIS3MDL magnetometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L145) | [`st,lis3mdl-magn`](../../../../build/dts/api/bindings/sensor/st,lis3mdl-magn.md#std-dtcompatible-st-lis3mdl-magn) |
| on-board | STMicroelectronics HTS221 humidity and temperature sensor on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L150) | [`st,hts221`](../../../../build/dts/api/compatibles/st,hts221.md#std-dtcompatible-st-hts221) |
| on-board | STMicroelectronics LPS22HB pressure sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L156) | [`st,lps22hb-press`](../../../../build/dts/api/bindings/sensor/st,lps22hb-press.md#std-dtcompatible-st-lps22hb-press) |
| on-board | STMicroelectronics LSM6DSL 6-axis accelerometer and gyrometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L161) | [`st,lsm6dsl`](../../../../build/dts/api/compatibles/st,lsm6dsl.md#std-dtcompatible-st-lsm6dsl) |
| on-board | STMicroelectronics VL53L0X Time of Flight sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L167) | [`st,vl53l0x`](../../../../build/dts/api/bindings/sensor/st,vl53l0x.md#std-dtcompatible-st-vl53l0x) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L517) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L528) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L536) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L215)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L224) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L233) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L57)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L66) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L543) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L276)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l471.dtsi?plain=1#L87) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L304)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L287) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L449)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L460) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l475.dtsi?plain=1#L13) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L201) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L207) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| Wi-Fi | on-board | es-WiFi module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/disco_l475_iot1/disco_l475_iot1.dts?plain=1#L208) | [`inventek,eswifi`](../../../../build/dts/api/bindings/wifi/inventek,eswifi.md#std-dtcompatible-inventek-eswifi) |

### Connections and IOs

Disco L475 IoT Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

Note that LED LD1 and SPI1 SCK use the same GPIO pin and cannot be used simultaneously.

#### Available pins:

For detailed information about available pins please refer to [STM32 Disco L475 IoT1 board User Manual](https://www.st.com/resource/en/user_manual/dm00347848.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PB6/PB7 (ST-Link Virtual Port Com)
- UART\_4 TX/RX : PA0/PA1 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C2 SCL/SDA : PB10/PB11 (Sensor I2C bus)
- I2C3 SCL/SDA : PC0/PC1
- SPI1 NSS/SCK/MISO/MOSI : PA2/PA5/PA6/PA7 (Arduino SPI)
- SPI3 SCK/MISO/MOSI : PC10/PC11/PC12 (BT SPI bus)
- PWM\_2\_CH1 : PA15
- PWM\_15\_CH1 : PB14 (LD2)
- USER\_PB : PC13
- LD1 : PA5 (same as SPI1 SCK)
- LD2 : PB14
- ADC12\_IN5 : PA0
- ADC123\_IN3 : PC2
- ADC123\_IN4 : PC3
- ADC12\_IN13 : PC4
- ADC12\_IN14 : PC5
- DAC1\_OUT1 : PA4

#### System Clock

Disco L475 IoT System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

Disco L475 IoT board has 6 U(S)ARTs. The Zephyr console output is assigned to UART1.
Default settings are 115200 8N1.

## Programming and Debugging

Disco L475 IoT board includes an ST-LINK/V2-1 embedded debug tool interface.

Applications for the `disco_l475_iot1` board configuration can be built and
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

#### Flashing an application to Disco L475 IoT

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Connect the Disco L475 IoT to your host computer using the USB port, then
run a serial host program to connect with your Nucleo board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application:

```shell
# From the root of the zephyr repository
west build -b disco_l475_iot1 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b disco_l475_iot1 samples/hello_world
west debug
```
