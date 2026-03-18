---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structcoredump__cmd__copy__arg.html
original_path: doxygen/html/structcoredump__cmd__copy__arg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump\_cmd\_copy\_arg Struct Reference

[Operating System Services](group__os__services.md) » [Coredump APIs](group__coredump__apis.md)

Coredump copy command ([COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819 "COREDUMP_CMD_COPY_STORED_DUMP")) argument definition.
[More...](#details)

`#include <[coredump.h](debug_2coredump_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#a724583bd7203d16cc46f06698acfc6ef) |
|  | Copy offset. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buffer](#a74495abb94670f983a3f136274485c40) |
|  | Copy destination buffer. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [length](#ae9266221235083dcf6efd7aba2177a75) |
|  | Copy length. |

## Detailed Description

Coredump copy command ([COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819 "COREDUMP_CMD_COPY_STORED_DUMP")) argument definition.

## Field Documentation

## [◆ ](#a74495abb94670f983a3f136274485c40)buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* coredump\_cmd\_copy\_arg::buffer |
| --- |

Copy destination buffer.

## [◆ ](#ae9266221235083dcf6efd7aba2177a75)length

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) coredump\_cmd\_copy\_arg::length |
| --- |

Copy length.

## [◆ ](#a724583bd7203d16cc46f06698acfc6ef)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) coredump\_cmd\_copy\_arg::offset |
| --- |

Copy offset.

---

The documentation for this struct was generated from the following file:

- zephyr/debug/[coredump.h](debug_2coredump_8h_source.md)

- [coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
