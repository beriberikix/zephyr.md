---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fcntl_8h.html
original_path: doxygen/html/fcntl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcntl.h File Reference

[Go to the source code of this file.](fcntl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [O\_CREAT](#a1cf6b1de1fffedaa1d26b189e9a8d2cc)   0x0200 |
| #define | [O\_ACCMODE](#a4dc4d45e07d2abc899bcaf04b2846a87)   ([O\_RDONLY](#a7a68c9ffaac7dbcd652225dd7c06a54b) | [O\_WRONLY](#a11b644a8526139c4cc1850dac1271ced) | [O\_RDWR](#abb0586253488ee61072b73557eeb873b)) |
| #define | [O\_RDONLY](#a7a68c9ffaac7dbcd652225dd7c06a54b)   00 |
| #define | [O\_WRONLY](#a11b644a8526139c4cc1850dac1271ced)   01 |
| #define | [O\_RDWR](#abb0586253488ee61072b73557eeb873b)   02 |
| #define | [O\_APPEND](#ae036f789407d21f07b211552d67b3214)   0x0400 |
| #define | [O\_EXCL](#a9f5acfe79fafe14b6694447bd0e9f10b)   0x0800 |
| #define | [O\_NONBLOCK](#a39d33ce33804efd4d52606d59071c6d8)   0x4000 |
| #define | [F\_DUPFD](#ab93a8621587aba90181efd7d3aeea67e)   0 |
| #define | [F\_GETFL](#a025fad21a889c79f02ec53abe3526c32)   3 |
| #define | [F\_SETFL](#af2939853c650561d3495ed40f68f6249)   4 |

| Functions | |
| --- | --- |
| int | [open](#ac843f2e35e60c3bbf1da47d84306f29b) (const char \*name, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),...) |
| int | [fcntl](#acfc4bf677fc9f8be66d9624175cb3775) (int fildes, int [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),...) |

## Macro Definition Documentation

## [◆ ](#ab93a8621587aba90181efd7d3aeea67e)F\_DUPFD

| #define F\_DUPFD   0 |
| --- |

## [◆ ](#a025fad21a889c79f02ec53abe3526c32)F\_GETFL

| #define F\_GETFL   3 |
| --- |

## [◆ ](#af2939853c650561d3495ed40f68f6249)F\_SETFL

| #define F\_SETFL   4 |
| --- |

## [◆ ](#a4dc4d45e07d2abc899bcaf04b2846a87)O\_ACCMODE

| #define O\_ACCMODE   ([O\_RDONLY](#a7a68c9ffaac7dbcd652225dd7c06a54b) | [O\_WRONLY](#a11b644a8526139c4cc1850dac1271ced) | [O\_RDWR](#abb0586253488ee61072b73557eeb873b)) |
| --- |

## [◆ ](#ae036f789407d21f07b211552d67b3214)O\_APPEND

| #define O\_APPEND   0x0400 |
| --- |

## [◆ ](#a1cf6b1de1fffedaa1d26b189e9a8d2cc)O\_CREAT

| #define O\_CREAT   0x0200 |
| --- |

## [◆ ](#a9f5acfe79fafe14b6694447bd0e9f10b)O\_EXCL

| #define O\_EXCL   0x0800 |
| --- |

## [◆ ](#a39d33ce33804efd4d52606d59071c6d8)O\_NONBLOCK

| #define O\_NONBLOCK   0x4000 |
| --- |

## [◆ ](#a7a68c9ffaac7dbcd652225dd7c06a54b)O\_RDONLY

| #define O\_RDONLY   00 |
| --- |

## [◆ ](#abb0586253488ee61072b73557eeb873b)O\_RDWR

| #define O\_RDWR   02 |
| --- |

## [◆ ](#a11b644a8526139c4cc1850dac1271ced)O\_WRONLY

| #define O\_WRONLY   01 |
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
