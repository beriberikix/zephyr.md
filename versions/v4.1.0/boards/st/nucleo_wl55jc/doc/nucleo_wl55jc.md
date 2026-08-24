---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.html
original_path: boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.html
---

# Nucleo WL55JC

Board Overview

[![../../../../_images/nucleo_wl55jc.jpg](https://docs.zephyrproject.org/4.1.0/_images/nucleo_wl55jc.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/nucleo_wl55jc.jpg)

Nucleo WL55JC

Name:
:   `nucleo_wl55jc`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32wl55xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_wl55jc/doc/nucleo_wl55jc.rst/../..)

## Overview

The NUCLEO-WL55JC STM32WL Nucleo-64 board provides an affordable and flexible
way for users to try out new concepts and build prototypes with the STM32WL
Series microcontroller, choosing from the various combinations of performance,
power consumption, and features.

- STM32WL55JC microcontroller multiprotocol LPWAN dual-core 32-bit
  (Arm® Cortex®-M4/M0+ at 48 MHz) in UFBGA73 package featuring:

  - Ultra-low-power MCU
  - RF transceiver (150 MHz to 960 MHz frequency range) supporting LoRa®,
    (G)FSK, (G)MSK, and BPSK modulations
  - 256-Kbyte Flash memory and 64-Kbyte SRAM
- 3 user LEDs
- 3 user buttons and 1 reset push-button
- 32.768 kHz LSE crystal oscillator
- 32 MHz HSE on-board oscillator
- Board connectors:

  - USB with Micro-B
  - MIPI debug connector
  - ARDUINO Uno V3 expansion connector
  - ST morpho extension pin headers for full access to all STM32WL I/Os
- Delivered with SMA antenna
- Flexible power-supply options: ST-LINK, USB VBUS, or external sources
- On-board STLINK-V3 debugger/programmer with USB re-enumeration capability:
  mass storage, Virtual COM port, and debug port
- Comprehensive free software libraries and examples available with the
  STM32CubeWL MCU Package
- Suitable for rapid prototyping of end nodes based on LoRaWAN, Sigfox, wM-Bus,
  and many other proprietary protocols
- Fully open hardware platform

More information about the board can be found at the [Nucleo WL55JC website](https://www.st.com/en/evaluation-tools/nucleo-wl55jc.html).

## Hardware

The STM32WL55JC long-range wireless and ultra-low-power devices embed a powerful
and ultra-low-power LPWAN-compliant radio solution, enabling the following
modulations: LoRa®, (G)FSK, (G)MSK, and BPSK
It provides the following hardware capabilities:

- Radio

  - Frequency range: 150 MHz to 960 MHz
  - Modulation: LoRa®, (G)FSK, (G)MSK and BPSK
  - RX sensitivity: –123 dBm for 2-FSK(at 1.2 Kbit/s), –148 dBm for LoRa®
    (at 10.4 kHz, spreading factor 12)
  - Transmitter high output power, programmable up to +22 dBm
  - Transmitter low output power, programmable up to +15 dBm
  - Compliant with the following radio frequency regulations such as
    ETSI EN 300 220, EN 300 113, EN 301 166, FCC CFR 47 Part 15, 24, 90, 101
    and the Japanese ARIB STD-T30, T-67, T-108
  - Compatible with standardized or proprietary protocols such as LoRaWAN®,
    Sigfox™, W-MBus and more (fully open wireless system-on-chip)
- Core

  - 32-bit Arm® Cortex®-M4 CPU

    - Adaptive real-time accelerator (ART Accelerator) allowing 0-wait-state
      execution from Flash memory, frequency up to 48 MHz, MPU
      and DSP instructions
    - 1.25 DMIPS/MHz (Dhrystone 2.1)
  - 32-bit Arm®Cortex®-M0+ CPU

    - Frequency up to 48 MHz, MPU
    - 0.95 DMIPS/MHz (Dhrystone 2.1)
- Security and identification

  - Hardware encryption AES 256-bit
  - True random number generator (RNG)
  - Sector protection against read/write operations (PCROP, RDP, WRP)
  - CRC calculation unit
  - Unique device identifier (64-bit UID compliant with IEEE 802-2001 standard)
  - 96-bit unique die identifier
  - Hardware public key accelerator (PKA)
  - Key management services
  - Secure sub-GHz MAC layer
  - Secure firmware update (SFU)
  - Secure firmware install (SFI)
- Supply and reset management

  - High-efficiency embedded SMPS step-down converter
  - SMPS to LDO smart switch
  - Ultra-safe, low-power BOR (brownout reset) with 5 selectable thresholds
  - Ultra-low-power POR/PDR
  - Programmable voltage detector (PVD)
  - VBAT mode with RTC and 20x32-byte backup registers
- Clock sources

  - 32 MHz crystal oscillator
  - TCXO support: programmable supply voltage
  - 32 kHz oscillator for RTC with calibration
  - High-speed internal 16 MHz factory trimmed RC (± 1 %)
  - Internal low-power 32 kHz RC
  - Internal multi-speed low-power 100 kHz to 48 MHz RC
  - PLL for CPU, ADC and audio clocks
- Memories

  - 256-Kbyte Flash memory
  - 64-Kbyte RAM
  - 20x32-bit backup register
  - Bootloader supporting USART and SPI interfaces
  - OTA (over-the-air) firmware update capable
  - Sector protection against read/write operations
- Rich analog peripherals (down to 1.62 V)

  - 12-bit ADC 2.5 Msps, up to 16 bits with hardware oversampling,
    conversion range up to 3.6 V
  - 12-bit DAC, low-power sample-and-hold
  - 2x ultra-low-power comparators
- System peripherals

  - Mailbox and semaphores for communication between Cortex®-M4 and Cortex®-M0+
    firmware
- Controllers

  - 2x DMA controller (7 channels each) supporting ADC, DAC, SPI, I2C, LPUART,
    USART, AES and timers
  - 2x USART (ISO 7816, IrDA, SPI)
  - 1x LPUART (low-power)
  - 2x SPI 16 Mbit/s (1 over 2 supporting I2S)
  - 3x I2C (SMBus/PMBus™)
  - 2x 16-bit 1-channel timer
  - 1x 16-bit 4-channel timer (supporting motor control)
  - 1x 32-bit 4-channel timer
  - 3x 16-bit ultra-low-power timer
  - 1x RTC with 32-bit sub-second wakeup counter
  - 1x independent SysTick
  - 1x independent watchdog
  - 1x window watchdog
- Up to 43 I/Os, most 5 V-tolerant
- Development support
  - Serial-wire debug (SWD), JTAG
  - Dual CPU cross trigger capabilities

More information about STM32WL55JC can be found here:

- [STM32WL55JC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32wl55jc.html)
- [STM32WL55JC datasheet](https://www.st.com/resource/en/datasheet/stm32wl55jc.pdf)
- [STM32WL55JC reference manual](https://www.st.com/resource/en/reference_manual/dm00451556-stm32wl5x-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf)

### Supported Features

The `nucleo_wl55jc` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_wl55jc/stm32wl55xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L31) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L344) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32WL RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L128) | [`st,stm32wl-rcc`](../../../../build/dts/api/bindings/clock/st,stm32wl-rcc.md#std-dtcompatible-st-stm32wl-rcc) |
| on-chip | STM32WL HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L65) | [`st,stm32wl-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32wl-hse-clock.md#std-dtcompatible-st-stm32wl-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32WB and STM32WL PLL node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L102) | [`st,stm32wb-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32wb-pll-clock.md#std-dtcompatible-st-stm32wb-pll-clock) |
| Counter | on-chip | STM32 counters[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L402) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L452) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L361) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L471) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L493) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L110) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L160) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on ST Morpho connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/st_morpho_connector.dtsi?plain=1#L10) | [`st-morpho-header`](../../../../build/dts/api/bindings/gpio/st-morpho-header.md#std-dtcompatible-st-morpho-header) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L281)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L269) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/nucleo_wl55jc.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L139) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/nucleo_wl55jc.dts?plain=1#L26) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| LoRa | on-chip | STM32WL Sub-GHz Radio[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L335) | [`st,stm32wl-subghz-radio`](../../../../build/dts/api/bindings/lora/st,stm32wl-subghz-radio.md#std-dtcompatible-st-stm32wl-subghz-radio) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L220) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L118) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_wl55jc/nucleo_wl55jc.dts?plain=1#L193) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L154) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L505) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L396)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L379) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L133) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L461) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L204) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L534) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L545) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L553) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L241) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L259) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L560) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L305)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L315) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| on-chip | STM32 SUBGHZ SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L325) | [`st,stm32-spi-subghz`](../../../../build/dts/api/bindings/spi/st,stm32-spi-subghz.md#std-dtcompatible-st-stm32-spi-subghz) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L60) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L193) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L386)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L369) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L227) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/wl/stm32wl.dtsi?plain=1#L233) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo WL55JC Board has 4 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

