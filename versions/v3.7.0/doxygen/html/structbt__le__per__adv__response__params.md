---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__le__per__adv__response__params.html
original_path: doxygen/html/structbt__le__per__adv__response__params.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_response\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [request\_event](#a1af01d0a027fb8659615874acbd388f9) |
|  | The periodic event counter of the request the response is sent to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [request\_subevent](#a3fc8ab0feb06714b28d22439cce60e41) |
|  | The subevent counter of the request the response is sent to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_subevent](#a0cec222d5ba8cc9e20939d441646c913) |
|  | The subevent the response shall be sent in. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot](#aea0428083ccd5f4dccc17e494f38b7c3) |
|  | The response slot the response shall be sent in. |

## Field Documentation

## [◆ ](#a1af01d0a027fb8659615874acbd388f9)request\_event

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_per\_adv\_response\_params::request\_event |
| --- |

The periodic event counter of the request the response is sent to.

[bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md "bt_le_per_adv_sync_recv_info")

Note
:   The response can be sent up to one periodic interval after the request was received.

## [◆ ](#a3fc8ab0feb06714b28d22439cce60e41)request\_subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_params::request\_subevent |
| --- |

The subevent counter of the request the response is sent to.

[bt\_le\_per\_adv\_sync\_recv\_info](structbt__le__per__adv__sync__recv__info.md "bt_le_per_adv_sync_recv_info")

## [◆ ](#aea0428083ccd5f4dccc17e494f38b7c3)response\_slot

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_params::response\_slot |
| --- |

The response slot the response shall be sent in.

## [◆ ](#a0cec222d5ba8cc9e20939d441646c913)response\_subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_response\_params::response\_subevent |
| --- |

The subevent the response shall be sent in.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_response\_params](structbt__le__per__adv__response__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
