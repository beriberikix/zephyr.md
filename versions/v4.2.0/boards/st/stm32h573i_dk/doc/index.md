---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32h573i_dk/doc/index.html
original_path: boards/st/stm32h573i_dk/doc/index.html
---

# STM32H573I-DK Discovery

Board Overview

[![../../../../_images/stm32h573i_dk.jpg](../../../../_images/stm32h573i_dk.jpg)
](../../../../_images/stm32h573i_dk.jpg)

STM32H573I-DK Discovery

Name:
:   `stm32h573i_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h573xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32h573i_dk/doc/index.rst/../..)

## Overview

The STM32H573I-DK Discovery kit is designed as a complete demonstration and
development platform for STMicroelectronics Arm® Cortex®-M33 core-based
STM32H573IIK3Q microcontroller with TrustZone®. Here are some highlights of
the STM32H573I-DK Discovery board:

- STM32H573IIK3Q microcontroller featuring 2 Mbytes of Flash memory and 640 Kbytes of SRAM in 176-pin BGA package
- 1.54-inch 240x240 pixels TFT-LCD with LED backlight and touch panel
- USB Type-C™ Host and device with USB power-delivery controller
- SAI Audio DAC stereo with one audio jacks for input/output,
- ST MEMS digital microphone with PDM interface
- Octo-SPI interface connected to 512Mbit Octo-SPI NORFlash memory device (MX25LM51245GXDI00 from MACRONIX)
- 10/100-Mbit Ethernet,
- microSD™
- A Wi‑Fi® add-on board
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
- 4 user LEDs
- User and reset push-buttons

More information about the board can be found at the [STM32H573I-DK Discovery website](https://www.st.com/en/evaluation-tools/stm32h573i-dk.html).

## Hardware

The STM32H573xx devices are an high-performance microcontrollers family (STM32H5
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 250 MHz.

- Core: ARM® 32-bit Cortex® -M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 375 DMPIS/MHz (Dhrystone 2.1)
- Security

  - Arm® TrustZone® with ARMv8-M mainline security extension
  - Up to 8 configurable SAU regions
  - TrustZone® aware and securable peripherals
  - Flexible lifecycle scheme with secure debug authentication
  - Preconfigured immutable root of trust (ST-iROT)
  - SFI (secure firmware installation)
  - Secure data storage with hardware unique key (HUK)
  - Secure firmware upgrade support with TF-M
  - 2x AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - Active tampers
  - True Random Number Generator (RNG) NIST SP800-90B compliant
- Clock management:

  - 25 MHz crystal oscillator (HSE)
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 64 MHz (HSI) trimmable by software
  - Internal low-power 32 kHz RC (LSI)( ±5%)
  - Internal 4 MHz oscillator (CSI), trimmable by software
  - Internal 48 MHz (HSI48) with recovery system
  - 3 PLLs for system clock, USB, audio, ADC
- Power management

  - Embedded regulator (LDO) with three configurable range output to supply the digital circuitry
  - Embedded SMPS step-down converter
- RTC with HW calendar, alarms and calibration
- Up to 139 fast I/Os, most 5 V-tolerant, up to 10 I/Os with independent supply down to 1.08 V
- Up to 16 timers and 2 watchdogs

  - 12x 16-bit
  - 2x 32-bit timers with up to 4 IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
  - 6x 16-bit low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer
- Memories

  - Up to 2 MB Flash, 2 banks read-while-write
  - 1 Kbyte OTP (one-time programmable)
  - 640 KB of SRAM including 64 KB with hardware parity check and 320 Kbytes with flexible ECC
  - 4 Kbytes of backup SRAM available in the lowest power modes
  - Flexible external memory controller with up to 16-bit data bus: SRAM, PSRAM, FRAM, SDRAM/LPSDR SDRAM, NOR/NAND memories
  - 1x OCTOSPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
  - 2x SD/SDIO/MMC interfaces
- Rich analog peripherals (independent supply)

  - 2x 12-bit ADC with up to 5 MSPS in 12-bit
  - 2x 12-bit D/A converters
  - 1x Digital temperature sensor
- 34x communication interfaces

  - 1x USB Type-C / USB power-delivery controller
  - 1x USB 2.0 full-speed host and device
  - 4x I2C FM+ interfaces (SMBus/PMBus)
  - 1x I3C interface
  - 12x U(S)ARTS (ISO7816 interface, LIN, IrDA, modem control)
  - 1x LP UART
  - 6x SPIs including 3 muxed with full-duplex I2S
  - 5x additional SPI from 5x USART when configured in Synchronous mode
  - 2x SAI
  - 2x FDCAN
  - 1x SDMMC interface
  - 2x 16 channel DMA controllers
  - 1x 8- to 14- bit camera interface
  - 1x HDMI-CEC
  - 1x Ethernel MAC interface with DMA controller
  - 1x 16-bit parallel slave synchronous-interface
- CORDIC for trigonometric functions acceleration
- FMAC (filter mathematical accelerator)
- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32H573 can be found here:

- [STM32H573 on www.st.com](https://www.st.com/en/microcontrollers/stm32h573ii.html)
- [STM32H573 reference manual](https://www.st.com/resource/en/reference_manual/rm0481-stm32h563h573-and-stm32h562-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32h573i_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32h573i_dk/stm32h573xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L29) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L309)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L273) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L520)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L483) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st%2Cstm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L149) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L54) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L60) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L68)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L75) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L82) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L97)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L103) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L111) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st%2Cstm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L368) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L474) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L301) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| Display | on-board | Sitronix ST7789V display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L138) | [`sitronix,st7789v`](../../../../build/dts/api/bindings/display/sitronix%2Cst7789v.md#std-dtcompatible-sitronix-st7789v) |
| DMA | on-chip | STM32U5 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L564) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L541) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L547) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st%2Cstm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| on-board | Generic MII PHY[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L292) | [`ethernet-phy`](../../../../build/dts/api/bindings/ethernet/phy/ethernet-phy.md#std-dtcompatible-ethernet-phy) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L123) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 XSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L394) | [`st,stm32-xspi-nor`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-xspi-nor.md#std-dtcompatible-st-stm32-xspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L188) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L437)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L207) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L588) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st%2Cstm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| I3C | on-chip | STM32H5 I3C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L461) | [`st,stm32-i3c`](../../../../build/dts/api/bindings/i3c/st%2Cstm32-i3c.md#std-dtcompatible-st-stm32-i3c) |
| Input | on-board | FT3267/FT5XX6/FT6XX6 capacitive touch panels[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L221) | [`focaltech,ft5336`](../../../../build/dts/api/bindings/input/focaltech%2Cft5336.md#std-dtcompatible-focaltech-ft5336) |
| on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L54) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L161) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L556) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st%2Cstm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L505) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| on-board | STM32 Flexible Memory Controller (NOR Flash/PSRAM/SRAM controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L106) | [`st,stm32-fmc-nor-psram`](../../../../build/dts/api/bindings/memory-controllers/st%2Cstm32-fmc-nor-psram.md#std-dtcompatible-st-stm32-fmc-nor-psram) |
| MIPI-DBI | on-board | STM32 FMC display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L130) | [`st,stm32-fmc-mipi-dbi`](../../../../build/dts/api/bindings/mipi-dbi/st%2Cmipi-dbi-fmc.md#std-dtcompatible-st-stm32-fmc-mipi-dbi) |
| MMC | on-chip | STM32 SDMMC Disk Access[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L495)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h563.dtsi?plain=1#L13) | [`st,stm32-sdmmc`](../../../../build/dts/api/bindings/mmc/st%2Cstm32-sdmmc.md#std-dtcompatible-st-stm32-sdmmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm%2Carmv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L131) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L299) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L687) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L182) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L362)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L346) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Regulator | on-board | Fixed voltage regulators[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/stm32h573i_dk.dts?plain=1#L64) | [`regulator-fixed`](../../../../build/dts/api/bindings/regulator/regulator-fixed.md#std-dtcompatible-regulator-fixed) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L155) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L531) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L326) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Digital Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L650) | [`st,stm32-digi-temp`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-digi-temp.md#std-dtcompatible-st-stm32-digi-temp) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L660) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L672) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L680) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st%2Cstm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L251)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L260) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L278) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| on-chip | STM32 UART[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L126) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| SMbus | on-chip | STM32 SMBus controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L692) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st%2Cstm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L498)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L487) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L229) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L353)[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L337) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L636) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L287) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L293) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| xSPI | on-chip | STM32 XSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h562.dtsi?plain=1#L261) | [`st,stm32-xspi`](../../../../build/dts/api/bindings/xspi/st%2Cstm32-xspi.md#std-dtcompatible-st-stm32-xspi) |

### Connections and IOs

STM32H573I-DK Discovery Board has 9 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32H573I-DK Discovery board User Manual](https://www.st.com/en/evaluation-tools/stm32h573i-dk.html).

#### Default Zephyr Peripheral Mapping:

- USART\_1 TX/RX : PA9/PA10 (VCP)
- USART\_3 TX/RX : PB11/PB10 (Arduino USART3)
- USER\_PB : PC13
- LD1 (green) : PI9
- DAC1 channel 1 output : PA4
- ADC1 channel 6 input : PF12

#### System Clock

STM32H573I-DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
240MHz, driven by 25MHz external oscillator (HSE).

#### Serial Port

STM32H573I-DK Discovery board has 3 U(S)ARTs. The Zephyr console output is
assigned to USART1. Default settings are 115200 8N1.

#### TFT LCD screen and touch panel

The TFT LCD screen and touch panel are supported for the STM32H573I-DK Discovery board.
They can be tested using [LVGL basic sample](../../../../samples/subsys/display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.") sample:

```shell
# From the root of the zephyr repository
west build -b stm32h573i_dk samples/subsys/display/lvgl
```

## Programming and Debugging

The `stm32h573i_dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **probe-rs** | ✅ |  |  |  |  |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

