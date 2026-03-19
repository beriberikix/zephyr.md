---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmipi__dsi__timings.html
original_path: doxygen/html/structmipi__dsi__timings.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi\_timings Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MIPI-DSI driver APIs](group__mipi__dsi__interface.md)

MIPI-DSI display timings.
[More...](#details)

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hactive](#a3a91e874a7da6c37bf9b06944a3d658a) |
|  | Horizontal active video. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hfp](#ad1b00493166d0276eb66d73be4b6968d) |
|  | Horizontal front porch. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hbp](#afb4451d7767a911ea6a92a9fbba5e935) |
|  | Horizontal back porch. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hsync](#a58f985d9c43cd149959dad7f12fcff8e) |
|  | Horizontal sync length. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vactive](#acc8077892efa4977fd667680d63f5c7c) |
|  | Vertical active video. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vfp](#ac44c32c7d150ddd4b327308196169578) |
|  | Vertical front porch. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vbp](#afff80261d02253b76a872ee805a4cd46) |
|  | Vertical back porch. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vsync](#a535e0177862b753ef9f4af011ed483a4) |
|  | Vertical sync length. |

## Detailed Description

MIPI-DSI display timings.

## Field Documentation

## [◆ ](#a3a91e874a7da6c37bf9b06944a3d658a)hactive

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::hactive |
| --- |

Horizontal active video.

## [◆ ](#afb4451d7767a911ea6a92a9fbba5e935)hbp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::hbp |
| --- |

Horizontal back porch.

## [◆ ](#ad1b00493166d0276eb66d73be4b6968d)hfp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::hfp |
| --- |

Horizontal front porch.

## [◆ ](#a58f985d9c43cd149959dad7f12fcff8e)hsync

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::hsync |
| --- |

Horizontal sync length.

## [◆ ](#acc8077892efa4977fd667680d63f5c7c)vactive

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::vactive |
| --- |

Vertical active video.

## [◆ ](#afff80261d02253b76a872ee805a4cd46)vbp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::vbp |
| --- |

Vertical back porch.

## [◆ ](#ac44c32c7d150ddd4b327308196169578)vfp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::vfp |
| --- |

Vertical front porch.

## [◆ ](#a535e0177862b753ef9f4af011ed483a4)vsync

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mipi\_dsi\_timings::vsync |
| --- |

Vertical sync length.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mipi\_dsi.h](drivers_2mipi__dsi_8h_source.md)

- [mipi\_dsi\_timings](structmipi__dsi__timings.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
