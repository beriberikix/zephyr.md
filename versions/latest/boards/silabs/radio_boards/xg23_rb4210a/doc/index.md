---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/radio_boards/xg23_rb4210a/doc/index.html
original_path: boards/silabs/radio_boards/xg23_rb4210a/doc/index.html
---

# EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)

Board Overview

[![../../../../../_images/efr32zg23-xg23-rb4210a.jpg](../../../../../_images/efr32zg23-xg23-rb4210a.jpg)
](../../../../../_images/efr32zg23-xg23-rb4210a.jpg)

EFR32xG23 868-915 MHz 20 dBm (xG23-RB4210A)

Name:
:   `xg23_rb4210a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32zg23b020f512im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/xg23_rb4210a/doc/index.rst/../..)

## Overview

The EFR32ZG23 Radio Board is the radio board delivered with
[xG23-PK6068A Website](https://www.silabs.com/development-tools/wireless/efr32xg23-pro-kit-20-dbm). It contains a Wireless System-On-Chip from the
EFR32ZG23 family built on an ARM Cortex®-M33 processor with excellent low
power capabilities.

The BRD4210A a.k.a. xG23-RB4210A radio board plugs into the Wireless Pro Kit
Mainboard BRD4002A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32ZG23B020F512IM48 SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 512 kB
- RAM: 64 kB
- Transmit power: up to +20 dBm
- Operation frequency: 868-915 MHz
- Crystals for LFXO (32.768 kHz) and HFXO (39 MHz).
- Silicon Labs Si7021 relative humidity and temperature sensor
- Low-power 128x128 pixel Memory LCD
- Macronix ultra low power 8-Mbit SPI flash (MX25R8035F)

For more information about the EFR32ZG23 SoC and BRD4210A board, refer to these
documents:

- [EFR32ZG23 Website](https://www.silabs.com/wireless/z-wave/800-series-modem-soc)
- [EFR32ZG23 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32zg23-datasheet.pdf)
- [EFR32xG23 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg23-rm.pdf)
- [xG23-PK6068A Website](https://www.silabs.com/development-tools/wireless/efr32xg23-pro-kit-20-dbm)
- [BRD4210A User Guide](https://www.silabs.com/documents/public/user-guides/ug507-brd4210a-user-guide.pdf)

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
| DMA | on-chip | ldma |
| I2C | on-chip | i2c |
| SPI | on-chip | spi |
| TRNG | on-chip | semailbox |
| WATCHDOG | on-chip | watchdog |
| ACMP | on-chip | comparator |

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA8 | EUSART0\_TX | UART Console TX |
| PA9 | EUSART0\_RX | UART Console RX |
| PB0 | GPIO | Board Controller Enable |
| PB1 | GPIO | Push Button 0 |
| PB2 | GPIO | LED0 |
| PB3 | GPIO | Push Button 1 |
| PC1 | EUSART1\_TX | Display/Flash SPI MOSI |
| PC2 | EUSART1\_RX | Flash SPI MISO |
| PC3 | EUSART1\_CLK | Display/Flash SPI Clock |
| PC4 | GPIO | Flash SPI Chip Select |
| PC5 | I2C0\_SCL | Si7021 I2C Clock |
| PC6 | GPIO | Display COM Inversion |
| PC7 | I2C0\_SDA | Si7021 I2C Data |
| PC8 | GPIO | Display SPI Chip Select |
| PC9 | GPIO | Display/Si7021 Enable |
| PD3 | GPIO | LED1 |

The default configuration can be found in
[boards/silabs/radio\_boards/xg23\_rb4210a/xg23\_rb4210a\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/xg23_rb4210a/xg23_rb4210a_defconfig)

### System Clock

The EFR32ZG23 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32ZG23 SoC has one USART and three EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

### Flashing

Connect the BRD4002A board with a mounted BRD4210A radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b xg23_rb4210a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! xg23_rb4210a/efr32zg23b020f512im48
```
