---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmspi__xfer.html
original_path: doxygen/html/structmspi__xfer.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_xfer Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Transfer API](group__mspi__transfer__api.md)

MSPI peripheral xfer format This includes transfer related settings that may require configuring the hardware.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [async](#abf10b3fed96161447ffb7a8a6dce7649) |
|  | Async or sync transfer. |
| enum [mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) | [xfer\_mode](#afa30e0fac32c6c3e7a3c9d7e29ccc8cb) |
|  | Transfer Mode. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_dummy](#adfe7adf63f83f40d1ab92ed511f4e917) |
|  | Configure TX dummy cycles. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_dummy](#a98f23415592095749a853f3d850d399f) |
|  | Configure RX dummy cycles. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_length](#a387dd891ab994d75561b50a094427d22) |
|  | Configure command length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr\_length](#ace851e368d69b76092f8429d83d963fd) |
|  | Configure address length. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [hold\_ce](#a335fd5fb02bc75053902c4d1b294af57) |
|  | Hold CE active after xfer. |
| struct [mspi\_ce\_control](structmspi__ce__control.md) | [ce\_sw\_ctrl](#ae2e7a475ac4bcec88f12742642087505) |
|  | Software CE control. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [priority](#a8a829f14523acb252507e291b574363d) |
|  | Priority 0 = Low (best effort) 1 = High (service immediately). |
| const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md) \* | [packets](#a49e4102b694ffb5f9afe72c81fb7ca94) |
|  | Transfer packets. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_packet](#a4061b26045ef860b8c9a6509ff054bc3) |
|  | Number of transfer packets. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timeout](#afd83aa864cf300e9848ef46b7331ca5a) |
|  | Transfer timeout value. |

## Detailed Description

MSPI peripheral xfer format This includes transfer related settings that may require configuring the hardware.

## Field Documentation

## [◆ ](#ace851e368d69b76092f8429d83d963fd)addr\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_xfer::addr\_length |
| --- |

Configure address length.

## [◆ ](#abf10b3fed96161447ffb7a8a6dce7649)async

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_xfer::async |
| --- |

Async or sync transfer.

## [◆ ](#ae2e7a475ac4bcec88f12742642087505)ce\_sw\_ctrl

| struct [mspi\_ce\_control](structmspi__ce__control.md) mspi\_xfer::ce\_sw\_ctrl |
| --- |

Software CE control.

## [◆ ](#a387dd891ab994d75561b50a094427d22)cmd\_length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_xfer::cmd\_length |
| --- |

Configure command length.

## [◆ ](#a335fd5fb02bc75053902c4d1b294af57)hold\_ce

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_xfer::hold\_ce |
| --- |

Hold CE active after xfer.

## [◆ ](#a4061b26045ef860b8c9a6509ff054bc3)num\_packet

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xfer::num\_packet |
| --- |

Number of transfer packets.

## [◆ ](#a49e4102b694ffb5f9afe72c81fb7ca94)packets

| const struct [mspi\_xfer\_packet](structmspi__xfer__packet.md)\* mspi\_xfer::packets |
| --- |

Transfer packets.

## [◆ ](#a8a829f14523acb252507e291b574363d)priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_xfer::priority |
| --- |

Priority 0 = Low (best effort) 1 = High (service immediately).

## [◆ ](#a98f23415592095749a853f3d850d399f)rx\_dummy

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_xfer::rx\_dummy |
| --- |

Configure RX dummy cycles.

## [◆ ](#afd83aa864cf300e9848ef46b7331ca5a)timeout

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_xfer::timeout |
| --- |

Transfer timeout value.

## [◆ ](#adfe7adf63f83f40d1ab92ed511f4e917)tx\_dummy

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mspi\_xfer::tx\_dummy |
| --- |

Configure TX dummy cycles.

## [◆ ](#afa30e0fac32c6c3e7a3c9d7e29ccc8cb)xfer\_mode

| enum [mspi\_xfer\_mode](group__mspi__interface.md#ga116259bbb1d12a10c2ba9e6051f2f000) mspi\_xfer::xfer\_mode |
| --- |

Transfer Mode.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_xfer](structmspi__xfer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
