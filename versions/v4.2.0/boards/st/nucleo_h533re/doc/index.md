---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_h533re/doc/index.html
original_path: boards/st/nucleo_h533re/doc/index.html
---

# Nucleo H533RE

Board Overview

[![../../../../_images/nucleo_h533re.jpg](https://docs.zephyrproject.org/4.2.0/_images/nucleo_h533re.jpg)
](https://docs.zephyrproject.org/4.2.0/_images/nucleo_h533re.jpg)

Nucleo H533RE

Name:
:   `nucleo_h533re`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h533xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_h533re/doc/index.rst/../..)

## Overview

The Nucleo H533RE board is designed as an affordable development platform for
STMicroelectronics ARM® Cortex®-M33 core-based STM32H533RET6
microcontroller with TrustZone®.
Here are some highlights of the Nucleo H533RE board:

- STM32H533RE microcontroller featuring 512 kbytes of Flash memory and 272 Kbytes of
  SRAM in LQFP64 package
- Board connectors:

  - USB Type-C™ Sink device FS
  - ST Zio expansion connector including Arduino Uno V3 connectivity (CN5, CN6, CN8, CN9)
  - ST morpho extension connector (CN7, CN10)
- Flexible board power supply:

  > - 5V\_USB\_STLK from ST-Link USB connector
  > - VIN (7 - 12V, 0.8) supplied via pin header CN6 pin 8 or CN7 pin 24
  > - ESV on the ST morpho connector CN7 Pin 6 (5V, O.5A)
  > - VBUS\_STLK from a USB charger via the ST-LINK USB connector
  > - VBUSC from the USB user connector (5V, 0.5A)
  > - 3V3\_EXT supplied via a pin header CN6 pin 4 or CN7 pin 16 (3.3V, 1.3A)
- On-board ST-LINK/V3EC debugger/programmer

  - mass storage
  - Virtual COM port
  - debug port
- One user LED shared with ARDUINO® Uno V3
- Two push-buttons: USER and RESET
- 32.768 kHz crystal oscillator

More information about the board can be found at the [NUCLEO\_H533RE website](https://www.st.com/en/evaluation-tools/nucleo-h533re).

## Hardware

The STM32H533xx devices are high-performance microcontrollers from the STM32H5
Series based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 250 MHz.

- Core: ARM® 32-bit Cortex® -M33 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 375 DMPIS/MHz (Dhrystone 2.1)
- Security

  - Arm® TrustZone® with Armv8-M mainline security extension
  - Up to eight configurable SAU regions
  - TrustZone® aware and securable peripherals
  - Flexible life cycle scheme with secure debug authentication
  - SESIP3 and PSA Level 3 certified assurance target
  - Preconfigured immutable root of trust (ST-iROT)
  - SFI (secure firmware installation)
  - Root of trust thanks to unique boot entry and secure hide protection area (HDP)
  - Secure data storage with hardware unique key (HUK)
  - Secure firmware upgrade support with TF-M
  - Two AES coprocessors including one with DPA resistance
  - Public key accelerator, DPA resistant
  - On-the-fly decryption of Octo-SPI external memories
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - Active tampers
- Clock management:

  - 24 MHz crystal oscillator (HSE)
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
- Up to 112 fast I/Os, most 5 V-tolerant, up to 10 I/Os with independent supply down to 1.08 V
- Up to 16 timers and 2 watchdogs

  - 8x 16-bit
  - 2x 32-bit timers with up to 4 IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
  - 2x 16-bit low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer
- Memories

  - Up to 512 Kbytes Flash, 2 banks read-while-write
  - 1 Kbyte OTP (one-time programmable)
  - 272 Kbytes of SRAM (80-Kbyte SRAM2 with ECC)
  - 2 Kbytes of backup SRAM available in the lowest power modes
  - Flexible external memory controller with up to 16-bit data bus: SRAM, PSRAM, FRAM, NOR/NAND memories
  - 1x OCTOSPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
  - 1x SD/SDIO/MMC interfaces
- Rich analog peripherals (independent supply)

  - 2x 12-bit ADC with up to 5 MSPS in 12-bit
  - 1x 12-bit DAC with 2 channels
  - 1x Digital temperature sensor
  - Voltage reference buffer
- 34x communication interfaces

  - 1x USB Type-C / USB power-delivery controller
  - 1x USB 2.0 full-speed host and device (crystal-less)
  - 3x I2C FM+ interfaces (SMBus/PMBus)
  - 2x I3C interface
  - 6x U(S)ARTS (ISO7816 interface, LIN, IrDA, modem control)
  - 1x LP UART
  - 4x SPIs including 3 muxed with full-duplex I2S
  - 4x additional SPI from 4x USART when configured in Synchronous mode
  - 2x FDCAN
  - 1x SDMMC interface
  - 2x 16 channel DMA controllers
  - 1x 8- to 14- bit camera interface
  - 1x HDMI-CEC
  - 1x 16-bit parallel slave synchronous-interface
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32H533RE can be found here:

- [STM32H533re on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h533re)
- [STM32H533 reference manual](https://www.st.com/resource/en/reference_manual/rm0481-stm32h533-stm32h563-stm32h573-and-stm32h562-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_h533re` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_h533re/stm32h533xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L29) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm,cortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L309) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| CAN | on-chip | STM32 FDCAN CAN FD controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L520) | [`st,stm32-fdcan`](../../../../build/dts/api/bindings/can/st,stm32-fdcan.md#std-dtcompatible-st-stm32-fdcan) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L149) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st,stm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L54) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L60) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L68)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L90) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L82) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U5 PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L97)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L103) | [`st,stm32u5-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32u5-pll-clock.md#std-dtcompatible-st-stm32u5-pll-clock) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L111) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L368) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L301) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L564) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st,stm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Ethernet | on-chip | STM32 Ethernet Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L541) | [`st,stm32-ethernet-controller`](../../../../build/dts/api/bindings/ethernet/st,stm32-ethernet-controller.md#std-dtcompatible-st-stm32-ethernet-controller) |
| on-chip | STM32H7 Ethernet[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L547) | [`st,stm32h7-ethernet`](../../../../build/dts/api/bindings/ethernet/st,stm32h7-ethernet.md#std-dtcompatible-st-stm32h7-ethernet) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L123) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L188) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| on-board | GPIO pins exposed on ST Morpho connector[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/st_morpho_connector.dtsi?plain=1#L10) | [`st-morpho-header`](../../../../build/dts/api/bindings/gpio/st-morpho-header.md#std-dtcompatible-st-morpho-header) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L437) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L588) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| I3C | on-chip | STM32H5 I3C controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L461) | [`st,stm32-i3c`](../../../../build/dts/api/bindings/i3c/st,stm32-i3c.md#std-dtcompatible-st-stm32-i3c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/nucleo_h533re.dts?plain=1#L43) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L161) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/nucleo_h533re.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| on-board | Group of PWM-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/nucleo_h533re.dts?plain=1#L35) | [`pwm-leds`](../../../../build/dts/api/bindings/led/pwm-leds.md#std-dtcompatible-pwm-leds) |
| MDIO | on-chip | STM32 MDIO Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L556) | [`st,stm32-mdio`](../../../../build/dts/api/bindings/mdio/st,stm32-mdio.md#std-dtcompatible-st-stm32-mdio) |
| Memory controller | on-chip | STM32 Flexible Memory Controller (FMC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h533.dtsi?plain=1#L20) | [`st,stm32-fmc`](../../../../build/dts/api/bindings/memory-controllers/st,stm32-fmc.md#std-dtcompatible-st-stm32-fmc) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L37) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L131) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L687) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L182) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L383)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L346) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L155) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L531) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L326) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Sensors | on-chip | STM32 Digital Temperature Sensor[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L650) | [`st,stm32-digi-temp`](../../../../build/dts/api/bindings/sensor/st,stm32-digi-temp.md#std-dtcompatible-st-stm32-digi-temp) |
| on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L660) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L672) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L680) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L251)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L269) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L278) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SMbus | on-chip | STM32 SMBus controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L692) | [`st,stm32-smbus`](../../../../build/dts/api/bindings/smbus/st,stm32-smbus.md#std-dtcompatible-st-stm32-smbus) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L487)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L498) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L229) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| on-chip | STM32 timers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L374)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L337) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L636) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st,stm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L287) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h5/stm32h5.dtsi?plain=1#L293) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Zephyr board options

The STM32H533 is a SoC with Cortex-M33 architecture. Zephyr provides support
for building for Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| nucleo\_h533re | For building Secure firmware |

### Connections and IOs

Nucleo H533RE Board has 8 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32H5 Nucleo-64 board User Manual](https://www.st.com/resource/en/user_manual/um3121-stm32h5-nucleo64-board-mb1814-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- ADC1 channel 0 input: PA0
- USART1 TX/RX : PB14/PB15 (Arduino USART1)
- SPI1 SCK/MISO/MOSI/NSS: PA5/PA6/PA7/PC9
- UART2 TX/RX : PA2/PA3 (VCP)
- USER\_PB : PC13

#### System Clock

Nucleo H533RE System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
240MHz, driven by an 24MHz high-speed external clock.

#### Serial Port

Nucleo H533RE board has up to 4 USARTs, 2 UARTs, and one LPUART. The Zephyr console output is assigned
to USART2. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM, you may want to disconnect VBAT from VDD\_MCU.
You can do it by removing `SB38` jumper on the back side of the board.
VBAT can be provided via the left ST Morpho connector’s pin 33.

## Programming and Debugging

The `nucleo_h533re` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo H533RE board includes an ST-LINK/V3EC embedded debug tool interface.
This probe allows to flash the board using various tools.

Applications for the `nucleo_h533re` board can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### OpenOCD Support

For now, openocd support for stm32h5 is not available on upstream OpenOCD.
You can check [OpenOCD official Github mirror](https://github.com/openocd-org/openocd/).
In order to use it though, you should clone from the customized
[STMicroelectronics OpenOCD Github](https://github.com/STMicroelectronics/OpenOCD/tree/openocd-cubeide-r6) and compile it following usual README guidelines.
Once it is done, you can set the OPENOCD and OPENOCD\_DEFAULT\_PATH variables in
[boards/st/nucleo\_h533re/board.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h533re/board.cmake) to point the build
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

Alternatively, OpenOCD, JLink, or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
$ west flash --runner pyocd
$ west flash --runner jlink
```

For pyOCD, additional target information needs to be installed
which can be done by executing the following commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32h5
```

#### Flashing an application to Nucleo H533RE

Connect the Nucleo H533RE to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h533re samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_h533re
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h533re samples/basic/blinky
west debug
```
