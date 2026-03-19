---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmpl__cmd__ntf.html
original_path: doxygen/html/structmpl__cmd__ntf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpl\_cmd\_ntf Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Proxy](group__bt__media__proxy.md)

Media command notification.
[More...](#details)

`#include <[media_proxy.h](media__proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [requested\_opcode](#adcd5228cef8b7629d54053b155a91aa7) |
|  | The opcode that was sent. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [result\_code](#a776bd9459d320e609697905067c0b284) |
|  | The result of the operation. |

## Detailed Description

Media command notification.

## Field Documentation

## [◆ ](#adcd5228cef8b7629d54053b155a91aa7)requested\_opcode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mpl\_cmd\_ntf::requested\_opcode |
| --- |

The opcode that was sent.

## [◆ ](#a776bd9459d320e609697905067c0b284)result\_code

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mpl\_cmd\_ntf::result\_code |
| --- |

The result of the operation.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[media\_proxy.h](media__proxy_8h_source.md)

- [mpl\_cmd\_ntf](structmpl__cmd__ntf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
