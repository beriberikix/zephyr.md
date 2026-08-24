---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/mikroe/clicker_ra4m1/doc/index.html
original_path: boards/mikroe/clicker_ra4m1/doc/index.html
---

# Clicker RA4M1

Board Overview

[![../../../../_images/mikroe_clicker_ra4m1.jpg](https://docs.zephyrproject.org/4.1.0/_images/mikroe_clicker_ra4m1.jpg)
](https://docs.zephyrproject.org/4.1.0/_images/mikroe_clicker_ra4m1.jpg)

Clicker RA4M1

Name:
:   `mikroe_clicker_ra4m1`

Vendor:
:   MikroElektronika d.o.o.

Architecture:
:   arm

SoC:
:   r7fa4m1ab3cfm

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/mikroe/clicker_ra4m1/doc/index.rst/../..)

## Overview

The Mikroe Clicker RA4M1 development board contains a Renesas Cortex-M4 based
R7FA4M1AB3CFM Microcontroller operating at up to 48 MHz with 256 KB of Flash
memory and 32 KB of SRAM.

## Hardware

The Clicker RA4M1 board contains a USB Type-C connector, two LEDs, two push
buttons, and a reset button. It has J-Link onboard and mikroBUS socket for
interfacing with external electronics. For more information about the
development board see the [Clicker RA4M1 website](https://www.mikroe.com/ra4m1-clicker) [[1]](#id2).

### Supported Features

The `mikroe_clicker_ra4m1` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `mikroe_clicker_ra4m1/r7fa4m1ab3cfm` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-M4 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L18) | [`arm,cortex-m4`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-m4.md#std-dtcompatible-arm-cortex-m4) |
| Clock control | on-chip | Renesas RA Clock Control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L88) | [`renesas,ra-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk-block.md#std-dtcompatible-renesas-ra-cgc-pclk-block) |
| on-chip | Renesas RA Clock Control Peripheral Clock[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L99)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L141) | [`renesas,ra-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pclk.md#std-dtcompatible-renesas-ra-cgc-pclk) |
| on-chip | Renesas RA Clock Generation Circuit external clock configuration[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L26) | [`renesas,ra-cgc-external-clock`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-external-clock.md#std-dtcompatible-renesas-ra-cgc-external-clock) |
| on-chip | Renesas RA Sub-Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L33) | [`renesas,ra-cgc-subclk`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-subclk.md#std-dtcompatible-renesas-ra-cgc-subclk) |
| on-chip | Generic fixed-rate clock provider[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L40) | [`fixed-clock`](../../../../build/dts/api/bindings/clock/fixed-clock.md#std-dtcompatible-fixed-clock) |
| on-chip | Renesas RA Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L61) | [`renesas,ra-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Cra-cgc-pll.md#std-dtcompatible-renesas-ra-cgc-pll) |
| GPIO & Headers | on-chip | Renesas RA series GPIO[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L167)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L273) | [`renesas,ra-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Cra-gpio.md#std-dtcompatible-renesas-ra-gpio) |
| on-board | GPIO pins exposed on Mikro BUS headers[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/clicker_ra4m1/mikroe_clicker_ra4m1.dts?plain=1#L45) | [`mikro-bus`](../../../../build/dts/api/bindings/gpio/mikro-bus.md#std-dtcompatible-mikro-bus) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/clicker_ra4m1/mikroe_clicker_ra4m1.dts?plain=1#L36) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARMv7-M NVIC (Nested Vectored Interrupt Controller)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L13) | [`arm,v7m-nvic`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cv7m-nvic.md#std-dtcompatible-arm-v7m-nvic) |
| on-chip | Renesas RA series interrupt controller unit[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L80) | [`renesas,ra-interrupt-controller-unit`](../../../../build/dts/api/bindings/interrupt-controller/renesas%2Cra-interrupt-controller-unit.md#std-dtcompatible-renesas-ra-interrupt-controller-unit) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/mikroe/clicker_ra4m1/mikroe_clicker_ra4m1.dts?plain=1#L24) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RA SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L296)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L315) | [`renesas,ra-sci`](../../../../build/dts/api/bindings/misc/renesas%2Cra-sci.md#std-dtcompatible-renesas-ra-sci) |
| MTD | on-chip | Flash node[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L156) | [`soc-nv-flash`](../../../../build/dts/api/bindings/mtd/soc-nv-flash.md#std-dtcompatible-soc-nv-flash) |
| Pin control | on-chip | The Renesas RA pin controller is a node responsible for controlling pin function selection and pin properties, such as routing a SCI0 RXD to P610[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L289) | [`renesas,ra-pinctrl-pfs`](../../../../build/dts/api/bindings/pinctrl/renesas%2Cra-pincrl-pfs.md#std-dtcompatible-renesas-ra-pinctrl-pfs) |
| Serial controller | on-chip | Renesas RA Series SCI based UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L309)[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L327) | [`renesas,ra-uart-sci`](../../../../build/dts/api/bindings/serial/renesas%2Cra-uart-sci.md#std-dtcompatible-renesas-ra-uart-sci) |
| SRAM | on-chip | Generic on-chip SRAM description[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/ra/ra-cm4-common.dtsi?plain=1#L73) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | ARMv7-M System Tick[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/armv7-m.dtsi?plain=1#L21) | [`arm,armv7m-systick`](../../../../build/dts/api/bindings/timer/arm%2Carmv7m-systick.md#std-dtcompatible-arm-armv7m-systick) |

## Programming and debugging

### Building & Flashing

You can build and flash an application in the usual way (See
[Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

Here is an example for building and flashing the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west flash
```

### Debugging

Debugging also can be done in the usual way.
The following command is debugging the [Blinky](../../../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.") application.
Also, see the instructions specific to the debug server that you use.

```shell
# From the root of the zephyr repository
west build -b mikroe_clicker_ra4m1 samples/basic/blinky
west debug
```

## References

[[1](#id3)]

[https://www.mikroe.com/ra4m1-clicker](https://www.mikroe.com/ra4m1-clicker)
