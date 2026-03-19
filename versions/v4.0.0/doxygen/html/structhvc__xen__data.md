---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structhvc__xen__data.html
original_path: doxygen/html/structhvc__xen__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hvc\_xen\_data Struct Reference

`#include <[console.h](xen_2console_8h_source.md)>`

| Data Fields | |
| --- | --- |
|  | [DEVICE\_MMIO\_RAM](#ae3cc2fc4118482bd8cd1f4405f68fef9) |
| const struct [device](structdevice.md) \* | [dev](#a1284a2f575e96b702a56798c7305c727) |
| struct [xencons\_interface](structxencons__interface.md) \* | [intf](#aab82bfb5b5da4f24731615882a987115) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [evtchn](#ace0cad3a06743f22e2e5e2d771f6b0e6) |
| [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) | [irq\_cb](#af8b24d53152774a9b15b24a0228fc9f5) |
| void \* | [irq\_cb\_data](#aa711ee34dac5db363dc00060174821b3) |

## Field Documentation

## [◆ ](#a1284a2f575e96b702a56798c7305c727)dev

| const struct [device](structdevice.md)\* hvc\_xen\_data::dev |
| --- |

## [◆ ](#ae3cc2fc4118482bd8cd1f4405f68fef9)DEVICE\_MMIO\_RAM

| hvc\_xen\_data::DEVICE\_MMIO\_RAM |
| --- |

## [◆ ](#ace0cad3a06743f22e2e5e2d771f6b0e6)evtchn

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) hvc\_xen\_data::evtchn |
| --- |

## [◆ ](#aab82bfb5b5da4f24731615882a987115)intf

| struct [xencons\_interface](structxencons__interface.md)\* hvc\_xen\_data::intf |
| --- |

## [◆ ](#af8b24d53152774a9b15b24a0228fc9f5)irq\_cb

| [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) hvc\_xen\_data::irq\_cb |
| --- |

## [◆ ](#aa711ee34dac5db363dc00060174821b3)irq\_cb\_data

| void\* hvc\_xen\_data::irq\_cb\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/[console.h](xen_2console_8h_source.md)

- [hvc\_xen\_data](structhvc__xen__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
