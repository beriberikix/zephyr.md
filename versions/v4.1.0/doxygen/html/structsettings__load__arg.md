---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsettings__load__arg.html
original_path: doxygen/html/structsettings__load__arg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_load\_arg Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md) » [Settings backend interface](group__settings__backend.md)

Arguments for data loading.
[More...](#details)

`#include <[settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [subtree](#a0764239993147761b12e8999f860d267) |
|  | Name of the subtree to be loaded. |
| [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535) | [cb](#aec32e51b4a6b61aff2ea415aa80a9987) |
|  | Pointer to the callback function. |
| void \* | [param](#a7cbe713a1e0d2885528644b5a54f27d3) |
|  | Parameter for callback function. |

## Detailed Description

Arguments for data loading.

Holds all parameters that changes the way data should be loaded from backend.

## Field Documentation

## [◆ ](#aec32e51b4a6b61aff2ea415aa80a9987)cb

| [settings\_load\_direct\_cb](group__settings.md#ga767bf6c2709b1c58afcf4d1c5ef0d535) settings\_load\_arg::cb |
| --- |

Pointer to the callback function.

If NULL then matching registered function would be used.

## [◆ ](#a7cbe713a1e0d2885528644b5a54f27d3)param

| void\* settings\_load\_arg::param |
| --- |

Parameter for callback function.

Parameter to be passed to the callback function.

## [◆ ](#a0764239993147761b12e8999f860d267)subtree

| const char\* settings\_load\_arg::subtree |
| --- |

Name of the subtree to be loaded.

If NULL, all values would be loaded.

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_load\_arg](structsettings__load__arg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
