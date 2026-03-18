---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodbus__iface__param.html
original_path: doxygen/html/structmodbus__iface__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus\_iface\_param Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MODBUS](group__modbus.md)

User parameter structure to configure Modbus interface as client or server.
[More...](#details)

`#include <[modbus.h](modbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) | [mode](#ae73f218d8810afb0c2efbf865ba8b3ba) |
|  | Mode of the interface. |
| union { |  |
| struct [modbus\_server\_param](structmodbus__server__param.md)   [server](#a77d88f81d11b0f9338ca227930abf53d) |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [rx\_timeout](#a7726b39e43e660adb63e24b4cf2e7ab7) |  |
|  | Amount of time client will wait for a response from the server. [More...](#a7726b39e43e660adb63e24b4cf2e7ab7) |
| }; |  |
| union { |  |
| struct [modbus\_serial\_param](structmodbus__serial__param.md)   [serial](#a77ff747b2e789e96691483994be1d596) |  |
|  | Serial support parameter of the interface. [More...](#a77ff747b2e789e96691483994be1d596) |
| struct [modbus\_raw\_cb](structmodbus__raw__cb.md)   [rawcb](#a6e06fe6fc4ba31b25b5ef461ee0e4f81) |  |
|  | Pointer to raw ADU callback function. [More...](#a6e06fe6fc4ba31b25b5ef461ee0e4f81) |
| }; |  |

## Detailed Description

User parameter structure to configure Modbus interface as client or server.

## Field Documentation

## [◆ ](#ad1051fdf8c0a8b094a98bb6f1d953530)[union]

| union { ... } [modbus\_iface\_param](structmodbus__iface__param.md) |
| --- |

## [◆ ](#af97ac97c4970ae077d8e10fa304817fa)[union]

| union { ... } [modbus\_iface\_param](structmodbus__iface__param.md) |
| --- |

## [◆ ](#ae73f218d8810afb0c2efbf865ba8b3ba)mode

| enum [modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) modbus\_iface\_param::mode |
| --- |

Mode of the interface.

## [◆ ](#a6e06fe6fc4ba31b25b5ef461ee0e4f81)rawcb

| struct [modbus\_raw\_cb](structmodbus__raw__cb.md) modbus\_iface\_param::rawcb |
| --- |

Pointer to raw ADU callback function.

## [◆ ](#a7726b39e43e660adb63e24b4cf2e7ab7)rx\_timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) modbus\_iface\_param::rx\_timeout |
| --- |

Amount of time client will wait for a response from the server.

## [◆ ](#a77ff747b2e789e96691483994be1d596)serial

| struct [modbus\_serial\_param](structmodbus__serial__param.md) modbus\_iface\_param::serial |
| --- |

Serial support parameter of the interface.

## [◆ ](#a77d88f81d11b0f9338ca227930abf53d)server

| struct [modbus\_server\_param](structmodbus__server__param.md) modbus\_iface\_param::server |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modbus/[modbus.h](modbus_8h_source.md)

- [modbus\_iface\_param](structmodbus__iface__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
