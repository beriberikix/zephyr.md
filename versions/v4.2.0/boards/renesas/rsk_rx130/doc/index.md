---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rsk_rx130/doc/index.html
original_path: boards/renesas/rsk_rx130/doc/index.html
---

# Renesas Starter Kit for RX130

Board Overview

[![../../../../_images/rsk_rx130.webp](../../../../_images/rsk_rx130.webp)
](../../../../_images/rsk_rx130.webp)

Renesas Starter Kit for RX130

Name:
:   `rsk_rx130`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   rx

SoC:
:   r5f51308axfp

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rsk_rx130/doc/index.rst/../..)

## Overview

The Renesas Starter Kit for RX130-512KB is the perfect starter kit for
developers who are new to the RX130 (Program Flash 512KB, Pin Count 100-pin),
which operates at up to 32 MHz and is based on the RXv1 core architecture,
making it suitable for various embedded applications

**MCU Native Pin Access**

The RSKRX130-512KB includes:

- 32-MHz, 32-bit RX MCUs in 100 pins LFQFP package, Micon Pin Headers
- Direct MCU pin access through standard headers for easy peripheral integration
- Internal high-speed oscillator and low-speed on-chip oscillators
- Three low power consumption modes

**System Control and Debugging**

- USB Full-Speed Device (mini-B connector) for communication and power
- Power source options:

  - USB-powered (debug port)
  - External power supply via standard input
- Debugging support:

  - Via Jlink debugger with RX adapter boards.
- User LEDs and buttons:

  - Four User LEDs (red x2, yellow, green)
  - Power LED (green) indicating availability of regulated power
  - One Reset button, three User buttons
- Ecosystems expansions:

  - Two Digilent Pmod (LCD and Spare) connectors
  - 2Kbit I2C EEPROM

**Special Feature Access**

- IEC60730 compliance
- Capacitive touch sensing unit
- LCD drive capability for displaying data or status in real-time applications

## Hardware

Detailed hardware features can be found at:

