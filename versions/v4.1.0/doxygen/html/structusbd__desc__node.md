---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structusbd__desc__node.html
original_path: doxygen/html/structusbd__desc__node.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| union { |  |
| struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md)   [str](#ae34fee200f7fd78355addafe79789cb4) |  |
| struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md)   [bos](#afd65079b8b969fa4101a3f9f662c7b6b) |  |
| }; |  |
| const void \*const | [ptr](#ac437b472e012e8fdec049f28e9f88944) |
|  | Opaque pointer to a descriptor payload. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bLength](#ad71ef74fd7fe43a8117704553a3be01c) |
|  | Descriptor size in bytes. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bDescriptorType](#a786e2911b5ec7d6c908c148be4d27f5f) |
|  | Descriptor type. |

## Detailed Description

Descriptor node.

Descriptor node is used to manage descriptors that are not directly part of a structure, such as string or BOS capability descriptors.

## Field Documentation

## [◆ ](#a080f8481b8a0b5278e132b85667686de)[union]

| union { ... } [usbd\_desc\_node](structusbd__desc__node.md) |
| --- |

## [◆ ](#a786e2911b5ec7d6c908c148be4d27f5f)bDescriptorType

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_desc\_node::bDescriptorType |
| --- |

Descriptor type.

## [◆ ](#ad71ef74fd7fe43a8117704553a3be01c)bLength

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_desc\_node::bLength |
| --- |

Descriptor size in bytes.

## [◆ ](#afd65079b8b969fa4101a3f9f662c7b6b)bos

| struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) usbd\_desc\_node::bos |
| --- |

## [◆ ](#a9f1941cd036c01387d8ad9a4aceb595a)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) usbd\_desc\_node::node |
| --- |

slist node struct

## [◆ ](#ac437b472e012e8fdec049f28e9f88944)ptr

| const void\* const usbd\_desc\_node::ptr |
| --- |

Opaque pointer to a descriptor payload.

## [◆ ](#ae34fee200f7fd78355addafe79789cb4)str

| struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md) usbd\_desc\_node::str |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_desc\_node](structusbd__desc__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
