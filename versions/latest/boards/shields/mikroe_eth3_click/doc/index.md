---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/mikroe_eth3_click/doc/index.html
original_path: boards/shields/mikroe_eth3_click/doc/index.html
---

# MikroElektronika ETH 3 Click

## Overview

ETH 3 Click is an accessory board in mikroBus™ form factor. It features [LAN9250](https://www.microchip.com/en-us/product/lan9250) [[2]](#id4),
a 10/100Mbps BASE-T stand alone Ethernet Controller with an on-board MAC & PHY,
16Kbyte FIFO Buffer and SPI serial interface.
More information at [ETH 3 Click Shield website](https://www.mikroe.com/eth-3-click) [[1]](#id2).

![MikroElektronika ETH 3 Click](../../../../_images/eth3_click.webp)

MikroElektronika ETH 3 Click (Credit: MikroElektronika)

### Pins Assignment of the Eth Click Shield

| Shield Connector Pin | Function |
| --- | --- |
| RST# | Ethernet Controller’s Reset |
| CS# | SPI’s Chip Select |
| SCK | SPI’s ClocK |
| SDO | SPI’s Slave Data Output (MISO) |
| SDI | SPI’s Slave Data Input (MISO) |
| INT | Ethernet Controller’s Interrupt Output |

## Requirements

This shield can only be used with a board which provides a configuration
for Mikro-BUS connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield mikroe_eth3_click` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b mikroe_stm32_m4_clicker --shield mikroe_eth3_click samples/net/dhcpv4_client
```

## References

[[1](#id3)]

[https://www.mikroe.com/eth-3-click](https://www.mikroe.com/eth-3-click)

[[2](#id5)]

[https://www.microchip.com/en-us/product/lan9250](https://www.microchip.com/en-us/product/lan9250)
