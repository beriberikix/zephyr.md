---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfs__file__t.html
original_path: doxygen/html/structfs__file__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_file\_t Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

File object representing an open file.
[More...](#details)

`#include <[fs_interface.h](fs__interface_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [filep](#aa63d13a3c2923f1adecb55ab7e6d1bfa) |
|  | Pointer to file object structure. |
| const struct [fs\_mount\_t](structfs__mount__t.md) \* | [mp](#af027d2f6b262d26d9d45551e4b9044e2) |
|  | Pointer to mount point structure. |
| [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) | [flags](#a9a4fbedc9df828f7ec8eb3b9734a054e) |
|  | Open/create flags. |

## Detailed Description

File object representing an open file.

The object needs to be initialized with [fs\_file\_t\_init()](group__file__system__api.md#gad44be87cbda3ddc48021ed16d515f564 "Initialize fs_file_t object.").

## Field Documentation

## [◆ ](#aa63d13a3c2923f1adecb55ab7e6d1bfa)filep

| void\* fs\_file\_t::filep |
| --- |

Pointer to file object structure.

## [◆ ](#a9a4fbedc9df828f7ec8eb3b9734a054e)flags

| [fs\_mode\_t](fs__interface_8h.md#a7090a1b41e73d393b8be3e18ab411027) fs\_file\_t::flags |
| --- |

Open/create flags.

## [◆ ](#af027d2f6b262d26d9d45551e4b9044e2)mp

| const struct [fs\_mount\_t](structfs__mount__t.md)\* fs\_file\_t::mp |
| --- |

Pointer to mount point structure.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs\_interface.h](fs__interface_8h_source.md)

- [fs\_file\_t](structfs__file__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
