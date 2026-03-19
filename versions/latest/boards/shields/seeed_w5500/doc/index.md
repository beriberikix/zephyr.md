---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/boards/shields/seeed_w5500/doc/index.html
original_path: boards/shields/seeed_w5500/doc/index.html
---

# Seeed W5500 Ethernet Shield

## Overview

Seeed [W5500 Ethernet Shield](https://wiki.seeedstudio.com/W5500_Ethernet_Shield_v1.0) [[2]](#id4) is an Arduino connector shield with:

- [W5500](https://wiznet.io/products/iethernet-chips/w5500) [[1]](#id2) 10/100 MBPS stand alone Ethernet controller with on-board MAC & PHY
  and 16 KiloBytes for FIFO buffer,
- SPI serial interface,
- Grove UART connector,
- Grove I2C connector,
- SD card slot.

![Seeed W5500 Ethernet Shield](../../../../_images/seeed_w5500.webp)

Seeed W5500 Ethernet Shield

### Pins Assignment of the W5500 Shield

| Shield Connector Pin | Function |
| --- | --- |
| RST | Ethernet Controller’s Reset |
| D2 | Ethernet Controller’s Interrupt Output |
| D10 | SPI’s Chip Select |
| D11 | SPI’s Master Output Slave Input (MOSI) |
| D12 | SPI’s Master Input Slave Output (MISO) |
| D13 | SPI’s Clock |

## Requirements

This shield can only be used with a board that provides a configuration
for Arduino connectors and defines node aliases for SPI and GPIO interfaces
(see [Shields](../../../../hardware/porting/shields.md#shields) for more details).

## Programming

Set `--shield seeed_w5500` when you invoke `west build`. For example:

```shell
# From the root of the zephyr repository
west build -b nrf52840dk/nrf52840 --shield seeed_w5500 samples/net/dhcpv4_client
```

## References

[[1](#id3)]

[https://wiznet.io/products/iethernet-chips/w5500](https://wiznet.io/products/iethernet-chips/w5500)

[[2](#id5)]

[https://wiki.seeedstudio.com/W5500\_Ethernet\_Shield\_v1.0](https://wiki.seeedstudio.com/W5500_Ethernet_Shield_v1.0)
