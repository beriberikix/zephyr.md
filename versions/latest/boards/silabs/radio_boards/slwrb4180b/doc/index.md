---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/slwrb4180b/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4180b/doc/index.html
---

# EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)

Board Overview

[![../../../../../_images/efr32mg21-slwrb4180b.webp](../../../../../_images/efr32mg21-slwrb4180b.webp)
](../../../../../_images/efr32mg21-slwrb4180b.webp)

EFR32xG21 2.4 GHz 20 dBm (SLWRB4180B)

Name:
:   `slwrb4180b`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg21a020f1024im32

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4180b/doc/index.rst/../..)

## Overview

The EFR32MG21 Mighty Gecko Radio Board is one of the two
radio boards delivered with [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit). It features a
Wireless System-On-Chip (SoC) from the EFR32MG21 family, built on an
ARM Cortex®-M33F processor, offering exceptional low-power performance.

The SLWRB4180B radio board is designed to connect seamlessly with
the Wireless Starter Kit Mainboards BRD4001A and BRD4002A

## Hardware

- EFR32MG21A020F1024IM32 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1024 kB
- RAM: 96 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).

For more information about the EFR32MG21 SoC and BRD4180B board, refer to these
documents:

- [EFR32MG21 Website](https://www.silabs.com/products/wireless/mesh-networking/efr32mg21-series-2-socs)
- [EFR32MG21 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg21-datasheet.pdf)
- [EFR32xG21 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg21-rm.pdf)
- [EFR32-SLWSTK6006A Website](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit)
- [BRD4180B User Guide](https://www.silabs.com/documents/public/user-guides/ug427-brd4180b-user-guide.pdf)

### Supported Features

The `slwrb4180b` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PD2
means Pin number 2 on PORTD, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PD2 | GPIO | LED0 |
| PD3 | GPIO | LED1 |
| PB0 | GPIO | Push Button PB0 |
| PB1 | GPIO | Push Button PB1 |
| PD4 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA5 | USART1\_TX | UART Console EFM\_BC\_TX US1\_TX |
| PA6 | USART1\_RX | UART Console EFM\_BC\_RX US1\_RX |

The default configuration can be found in
[boards/silabs/radio\_boards/slwrb4180b/slwrb4180b\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4180b/slwrb4180b_defconfig)

## Programming and Debugging

The `slwrb4180b` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

Connect the BRD4001A or BRD4002A mainboard, with the BRD4180B radio module mounted,
to your host computer via the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4180b samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! slwrb4180b
```
