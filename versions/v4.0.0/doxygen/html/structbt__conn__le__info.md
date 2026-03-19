---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__info.html
original_path: doxygen/html/structbt__conn__le__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

LE Connection Info Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [src](#a5f1eacec82f31182460d6d5359a8b295) |
|  | Source (Local) Identity Address. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [dst](#a1f78e1c0ed3482ce6eec9ce6eeda4769) |
|  | Destination (Remote) Identity Address or remote Resolvable Private Address (RPA) before identity has been resolved. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [local](#a3be5df0deb0af08f84843eb3c6a5e5ae) |
|  | Local device address used during connection setup. |
| const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | [remote](#a236d1c97c735c7cfaead0b1a3672d512) |
|  | Remote device address used during connection setup. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a95a1f635e53f16d5839cdd58f4bda962) |
|  | Connection interval. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [latency](#acd83835fe5ec0878fd653b87cb570a49) |
|  | Connection peripheral latency. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#afb4dc594d063fbbad2bcd4acf047f716) |
|  | Connection supervision timeout. |
| const struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md) \* | [phy](#a215d39c6cd7da1ac033529b5541cbfc1) |
| const struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md) \* | [data\_len](#ae309f390c8d7b33a4de55791af235ab0) |

## Detailed Description

LE Connection Info Structure.

## Field Documentation

## [◆ ](#ae309f390c8d7b33a4de55791af235ab0)data\_len

| const struct [bt\_conn\_le\_data\_len\_info](structbt__conn__le__data__len__info.md)\* bt\_conn\_le\_info::data\_len |
| --- |

## [◆ ](#a1f78e1c0ed3482ce6eec9ce6eeda4769)dst

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_conn\_le\_info::dst |
| --- |

Destination (Remote) Identity Address or remote Resolvable Private Address (RPA) before identity has been resolved.

## [◆ ](#a95a1f635e53f16d5839cdd58f4bda962)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_info::interval |
| --- |

Connection interval.

## [◆ ](#acd83835fe5ec0878fd653b87cb570a49)latency

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_info::latency |
| --- |

Connection peripheral latency.

## [◆ ](#a3be5df0deb0af08f84843eb3c6a5e5ae)local

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_conn\_le\_info::local |
| --- |

Local device address used during connection setup.

## [◆ ](#a215d39c6cd7da1ac033529b5541cbfc1)phy

| const struct [bt\_conn\_le\_phy\_info](structbt__conn__le__phy__info.md)\* bt\_conn\_le\_info::phy |
| --- |

## [◆ ](#a236d1c97c735c7cfaead0b1a3672d512)remote

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_conn\_le\_info::remote |
| --- |

Remote device address used during connection setup.

## [◆ ](#a5f1eacec82f31182460d6d5359a8b295)src

| const [bt\_addr\_le\_t](structbt__addr__le__t.md)\* bt\_conn\_le\_info::src |
| --- |

Source (Local) Identity Address.

## [◆ ](#afb4dc594d063fbbad2bcd4acf047f716)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_info::timeout |
| --- |

Connection supervision timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_info](structbt__conn__le__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
