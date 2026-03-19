---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__le__per__adv__subevent__data__params.html
original_path: doxygen/html/structbt__le__per__adv__subevent__data__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_per\_adv\_subevent\_data\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [subevent](#a55f2da6041b538b3bc4bff38cd4d2953) |
|  | The subevent to set data for. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot\_start](#a1354e9505239de3c42969138d719d775) |
|  | The first response slot to listen to. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [response\_slot\_count](#a86d858606943a82917835a0172e88663) |
|  | The number of response slots to listen to. |
| const struct [net\_buf\_simple](structnet__buf__simple.md) \* | [data](#a46103c988d8ac360b7e26310a0322b4e) |
|  | The data to send. |

## Field Documentation

## [◆ ](#a46103c988d8ac360b7e26310a0322b4e)data

| const struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_le\_per\_adv\_subevent\_data\_params::data |
| --- |

The data to send.

## [◆ ](#a86d858606943a82917835a0172e88663)response\_slot\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_count |
| --- |

The number of response slots to listen to.

## [◆ ](#a1354e9505239de3c42969138d719d775)response\_slot\_start

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_subevent\_data\_params::response\_slot\_start |
| --- |

The first response slot to listen to.

## [◆ ](#a55f2da6041b538b3bc4bff38cd4d2953)subevent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_per\_adv\_subevent\_data\_params::subevent |
| --- |

The subevent to set data for.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_per\_adv\_subevent\_data\_params](structbt__le__per__adv__subevent__data__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
