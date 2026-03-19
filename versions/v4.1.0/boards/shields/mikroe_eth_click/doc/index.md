---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/mikroe_eth_click/doc/index.html
original_path: boards/shields/mikroe_eth_click/doc/index.html
---

# MikroElektronika ETH Click

## Overview

ETH Click is an accessory board in mikroBus™ form factor. It features [ENC28J60](https://www.microchip.com/wwwproducts/en/en022889) [[2]](#id3),
a 28-pin, 10BASE-T stand alone Ethernet Controller with an on-board MAC & PHY,
8K Bytes of Buffer RAM and SPI serial interface.
More information at [Eth Click Shield website](https://www.mikroe.com/eth-click) [[1]](#id1).

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

Set `--shield mikroe_eth_click` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b lpcxpresso55s69 --shield mikroe_eth_click samples/net/dhcpv4_client
```

## References

[[1](#id2)]

[https://www.mikroe.com/eth-click](https://www.mikroe.com/eth-click)

[[2](#id4)]

[https://www.microchip.com/wwwproducts/en/en022889](https://www.microchip.com/wwwproducts/en/en022889)
