---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/semtech_sx1276mb1mas/doc/index.html
original_path: boards/shields/semtech_sx1276mb1mas/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Semtech SX1276MB1MAS LoRa Shield

## Overview

The Semtech SX1276MB1MAS LoRa shield is an Arduino compatible shield based on
the SX1276 LoRa transceiver from Semtech.

More information about the shield can be found at the [mbed SX1276MB1xAS
website](https://os.mbed.com/components/SX1276MB1xAS/) [[1]](#id1).

### Pins Assignment of the Semtech SX1276MB1MAS LoRa Shield

| Shield Connector Pin | Function |
| --- | --- |
| A0 | SX1276 RESET |
| A3 | SX1276 DIO4 (1) |
| A4 | Antenna RX/TX |
| D2 | SX1276 DIO0 |
| D3 | SX1276 DIO1 |
| D4 | SX1276 DIO2 |
| D5 | SX1276 DIO3 |
| D8 | SX1276 DIO4 (1) |
| D9 | SX1276 DIO5 |
| D10 | SX1276 SPI NSS |
| D11 | SX1276 SPI MOSI |
| D12 | SX1276 SPI MISO |
| D13 | SX1276 SPI SCK |

1. SX1276 DIO4 is configured on D8 by default. It is possible to reconfigure it
   in devicetree to A3 if needed.

## Requirements

This shield can only be used with a board which provides a configuration for
Arduino connectors and defines node aliases for SPI and GPIO interfaces (see
[Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `-DSHIELD=semtech_sx1271mb1mas` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b nucleo_l073rz samples/subsys/lorawan/class_a -- -DSHIELD=semtech_sx1276mb1mas
```

## References

[[1](#id2)]

[https://os.mbed.com/components/SX1276MB1xAS/](https://os.mbed.com/components/SX1276MB1xAS/)
