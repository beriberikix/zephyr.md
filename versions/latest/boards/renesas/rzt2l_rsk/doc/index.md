---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzt2l_rsk/doc/index.html
original_path: boards/renesas/rzt2l_rsk/doc/index.html
---

# Renesas Starter Kit+ for RZ/T2L

Board Overview

[![../../../../_images/rzt2l_rsk.webp](../../../../_images/rzt2l_rsk.webp)
](../../../../_images/rzt2l_rsk.webp)

Renesas Starter Kit+ for RZ/T2L

Name:
:   `rzt2l_rsk`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a07g074m04gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzt2l_rsk/doc/index.rst/../..)

## Overview

Renesas Starter Kit+ for RZ/T2L is an evaluation and development kit for the RZ/T2L MPU.
By simply connecting the bundled cable to your PC, you can immediately start evaluation through an
on-board emulator. This product contains rich functional ICs such as Gigabit Ethernet PHY and
Octal Flash so you can evaluate various functions of the RZ/T2L without an extension board.

- On-board RZ/T2L MPU 196-pin (R9A07G074M04GBG)
- Rich functional ICs such as Gigabit Ethernet PHY and Octal Flash
  so you can evaluate various functions of the RZ/T2L without an extension board
- Generic interfaces such as Pmod/Grove/QWIIC/mikroBUS
- Pin headers for external extension enable you to evaluate many use cases
- Emulator circuit is mounted, and program debugging can be started by simply connecting USB cable
  to PC (two USB cables are included, one for emulator and the other for power supply)
- On-board memory components:

  - Octa Flash (512MBit)
  - HyperRAM (64Mbit)
  - QSPI Serial Flash (128Mbit)
  - I2C EEPROM (16Kbit)
- Communication interfaces include:

  - Debug interfaces (J-Link OB, MIPI-10, MIPI-20, Mictor-38)
  - Ethernet
  - CAN
  - USB
  - RS485
  - UART
  - I2C
  - SPI

## Hardware

The Renesas RZ/T2L MPU documentation can be found at [RZ/T2L Group Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-high-performance-mpu-realizing-high-speed-and-high-precision-real-time-control-ethercat) [[1]](#id3)

[![RZ/T2L group feature](../../../../_images/rzt2l_block_diagram.webp)
](../../../../_images/rzt2l_block_diagram.webp)

RZ/T2L block diagram (Credit: Renesas Electronics Corporation)

Detailed hardware features for the board can be found at [RZ/T2L-RSK Website](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-rsk-renesas-starter-kit-rzt2l) [[2]](#id5)

### Supported Features

The `rzt2l_rsk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzt2l_rsk/r9a07g074m04gbg` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L20) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm%2Ccortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| GPIO & Headers | on-chip | Renesas RZ GPIO controller[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L380)[21 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L249) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas%2Crz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2l_rsk/rzt2l_rsk.dts?plain=1#L44) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L39) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm%2Cgic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | Renesas RZ external interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L161)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L98) | [`renesas,rz-ext-irq`](../../../../build/dts/api/bindings/interrupt-controller/renesas%2Crz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2l_rsk/rzt2l_rsk.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RZ SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L484)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L502) | [`renesas,rz-sci`](../../../../build/dts/api/bindings/misc/renesas%2Crz-sci.md#std-dtcompatible-renesas-rz-sci) |
| MTD | on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L67) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas RZ/T pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L243) | [`renesas,rzt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas%2Crzt-pinctrl.md#std-dtcompatible-renesas-rzt-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L495)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L513) | [`renesas,rz-sci-uart`](../../../../build/dts/api/bindings/serial/renesas%2Crz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L48) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g074.dtsi?plain=1#L27) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm%2Carmv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins G12, G11),
- UART2 connected to the PMOD Header (J25, pins M1, L2),
- LEDs defined as `led1` and `led3`,

The Zephyr console uses UART0.

## Programming and Debugging

The `rzt2l_rsk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rzt2l_rsk` board can be
built, flashed, and debugged in the usual way. See [Building an Application](../../../../develop/application/index.md#build-an-application)
and [Run an Application](../../../../develop/application/index.md#application-run) for more details on building and running.

To use J-Link OB on RSK+RZT2L,

1. Open the jumper pin (J9) for switching the debug connection.
2. Connect the micro-USB type-B to J-Link OB USB connector (J10), and then the LED6 is lighted.

### Console

The UART port is accessed by USB-Serial port (CN16).

### Debugging

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rzt2l_rsk samples/hello_world
west debug
```

### Flashing

Before using `flash` command, the board must be set to xSPI1 boot mode.

```shell
# From the root of the zephyr repository
west build -b rzt2l_rsk samples/hello_world
west flash
```

## References

[[1](#id4)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-high-performance-mpu-realizing-high-speed-and-high-precision-real-time-control-ethercat](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-high-performance-mpu-realizing-high-speed-and-high-precision-real-time-control-ethercat)

[[2](#id6)]

[https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-rsk-renesas-starter-kit-rzt2l](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rzt2l-rsk-renesas-starter-kit-rzt2l)