- RX130 MCU: [RX130 Group User’s Manual Hardware](https://www.renesas.com/en/document/mah/rx130-group-users-manual-hardware-rev300)
- RSK-RX130-512KB: [RSK\_RX130\_512KB - User’s Manual](https://www.renesas.com/en/document/mat/renesas-starter-kit-rx130-512kb-users-manual-rev100)

### Supported Features

The `rsk_rx130` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rsk_rx130@512kb/r5f51308axfp` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | Renesas RX CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L24) | [`renesas,rx`](../../../../build/dts/api/bindings/cpu/renesas%2Crx.md#std-dtcompatible-renesas-rx) |
| Clock control | on-chip | Renesas RX Root Clock Generation Circuit[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L15)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L46) | [`renesas,rx-cgc-root-clock`](../../../../build/dts/api/bindings/clock/renesas%2Crx-cgc-root-clock.md#std-dtcompatible-renesas-rx-cgc-root-clock) |
| on-chip | Renesas RX Clock Generation Circuit PLL Clock[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L53) | [`renesas,rx-cgc-pll`](../../../../build/dts/api/bindings/clock/renesas%2Crx-cgc-pll.md#std-dtcompatible-renesas-rx-cgc-pll) |
| on-chip | Renesas RX clock control node pclk block[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L62) | [`renesas,rx-cgc-pclk-block`](../../../../build/dts/api/bindings/clock/renesas%2Crx-cgc-pclk-block.md#std-dtcompatible-renesas-rx-cgc-pclk-block) |
| on-chip | Renesas RX Clock Control Peripheral Clock[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L71)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L100) | [`renesas,rx-cgc-pclk`](../../../../build/dts/api/bindings/clock/renesas%2Crx-cgc-pclk.md#std-dtcompatible-renesas-rx-cgc-pclk) |
| GPIO & Headers | on-chip | Renesas RX series GPIO[3 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L298)[10 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L230) | [`renesas,rx-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crx-gpio.md#std-dtcompatible-renesas-rx-gpio) |
| I2C | on-chip | Renesas RX I2C Master controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L757) | [`renesas,rx-i2c`](../../../../build/dts/api/bindings/i2c/renesas%2Crx-i2c.md#std-dtcompatible-renesas-rx-i2c) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rsk_rx130/rsk_rx130.dts?plain=1#L39) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | Renesas ICU Interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L32) | [`renesas,rx-icu`](../../../../build/dts/api/bindings/interrupt-controller/renesas%2Crx-icu.md#std-dtcompatible-renesas-rx-icu) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rsk_rx130/rsk_rx130.dts?plain=1#L25) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RX External Interrupt[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L160)[7 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L150) | [`renesas,rx-external-interrupt`](../../../../build/dts/api/bindings/misc/renesas%2Crx-external-interrupt.md#std-dtcompatible-renesas-rx-external-interrupt) |
| on-chip | Renesas RX SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L543)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L528) | [`renesas,rx-sci`](../../../../build/dts/api/bindings/misc/renesas%2Crx-sci.md#std-dtcompatible-renesas-rx-sci) |
| on-chip | Renesas RX MTU controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L611) | [`renesas,rx-mtu`](../../../../build/dts/api/bindings/misc/renesas%2Crx-mtu.md#std-dtcompatible-renesas-rx-mtu) |
| Pin control | on-chip | Renesas RX Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L53) | [`renesas,rx-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crx-pinctrl.md#std-dtcompatible-renesas-rx-pinctrl) |
| on-chip | Rensas RX Pinmux (Multi Function Pin Controller, MPC)[13 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L59) | [`renesas,rx-pinmux`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crx-pinmux.md#std-dtcompatible-renesas-rx-pinmux) |
| PWM | on-chip | Renesas PWM RX Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L655)[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L629) | [`renesas,rx-mtu-pwm`](../../../../build/dts/api/bindings/pwm/renesas%2Crx-mtu-pwm.md#std-dtcompatible-renesas-rx-mtu-pwm) |
| Serial controller | on-chip | Renesas RX SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L552)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L537) | [`renesas,rx-uart-sci`](../../../../build/dts/api/bindings/serial/renesas%2Crx-uart-sci.md#std-dtcompatible-renesas-rx-uart-sci) |
| SPI | on-chip | Renesas RX RSPI[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L802) | [`renesas,rx-rspi`](../../../../build/dts/api/bindings/spi/renesas%2Crx-rspi.md#std-dtcompatible-renesas-rx-rspi) |
| SRAM | on-chip | Generic on-chip SRAM[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/r5f51308axfp.dtsi?plain=1#L152) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | Renesas RX timer node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L768) | [`renesas,rx-timer-cmt-start-control`](../../../../build/dts/api/bindings/timer/renesas%2Crx-timer-cmt-start-control.md#std-dtcompatible-renesas-rx-timer-cmt-start-control) |
| on-chip | Renesas RX timer node[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L777)[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/rx/renesas/rx130-common.dtsi?plain=1#L790) | [`renesas,rx-timer-cmt`](../../../../build/dts/api/bindings/timer/renesas%2Crx-timer-cmt.md#std-dtcompatible-renesas-rx-timer-cmt) |

## Programming and Debugging

The `rsk_rx130` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rsk_rx130@512kb` board target can be built, flashed, and
debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

If you want to build Zephyr application for RSK-RX130 board using Renesas GCC RX toolchain follow
the steps below:

> - Download and install GCC for RX toolchain:
>
>   [https://llvm-gcc-renesas.com/rx-download-toolchains/](https://llvm-gcc-renesas.com/rx-download-toolchains/)
> - Set env variable:
>
> > ```shell
> > export ZEPHYR_TOOLCHAIN_VARIANT=cross-compile
> > export CROSS_COMPILE=<Path to your toolchain>/bin/rx-elf-
> > ```
>
> - Build the Blinky Sample for RSK-RX130-512KB:
>
> > ```shell
> > cd ~/zephyrproject/zephyr
> > west build -p always -b rsk_rx130@512kb samples/basic/blinky
> > ```

### Flashing

Program can be flashed to RSKRX130-512KB using Jlink with RX adapter boards, by
connecting the board’s debug connector port to the host PC. Here’s an example
for building and flashing the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rsk_rx130@512kb samples/hello_world
west flash
```

### Debugging

You can use [Renesas Debug extension](https://marketplace.visualstudio.com/items?itemName=RenesasElectronicsCorporation.renesas-debug) on Visual Studio code for a visual debug interface.
The configuration for launch.json is as below.

```json
{
  "version": "0.2.0",
  "configurations": [
      {
          "type": "renesas-hardware",
          "request": "launch",
          "name": "Renesas GDB Hardware Debugging",
          "target": {
              "deviceFamily": "RX",
              "device": "R5F51308",
              "debuggerType": "SEGGERJLINKRX",
          }
      }
  ]
}
```

## References

- [RSK\_RX130\_512KB Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx130-512kb-starter-kit-renesas-starter-kit-rx130-512kb)
- [RX130 MCU group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rx-32-bit-performance-efficiency-mcus/rx130-cost-optimized-high-performance-32-bit-microcontroller-enhanced-touch-key-function-and-5v-operation)
