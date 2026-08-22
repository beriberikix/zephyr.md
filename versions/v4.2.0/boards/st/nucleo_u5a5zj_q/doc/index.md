---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_u5a5zj_q/doc/index.html
original_path: boards/st/nucleo_u5a5zj_q/doc/index.html
---

# Nucleo U5A5ZJ Q

Board Overview

Name:
:   `nucleo_u5a5zj_q`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u5a5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_u5a5zj_q/doc/index.rst/../..)

## Overview

The Nucleo U5A5ZJ Q board, featuring an ARM Cortex-M33 based STM32U5A5ZJ MCU,
provides an affordable and flexible way for users to try out new concepts and
build prototypes by choosing from the various combinations of performance and
power consumption features. Here are some highlights of the Nucleo U5A5ZJ Q
board:

- STM32U5A5ZJ microcontroller in LQFP144 package
- Internal SMPS to generate V core logic supply
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32 I/Os
- On-board ST-LINK/V3E debugger/programmer
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
  - ST-Link V3E
- Three users LEDs
- Two push-buttons: USER and RESET
- USB Type-C ™ Sink device FS

## Hardware

The STM32U5A5xx devices are an ultra-low-power microcontrollers family (STM32U5
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 160 MHz.

- Includes ST state-of-the-art patented technology
- Ultra-low-power with FlexPowerControl:

  - 1.71 V to 3.6 V power supply
  - -40 °C to +85/125 °C temperature range
  - Low-power background autonomous mode (LPBAM): autonomous peripherals with
    DMA, functional down to Stop 2 mode
  - VBAT mode: supply for RTC, 32 x 32-bit backup registers and 2-Kbyte backup SRAM
  - 150 nA Shutdown mode (24 wake-up pins)
  - 195 nA Standby mode (24 wake-up pins)
  - 480 nA Standby mode with RTC
  - 2 µA Stop 3 mode with 40-Kbyte SRAM
  - 8.2 µA Stop 3 mode with 2.5-Mbyte SRAM
  - 4.65 µA Stop 2 mode with 40-Kbyte SRAM
  - 17.5 µA Stop 2 mode with 2.5-Mbyte SRAM
  - 18.5 µA/MHz Run mode at 3.3 V
- Core:

  - Arm® 32-bit Cortex®-M33 CPU with TrustZone®, MPU, DSP,
    and FPU ART Accelerator
  - 32-Kbyte ICACHE allowing 0-wait-state execution from flash and external
    memories: frequency up to 160 MHz, 240 DMIPS
  - 16-Kbyte DCACHE1 for external memories
- Power management:

  - Embedded regulator (LDO) and SMPSstep-down converter supporting switch
    on-the-fly and voltage scaling
- Benchmarks:

  - 1.5 DMIPS/MHz (Drystone 2.1)
  - 655 CoreMark® (4.09 CoreMark®/MHz)
  - 369 ULPMark™-CP
  - 89 ULPMark™-PP
  - 47.2 ULPMark™-CM
  - 120000 SecureMark™-TLS
- Memories:

  - 4-Mbyte flash memory with ECC, 2 banks readwhile-write, including 512 Kbytes
    with 100 kcycles
  - With SRAM3 ECC off: 2514-Kbyte RAM including 66 Kbytes with ECC
  - With SRAM3 ECC on: 2450-Kbyte RAMincluding 322 Kbytes with ECC
  - External memory interface supporting SRAM,PSRAM, NOR, NAND, and FRAM memories
  - 2 Octo-SPI memory interfaces
  - 16-bit HSPI memory interface up to 160 MHz
- Rich graphic features:

  - Neo-Chrom GPU (GPU2D) accelerating any angle rotation, scaling, and
    perspective correct texture mapping
  - 16-Kbyte DCACHE2
  - Chrom-ART Accelerator (DMA2D) for smoothmotion and transparency effects
  - Chrom-GRC (GFXMMU) allowing up to 20 % of graphic resources optimization
  - MIPI® DSI host controller with two DSI lanes running at up to 500 Mbit/s each
  - LCD-TFT controller (LTDC)
  - Digital camera interface
- General-purpose input/outputs:

  - Up to 156 fast I/Os with interrupt capability most 5V-tolerant and
    up to 14 I/Os with independent supply down to 1.08 V
- Clock management:

  - 4 to 50 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (± 1 %)
  - Internal low-power 32 kHz RC (± 5 %)
  - 2 internal multispeed 100 kHz to 48 MHz oscillators, including one
    autotrimmed by LSE (better than ± 0.25 % accuracy)
  - Internal 48 MHz
  - 5 PLLs for system clock, USB, audio, ADC, DSI
- Security and cryptography:

  - SESIP3 and PSA Level 3 Certified Assurance Target
  - Arm® TrustZone® and securable I/Os, memories, and peripherals
  - Flexible life cycle scheme with RDP andpassword-protected debug
  - Root of trust thanks to unique boot entry and secure hide-protection area (HDP)
  - Secure firmware installation (SFI) thanks to embedded root secure services (RSS)
  - Secure data storage with hardware unique key (HUK)
  - Secure firmware upgrade support with TF-M
  - 2 AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte OTP (one-time programmable)
  - Active tampers
- Up to 17 timers, 2 watchdogs and RTC:

  - 19 timers: 2 16-bit advanced motor-control, 4 32-bit, 3 16-bit general
    purpose, 2 16-bit basic, 4 low-power 16-bit (available in Stop mode),
    2 SysTick timers, and 2 watchdogs
  - RTC with hardware calendar, alarms, and calibration
- Up to 25 communication peripherals:

  - 1 USB Type-C®/USB power delivery controller
  - 1 USB OTG high-speed with embedded PHY
  - 2 SAIs (serial audio interface)
  - 6 I2C FM+(1 Mbit/s), SMBus/PMBus™
  - 7 USARTs (ISO 7816, LIN, IrDA, modem)
  - 3 SPIs (6x SPIs with OCTOSPI/HSPI)
  - 1 CAN FD controller
  - 2 SDMMC interfaces
  - 1 multifunction digital filter (6 filters) + 1 audio digital filter
    with sound-activity detection
  - Parallel synchronous slave interface
- Mathematical coprocessor:

  - CORDIC for trigonometric functions acceleration
  - FMAC (filter mathematical accelerator)
- Rich analog peripherals (independent supply):

  - 2 14-bit ADC 2.5-Msps with hardware oversampling
  - 1 12-bit ADC 2.5-Msps, with hardware oversampling, autonomous in Stop 2 mode
  - 12-bit DAC (2 channels), low-power sample, and hold, autonomous in Stop 2 mode
  - 2 operational amplifiers with built-in PGA
  - 2 ultra-low-power comparators
- ECOPACK2 compliant packages

More information about STM32U5A5ZJ can be found here:

- [STM32U5A5ZJ on www.st.com](https://www.st.com/en/microcontrollers/stm32u5a5zj.html)
- [STM32U5A5 reference manual](https://www.st.com/resource/en/reference_manual/rm0456-stm32u5-series-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_u5a5zj_q` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_u5a5zj_q/stm32u5a5xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L35) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L759)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u595.dtsi?plain=1#L74) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L796) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L177) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L83) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L96)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L89) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32U5 Multi Speed Internal Clock[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L103) | [`st,stm32u5-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-msi-clock.md#std-dtcompatible-st-stm32u5-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L117) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L132)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L138) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L152) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L558) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_crypt.dtsi?plain=1#L9) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L751) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L807) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L159) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L216) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-chip | Serial Wire - JTAG Connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L892) | [`swj-connector`](../../../../build/dts/api/bindings/gpio/swj-connector.md#std-dtcompatible-swj-connector) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u5a5zj_q/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L371)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L395) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32 SAI controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L473) | [`st,stm32-sai`](../../../../build/dts/api/bindings/i2s/st%2Cstm32-sai.md#std-dtcompatible-st-stm32-sai) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u5a5zj_q/nucleo_u5a5zj_q-common.dtsi?plain=1#L32) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L189) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u5a5zj_q/nucleo_u5a5zj_q-common.dtsi?plain=1#L13) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u5a5zj_q/nucleo_u5a5zj_q-common.dtsi?plain=1#L42) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L44) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-chip | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L50) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MMC | on-chip | STM32 SDMMC Disk Access[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L741) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L43) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L167) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u5a5zj_q/nucleo_u5a5zj_q.dts?plain=1#L38) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L696) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st%2Cstm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | STM32U5 OTG HS PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_hs.dtsi?plain=1#L26) | [`st,stm32u5-otghs-phy`](../../../../build/dts/api/bindings/phy/st%2Cstm32u5-otghs-phy.md#std-dtcompatible-st-stm32u5-otghs-phy) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L210) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L820) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st%2Cstm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L536)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L504) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L183) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L722) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L463) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L902) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L914)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L923) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L939)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L932) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L296)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L305) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L314) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L332) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L946) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L341)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L351) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L78) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_extra.dtsi?plain=1#L71) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st%2Cstm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L419) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L527)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L495) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 OTGHS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5_usbotg_hs.dtsi?plain=1#L12) | [`st,stm32-otghs`](../../../../build/dts/api/bindings/usb/st%2Cstm32-otghs.md#std-dtcompatible-st-stm32-otghs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L273) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u5/stm32u5.dtsi?plain=1#L279) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo U5A5ZJ Q Board has 10 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32 Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/um2861-stm32u5-nucleo144-board-mb1549-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- CAN/CANFD\_TX: PD1
- CAN/CANFD\_RX: PD0
- DAC1\_OUT1 : PA4
- I2C\_1\_SCL : PB8
- I2C\_1\_SDA : PB9
- I2C\_2\_SCL : PF1
- I2C\_2\_SDA : PF0
- LD1 : PC7
- LD2 : PB7
- LD3 : PG2
- LPUART\_1\_TX : PG7
- LPUART\_1\_RX : PG8
- SPI\_1 nCS (GPIO) : PD14
- SPI\_1\_SCK : PA5
- SPI\_1\_MISO : PA6
- SPI\_1\_MOSI : PA7
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PD5
- UART\_2\_RX : PD6
- USER\_PB : PC13
- USB\_DM : PA11
- USB\_DP : PA12

#### System Clock

Nucleo U5A5ZJ Q System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
160MHz, driven by the 16MHz high speed oscillator.

#### Serial Port

Nucleo U5A5ZJ Q board has 6 U(S)ARTs. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB50` jumper on the back side of the board.

#### Using USB

USB 2.0 high speed (HS) operation requires the HSE clock source to be populated
and enabled. The Nucleo U5A5ZJ-Q includes the 16MHz oscillator and required
jumper settings.

## Programming and Debugging

The `nucleo_u5a5zj_q` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo U5A5ZJ-Q board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash the board using various tools.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
$ west flash --runner pyocd
```

For pyOCD, additional target information needs to be installed.
This can be done by executing the following commands.

```shell
$ pyocd pack --update
$ pyocd pack --install stm32u5
```

#### Flashing an application to Nucleo U5A5ZJ Q

Connect the Nucleo U5A5ZJ Q to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u5a5zj_q samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

Default flasher for this board is openocd. It could be used in the usual way.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u5a5zj_q samples/basic/blinky
west debug
```

Note: Check the `build/tfm` directory to ensure that the commands required by these scripts
(`readlink`, etc.) are available on your system. Please also check `STM32_Programmer_CLI`
(which is used for initialization) is available in the PATH.
