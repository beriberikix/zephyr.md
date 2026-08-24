---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rx__external__interrupt_8h.html
original_path: doxygen/html/renesas__rx__external__interrupt_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rx\_external\_interrupt.h File Reference

`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](renesas__rx__external__interrupt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gpio\_rx\_callback](structgpio__rx__callback.md) |

| Functions | |
| --- | --- |
| int | [gpio\_rx\_interrupt\_set](#aaee6debb5a530f1202bf04f05be3ba98) (const struct [device](structdevice.md) \*dev, struct [gpio\_rx\_callback](structgpio__rx__callback.md) \*callback) |
| void | [gpio\_rx\_interrupt\_unset](#aa4e8687d852850bd1ace1fafba911bce) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port\_num, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pin) |

## Function Documentation

## [◆ ](#aaee6debb5a530f1202bf04f05be3ba98)gpio\_rx\_interrupt\_set()

| int gpio\_rx\_interrupt\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [gpio\_rx\_callback](structgpio__rx__callback.md) \* | *callback* ) |

## [◆ ](#aa4e8687d852850bd1ace1fafba911bce)gpio\_rx\_interrupt\_unset()

| void gpio\_rx\_interrupt\_unset | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *port\_num*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *pin* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [renesas\_rx\_external\_interrupt](dir_a87f3c868dca62dbe5503bf385ba65f5.md)
- [renesas\_rx\_external\_interrupt.h](renesas__rx__external__interrupt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
