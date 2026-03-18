---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/pjrc/teensy4/doc/index.html
original_path: boards/pjrc/teensy4/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# PJRC TEENSY 4

## Overview

The Teensy is a complete USB-based microcontroller development system, in a
very small footprint, capable of implementing many types of projects. All
programming is done via the USB port.

![TEENSY40](../../../../_images/teensy40.jpg)

TEENSY40 (Credit: [https://www.pjrc.com](https://www.pjrc.com))

![TEENSY41](../../../../_images/teensy41.jpg)

TEENSY41 (Credit: [https://www.pjrc.com](https://www.pjrc.com))

## Hardware

Teensy 4.0:

- MIMXRT1062DVL6A MCU (600 MHz, 1024 KB on-chip memory)
- 16 Mbit QSPI Flash
- LED
- USB 2.0 host connector

Teensy 4.1:

- MIMXRT1062DVJ6A MCU (600 MHz, 1024 KB on-chip memory)
- 64 Mbit QSPI Flash
- LED
- USB 2.0 host connector
- USB 2.0 OTG connector
- 10/100 Mbit/s Ethernet PHY
- TF socket for SD card

See the [Teensy 4.0 Website](https://www.pjrc.com/store/teensy40.html) for a complete hardware description.

### Supported Features

The teensy40 board configuration supports the following hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| NVIC | on-chip | nested vector interrupt controller |
| SYSTICK | on-chip | systick |
| GPIO | on-chip | gpio |
| I2C | on-chip | i2c |
| UART | on-chip | serial port-polling; serial port-interrupt |
| USB | on-chip | USB device |

The default configuration can be found in
[boards/pjrc/teensy4/teensy40\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pjrc/teensy4/teensy40_defconfig)

The teensy41 board configuration supports additional hardware
features:

| Interface | Controller | Driver/Component |
| --- | --- | --- |
| SDHC | on-chip | disk access |
| ENET | on-chip | ethernet |

The default configuration can be found in
[boards/pjrc/teensy4/teensy41\_defconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/pjrc/teensy4/teensy41_defconfig)

Other hardware features are not currently supported by the port.

### Connections and IOs

Pin mappings from Teensy to MIMXRT1062 SoC.

| Pin | Pad ID | Usage |
| --- | --- | --- |
| 0 | AD\_B0\_03 | GPIO1\_3 / UART6\_RX / CAN2\_RX |
| 1 | AD\_B0\_02 | GPIO1\_2 / UART6\_TX / CAN2\_TX |
| 2 | EMC\_04 | GPIO4\_4 |
| 3 | EMC\_05 | GPIO4\_5 |
| 4 | EMC\_06 | GPIO4\_6 |
| 5 | EMC\_08 | GPIO4\_8 |
| 6 | B0\_10 | GPIO2\_10 |
| 7 | B1\_01 | GPIO2\_17 / UART4\_RX |
| 8 | B1\_00 | GPIO2\_16 / UART4\_TX |
| 9 | B0\_11 | GPIO2\_11 |
| 10 | B0\_00 | GPIO2\_0 |
| 11 | B0\_02 | GPIO2\_2 |
| 12 | B0\_01 | GPIO2\_1 |
| 13 | B0\_03 | GPIO2\_3 / LED |
| 14 | AD\_B1\_02 | GPIO1\_18 / UART2\_TX |
| 15 | AD\_B1\_03 | GPIO1\_19 / UART2\_RX |
| 16 | AD\_B1\_07 | GPIO1\_23 / UART3\_RX / I2C3\_SCL |
| 17 | AD\_B1\_06 | GPIO1\_22 / UART3\_TX / I2C3\_SDA |
| 18 | AD\_B1\_01 | GPIO1\_17 / I2C1\_SDA |
| 19 | AD\_B1\_00 | GPIO1\_16 / I2C1\_SCL |
| 20 | AD\_B1\_10 | GPIO1\_26 / UART8\_TX |
| 21 | AD\_B1\_11 | GPIO1\_27 / UART8\_RX |
| 22 | AD\_B1\_08 | GPIO1\_24 / CAN1\_TX |
| 23 | AD\_B1\_09 | GPIO1\_25 / CAN1\_RX |
| 24 | AD\_B0\_12 | GPIO1\_12 / UART1\_TX / I2C4\_SCL |
| 25 | AD\_B0\_13 | GPIO1\_13 / UART1\_RX / I2C4\_SDA |
| 26 | AD\_B1\_14 | GPIO1\_30 |
| 27 | AD\_B1\_15 | GPIO1\_31 |
| 28 | EMC\_32 | GPIO3\_18 / UART7\_RX |
| 29 | EMC\_31 | GPIO4\_31 / UART7\_TX |
| 30 | EMC\_37 | GPIO3\_23 / CAN3\_RX |
| 31 | EMC\_36 | GPIO3\_22 / CAN3\_TX |
| 32 | B0\_12 | GPIO2\_12 |
| 33 | EMC\_07 | GPIO4\_7 |

Only Teensy 4.0:

| 34 | SD\_B0\_03 | GPIO3\_15 |
| --- | --- | --- |
| 35 | SD\_B0\_02 | GPIO3\_14 |
| 36 | SD\_B0\_01 | GPIO3\_13 |
| 37 | SD\_B0\_00 | GPIO3\_12 |
| 38 | SD\_B0\_05 | GPIO3\_17 |
| 39 | SD\_B0\_04 | GPIO3\_16 |

Only Teensy 4.1:

| 34 | B1\_13 | GPIO2\_29 / UART5\_RX |
| --- | --- | --- |
| 35 | B1\_12 | GPIO2\_28 / UART5\_TX |
| 36 | B1\_02 | GPIO2\_18 |
| 37 | B1\_03 | GPIO2\_19 |
| 38 | AD\_B1\_12 | GPIO1\_28 |
| 39 | AD\_B1\_13 | GPIO1\_29 |
| 40 | AD\_B1\_04 | GPIO1\_20 |
| 41 | AD\_B1\_05 | GPIO1\_21 |

## Programming and Debugging

### Flashing

Build applications as usual (see [Building an Application](../../../../develop/application/index.md#build-an-application) for more details).

Flash hex-file with the documented tools:

### Debugging

Console output is mapped to teensy pins 0 (RX1) and 1 (TX1). Connect a usb-to-serial adapter
to use this serial console. Use the following settings with your serial terminal of choice (minicom, putty,
etc.):

- Speed: 115200
- Data: 8 bits
- Parity: None
- Stop bits: 1

## References
