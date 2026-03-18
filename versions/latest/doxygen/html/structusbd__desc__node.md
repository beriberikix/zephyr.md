---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbd__desc__node.html
original_path: doxygen/html/structusbd__desc__node.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_desc\_node Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

Descriptor node.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#a9f1941cd036c01387d8ad9a4aceb595a) |
|  | slist node struct |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [idx](#a0705a86aa6d7f532eb6be794f2c60d06): 8 |
|  | Descriptor index, required for string descriptors. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [utype](#a50e1b8db1dd6a4f3ca541394ad9d9adf): 8 |
|  | Descriptor usage type (not bDescriptorType). |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [utf16le](#a266d0936f7684f6a3047e2a6d1875458): 1 |
|  | If not set, string descriptor must be converted to UTF16LE. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [custom\_sn](#a322537e0b35d0590ba0f4e19ae5bb3ac): 1 |
|  | If not set, device stack obtains SN using the hwinfo API. |
| void \* | [desc](#a4d4692341a7785b5a0af762b1810e80f) |
|  | Pointer to a descriptor. |

## Detailed Description

Descriptor node.

Descriptor node is used to manage descriptors that are not directly part of a structure, such as string or bos descriptors.

## Field Documentation

## [◆ ](#a322537e0b35d0590ba0f4e19ae5bb3ac)custom\_sn

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_desc\_node::custom\_sn |
| --- |

If not set, device stack obtains SN using the hwinfo API.

## [◆ ](#a4d4692341a7785b5a0af762b1810e80f)desc

| void\* usbd\_desc\_node::desc |
| --- |

Pointer to a descriptor.

## [◆ ](#a0705a86aa6d7f532eb6be794f2c60d06)idx

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_desc\_node::idx |
| --- |

Descriptor index, required for string descriptors.

## [◆ ](#a9f1941cd036c01387d8ad9a4aceb595a)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) usbd\_desc\_node::node |
| --- |

slist node struct

## [◆ ](#a266d0936f7684f6a3047e2a6d1875458)utf16le

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_desc\_node::utf16le |
| --- |

If not set, string descriptor must be converted to UTF16LE.

## [◆ ](#a50e1b8db1dd6a4f3ca541394ad9d9adf)utype

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int usbd\_desc\_node::utype |
| --- |

Descriptor usage type (not bDescriptorType).

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_desc\_node](structusbd__desc__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
