---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodbus__adu.html
original_path: doxygen/html/structmodbus__adu.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus\_adu Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MODBUS](group__modbus.md)

Frame struct used internally and for raw ADU support.
[More...](#details)

`#include <[modbus.h](modbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [trans\_id](#a04f0aa95985cc491649ba47f8ba064c8) |
|  | Transaction Identifier. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [proto\_id](#ae0422aacfe323ce6ca83069a54315fa0) |
|  | Protocol Identifier. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [length](#aa33f175677a0100c1f8a84a72c5ca247) |
|  | Length of the data only (not the length of unit ID + PDU). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [unit\_id](#ab1fc3e76f3f406c8a0715055088d290d) |
|  | Unit Identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [fc](#a015e7b842349dc5567cc51cbf1f87420) |
|  | Function Code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a7e94e4a0557717445ab2d791f8a97b7b) [CONFIG\_MODBUS\_BUFFER\_SIZE - 4] |
|  | Transaction Data. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc](#a78b8008e05c8d588d0ecba71e432d14e) |
|  | RTU CRC. |

## Detailed Description

Frame struct used internally and for raw ADU support.

## Field Documentation

## [◆ ](#a78b8008e05c8d588d0ecba71e432d14e)crc

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modbus\_adu::crc |
| --- |

RTU CRC.

## [◆ ](#a7e94e4a0557717445ab2d791f8a97b7b)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modbus\_adu::data[CONFIG\_MODBUS\_BUFFER\_SIZE - 4] |
| --- |

Transaction Data.

## [◆ ](#a015e7b842349dc5567cc51cbf1f87420)fc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modbus\_adu::fc |
| --- |

Function Code.

## [◆ ](#aa33f175677a0100c1f8a84a72c5ca247)length

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modbus\_adu::length |
| --- |

Length of the data only (not the length of unit ID + PDU).

## [◆ ](#ae0422aacfe323ce6ca83069a54315fa0)proto\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modbus\_adu::proto\_id |
| --- |

Protocol Identifier.

## [◆ ](#a04f0aa95985cc491649ba47f8ba064c8)trans\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modbus\_adu::trans\_id |
| --- |

Transaction Identifier.

## [◆ ](#ab1fc3e76f3f406c8a0715055088d290d)unit\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modbus\_adu::unit\_id |
| --- |

Unit Identifier.

---

The documentation for this struct was generated from the following file:

- zephyr/modbus/[modbus.h](modbus_8h_source.md)

- [modbus\_adu](structmodbus__adu.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
