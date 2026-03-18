---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionpd__ext__header.html
original_path: doxygen/html/unionpd__ext__header.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_ext\_header Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Build an extended message header See Table 6-3 Extended Message Header.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [data\_size](#a4a7a948d3463ddfbebf1d75faeda293e): 9 |  |
|  | Number of total bytes in data block. [More...](#a4a7a948d3463ddfbebf1d75faeda293e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [reserved0](#aae09d0399c0a121e3c216047e908b9ec): 1 |  |
|  | Reserved. [More...](#aae09d0399c0a121e3c216047e908b9ec) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [request\_chunk](#a36a65a1e52875721758d1273b0e76279): 1 |  |
|  | 1 for a chunked message, else 0 [More...](#a36a65a1e52875721758d1273b0e76279) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [chunk\_number](#aced0489c4e2462652c0d91187c07b27e): 4 |  |
|  | Chunk number when chkd = 1, else 0. [More...](#aced0489c4e2462652c0d91187c07b27e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [chunked](#a180ccc6854c1341e638ca338e6eb1cd8): 1 |  |
|  | 1 for chunked messages [More...](#a180ccc6854c1341e638ca338e6eb1cd8) |
| }; |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [raw\_value](#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f) |
|  | Raw PD Ext Header value. |

## Detailed Description

Build an extended message header See Table 6-3 Extended Message Header.

## Field Documentation

## [◆ ](#a69b9d12c8810ae52b389cef6253f912d)[struct]

| struct { ... } [pd\_ext\_header](unionpd__ext__header.md) |
| --- |

## [◆ ](#aced0489c4e2462652c0d91187c07b27e)chunk\_number

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::chunk\_number |
| --- |

Chunk number when chkd = 1, else 0.

## [◆ ](#a180ccc6854c1341e638ca338e6eb1cd8)chunked

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::chunked |
| --- |

1 for chunked messages

## [◆ ](#a4a7a948d3463ddfbebf1d75faeda293e)data\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::data\_size |
| --- |

Number of total bytes in data block.

## [◆ ](#a8a1d0f0d38b3a5c4aa3a80586e7a1e8f)raw\_value

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::raw\_value |
| --- |

Raw PD Ext Header value.

## [◆ ](#a36a65a1e52875721758d1273b0e76279)request\_chunk

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::request\_chunk |
| --- |

1 for a chunked message, else 0

## [◆ ](#aae09d0399c0a121e3c216047e908b9ec)reserved0

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pd\_ext\_header::reserved0 |
| --- |

Reserved.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_ext\_header](unionpd__ext__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
