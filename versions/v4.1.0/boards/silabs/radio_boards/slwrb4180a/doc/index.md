---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/radio_boards/slwrb4180a/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4180a/doc/index.html
---

# EFR32xG21 2.4 GHz 20 dBm (SLWRB4180A)

Board Overview

[![../../../../../_images/efr32mg21-slwrb4180a.jpg](../../../../../_images/efr32mg21-slwrb4180a.jpg)
](../../../../../_images/efr32mg21-slwrb4180a.jpg)

EFR32xG21 2.4 GHz 20 dBm (SLWRB4180A)

Name:
:   `slwrb4180a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg21a020f1024im32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4180a/doc/index.rst/../..)

## Overview

The EFR32MG21 Mighty Gecko Radio Board is one of the two
radio boards delivered with [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit). It contains
a Wireless System-On-Chip from the EFR32MG21 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

The BRD4180A a.k.a. SLWRB4180A radio board plugs into the Wireless Starter Kit
Mainboard BRD4001A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32MG21A020F1024IM32 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1024 kB
- RAM: 96 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).

For more information about the EFR32MG21 SoC and BRD4180A board, refer to these
documents:

- [EFR32MG21 Website](https://www.silabs.com/products/wireless/mesh-networking/efr32mg21-series-2-socs)
- [EFR32MG21 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg21-datasheet.pdf)
- [EFR32xG21 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg21-rm.pdf)
- [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit)
- [BRD4180A User Guide](https://www.silabs.com/documents/public/user-guides/ug385-brd4180a-user-guide.pdf)

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| COUNTER | on-chip | rtcc |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial port-polling; serial port-interrupt |
| I2C | on-chip | i2c port-polling |
| DMA | on-chip | ldma | |
| WATCHDOG | on-chip | watchdog |

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PB0 | GPIO | LED0 |
| PB1 | GPIO | LED1 |
| PD2 | GPIO | Push Button PB0 |
| PD3 | GPIO | Push Button PB1 |
| PD4 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA5 | USART1\_TX | UART Console EFM\_BC\_TX US1\_TX |
| PA6 | USART1\_RX | UART Console EFM\_BC\_RX US1\_RX |

The default configuration can be found in
[boards/silabs/radio\_boards/slwrb4180a/slwrb4180a\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180a/slwrb4180a_defconfig)

### System Clock

The EFR32MG21 SoC is configured to use the 38.4 MHz external oscillator on the
board.

### Serial Port

The EFR32MG21 SoC has three USARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

### Flashing

Connect the BRD4001A board with a mounted BRD4180A radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4180a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! slwrb4180a
```
