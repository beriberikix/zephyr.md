---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsettings__store.html
original_path: doxygen/html/structsettings__store.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_store Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md) » [Settings backend interface](group__settings__backend.md)

Backend handler node for storage handling.
[More...](#details)

`#include <[settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [cs\_next](#a9f382f4e61737585228a6a3b86e9a38c) |
|  | Linked list node info for internal usage. |
| const struct [settings\_store\_itf](structsettings__store__itf.md) \* | [cs\_itf](#aaa0f629059f0c49b0f92f278791ce19c) |
|  | Backend handler structure. |

## Detailed Description

Backend handler node for storage handling.

## Field Documentation

## [◆ ](#aaa0f629059f0c49b0f92f278791ce19c)cs\_itf

| const struct [settings\_store\_itf](structsettings__store__itf.md)\* settings\_store::cs\_itf |
| --- |

Backend handler structure.

## [◆ ](#a9f382f4e61737585228a6a3b86e9a38c)cs\_next

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) settings\_store::cs\_next |
| --- |

Linked list node info for internal usage.

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_store](structsettings__store.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
