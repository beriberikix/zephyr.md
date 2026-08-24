---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/stm32h7s78_dk/doc/index.html
original_path: boards/st/stm32h7s78_dk/doc/index.html
---

# STM32H7S78-DK Discovery

Board Overview

[![../../../../_images/stm32h7s78_dk.jpg](https://docs.zephyrproject.org/4.1.0/_images/stm32h7s78_dk.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/stm32h7s78_dk.jpg)

STM32H7S78-DK Discovery

Name:
:   `stm32h7s78_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32h7s7xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32h7s78_dk/doc/index.rst/../..)

## Overview

The STM32H7S78-DK Discovery kit is designed as a complete demonstration and
development platform for STMicroelectronics Arm® Cortex®-M7 core-based
STM32H7S7L8H6H microcontroller with TrustZone®. Here are some highlights of
the STM32H7S78-DK Discovery board:

- STM32H7S7L8H6H microcontroller featuring 64Kbytes of Flash memory and 620 Kbytes of SRAM in 225-pin TFBGA package
- USB Type-C™ Host and device with USB power-delivery controller
- SAI Audio DAC stereo with one audio jacks for input/output,
- ST MEMS digital microphone with PDM interface
- Octo-SPI interface connected to 512Mbit Octo-SPI NORFlash memory device (MX66UW1G45GXD100 from MACRONIX)
- 10/100-Mbit Ethernet,
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

More information about the board can be found at the [STM32H7S78-DK Discovery website](https://www.st.com/en/evaluation-tools/stm32h7s78-dk.html).

## Hardware

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
  - Embedded SMPS step-down converter
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

More information about STM32H7S7 can be found here:

- [STM32H7Sx on www.st.com](https://www.st.com/en/evaluation-tools/stm32h7s78-dk.html)
- [STM32H7Sx reference manual](https://www.st.com/resource/en/reference_manual/rm0477-stm32h7rx7sx-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32h7s78_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32h7s78_dk/stm32h7s7xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M7 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L34) | [`arm,cortex-m7`](../../../../build/dts/api/bindings/cpu/arm,cortex-m7.md#std-dtcompatible-arm-cortex-m7) |
| ADC | on-chip | STM32 ADC[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L740) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32H7RS RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L193) | [`st,stm32h7rs-rcc`](../../../../build/dts/api/bindings/clock/st,stm32h7rs-rcc.md#std-dtcompatible-st-stm32h7rs-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L91) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | STM32 HSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L97) | [`st,stm32h7-hsi-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7-hsi-clock.md#std-dtcompatible-st-stm32h7-hsi-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L105)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L112) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L119) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32H7RS main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L134)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L141) | [`st,stm32h7rs-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32h7rs-pll-clock.md#std-dtcompatible-st-stm32h7rs-pll-clock) |
| on-chip | STM32 Clock multiplexer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L155) | [`st,stm32-clock-mux`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mux.md#std-dtcompatible-st-stm32-clock-mux) |
| on-chip | STM32 Microcontroller Clock Output (MCO)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L163) | [`st,stm32-clock-mco`](../../../../build/dts/api/bindings/clock/st,stm32-clock-mco.md#std-dtcompatible-st-stm32-clock-mco) |
| Counter | on-chip | STM32 counters[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L543) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L175) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[12 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L232) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h7s78_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L395) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| I2S | on-chip | STM32H7 I2S controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L484) | [`st,stm32h7-i2s`](../../../../build/dts/api/bindings/i2s/st,stm32h7-i2s.md#std-dtcompatible-st-stm32h7-i2s) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h7s78_dk/stm32h7s78_dk.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | STM32H7RS External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L204) | [`st,stm32h7rs-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32h7rs-exti.md#std-dtcompatible-st-stm32h7rs-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32h7s78_dk/stm32h7s78_dk.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MMU / MPU | on-chip | ARMv7-M Memory Protection Unit (MPU)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L41) | [`arm,armv7m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv7m-mpu.md#std-dtcompatible-arm-armv7m-mpu) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L184) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L795) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L226) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L537)[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L520) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L198) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L772) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| Sensors | on-chip | STM32 family TEMP node for production calibrated sensors with two calibration temperatures[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L800) | [`st,stm32-temp-cal`](../../../../build/dts/api/bindings/sensor/st,stm32-temp-cal.md#std-dtcompatible-st-stm32-temp-cal) |
| on-chip | STM32 VBAT[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L812) | [`st,stm32-vbat`](../../../../build/dts/api/bindings/sensor/st,stm32-vbat.md#std-dtcompatible-st-stm32-vbat) |
| on-chip | STM32 VREF+[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L819) | [`st,stm32-vref`](../../../../build/dts/api/bindings/sensor/st,stm32-vref.md#std-dtcompatible-st-stm32-vref) |
| Serial controller | on-chip | STM32 USART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L329) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L353)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L361) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st,stm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L386) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L464)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L431) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st,stm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L49) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L527)[9 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L510) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L729) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 OTGFS controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L780) | [`st,stm32-otgfs`](../../../../build/dts/api/bindings/usb/st,stm32-otgfs.md#std-dtcompatible-st-stm32-otgfs) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L495) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/h7rs/stm32h7rs.dtsi?plain=1#L502) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Zephyr board options

The STM32HS7 is a SoC with Cortex-M7 architecture. Zephyr provides support
for building for Secure firmware.

The BOARD options are summarized below:

| BOARD | Description |
| --- | --- |
| stm32h7s78\_dk | For building Secure firmware |

### Connections and IOs

STM32H7S78-DK Discovery Board has 12 GPIO controllers. These controllers are responsible for pin muxing,
input/output, pull-up, etc.

For more details please refer to [STM32H7S78-DK Discovery board User Manual](https://www.st.com/en/evaluation-tools/stm32h7s78-dk.html).

#### Default Zephyr Peripheral Mapping:

- USART\_4 TX/RX : PD1/PD0 (VCP)
- USART\_7 TX/RX : PE8/PE7 (Arduino USART7)
- USER\_PB : PC13
- LD1 (green) : PO1
- LD2 (orange) : PO5
- LD3 (red) : PM2
- LD4 (blue) : PM3
- ADC1 channel 6 input : PF12
- USB OTG FS DM/DP : PM12/PM11

#### System Clock

STM32H7S78-DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
500MHz, driven by 24MHz external oscillator (HSE).

#### Serial Port

STM32H7S78-DK Discovery board has 2 U(S)ARTs. The Zephyr console output is
assigned to USART4. Default settings are 115200 8N1.

#### USB

STM32H7S78-DK Discovery board has 2 USB Type-C connectors. Currently, only
USB port2 (FS) is supported.

## Programming and Debugging

STM32H7S78-DK Discovery board includes an ST-LINK/V3E embedded debug tool interface.

Applications for the `stm32h7s78_dk` board configuration can be built and
flashed in the usual way (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

#### Flashing an application to STM32H7S78-DK Discovery

Connect the STM32H7S78-DK Discovery to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b stm32h7s78_dk samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! stm32h7s78_dk
```

### Debugging

You can debug an application in the usual way. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b stm32h7s78_dk samples/hello_world
west debug
```
