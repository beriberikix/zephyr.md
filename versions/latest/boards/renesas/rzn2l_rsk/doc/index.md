---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzn2l_rsk/doc/index.html
original_path: boards/renesas/rzn2l_rsk/doc/index.html
---

# Renesas Starter Kit+ for RZ/N2L

Board Overview

[![../../../../_images/rzn2l_rsk.webp](https://docs.zephyrproject.org/4.2.0/_images/rzn2l_rsk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzn2l_rsk.webp)

Renesas Starter Kit+ for RZ/N2L

Name:
:   `rzn2l_rsk`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a07g084m04gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzn2l_rsk/doc/index.rst/../..)

## Overview

Renesas Starter Kit+ for RZ/N2L is for evaluation or development using the RZ/N2L MPU.
With the on-board emulator, you can start evaluation by simply connecting the bundled cable with
your PC. This product has rich functional ICs such as Gigabit Ethernet PHY and Octal Flash,
you can fully evaluate functions without an extension board.

- On-board RZ/N2L MPU 225-pin (R9A07G084M04GBG)
- Rich functional ICs such as Gigabit Ethernet PHY and Octal Flash are mounted,
  so functions of target MPU can be fully evaluated
- Generic interfaces such as Pmod/Grove/Qwiic/mikroBUS
- Pin headers for external extension enable you to evaluate many use cases
- Emulator circuit is mounted, and program debugging can be started by simply connecting USB cable
  to PC (two USB cables are included, one for emulator and the other for power supply)
- On-board memory components:

  - SDRAM (256MBit)
  - NOR Flash (256MBit)
  - Octa Flash (512MBit)
  - HyperRAM (64Mbit)
  - QSPI Serial Flash (512Mbit)
  - I2C EEPROM (32Kbit)
- Communication interfaces include:

  - Debug interfaces (J-Link OB, MIPI-10, MIPI-20)
  - Ethernet
  - CAN
  - USB
  - RS485
  - UART
  - I2C
  - SPI

## Hardware

The Renesas RZ/N2L MPU documentation can be found at [RZ/N2L Group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-integrated-tsn-compliant-3-port-gigabit-ethernet-switch-enables-various-industrial-applications) [[1]](#id3)

[![RZ/N2L group feature](https://docs.zephyrproject.org/4.2.0/_images/rzn2l_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzn2l_block_diagram.webp)

RZ/N2L block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZ/N2L-RSK Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-rsk-renesas-starter-kit-rzn2l) [[2]](#id5)

### Supported Features

The `rzn2l_rsk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzn2l_rsk/r9a07g084m04gbg` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L19) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm,cortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| GPIO & Headers | on-chip | Renesas RZ GPIO controller[6 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L285)[19 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L248) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzn2l_rsk/rzn2l_rsk.dts?plain=1#L53) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L38) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | Renesas RZ external interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L160)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L97) | [`renesas,rz-ext-irq`](../../../../build/dts/api/bindings/interrupt-controller/renesas,rz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzn2l_rsk/rzn2l_rsk.dts?plain=1#L29) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RZ SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L484)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L502) | [`renesas,rz-sci`](../../../../build/dts/api/bindings/misc/renesas,rz-sci.md#std-dtcompatible-renesas-rz-sci) |
| MTD | on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L66) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas RZ/N2L Pin Controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L242) | [`renesas,rzn-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas,rzn-pinctrl.md#std-dtcompatible-renesas-rzn-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L495)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L513) | [`renesas,rz-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,rz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L47) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzn/r9a07g084.dtsi?plain=1#L26) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins H15, G11),
- UART3 connected to the PMOD Header (J25, pins E14, E15),
- LEDs defined as `led0`, `led1`, `led2` and `led3`,

The Zephyr console uses UART0.

## Programming and Debugging

The `rzn2l_rsk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rzn2l_rsk` board can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

To use J-Link OB on RSK+RZN2L,

1. Open the jumper pin (J9) for switching the debug connection.
2. Connect the micro-USB type-B to J-Link OB USB connector (J10), and then the LED4 is lighted.

### Console

The UART port is accessed by USB-Serial port (CN16).

### Debugging

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rzn2l_rsk samples/hello_world
west debug
```

### Flashing

Before using `flash` command, the board must be set to xSPI boot mode.

```shell
# From the root of the zephyr repository
west build -b rzn2l_rsk samples/hello_world
west flash
```

## References

[[1](#id4)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-integrated-tsn-compliant-3-port-gigabit-ethernet-switch-enables-various-industrial-applications](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-integrated-tsn-compliant-3-port-gigabit-ethernet-switch-enables-various-industrial-applications)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-rsk-renesas-starter-kit-rzn2l](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzn2l-rsk-renesas-starter-kit-rzn2l)
