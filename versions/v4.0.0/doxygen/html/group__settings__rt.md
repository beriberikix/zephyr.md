---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__settings__rt.html
original_path: doxygen/html/group__settings__rt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Settings subsystem runtime

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md)

API for runtime settings.
[More...](#details)

| Functions | |
| --- | --- |
| int | [settings\_runtime\_set](#gae1b95c47c49774d53b4745af810e881e) (const char \*name, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Set a value with a specific key to a module handler. |
| int | [settings\_runtime\_get](#ga99a4714ba8c184afc659c43ec2020844) (const char \*name, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Get a value corresponding to a key from a module handler. |
| int | [settings\_runtime\_commit](#gafa96974170dced7a131bfd5f022483f8) (const char \*name) |
|  | Apply settings in a module handler. |

## Detailed Description

API for runtime settings.

## Function Documentation

## [◆ ](#gafa96974170dced7a131bfd5f022483f8)settings\_runtime\_commit()

| int settings\_runtime\_commit | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[settings.h](settings_8h.md)>`

Apply settings in a module handler.

Parameters
:   | name | Key in string format. |
    | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga99a4714ba8c184afc659c43ec2020844)settings\_runtime\_get()

| int settings\_runtime\_get | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[settings.h](settings_8h.md)>`

Get a value corresponding to a key from a module handler.

Parameters
:   | name | Key in string format. |
    | --- | --- |
    | data | Returned binary value. |
    | len | requested value length in bytes. |

Returns
:   length of data read on success, negative on failure.

## [◆ ](#gae1b95c47c49774d53b4745af810e881e)settings\_runtime\_set()

| int settings\_runtime\_set | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[settings.h](settings_8h.md)>`

Set a value with a specific key to a module handler.

Parameters
:   | name | Key in string format. |
    | --- | --- |
    | data | Binary value. |
    | len | Value length in bytes. |

Returns
:   0 on success, non-zero on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
