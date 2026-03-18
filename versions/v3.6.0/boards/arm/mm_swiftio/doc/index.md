---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mm_swiftio/doc/index.html
original_path: boards/arm/mm_swiftio/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MadMachine SwiftIO

## Overview

The SwiftIO board, designed by MadMachine is the world’s first board
designed with support for the modern [Swift language](https://docs.swift.org/swift-book/). Zephyr provides basic
low-level capabilities for the SwiftIO board. Swift application would
run on top of Zephyr. More information about the board can be found
at:

- [MadMachine Homepage](https://madmachine.io)
- [SwiftIO API Reference](https://madmachineio.github.io/SwiftIO/documentation/swiftio/)

![SwiftIO Board](../../../../_images/mm_swiftio.jpg)

## Hardware

- i.MX RT1052 Cortex-M7 processor at 600MHz
- 8MB QSPI Flash, 32MB SDRAM
- On-board DAPLink debugger with serial port
- User RGB LED, USB 2.0 Connector, microSD slot

### Supported Features

The mm\_swiftio board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| DISPLAY | on-chip | display |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| UART | on-chip | serial port-polling; serial port-interrupt |
| USB | on-chip | USB device |

### Connections and IOs

Note:
The following SwiftIO pinout diagram is used for Swift programming.
The Swift ID is not the same as the Zephyr driver ID.

| Name | | GPIO | | Other peripherals | |
| --- | --- | --- | --- | --- | --- |
| Swift ID | Pin name | Swift ID | Zephyr driver | Swift ID | Zephyr driver |
| P0 | GPIO\_AD\_B1\_03 | D0 | GPIO1\_IO19 | UART0 | UART\_2 |
| P1 | GPIO\_AD\_B1\_02 | D1 | GPIO1\_IO18 |
| P2 | GPIO\_AD\_B0\_03 | D2 | GPIO1\_IO03 | UART1 | UART\_6 |
| P3 | GPIO\_AD\_B0\_02 | D3 | GPIO1\_IO02 |
| P4 | GPIO\_B1\_14 | D4 | GPIO2\_IO30 |  |  |
| P5 | GPIO\_B1\_15 | D5 | GPIO2\_IO31 |  |  |
| P6 | GPIO\_B0\_03 | D6 | GPIO2\_IO03 | SPI0 | SPI\_4 |
| P7 | GPIO\_B0\_02 | D7 | GPIO2\_IO02 |
| P8 | GPIO\_B0\_01 | D8 | GPIO2\_IO01 |
| P9 | GPIO\_B0\_00 | D9 | GPIO2\_IO00 |
| P10 | GPIO\_B1\_03 | D10 | GPIO2\_IO19 |  |  |
| P11 | GPIO\_B1\_02 | D11 | GPIO2\_IO18 |  |  |
| P12 | GPIO\_B1\_01 | D12 | GPIO2\_IO17 | UART2 | UART\_4 |
| P13 | GPIO\_B1\_00 | D13 | GPIO2\_IO16 |
| P14 | GPIO\_AD\_B1\_15 | D14 | GPIO1\_IO31 | SPI1 | SPI\_3 |
| P15 | GPIO\_AD\_B1\_14 | D15 | GPIO1\_IO30 |
| P16 | GPIO\_AD\_B1\_13 | D16 | GPIO1\_IO29 |
| P17 | GPIO\_AD\_B1\_12 | D17 | GPIO1\_IO28 |
| P18 | GPIO\_AD\_B1\_11 | D18 | GPIO1\_IO27 | UART3 | UART\_8 |
| P19 | GPIO\_AD\_B1\_10 | D19 | GPIO1\_IO26 |
| P20 | GPIO\_AD\_B1\_09 | D20 | GPIO1\_IO25 |  |  |
| P21 | GPIO\_AD\_B1\_08 | D21 | GPIO1\_IO24 |  |  |
| P22 | GPIO\_AD\_B1\_05 | D22 | GPIO1\_IO21 |  |  |
| P23 | GPIO\_AD\_B1\_04 | D23 | GPIO1\_IO20 |  |  |
| P24 | GPIO\_AD\_B0\_15 | D24 | GPIO1\_IO15 |  |  |
| P25 | GPIO\_AD\_B0\_14 | D25 | GPIO1\_IO14 |  |  |
| P26 | GPIO\_B0\_04 | D26 | GPIO2\_IO04 |  |  |
| P27 | GPIO\_B0\_05 | D27 | GPIO2\_IO05 |  |  |
| P28 | GPIO\_B0\_06 | D28 | GPIO2\_IO06 |  |  |
| P29 | GPIO\_B0\_07 | D29 | GPIO2\_IO07 |  |  |
| P30 | GPIO\_B0\_08 | D30 | GPIO2\_IO08 |  |  |
| P31 | GPIO\_B0\_09 | D31 | GPIO2\_IO09 |  |  |
| P32 | GPIO\_B0\_10 | D32 | GPIO2\_IO10 |  |  |
| P33 | GPIO\_B0\_11 | D33 | GPIO2\_IO11 |  |  |
| P34 | GPIO\_B0\_12 | D34 | GPIO2\_IO12 |  |  |
| P35 | GPIO\_B0\_13 | D35 | GPIO2\_IO13 |  |  |
| P36 | GPIO\_B0\_14 | D36 | GPIO2\_IO14 |  |  |
| P37 | GPIO\_B0\_15 | D37 | GPIO2\_IO15 |  |  |
| P38 | GPIO\_B1\_11 | D38 | GPIO2\_IO27 |  |  |
| P39 | GPIO\_B1\_10 | D39 | GPIO2\_IO26 |  |  |
| P40 | GPIO\_B1\_9 | D40 | GPIO2\_IO25 |  |  |
| P41 | GPIO\_B1\_8 | D41 | GPIO2\_IO24 |  |  |
| P42 | GPIO\_B1\_7 | D42 | GPIO2\_IO23 |  |  |
| P43 | GPIO\_B1\_6 | D43 | GPIO2\_IO22 |  |  |
| P44 | GPIO\_B1\_5 | D44 | GPIO2\_IO21 |  |  |
| P45 | GPIO\_B1\_4 | D45 | GPIO2\_IO20 |  |  |
|  | GPIO\_AD\_B1\_07 |  |  | I2C0 | I2C\_3 |
|  | GPIO\_AD\_B1\_06 |  |  |
|  | GPIO\_AD\_B1\_00 |  |  | I2C1 | I2C\_1 |
|  | GPIO\_AD\_B1\_01 |  |  |

## Programming and Flash

Build applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

### Configuring a Debug Probe

This board is configured by default to use the [OpenSDA DAPLink Onboard Debug Probe](../../../../develop/flash_debug/probes.md#opensda-daplink-onboard-debug-probe),
however the [pyOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#pyocd-debug-host-tools) do not yet support programming the
external flashes on this board so you must flash the device by copying files

### Configuring a Console

Regardless of your choice in debug probe, we will use the OpenSDA
microcontroller as a USB-to-serial adapter for the serial console.

Connect a USB cable from your PC to Serial of SwiftIO.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Connect a USB cable from your PC to “Serial” port of SwiftIO.
On Ubuntu, DAPLink debug probes appear on the host
computer as a USB disk mounted to `/media/<user>/SWIFTIODBGR/`,
where `<user>` is your login name.

```shell
west build -b mm_swiftio samples/hello_world
cp build/zephyr/zephyr.bin /media/<user>/SWIFTIODBGR/
```

Open a serial terminal, reset the board (press the “reset” button), and you should
see the following message in the terminal:

```shell
***** Booting Zephyr OS v2.1.0-rc1 *****
Hello World! mm_swiftio
```
