---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmipi__dsi__msg.html
original_path: doxygen/html/structmipi__dsi__msg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi\_msg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DSI driver APIs](group__mipi__dsi__interface.md)

MIPI-DSI read/write message.
[More...](#details)

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a92dc0767c36f31cb23207a0581d3355f) |
|  | Payload data type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#ac93016853da47dc07094e7fe44e4625f) |
|  | Flags controlling message transmission. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd](#a45ee5101f773a600e116d41a247cdcf4) |
|  | Command (only for DCS). |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [tx\_len](#a4cb0756c8cffa6acc10fee77ba6d4b17) |
|  | Transmission buffer length. |
| const void \* | [tx\_buf](#a73e62f4c7e45f0553fd0deeec06356a2) |
|  | Transmission buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rx\_len](#ab17fda1dbb330bc8e66597ef816f413f) |
|  | Reception buffer length. |
| void \* | [rx\_buf](#aa21b5be5cdfac9411601c83f72e58405) |
|  | Reception buffer. |

## Detailed Description

MIPI-DSI read/write message.

## Field Documentation

## [◆ ](#a45ee5101f773a600e116d41a247cdcf4)cmd

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mipi\_dsi\_msg::cmd |
| --- |

Command (only for DCS).

## [◆ ](#ac93016853da47dc07094e7fe44e4625f)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mipi\_dsi\_msg::flags |
| --- |

Flags controlling message transmission.

## [◆ ](#aa21b5be5cdfac9411601c83f72e58405)rx\_buf

| void\* mipi\_dsi\_msg::rx\_buf |
| --- |

Reception buffer.

## [◆ ](#ab17fda1dbb330bc8e66597ef816f413f)rx\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mipi\_dsi\_msg::rx\_len |
| --- |

Reception buffer length.

## [◆ ](#a73e62f4c7e45f0553fd0deeec06356a2)tx\_buf

| const void\* mipi\_dsi\_msg::tx\_buf |
| --- |

Transmission buffer.

## [◆ ](#a4cb0756c8cffa6acc10fee77ba6d4b17)tx\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mipi\_dsi\_msg::tx\_len |
| --- |

Transmission buffer length.

## [◆ ](#a92dc0767c36f31cb23207a0581d3355f)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mipi\_dsi\_msg::type |
| --- |

Payload data type.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dsi.h](drivers_2mipi__dsi_8h_source.md)

- [mipi\_dsi\_msg](structmipi__dsi__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
