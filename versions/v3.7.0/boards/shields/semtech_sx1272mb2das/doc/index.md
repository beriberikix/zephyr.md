---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/boards/shields/semtech_sx1272mb2das/doc/index.html
original_path: boards/shields/semtech_sx1272mb2das/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Semtech SX1272MB2DAS LoRa Shield

## Overview

The Semtech SX1272MB2DAS LoRa shield is an Arduino
compatible shield based on the SX1272 LoRa transceiver
from Semtech.

More information about the shield can be found
at the [mbed SX1272MB2xAS website](https://os.mbed.com/components/SX1272MB2xAS/) [[1]](#id1).

### Pins Assignment of the Semtech SX1272MB2DAS LoRa Shield

| Shield Connector Pin | Function |
| --- | --- |
| A0 | SX1272 RESET |
| D2 | SX1272 DIO0 |
| D3 | SX1272 DIO1 |
| D4 | SX1272 DIO2 |
| D5 | SX1272 DIO3 |
| D10 | SX1272 SPI NSS |
| D11 | SX1272 SPI MOSI |
| D12 | SX1272 SPI MISO |
| D13 | SX1272 SPI SCK |

The SX1272 signals DIO4 and DIO5 are not available at the shield connector.

## Requirements

This shield can only be used with a board which provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield semtech_sx1272mb2das` when you invoke `west build`. For
example:

```shell
# From the root of the zephyr repository
west build -b nucleo_f429zi --shield semtech_sx1272mb2das samples/subsys/lorawan/class_a
```

## References

[[1](#id2)]

[https://os.mbed.com/components/SX1272MB2xAS/](https://os.mbed.com/components/SX1272MB2xAS/)
