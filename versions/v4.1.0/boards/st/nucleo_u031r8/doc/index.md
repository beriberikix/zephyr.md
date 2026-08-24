---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/st/nucleo_u031r8/doc/index.html
original_path: boards/st/nucleo_u031r8/doc/index.html
---

# Nucleo U031R8

Board Overview

[![../../../../_images/nucleo_u031r8.jpg](https://docs.zephyrproject.org/4.1.0/_images/nucleo_u031r8.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/nucleo_u031r8.jpg)

Nucleo U031R8

Name:
:   `nucleo_u031r8`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u031xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_u031r8/doc/index.rst/../..)

## Overview

The Nucleo U031R8 board, featuring an ARM Cortex-M0+ based STM32U031R8 MCU,
provides an affordable and flexible way for users to try out new concepts and
build prototypes by choosing from the various combinations of performance and
power consumption features. Here are some highlights of the Nucleo U031R8
board:

- STM32U031R8 microcontroller in LQFP48 package
- Two types of extension resources:

  - Arduino Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32U0 I/Os
- On-board STLINK-V2EC debugger/programmer with USB re-enumeration
  capability: mass storage, Virtual COM port, and debug port
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
- User LED shared with ARDUINO® Uno V3
- Two push-buttons: USER and RESET
- USB Type-C® connector for the ST-LINK

More information about the board can be found at the [NUCLEO\_U031R8 website](https://www.st.com/en/evaluation-tools/nucleo-u031r8.html).

## Hardware

The STM32U031x4/6/8 devices are an ultra-low-power microcontrollers family (STM32U0
Series) based on the high-performance Arm® Cortex®-M0+ 32-bit RISC core.
They operate at a frequency of up to 56 MHz.

- Includes ST state-of-the-art patented technology
- Ultra-low-power with FlexPowerControl:

  - 1.71 V to 3.6 V power supply
  - -40 °C to +85/125 °C temperature range
  - 130 nA VBAT mode: supply for RTC, 9 x 32-bit backup registers
  - 16 nA Shutdown mode (4 wake-up pins)
  - 30 nA Standby mode (6 wake-up pins) without RTC
  - 160 nA Standby mode with RTC
  - 630 nA Stop 2 mode with RTC
  - 515 nA Stop 2 mode without RTC
  - 4 µA wake-up from Stop mode
  - 52 µA/MHz Run mode
  - Brownout reset
- Core:

  - 32-bit Arm® Cortex®-M0+ CPU, frequency up to 56 MHz
- ART Accelerator:

  - 1-Kbyte instruction cache allowing 0-wait-state execution from flash memory
- Benchmarks:

  - 1.13 DMIPS/MHz (Drystone 2.1)
  - 134 CoreMark® (2.4 CoreMark/MHz at 56 MHz)
  - 430 ULPMark™-CP
  - 167 ULPMark™-PP
  - 20.3 ULPMark™-CM
- Memories:

  - 64-Kbyte single bank flash memory, proprietary code readout protection
  - 12-Kbyte SRAM with hardware parity check
- General-purpose input/outputs:

  - Up to 53 fast I/Os, most of them 5 V‑tolerant
- Clock management:

  - 4 to 48 MHz crystal oscillator
  - 32 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (±1%)
  - Internal low-power 32 kHz RC (±5%)
  - Internal multispeed 100 kHz to 48 MHz oscillator,
    auto-trimmed by LSE (better than ±0.25 % accuracy)
  - PLL for system clock, ADC
- Security:

  - Customer code protection
  - Robust read out protection (RDP): 3 protection level states
    and password-based regression (128-bit PSWD)
  - Hardware protection feature (HDP)
  - Secure boot
  - True random number generation, candidate for NIST SP 800-90B certification
  - Candidate for Arm® PSA level 1 and SESIP level 3 certifications
  - 5 passive anti-tamper pins
  - 96-bit unique ID
- Up to 9 timers, RTC, and 2 watchdogs :

  - 1x 16-bit advanced motor-control, 1x 32-bit and 3x 16-bit general purpose,
    2x 16-bit basic, 2x low-power 16-bit timers (available in Stop mode),
    2x watchdogs, SysTick timer
  - RTC with hardware calendar, alarms and calibration
- Up to 16 communication peripherals:

  - 6x USARTs/LPUARTs (SPI, ISO 7816, LIN, IrDA, modem)
  - 3x I2C interfaces supporting Fast-mode and Fast-mode Plus (up to 1 Mbit/s)
  - 2x SPIs, plus 4x USARTs in SPI mode
  - IRTIM (Infrared interface)
- Rich analog peripherals (independent supply):

  - 1x 12-bit ADC (0.4 µs conversion time), up to 16-bit with hardware oversampling
  - 1x 12-bit DAC output channel, low-power sample and hold
  - 1x general-purpose operational amplifier with built-in PGA (variable gain up to 16)
  - 1x ultra-low-power comparator
- ECOPACK2 compliant packages

More information about STM32U031R8 can be found here:

- [STM32U031R8 on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u031r8)
- [STM32U031R8 reference manual](https://www.st.com/resource/en/reference_manual/rm0503-stm32u0-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_u031r8` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_u031r8/stm32u031xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M0+ CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L30) | [`arm,cortex-m0+`](../../../../build/dts/api/bindings/cpu/arm,cortex-m0+.md#std-dtcompatible-arm-cortex-m0) |
| ADC | on-chip | STM32 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L259) | [`st,stm32-adc`](../../../../build/dts/api/bindings/adc/st,stm32-adc.md#std-dtcompatible-st-stm32-adc) |
| Clock control | on-chip | STM32F0/G0 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L112) | [`st,stm32f0-rcc`](../../../../build/dts/api/bindings/clock/st,stm32f0-rcc.md#std-dtcompatible-st-stm32f0-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L44) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L50)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L57) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32 MSI Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L64) | [`st,stm32-msi-clock`](../../../../build/dts/api/bindings/clock/st,stm32-msi-clock.md#std-dtcompatible-st-stm32-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L71) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st,stm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| on-chip | STM32U0 Main PLL[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L86) | [`st,stm32u0-pll-clock`](../../../../build/dts/api/bindings/clock/st,stm32u0-pll-clock.md#std-dtcompatible-st-stm32u0-pll-clock) |
| Counter | on-chip | STM32 counters[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L417) | [`st,stm32-counter`](../../../../build/dts/api/bindings/counter/st,stm32-counter.md#std-dtcompatible-st-stm32-counter) |
| Cryptographic accelerator | on-chip | STM32 AES Accelerator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L380) | [`st,stm32-aes`](../../../../build/dts/api/bindings/crypto/st,stm32-aes.md#std-dtcompatible-st-stm32-aes) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L276) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st,stm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32 DMA controller (V2)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L320) | [`st,stm32-dma-v2`](../../../../build/dts/api/bindings/dma/st,stm32-dma-v2.md#std-dtcompatible-st-stm32-dma-v2) |
| on-chip | STM32 DMAMUX controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L331) | [`st,stm32-dmamux`](../../../../build/dts/api/bindings/dma/st,stm32-dmamux.md#std-dtcompatible-st-stm32-dmamux) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L94) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st,stm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L142) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st,stm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u031r8/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L284)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L308) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st,stm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u031r8/nucleo_u031r8.dts?plain=1#L35) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv6-M NVIC (Nested Vectored Interrupt Controller) controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L13) | [`arm,v6m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v6m-nvic.md#std-dtcompatible-arm-v6m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L124) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st,stm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u031r8/nucleo_u031r8.dts?plain=1#L27) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L102) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st,stm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L136) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st,stm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| PWM | on-chip | STM32 PWM[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L411)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L455) | [`st,stm32-pwm`](../../../../build/dts/api/bindings/pwm/st,stm32-pwm.md#std-dtcompatible-st-stm32-pwm) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L118) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st,stm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L372) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st,stm32-rng.md#std-dtcompatible-st-stm32-rng) |
| RTC | on-chip | STM32 RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L390) | [`st,stm32-rtc`](../../../../build/dts/api/bindings/rtc/st,stm32-rtc.md#std-dtcompatible-st-stm32-rtc) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L191)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L209) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st,stm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 LPUART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L227) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st,stm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32 SPI controller with embedded Rx and Tx FIFOs[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L342) | [`st,stm32-spi-fifo`](../../../../build/dts/api/bindings/spi/st,stm32-spi-fifo.md#std-dtcompatible-st-stm32-spi-fifo) |
| Timer | on-chip | ARMv6-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv6-m.dtsi?plain=1#L21) | [`arm,armv6m-systick`](../../../../build/dts/api/bindings/timer/arm,armv6m-systick.md#std-dtcompatible-arm-armv6m-systick) |
| on-chip | STM32 timers[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L401)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L445) | [`st,stm32-timers`](../../../../build/dts/api/bindings/timer/st,stm32-timers.md#std-dtcompatible-st-stm32-timers) |
| on-chip | STM32 low-power timer (LPTIM)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L533) | [`st,stm32-lptim`](../../../../build/dts/api/bindings/timer/st,stm32-lptim.md#std-dtcompatible-st-stm32-lptim) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L245) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u0/stm32u0.dtsi?plain=1#L251) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st,stm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo U031R8 Board has 10 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32U031 User Manual](https://www.st.com/resource/en/user_manual/um3261-stm32u0-series-safety-manual-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- DAC1\_OUT1 : PA4
- LD1 : PA5
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_2\_TX : PA2
- UART\_2\_RX : PA3
- USER\_PB : PC13

#### System Clock

Nucleo U031R8 System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
48MHz, driven by 4MHz medium speed internal oscillator.

#### Serial Port

Nucleo U031R8 board has 4 U(S)ARTs. The Zephyr console output is assigned to
USART2. Default settings are 115200 8N1.

## Programming and Debugging

Nucleo U031R8 board includes an ST-LINK/V3 embedded debug tool interface.
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

For pyOCD, additional target information needs to be installed
by executing the following pyOCD commands:

```shell
$ pyocd pack --update
$ pyocd pack --install stm32u0
```

#### Flashing an application to Nucleo U031R8

Connect the Nucleo U031R8 to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u031r8 samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_u031r8
```

### Debugging

Default flasher for this board is openocd. It could be used in the usual way.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u031r8 samples/basic/blinky
west debug
```

Note: Check the `build/tfm` directory to ensure that the commands required by these scripts
(`readlink`, etc.) are available on your system. Please also check `STM32_Programmer_CLI`
(which is used for initialization) is available in the PATH.
