---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mman_8h.html
original_path: doxygen/html/mman_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mman.h File Reference

`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](mman_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PROT\_NONE](#a6a982b48b8d3eb8eccd17e0d54ee5379)   0x0 |
| #define | [PROT\_READ](#a15bf68ce8b590838b3a5c0b639d8d519)   0x1 |
| #define | [PROT\_WRITE](#a2a79c8ceefb8fc25a940ae07a3d94429)   0x2 |
| #define | [PROT\_EXEC](#a77848f068638e916c72cd543f5ecb815)   0x4 |
| #define | [MAP\_SHARED](#a57028962c2a7c0c802ca6613492f2ef3)   0x1 |
| #define | [MAP\_PRIVATE](#a398ef47a991a44389aa9818c98a28d24)   0x2 |
| #define | [MAP\_FIXED](#a387ec707b30c5e78cf20a14517a63b96)   0x4 |
| #define | [MAP\_ANONYMOUS](#ae4f86bff73414c5fc08c058f957212f0)   0x20 |
| #define | [MS\_SYNC](#aee74e153705852ce48dca911f1b94d72)   0x0 |
| #define | [MS\_ASYNC](#a98930d8c4137a6cf3f9e21b2b7c84c24)   0x1 |
| #define | [MS\_INVALIDATE](#ad094236c94cb5fcfd6a663b646782bc8)   0x2 |
| #define | [MAP\_FAILED](#a8523dcf952f6ff059a3bed717e4f1296)   ((void \*)-1) |
| #define | [MCL\_CURRENT](#a22408a60244fd4662ed07d8afd74f8d0)   0 |
| #define | [MCL\_FUTURE](#a403c070913f388ac8d97521f949533ae)   1 |

| Functions | |
| --- | --- |
| int | [mlock](#a49da9349d68e3ced27b73c1b2e88ebf3) (const void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int | [mlockall](#ad4697a198c5b65f462dc77e3699a4f03) (int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| void \* | [mmap](#ac2e7d057b16f0c959ffb39d8719eb1ed) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, int prot, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), int fildes, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)) |
| int | [msync](#abef113c04cdf88b279b9d4204a63d448) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| int | [munlock](#ad3cfd73f8180a1a364cb57dc909bcb69) (const void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int | [munlockall](#a03b30383879c5b943ac4d4f9077aeb66) (void) |
| int | [munmap](#a01ff21bc70401bee9b80c350763087f7) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int | [shm\_open](#a14d35ac0e791a20d8773bfa13c456c2b) (const char \*name, int oflag, [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) mode) |
| int | [shm\_unlink](#a4037e49e9537e24edd610bd1acf090da) (const char \*name) |

## Macro Definition Documentation

## [◆ ](#ae4f86bff73414c5fc08c058f957212f0)MAP\_ANONYMOUS

| #define MAP\_ANONYMOUS   0x20 |
| --- |

## [◆ ](#a8523dcf952f6ff059a3bed717e4f1296)MAP\_FAILED

| #define MAP\_FAILED   ((void \*)-1) |
| --- |

## [◆ ](#a387ec707b30c5e78cf20a14517a63b96)MAP\_FIXED

| #define MAP\_FIXED   0x4 |
| --- |

## [◆ ](#a398ef47a991a44389aa9818c98a28d24)MAP\_PRIVATE

| #define MAP\_PRIVATE   0x2 |
| --- |

## [◆ ](#a57028962c2a7c0c802ca6613492f2ef3)MAP\_SHARED

| #define MAP\_SHARED   0x1 |
| --- |

## [◆ ](#a22408a60244fd4662ed07d8afd74f8d0)MCL\_CURRENT

| #define MCL\_CURRENT   0 |
| --- |

## [◆ ](#a403c070913f388ac8d97521f949533ae)MCL\_FUTURE

| #define MCL\_FUTURE   1 |
| --- |

## [◆ ](#a98930d8c4137a6cf3f9e21b2b7c84c24)MS\_ASYNC

| #define MS\_ASYNC   0x1 |
| --- |

## [◆ ](#ad094236c94cb5fcfd6a663b646782bc8)MS\_INVALIDATE

| #define MS\_INVALIDATE   0x2 |
| --- |

## [◆ ](#aee74e153705852ce48dca911f1b94d72)MS\_SYNC

| #define MS\_SYNC   0x0 |
| --- |

## [◆ ](#a77848f068638e916c72cd543f5ecb815)PROT\_EXEC

| #define PROT\_EXEC   0x4 |
| --- |

## [◆ ](#a6a982b48b8d3eb8eccd17e0d54ee5379)PROT\_NONE

| #define PROT\_NONE   0x0 |
| --- |

## [◆ ](#a15bf68ce8b590838b3a5c0b639d8d519)PROT\_READ

| #define PROT\_READ   0x1 |
| --- |

## [◆ ](#a2a79c8ceefb8fc25a940ae07a3d94429)PROT\_WRITE

| #define PROT\_WRITE   0x2 |
| --- |

## Function Documentation

## [◆ ](#a49da9349d68e3ced27b73c1b2e88ebf3)mlock()

| int mlock | ( | const void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

## [◆ ](#ad4697a198c5b65f462dc77e3699a4f03)mlockall()

| int mlockall | ( | int | *flags* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac2e7d057b16f0c959ffb39d8719eb1ed)mmap()

| void \* mmap | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | int | *prot*, |
|  |  | int | *flags*, |
|  |  | int | *fildes*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *off* ) |

## [◆ ](#abef113c04cdf88b279b9d4204a63d448)msync()

| int msync | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length*, |
|  |  | int | *flags* ) |

## [◆ ](#ad3cfd73f8180a1a364cb57dc909bcb69)munlock()

| int munlock | ( | const void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

## [◆ ](#a03b30383879c5b943ac4d4f9077aeb66)munlockall()

| int munlockall | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a01ff21bc70401bee9b80c350763087f7)munmap()

| int munmap | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

## [◆ ](#a14d35ac0e791a20d8773bfa13c456c2b)shm\_open()

| int shm\_open | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | int | *oflag*, |
|  |  | [mode\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#adb8322e115035a284aab704909e63d00) | *mode* ) |

## [◆ ](#a4037e49e9537e24edd610bd1acf090da)shm\_unlink()

| int shm\_unlink | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [sys](dir_cc460655c5c2e41a71042dab318aca48.md)
- [mman.h](mman_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
