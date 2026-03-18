---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodbus__server__param.html
original_path: doxygen/html/structmodbus__server__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus\_server\_param Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MODBUS](group__modbus.md)

Modbus server parameter.
[More...](#details)

`#include <[modbus.h](modbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [modbus\_user\_callbacks](structmodbus__user__callbacks.md) \* | [user\_cb](#ad8f72ea4e7dbbd81e23415e25b7d94be) |
|  | Pointer to the User Callback structure. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unit\_id](#a323a3a9be08f3c77df9f06b135f7f379) |
|  | Modbus unit ID of the server. |

## Detailed Description

Modbus server parameter.

## Field Documentation

## [◆ ](#a323a3a9be08f3c77df9f06b135f7f379)unit\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modbus\_server\_param::unit\_id |
| --- |

Modbus unit ID of the server.

## [◆ ](#ad8f72ea4e7dbbd81e23415e25b7d94be)user\_cb

| struct [modbus\_user\_callbacks](structmodbus__user__callbacks.md)\* modbus\_server\_param::user\_cb |
| --- |

Pointer to the User Callback structure.

---

The documentation for this struct was generated from the following file:

- zephyr/modbus/[modbus.h](modbus_8h_source.md)

- [modbus\_server\_param](structmodbus__server__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
