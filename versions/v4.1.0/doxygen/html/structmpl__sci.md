---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmpl__sci.html
original_path: doxygen/html/structmpl__sci.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpl\_sci Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Proxy](group__bt__media__proxy.md)

Search control item.
[More...](#details)

`#include <[media_proxy.h](media__proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#a348314407c7b46d5ed583b97dfe932bc) |
|  | Length of type and parameter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a1dfc87f7e8b509ca05cbcd97a245953f) |
|  | MEDIA\_PROXY\_SEARCH\_TYPE\_<...>. |
| char | [param](#abcb13d8005212f480eaaf8a8296f6023) [62] |
|  | Search parameter. |

## Detailed Description

Search control item.

## Field Documentation

## [◆ ](#a348314407c7b46d5ed583b97dfe932bc)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mpl\_sci::len |
| --- |

Length of type and parameter.

## [◆ ](#abcb13d8005212f480eaaf8a8296f6023)param

| char mpl\_sci::param[62] |
| --- |

Search parameter.

## [◆ ](#a1dfc87f7e8b509ca05cbcd97a245953f)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mpl\_sci::type |
| --- |

MEDIA\_PROXY\_SEARCH\_TYPE\_<...>.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[media\_proxy.h](media__proxy_8h_source.md)

- [mpl\_sci](structmpl__sci.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
