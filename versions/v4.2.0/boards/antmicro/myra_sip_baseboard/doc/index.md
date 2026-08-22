---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/antmicro/myra_sip_baseboard/doc/index.html
original_path: boards/antmicro/myra_sip_baseboard/doc/index.html
---

# Myra SiP Baseboard

Board Overview

[![../../../../_images/myra_sip_baseboard.webp](../../../../_images/myra_sip_baseboard.webp)
](../../../../_images/myra_sip_baseboard.webp)

Myra SiP Baseboard

Name:
:   `myra_sip_baseboard`

Vendor:
:   Antmicro

Architecture:
:   arm

SoC:
:   myra

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/antmicro/myra_sip_baseboard/doc/index.rst/../..)

## Overview

The Myra SiP Baseboard features Antmicro’s **Myra** SiP, which integrates the **STM32G491REI6** MCU,
128kB FRAM, and FTDI FT231XQ USB to UART converter. The board is equipped with temperature,
humidity, and pressure sensors, designed to help monitor conditions in server rooms.

The sensors are placed on a separate island that is detachable from the main PCB and can be
installed directly in the required place. It provides local storage for data logging and a battery
backup for protection against data loss. The board can be used as a building block for PoC solutions
for monitoring environmental parameters.

Key features include:

- STM32G491REI6 MCU (Cortex-M4, 170 MHz)
- 128 KB Fujitsu FRAM
- FTDI FT231XQ USB to UART converter
- 50 mm x 26.5 mm PCB
- USB-C Connector for data and power
- SHT45 temperature + humidity sensor
- BME280 temperature + humidity + pressure sensor
- QWIIC connectors for peripheral expansion
- RTC with battery backup

More information about the board can be found on [Antmicro’s Open Hardware Portal](https://openhardware.antmicro.com/boards/environment-sensor-sip-baseboard).

## Hardware

Myra SiP provides the following hardware:

- **STM32G491REI6 MCU**:

  - ARM Cortex-M4 CPU with FPU, up to 170 MHz
  - Clock Sources:

    - 4 to 48 MHz external crystal oscillator (HSE)
    - 32 kHz crystal oscillator for RTC (LSE)
    - Internal 16 MHz RC (±1%)
    - Internal low-power 32 kHz RC (±5%)
    - 2 PLLs for system clock, USB, audio, ADC
  - RTC: Real-time clock with hardware calendar, alarms, and calibration
  - Timers:

    - 1x 32-bit timer and 2x 16-bit timers with up to 4x IC/OC/PWM or pulse counter and quadrature
      (incremental) encoder input
    - 3x 16-bit advanced motor control timers with up to 8x PWM channels, dead time generation,
      emergency stop
    - 1x 16-bit timer with 2x IC/OC, one OCN/PWM, dead time generation, emergency stop
    - 2x watchdog timers (independent, window)
    - 2x 16-bit basic timers
    - SysTick timer
    - 1x low-power timer
  - I/Os: Up to 86 fast I/Os, most 5V tolerant
  - Memory:

    - 512 KB Flash memory with ECC and PCROP protection
    - 96 KB SRAM including 32 KB with hardware parity check
  - Analog peripherals:

    - 3x 16-bit ADCs with up to 36 channels, hardware oversampling, and resolution up to 16-bit
    - 4x 12-bit DAC channels
    - 4x ultra-fast rail-to-rail analog comparators
    - 4x operational amplifiers with built-in PGA
    - Internal temperature sensor and voltage reference with support for three output voltages
      (2.048 V, 2.5 V, 2.9 V)
  - Communication Interfaces:

    - 2x FDCAN controllers supporting flexible data rate
    - 3x I2C Fast Mode Plus (1 Mbit/s) with 20 mA current sink, SMBus/PMBus support
    - 5x USART/UART (ISO 7816, LIN, IrDA, modem control)
    - 1x LPUART
    - 3x SPI interfaces (2x with multiplexed half-duplex I²S)
    - 1x SAI (serial audio interface)
    - USB 2.0 full-speed with LPM and BCD support
    - IRTIM (infrared interface)
    - USB Type-C™ / USB Power Delivery (UCPD)
  - Other Peripherals:

    - 16-channel DMA controller
    - True Random Number Generator (RNG)
    - CRC calculation unit, 96-bit unique ID
    - Development support: SWD, JTAG, Embedded Trace Macrocell™
    - ECOPACK2® compliant packages
- **128 KB Fujitsu MB85RS1MT FRAM**: Local storage for data logging, allowing non-volatile memory storage.
- **FTDI FT231XQ USB to UART converter**: Provides a reliable USB to UART interface.

More information about STM32G491RE can be found here:

- [STM32G491RE on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32g491re.html)

### Other board’s peripherals:

- USB-C Connector: For data and power.
- SHT45 sensor:

  - Relative humidity accuracy: ±1.0% RH
  - Operating humidity range: 0-100% RH
  - Temperature accuracy: ±0.1°C
  - Operating temperature range: -40°C to 125°C
- BME280 sensor:

  - Relative humidity accuracy: ±3% RH
  - Temperature accuracy: ±1°C
  - Pressure accuracy: ±1 hPa
  - Operating temperature range: -40°C to 85°C
  - Pressure range: 300-1100 hPa
- QWIIC connectors: For easy peripheral expansion.

### Supported Features

The `myra_sip_baseboard` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `myra_sip_baseboard/myra` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L32) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L106)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L122) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L388)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g491.dtsi?plain=1#L13) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L173) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L60) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L73)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L66) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L80) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32G4 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L95) | [`st,stm32g4-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32g4-pll-clock.md#std-dtcompatible-st-stm32g4-pll-clock) |
| Counter | on-chip | STM32 counters[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L437) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L138)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L146) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L631) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L648) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L154) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L206) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L322)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L334) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L40) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L185) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L32) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L163) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L145) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| on-chip | Fujitsu MB85RSXX SPI FRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/antmicro/myra.dtsi?plain=1#L18) | [`fujitsu,mb85rsxx`](../../../../build/dts/api/bindings/mtd/fujitsu%2Cmb85rsxx.md#std-dtcompatible-fujitsu-mb85rsxx) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L694) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L200) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L442)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L420) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L179) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L609) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L598) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | BME280 integrated environmental sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L110) | [`bosch,bme280`](../../../../build/dts/api/compatibles/bosch%2Cbme280.md#std-dtcompatible-bosch-bme280) |
| on-board | Sensirion SHT4x humidity and temperature sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/antmicro/myra_sip_baseboard/myra_sip_baseboard.dts?plain=1#L115) | [`sensirion,sht4x`](../../../../build/dts/api/bindings/sensor/sensirion%2Csht4x.md#std-dtcompatible-sensirion-sht4x) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L668) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L679) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L687) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L263) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L290) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L299) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L699) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L368)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L358) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L659) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L399) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L427)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L410) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L617) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L308) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/g4/stm32g4.dtsi?plain=1#L314) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Antmicro’s Myra SiP Baseboard provides the following default pin mappings for peripherals:

