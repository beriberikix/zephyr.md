---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/stm32u083c_dk/doc/index.html
original_path: boards/st/stm32u083c_dk/doc/index.html
---

# STM32U083C-DK

Board Overview

[![../../../../_images/stm32u083c_dk.jpg](../../../../_images/stm32u083c_dk.jpg)
](../../../../_images/stm32u083c_dk.jpg)

STM32U083C-DK

Name:
:   `stm32u083c_dk`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u083xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/stm32u083c_dk/doc/index.rst/../..)

## Overview

The STM32U083C\_DK board, featuring an ARM Cortex-M0+ based STM32U083MC MCU,
provides an affordable and flexible way for users to try out new concepts and
build prototypes by choosing from the various combinations of performance and
power consumption features. Here are some highlights of the STM32U083C\_DK
board:

- Ultra-low-power STM32U083MC microcontroller based on the Arm® Cortex®‑M0+ core,
  featuring 256 Kbytes of flash memory and 40 Kbytes of SRAM in an LQFP80 package.
- Board connectors:

  - ST-LINK USB Type-C connector
  - User USB Device with USB Type-C connector
  - mikroBUS connectors
  - MIPI debug in connector (Arm® Cortex® 10‑pin 1.27 mm‑pitch
    debug connector over STDC14 footprint)
  - Extension connectors for full access to all STM32 I/Os
  - VBAT dedicated connector provides the capability to power the board on a battery
- Flexible power-supply options:

  - ST-LINK USB VBUS, USB connector, or external sources
- 4×24-segment LCD
- Three user LEDs
- Reset push-button
- User joystick
- Touchkey
- Temperature sensor

