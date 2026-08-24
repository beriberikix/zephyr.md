---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_h7s3l8/doc/index.html
original_path: boards/st/nucleo_h7s3l8/doc/index.html
---

# Nucleo H7S3L8

Board Overview

[![../../../../_images/nucleo_h7s3l8.webp](https://docs.zephyrproject.org/4.2.0/_images/nucleo_h7s3l8.webp)
](https://docs.zephyrproject.org/4.2.0/_images/nucleo_h7s3l8.webp)

Nucleo H7S3L8

Name:
:   `nucleo_h7s3l8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h7s3xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_h7s3l8/doc/index.rst/../..)

## Overview

The STM32 Nucleo-144 board provides an affordable and flexible way for users
to try out new concepts and build prototypes by choosing from the various combinations
of performance and power consumption features, provided by the STM32 microcontroller.

The ST Zio connector, which extends the ARDUINO® Uno V3 connectivity, and
the ST morpho headers provide an easy means of expanding the functionality of the Nucleo
open development platform with a wide choice of specialized shields.
The STM32 Nucleo-144 board does not require any separate probe as it integrates
the ST-LINK V3 debugger/programmer.

The STM32 Nucleo-144 board comes with the STM32 comprehensive free software
libraries and examples available with the STM32Cube MCU Package.

Key Features

- STM32 microcontroller with 64Kbytes of flash and 620Kbytes of RAM in TFBGA225 package
- Ethernet compliant with IEEE-802.3-2002
- USB USB Device only, USB OTG full speed, or SNK/UFP (full-speed or high-speed mode)
- 3 user LEDs
- 2 user and reset push-buttons
- 32.768 kHz crystal oscillator
- Board connectors:

> - USB with Micro-AB or USB Type-C®
> - Ethernet RJ45
> - MIPI20 compatible connector with trace signals

- Flexible power-supply options: ST-LINK USB VBUS or external sources
- External or internal SMPS to generate Vcore logic supply
- On-board ST-LINK/V3 debugger/programmer with USB re-enumeration
- capability: mass storage, virtual COM port and debug port

More information about the board can be found at the [Nucleo H7S3L8 website](https://www.st.com/en/evaluation-tools/nucleo-h7s3l8.html).

## Hardware

Nucleo H7S3L8 provides the following hardware components:

The STM32H7S7xx devices are a high-performance microcontrollers family (STM32H7
Series) based on the high-performance Arm® Cortex®-M7 32-bit RISC core.
They operate at a frequency of up to 500 MHz.

- Core: ARM® 32-bit Cortex® -M7 CPU with TrustZone® and FPU.
- Performance benchmark:

  - 1284 DMPIS/MHz (Dhrystone 2.1)
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

  - 24 MHz crystal oscillator (HSE)
  - 32768 Hz crystal oscillator for RTC (LSE)
  - Internal 64 MHz (HSI) trimmable by software
  - Internal low-power 32 kHz RC (LSI)( ±5%)
  - Internal 4 MHz oscillator (CSI), trimmable by software
  - Internal 48 MHz (HSI48) with recovery system
  - 3 PLLs for system clock, USB, audio, ADC
- Power management

  - Embedded regulator (LDO) with three configurable range output to supply the digital circuitry
- RTC with HW calendar, alarms and calibration
- Up to 152 fast I/Os, most 5 V-tolerant, up to 10 I/Os with independent supply down to 1.08 V
- Up to 16 timers and 2 watchdogs

  - 16x 16-bit
  - 4x 32-bit timers with up to 4 IC/OC/PWM or pulse counter and quadrature (incremental) encoder input
  - 5x 16-bit low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 1x SysTick timer
- Memories

  - Up to 64KB Flash, 2 banks read-while-write
  - 1 Kbyte OTP (one-time programmable)
  - 640 KB of SRAM including 64 KB with hardware parity check and 320 Kbytes with flexible ECC
  - 4 Kbytes of backup SRAM available in the lowest power modes
  - Flexible external memory controller with up to 16-bit data bus: SRAM, PSRAM, FRAM, SDRAM/LPSDR SDRAM, NOR/NAND memories
  - 2x OCTOSPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
  - 1x HEXASPI memory interface with on-the-fly decryption and support for serial PSRAM/NAND/NOR, Hyper RAM/Flash frame formats
  - 2x SD/SDIO/MMC interfaces
- Rich analog peripherals (independent supply)

  - 2x 12-bit ADC with up to 5 MSPS in 12-bit
  - 1x Digital temperature sensor
- 35x communication interfaces

  - 1x USB Type-C / USB power-delivery controller
  - 1x USB OTG full-speed with PHY
  - 1x USB OTG high-speed with PHY
  - 3x I2C FM+ interfaces (SMBus/PMBus)
  - 1x I3C interface
  - 7x U(S)ARTS (ISO7816 interface, LIN, IrDA, modem control)
  - 2x LP UART
  - 6x SPIs including 3 muxed with full-duplex I2S
  - 2x SAI
  - 2x FDCAN
  - 2x SD/SDIO/MMC interface
  - 2x 16 channel DMA controllers
  - 1x 8- to 16- bit camera interface
  - 1x HDMI-CEC
  - 1x Ethernel MAC interface with DMA controller
  - 1x 16-bit parallel slave synchronous-interface
  - 1x SPDIF-IN interface
  - 1x MDIO slave interface
- CORDIC for trigonometric functions acceleration
- FMAC (filter mathematical accelerator)
- CRC calculation unit
- Development support: serial wire debug (SWD), JTAG, Embedded Trace Macrocell™

More information about STM32H7S3 can be found here:

- [STM32H7S3L8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32h7s3l8.html)
- [STM32H7Sx reference manual](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_h7s3l8` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_h7s3l8/stm32h7s3xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L35) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L764)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L780) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32H7RS RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L195) | [`st,stm32h7rs-rcc`](../../../../build/dts/api/bindings/clock/st,stm32h7rs-rcc.md#std-dtcompatible-st-stm32h7rs-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L93) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L99) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L107) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L121) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7RS main PLL[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L136)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L150) | [`st,stm32h7rs-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7rs-pll-clock.md#std-dtcompatible-st-stm32h7rs-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L157) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L165) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L567) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L177) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| on-board | STM32 XSPI Flash controller supporting the JEDEC CFI interface[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h7s3l8/nucleo_h7s3l8.dts?plain=1#L194) | [`st,stm32-xspi-nor`](../../../../build/dts/api/bindings/flash_controller/st,stm32-xspi-nor.md#std-dtcompatible-st-stm32-xspi-nor) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L234) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h7s3l8/arduino_r3_connector.dtsi?plain=1#L7) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L397)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L409) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L486) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h7s3l8/nucleo_h7s3l8.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32H7RS External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L206) | [`st,stm32h7rs-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32h7rs-exti.md#std-dtcompatible-st-stm32h7rs-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h7s3l8/nucleo_h7s3l8.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L42) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L186) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_h7s3l8/nucleo_h7s3l8.dts?plain=1#L170) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L819) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L228) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L544) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L200) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L796) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L824) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L836) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L843) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L331)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L339) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L355) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L388) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L433)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L444) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L50) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[11 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L534) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L753) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L804) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L519) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L526) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |
| xSPI | on-chip | STM32 XSPI Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L508)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L497) | [`st,stm32-xspi`](../../../../build/dts/api/bindings/xspi/st,stm32-xspi.md#std-dtcompatible-st-stm32-xspi) |

For more details please refer to [STM32H7R/S Nucleo-144 board User Manual](https://www.st.com/resource/en/user_manual/um3276-stm32h7rx7sx-nucleo144-board-mb1737-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

The Nucleo H7S3L8 board features a ST Zio connector (extended Arduino Uno V3)
and a ST morpho connector. Board is configured as follows:

- UART\_3 TX/RX : PD8/PD9 (ST-Link Virtual Port Com)
- USER\_PB : PC13
- LD1 : PD10
- LD2 : PD13
- LD3 : PB7
- I2C : PB8, PB9
- SPI1 NSS/SCK/MISO/MOSI : PD14PA5/PA6/PB5 (Arduino SPI)

#### System Clock

Nucleo H7S3L8 System Clock could be driven by an internal or external
oscillator, as well as the main PLL clock. By default, the System clock is
driven by the PLL clock at 600MHz, driven by an 24MHz high-speed external clock.

#### Serial Port

Nucleo H7S3L8 board has 4 UARTs and 3 USARTs plus one LowPower UART. The Zephyr console
output is assigned to UART3. Default settings are 115200 8N1.

#### Backup SRAM

In order to test backup SRAM you may want to disconnect VBAT from VDD. You can
do it by removing `SB13` jumper on the back side of the board.

## Programming and Debugging

The `nucleo_h7s3l8` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo H7S3L8 board includes an ST-LINK/V3 embedded debug tool interface.

Note

Check if your ST-LINK V3 has newest FW version. It can be done with [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html)

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, OpenOCD or JLink can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner openocd
```

#### Flashing an application to Nucleo H7S3L8

First, connect the NUCLEO-H7S3L8 to your host computer using
the USB port to prepare it for flashing. Then build and flash your application.

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your NUCLEO-H7S3L8 board.

```shell
$ minicom -b 115200 -D /dev/ttyACM0
```

or use screen:

```shell
$ screen /dev/ttyACM0 115200
```

Build and flash the application:

```shell
# From the root of the zephyr repository
west build -b nucleo_h7s3l8 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
$ Hello World! nucleo_h7s3l8
```

Blinky example can also be used:

```shell
# From the root of the zephyr repository
west build -b nucleo_h7s3l8 samples/basic/blinky
west flash
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_h7s3l8 samples/hello_world
west debug
```