#### Default Zephyr Peripheral Mapping:

- LPUART\_1 TX/RX : PA3/PA2 (ST-Link Virtual Port Com)
- I2C\_2\_SCL : PA12 (Arduino I2C)
- I2C\_2\_SDA : PA11 (Arduino I2C)
- SPI\_1\_NSS : PA4 (arduino\_spi)
- SPI\_1\_SCK : PA5 (arduino\_spi)
- SPI\_1\_MISO : PA6 (arduino\_spi)
- SPI\_1\_MOSI : PA7 (arduino\_spi)
- ADC1\_IN5 : PB1 (Arduino pin A0)
- DAC1\_OUT1 : PA10 (Arduino pin A2)

#### System Clock

Nucleo WL55JC System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by HSE clock at
32MHz.

#### Serial Port

Nucleo WL55JC board has 2 (LP)U(S)ARTs. The Zephyr console output is assigned
to LPUART\_1.
Default settings are 115200 8N1.

## Programming and Debugging

Nucleo WL55JC board includes an STLINK-V3 embedded debug tool interface.

Applications for the `nucleo_wl55jc` board configuration can be built the
usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application)).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to Nucleo WL55JC

Connect the Nucleo WL55JC to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyUSB0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wl55jc samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_wl55jc samples/basic/blinky
west debug
```
