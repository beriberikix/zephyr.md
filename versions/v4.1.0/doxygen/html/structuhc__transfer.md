---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structuhc__transfer.html
original_path: doxygen/html/structuhc__transfer.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc\_transfer Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB host controller driver API](group__uhc__api.md)

UHC endpoint buffer info.
[More...](#details)

`#include <[uhc.h](uhc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#ae1fcb0b866e3d7c5b5ea9dff6221f37d) |
|  | dlist node |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [setup\_pkt](#af5e8080b91078a1c9f8ff269c72d70e9) [8] |
|  | Control transfer setup packet. |
| struct [net\_buf](structnet__buf.md) \* | [buf](#a170385b08171659f05ac7112faf8e587) |
|  | Transfer data buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ep](#aaf664844dc9f1871cce3d38516c042ef) |
|  | Endpoint to which request is associated. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mps](#a61a6c74cc7c026404ccf42d1164765b8) |
|  | Maximum packet size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#af6d6de482f092e4f85679722ad609cbf) |
|  | Interval, used for periodic transfers only. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [start\_frame](#a23e4115c774134ccd143189b0f4f2460) |
|  | Start frame, used for periodic transfers only. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [queued](#ad2b246c850c3b30f7d2b58fc9a47008b): 1 |
|  | Flag marks request buffer is queued. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [stage](#a9983482be9724e281e56c978ce27d93f): 2 |
|  | Control stage status, up to the driver to use it or not. |
| struct [usb\_device](structusb__device.md) \* | [udev](#a81a8a80809420787f4c0ab232a24a514) |
|  | Pointer to USB device. |
| void \* | [cb](#ad4d80a3f20cdec7dd2237a98054dd287) |
|  | Pointer to transfer completion callback (opaque for the UHC). |
| void \* | [priv](#a0f2d4a735ce224260d100dc756b1900f) |
|  | Pointer to completion callback private data. |
| int | [err](#a11f002f91b1039c226b7c9feb8223e11) |
|  | Transfer result, 0 on success, other values on error. |

## Detailed Description

UHC endpoint buffer info.

This structure is mandatory for all UHC request. It contains the meta data about the request and FIFOs to store [net\_buf](structnet__buf.md "Network buffer representation.") structures for each request.

The members of this structure should not be used directly by a higher layer (host stack).

## Field Documentation

## [◆ ](#a170385b08171659f05ac7112faf8e587)buf

| struct [net\_buf](structnet__buf.md)\* uhc\_transfer::buf |
| --- |

Transfer data buffer.

## [◆ ](#ad4d80a3f20cdec7dd2237a98054dd287)cb

| void\* uhc\_transfer::cb |
| --- |

Pointer to transfer completion callback (opaque for the UHC).

## [◆ ](#aaf664844dc9f1871cce3d38516c042ef)ep

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uhc\_transfer::ep |
| --- |

Endpoint to which request is associated.

## [◆ ](#a11f002f91b1039c226b7c9feb8223e11)err

| int uhc\_transfer::err |
| --- |

Transfer result, 0 on success, other values on error.

## [◆ ](#af6d6de482f092e4f85679722ad609cbf)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) uhc\_transfer::interval |
| --- |

Interval, used for periodic transfers only.

## [◆ ](#a61a6c74cc7c026404ccf42d1164765b8)mps

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) uhc\_transfer::mps |
| --- |

Maximum packet size.

## [◆ ](#ae1fcb0b866e3d7c5b5ea9dff6221f37d)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) uhc\_transfer::node |
| --- |

dlist node

## [◆ ](#a0f2d4a735ce224260d100dc756b1900f)priv

| void\* uhc\_transfer::priv |
| --- |

Pointer to completion callback private data.

## [◆ ](#ad2b246c850c3b30f7d2b58fc9a47008b)queued

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int uhc\_transfer::queued |
| --- |

Flag marks request buffer is queued.

## [◆ ](#af5e8080b91078a1c9f8ff269c72d70e9)setup\_pkt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uhc\_transfer::setup\_pkt[8] |
| --- |

Control transfer setup packet.

## [◆ ](#a9983482be9724e281e56c978ce27d93f)stage

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int uhc\_transfer::stage |
| --- |

Control stage status, up to the driver to use it or not.

## [◆ ](#a23e4115c774134ccd143189b0f4f2460)start\_frame

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) uhc\_transfer::start\_frame |
| --- |

Start frame, used for periodic transfers only.

## [◆ ](#a81a8a80809420787f4c0ab232a24a514)udev

| struct [usb\_device](structusb__device.md)\* uhc\_transfer::udev |
| --- |

Pointer to USB device.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb/[uhc.h](uhc_8h_source.md)

- [uhc\_transfer](structuhc__transfer.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
