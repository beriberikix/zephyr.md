---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsmbus__dt__spec.html
original_path: doxygen/html/structsmbus__dt__spec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smbus\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SMBus Interface](group__smbus__interface.md)

Complete SMBus DT information.
[More...](#details)

`#include <[smbus.h](smbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [bus](#a2b34afb2bc5d55382bc11e0a5ee72684) |
|  | SMBus bus. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a0f6080e33e04405a42e9d29118512d08) |
|  | Address of the SMBus peripheral device. |

## Detailed Description

Complete SMBus DT information.

## Field Documentation

## [◆ ](#a0f6080e33e04405a42e9d29118512d08)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) smbus\_dt\_spec::addr |
| --- |

Address of the SMBus peripheral device.

## [◆ ](#a2b34afb2bc5d55382bc11e0a5ee72684)bus

| const struct [device](structdevice.md)\* smbus\_dt\_spec::bus |
| --- |

SMBus bus.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[smbus.h](smbus_8h_source.md)

- [smbus\_dt\_spec](structsmbus__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
