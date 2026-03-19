---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__event__data.html
original_path: doxygen/html/structmspi__event__data.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_event\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI callback API](group__mspi__callback__api.md)

MSPI event data.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [controller](#af788dc5374778055d1ee9fddbe2a4d8d) |
|  | Pointer to the bus controller. |
| const struct [mspi\_dev\_id](structmspi__dev__id.md) \* | [dev\_id](#ab1138c26f9a6b11b75e1e50fb3e5d8e9) |
|  | Pointer to the peripheral device ID. |
| const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \* | [packet](#a1bb8c4591ced464181927b0c00003205) |
|  | Pointer to a transfer packet. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [status](#a4b926cf5abb4f23bb7e1f85fecd323ef) |
|  | MSPI event status. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [packet\_idx](#a6e71714475e45a0d758aa49db33ff57e) |
|  | Packet index. |

## Detailed Description

MSPI event data.

## Field Documentation

## [◆ ](#af788dc5374778055d1ee9fddbe2a4d8d)controller

| const struct [device](structdevice.md)\* mspi\_event\_data::controller |
| --- |

Pointer to the bus controller.

## [◆ ](#ab1138c26f9a6b11b75e1e50fb3e5d8e9)dev\_id

| const struct [mspi\_dev\_id](structmspi__dev__id.md)\* mspi\_event\_data::dev\_id |
| --- |

Pointer to the peripheral device ID.

## [◆ ](#a1bb8c4591ced464181927b0c00003205)packet

| const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md)\* mspi\_event\_data::packet |
| --- |

Pointer to a transfer packet.

## [◆ ](#a6e71714475e45a0d758aa49db33ff57e)packet\_idx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_event\_data::packet\_idx |
| --- |

Packet index.

## [◆ ](#a4b926cf5abb4f23bb7e1f85fecd323ef)status

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_event\_data::status |
| --- |

MSPI event status.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_event\_data](structmspi__event__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
