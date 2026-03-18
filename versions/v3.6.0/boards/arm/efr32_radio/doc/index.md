---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/arm/efr32_radio/doc/index.html
original_path: boards/arm/efr32_radio/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# EFR32 Radio Boards

## Overview

Support for EFR32 Radio boards is provided by one of the starter kits

- [SLWSTK6020B Bluetooth SoC Starter Kit](https://www.silabs.com/products/development-tools/wireless/bluetooth/blue-gecko-bluetooth-low-energy-soc-starter-kit)
- [SLWSTK6000B Mighty Gecko Wireless Starter Kit](https://www.silabs.com/products/development-tools/wireless/mesh-networking/mighty-gecko-starter-kit)
- [SLWSTK6061B Proprietary Wireless Starter Kit](https://www.silabs.com/products/development-tools/wireless/proprietary/slwstk6061b-efr32-flex-gecko-868-mhz-2-4-ghz-and-sub-ghz-starter-kit)
- [SLWSTK6006A Mighty Gecko Wireless Starter Kit](https://www.silabs.com/products/development-tools/wireless/efr32xg21-wireless-starter-kit)

![SLWSTK6020B Bluetooth SoC Starter Kit](../../../../_images/efr32_slwstk6020b.jpg)

SLWSTK6020B (image courtesy of Silicon Labs)

## Hardware

Wireless Starter Kit Mainboard:

- Advanced Energy Monitoring provides real-time information about the energy
  consumption of an application or prototype design.
- Ultra-low power 128x128 pixel memory LCD
- 2 user buttons and 2 LEDs
- 20 pin expansion header
- Si7021 Humidity and Temperature Sensor
- On-board Segger J-Link USB and Ethernet debugger

For more information about the BRD4001A board, refer to these documents:

- [EFR32BG13 Blue Gecko Bluetooth Starter Kit User’s Guide](https://www.silabs.com/documents/public/user-guides/ug279-brd4104a-user-guide.pdf)
- [EFR32MG21 Mighty Gecko Wireless Starter Kit User’s Guide](https://www.silabs.com/documents/public/user-guides/ug385-brd4180a-user-guide.pdf)
- [WSTK Main Board BRD4001A Schematics](https://www.silabs.com/documents/public/schematic-files/BRD4001A-A01-schematic.pdf)

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

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PF4 | GPIO | LED0 |
| PF5 | GPIO | LED1 |
| PF6 | GPIO | Push Button PB0 |
| PF7 | GPIO | Push Button PB1 |
| PA5 | GPIO | Board Controller Enable EFM\_BC\_EN |
| PA0 | USART0\_TX | UART Console EFM\_BC\_TX US0\_TX #0 |
| PA1 | USART0\_RX | UART Console EFM\_BC\_RX US0\_RX #0 |
| PC6 | SPI\_MOSI | Flash MOSI US1\_TX #11 |
| PC7 | SPI\_MISO | Flash MISO US1\_RX #11 |
| PC8 | SPI\_SCLK | Flash SCLK US1\_CLK #11 |
| PA4 | SPI\_CS | Flash Chip Select (GPIO) |

## Programming and Debugging

The BRD4001A includes an [J-Link](https://www.segger.com/jlink-debug-probes.html) serial and debug adaptor built into the
board. The adaptor provides:

- A USB connection to the host computer, which exposes a debug interface and a
  USB Serial Port.
- A physical UART connection which is relayed over interface USB Serial port.
- An Ethernet connection to support remote debugging.

It is compatible with the following host debug tools:

- [OpenOCD Debug Host Tools](../../../../develop/flash_debug/host-tools.md#openocd-debug-host-tools)
- [J-Link Debug Host Tools](../../../../develop/flash_debug/host-tools.md#jlink-debug-host-tools)

OpenOCD is included in the Zephyr SDK. Refer to the links above for information
on how to install required host debug tools if you are not using the Zephyr SDK.

### Flashing

Connect the BRD4001A main board with the mounted radio module to your host
computer using the USB port.

Following example shows how to build the [Hello World](../../../../samples/hello_world/README.md#hello-world) application for
BRD4104A radio module.

```shell
# From the root of the zephyr repository
west build -b efr32_radio_brd4104a samples/hello_world
west flash
```

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you should see the following message in the terminal:

```shell
Hello World! efr32_radio_brd4104a
```
