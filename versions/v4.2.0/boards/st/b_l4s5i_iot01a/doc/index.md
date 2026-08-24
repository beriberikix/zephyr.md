---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/b_l4s5i_iot01a/doc/index.html
original_path: boards/st/b_l4s5i_iot01a/doc/index.html
---

# B-L4S5I-IOT01A Discovery kit

Board Overview

[![../../../../_images/b-l4s5i_iot01a.jpg](https://docs.zephyrproject.org/4.2.0/_images/b-l4s5i_iot01a.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/b-l4s5i_iot01a.jpg)

B-L4S5I-IOT01A Discovery kit

Name:
:   `b_l4s5i_iot01a`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l4s5xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/b_l4s5i_iot01a/doc/index.rst/../..)

## Overview

The B\_L4S5I\_IOT01A Discovery kit features an ARM Cortex-M4 based STM32L4S5VI MCU
with a wide range of connectivity support and configurations. Here are
some highlights of the B\_L4S5I\_IOT01A Discovery kit:

- STM32L4S5VIT6 microcontroller featuring 2 Mbyte of Flash memory, 640 Kbytes of RAM in LQFP100 package
- On-board ST-LINK/V2-1 supporting USB re-enumeration capability
- Three different interfaces supported on USB:

  > - Virtual com port
  > - Mass storage
  > - Debug port
- ARDUINO ® Uno V3 and Pmod TM expansion connector
- 4 LEDs (2 for user, wifi, BLE)
- 2 push-buttons (user and reset)
- USB OTG FS with micro-AB connector
- Dynamic NFC tag
- 2 digital omnidirectional microphones
- Capacitive digital sensor for relative humidity and temperature
- Time-of-flight and gesture-detection sensors
- High-performance 3-axis magnetometer
- 3D accelerometer and 3D gyroscope
- 64-Mbit Quad-SPI Flash memory
- Bluetooth ® 4.1 module
- 802.11 b/g/n compliant Wi‐Fi ® module
- MCU current ammeter with 4 ranges and auto-calibration
- Flexible power supply options:
  :   - ST-LINK/V2-1
      - USB FS connector
      - External 5 V

More information about the board can be found at the [B L4S5I IOT01A Discovery kit website](https://www.st.com/en/evaluation-tools/b-l4s5i-iot01a.html).

## Hardware

The STM32L4S5VI SoC provides the following hardware features:

- Ultra-low-power with FlexPowerControl (down to 130 nA Standby mode and 100 uA/MHz run mode)
- Core: ARM® 32-bit Cortex®-M4 CPU with FPU, frequency up to 120 MHz, 100DMIPS/1.25DMIPS/MHz (Dhrystone 2.1)
- Clock Sources:
  :   - 4 to 48 MHz crystal oscillator
      - 32 kHz crystal oscillator for RTC (LSE)
      - Internal 16 MHz factory-trimmed RC ( ±1%)
      - Internal low-power 32 kHz RC ( ±5%)
      - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
        LSE (better than ±0.25 % accuracy)
      - 3 PLLs for system clock, USB, audio, ADC
- RTC with HW calendar, alarms and calibration
- Up to 21 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- 16x timers:
  :   - 2x 16-bit advanced control
      - 2x 32-bit and 5x 16-bit general purpose
      - 2x 16-bit basic
      - 2x low-power 16-bit timers (available in Stop mode)
      - 2x watchdogs
      - SysTick timer
- Up to 83 fast I/Os, most 5 V-tolerant
- Memories
  :   - Up to 2 MB Flash, 2 banks read-while-write, proprietary code readout protection
      - Up to 640 KB of SRAM including 32 KB with hardware parity check
      - External memory interface for static memories supporting SRAM, PSRAM, NOR and NAND memories
      - Octo SPI memory interface
- 4x digital filters for sigma delta modulator
- Rich analog peripherals (independent supply)
  :   - 1x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200 uA/MSPS
      - 2x 12-bit DAC, low-power sample and hold
      - 2x operational amplifiers with built-in PGA
      - 2x ultra-low-power comparators
- 18x communication interfaces
  :   - USB OTG 2.0 full-speed, LPM and BCD
      - 2x SAIs (serial audio interface)
      - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
      - 6x USARTs (ISO 7816, LIN, IrDA, modem)
      - 3x SPIs (4x SPIs with the Quad SPI)
      - CAN (2.0B Active) and SDMMC interface
      - SDMMC I/F
      - DCMI camera interface
- 14-channel DMA controller with multiplex request router
- True random number generator
- CRC calculation unit, 96-bit unique ID
- AES and HASH hardware accelerators
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L4S5VI can be found here:
:   - [STM32L4S5VI on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32l4s5vi.html)
    - [STM32L4S5 reference manual](https://www.st.com/resource/en/reference_manual/dm00310109.pdf)

### Supported Features

The `b_l4s5i_iot01a` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `b_l4s5i_iot01a/stm32l4s5xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L33) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L397) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V1 compatible with BlueNRG-MS devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L158) | [`st,hci-spi-v1`](../../../../build/dts/api/bindings/bluetooth/st,hci-spi-v1.md#std-dtcompatible-st-hci-spi-v1) |
| CAN | on-chip | STM32 CAN controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L295) | [`st,stm32-bxcan`](../../../../build/dts/api/bindings/can/st,stm32-bxcan.md#std-dtcompatible-st-stm32-bxcan) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L136) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L73) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L80) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L87) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L102) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L110) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L320) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32L4 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4s5.dtsi?plain=1#L13) | [`st,stm32l4-aes`](../../../../build/dts/api/bindings/crypto/st,stm32l4-aes.md#std-dtcompatible-st-stm32l4-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L372) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L429)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L439) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L326) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 OSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L249) | [`st,stm32-ospi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L168) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L242)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L254) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L42) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L147) | [`st,stm32-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32-exti.md#std-dtcompatible-st-stm32-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Battery Backed RAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4r5.dtsi?plain=1#L29) | [`st,stm32-bbram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-bbram.md#std-dtcompatible-st-stm32-bbram) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L350) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L126) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L179) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L380)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L394) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st,stm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L409) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L162) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Power management | on-chip | STM32 power controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L483) | [`st,stm32-pwr`](../../../../build/dts/api/bindings/power/st,stm32-pwr.md#std-dtcompatible-st-stm32-pwr) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L314)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L297) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L471) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L386) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics LIS3MDL magnetometer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L115) | [`st,lis3mdl-magn`](../../../../build/dts/api/bindings/sensor/st,lis3mdl-magn.md#std-dtcompatible-st-lis3mdl-magn) |
| on-board | STMicroelectronics HTS221 humidity and temperature sensor on I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L120) | [`st,hts221`](../../../../build/dts/api/compatibles/st,hts221.md#std-dtcompatible-st-hts221) |
| on-board | STMicroelectronics LPS22HB pressure sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L125) | [`st,lps22hb-press`](../../../../build/dts/api/bindings/sensor/st,lps22hb-press.md#std-dtcompatible-st-lps22hb-press) |
| on-board | STMicroelectronics LSM6DSL 6-axis accelerometer and gyrometer accessed through I2C bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L130) | [`st,lsm6dsl`](../../../../build/dts/api/compatibles/st,lsm6dsl.md#std-dtcompatible-st-lsm6dsl) |
| on-board | STMicroelectronics VL53L0X Time of Flight sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L136) | [`st,vl53l0x`](../../../../build/dts/api/bindings/sensor/st,vl53l0x.md#std-dtcompatible-st-vl53l0x) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L517) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L528) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L536) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L215)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L224) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L233) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L106) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L543) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L276)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L148) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L62) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L304)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L287) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L449) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L304) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Video | on-chip | STM32 Digital Camera Memory Interface (DCMI)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4p5.dtsi?plain=1#L338) | [`st,stm32-dcmi`](../../../../build/dts/api/bindings/video/st,stm32-dcmi.md#std-dtcompatible-st-stm32-dcmi) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L201) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l4/stm32l4.dtsi?plain=1#L207) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| Wi-Fi | on-board | es-WiFi module[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/b_l4s5i_iot01a/b_l4s5i_iot01a.dts?plain=1#L167) | [`inventek,eswifi`](../../../../build/dts/api/bindings/wifi/inventek,eswifi.md#std-dtcompatible-inventek-eswifi) |

### Connections and IOs

B\_L4S5I\_IOT01A Discovery kit has 9 GPIO controllers (from A to I). These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [B L47S5I IOT01A board User Manual](https://www.st.com/resource/en/user_manual/dm00698410.pdf).

#### Default Zephyr Peripheral Mapping:

- UART\_1 TX/RX : PB6/PB7 (ST-Link Virtual Port Com)
- UART\_4 TX/RX : PA0/PA1 (Arduino Serial)
- I2C1 SCL/SDA : PB8/PB9 (Arduino I2C)
- I2C2 SCL/SDA : PB10/PB11 (Sensor I2C bus)
- SPI1 NSS/SCK/MISO/MOSI : PA2/PA5/PA6/PA7 (Arduino SPI)
- SPI3 SCK/MISO/MOSI : PC10/PC11/PC12 (BT SPI bus)
- PWM\_2\_CH1 : PA15
- LD1 : PA5
- LD2 : PB14
- user button : PC13

#### System Clock

B\_L4S5I\_IOT01A Discovery System Clock could be driven by an internal or external oscillator,
as well as the main PLL clock. By default the System clock is driven by the PLL clock at 80MHz,
driven by 16MHz high speed internal oscillator.

#### Serial Port

B\_L4S5I\_IOT01A Discovery kit has 4 U(S)ARTs. The Zephyr console output is assigned to UART1.
Default settings are 115200 8N1.

## Programming and Debugging

The `b_l4s5i_iot01a` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

B\_L4S5I\_IOT01A Discovery kit includes an ST-LINK/V2-1 embedded debug tool interface.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner jlink
```

#### Flashing an application to B\_L4S5I\_IOT01A Discovery kit

Connect the B\_L4S5I\_IOT01A Discovery kit to your host computer using the USB
port, then run a serial host program to connect with your Discovery
board. For example:

```shell
$ minicom -D /dev/ttyACM0
```

Then, build and flash in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b b_l4s5i_iot01a samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! arm
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b b_l4s5i_iot01a samples/hello_world
west debug
```
