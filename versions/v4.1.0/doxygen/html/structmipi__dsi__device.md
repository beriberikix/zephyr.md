---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmipi__dsi__device.html
original_path: doxygen/html/structmipi__dsi__device.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi\_device Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DSI driver APIs](group__mipi__dsi__interface.md)

MIPI-DSI device.
[More...](#details)

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_lanes](#ae2e6fddb1651a71c1b969ecec295e1c0) |
|  | Number of data lanes. |
| struct [mipi\_dsi\_timings](structmipi__dsi__timings.md) | [timings](#af9ec42cd1fcb16cf63060b0097180f3f) |
|  | Display timings. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pixfmt](#a729dd69843ee3eaf6bd5cbd2e725fdea) |
|  | Pixel format. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [mode\_flags](#af22eab1f95d8865fe7a67e49d6e36f8c) |
|  | Mode flags. |

## Detailed Description

MIPI-DSI device.

## Field Documentation

## [◆ ](#ae2e6fddb1651a71c1b969ecec295e1c0)data\_lanes

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mipi\_dsi\_device::data\_lanes |
| --- |

Number of data lanes.

## [◆ ](#af22eab1f95d8865fe7a67e49d6e36f8c)mode\_flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_device::mode\_flags |
| --- |

Mode flags.

## [◆ ](#a729dd69843ee3eaf6bd5cbd2e725fdea)pixfmt

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_device::pixfmt |
| --- |

Pixel format.

## [◆ ](#af9ec42cd1fcb16cf63060b0097180f3f)timings

| struct [mipi\_dsi\_timings](structmipi__dsi__timings.md) mipi\_dsi\_device::timings |
| --- |

Display timings.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dsi.h](drivers_2mipi__dsi_8h_source.md)

- [mipi\_dsi\_device](structmipi__dsi__device.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
