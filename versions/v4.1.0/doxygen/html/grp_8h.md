---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/grp_8h.html
original_path: doxygen/html/grp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grp.h File Reference

`#include <[zephyr/posix/sys/stat.h](stat_8h_source.md)>`

[Go to the source code of this file.](grp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [group](structgroup.md) |
|  | Group structure. [More...](structgroup.md#details) |

| Functions | |
| --- | --- |
| int | [getgrnam\_r](#acf054c85917adbbc3687004d51317685) (const char \*name, struct [group](structgroup.md) \*grp, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bufsize, struct [group](structgroup.md) \*\*result) |
| int | [getgrgid\_r](#a64e84dfb3f386daaa7530fc8177a6056) ([gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) gid, struct [group](structgroup.md) \*grp, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bufsize, struct [group](structgroup.md) \*\*result) |

## Function Documentation

## [◆ ](#a64e84dfb3f386daaa7530fc8177a6056)getgrgid\_r()

| int getgrgid\_r | ( | [gid\_t](posix__types_8h.md#a3a7834be1a79bb0c5a65d3546c2e3bd8) | *gid*, |
| --- | --- | --- | --- |
|  |  | struct [group](structgroup.md) \* | *grp*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bufsize*, |
|  |  | struct [group](structgroup.md) \*\* | *result* ) |

## [◆ ](#acf054c85917adbbc3687004d51317685)getgrnam\_r()

| int getgrnam\_r | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | struct [group](structgroup.md) \* | *grp*, |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bufsize*, |
|  |  | struct [group](structgroup.md) \*\* | *result* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [grp.h](grp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
