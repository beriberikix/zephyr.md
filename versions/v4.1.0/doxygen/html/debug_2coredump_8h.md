---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/debug_2coredump_8h.html
original_path: doxygen/html/debug_2coredump_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump.h File Reference

`#include <stddef.h>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](debug_2coredump_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md) |
|  | Coredump copy command ([COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819 "COREDUMP_CMD_COPY_STORED_DUMP")) argument definition. [More...](structcoredump__cmd__copy__arg.md#details) |

| Macros | |
| --- | --- |
| #define | [COREDUMP\_BEGIN\_STR](#acc9e7259fd50fc8e2fb9cbbccb6b0638)   "BEGIN#" |
| #define | [COREDUMP\_END\_STR](#a93ebd2883ffe26c5352c3b429fa62688)   "END#" |
| #define | [COREDUMP\_ERROR\_STR](#a2a1d82ed80cd3a715dd489beddbce57f)   "ERROR CANNOT DUMP#" |
| #define | [COREDUMP\_PREFIX\_STR](#a0a42d70f4a13d3b7c43627259992ba39)   "#CD:" |

| Enumerations | |
| --- | --- |
| enum | [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) { [COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb) , [COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83) , [COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483) , [COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d) } |
|  | Query ID. [More...](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) |
| enum | [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) {     [COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f) , [COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa) , [COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6) , [COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819) ,     [COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321) , [COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)   } |
|  | Command ID. [More...](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) |

| Functions | |
| --- | --- |
| static void | [coredump](group__coredump__apis.md#gab97503d4de13bdde139fe0880947379a) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const struct [arch\_esf](structarch__esf.md) \*esf, struct [k\_thread](structk__thread.md) \*thread) |
|  | Perform coredump. |
| static void | [coredump\_memory\_dump](group__coredump__apis.md#gab8823860579eee41380da8b7a4d93cd0) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr) |
|  | Dump memory region. |
| static void | [coredump\_buffer\_output](group__coredump__apis.md#gabe58e47cc733572a6650d3fd2cfc7d9d) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Output the buffer via coredump. |
| static int | [coredump\_query](group__coredump__apis.md#ga772697785da4247a7a8c3fccdbe921ce) (enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg) |
|  | Perform query on coredump subsystem. |
| static int | [coredump\_cmd](group__coredump__apis.md#ga5c7f6fb24c724ede550d2c54f7ce2336) (enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) query\_id, void \*arg) |
|  | Perform command on coredump subsystem. |

## Macro Definition Documentation

## [◆ ](#acc9e7259fd50fc8e2fb9cbbccb6b0638)COREDUMP\_BEGIN\_STR

| #define COREDUMP\_BEGIN\_STR   "BEGIN#" |
| --- |

## [◆ ](#a93ebd2883ffe26c5352c3b429fa62688)COREDUMP\_END\_STR

| #define COREDUMP\_END\_STR   "END#" |
| --- |

## [◆ ](#a2a1d82ed80cd3a715dd489beddbce57f)COREDUMP\_ERROR\_STR

| #define COREDUMP\_ERROR\_STR   "ERROR CANNOT DUMP#" |
| --- |

## [◆ ](#a0a42d70f4a13d3b7c43627259992ba39)COREDUMP\_PREFIX\_STR

| #define COREDUMP\_PREFIX\_STR   "#CD:" |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coredump.h](debug_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
