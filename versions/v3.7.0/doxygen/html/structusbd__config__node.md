---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structusbd__config__node.html
original_path: doxygen/html/structusbd__config__node.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_config\_node Struct Reference

[Connectivity](group__connectivity.md) » [USB](group__usb.md) » [USB device core API](group__usbd__api.md)

Device configuration node.
[More...](#details)

`#include <[usbd.h](usbd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a003a8d9132b319f54583263c4da1e060) |
|  | slist node struct |
| void \* | [desc](#a55081d79ab3e6b41a091b3f65d7d2d87) |
|  | Pointer to configuration descriptor. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [class\_list](#a00493162af2344d3d39f834b4834ef78) |
|  | List of registered classes (functions). |

## Detailed Description

Device configuration node.

Configuration node is used to manage device configurations, at least one configuration is required. It does not have an index, instead bConfigurationValue of the descriptor is used for identification.

## Field Documentation

## [◆ ](#a00493162af2344d3d39f834b4834ef78)class\_list

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) usbd\_config\_node::class\_list |
| --- |

List of registered classes (functions).

## [◆ ](#a55081d79ab3e6b41a091b3f65d7d2d87)desc

| void\* usbd\_config\_node::desc |
| --- |

Pointer to configuration descriptor.

## [◆ ](#a003a8d9132b319f54583263c4da1e060)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) usbd\_config\_node::node |
| --- |

slist node struct

---

The documentation for this struct was generated from the following file:

- zephyr/usb/[usbd.h](usbd_8h_source.md)

- [usbd\_config\_node](structusbd__config__node.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
