---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structjwt__builder.html
original_path: doxygen/html/structjwt__builder.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

jwt\_builder Struct Reference

[Utilities](group__utilities.md) » [JSON](group__json.md) » [JSON Web Token (JWT)](group__jwt.md)

JWT data tracking.
[More...](#details)

`#include <[jwt.h](jwt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char \* | [base](#a23a0aa512e5bc66722b6d7a8cf20aa95) |
|  | The base of the buffer we are writing to. |
| char \* | [buf](#a74a3d3e645f8b438bcdf12abdf0aabf7) |
|  | The place in this buffer where we are currently writing. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [len](#a8fcc85d6704b63cd773397a5a4d9774d) |
|  | The remaining free space in `buf`. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [overflowed](#af53cb40609f623b95ff68d3c66a387ce) |
|  | Flag that is set if we try to write past the end of the buffer. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char | [wip](#a4bd0376eef7f162e9e9e1e1399388fed) [3] |
| int | [pending](#a7e4880c8fc8136083bad0ef2559c67e4) |

## Detailed Description

JWT data tracking.

JSON Web Tokens contain several sections, each encoded in Base64URL. This structure tracks the token as it is being built, including limits on the amount of available space. It should be initialized with [jwt\_init\_builder()](group__jwt.md#gab10ee40ee3c0b3eea98051c2acbb8a75 "Initialize the JWT builder.").

## Field Documentation

## [◆ ](#a23a0aa512e5bc66722b6d7a8cf20aa95)base

| char\* jwt\_builder::base |
| --- |

The base of the buffer we are writing to.

## [◆ ](#a74a3d3e645f8b438bcdf12abdf0aabf7)buf

| char\* jwt\_builder::buf |
| --- |

The place in this buffer where we are currently writing.

## [◆ ](#a8fcc85d6704b63cd773397a5a4d9774d)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) jwt\_builder::len |
| --- |

The remaining free space in `buf`.

## [◆ ](#af53cb40609f623b95ff68d3c66a387ce)overflowed

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) jwt\_builder::overflowed |
| --- |

Flag that is set if we try to write past the end of the buffer.

If set, the token is not valid.

## [◆ ](#a7e4880c8fc8136083bad0ef2559c67e4)pending

| int jwt\_builder::pending |
| --- |

## [◆ ](#a4bd0376eef7f162e9e9e1e1399388fed)wip

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char jwt\_builder::wip[3] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/data/[jwt.h](jwt_8h_source.md)

- [jwt\_builder](structjwt__builder.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
