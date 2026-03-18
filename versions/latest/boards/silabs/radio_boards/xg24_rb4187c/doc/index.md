---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
original_path: boards/silabs/radio_boards/xg24_rb4187c/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# EFR32xG24 2.4 GHz 20 dBm (xG24-RB4187C)

## Overview

The EFR32MG24 Mighty Gecko Radio Board is one of the two
radio boards delivered with [xG24-PK6010A Website](https://www.silabs.com/development-tools/wireless/efr32xg24-pro-kit-20-dbm). It contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

![xG24-RB4187C Mighty Gecko Radio Board](../../../../../_images/efr32mg24-xg24-rb4187c.jpg)

xG24-RB4187C (image courtesy of Silicon Labs)

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

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| COUNTER | on-chip | stimer |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |
| I2C | on-chip | i2c |
| TRNG | on-chip | semailbox |
| WATCHDOG | on-chip | watchdog |

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PB2 | GPIO | LED0 |
| PB4 | GPIO | LED1 |
| PB1 | GPIO | Push Button 0 |
| PB3 | GPIO | Push Button 1 |
| PB0 | GPIO | Board Controller Enable VCOM\_ENABLE |
| PA8 | USART0\_TX | UART Console VCOM\_TX US0\_TX |
| PA9 | USART0\_RX | UART Console VCOM\_RX US0\_RX |

The default configuration can be found in
[boards/silabs/radio\_boards/xg24\_rb4187c/xg24\_rb4187c\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg24_rb4187c/xg24_rb4187c_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

### Flashing

Connect the BRD4002A board with a mounted BRD4187C radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello-world) application.

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
