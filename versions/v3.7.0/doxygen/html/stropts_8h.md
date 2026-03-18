---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stropts_8h.html
original_path: doxygen/html/stropts_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stropts.h File Reference

[Go to the source code of this file.](stropts_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [strbuf](structstrbuf.md) |

| Macros | |
| --- | --- |
| #define | [RS\_HIPRI](#ab12b3c3c77f22b0999f6b2cec1812da9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |

| Functions | |
| --- | --- |
| int | [putmsg](#a2e8c9b125d5b2b9e9c0f119bb8489c5e) (int fildes, const struct [strbuf](structstrbuf.md) \*ctlptr, const struct [strbuf](structstrbuf.md) \*dataptr, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| int | [fdetach](#ace3f43f93319016fce6e1ce8bb135ee2) (const char \*path) |
| int | [fattach](#aad1d52cad379cd124cbed912aa636ad1) (int fildes, const char \*path) |
| int | [getmsg](#a49857bef3fb1cecd099e67c8df35c8ef) (int fildes, struct [strbuf](structstrbuf.md) \*ctlptr, struct [strbuf](structstrbuf.md) \*dataptr, int \*flagsp) |
| int | [getpmsg](#a55b37250892d8a0821df369a5f744099) (int fildes, struct [strbuf](structstrbuf.md) \*ctlptr, struct [strbuf](structstrbuf.md) \*dataptr, int \*bandp, int \*flagsp) |
| int | [isastream](#add5237bf6844593ab11f8daa15d16070) (int fildes) |

## Macro Definition Documentation

## [◆ ](#ab12b3c3c77f22b0999f6b2cec1812da9)RS\_HIPRI

| #define RS\_HIPRI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## Function Documentation

## [◆ ](#aad1d52cad379cd124cbed912aa636ad1)fattach()

| int fattach | ( | int | *fildes*, |
| --- | --- | --- | --- |
|  |  | const char \* | *path* ) |

## [◆ ](#ace3f43f93319016fce6e1ce8bb135ee2)fdetach()

| int fdetach | ( | const char \* | *path* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a49857bef3fb1cecd099e67c8df35c8ef)getmsg()

| int getmsg | ( | int | *fildes*, |
| --- | --- | --- | --- |
|  |  | struct [strbuf](structstrbuf.md) \* | *ctlptr*, |
|  |  | struct [strbuf](structstrbuf.md) \* | *dataptr*, |
|  |  | int \* | *flagsp* ) |

## [◆ ](#a55b37250892d8a0821df369a5f744099)getpmsg()

| int getpmsg | ( | int | *fildes*, |
| --- | --- | --- | --- |
|  |  | struct [strbuf](structstrbuf.md) \* | *ctlptr*, |
|  |  | struct [strbuf](structstrbuf.md) \* | *dataptr*, |
|  |  | int \* | *bandp*, |
|  |  | int \* | *flagsp* ) |

## [◆ ](#add5237bf6844593ab11f8daa15d16070)isastream()

| int isastream | ( | int | *fildes* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a2e8c9b125d5b2b9e9c0f119bb8489c5e)putmsg()

| int putmsg | ( | int | *fildes*, |
| --- | --- | --- | --- |
|  |  | const struct [strbuf](structstrbuf.md) \* | *ctlptr*, |
|  |  | const struct [strbuf](structstrbuf.md) \* | *dataptr*, |
|  |  | int | *flags* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [stropts.h](stropts_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
