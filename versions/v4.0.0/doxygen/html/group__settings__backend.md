---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__settings__backend.html
original_path: doxygen/html/group__settings__backend.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Settings backend interface

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md)

settings
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [settings\_store](structsettings__store.md) |
|  | Backend handler node for storage handling. [More...](structsettings__store.md#details) |
| struct | [settings\_load\_arg](structsettings__load__arg.md) |
|  | Arguments for data loading. [More...](structsettings__load__arg.md#details) |
| struct | [settings\_store\_itf](structsettings__store__itf.md) |
|  | Backend handler functions. [More...](structsettings__store__itf.md#details) |

| Functions | |
| --- | --- |
| void | [settings\_src\_register](#gad16bb70588cf69873f8872d7bf90e1c6) (struct [settings\_store](structsettings__store.md) \*cs) |
|  | Register a backend handler acting as source. |
| void | [settings\_dst\_register](#ga37bcada0be44b023cd3759e519e69d01) (struct [settings\_store](structsettings__store.md) \*cs) |
|  | Register a backend handler acting as destination. |
| struct [settings\_handler\_static](structsettings__handler__static.md) \* | [settings\_parse\_and\_lookup](#gab03a10ed0b65809369b4b6f220aa3df6) (const char \*name, const char \*\*next) |
|  | Parses a key to an array of elements and locate corresponding module handler. |
| int | [settings\_call\_set\_handler](#gaf94e311eba2b109cdbddd2767e502e77) (const char \*name, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*read\_cb\_arg, const struct [settings\_load\_arg](structsettings__load__arg.md) \*load\_arg) |
|  | Calls settings handler. |

## Detailed Description

settings

## Function Documentation

## [◆ ](#gaf94e311eba2b109cdbddd2767e502e77)settings\_call\_set\_handler()

| int settings\_call\_set\_handler | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) | *read\_cb*, |
|  |  | void \* | *read\_cb\_arg*, |
|  |  | const struct [settings\_load\_arg](structsettings__load__arg.md) \* | *load\_arg* ) |

`#include <[settings.h](settings_8h.md)>`

Calls settings handler.

Parameters
:   | [in] | name | The name of the data found in the backend. |
    | --- | --- | --- |
    | [in] | len | The size of the data found in the backend. |
    | [in] | read\_cb | Function provided to read the data from the backend. |
    | [in,out] | read\_cb\_arg | Arguments for the read function provided by the backend. |
    | [in,out] | load\_arg | Arguments for data loading. |

Returns
:   0 or negative error code

## [◆ ](#ga37bcada0be44b023cd3759e519e69d01)settings\_dst\_register()

| void settings\_dst\_register | ( | struct [settings\_store](structsettings__store.md) \* | *cs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Register a backend handler acting as destination.

Parameters
:   | cs | Backend handler node containing handler information. |
    | --- | --- |

## [◆ ](#gab03a10ed0b65809369b4b6f220aa3df6)settings\_parse\_and\_lookup()

| struct [settings\_handler\_static](structsettings__handler__static.md) \* settings\_parse\_and\_lookup | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const char \*\* | *next* ) |

`#include <[settings.h](settings_8h.md)>`

Parses a key to an array of elements and locate corresponding module handler.

Parameters
:   | [in] | name | in string format |
    | --- | --- | --- |
    | [out] | next | remaining of name after matched handler |

Returns
:   [settings\_handler\_static](structsettings__handler__static.md "Config handlers without the node element, used for static handlers.") on success, NULL on failure.

## [◆ ](#gad16bb70588cf69873f8872d7bf90e1c6)settings\_src\_register()

| void settings\_src\_register | ( | struct [settings\_store](structsettings__store.md) \* | *cs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Register a backend handler acting as source.

Parameters
:   | cs | Backend handler node containing handler information. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
