---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structgpio__ra__callback.html
original_path: doxygen/html/structgpio__ra__callback.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_ra\_callback Struct Reference

`#include <[renesas_ra_external_interrupt.h](renesas__ra__external__interrupt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [device](structdevice.md) \* | [port](#ae2a5801c1a3f38dbb1c7b83fcf6373d5) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [port\_num](#acb33518d1af46916fbbe0acd666b1bbc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pin](#a5e89aec076339fb4debe3a6b2041cf34) |
| enum gpio\_int\_trig | [trigger](#a78fde66020bebe07d34c63ade045d269) |
| enum gpio\_int\_mode | [mode](#a5c89f78aba384aa8fcbef25ae48c3bcd) |
| void(\* | [isr](#afe6c9d43bf51368103f8210e13b6c550) )(const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](#a5e89aec076339fb4debe3a6b2041cf34)) |

## Field Documentation

## [◆ ](#afe6c9d43bf51368103f8210e13b6c550)isr

| void(\* gpio\_ra\_callback::isr) (const struct [device](structdevice.md) \*dev, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) [pin](#a5e89aec076339fb4debe3a6b2041cf34)) |
| --- |

## [◆ ](#a5c89f78aba384aa8fcbef25ae48c3bcd)mode

| enum gpio\_int\_mode gpio\_ra\_callback::mode |
| --- |

## [◆ ](#a5e89aec076339fb4debe3a6b2041cf34)pin

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio\_ra\_callback::pin |
| --- |

## [◆ ](#ae2a5801c1a3f38dbb1c7b83fcf6373d5)port

| struct [device](structdevice.md)\* gpio\_ra\_callback::port |
| --- |

## [◆ ](#acb33518d1af46916fbbe0acd666b1bbc)port\_num

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gpio\_ra\_callback::port\_num |
| --- |

## [◆ ](#a78fde66020bebe07d34c63ade045d269)trigger

| enum gpio\_int\_trig gpio\_ra\_callback::trigger |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/misc/renesas\_ra\_external\_interrupt/[renesas\_ra\_external\_interrupt.h](renesas__ra__external__interrupt_8h_source.md)

- [gpio\_ra\_callback](structgpio__ra__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
