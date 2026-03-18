---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/boards/shields/arceli_eth_w5500/doc/index.html
original_path: boards/shields/arceli_eth_w5500/doc/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# ARCELI W5500 ETH

## Overview

ARCELI W5500 etherner is breakout board with SPI bus access over 10 pin header.
[W5500](https://www.wiznet.io/product-item/w5500/) [[1]](#id1) is 10/100 MBPS stand alone Ethernet controller with on-board MAC & PHY,
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

Set `-DSHIELD=arceli_eth_w5500` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk_nrf52840 samples/net/dhcpv4_client -- -DSHIELD=arceli_eth_w5500
```

## References

[[1](#id2)]

[https://www.wiznet.io/product-item/w5500/](https://www.wiznet.io/product-item/w5500/)
