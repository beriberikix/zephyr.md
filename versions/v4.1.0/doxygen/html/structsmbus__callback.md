---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsmbus__callback.html
original_path: doxygen/html/structsmbus__callback.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smbus\_callback Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [SMBus Interface](group__smbus__interface.md)

SMBus callback structure.
[More...](#details)

`#include <[smbus.h](smbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a89fb6ad70aa53dba53aa85ebaea91f60) |
|  | This should be used in driver for a callback list management. |
| [smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9) | [handler](#a2017d57f8b1bbed10d37cb24a5212bc1) |
|  | Actual callback function being called when relevant. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#a707cc2c4cd2abf214343686d84cd1594) |
|  | Peripheral device address. |

## Detailed Description

SMBus callback structure.

Used to register a callback in the driver instance callback list. As many callbacks as needed can be added as long as each of them is a unique pointer of struct [smbus\_callback](structsmbus__callback.md "SMBus callback structure.").

Note: Such struct should not be allocated on stack.

## Field Documentation

## [◆ ](#a707cc2c4cd2abf214343686d84cd1594)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) smbus\_callback::addr |
| --- |

Peripheral device address.

## [◆ ](#a2017d57f8b1bbed10d37cb24a5212bc1)handler

| [smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9) smbus\_callback::handler |
| --- |

Actual callback function being called when relevant.

## [◆ ](#a89fb6ad70aa53dba53aa85ebaea91f60)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) smbus\_callback::node |
| --- |

This should be used in driver for a callback list management.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[smbus.h](smbus_8h_source.md)

- [smbus\_callback](structsmbus__callback.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
