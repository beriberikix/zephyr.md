---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32l562e_dk/doc/index.html
original_path: boards/st/stm32l562e_dk/doc/index.html
---

# STM32L562E-DK Discovery

Board Overview

[![../../../../_images/stm32l562e_dk.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32l562e_dk.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32l562e_dk.jpg)

STM32L562E-DK Discovery

Name:
:   `stm32l562e_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32l562xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32l562e_dk/doc/index.rst/../..)

## Overview

The STM32L562E-DK Discovery kit is designed as a complete demonstration and
development platform for STMicroelectronics Arm® Cortex®-M33 core-based
STM32L562QEI6QU microcontroller with TrustZone®. Here are some highlights of
the STM32L562E-DK Discovery board:

- STM32L562QEI6QU microcontroller featuring 512 Kbytes of Flash memory and 256 Kbytes of SRAM in BGA132 package
- 1.54” 240 x 240 pixel-262K color TFT LCD module with parallel interface and touch-control panel
- USB Type-C™ Sink device FS
- On-board energy meter: 300 nA to 150 mA measurement range with a dedicated USB interface
- SAI Audio CODEC
- MEMS digital microphones
- 512-Mbit Octal-SPI Flash memory
- Bluetooth® V4.1 Low Energy module
- iNEMO 3D accelerometer and 3D gyroscope
- Board connectors

  - STMod+ expansion connector with fan-out expansion board for Wi‑Fi®, Grove and mikroBUS™ compatible connectors
  - Pmod™ expansion connector
  - Audio MEMS daughterboard expansion connector
  - ARDUINO® Uno V3 expansion connector
- Flexible power-supply options

  - ST-LINK
  - USB VBUS
  - external sources
- On-board STLINK-V3E debugger/programmer with USB re-enumeration capability:

  - mass storage
  - Virtual COM port
  - debug port
- 2 user LEDs
- User and reset push-buttons

More information about the board can be found at the [STM32L562E-DK Discovery website](https://www.st.com/en/evaluation-tools/stm32l562e-dk.html).

## Hardware

The STM32L562xx devices are an ultra-low-power microcontrollers family (STM32L5
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 110 MHz.

- Ultra-low-power with FlexPowerControl (down to 108 nA Standby mode and 62 uA/MHz run mode)
- Core: ARM® 32-bit Cortex® -M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 1.5 DMPIS/MHz (Drystone 2.1)
  - 442 CoreMark® (4.02 CoreMark® /MHZ)
- Security

  - Arm® TrustZone® and securable I/Os memories and peripherals
  - Flexible life cycle scheme with RDP (readout protection)
  - Root of trust thanks to unique boot entry and hide protection area (HDP)
  - Secure Firmware Installation thanks to embedded Root Secure Services
  - Secure Firmware Update support with TF-M
  - AES coprocessor
  - Public key accelerator
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - Active tamper and protection temperature, voltage and frequency attacks
  - True Random Number Generator NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte One-Time Programmable for user data
- Clock management:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC ( ±1%)
  - Internal low-power 32 kHz RC ( ±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator, auto-trimmed by
    LSE (better than ±0.25 % accuracy)
  - 3 PLLs for system clock, USB, audio, ADC
- Power management

  - Embedded regulator (LDO) with three configurable range output to supply the digital circuitry
  - Embedded SMPS step-down converter
  - External SMPS support
- RTC with HW calendar, alarms and calibration
- Up to 114 fast I/Os, most 5 V-tolerant, up to 14 I/Os with independent supply down to 1.08 V
- Up to 22 capacitive sensing channels: support touchkey, linear and rotary touch sensors
- Up to 16 timers and 2 watchdogs

  - 2x 16-bit advanced motor-control
  - 2x 32-bit and 5x 16-bit general purpose
  - 2x 16-bit basic
  - 3x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer
- Memories

  - Up to 512 MB Flash, 2 banks read-while-write
  - 512 KB of SRAM including 64 KB with hardware parity check
  - External memory interface for static memories supporting SRAM, PSRAM, NOR, NAND and FRAM memories
  - OCTOSPI memory interface
- Rich analog peripherals (independent supply)

  - 3x 12-bit ADC 5 MSPS, up to 16-bit with hardware oversampling, 200 uA/MSPS
  - 2x 12-bit DAC, low-power sample and hold
  - 2x operational amplifiers with built-in PGA
  - 2x ultra-low-power comparators
  - 4x digital filters for sigma delta modulator
- 19x communication interfaces

  - USB Type-C / USB power delivery controller
  - 2.0 full-speed crystal less solution, LPM and BCD
  - 2x SAIs (serial audio interface)
  - 4x I2C FM+(1 Mbit/s), SMBus/PMBus
  - 6x USARTs (ISO 7816, LIN, IrDA, modem)
  - 3x SPIs (7x SPIs with USART and OCTOSPI in SPI mode)
  - 1xFDCAN
  - 1xSDMMC interface
  - 2x 14 channel DMA controllers
- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32L562QE can be found here:

- [STM32L562QE on www.st.com](https://www.st.com/en/microcontrollers/stm32l562qe.html)
- [STM32L562 reference manual](https://www.st.com/resource/en/reference_manual/DM00346336.pdf)

### Supported Features

The `stm32l562e_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32l562e_dk/stm32l562xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L33) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L657)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L673) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V1 compatible with BlueNRG-MS devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L205) | [`st,hci-spi-v1`](../../../../build/dts/api/bindings/bluetooth/st,hci-spi-v1.md#std-dtcompatible-st-hci-spi-v1) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L146) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L74) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L87)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L80) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L94) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L101) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L116) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| Counter | on-chip | STM32 counters[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L502) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l562.dtsi?plain=1#L13) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L407) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-board | ST7789V 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L93) | [`sitronix,st7789v`](../../../../build/dts/api/bindings/display/sitronix,st7789v.md#std-dtcompatible-sitronix-st7789v) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L329) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L351) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L124) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 OSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L226) | [`st,stm32-ospi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L363)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L375) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L187) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech,ft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L27) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L159) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L15) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L710) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-board | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L62) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MIPI-DBI | on-board | STM32 FMC display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L86) | [`st,stm32-fmc-mipi-dbi`](../../../../build/dts/api/bindings/mipi-dbi/st,mipi-dbi-fmc.md#std-dtcompatible-st-stm32-fmc-mipi-dbi) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L397) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L41) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L133) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk.dts?plain=1#L47) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L435) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st,stm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L744) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L496)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L479) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L153) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L447) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L458) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics LSM6DSO 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L181) | [`st,lsm6dso`](../../../../build/dts/api/compatibles/st,lsm6dso.md#std-dtcompatible-st-lsm6dso) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L718) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L729) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L737) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L264)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L273) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L291) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L309) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L749) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L387)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L415) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L69) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L702) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st,stm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L318) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L486)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L469) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L689) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L250) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L256) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

#### `stm32l562e_dk/stm32l562xx/ns` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L33) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L657)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L673) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Bluetooth | on-board | STMicroelectronics SPI protocol V1 compatible with BlueNRG-MS devices[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L205) | [`st,hci-spi-v1`](../../../../build/dts/api/bindings/bluetooth/st,hci-spi-v1.md#std-dtcompatible-st-hci-spi-v1) |
| Clock control | on-chip | STM32 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L146) | [`st,stm32-rcc`](../../../../build/dts/api/bindings/clock/st,stm32-rcc.md#std-dtcompatible-st-stm32-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L74) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L87)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L80) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L94) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L101) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32L4/L5 main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L116) | [`st,stm32l4-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32l4-pll-clock.md#std-dtcompatible-st-stm32l4-pll-clock) |
| Counter | on-chip | STM32 counters[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L502) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l562.dtsi?plain=1#L13) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L407) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-board | ST7789V 320x240 display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L93) | [`sitronix,st7789v`](../../../../build/dts/api/bindings/display/sitronix,st7789v.md#std-dtcompatible-sitronix-st7789v) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L329) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L351) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L124) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 OSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L226) | [`st,stm32-ospi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-ospi-nor.md#std-dtcompatible-st-stm32-ospi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO controller[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L185) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L363)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L375) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L187) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech,ft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L27) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L159) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L15) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L710) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-board | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L62) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MIPI-DBI | on-board | STM32 FMC display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L86) | [`st,stm32-fmc-mipi-dbi`](../../../../build/dts/api/bindings/mipi-dbi/st,mipi-dbi-fmc.md#std-dtcompatible-st-stm32-fmc-mipi-dbi) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L397) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st,stm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L41) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L133) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_stm32l562xx_ns.dts?plain=1#L39) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| OCTOSPI | on-chip | STM32 OSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L435) | [`st,stm32-ospi`](../../../../build/dts/api/bindings/ospi/st,stm32-ospi.md#std-dtcompatible-st-stm32-ospi) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L744) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L179) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L496)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L479) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L153) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L447) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L458) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-board | STMicroelectronics LSM6DSO 6-axis IMU (Inertial Measurement Unit) sensor accessed through SPI bus[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32l562e_dk/stm32l562e_dk_common.dtsi?plain=1#L181) | [`st,lsm6dso`](../../../../build/dts/api/compatibles/st,lsm6dso.md#std-dtcompatible-st-lsm6dso) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L718) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L729) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L737) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L264)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L273) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L291) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L309) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L749) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L387)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L415) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L69) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| USB Type-C Port Controller | on-chip | STM32 USB Type-C / Power Delivery[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L702) | [`st,stm32-ucpd`](../../../../build/dts/api/bindings/tcpc/st,stm32-ucpd.md#std-dtcompatible-st-stm32-ucpd) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L318) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L486)[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L469) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L689) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L250) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/l5/stm32l5.dtsi?plain=1#L256) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Zephyr board options

The STM32L562e is an SoC with Cortex-M33 architecture. Zephyr provides support
for building for both Secure and Non-Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| stm32l562e\_dk | For building Trust Zone Disabled firmware |
| stm32l562e\_dk/stm32l562xx/ns | For building Non-Secure firmware |

Here are the instructions to build Zephyr with a non-secure configuration,
using [TF-M IPC](../../../../samples/tfm_integration/tfm_ipc/README.md#tfm_ipc "Implement communication between the secure and non-secure images using IPC.") sample:

> ```shell
> $ west build -b stm32l562e_dk/stm32l562xx/ns samples/tfm_integration/tfm_ipc/
> ```

Once done, before flashing, you need to first run a generated script that
will set platform option bytes config and erase platform (among others,
option bit TZEN will be set).

> ```shell
> $ ./build/tfm/api_ns/regression.sh
> $ west flash
> ```

Please note that, after having run a TFM sample on the board, you will need to
run `./build/tfm/api_ns/regression.sh` once more to clean up the board from secure
options and get back the platform back to a “normal” state and be able to run
usual, non-TFM, binaries.
Also note that, even then, TZEN will remain set, and you will need to use
[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) to disable it fully, if required.

### Connections and IOs

STM32L562E-DK Discovery Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32L562E-DK Discovery board User Manual](https://www.st.com/resource/en/user_manual/dm00635554.pdf).

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX/RX : PA9/PA10
- USART\_3 TX/RX : PC10/PC11
- I2C\_1 SCL/SDA : PB6/PB7
- SPI\_1 SCK/MISO/MOSI : PG2/PG3/PG4 (BT SPI bus)
- SPI\_3 NSS/SCK/MISO/MOSI : PE0/PG9/PB4/PB5 (Arduino SPI)
- USER\_PB : PC13
- LD10 : PG12
- PWM\_2\_CH1 : PA0
- DAC1 : PA4
- ADC1 : PC4

#### System Clock

STM32L562E-DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
110MHz, driven by 4MHz medium speed internal oscillator.

#### Serial Port

STM32L562E-DK Discovery board has 6 U(S)ARTs. The Zephyr console output is
assigned to USART1. Default settings are 115200 8N1.

#### TFT LCD screen and touch panel

The TFT LCD screen and touch panel are supported for the STM32L562E-DK Discovery board.
They can be tested using [LVGL basic sample](../../../../samples/subsys/display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.") sample:

```shell
# From the root of the zephyr repository
west build -b stm32l562e_dk samples/subsys/display/lvgl
```

## Programming and Debugging

STM32L562E-DK Discovery board includes an ST-LINK/V3E embedded debug tool interface.

Applications for the `stm32l562e_dk` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

Support can also be enabled for pyOCD by adding “pack” support with the
following pyOCD commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32l562qe
```

#### Flashing an application to STM32L562E-DK Discovery

Connect the STM32L562E-DK Discovery to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b stm32l562e_dk samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! stm32l562e_dk
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32l562e_dk samples/hello_world
west debug
```
