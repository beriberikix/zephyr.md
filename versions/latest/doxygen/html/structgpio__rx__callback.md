---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structgpio__rx__callback.html
original_path: doxygen/html/structgpio__rx__callback.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_rx\_callback Struct Reference

`#include <[zephyr/drivers/misc/renesas_rx_external_interrupt/renesas_rx_external_interrupt.h](renesas__rx__external__interrupt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [device](structdevice.md) \* | [port](#a3d57065fd5dca68a35e33a1d8c195939) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [port\_num](#a46b0d0b6c5a088c8f142f222c1044327) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pin](#ad2e07a69f97532116b893554b6841d52) |
| enum gpio\_int\_trig | [trigger](#a7bbf270c50f0ac44dbf5a1a41773ad77) |
| enum gpio\_int\_mode | [mode](#a325319906ec519a836a1025831d3ca9b) |
| void(\* | [isr](#aa15600e26b37674069c6d3c66aa60d4d) )(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](#ad2e07a69f97532116b893554b6841d52)) |

## Field Documentation

## [◆ ](#aa15600e26b37674069c6d3c66aa60d4d)isr

| void(\* gpio\_rx\_callback::isr) (const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](#ad2e07a69f97532116b893554b6841d52)) |
| --- |

## [◆ ](#a325319906ec519a836a1025831d3ca9b)mode

| enum gpio\_int\_mode gpio\_rx\_callback::mode |
| --- |

## [◆ ](#ad2e07a69f97532116b893554b6841d52)pin

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio\_rx\_callback::pin |
| --- |

## [◆ ](#a3d57065fd5dca68a35e33a1d8c195939)port

| struct [device](structdevice.md)\* gpio\_rx\_callback::port |
| --- |

## [◆ ](#a46b0d0b6c5a088c8f142f222c1044327)port\_num

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio\_rx\_callback::port\_num |
| --- |

## [◆ ](#a7bbf270c50f0ac44dbf5a1a41773ad77)trigger

| enum gpio\_int\_trig gpio\_rx\_callback::trigger |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/misc/renesas\_rx\_external\_interrupt/[renesas\_rx\_external\_interrupt.h](renesas__rx__external__interrupt_8h_source.md)

- [gpio\_rx\_callback](structgpio__rx__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