STM32H573I-DK Discovery board includes an ST-LINK/V3E embedded debug tool interface.

Applications for the `stm32h573i_dk` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### OpenOCD Support

For now, OpenOCD support for STM32H5 is not available on upstream OpenOCD.
You can check [OpenOCD official Github mirror](https://github.com/openocd-org/openocd/).
In order to use it though, you should clone from the customized
[STMicroelectronics OpenOCD Github](https://github.com/STMicroelectronics/OpenOCD/tree/openocd-cubeide-r6) and compile it following usual README guidelines.
Once it is done, you can set the OPENOCD and OPENOCD\_DEFAULT\_PATH variables in
[boards/st/stm32h573i\_dk/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h573i_dk/board.cmake) to point the build
to the paths of the OpenOCD binary and its scripts, before
including the common openocd.board.cmake file:

> ```text
> set(OPENOCD "<path_to_openocd_repo>/src/openocd" CACHE FILEPATH "" FORCE)
> set(OPENOCD_DEFAULT_PATH <path_to_opneocd_repo>/tcl)
> include(${ZEPHYR_BASE}/boards/common/openocd.board.cmake)
> ```

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
```

For pyOCD, additional target information needs to be installed
by executing the following commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32h5
```

#### Flashing an application to STM32H573I-DK Discovery

Connect the STM32H573I-DK Discovery to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b stm32h573i_dk samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! stm32h573i_dk
```

### Debugging

Waiting for OpenOCD support, debugging could be performed with pyOCD which
requires to enable “pack” support with the following pyOCD command:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32h5
```

Once installed, you can debug an application in the usual way. Here is an
example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32h573i_dk samples/hello_world
west debug
```
