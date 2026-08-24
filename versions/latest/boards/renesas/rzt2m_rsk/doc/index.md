---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzt2m_rsk/doc/index.html
original_path: boards/renesas/rzt2m_rsk/doc/index.html
---

# Renesas Starter Kit+ for RZ/T2M

Board Overview

[![../../../../_images/rzt2m_rsk.webp](https://docs.zephyrproject.org/4.2.0/_images/rzt2m_rsk.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzt2m_rsk.webp)

Renesas Starter Kit+ for RZ/T2M

Name:
:   `rzt2m_rsk`

Vendor:
:   Renesas Electronics Corporation

Architecture:
:   arm

SoC:
:   r9a07g075m24gbg

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/renesas/rzt2m_rsk/doc/index.rst/../..)

## Overview

The Renesas Starter Kit+ for RZ/T2M is an evaluation and development kit for the RZ/T2M MPU.
The board is powered through a 5V input via a DC Power Jack or USB Type-C Connector.

- On-board RZ/T2M MPU 320-pin (R9A07G075M24GBG)
- Rich functional ICs such as Gigabit Ethernet PHY and Octal Flash are mounted,
  functions of target MPU can be fully evaluated
- Generic interface such as Pmod/Grove/QWIIC/mikroBUS
- The pin header enables users to freely combine with the user’s hardware system and evaluate RZ/T2M
- Emulator circuit is mounted, can start program debugging by simply connecting USB cable
  to PC (two USB cables are bundled: one for emulator, and the other for power supply)
- On-board memory components:

  - SDRAM (256MBit)
  - NOR Flash (256MBit)
  - Octa Flash (512MBit)
  - HyperRAM (512Mbit)
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

The Renesas RZ/T2M MPU documentation can be found at [RZT2M Product page](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzt2m-high-performance-multi-function-mpu-realizing-high-speed-processing-and-high-precision-control) [[1]](#id2)

[![RZ/T2M group feature](https://docs.zephyrproject.org/4.2.0/_images/rzt2m_block_diagram.webp)
](https://docs.zephyrproject.org/4.2.0/_images/rzt2m_block_diagram.webp)

### Supported Features

The `rzt2m_rsk` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

#### `rzt2m_rsk/r9a07g075m24gbg/cr520` target

| Type | Location | Description | Compatible |
| --- | --- | --- | --- |
| CPU | on-chip | ARM Cortex-R52 CPU[2 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L21) | [`arm,cortex-r52`](../../../../build/dts/api/bindings/cpu/arm,cortex-r52.md#std-dtcompatible-arm-cortex-r52) |
| GPIO & Headers | on-chip | Renesas RZ GPIO controller[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L346)[20 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L255) | [`renesas,rz-gpio`](../../../../build/dts/api/bindings/gpio/renesas,rz-gpio.md#std-dtcompatible-renesas-rz-gpio) |
| Input | on-board | Group of GPIO-bound input keys[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2m_rsk/rzt2m_rsk_r9a07g075m24gbg_cr520.dts?plain=1#L54) | [`gpio-keys`](../../../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys) |
| Interrupt controller | on-chip | ARM Generic Interrupt Controller v3[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L46) | [`arm,gic-v3`](../../../../build/dts/api/bindings/interrupt-controller/arm,gic-v3.md#std-dtcompatible-arm-gic-v3) |
| on-chip | Renesas RZ external interrupt controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L122)[15 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L104) | [`renesas,rz-ext-irq`](../../../../build/dts/api/bindings/interrupt-controller/renesas,rz-ext-irq.md#std-dtcompatible-renesas-rz-ext-irq) |
| LED | on-board | Group of GPIO-controlled LEDs[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/renesas/rzt2m_rsk/rzt2m_rsk_r9a07g075m24gbg_cr520.dts?plain=1#L30) | [`gpio-leds`](../../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) |
| Miscellaneous | on-chip | Renesas RZ SCI controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L482)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L500) | [`renesas,rz-sci`](../../../../build/dts/api/bindings/misc/renesas,rz-sci.md#std-dtcompatible-renesas-rz-sci) |
| MTD | on-chip | Fixed partitions of a flash (or other non-volatile storage) memory[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L74) | [`fixed-partitions`](../../../../build/dts/api/bindings/mtd/fixed-partitions.md#std-dtcompatible-fixed-partitions) |
| Pin control | on-chip | Renesas RZ/T pin controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L249) | [`renesas,rzt-pinctrl`](../../../../build/dts/api/bindings/pinctrl/renesas,rzt-pinctrl.md#std-dtcompatible-renesas-rzt-pinctrl) |
| Serial controller | on-chip | Renesas RZ SCI UART controller[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L493)[5 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L511) | [`renesas,rz-sci-uart`](../../../../build/dts/api/bindings/serial/renesas,rz-sci-uart.md#std-dtcompatible-renesas-rz-sci-uart) |
| SRAM | on-chip | Generic on-chip SRAM[4 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L55) | [`mmio-sram`](../../../../build/dts/api/bindings/sram/mmio-sram.md#std-dtcompatible-mmio-sram) |
| Timer | on-chip | per-core ARM architected timer[1 ](https://github.com/zephyrproject-rtos/zephyr/blob/main/dts/arm/renesas/rz/rzt/r9a07g075.dtsi?plain=1#L34) | [`arm,armv8-timer`](../../../../build/dts/api/bindings/timer/arm,armv8-timer.md#std-dtcompatible-arm-armv8-timer) |

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins K18, K19),
- UART3 connected to the PMOD Header (J25, pins H16, G20),
- LEDs defined as `led0`, `led1`, `led2` and `led3`,

The Zephyr console uses UART0.

## Programming and Debugging

The `rzt2m_rsk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** | **attach** | **rtt** | **debugserver** |
| --- | --- | --- | --- | --- | --- |
| **[jlink](../../../../develop/flash_debug/host-tools.md#runner-jlink)** | ✅ (default) | ✅ (default) | ✅ | ✅ | ✅ |

Applications for the `rzt2m_rsk` board can be built in the usual way as
documented in [Building an Application](../../../../develop/application/index.md#build-an-application).

To use J-Link OB on RSK+RZT2M,

1. Open the jumper pin (J9) for switching the debug connection.
2. Connect the micro-USB type-B to J-Link OB USB connector (J10), and then the LED4 is lighted.

### Console

The UART port is accessed by USB-Serial port (CN16).

### Debugging

Here is an example for building and debugging with the [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b rzt2m_rsk/r9a07g075m24gbg/cr520 samples/hello_world
west debug
```

### Flashing

Before using `flash` command, the board must be set to xSPI boot mode.

```shell
# From the root of the zephyr repository
west build -b rzt2m_rsk/r9a07g075m24gbg/cr520 samples/hello_world
west flash
```

## References

[[1](#id3)]

[https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzt2m-high-performance-multi-function-mpu-realizing-high-speed-processing-and-high-precision-control](https://www.renesas.com/us/en/products/microcontrollers-microprocessors/rz-mpus/rzt2m-high-performance-multi-function-mpu-realizing-high-speed-processing-and-high-precision-control)
