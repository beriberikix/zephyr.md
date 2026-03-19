---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/fcntl_8h.html
original_path: doxygen/html/fcntl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcntl.h File Reference

`#include <[zephyr/sys/fdtable.h](fdtable_8h_source.md)>`

[Go to the source code of this file.](fcntl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [O\_APPEND](#ae036f789407d21f07b211552d67b3214)   [ZVFS\_O\_APPEND](fdtable_8h.md#afa29fb3c7ff76f1e6cf2d69947865163) |
| #define | [O\_CREAT](#a1cf6b1de1fffedaa1d26b189e9a8d2cc)   [ZVFS\_O\_CREAT](fdtable_8h.md#aff3387bcd512c9bea99c94aa3c459214) |
| #define | [O\_EXCL](#a9f5acfe79fafe14b6694447bd0e9f10b)   [ZVFS\_O\_EXCL](fdtable_8h.md#a2cb7a8f1c86ab67839458f0bc4198515) |
| #define | [O\_NONBLOCK](#a39d33ce33804efd4d52606d59071c6d8)   [ZVFS\_O\_NONBLOCK](fdtable_8h.md#a122add73257644aab0689853c57c53f3) |
| #define | [O\_TRUNC](#ad1d67e453fb3031f40f8cd3403773813)   [ZVFS\_O\_TRUNC](fdtable_8h.md#aecd7cfa3a9afdf22aac7b90911f4f459) |
| #define | [O\_ACCMODE](#a4dc4d45e07d2abc899bcaf04b2846a87)   ([ZVFS\_O\_RDONLY](fdtable_8h.md#a1aeb8126a4c817bdd2740a93f191de16) | [ZVFS\_O\_RDWR](fdtable_8h.md#a82be0ad3089fdd844137845fa50d6e21) | [ZVFS\_O\_WRONLY](fdtable_8h.md#abf07c70a006713aaed00a82ed87fb2be)) |
| #define | [O\_RDONLY](#a7a68c9ffaac7dbcd652225dd7c06a54b)   [ZVFS\_O\_RDONLY](fdtable_8h.md#a1aeb8126a4c817bdd2740a93f191de16) |
| #define | [O\_RDWR](#abb0586253488ee61072b73557eeb873b)   [ZVFS\_O\_RDWR](fdtable_8h.md#a82be0ad3089fdd844137845fa50d6e21) |
| #define | [O\_WRONLY](#a11b644a8526139c4cc1850dac1271ced)   [ZVFS\_O\_WRONLY](fdtable_8h.md#abf07c70a006713aaed00a82ed87fb2be) |
| #define | [F\_DUPFD](#ab93a8621587aba90181efd7d3aeea67e)   [ZVFS\_F\_DUPFD](fdtable_8h.md#ac72b82ab9384b25f52acb061f96779b2) |
| #define | [F\_GETFL](#a025fad21a889c79f02ec53abe3526c32)   [ZVFS\_F\_GETFL](fdtable_8h.md#a02737faaf00631600b940982d1c9d0e5) |
| #define | [F\_SETFL](#af2939853c650561d3495ed40f68f6249)   [ZVFS\_F\_SETFL](fdtable_8h.md#a9f090c1504183cc5a023908dea28940b) |

| Functions | |
| --- | --- |
| int | [open](#ac843f2e35e60c3bbf1da47d84306f29b) (const char \*name, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),...) |
| int | [fcntl](#acfc4bf677fc9f8be66d9624175cb3775) (int fildes, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),...) |

## Macro Definition Documentation

## [◆ ](#ab93a8621587aba90181efd7d3aeea67e)F\_DUPFD

| #define F\_DUPFD   [ZVFS\_F\_DUPFD](fdtable_8h.md#ac72b82ab9384b25f52acb061f96779b2) |
| --- |

## [◆ ](#a025fad21a889c79f02ec53abe3526c32)F\_GETFL

| #define F\_GETFL   [ZVFS\_F\_GETFL](fdtable_8h.md#a02737faaf00631600b940982d1c9d0e5) |
| --- |

## [◆ ](#af2939853c650561d3495ed40f68f6249)F\_SETFL

| #define F\_SETFL   [ZVFS\_F\_SETFL](fdtable_8h.md#a9f090c1504183cc5a023908dea28940b) |
| --- |

## [◆ ](#a4dc4d45e07d2abc899bcaf04b2846a87)O\_ACCMODE

| #define O\_ACCMODE   ([ZVFS\_O\_RDONLY](fdtable_8h.md#a1aeb8126a4c817bdd2740a93f191de16) | [ZVFS\_O\_RDWR](fdtable_8h.md#a82be0ad3089fdd844137845fa50d6e21) | [ZVFS\_O\_WRONLY](fdtable_8h.md#abf07c70a006713aaed00a82ed87fb2be)) |
| --- |

## [◆ ](#ae036f789407d21f07b211552d67b3214)O\_APPEND

| #define O\_APPEND   [ZVFS\_O\_APPEND](fdtable_8h.md#afa29fb3c7ff76f1e6cf2d69947865163) |
| --- |

## [◆ ](#a1cf6b1de1fffedaa1d26b189e9a8d2cc)O\_CREAT

| #define O\_CREAT   [ZVFS\_O\_CREAT](fdtable_8h.md#aff3387bcd512c9bea99c94aa3c459214) |
| --- |

## [◆ ](#a9f5acfe79fafe14b6694447bd0e9f10b)O\_EXCL

| #define O\_EXCL   [ZVFS\_O\_EXCL](fdtable_8h.md#a2cb7a8f1c86ab67839458f0bc4198515) |
| --- |

## [◆ ](#a39d33ce33804efd4d52606d59071c6d8)O\_NONBLOCK

| #define O\_NONBLOCK   [ZVFS\_O\_NONBLOCK](fdtable_8h.md#a122add73257644aab0689853c57c53f3) |
| --- |

## [◆ ](#a7a68c9ffaac7dbcd652225dd7c06a54b)O\_RDONLY

| #define O\_RDONLY   [ZVFS\_O\_RDONLY](fdtable_8h.md#a1aeb8126a4c817bdd2740a93f191de16) |
| --- |

## [◆ ](#abb0586253488ee61072b73557eeb873b)O\_RDWR

| #define O\_RDWR   [ZVFS\_O\_RDWR](fdtable_8h.md#a82be0ad3089fdd844137845fa50d6e21) |
| --- |

## [◆ ](#ad1d67e453fb3031f40f8cd3403773813)O\_TRUNC

| #define O\_TRUNC   [ZVFS\_O\_TRUNC](fdtable_8h.md#aecd7cfa3a9afdf22aac7b90911f4f459) |
| --- |

## [◆ ](#a11b644a8526139c4cc1850dac1271ced)O\_WRONLY

| #define O\_WRONLY   [ZVFS\_O\_WRONLY](fdtable_8h.md#abf07c70a006713aaed00a82ed87fb2be) |
| --- |

## Function Documentation

## [◆ ](#acfc4bf677fc9f8be66d9624175cb3775)fcntl()

| int fcntl | ( | int | *fildes*, |
| --- | --- | --- | --- |
|  |  | int | *cmd*, |
|  |  |  | *...* ) |

## [◆ ](#ac843f2e35e60c3bbf1da47d84306f29b)open()

| int open | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | int | *flags*, |
|  |  |  | *...* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [fcntl.h](fcntl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
