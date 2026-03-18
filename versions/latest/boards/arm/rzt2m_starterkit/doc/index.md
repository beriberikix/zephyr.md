---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/rzt2m_starterkit/doc/index.html
original_path: boards/arm/rzt2m_starterkit/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Renesas Starter Kit+ for RZ/T2M

## Overview

The Renesas Starter Kit+ for RZ/T2M is an evaluation and development kit for the RZ/T2M MPU.
The board is powered through a 5V input via a DC Power Jack or USB Type-C Connector.

[![Starter Kit+ for RZ/T2M](../../../../_images/rzt2m_starterkit.png)](../../../../_images/rzt2m_starterkit.png)

Starter Kit+ for RZ/T2M (Credit: Renesas)

## Hardware

The board utilizes the SoC of part no. R9A07G075M24GBG, with 2MB of RAM.

It has several on-board memory components:

- SDRAM (256MBit),
- NOR Flash (256MBit),
- Octa Flash (512MBit),
- HyperRAM (512Mbit),
- QSPI Serial Flash (512Mbit),
- I2C EEPROM (32Kbit).

The communication interfaces include:

- Debug interfaces (J-Link, MIPI-10, MIPI-20),
- Ethernet,
- CAN,
- USB,
- RS485,
- UART,
- I2C,
- SPI.

### Supported Features

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| PINCTRL | on-chip | pinctrl |
| UART | on-chip | serial |
| GPIO | on-chip | gpio |

Other hardware features are not currently supported by the port.

### Connections and IOs

By default, the board is configured for use with:

- UART0 connected to the USB serial port (pins K18, K19),
- UART3 connected to the PMOD Header (J25, pins H16, G20),
- LEDs defined as led0, led1, led2 and led3,

The Zephyr console uses UART0.

## Programming and Debugging

### Debugging

Connect to the board using the J-Link On-board USB connector.
Use west to start the debug server:

```shell
west debugserver
```

Connect GDB to the server and load an application:

```text
target remote :2331
file build/zephyr/zephyr.elf
load
```

## References
