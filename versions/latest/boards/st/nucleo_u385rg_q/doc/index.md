---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/st/nucleo_u385rg_q/doc/index.html
original_path: boards/st/nucleo_u385rg_q/doc/index.html
---

# Nucleo U385RG Q

Board Overview

[![../../../../_images/nucleo_u385rg_q.webp](../../../../_images/nucleo_u385rg_q.webp)
](../../../../_images/nucleo_u385rg_q.webp)

Nucleo U385RG Q

Name:
:   `nucleo_u385rg_q`

Vendor:
:   STMicroelectronics

Architecture:
:   arm

SoC:
:   stm32u385xx

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/st/nucleo_u385rg_q/doc/index.rst/../..)

## Overview

The Nucleo U385RG board, featuring an ARM® Cortex® -M33 with
TrustZone® based STM32U385RG MCU, provides an affordable and flexible
way for users to try out new concepts and build prototypes by choosing from
the various combinations of performance and power consumption features.
Here are some highlights of the Nucleo U385RG board:

- STM32U385RG microcontroller in an LQFP64 or LQFP48 package
- Two types of extension resources:

  - Arduino® Uno V3 connectivity
  - ST morpho extension pin headers for full access to all STM32U3 I/Os
- On-board STLINK-V2EC debugger/programmer with USB re-enumeration
  capability: mass storage, Virtual COM port, and debug port
- Flexible board power supply:

  - USB VBUS or external source(3.3V, 5V, 7 - 12V)
- Two push-buttons: USER and RESET
- 32.768 kHz crystal oscillator
- Second user LED shared with ARDUINO® Uno V3
- External or internal SMPS to generate Vcore logic supply
- 24 MHz or 48 MHz HSE
- User USB Device full speed, or USB SNK/UFP full speed
- Cryptography
- CAN FD transceiver
- Board connectors:

> - External SMPS experimentation dedicated connector
> - USB Type-C® , Micro-B, or Mini-B connector for the ST-LINK
> - USB Type-C® user connector
> - MIPI® debug connector
> - CAN FD header

