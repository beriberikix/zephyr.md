---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structfs__dirent.html
original_path: doxygen/html/structfs__dirent.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_dirent Struct Reference

[Operating System Services](group__os__services.md) » [File System APIs](group__file__system__api.md)

Structure to receive file or directory information.
[More...](#details)

`#include <[fs.h](fs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) | [type](#ac3dcca17b8b22401913e5b3215d4be11) |
|  | File/directory type (FS\_DIR\_ENTRY\_FILE or FS\_DIR\_ENTRY\_DIR). |
| char | [name](#af9c22b97ead96be25fb3edf0df98a769) [[MAX\_FILE\_NAME](fs__interface_8h.md#af43dedece15d018ffad8970492870bac)+1] |
|  | Name of file or directory. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#ac94ea69af234587aae3cea5cbd98d533) |
|  | Size of file (0 if directory). |

## Detailed Description

Structure to receive file or directory information.

Used in functions that read the directory entries to get file or directory information.

## Field Documentation

## [◆ ](#af9c22b97ead96be25fb3edf0df98a769)name

| char fs\_dirent::name[[MAX\_FILE\_NAME](fs__interface_8h.md#af43dedece15d018ffad8970492870bac)+1] |
| --- |

Name of file or directory.

## [◆ ](#ac94ea69af234587aae3cea5cbd98d533)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) fs\_dirent::size |
| --- |

Size of file (0 if directory).

## [◆ ](#ac3dcca17b8b22401913e5b3215d4be11)type

| enum [fs\_dir\_entry\_type](group__file__system__api.md#ga79f37397a1590284fae2c4b456f26afb) fs\_dirent::type |
| --- |

File/directory type (FS\_DIR\_ENTRY\_FILE or FS\_DIR\_ENTRY\_DIR).

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fs.h](fs_8h_source.md)

- [fs\_dirent](structfs__dirent.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
