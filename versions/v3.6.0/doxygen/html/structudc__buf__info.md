---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structudc__buf__info.html
original_path: doxygen/html/structudc__buf__info.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc\_buf\_info Struct Reference

UDC endpoint buffer info.
[More...](#details)

`#include <[udc.h](udc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ep](#a0a1c09f587d3f6847cb7ce77514a3321) |
|  | Endpoint to which request is associated. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [setup](#a9664e1f7cddd36dbc7d206b52da45170): 1 |
|  | Flag marks setup transfer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [data](#ab500ff0bf12ecdbbd4f3cb48d0556ed2): 1 |
|  | Flag marks data stage of setup transfer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [status](#a84cf74496eddc4a69a47d23dcdbf753f): 1 |
|  | Flag marks status stage of setup transfer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [zlp](#afc2d0c391aca7f68a1ae5539a1fed8a0): 1 |
|  | Flag marks ZLP at the end of a transfer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [claimed](#a9b03b6dd8418d4200733a612aac73daa): 1 |
|  | Flag marks request buffer claimed by the controller (TBD). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [queued](#a4cd2e83000a0551d126bebe89552eab9): 1 |
|  | Flag marks request buffer is queued (TBD). |
| void \* | [owner](#a33e927f23d227a4974915c65927284ec) |
|  | Transfer owner (usually pointer to a class instance). |
| int | [err](#af1c92f1cdd6e0474a19f788140fdc573) |
|  | Transfer result, 0 on success, other values on error. |

## Detailed Description

UDC endpoint buffer info.

This structure is mandatory for all UDC request. It contains the meta data about the request and is stored in user\_data array of [net\_buf](structnet__buf.md "Network buffer representation.") structure for each request.

## Field Documentation

## [◆ ](#a9b03b6dd8418d4200733a612aac73daa)claimed

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::claimed |
| --- |

Flag marks request buffer claimed by the controller (TBD).

## [◆ ](#ab500ff0bf12ecdbbd4f3cb48d0556ed2)data

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::data |
| --- |

Flag marks data stage of setup transfer.

## [◆ ](#a0a1c09f587d3f6847cb7ce77514a3321)ep

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) udc\_buf\_info::ep |
| --- |

Endpoint to which request is associated.

## [◆ ](#af1c92f1cdd6e0474a19f788140fdc573)err

| int udc\_buf\_info::err |
| --- |

Transfer result, 0 on success, other values on error.

## [◆ ](#a33e927f23d227a4974915c65927284ec)owner

| void\* udc\_buf\_info::owner |
| --- |

Transfer owner (usually pointer to a class instance).

## [◆ ](#a4cd2e83000a0551d126bebe89552eab9)queued

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::queued |
| --- |

Flag marks request buffer is queued (TBD).

## [◆ ](#a9664e1f7cddd36dbc7d206b52da45170)setup

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::setup |
| --- |

Flag marks setup transfer.

## [◆ ](#a84cf74496eddc4a69a47d23dcdbf753f)status

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::status |
| --- |

Flag marks status stage of setup transfer.

## [◆ ](#afc2d0c391aca7f68a1ae5539a1fed8a0)zlp

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int udc\_buf\_info::zlp |
| --- |

Flag marks ZLP at the end of a transfer.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[udc.h](udc_8h_source.md)

- [udc\_buf\_info](structudc__buf__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
