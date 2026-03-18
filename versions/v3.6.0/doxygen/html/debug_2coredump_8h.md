---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/debug_2coredump_8h.html
original_path: doxygen/html/debug_2coredump_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

| Enumerations | |
| --- | --- |
| enum | [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) { [COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb) , [COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83) , [COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483) , [COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d) } |
|  | Query ID. [More...](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) |
| enum | [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) {     [COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f) , [COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa) , [COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6) , [COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819) ,     [COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321) , [COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)   } |
|  | Command ID. [More...](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) |

| Functions | |
| --- | --- |
| void | [coredump](group__coredump__apis.md#gac8e7b27f4bbef5120b745677d5c64200) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const z\_arch\_esf\_t \*esf, struct [k\_thread](structk__thread.md) \*thread) |
|  | Perform coredump. |
| void | [coredump\_memory\_dump](group__coredump__apis.md#ga835467b2517f871b0092f0dd7757f14b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr) |
|  | Dump memory region. |
| void | [coredump\_buffer\_output](group__coredump__apis.md#ga00bc832d1a9fb7d23d63c09abcf313eb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Output the buffer via coredump. |
| int | [coredump\_query](group__coredump__apis.md#gad521f35e7b487cbaed553f8f8e4a9e27) (enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg) |
|  | Perform query on coredump subsystem. |
| int | [coredump\_cmd](group__coredump__apis.md#ga9ebe60f88decfba5b798736984b4c496) (enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) query\_id, void \*arg) |
|  | Perform command on coredump subsystem. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coredump.h](debug_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
