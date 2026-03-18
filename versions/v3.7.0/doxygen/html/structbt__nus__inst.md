---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__nus__inst.html
original_path: doxygen/html/structbt__nus__inst.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_nus\_inst Struct Reference

`#include <[inst.h](inst_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_gatt\_service\_static](structbt__gatt__service__static.md) \* | [svc](#a3a3dd0e1f20e47a39124f10982a6be59) |
|  | Pointer to the NUS Service Instance. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | [cbs](#a47c7d47a0cbad0e5696c64e3592de776) |
|  | List of subscribers to invoke callbacks on asynchronous events. |

## Field Documentation

## [◆ ](#a47c7d47a0cbad0e5696c64e3592de776)cbs

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)\* bt\_nus\_inst::cbs |
| --- |

List of subscribers to invoke callbacks on asynchronous events.

## [◆ ](#a3a3dd0e1f20e47a39124f10982a6be59)svc

| const struct [bt\_gatt\_service\_static](structbt__gatt__service__static.md)\* bt\_nus\_inst::svc |
| --- |

Pointer to the NUS Service Instance.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/nus/[inst.h](inst_8h_source.md)

- [bt\_nus\_inst](structbt__nus__inst.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
