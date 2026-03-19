---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structuhc__data.html
original_path: doxygen/html/structuhc__data.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc\_data Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB host controller driver API](group__uhc__api.md)

Common UHC driver data structure.
[More...](#details)

`#include <[uhc.h](uhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [uhc\_device\_caps](structuhc__device__caps.md) | [caps](#ac2a48d1d6692931807e8985799c5bdb0) |
|  | Controller capabilities. |
| struct [k\_mutex](structk__mutex.md) | [mutex](#a08772cdd5b42bd11ca4a06a75df846e9) |
|  | Driver access mutex. |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [ctrl\_xfers](#a32eec449ffbe5e6c262c907e6e6b475a) |
|  | dlist for control transfers |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [bulk\_xfers](#ac6214566324740c34a8bba42515d1d32) |
|  | dlist for bulk transfers |
| [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) | [event\_cb](#afd1a0828a0ca3e397dba09fe38fd8050) |
|  | Callback to submit an UHC event to upper layer. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [status](#a10852f2523cc733541cc9ea51706559f) |
|  | USB host controller status. |
| void \* | [priv](#a294120f6cf8563cb9564c51fcf56d883) |
|  | Driver private data. |

## Detailed Description

Common UHC driver data structure.

Mandatory structure for each UHC controller driver. To be implemented as device's private data (device->data).

## Field Documentation

## [◆ ](#ac6214566324740c34a8bba42515d1d32)bulk\_xfers

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) uhc\_data::bulk\_xfers |
| --- |

dlist for bulk transfers

## [◆ ](#ac2a48d1d6692931807e8985799c5bdb0)caps

| struct [uhc\_device\_caps](structuhc__device__caps.md) uhc\_data::caps |
| --- |

Controller capabilities.

## [◆ ](#a32eec449ffbe5e6c262c907e6e6b475a)ctrl\_xfers

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) uhc\_data::ctrl\_xfers |
| --- |

dlist for control transfers

## [◆ ](#afd1a0828a0ca3e397dba09fe38fd8050)event\_cb

| [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) uhc\_data::event\_cb |
| --- |

Callback to submit an UHC event to upper layer.

## [◆ ](#a08772cdd5b42bd11ca4a06a75df846e9)mutex

| struct [k\_mutex](structk__mutex.md) uhc\_data::mutex |
| --- |

Driver access mutex.

## [◆ ](#a294120f6cf8563cb9564c51fcf56d883)priv

| void\* uhc\_data::priv |
| --- |

Driver private data.

## [◆ ](#a10852f2523cc733541cc9ea51706559f)status

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) uhc\_data::status |
| --- |

USB host controller status.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[uhc.h](uhc_8h_source.md)

- [uhc\_data](structuhc__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
