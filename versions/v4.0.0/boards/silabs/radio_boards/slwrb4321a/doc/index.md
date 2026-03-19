---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/silabs/radio_boards/slwrb4321a/doc/index.html
original_path: boards/silabs/radio_boards/slwrb4321a/doc/index.html
---

# WGM160P Wi-Fi Module (SLWRB4321A)

Board Overview

[![../../../../../_images/wgm160p-starter-kit.jpg](../../../../../_images/wgm160p-starter-kit.jpg)
](../../../../../_images/wgm160p-starter-kit.jpg)

WGM160P Wi-Fi Module (SLWRB4321A)

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efm32gg11b820f2048gm64

## Overview

The WGM160P Starter Kit SLWSTK6121A comes with the BRD4321A radio board.
This radio boards contains a WGM160P module, which combines the WF200 Wi-Fi
transceiver with an EFM32GG11 microcontroller.

## Hardware

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra low power 128x128 pixel color Memory-LCD
- 2 user buttons and 2 LEDs
- Si7021 Humidity and Temperature Sensor
- On-board Segger J-Link USB and Ethernet debugger
- 10/100Base-TX ethernet PHY and RJ-45 jack (on included expansion board)
- MicroSD card slot
- USB Micro-AB connector

For more information about the WGM160P and SLWSTK6121A board:

- [WGM160P Website](https://www.silabs.com/wireless/wi-fi/wfm160-series-1-modules)
- [WGM160P Datasheet](https://www.silabs.com/documents/public/data-sheets/wgm160p-datasheet.pdf)
- [SLWSTK6121A Website](https://www.silabs.com/development-tools/wireless/wi-fi/wgm160p-wifi-module-starter-kit)
- [SLWSTK6121A User Guide](https://www.silabs.com/documents/public/user-guides/ug351-brd4321a-user-guide.pdf)
- [EFM32GG11 Datasheet](https://www.silabs.com/documents/public/data-sheets/efm32gg11-datasheet.pdf)
- [EFM32GG11 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efm32gg11-rm.pdf)
- [WF200 Datasheet](https://www.silabs.com/documents/public/data-sheets/wf200-datasheet.pdf)

### Supported Features

The slwrb4321a board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| COUNTER | on-chip | rtcc |
| ETHERNET | on-chip | ethernet |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c port-polling |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| UART | on-chip | serial port-polling; serial port-interrupt |

The default configuration can be found in
[boards/silabs/radio\_boards/slwrb4321a/slwrb4321a\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/radio_boards/slwrb4321a/slwrb4321a_defconfig)

Other hardware features, including the WF200 WiFi transceiver, are
currently not supported by the port.

### Connections and IOs

The WGM160P’s EFM32GG11 SoC has six GPIO controllers (PORTA to PORTF), all of which are
currently enabled for the SLWSTK6121A board.

In the following table, the column **Name** contains pin names. For example, PE1
means pin number 1 on PORTE, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA4 | GPIO | LED0 |
| PA5 | GPIO | LED1 |
| PD6 | GPIO | Push Button PB0 |
| PD8 | GPIO | Push Button PB1 |
| PE7 | UART\_TX | UART TX Console VCOM\_TX US0\_TX #1 |
| PE6 | UART\_RX | UART RX Console VCOM\_RX US0\_RX #1 |
| PB11 | I2C\_SDA | SENSOR\_I2C\_SDA I2C1\_SDA #1 |
| PB12 | I2C\_SCL | SENSOR\_I2C\_SCL I2C1\_SCL #1 |

### System Clock

The EFM32GG11 SoC is configured to use the 50 MHz external oscillator on the
board.

### Serial Port

The EFM32GG11 SoC has four USARTs, two UARTs and two Low Energy UARTs (LEUART).
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The SLWSTK6121A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer
- A physical UART connection which is relayed over interface USB serial port.

#### Flashing an application to SLWSTK6121A

Connect the SLWSTK6121A to your host computer using the USB port.

Here is an example to build and flash the [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") application.

```shell
# From the root of the zephyr repository
west build -b slwrb4321a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! slwrb4321a
```
