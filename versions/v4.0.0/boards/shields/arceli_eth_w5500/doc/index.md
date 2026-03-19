---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/boards/shields/arceli_eth_w5500/doc/index.html
original_path: boards/shields/arceli_eth_w5500/doc/index.html
---

# ARCELI W5500 ETH

## Overview

ARCELI W5500 Ethernet is breakout board with SPI bus access over 10 pin header.
[W5500](https://wiznet.io/products/iethernet-chips/w5500) [[1]](#id1) is 10/100 MBPS stand alone Ethernet controller with on-board MAC & PHY,
16 KiloBytes for FIFO buffer and SPI serial interface.

### Pins Assignment of the W5500 Shield

| Shield Connector Pin | Function |
| --- | --- |
| RST# | Ethernet Controller’s Reset |
| CS# | SPI’s Chip Select |
| SCK | SPI’s ClocK |
| SDO | SPI’s Slave Data Output (MISO) |
| SDI | SPI’s Slave Data Input (MISO) |
| INT | Ethernet Controller’s Interrupt Output |

## Requirements

This shield/breakout board can be used with any board with SPI interfaces in
Arduino header or custom header (by adjusting the overlay).

## Programming

Set `--shield arceli_eth_w5500` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield arceli_eth_w5500 samples/net/dhcpv4_client
```

## References

[[1](#id2)]

[https://wiznet.io/products/iethernet-chips/w5500](https://wiznet.io/products/iethernet-chips/w5500)
