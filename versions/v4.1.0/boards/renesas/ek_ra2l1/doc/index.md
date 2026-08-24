---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/renesas/ek_ra2l1/doc/index.html
original_path: boards/renesas/ek_ra2l1/doc/index.html
---

# ek\_ra2l1

Board Overview

[![../../../../_images/ek_ra2l1.webp](https://docs.zephyrproject.org/4.1.0/_images/ek_ra2l1.webp)
](https://docs.zephyrproject.org/4.1.0/_images/ek_ra2l1.webp)

ek\_ra2l1

Name:
:   `ek_ra2l1`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r7fa2l1abxxfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/ek_ra2l1/doc/index.rst/../..)

## Overview

The EK-RA2L1 is an evaluation kit for Renesas RA2L1 Microcontroller Group.

Renesas RA2L1 Microcontroller Group has following features

- 48MHz, Arm Cortex-M23 core
- 256kB or 128kB Code Flash, 8kB Data Flash, 32kB SRAM (divided on 2 equal areas
  with- and without- ECC support)
- SCI x 5
- SPI x 2
- I2C x 2
- CAN x 1
- 12-bit A/D Converter
- 12-bit D/A Converter
- Low-Power Analog Comparator x 2
- Temperature Sensor
- General PWM Timer 32-bit x 4
- General PWM Timer 16-bit x 6
- Low Power Asynchronous General-Purpose Timer x 2
- Watchdog Timer (WDT)
- Independent Watchdog Timer (IWDT)
- up to 85 Input/Output pins (depends on the package type)

## Hardware

EK-RA2L1 has following features.

- Native pin access through 1 x 40-pin and 3 x 20-pin male headers
- MCU current measurement points for precision current consumption measurement
- Multiple clock sources – Low-precision clocks are available internal to the MCU.
  Additionally, MCU oscillator and sub-clock oscillator crystals,
  20.000 MHz and 32,768 Hz, are provided for precision
- SEGGER J-Link on-board programmer and debugger
- Two Digilent Pmod (SPI and UART)
- Three user LEDs (red, blue, green)
- Power LED (white) indicating availability of regulated power
- Debug LED (yellow) indicating the debug connection
- Two user buttons
- One reset button

### Supported Features

The `ek_ra2l1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `ek_ra2l1/r7fa2l1abxxfp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M23 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L21) | [`arm,cortex-m23`](../../../../build/dts/api/bindings/cpu/arm,cortex-m23.md#std-dtcompatible-arm-cortex-m23) |
| Clock control | on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L16) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L23) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L41) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L48) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L58)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/r7fa2l1xxxxfp.dtsi?plain=1#L80) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas,ra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| GPIO & Headers | on-chip | Renesas RA GPIO IO port[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L118)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L68) | [`renesas,ra-gpio-ioport`](../../../../build/dts/api/bindings/gpio/renesas,ra-gpio-ioport.md#std-dtcompatible-renesas-ra-gpio-ioport) |
| Interrupt controller | on-chip | ARMv8-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L13) | [`arm,v8m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm,v8m-nvic.md#std-dtcompatible-arm-v8m-nvic) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/ek_ra2l1/ek_ra2l1.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L154)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L169) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas,ra-sci.md#std-dtcompatible-renesas-ra-sci) |
| MMU / MPU | on-chip | ARMv8-M MPU (Memory Protection Unit)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L28) | [`arm,armv8m-mpu`](../../../../build/dts/api/bindings/mmu_mpu/arm,armv8m-mpu.md#std-dtcompatible-arm-armv8m-mpu) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L55) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | The Renesas RA pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a SCI0 RXD to P610[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L148) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas,ra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| Serial controller | on-chip | Renesas RA SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L162)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L175) | [`renesas,ra-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,ra-sci-uart.md#std-dtcompatible-renesas-ra-sci-uart) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra2/ra2l1.dtsi?plain=1#L38) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv8-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv8-m.dtsi?plain=1#L21) | [`arm,armv8m-systick`](../../../../build/dts/api/bindings/timer/arm,armv8m-systick.md#std-dtcompatible-arm-armv8m-systick) |

## Programming and debugging

### Building & Flashing

You can build and flash an application with onboard J-Link debug adapter.
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b ek_ra2l1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done with onboard J-Link debug adapter.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b ek_ra2l1 samples/basic/blinky
west debug
```

Or you can use Segger Ozone ([Segger Ozone Download](https://www.segger.com/downloads/jlink#Ozone)) for a visual debug interface

Once downloaded and installed, open Segger Ozone and configure the debug project
like so:

- Target Device: R7FA2L1AB
- Target Interface: SWD
- Target Interface Speed: 4 MHz
- Host Interface: USB
- Program File: <path/to/your/build/zephyr.elf>

## References
