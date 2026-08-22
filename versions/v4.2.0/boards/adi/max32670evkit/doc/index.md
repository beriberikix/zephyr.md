---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32670evkit/doc/index.html
original_path: boards/adi/max32670evkit/doc/index.html
---

# MAX32670EVKIT

Board Overview

[![../../../../_images/max32670evkit.webp](../../../../_images/max32670evkit.webp)
](../../../../_images/max32670evkit.webp)

MAX32670EVKIT

Name:
:   `max32670evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32670

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32670evkit/doc/index.rst/../..)

## Overview

The MAX32670 evaluation kit (EV kit) provides a platform for evaluation capabilities
of the MAX32670. The MAX32670 is an ultra-low-power, cost-effective, highly reliable
32-bit microcontroller that enables designs with complex sensor processing without
compromising battery life. It combines a flexible and versatile power management unit
with the powerful Arm® Cortex®-M4 core with floating point unit (FPU).
The MAX32670 also offers legacy designs an easy and cost optimal upgradepath
from 8-bit or 16-bit microcontrollers.

The Zephyr port is running on the MAX32670 MCU.

## Hardware

- MAX32670 MCU:

  - High-Efficiency Microcontroller for Low-Power, High-Reliability Devices

    - Arm Cortex-M4 Core with FPU up to 100MHz
    - 384KB Flash Memory with Error Correction
    - 160KB SRAM (128KB with ECC Enabled),Optionally Preserved in Lowest Power Modes
    - 16KB Unified Cache with ECC
    - UART Bootloader

      > - Dual- or Single-Supply Operation
      > - Ultra-Low 0.9V to 1.1V VCORE Supply Voltage
      > - Internal LDO Operation from 1.7V to 3.6V SingleSupply
    - Wide Operating Temperature: -40°C to +105°C
  - Flexible Clocking Schemes

    - Internal High-Speed 100MHz Oscillator
    - Internal Low-Power 7.3728MHz and Ultra-Low-Power 80kHz Oscillators
    - 16MHz to 32MHz Oscillator (External CrystalRequired)
    - 32.768kHz Oscillator (External Crystal Required)
    - External Clock Input for the Core
    - External Clock Input for the LPUART and LPTMR
  - Power Management Maximizes Uptime for Battery Applications

    - 44μA/MHz Active at 0.9V up to 12MHz
    - 50μA/MHz Active at 1.1V up to 100MHz
    - 2.6μA Full Memory Retention Power in BACKUPMode at VDD = 1.8V
    - 350nA Ultra-Low-Power RTC at VDD = 1.8V
    - Wake from LPUART or LPTMR
  - Optimal Peripheral Mix Provides Platform Scalability

    - Up to 31 General-Purpose I/O Pins
    - Up to Three SPI Master/Slave (up to 50MHz)
    - Up to Three 4-Wire UART
    - One Low-Power UART (LPUART)
    - Up to Three I2C Master/Slave 3.4Mbps High Speed
    - 8-Channel Standard DMA Controller
    - Up to Four 32-Bit Timers (TMR)
    - Up to Two Low-Power 32-Bit Timers (LPTMR)
    - Two Windowed Watchdog Timers
    - One I2S Slave for Digital Audio Interface
  - Security and Integrity

    - Available Secure Boot
    - AES 128/192/256 Hardware Acceleration Engine
    - 32-Bit CRC Acceleration Engine
- Benefits and Features of MAX32670EVKIT:

  - USB 2.0 Micro B to Serial UART Bridge
  - UART0 and UART3 Interface is Selectable Through On-Board Jumpers
  - On-Board MAX32625PICO-Based Debugger
  - Boot Load Enable Circuitry
  - SPI and I2C Signals Accessed Through 0.1in Headers
  - GPIOs and Miscellaneous Signals Accessed Through 0.1in Headers
  - Board Power Provided by USB Port
  - On-Board SIMO Regulator and LDO for IC and Peripherals
  - Individual Power Measurement on all IC Rails Through Jumpers
  - Two General-Purpose LED and One GeneralPurpose Pushbutton Switch

### Supported Features

The `max32670evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32670evkit/max32670` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC 10-Bits[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-10b`](../../../../build/dts/api/bindings/adc/adi%2Cmax32-adc-10b.md#std-dtcompatible-adi-max32-adc-10b) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi%2Cmax32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L60) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L153) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi%2Cmax32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L76) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi%2Cmax32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi%2Cmax32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi%2Cmax32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi%2Cmax32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32670evkit/max32670evkit.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32670evkit/max32670evkit.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi%2Cmax32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi%2Cmax32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi%2Cmax32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi%2Cmax32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L95)[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L105) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi%2Cmax32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi%2Cmax32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32670.dtsi?plain=1#L86) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi%2Cmax32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | P0\_22 | | Open | | --- | | Close | | | Disconnects red LED from P0\_22. | | --- | | Connects red to P0\_22. | |
| JP2 | P0\_23 | | Open | | --- | | Close | | | Disconnects green LED from P0\_23. | | --- | | Connects green LED to P0\_23. | |
| JP3 | P0\_20 P0\_26 | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial port P0\_8 (UART0\_RX). | | --- | | Connects the USB to serial port P0\_26 (LPUART0\_RX). | |
| JP4 | P0\_9 P0\_27 | | 2-1 | | --- | | 2-3 | | | Connects the USB to serial port P0\_9 (UART0\_TX). | | --- | | Connects the USB to serial port P0\_27 (LPUART0\_TX). | |
| JP5 | VDD | | Open | | --- | | Close | | | Disconnects power to VDD. | | --- | | Connects power to VDD. | |
| JP6 | VCORE | | Open | | --- | | Close | | | Disconnects power to VCORE. | | --- | | Connects power to VCORE. | |
| JP7 | SIMO RSEL2 | | 1-2 | | --- | | 3-4 | | 5-6 | | | Sets output 2 of the SIMO regulator to 0.9V. | | --- | | Sets output 2 of the SIMO regulator to 1.0V. | | Sets output 2 of the SIMO regulator to 1.1V. | |

## Programming and Debugging

The `max32670evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

The MAX32670 EVKIT integrates a MAX32625PICO based debugger for DAPLink functionality.

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32670EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32670evkit.html)
