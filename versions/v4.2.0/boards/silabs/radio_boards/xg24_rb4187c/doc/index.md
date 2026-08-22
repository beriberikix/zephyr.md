---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
original_path: boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
---

# EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

Board Overview

[![../../../../../_images/efr32mg24-xg24-rb4187c.jpg](../../../../../_images/efr32mg24-xg24-rb4187c.jpg)
](../../../../../_images/efr32mg24-xg24-rb4187c.jpg)

EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

Name:
:   `xg24_rb4187c`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg24b220f1536im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg24_rb4187c/doc/index.rst/../..)

## Overview

The EFR32MG24 Mighty Gecko Radio Board is one of the two
radio boards delivered with [xG24-PK6010A Website](https://www.silabs.com/development-tools/wireless/efr32xg24-pro-kit-20-dbm). It contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

The BRD4187C a.k.a. xG24-RB4187C radio board plugs into the Wireless Pro Kit
Mainboard BRD4002A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32MG24B220F1536IM48 Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).

For more information about the EFR32MG24 SoC and BRD4187C board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/brd4187c-rm.pdf)
- [xG24-PK6010A Website](https://www.silabs.com/development-tools/wireless/efr32xg24-pro-kit-20-dbm)
- [BRD4187C User Guide](https://www.silabs.com/documents/public/user-guides/ug526-brd4187c-user-guide.pdf)

### Supported Features

The `xg24_rb4187c` board supports the hardware features listed below.

on-chip / on-board
:   Feature integrated in the SoC / present on the board.

2 / 2
:   Number of instances that are enabled / disabled.   
    Click on the label to see the first instance of this feature in the board/SoC DTS files.

`vnd,foo`
:   Compatible string for the Devicetree binding matching the feature.   
    Click on the link to view the binding documentation.

### System Clock

The EFR32MG24 SoC is configured to use the HFRCODPLL oscillator at 78 MHz as the system clock,
locked to the 39 MHz external crystal oscillator on the board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

The `xg24_rb4187c` board supports the runners and associated west commands listed below.

|  | **flash** | **debug** |
| --- | --- | --- |

### Flashing

Connect the BRD4002A board with a mounted BRD4187C radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xg24_rb4187c samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg24_rb4187c
```
