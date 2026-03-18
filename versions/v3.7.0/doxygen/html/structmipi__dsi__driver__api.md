---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmipi__dsi__driver__api.html
original_path: doxygen/html/structmipi__dsi__driver__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DSI driver APIs](group__mipi__dsi__interface.md)

MIPI-DSI host driver API.
[More...](#details)

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [attach](#a17ebe7832179f0f57d6bf89d631ba16c) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [transfer](#aa521f40ca114dbf1d37d6f158819861e) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg) |
| int(\* | [detach](#a1fbbf38f9918623f69a8a7a9f9ddaf34) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |

## Detailed Description

MIPI-DSI host driver API.

## Field Documentation

## [◆ ](#a17ebe7832179f0f57d6bf89d631ba16c)attach

| int(\* mipi\_dsi\_driver\_api::attach) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
| --- |

## [◆ ](#a1fbbf38f9918623f69a8a7a9f9ddaf34)detach

| int(\* mipi\_dsi\_driver\_api::detach) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
| --- |

## [◆ ](#aa521f40ca114dbf1d37d6f158819861e)transfer

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* mipi\_dsi\_driver\_api::transfer) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dsi.h](drivers_2mipi__dsi_8h_source.md)

- [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