- LPUART\_1\_TX : PA2
- LPUART\_1\_RX : PA3
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB9
- SPI\_CS2 : PB2
- SPI\_CS3 : PA7
- SPI\_2\_SCK : PB13
- SPI\_2\_MISO : PB14
- SPI\_2\_MOSI : PB15
- PWM\_2\_CH1 : PA5
- USER\_PB : PC13
- LD2 : PA5
- ADC1\_IN1 : PA0
- DAC1\_OUT1 : PA4
- USB\_MCU\_N : PA11
- USB\_MCU\_P : PA12
- SWDIO-JMTS : PA13
- SWCLK-JTCK : PA14
- JTDI : PA15
- JTDO : PB3
- JTRST : PB4
- FRAM\_HOLD (ACTIVE LOW) : PB10
- FRAM\_WP (ACTIVE LOW) : PB11
- FRAM\_CS (ACTIVE LOW) : PB12
- GPIO\_PC10 : PC10
- GPIO\_PC11 : PC11
- GPIO\_PC12 : PC12
- PF0\_OSC : PF0

### System Clock

System clock can be driven by an internal or an external oscillator, as well as by the main PLL
clock. By default, system clock is driven by PLL clock at 170MHz (boost mode selected), which in
turn, is driven by the 8MHz high speed external oscillator (HSE). While the HSE oscillator is
capable of operating at frequencies up to 48 MHz by default, in this configuration, it is
specifically set to 8 MHz.

### Serial Port

The Myra SiP Baseboard has 5 U(S)ARTs. The Zephyr console output is assigned to LPUART1. The default
settings are 115200 8N1.

## Programming and Debugging

The `myra_sip_baseboard` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `myra_sip_baseboard` board target can be built and flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and [Run an Application](../../../../develop/application/index.md#application-run) for more details).

## Flashing

This board has a USB-JTAG interface and can be used with OpenOCD.

Connect the Myra SiP Baseboard to your host computer using the USB port, then build and flash
the application. Here is an example for [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.").

```shell
# From the root of the zephyr repository
west build -b myra_sip_baseboard samples/hello_world
west flash
```

Then run a serial host program to connect with the Myra SiP Baseboard, e.g. using picocom:

```shell
$ picocom /dev/ttyUSB0 -b 115200
```

Warning

The board has only one port that is used for both programming and the console. For this reason, it is
recommended to set `CONFIG_BOOT_DELAY` to an arbitrary value. This is especially important when
running twister tests on the device. You should then also use the `--flash-before` and
`--device-flash-timeout=120` options:

```shell
$ scripts/twister --device-testing --device-serial /dev/ttyUSB0 --device-serial-baud 115200 -p myra_sip_baseboard --flash-before --device-flash-timeout=120 -v
```

## Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b myra_sip_baseboard samples/hello_world
west debug
```
