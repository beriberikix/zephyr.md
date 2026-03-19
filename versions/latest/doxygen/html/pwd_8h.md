---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pwd_8h.html
original_path: doxygen/html/pwd_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pwd.h File Reference

`#include <[zephyr/posix/sys/stat.h](stat_8h_source.md)>`

[Go to the source code of this file.](pwd_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [passwd](structpasswd.md) |

| Functions | |
| --- | --- |
| int | [getpwnam\_r](#a9848a1faaee1b74dbc399b2d746ef16c) (const char \*nam, struct [passwd](structpasswd.md) \*pwd, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bufsize, struct [passwd](structpasswd.md) \*\*result) |
| int | [getpwuid\_r](#a171c52c8fac39d01f77ed0d69efbaa61) ([uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) uid, struct [passwd](structpasswd.md) \*pwd, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bufsize, struct [passwd](structpasswd.md) \*\*result) |

## Function Documentation

## [◆ ](#a9848a1faaee1b74dbc399b2d746ef16c)getpwnam\_r()

| int getpwnam\_r | ( | const char \* | *nam*, |
| --- | --- | --- | --- |
|  |  | struct [passwd](structpasswd.md) \* | *pwd*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bufsize*, |
|  |  | struct [passwd](structpasswd.md) \*\* | *result* ) |

## [◆ ](#a171c52c8fac39d01f77ed0d69efbaa61)getpwuid\_r()

| int getpwuid\_r | ( | [uid\_t](posix__types_8h.md#a75bb141dc55bc89a8ddc565fd374e3d9) | *uid*, |
| --- | --- | --- | --- |
|  |  | struct [passwd](structpasswd.md) \* | *pwd*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bufsize*, |
|  |  | struct [passwd](structpasswd.md) \*\* | *result* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [pwd.h](pwd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
