---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/radio_boards/slwrb4161a/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4161a/doc/index.html
---

# EFR32MG12 2.4 GHz 19 dBm (SLWRB4161A)

Board Overview

[![../../../../../_images/efr32mg12-slwrb4161a.jpeg](../../../../../_images/efr32mg12-slwrb4161a.jpeg)
](../../../../../_images/efr32mg12-slwrb4161a.jpeg)

EFR32MG12 2.4 GHz 19 dBm (SLWRB4161A)

Name:
:   `slwrb4161a`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg12p432f1024gl125

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/radio_boards/slwrb4161a/doc/index.rst/../..)

## Overview

The EFR32MG12 Mighty Gecko Radio Board contains a Wireless System-On-Chip
from the EFR32MG12 family built on an ARM Cortex®-M4F processor with excellent
low power capabilities.

The BRD4161A a.k.a. SLWRB4161A radio board plugs into the Wireless Starter Kit
Mainboard BRD4001A and is supported as one of [Radio Boards](../../index.md#silabs-radio-boards).

## Hardware

- EFR32MG12P432F1024GL125 Mighty Gecko SoC
- CPU core: ARM Cortex®-M4 with FPU
- Flash memory: 1024 kB
- RAM: 256 kB
- Transmit power: up to +19 dBm
- Operation frequency: 2.4 GHz and Sub-Ghz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).

For more information about the EFR32MG12 SoC and BRD4170A board, refer to these
documents:

- [EFR32MG12 Website](https://www.silabs.com/wireless/zigbee/efr32mg12-series-1-socs)
- [EFR32MG12 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg12-datasheet.pdf)
- [EFR32xG12 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg12-rm.pdf)
- [BRD4161A User Guide](https://www.silabs.com/documents/public/user-guides/ug260-brd4161a-user-guide.pdf)

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
| SPI(M) | on-chip | spi port-polling |
| WATCHDOG | on-chip | watchdog |

The default configuration can be found in
[boards/silabs/radio\_boards/slwrb4161a/slwrb4161a\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4161a/slwrb4161a_defconfig)

### Connections and IOs

In the following table, the column **Pin** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Pin | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PF6 | GPIO | Push Button PB0 |
| PF7 | GPIO | Push Button PB1 |
| PA5 | GPIO | Board Controller Enable VCOM\_ENABLE |
| PA0 | USART0\_TX | UART Console VCOM\_TX US0\_TX #0 |
| PA1 | USART0\_RX | UART Console VCOM\_RX US0\_RX #0 |
| PC6 | SPI\_MOSI | Flash MOSI US1\_TX #11 |
| PC7 | SPI\_MISO | Flash MISO US1\_RX #11 |
| PC8 | SPI\_SCLK | Flash SCLK US1\_CLK #11 |
| PA4 | SPI\_CS | Flash Chip Select (GPIO) |

### System Clock

The EFR32MG12P SoC is configured to use the 38.4 MHz external oscillator on the
board.

### Serial Port

The EFR32MG12P SoC has four USARTs and one Low Energy UARTs (LEUART).
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

### Flashing

Connect the BRD4001A board with a mounted BRD4161A radio module to your host
computer using the USB port.

Here is an example for the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4161a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! slwrb4161a
```
