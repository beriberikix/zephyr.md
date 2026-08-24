---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/adi/max32662evkit/doc/index.html
original_path: boards/adi/max32662evkit/doc/index.html
---

# MAX32662EVKIT

Board Overview

[![../../../../_images/max32662evkit.webp](https://docs.zephyrproject.org/4.2.0/_images/max32662evkit.webp)
](https://docs.zephyrproject.org/4.2.0/_images/max32662evkit.webp)

MAX32662EVKIT

Name:
:   `max32662evkit`

Vendor:
:   Analog Devices, Inc.

Architecture:
:   arm

SoC:
:   max32662

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/adi/max32662evkit/doc/index.rst/../..)

## Overview

The MAX32662 evaluation kit (EV kit) provides a platform for evaluating
the capabilities of the MAX32662 microcontroller, which is a cost-effective,
ultra-low power, highly integrated 32-bit microcontroller designed
for battery-powered edge devices.

The Zephyr port is running on the MAX32662 MCU.

## Hardware

- MAX32662 MCU:

  - High-Efficiency Microcontroller for Low-Power High-Reliability Devices

    - 256KB Flash
    - 80KB SRAM, Optionally Preserved in LowestPower BACKUP Mode
    - 16KB Unified Cache
    - Memory Protection Unit (MPU)
    - Dual- or Single-Supply Operation: 1.7V to 3.6V
    - Wide Operating Temperature: -40°C to +105°C
  - Flexible Clocking Schemes

    - Internal High-Speed 100MHz
    - Internal Low-Power 7.3728MHz
    - Ultra-Low-Power 80kHz
    - 16MHz–32MHz (External Crystal Required)
    - 32.768kHz (External Crystal Required)
    - External Clock Inputs for CPU and Low-PowerTimer
  - Power Management Maximizes Uptime for Battery Applications

    - 50μA/MHz at 0.9V up to 12MHz (CoreMark®) inACTIVE Mode
    - 44μA/MHz at 1.1V up to 100MHz (While(1)) inACTIVE Mode
    - 2.15μA Full Memory Retention Current in BACKUPMode at VDDIO = 1.8V
    - 2.4μA Full Memory Retention Current in BACKUPMode at VDDIO = 3.3V
    - 350nA Ultra-Low-Power RTC
    - Wakeup from Low-Power Timer
  - Optimal Peripheral Mix Provides Platform Scalability

    - Up to 21 General-Purpose I/O Pins
    - 4-Channel, 12-Bit, 1Msps ADC
    - Two SPI Controller/Target
    - One I2S Controller/Target
    - Two 4-Wire UART
    - Two I2C Controller/Target
    - One CAN 2.0B Controller
    - 4-Channel Standard DMA Controller
    - Three 32-Bit Timers
    - One 32-Bit Low-Power Timer
    - One Watchdog Timer
    - CMOS-Level 32.768kHz Calibration Output
    - AES-128/192/256 Hardware Accelerator
- Benefits and Features of MAX32662EVKIT:

  - 3-Pin Terminal Block for CAN Bus 2.0B
  - 128 x 128 (1.45in) Color TFT Display with SPI Interface
  - Selectable On-Board High-Precision Voltage Reference
  - USB 2.0 Micro-B to Serial UART
  - All GPIOs Signals Accessed through 0.1in Headers
  - Four Analog Inputs Accessed through 0.1in Header
  - SWD 10-Pin Header
  - Board Power Provided by USB Port
  - On-Board LDO Regulators
  - Individual Power Measurement on All IC Rails through Jumpers
  - One General-Purpose LED
  - One General-Purpose Pushbutton Switch

### Supported Features

The `max32662evkit` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `max32662evkit/max32662` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4F CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L25) | [`arm,cortex-m4f`](../../../../build/dts/api/bindings/cpu/arm,cortex-m4f.md#std-dtcompatible-arm-cortex-m4f) |
| ADC | on-chip | ADI MAX32 ADC SAR[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L230) | [`adi,max32-adc-sar`](../../../../build/dts/api/bindings/adc/adi,max32-adc-sar.md#std-dtcompatible-adi-max32-adc-sar) |
| CAN | on-chip | ADI MAX32 CAN Node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L131) | [`adi,max32-can`](../../../../build/dts/api/bindings/can/adi,max32-can.md#std-dtcompatible-adi-max32-can) |
| Clock control | on-chip | MAX32 Global Control[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L118) | [`adi,max32-gcr`](../../../../build/dts/api/bindings/clock/adi,max32-gcr.md#std-dtcompatible-adi-max32-gcr) |
| on-chip | Generic fixed-rate clock provider[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L53)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L67) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| Counter | on-chip | ADI MAX32 counter[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L250) | [`adi,max32-counter`](../../../../build/dts/api/bindings/counter/adi,max32-counter.md#std-dtcompatible-adi-max32-counter) |
| on-chip | ADI MAX32 compatible Counter RTC[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L124) | [`adi,max32-rtc-counter`](../../../../build/dts/api/bindings/counter/adi,max32-rtc-counter.md#std-dtcompatible-adi-max32-rtc-counter) |
| Display | on-board | Sitronix ST7735X display controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L62) | [`sitronix,st7735r`](../../../../build/dts/api/bindings/display/sitronix,st7735r.md#std-dtcompatible-sitronix-st7735r) |
| DMA | on-chip | ADI MAX32 DMA[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L80) | [`adi,max32-dma`](../../../../build/dts/api/bindings/dma/adi,max32-dma.md#std-dtcompatible-adi-max32-dma) |
| Flash controller | on-chip | MAX32XXX flash controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L102) | [`adi,max32-flash-controller`](../../../../build/dts/api/bindings/flash_controller/adi,max32-flash-controller.md#std-dtcompatible-adi-max32-flash-controller) |
| GPIO & Headers | on-chip | MAX32 GPIO[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L166) | [`adi,max32-gpio`](../../../../build/dts/api/bindings/gpio/adi,max32-gpio.md#std-dtcompatible-adi-max32-gpio) |
| I2C | on-chip | ADI MAX32 I2C[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L138)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L127) | [`adi,max32-i2c`](../../../../build/dts/api/bindings/i2c/adi,max32-i2c.md#std-dtcompatible-adi-max32-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L37) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/adi/max32662evkit/max32662evkit.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| MTD | on-chip | Flash node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L110) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | MAX32 Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L160) | [`adi,max32-pinctrl`](../../../../build/dts/api/bindings/pinctrl/adi,max32-pinctrl.md#std-dtcompatible-adi-max32-pinctrl) |
| PWM | on-chip | ADI MAX32 PWM[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L254) | [`adi,max32-pwm`](../../../../build/dts/api/bindings/pwm/adi,max32-pwm.md#std-dtcompatible-adi-max32-pwm) |
| RNG | on-chip | ADI MAX32XXX TRNG[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L214) | [`adi,max32-trng`](../../../../build/dts/api/bindings/rng/adi,max32-trng.md#std-dtcompatible-adi-max32-trng) |
| Serial controller | on-chip | MAX32 UART[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L187)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L196) | [`adi,max32-uart`](../../../../build/dts/api/bindings/serial/adi,max32-uart.md#std-dtcompatible-adi-max32-uart) |
| SPI | on-chip | ADI MAX32 SPI[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32662.dtsi?plain=1#L90) | [`adi,max32-spi`](../../../../build/dts/api/bindings/spi/adi,max32-spi.md#std-dtcompatible-adi-max32-spi) |
| SRAM | on-chip | Generic on-chip SRAM[8 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L97) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm,armv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |
| on-chip | ADI MAX32 timer[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L242) | [`adi,max32-timer`](../../../../build/dts/api/bindings/timer/adi,max32-timer.md#std-dtcompatible-adi-max32-timer) |
| Watchdog | on-chip | MAX32XXX watchdog[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/adi/max32/max32xxx.dtsi?plain=1#L221) | [`adi,max32-watchdog`](../../../../build/dts/api/bindings/watchdog/adi,max32-watchdog.md#std-dtcompatible-adi-max32-watchdog) |

### Connections and IOs

| Name | Name | Settings | Description |
| --- | --- | --- | --- |
| JP1 | VREF EN | | 1-2 | | --- | | Open | | | Connects the external voltage reference to the VREF pin; must be enabled in the software. See the External Voltage Reference (VREF) section for additional information. | | --- | | Disconnects the external voltage reference. | |
| JP2 | I2C1\_SCL\_PU | | 1-2 | | --- | | Open | | | Connects the pull-up to I2C1A\_SCL (P0.6); sourced by V\_AUX. | | --- | | Disconnects the pull-up from I2C1A\_SCL (P0.6); sourced by V\_AUX. | |
| JP3 | N/A | N/A | Does not exist. |
| JP4 | I2C1\_SDA\_PU | | 1-2 | | --- | | Oepn | | | Connects the pull-up to I2C1A\_SDA (P0.9); sourced by V\_AUX. | | --- | | Disconnects the pull-up from I2C1A\_SDA (P0.9); sourced by V\_AUX. | |
| JP5 | LED0 EN | | 1-2 | | --- | | Open | | | Enables LED0. | | --- | | Disables LED0. | |
| JP6 | CTS0A EN | | 1-2 | | --- | | Open | | | Connects the USB-to-serial bridge to UART0A\_CTS (P0.20). | | --- | | Disconnects the USB-to-serial bridge from UART0A\_CTS (P0.20). | |
| JP7 | RX0A EN | | 1-2 | | --- | | Open | | | Connects the USB-to-serial bridge to UART0A\_RX (P0.11). | | --- | | Disconnects the USB-to-serial bridge from UART0A\_RX (P0.11). | |
| JP8 | TX0A EN | | 1-2 | | --- | | Open | | | Connects the USB-to-serial bridge to UART0A\_TX (P0.10). | | --- | | Disconnects the USB-to-serial bridge from UART0A\_TX (P0.10). | |
| JP9 | RTS0A EN | | 1-2 | | --- | | Open | | | Connects the USB-to-serial bridge to UART0A\_RTS (P0.19). | | --- | | Disconnects the USB-to-serial bridge from UART0A\_RTS (P0.19). | |
| JP10 | VCORE EN | | 1-2 | | --- | | Open | | | Connects 1V1 to VCORE. | | --- | | Disconnects 1V1 from VCORE. | |
| JP11 | VDDIO/VDDASEL | | 2-1 | | --- | | 2-3 | | | Connects 1V8 to V\_AUX, VDDIO EN (JP12), and VDDA EN (JP13) jumpers. | | --- | | Connects 3V3 to V\_AUX, VDDIO EN (JP12), and VDDA EN (JP13) jumpers. | |
| JP12 | VDDIO EN | | 1-2 | | --- | | Open | | | Connects the JP11 selected voltage to VDDIO. | | --- | | Disconnects the voltage from VDDIO. | |

## Programming and Debugging

The `max32662evkit` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **[openocd](../../../../develop/flash_debug/host-tools.md#runner-openocd)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

### Flashing

An Arm® debug access port (DAP) provides an external interface for debugging during application
development. The DAP is a standard Arm CoreSight® serial wire debug port, uses a two-pin serial
interface (SWDCLK and SWDIO), and is accessed through 10-pin header (J3). Logic levels are set
to V\_AUX (1V8 or 3V3), which is determined by the shunt placement on JP11. In addition,
the UART1A port can also be accessed through J3.

Once the debug probe is connected to your host computer, then you can simply run the
`west flash` command to write a firmware image into flash. To perform a full erase,
pass the `--erase` option when executing `west flash`.

Note

This board uses OpenOCD as the default debug interface. You can also use
a Segger J-Link with Segger’s native tooling by overriding the runner,
appending `--runner jlink` to your `west` command(s). The J-Link should
be connected to the standard 2\*5 pin debug connector (J3) using an
appropriate adapter board and cable.

### Debugging

Please refer to the [Flashing](#flashing) section and run the `west debug` command
instead of `west flash`.

## References

- [MAX32662EVKIT web page](https://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/max32662evkit.html)
