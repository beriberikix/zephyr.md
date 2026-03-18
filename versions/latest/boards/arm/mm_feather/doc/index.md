---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/mm_feather/doc/index.html
original_path: boards/arm/mm_feather/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MadMachine SwiftIO Feather

## Overview

The SwiftIO Feather board, designed by MadMachine is
designed with support for the modern [Swift language](https://docs.swift.org/swift-book/). Zephyr provides basic
low-level capabilities for the SwiftIO Feather board. Swift application would
run on top of Zephyr. More information about the board can be found
at:

- [MadMachine Homepage](https://madmachine.io)
- [SwiftIO API Reference](https://madmachineio.github.io/SwiftIO/documentation/swiftio/)

![SwiftIO Feather Board](../../../../_images/mm_feather.jpg)

## Hardware

- MIMXRT1062DVL6B MCU (Cortex-M7 at 600MHz, 2048KB on-chip memory)
- Memory

  > - 8MB QSPI Flash
  > - 32MB SDRAM
  > - TF socket for SD card
- USB

  > - USB-C 2.0 OTG connector
- Power

  > - 5V USB power
  > - 4.2V DC jack
- Debug

  > - SWD connector
- RGB LED

### Supported Features

The mm\_feather board configuration supports the following hardware
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
| I2S | on-chip | I2S |
| USB | on-chip | USB device |

### Connections and IOs

Note:
The following SwiftIO Feather pinout diagram is used for Swift programming.
The Swift ID is not the same as the Zephyr driver ID.

| Name | | GPIO | | Other peripherals | |
| --- | --- | --- | --- | --- | --- |
| Swift ID | Pin name | Swift ID | Zephyr driver | Swift ID | Zephyr driver |
| P0 | GPIO\_AD\_B1\_04 | D0 | GPIO1\_IO20 |  |  |
| P1 | GPIO\_AD\_B1\_08 | D1 | GPIO1\_IO24 |  |  |
| P2 | GPIO\_AD\_B1\_09 | D2 | GPIO1\_IO25 |  |  |
| P3 | GPIO\_AD\_B1\_10 | D3 | GPIO1\_IO26 | UART1 | UART\_8 |
| P4 | GPIO\_AD\_B1\_11 | D4 | GPIO1\_IO27 |
| P5 | GPIO\_AD\_B1\_12 | D5 | GPIO1\_IO28 |  |  |
| P6 | GPIO\_AD\_B1\_15 | D6 | GPIO1\_IO31 | SPI0 | SPI\_3 |
| P7 | GPIO\_AD\_B1\_14 | D7 | GPIO1\_IO30 |
| P8 | GPIO\_AD\_B1\_13 | D8 | GPIO1\_IO29 |
| P9 | GPIO\_AD\_B1\_03 | D9 | GPIO1\_IO19 | UART0 | UART\_2 |
| P10 | GPIO\_AD\_B1\_02 | D10 | GPIO1\_IO18 |
| P11 | GPIO\_AD\_B1\_05 | D11 | GPIO1\_IO21 |  |  |
| P12 | GPIO\_AD\_B0\_14 | D12 | GPIO1\_IO14 | CAN0 | CAN\_3 |
| P13 | GPIO\_AD\_B0\_15 | D13 | GPIO1\_IO15 |
| P14 | GPIO\_B0\_00 | D14 | GPIO2\_IO00 |  |  |
| P15 | GPIO\_B1\_03 | D15 | GPIO2\_IO19 |  |  |
| P16 | GPIO\_B1\_02 | D16 | GPIO2\_IO18 |  |  |
| P17 | GPIO\_B1\_01 | D17 | GPIO2\_IO17 | UART2 | UART\_4 |
| P18 | GPIO\_B1\_00 | D18 | GPIO2\_IO16 |
| P19 | GPIO\_B1\_15 | D19 | GPIO2\_IO31 |  |  |
| P20 | GPIO\_B1\_14 | D20 | GPIO2\_IO30 |  |  |
| P21 | GPIO\_B0\_03 | D21 | GPIO2\_IO03 | SPI1 | SPI\_4 |
| P22 | GPIO\_B0\_02 | D22 | GPIO2\_IO02 |
| P23 | GPIO\_B0\_01 | D23 | GPIO2\_IO01 |
| P24 | GPIO\_B0\_04 | D24 | GPIO2\_IO04 |  |  |
| P25 | GPIO\_B0\_05 | D25 | GPIO2\_IO05 |  |  |
| P26 | GPIO\_B0\_06 | D26 | GPIO2\_IO06 |  |  |
| P27 | GPIO\_B0\_07 | D27 | GPIO2\_IO07 |  |  |
| P28 | GPIO\_B0\_08 | D28 | GPIO2\_IO08 |  |  |
| P29 | GPIO\_B0\_09 | D29 | GPIO2\_IO09 |  |  |
| P30 | GPIO\_B0\_10 | D30 | GPIO2\_IO10 |  |  |
| P31 | GPIO\_B0\_11 | D31 | GPIO2\_IO11 |  |  |
| P32 | GPIO\_B0\_12 | D32 | GPIO2\_IO12 |  |  |
| P33 | GPIO\_B0\_13 | D33 | GPIO2\_IO13 |  |  |
| P34 | GPIO\_B0\_14 | D34 | GPIO2\_IO14 |  |  |
| P35 | GPIO\_B0\_15 | D35 | GPIO2\_IO15 |  |  |
|  | GPIO\_AD\_B1\_07 |  | GPIO1\_IO23 | I2C0 | I2C\_3 |
|  | GPIO\_AD\_B1\_06 |  | GPIO1\_IO22 |
|  | GPIO\_AD\_B1\_00 |  | GPIO1\_IO16 | I2C1 | I2C\_1 |
|  | GPIO\_AD\_B1\_00 |  | GPIO1\_IO17 |

## Programming and Flash

Build and flash applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) and
[Run an Application](../../../../develop/application/index.md#application-run) for more details).

### Configuring a Console

Connect a USB-to-serial adapter from your PC to corresponding UART pins of SwiftIO Feather.

Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

### Flashing

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

Connect a DAPLink debugger from your PC to corresponding SWD pins of SwiftIO Feather.

```shell
# From the root of the zephyr repository
west build -b mm_feather samples/hello_world
west flash
```

Open a serial terminal, reset the board (press the “reset” button), and you should
see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1-301-gd9c666a5abf8  ***
Hello World! mm_feather
```

### Debugging

Here is an example for the [Hello World](../../../../samples/hello_world/README.md#hello-world) application.

```shell
# From the root of the zephyr repository
west build -b mm_feather samples/hello_world
west debug
```

Open a serial terminal, step through the application in your debugger, and you
should see the following message in the terminal:

```shell
*** Booting Zephyr OS build v2.6.0-rc1-301-gd9c666a5abf8  ***
Hello World! mm_feather
```