More information about the board can be found at the [STM32U083\_DK website](https://www.st.com/en/evaluation-tools/stm32u083c-dk.html).

## Hardware

The STM32U083xC devices are an ultra-low-power microcontrollers family (STM32U0
Series) based on the high-performance Arm® Cortex®-M0+ 32-bit RISC core.
They operate at a frequency of up to 56 MHz.

- Includes ST state-of-the-art patented technology
- Ultra-low-power with FlexPowerControl:

  - 1.71 V to 3.6 V power supply
  - -40 °C to +85/125 °C temperature range
  - 130 nA VBAT mode: supply for RTC, 9 x 32-bit backup registers
  - 16 nA Shutdown mode (6 wake-up pins)
  - 30 nA Standby mode (6 wake-up pins) without RTC
  - 160 nA Standby mode with RTC
  - 825 nA Stop 2 mode with RTC
  - 695 nA Stop 2 mode without RTC
  - 4 µA wake-up from Stop mode
  - 52 µA/MHz Run mode (LDO mode)
  - Brownout reset
- Core:

  - 32-bit Arm® Cortex®-M0+ CPU, frequency up to 56 MHz
- ART Accelerator:

  - 1-Kbyte instruction cache allowing 0-wait-state execution from flash memory
- Benchmarks:

  - 1.13 DMIPS/MHz (Drystone 2.1)
  - 134 CoreMark® (2.4 CoreMark/MHz at 56 MHz)
  - 407 ULPMark™-CP
  - 143 ULPMark™-PP
  - 19.7 ULPMark™-CM
- Memories:

  - 256-Kbyte single bank flash memory, proprietary code readout protection
  - 40-Kbyte SRAM with hardware parity check
- General-purpose input/outputs:

  - Up to 69 fast I/Os, most of them 5 V‑tolerant
- Clock management:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (±1%)
  - Internal low-power 32 kHz RC (±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator,
    auto-trimmed by LSE (better than ±0.25 % accuracy)
  - Internal 48 MHz with clock recovery
  - PLL for system clock, USB, ADC
- Security:

  - Customer code protection
  - Robust read out protection (RDP): 3 protection level states
    and password-based regression (128-bit PSWD)
  - Hardware protection feature (HDP)
  - Secure boot
  - AES: 128/256-bit key encryption hardware accelerator
  - True random number generation, candidate for NIST SP 800-90B certification
  - Candidate for Arm® PSA level 1 and SESIP level 3 certifications
  - 5 passive anti-tamper pins
  - 96-bit unique ID
- Up to 10 timers, 2 watchdogs and RTC:

  - 1x 16-bit advanced motor-control, 1x 32-bit and 3x 16-bit general purpose,
    2x 16-bit basic, 3x low-power 16-bit timers (available in Stop mode),
    2x watchdogs, SysTick timer
  - RTC with hardware calendar, alarms and calibration
- Up to 20 communication peripherals:

  - 1 USB 2.0 full-speed crystal-less solution with LPM and BCD
  - 7 USARTs/LPUARTs (SPI, ISO 7816, LIN, IrDA, modem)
  - 4 I2C interfaces supporting Fast-mode and Fast-mode Plus (up to 1 Mbit/s)
  - 3 SPIs, plus 4x USARTs in SPI mode
  - IRTIM (Infrared interface)
- Rich analog peripherals (independent supply):

  - 1x 12-bit ADC (0.4 µs conversion time), up to 16-bit with hardware oversampling
  - 1x 12-bit DAC output channel, low-power sample and hold
  - 1x general-purpose operational amplifier with built-in PGA (variable gain up to 16)
  - 2x ultra-low-power comparators
- LCD driver:
  - 8\*48 or 4\*52 segments, with step-up converter
- General-purpose inputs/outputs:
  - Up to 69 fast I/Os, most of them 5 V-tolerant
- ECOPACK2 compliant packages

More information about STM32U083MC can be found here:

- [STM32U083MC on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u083mc)
- [STM32U083 reference manual](https://www.st.com/resource/en/reference_manual/rm0503-stm32u0-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `stm32u083c_dk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `stm32u083c_dk/stm32u083xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L30) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m0%2B.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L282) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L135) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L67) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L73)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L80) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L87) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L94) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U0 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L109) | [`st,stm32u0-pll-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u0-pll-clock.md#std-dtcompatible-st-stm32u0-pll-clock) |
| Counter | on-chip | STM32 counters[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L440) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st%2Cstm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L403) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st%2Cstm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L299) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L343) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L354) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st%2Cstm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L117) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L165) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32u083c_dk/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L307)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L331) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-chip | STM32 Tocuh Sensing Controller (TSC) driver[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L579) | [`st,stm32-tsc`](../../../../build/dts/api/bindings/input/st%2Cstm32-tsc.md#std-dtcompatible-st-stm32-tsc) |
| on-board | Input driver for STM32 Tocuh Sensing Controller (TSC)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32u083c_dk/stm32u083c_dk.dts?plain=1#L168) | [`tsc-keys`](../../../../build/dts/api/bindings/input/tsc-keys.md#std-dtcompatible-tsc-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L147) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/stm32u083c_dk/stm32u083c_dk.dts?plain=1#L28) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L125) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| PHY | on-chip | This binding is to be used by all the usb transceivers which are built-in with USB IP[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u073.dtsi?plain=1#L75) | [`usb-nop-xceiv`](../../../../build/dts/api/bindings/phy/usb-nop-xceiv.md#std-dtcompatible-usb-nop-xceiv) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L159) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L434)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L478) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st%2Cstm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L141) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L395) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L413) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st%2Cstm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L223)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L214) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L250) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L385)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L365) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st%2Cstm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L424)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L468) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st%2Cstm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L568)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L556) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st%2Cstm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| USB | on-chip | STM32 USB controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u073.dtsi?plain=1#L51) | [`st,stm32-usb`](../../../../build/dts/api/bindings/usb/st%2Cstm32-usb.md#std-dtcompatible-st-stm32-usb) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L268) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L274) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

STM32U083C\_DK Board has 10 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32U083MC User Manual](https://www.st.com/resource/en/user_manual/um3292-discovery-kit-with-STM32U083MC-MCU.pdf).

#### Default Zephyr Peripheral Mapping:

- ADC1\_IN8 : PA4
- I2C1\_SCL : PB8
- I2C1\_SDA : PB9
- LPUART\_1\_TX : PG7
- LPUART\_1\_RX : PG8
- SPI1\_NSS : PA4
- SPI1\_SCK : PA5
- SPI1\_MISO : PA6
- SPI1\_MOSI : PA7
- SPI1\_CS : PA15
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3

#### System Clock

STM32U083C\_DK System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
48MHz, driven by 4MHz medium speed internal oscillator.

#### Serial Port

STM32U083C\_DK board has 7 U(S)ARTs. The Zephyr console output is assigned to
USART2. Default settings are 115200 8N1.

## Programming and Debugging

The `stm32u083c_dk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

STM32U083C\_DK board includes an ST-LINK/V3 embedded debug tool interface.
This probe allows to flash the board using various tools.

### Flashing

The board is configured to be flashed using west [STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) runner,
so its [installation](../../../../develop/flash_debug/host-tools.md#stm32cubeprog-flash-host-tools) is required.

Alternatively, JLink or pyOCD can also be used to flash the board using
the `--runner` (or `-r`) option:

```shell
$ west flash --runner pyocd
$ west flash --runner jlink
```

For pyOCD, additional target information needs to be installed.
This can be done by executing the following commands.

```shell
$ pyocd pack --update
$ pyocd pack --install stm32u0
```

#### Flashing an application to STM32U083C\_DK

Connect the STM32U083C\_DK to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b stm32u083c_dk samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! stm32u083c_dk/stm32u083xx
```

### Debugging

Default flasher for this board is openocd. It could be used in the usual way.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u083rc samples/basic/blinky
west debug
```

Note: Check the `build/tfm` directory to ensure that the commands required by these scripts
(`readlink`, etc.) are available on your system. Please also check `STM32_Programmer_CLI`
(which is used for initialization) is available in the PATH.
