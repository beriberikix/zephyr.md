---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/renesas/rzn2l_rsk/doc/index.html
original_path: boards/renesas/rzn2l_rsk/doc/index.html
---

# Renesas Starter Kit+ for RZ/N2L

Board Overview

[![../../../../_images/rzn2l_rsk.webp](../../../../_images/rzn2l_rsk.webp)
](../../../../_images/rzn2l_rsk.webp)

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

[![RZ/N2L group feature](../../../../_images/rzn2l_block_diagram.webp)
](../../../../_images/rzn2l_block_diagram.webp)

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

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins H15, G11),
- UART3 connected to the PMOD Header (J25, pins E14, E15),
- LEDs defined as `led0`, `led1`, `led2` and `led3`,

The Zephyr console uses UART0.

## Programming and Debugging

The `rzn2l_rsk` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

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
