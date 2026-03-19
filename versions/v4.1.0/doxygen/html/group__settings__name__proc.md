---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__settings__name__proc.html
original_path: doxygen/html/group__settings__name__proc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Settings name processing

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md)

API for const name processing.
[More...](#details)

| Functions | |
| --- | --- |
| int | [settings\_name\_steq](#ga6d9d36d54a1bfd59bf7729621653edd9) (const char \*name, const char \*key, const char \*\*next) |
|  | Compares the start of name with a key. |
| int | [settings\_name\_next](#gacf259320845ae83c46df634f93c6d3e5) (const char \*name, const char \*\*next) |
|  | determine the number of characters before the first separator |

## Detailed Description

API for const name processing.

## Function Documentation

## [◆ ](#gacf259320845ae83c46df634f93c6d3e5)settings\_name\_next()

| int settings\_name\_next | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const char \*\* | *next* ) |

`#include <[settings.h](settings_8h.md)>`

determine the number of characters before the first separator

Parameters
:   | [in] | name | in string format |
    | --- | --- | --- |
    | [out] | next | pointer to remaining of name (excluding separator) |

Returns
:   index of the first separator, in case no separator was found this is the size of name

## [◆ ](#ga6d9d36d54a1bfd59bf7729621653edd9)settings\_name\_steq()

| int settings\_name\_steq | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const char \* | *key*, |
|  |  | const char \*\* | *next* ) |

`#include <[settings.h](settings_8h.md)>`

Compares the start of name with a key.

Parameters
:   | [in] | name | in string format |
    | --- | --- | --- |
    | [in] | key | comparison string |
    | [out] | next | pointer to remaining of name, when the remaining part starts with a separator the separator is removed from next |

Some examples: settings\_name\_steq("bt/btmesh/iv", "b", &next) returns 1, next="t/btmesh/iv" settings\_name\_steq("bt/btmesh/iv", "bt", &next) returns 1, next="btmesh/iv" settings\_name\_steq("bt/btmesh/iv", "bt/", &next) returns 0, next=NULL settings\_name\_steq("bt/btmesh/iv", "bta", &next) returns 0, next=NULL

REMARK: This routine could be simplified if the [settings\_handler](structsettings__handler.md "Config handlers for subtree implement a set of handler functions.") names would include a separator at the end.

Returns
:   0: no match 1: match, next can be used to check if match is full

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
