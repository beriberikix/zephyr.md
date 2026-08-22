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

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins G12, G11),
- UART2 connected to the PMOD Header (J25, pins M1, L2),
- LEDs defined as `led1` and `led3`,

The Zephyr console uses UART0.

## Programming and Debugging

The `rzt2l_rsk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

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
