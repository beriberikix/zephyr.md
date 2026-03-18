---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structsettings__handler.html
original_path: doxygen/html/structsettings__handler.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

settings\_handler Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Settings](group__settings.md)

Config handlers for subtree implement a set of handler functions.
[More...](#details)

`#include <[settings.h](settings_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ab8eee945dc866ec90b272fb526abc646) |
|  | Name of subtree. |
| int(\* | [h\_get](#a8d4036babe22872777610e54c4dadf21) )(const char \*key, char \*val, int val\_len\_max) |
|  | Get values handler of settings items identified by keyword names. |
| int(\* | [h\_set](#a70aa25bf3b53898ab22906e9949963a4) )(const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
|  | Set value handler of settings items identified by keyword names. |
| int(\* | [h\_commit](#ad5e23a2acf29bbb2a5a4f249b5f80e0a) )(void) |
|  | This handler gets called after settings has been loaded in full. |
| int(\* | [h\_export](#a30207125407f57a0f117ecaee5a2054a) )(int(\*export\_func)(const char \*[name](#ab8eee945dc866ec90b272fb526abc646), const void \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len)) |
|  | This gets called to dump all current settings items. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a6aa2cc76c84341c3d29b679d2cc9c6ab) |
|  | Linked list node info for module internal usage. |

## Detailed Description

Config handlers for subtree implement a set of handler functions.

These are registered using a call to [settings\_register](group__settings.md#gab2043a6d799202e177cc3dfa0cbfa531 "settings_register").

## Field Documentation

## [◆ ](#ad5e23a2acf29bbb2a5a4f249b5f80e0a)h\_commit

| int(\* settings\_handler::h\_commit) (void) |
| --- |

This handler gets called after settings has been loaded in full.

User might use it to apply setting to the application.

Return: 0 on success, non-zero on failure.

## [◆ ](#a30207125407f57a0f117ecaee5a2054a)h\_export

| int(\* settings\_handler::h\_export) (int(\*export\_func)(const char \*[name](#ab8eee945dc866ec90b272fb526abc646), const void \*val, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) val\_len)) |
| --- |

This gets called to dump all current settings items.

This happens when [settings\_save](group__settings.md#ga789410aa059398d6c8a7851ea6945b55 "settings_save") tries to save the settings. Parameters:

- export\_func: the pointer to the internal function which appends a single key-value pair to persisted settings. Don't store duplicated value. The name is subtree/key string, val is the string with value.

Remarks
:   The User might limit a implementations of handler to serving only one keyword at one call - what will impose limit to get/set values using full subtree/key name.

Return: 0 on success, non-zero on failure.

## [◆ ](#a8d4036babe22872777610e54c4dadf21)h\_get

| int(\* settings\_handler::h\_get) (const char \*key, char \*val, int val\_len\_max) |
| --- |

Get values handler of settings items identified by keyword names.

Parameters:

- key[in] the name with skipped part that was used as name in handler registration
- val[out] buffer to receive value.
- val\_len\_max[in] size of that buffer.

Return: length of data read on success, negative on failure.

## [◆ ](#a70aa25bf3b53898ab22906e9949963a4)h\_set

| int(\* settings\_handler::h\_set) (const char \*key, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [settings\_read\_cb](group__settings.md#ga51cdac276c1fb8cd27fc3eec42749a04) read\_cb, void \*cb\_arg) |
| --- |

Set value handler of settings items identified by keyword names.

Parameters:

- key[in] the name with skipped part that was used as name in handler registration
- len[in] the size of the data found in the backend.
- read\_cb[in] function provided to read the data from the backend.
- cb\_arg[in] arguments for the read function provided by the backend.

Return: 0 on success, non-zero on failure.

## [◆ ](#ab8eee945dc866ec90b272fb526abc646)name

| const char\* settings\_handler::name |
| --- |

Name of subtree.

## [◆ ](#a6aa2cc76c84341c3d29b679d2cc9c6ab)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) settings\_handler::node |
| --- |

Linked list node info for module internal usage.

---

The documentation for this struct was generated from the following file:

- zephyr/settings/[settings.h](settings_8h_source.md)

- [settings\_handler](structsettings__handler.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
