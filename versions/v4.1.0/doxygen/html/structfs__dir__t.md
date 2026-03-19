---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfs__dir__t.html
original_path: doxygen/html/structfs__dir__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_dir\_t Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

Directory object representing an open directory.
[More...](#details)

`#include <[fs_interface.h](fs__interface_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [dirp](#afdd8e0b7b0c528a420c050718213d1ff) |
|  | Pointer to directory object structure. |
| const struct [fs\_mount\_t](structfs__mount__t.md) \* | [mp](#a6d8e0c603a33ed4870fcd7b82e1bc0a4) |
|  | Pointer to mount point structure. |

## Detailed Description

Directory object representing an open directory.

The object needs to be initialized with [fs\_dir\_t\_init()](group__file__system__api.md#gacd31440cd0b10308e55a0484828ea2f3 "Initialize fs_dir_t object.").

## Field Documentation

## [◆ ](#afdd8e0b7b0c528a420c050718213d1ff)dirp

| void\* fs\_dir\_t::dirp |
| --- |

Pointer to directory object structure.

## [◆ ](#a6d8e0c603a33ed4870fcd7b82e1bc0a4)mp

| const struct [fs\_mount\_t](structfs__mount__t.md)\* fs\_dir\_t::mp |
| --- |

Pointer to mount point structure.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs\_interface.h](fs__interface_8h_source.md)

- [fs\_dir\_t](structfs__dir__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
