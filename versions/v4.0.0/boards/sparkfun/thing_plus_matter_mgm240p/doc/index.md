---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/sparkfun/thing_plus_matter_mgm240p/doc/index.html
original_path: boards/sparkfun/thing_plus_matter_mgm240p/doc/index.html
---

# SparkFun Thing Plus Matter

## Overview

The MGM240P Mighty Sparkfun Think Plus Matter contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

[![MGM240P Sparkfun Think Plus Matter](../../../../_images/MGM240P_Thing_Plus.jpg)
](../../../../_images/MGM240P_Thing_Plus.jpg)

MGM240P Sparkfun Think Plus Matter (image courtesy of Sparkfun)

## Hardware

- Based on the Series 2 EFR32MG24 SoC
- CPU core: 32-bit ARM® Cortex®-M33 core at 39 MHz
- Flash memory: 1536 kB
- RAM: 256 kB
- Supports Multiple 802.15.4 Wireless Protocols (Zigbee and OpenThread)
- Bluetooth Low Energy 5.3
- Crystals for LFXO (32 kHz) and HFXO (39 MHz).

For more information about the EFR32MG24 SoC and BRD2601B board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs#)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg24-rm.pdf)
- [MGM240P Datasheet](https://cdn.sparkfun.com/assets/1/4/5/e/5/MGM240P-Datasheet.pdf)
- [MGM240P Schematics](https://cdn.sparkfun.com/assets/0/f/8/4/9/Thing_Plus_MGM240P.pdf)

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| COUNTER | on-chip | stimer |
| FLASH | on-chip | flash memory |
| GPIO | on-chip | gpio |
| UART | on-chip | serial |
| TRNG | on-chip | semailbox |
| WATCHDOG | on-chip | watchdog |
| I2C(M/S) | on-chip | i2c |
| RADIO | on-chip | bluetooth |

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on PORTA, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA8 | GPIO | LED0 |
| PA5 | USART0\_TX | UART Console EFM\_BC\_TX US0\_TX |
| PA6 | USART0\_RX | UART Console EFM\_BC\_RX US0\_RX |

The default configuration can be found in
[boards/sparkfun/thing\_plus\_matter\_mgm240p/sparkfun\_thing\_plus\_matter\_mgm240p\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/sparkfun/thing_plus_matter_mgm240p/sparkfun_thing_plus_matter_mgm240p_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
from [J-Link-Downloads](https://www.segger.com/downloads/jlink)

### Flashing

The sample application [Hello World](../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b sparkfun_thing_plus_mgm240p samples/hello_world
```

Connect the sparkfun\_thing\_plus\_mgm240p to your host computer using the USB port and you
should see a USB connection.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! _sparkfun_thing_plus_matter_mgm240p
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

```shell
# From the root of the zephyr repository
west build -b sparkfun_thing_plus_matter_mgm240p samples/bluetooth/observer
```