More information about the board can be found at the [NUCLEO\_U385RG website](https://www.st.com/en/evaluation-tools/nucleo-u385rg.html).

## Hardware

The STM32U385xx devices are an ultra-low-power microcontrollers family (STM32U3
Series) based on the high-performance Arm® Cortex®-M33 32-bit RISC core.
They operate at a frequency of up to 96 MHz.

- Includes ST state-of-the-art patented technology
- Ultra-low-power with FlexPowerControl:

  - 1.71 V to 3.6 V power supply
  - -40 °C to +105 °C temperature range
  - VBAT mode: supply for RTC, 32 x 32-bit backup registers
  - 1.6 μA Stop 3 mode with 8-Kbyte SRAM
  - 2.2 μA Stop 3 mode with full SRAM
  - 3.8 μA Stop 2 mode with 8-Kbyte SRAM
  - 4.5 μA Stop 2 mode with full SRAM
  - 9.5 μA/MHz Run mode @ 3.3 V (While(1) SMPS step-down converter mode)
  - 13 μA/MHz Run mode @ 3.3 V/48 MHz (CoreMark® SMPS step-down converter mode)
  - 16 μA/MHz Run mode @ 3.3 V/96 MHz (CoreMark® SMPS step-down converter mode)
  - Brownout reset
- Core:

  - 32-bit Arm® Cortex®-M33 CPU with TrustZone® and FPU
- ART Accelerator:

  - 8-Kbyte instruction cache allowing 0-wait-state execution from flash and external memories:
    frequency up to 96 MHz, MPU, 144 DMIPS and DSP instructions
- Power management:

  - Embedded regulator (LDO) and SMPS step-down converter supporting switch on-the-fly and voltage scaling
- Benchmarks:

  - 1.5 DMIPS/MHz (Drystone 2.1)
  - 387 CoreMark® (4.09 CoreMark/MHz at 56 MHz)
  - 500 ULPMark™ -CP
  - 117 ULPMark™ -CM
  - 202000 SecureMark™ -TLS
- Memories:

  - 1-Mbyte flash memory with ECC, 2 banks read-while-write
  - 256 Kbytes of SRAM including 64 Kbytes with hardware parity check
  - OCTOSPI external memory interface supporting SRAM, PSRAM, NOR, NAND, and FRAM memories
- General-purpose input/outputs:

  - Up to 82 fast I/Os with interrupt capability most 5 V-tolerant and up to 14 I/Os with independent supply down to 1.08 V
- Clock management:

  - 4 to 50 MHz crystal oscillator
  - 32.768 kHz crystal oscillator for RTC (LSE)
  - Internal 16 MHz factory-trimmed RC (±1 %)
  - Internal low-power RC with frequency 32 kHz or 250 Hz (±5 %)
  - 2 internal multispeed 3 MHz to 96 MHz oscillators
  - Internal 48 MHz with clock recovery
  - Accurate MSI in PLL-mode and up to 96 MHz with 32.768 kHz, 16 MHz, or 32 MHz crystal oscillator
- Security and cryptography:

  - Arm® TrustZone® and securable I/Os, memories, and peripherals
  - Flexible life cycle scheme with RDP and password protected debug
  - Root of trust due to unique boot entry and secure hide protection area (HDP)
  - Secure firmware installation (SFI) from embedded root secure services (RSS)
  - Secure data storage with hardware unique key (HUK)
  - Secure firmware upgrade
  - Support of Trusted firmware for Cortex® M (TF-M)
  - Two AES coprocessors, one with side channel attack resistance (SCA) (SAES)
  - Public key accelerator, SCA resistant
  - Key hardware protection
  - Attestation keys
  - HASH hardware accelerator
  - True random number generator, NIST SP800-90B compliant
  - 96-bit unique ID
  - 512-byte OTP (one-time programmable)
  - Antitamper protection
- Up to 15 timers and 2 watchdogs :

  - 1x 16-bit advanced motor-control
  - 3x 32-bit and 3x 16-bit general purpose
  - 2x 16-bit basic
  - 4x low-power 16-bit timers (available in Stop mode)
  - 2x watchdogs
  - 2x SysTick timer
  - RTC with hardware calendar
  - Alarms
  - Calibration
- Up to 19 communication peripherals:

  - 1 USB 2.0 full-speed controller
  - 1 SAI (serial audio interface)
  - 3 I2C FM+(1 Mbit/s), SMBus/PMBus™
  - 2 I3C (SDR), with support of I2C FM+ mode
  - 2 USARTs and 2 UARTs (SPI, ISO 7816, LIN, IrDA, modem), 1 LPUART
  - 3 SPIs (6 SPIs including 1 with OCTOSPI + 2 with USART)
  - 1 CAN FD controller
  - 1 SDMMC interface
  - 1 audio digital filter with sound-activity detection
- 12-channel GPDMA controller, functional in Sleep and Stop modes (up to Stop 2)
- Up to 21 capacitive sensing channels:

  - Support touch key, linear, and rotary touch sensors
- Rich analog peripherals (independent supply):

  - 2x 12-bit ADC 2.5 Msps, with hardware oversampling
  - 12-bit DAC module with 2 D/A converters, low-power sample and hold, autonomous in Stop 1 mode
  - 2 operational amplifiers with built-in PGA
  - 2 ultralow-power comparators
- CRC calculation unit
- Debug:

  - Development support: serial-wire debug (SWD), JTAG, Embedded Trace Macrocell™ (ETM)
- ECOPACK2 compliant packages

More information about STM32U385RG can be found here:

- [STM32U385RG on www.st.com](https://www.st.com/en/microcontrollers-microprocessors/stm32u385rg)
- [STM32U385RG reference manual](https://www.st.com/resource/en/reference_manual/rm0487-stm32u3-series-armbased-32bit-mcus-stmicroelectronics.pdf)

### Supported Features

The `nucleo_u385rg_q` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `nucleo_u385rg_q/stm32u385xx` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M33 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L27) | [`arm,cortex-m33`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m33.md#std-dtcompatible-arm-cortex-m33) |
| ADC | on-chip | STM32N6 ADC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L240)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L256) | [`st,stm32n6-adc`](../../../../build/dts/api/bindings/adc/st%2Cstm32n6-adc.md#std-dtcompatible-st-stm32n6-adc) |
| Clock control | on-chip | STM32U5 RCC (Reset and Clock controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L108) | [`st,stm32u5-rcc`](../../../../build/dts/api/bindings/clock/st%2Cstm32u5-rcc.md#std-dtcompatible-st-stm32u5-rcc) |
| on-chip | STM32 HSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L39) | [`st,stm32-hse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-hse-clock.md#std-dtcompatible-st-stm32-hse-clock) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L45)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L52) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | STM32U3 Multi Speed Internal Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L59)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L66) | [`st,stm32u3-msi-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32u3-msi-clock.md#std-dtcompatible-st-stm32u3-msi-clock) |
| on-chip | STM32 LSE Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L73) | [`st,stm32-lse-clock`](../../../../build/dts/api/bindings/clock/st%2Cstm32-lse-clock.md#std-dtcompatible-st-stm32-lse-clock) |
| DAC | on-chip | STM32 family DAC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L272) | [`st,stm32-dac`](../../../../build/dts/api/bindings/dac/st%2Cstm32-dac.md#std-dtcompatible-st-stm32-dac) |
| DMA | on-chip | STM32U5 DMA controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L324) | [`st,stm32u5-dma`](../../../../build/dts/api/bindings/dma/st%2Cstm32u5-dma.md#std-dtcompatible-st-stm32u5-dma) |
| Flash controller | on-chip | STM32 Family flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L90) | [`st,stm32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/st%2Cstm32-flash-controller.md#std-dtcompatible-st-stm32-flash-controller) |
| GPIO & Headers | on-chip | STM32 GPIO Controller[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L147) | [`st,stm32-gpio`](../../../../build/dts/api/bindings/gpio/st%2Cstm32-gpio.md#std-dtcompatible-st-stm32-gpio) |
| on-board | GPIO pins exposed on Arduino Uno (R3) headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/arduino_r3_connector.dtsi?plain=1#L8) | [`arduino-header-r3`](../../../../build/dts/api/bindings/gpio/arduino-header-r3.md#std-dtcompatible-arduino-header-r3) |
| I2C | on-chip | STM32 I2C V2 controller[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L280) | [`st,stm32-i2c-v2`](../../../../build/dts/api/bindings/i2c/st%2Cstm32-i2c-v2.md#std-dtcompatible-st-stm32-i2c-v2) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L34) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| on-chip | STM32G0 External Interrupt Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L120) | [`st,stm32g0-exti`](../../../../build/dts/api/bindings/interrupt-controller/st%2Cstm32g0-exti.md#std-dtcompatible-st-stm32g0-exti) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | STM32 flash memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L98) | [`st,stm32-nv-flash`](../../../../build/dts/api/bindings/mtd/st%2Cstm32-nv-flash.md#std-dtcompatible-st-stm32-nv-flash) |
| on-board | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/st/nucleo_u385rg_q/nucleo_u385rg_q.dts?plain=1#L52) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | STM32 Pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L141) | [`st,stm32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/st%2Cstm32-pinctrl.md#std-dtcompatible-st-stm32-pinctrl) |
| Reset controller | on-chip | STM32 Reset and Clock Control (RCC) Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L114) | [`st,stm32-rcc-rctl`](../../../../build/dts/api/bindings/reset/st%2Cstm32-rcc-rctl.md#std-dtcompatible-st-stm32-rcc-rctl) |
| RNG | on-chip | STM32 Random Number Generator[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L316) | [`st,stm32-rng`](../../../../build/dts/api/bindings/rng/st%2Cstm32-rng.md#std-dtcompatible-st-stm32-rng) |
| Serial controller | on-chip | STM32 USART[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L204) | [`st,stm32-usart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-usart.md#std-dtcompatible-st-stm32-usart) |
| on-chip | STM32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L222) | [`st,stm32-uart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-uart.md#std-dtcompatible-st-stm32-uart) |
| on-chip | STM32 LPUART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L231) | [`st,stm32-lpuart`](../../../../build/dts/api/bindings/serial/st%2Cstm32-lpuart.md#std-dtcompatible-st-stm32-lpuart) |
| SPI | on-chip | STM32H7 SPI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L357)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L337) | [`st,stm32h7-spi`](../../../../build/dts/api/bindings/spi/st%2Cstm32h7-spi.md#std-dtcompatible-st-stm32h7-spi) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |
| Watchdog | on-chip | STM32 watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L367) | [`st,stm32-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-watchdog.md#std-dtcompatible-st-stm32-watchdog) |
| on-chip | STM32 system window watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/st/u3/stm32u3.dtsi?plain=1#L373) | [`st,stm32-window-watchdog`](../../../../build/dts/api/bindings/watchdog/st%2Cstm32-window-watchdog.md#std-dtcompatible-st-stm32-window-watchdog) |

### Connections and IOs

Nucleo U385RG Board has 14 GPIO controllers. These controllers are responsible
for pin muxing, input/output, pull-up, etc.

For more details please refer to [STM32U385RG board user manual](https://www.st.com/resource/en/user_manual/um3062-stm32u3u5-nucleo64-board-mb1841-stmicroelectronics.pdf).

#### Default Zephyr Peripheral Mapping:

- DAC1\_OUT1 : PA4
- I2C1 SCL/SDA : PB6/PB7 (Arduino I2C)
- LD4 : PA5
- LPUART\_1\_TX : PA2
- LPUART\_1\_RX : PA3
- SPI3 NSS/SCK/MISO/MOSI : PA15/PB3/PB4/PB5 (Arduino SPI)
- UART\_1\_TX : PA9
- UART\_1\_RX : PA10
- UART\_3\_TX : PC10
- UART\_3\_RX : PC11
- USER\_PB : PC13

#### System Clock

Nucleo U385RG System Clock could be driven by internal or external oscillator,
as well as main PLL clock. By default System clock is driven by PLL clock at
48MHz, driven by 4MHz medium speed internal oscillator.

#### Serial Port

Nucleo U385RG board has 4 U(S)ARTs, 1 LPUART. The Zephyr console output is assigned to
USART1. Default settings are 115200 8N1.

## Programming and Debugging

The `nucleo_u385rg_q` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[pyocd](../../../../develop/flash_debug/host-tools.md#runner-pyocd)** | ✅ | ✅ (default) | ✅ | ✅ | ✅ |
| **[stm32cubeprogrammer](../../../../develop/flash_debug/host-tools.md#runner-stm32cubeprogrammer)** | ✅ (default) |  |  |  |  |

Nucleo U385RG board includes an ST-LINK/V3 embedded debug tool interface.
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
$ pyocd pack --install stm32u3
```

#### Flashing an application to Nucleo U385RG

Connect the Nucleo U385RG to your host computer using the USB port.
Then build and flash an application. Here is an example for the
[Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

Run a serial host program to connect with your Nucleo board:

```shell
$ minicom -D /dev/ttyACM0
```

Then build and flash the application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u385rg_q samples/hello_world
west flash
```

You should see the following message on the console:

```shell
Hello World! nucleo_u385rg_q
```

### Debugging

Default debugger for this board is OpenOCD. It can be used in the usual way.
Here is an example for the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b nucleo_u385rg_q samples/basic/blinky
west debug
```

Note: Check the `build/tfm` directory to ensure that the commands required by these scripts
(`readlink`, etc.) are available on your system. Please also check `STM32_Programmer_CLI`
(which is used for initialization) is available in the PATH.
