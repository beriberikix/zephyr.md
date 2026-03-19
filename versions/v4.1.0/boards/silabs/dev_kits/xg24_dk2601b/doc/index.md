---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/silabs/dev_kits/xg24_dk2601b/doc/index.html
original_path: boards/silabs/dev_kits/xg24_dk2601b/doc/index.html
---

# EFR32xG24 Dev Kit (xG24-DK2601B)

Board Overview

[![../../../../../_images/xg24_dk2601b.jpg](../../../../../_images/xg24_dk2601b.jpg)
](../../../../../_images/xg24_dk2601b.jpg)

EFR32xG24 Dev Kit (xG24-DK2601B)

Name:
:   `xg24_dk2601b`

Vendor:
:   Silicon Laboratories

Architecture:
:   arm

SoC:
:   efr32mg24b310f1536im48

[
Browse board sources
](https://github.com/zephyrproject-rtos/zephyr/blob/main//boards/silabs/dev_kits/xg24_dk2601b/doc/index.rst/../..)

## Overview

The EFR32MG24 Mighty Gecko Board dev kit contains
a Wireless System-On-Chip from the EFR32MG24 family built on an
ARM Cortex®-M33F processor with excellent low power capabilities.

## Hardware

- EFR32MG24B310F1536IM48-B Mighty Gecko SoC
- CPU core: ARM Cortex®-M33 with FPU
- Flash memory: 1536 kB
- RAM: 256 kB
- Transmit power: up to +20 dBm
- Operation frequency: 2.4 GHz
- Crystals for LFXO (32.768 kHz) and HFXO (38.4 MHz).
- On board devices:

  - Silicon Labs Si7021 relative humidity & temperature sensor
  - Silicon Labs Si7210 hall effect sensor
  - 2x TDK InvenSense ICS-43434 MEMS microphones with I2S output
  - TDK InvenSense ICM-20689 6-axis inertial measurement sensor
  - Vishay VEML6035 ambient light sensor
  - Bosch BMP384 pressure sensor with internal temperature sensor
  - MX25R3235F 32 Mbit SPI data flash

For more information about the EFR32MG24 SoC and BRD2601B board, refer to these
documents:

- [EFR32MG24 Website](https://www.silabs.com/wireless/zigbee/efr32mg24-series-2-socs#)
- [EFR32MG24 Datasheet](https://www.silabs.com/documents/public/data-sheets/efr32mg24-datasheet.pdf)
- [EFR32xG24 Reference Manual](https://www.silabs.com/documents/public/reference-manuals/efr32xg24-rm.pdf)
- [BRD2601B User Guide](https://www.silabs.com/documents/public/user-guides/ug524-brd2601b-user-guide.pdf)

### Supported Features

The board configuration supports the following hardware features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| MPU | on-chip | memory protection unit |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| SYSRTC | on-chip | counter, timer |
| MSC | on-chip | flash memory |
| GPIO | on-chip | gpio |
| EUSART | on-chip | serial, spi |
| USART | on-chip | serial, spi |
| LDMA | on-chip | dma |
| SE | on-chip | entropy |
| WDOG | on-chip | watchdog |
| I2C | on-chip | i2c |
| RADIO | on-chip | bluetooth |
| ACMP | on-chip | comparator |

Other hardware features are currently not supported by the port.

### Connections and IOs

In the following table, the column **Name** contains Pin names. For example, PA2
means Pin number 2 on Port A, as used in the board’s datasheets and manuals.

| Name | Function | Usage |
| --- | --- | --- |
| PA4 | GPIO | LED0 |
| PB0 | GPIO | LED1 |
| PD2 | GPIO | LED2 |
| PB2 | GPIO | Push Button 0 |
| PB3 | GPIO | Push Button 1 |
| PA5 | USART0\_TX | UART Console |
| PA6 | USART0\_RX | UART Console |
| PC3 | EUSART1\_TX | SPI bus: flash, IMU |
| PC2 | EUSART1\_RX | SPI bus: flash, IMU |
| PC1 | EUSART1\_SCLK | SPI bus: flash, IMU |
| PC0 | EUSART1\_CS | SPI bus: flash |
| PC4 | I2C0\_SCL | I2C bus |
| PC5 | I2C0\_SDA | I2C bus |

The default configuration can be found in
[boards/silabs/dev\_kits/xg24\_dk2601b/xg24\_dk2601b\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/silabs/dev_kits/xg24_dk2601b/xg24_dk2601b_defconfig)

### System Clock

The EFR32MG24 SoC is configured to use the 39 MHz external oscillator on the
board.

### Serial Port

The EFR32MG24 SoC has one USART and two EUSARTs.
USART0 is connected to the board controller and is used for the console.

## Programming and Debugging

Note

Before using the kit the first time, you should update the J-Link firmware
in Simplicity Studio.

### Flashing

The sample application [Hello World](../../../../../samples/hello_world/README.md#hello_world "Print "Hello World" to the console.") is used for this example.
Build the Zephyr kernel and application:

```shell
# From the root of the zephyr repository
west build -b xg24_dk2601b samples/hello_world
```

Connect the xg24\_dk2601b to your host computer using the USB port and you
should see a USB connection.

Open a serial terminal (minicom, putty, etc.) with the following settings:

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

Reset the board and you’ll see the following message on the corresponding serial port
terminal session:

```shell
Hello World! xg24_dk2601b
```

### Bluetooth

To use the BLE function, run the command below to retrieve necessary binary
blobs from the SiLabs HAL repository.

```shell
west blobs fetch hal_silabs
```

Then build the Zephyr kernel and a Bluetooth sample with the following
command. The [Observer](../../../../../samples/bluetooth/observer/README.md#bluetooth_observer "Scan for Bluetooth devices nearby and print their information.") sample application is used in
this example.

```shell
# From the root of the zephyr repository
west build -b xg24_dk2601b samples/bluetooth/observer
```
