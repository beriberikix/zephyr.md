---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structespi__oob__packet.html
original_path: doxygen/html/structespi__oob__packet.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi\_oob\_packet Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ESPI Driver APIs](group__espi__interface.md)

eSPI out-of-band transaction packet format
[More...](#details)

`#include <[espi.h](espi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a0b19890b5e63ecbd1b95eef57fd9263f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#adf45a10c88a171df8e7138929958b346) |

## Detailed Description

eSPI out-of-band transaction packet format

For Tx packet, eSPI driver client shall specify the OOB payload data and its length in bytes. For Rx packet, eSPI driver client shall indicate the maximum number of bytes that can receive, while the eSPI driver should update the length field with the actual data received/available.

In all cases, the length does not include OOB header size 3 bytes.

## Field Documentation

## [◆ ](#a0b19890b5e63ecbd1b95eef57fd9263f)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* espi\_oob\_packet::buf |
| --- |

## [◆ ](#adf45a10c88a171df8e7138929958b346)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) espi\_oob\_packet::len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[espi.h](espi_8h_source.md)

- [espi\_oob\_packet](structespi__oob__packet.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
