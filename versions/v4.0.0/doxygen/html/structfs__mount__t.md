---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfs__mount__t.html
original_path: doxygen/html/structfs__mount__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mount\_t Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

File system mount info structure.
[More...](#details)

`#include <[fs.h](fs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) | [node](#aef11f6864a114ce5a0ebdf5c8f367c65) |
|  | Entry for the fs\_mount\_list list. |
| int | [type](#a6cd46d4e3106c7d8cfbab00fef54580f) |
|  | File system type. |
| const char \* | [mnt\_point](#a30e9d3bcfb3b08b051dbbdbd52ae0fdf) |
|  | Mount point directory name (ex: "/fatfs"). |
| void \* | [fs\_data](#a5c2e3e4fa34e5396b6e37fa0b09d5554) |
|  | Pointer to file system specific data. |
| void \* | [storage\_dev](#a3e4c227d5a3c837f21bedff1ada91261) |
|  | Pointer to backend storage device. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [mountp\_len](#a9b9bdef7b6a7185167ba51bc7a9848b6) |
|  | Length of Mount point string. |
| const struct [fs\_file\_system\_t](structfs__file__system__t.md) \* | [fs](#a2c70ac7f92ef5ae7d387a8db38a49983) |
|  | Pointer to File system interface of the mount point. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#ac5bd11869b64cfe1794b446d388c7116) |
|  | Mount flags. |

## Detailed Description

File system mount info structure.

## Field Documentation

## [◆ ](#ac5bd11869b64cfe1794b446d388c7116)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fs\_mount\_t::flags |
| --- |

Mount flags.

## [◆ ](#a2c70ac7f92ef5ae7d387a8db38a49983)fs

| const struct [fs\_file\_system\_t](structfs__file__system__t.md)\* fs\_mount\_t::fs |
| --- |

Pointer to File system interface of the mount point.

## [◆ ](#a5c2e3e4fa34e5396b6e37fa0b09d5554)fs\_data

| void\* fs\_mount\_t::fs\_data |
| --- |

Pointer to file system specific data.

## [◆ ](#a30e9d3bcfb3b08b051dbbdbd52ae0fdf)mnt\_point

| const char\* fs\_mount\_t::mnt\_point |
| --- |

Mount point directory name (ex: "/fatfs").

## [◆ ](#a9b9bdef7b6a7185167ba51bc7a9848b6)mountp\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fs\_mount\_t::mountp\_len |
| --- |

Length of Mount point string.

## [◆ ](#aef11f6864a114ce5a0ebdf5c8f367c65)node

| [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) fs\_mount\_t::node |
| --- |

Entry for the fs\_mount\_list list.

## [◆ ](#a3e4c227d5a3c837f21bedff1ada91261)storage\_dev

| void\* fs\_mount\_t::storage\_dev |
| --- |

Pointer to backend storage device.

## [◆ ](#a6cd46d4e3106c7d8cfbab00fef54580f)type

| int fs\_mount\_t::type |
| --- |

File system type.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs.h](fs_8h_source.md)

- [fs\_mount\_t](structfs__mount__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
