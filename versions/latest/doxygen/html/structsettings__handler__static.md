---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsettings__handler__static.html
original_path: doxygen/html/structsettings__handler__static.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_handler\_static Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md)

Config handlers without the node element, used for static handlers.
[More...](#details)

`#include <[settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#aa8e57471bd89f4792cfb0689462b6f9b) |
|  | Name of subtree. |
| int(\* | [h\_get](#acc65e884503cf7db1276e7777f57fb12) )(const char \*key, char \*val, int val\_len\_max) |
|  | Get values handler of settings items identified by keyword names. |
| int(\* | [h\_set](#a2cf94a6dad3ec35ca58b5ef869c7edae) )(const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
|  | Set value handler of settings items identified by keyword names. |
| int(\* | [h\_commit](#a093ab8346aedd0a9cb06dfaa4387f393) )(void) |
|  | This handler gets called after settings has been loaded in full. |
| int(\* | [h\_export](#abb1df3f0f05fb2a57cd08e380bfffa09) )(int(\*export\_func)(const char \*[name](#aa8e57471bd89f4792cfb0689462b6f9b), const void \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len)) |
|  | This gets called to dump all current settings items. |

## Detailed Description

Config handlers without the node element, used for static handlers.

These are registered using a call to [SETTINGS\_STATIC\_HANDLER\_DEFINE()](group__settings.md#ga2098bcfc32c6daa13292d937712e476e "Define a static handler for settings items.").

## Field Documentation

## [◆ ](#a093ab8346aedd0a9cb06dfaa4387f393)h\_commit

| int(\* settings\_handler\_static::h\_commit) (void) |
| --- |

This handler gets called after settings has been loaded in full.

User might use it to apply setting to the application.

## [◆ ](#abb1df3f0f05fb2a57cd08e380bfffa09)h\_export

| int(\* settings\_handler\_static::h\_export) (int(\*export\_func)(const char \*[name](#aa8e57471bd89f4792cfb0689462b6f9b), const void \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len)) |
| --- |

This gets called to dump all current settings items.

This happens when [settings\_save](group__settings.md#ga789410aa059398d6c8a7851ea6945b55 "settings_save") tries to save the settings. Parameters:

- export\_func: the pointer to the internal function which appends a single key-value pair to persisted settings. Don't store duplicated value. The name is subtree/key string, val is the string with value.

Remarks
:   The User might limit a implementations of handler to serving only one keyword at one call - what will impose limit to get/set values using full subtree/key name.

Return: 0 on success, non-zero on failure.

## [◆ ](#acc65e884503cf7db1276e7777f57fb12)h\_get

| int(\* settings\_handler\_static::h\_get) (const char \*key, char \*val, int val\_len\_max) |
| --- |

Get values handler of settings items identified by keyword names.

Parameters:

- key[in] the name with skipped part that was used as name in handler registration
- val[out] buffer to receive value.
- val\_len\_max[in] size of that buffer.

Return: length of data read on success, negative on failure.

## [◆ ](#a2cf94a6dad3ec35ca58b5ef869c7edae)h\_set

| int(\* settings\_handler\_static::h\_set) (const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
| --- |

Set value handler of settings items identified by keyword names.

Parameters:

- key[in] the name with skipped part that was used as name in handler registration
- len[in] the size of the data found in the backend.
- read\_cb[in] function provided to read the data from the backend.
- cb\_arg[in] arguments for the read function provided by the backend.

Return: 0 on success, non-zero on failure.

## [◆ ](#aa8e57471bd89f4792cfb0689462b6f9b)name

| const char\* settings\_handler\_static::name |
| --- |

Name of subtree.

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_handler\_static](structsettings__handler__static.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
