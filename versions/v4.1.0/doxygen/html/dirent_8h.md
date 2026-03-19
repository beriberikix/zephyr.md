---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dirent_8h.html
original_path: doxygen/html/dirent_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dirent.h File Reference

`#include <[zephyr/posix/sys/dirent.h](sys_2dirent_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](dirent_8h_source.md)

| Functions | |
| --- | --- |
| int | [closedir](#aaeac2b41e8c2c3a5f91c9bd511a8c0a6) ([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp) |
| [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* | [fdopendir](#a58be90fffc0b5713ea34e39eb26d59f3) (int fd) |
| [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* | [opendir](#ae27c7f260a652b74c43296993d14ef0b) (const char \*dirname) |
| struct [dirent](structdirent.md) \* | [readdir](#a824e3b8c5995631b373ddb65cb674318) ([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp) |
| void | [rewinddir](#ad4fcb58b9194b1a3c1699654de963719) ([DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \*dirp) |

## Function Documentation

## [◆ ](#aaeac2b41e8c2c3a5f91c9bd511a8c0a6)closedir()

| int closedir | ( | [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* | *dirp* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a58be90fffc0b5713ea34e39eb26d59f3)fdopendir()

| [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* fdopendir | ( | int | *fd* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae27c7f260a652b74c43296993d14ef0b)opendir()

| [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* opendir | ( | const char \* | *dirname* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a824e3b8c5995631b373ddb65cb674318)readdir()

| struct [dirent](structdirent.md) \* readdir | ( | [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* | *dirp* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad4fcb58b9194b1a3c1699654de963719)rewinddir()

| void rewinddir | ( | [DIR](sys_2dirent_8h.md#a6808d95339147c6e29523463181854cc) \* | *dirp* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [dirent.h](dirent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
