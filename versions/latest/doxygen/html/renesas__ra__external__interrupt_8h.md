---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas__ra__external__interrupt_8h.html
original_path: doxygen/html/renesas__ra__external__interrupt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_ra\_external\_interrupt.h File Reference

`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](renesas__ra__external__interrupt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gpio\_ra\_callback](structgpio__ra__callback.md) |

| Functions | |
| --- | --- |
| int | [gpio\_ra\_interrupt\_set](#ab32020826df52c8ae436a1160d5b0605) (const struct [device](structdevice.md) \*dev, struct [gpio\_ra\_callback](structgpio__ra__callback.md) \*callback) |
| void | [gpio\_ra\_interrupt\_unset](#ab5b65b767c07a8f2c532e0ad0f3ef450) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port\_num, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |

## Function Documentation

## [◆ ](#ab32020826df52c8ae436a1160d5b0605)gpio\_ra\_interrupt\_set()

| int gpio\_ra\_interrupt\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_ra\_callback](structgpio__ra__callback.md) \* | *callback* ) |

## [◆ ](#ab5b65b767c07a8f2c532e0ad0f3ef450)gpio\_ra\_interrupt\_unset()

| void gpio\_ra\_interrupt\_unset | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *port\_num*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [renesas\_ra\_external\_interrupt](dir_dbfa80aaa1bc15a2c1d7fcdf12d925d3.md)
- [renesas\_ra\_external\_interrupt.h](renesas__ra__external__interrupt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
