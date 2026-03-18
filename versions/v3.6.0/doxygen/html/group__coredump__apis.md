---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__coredump__apis.html
original_path: doxygen/html/group__coredump__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Coredump APIs

[Operating System Services](group__os__services.md)

Coredump APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md) |
|  | Coredump copy command ([COREDUMP\_CMD\_COPY\_STORED\_DUMP](#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819)) argument definition. [More...](structcoredump__cmd__copy__arg.md#details) |

| Enumerations | |
| --- | --- |
| enum | [coredump\_query\_id](#ga26360cadb6b43f5c86b59332e66008f5) { [COREDUMP\_QUERY\_GET\_ERROR](#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb) , [COREDUMP\_QUERY\_HAS\_STORED\_DUMP](#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83) , [COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483) , [COREDUMP\_QUERY\_MAX](#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d) } |
|  | Query ID. [More...](#ga26360cadb6b43f5c86b59332e66008f5) |
| enum | [coredump\_cmd\_id](#ga48765a88d430aaec373a2ce6e4796578) {     [COREDUMP\_CMD\_CLEAR\_ERROR](#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f) , [COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa) , [COREDUMP\_CMD\_ERASE\_STORED\_DUMP](#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6) , [COREDUMP\_CMD\_COPY\_STORED\_DUMP](#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819) ,     [COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321) , [COREDUMP\_CMD\_MAX](#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)   } |
|  | Command ID. [More...](#ga48765a88d430aaec373a2ce6e4796578) |

| Functions | |
| --- | --- |
| void | [coredump](#gac8e7b27f4bbef5120b745677d5c64200) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const z\_arch\_esf\_t \*esf, struct [k\_thread](structk__thread.md) \*thread) |
|  | Perform coredump. |
| void | [coredump\_memory\_dump](#ga835467b2517f871b0092f0dd7757f14b) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr) |
|  | Dump memory region. |
| void | [coredump\_buffer\_output](#ga00bc832d1a9fb7d23d63c09abcf313eb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buflen) |
|  | Output the buffer via coredump. |
| int | [coredump\_query](#gad521f35e7b487cbaed553f8f8e4a9e27) (enum [coredump\_query\_id](#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg) |
|  | Perform query on coredump subsystem. |
| int | [coredump\_cmd](#ga9ebe60f88decfba5b798736984b4c496) (enum [coredump\_cmd\_id](#ga48765a88d430aaec373a2ce6e4796578) query\_id, void \*arg) |
|  | Perform command on coredump subsystem. |

## Detailed Description

Coredump APIs.

## Enumeration Type Documentation

## [◆ ](#ga48765a88d430aaec373a2ce6e4796578)coredump\_cmd\_id

| enum [coredump\_cmd\_id](#ga48765a88d430aaec373a2ce6e4796578) |
| --- |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Command ID.

| Enumerator | |
| --- | --- |
| COREDUMP\_CMD\_CLEAR\_ERROR | Clear error code from backend.  Returns 0 if successful, failed otherwise. |
| COREDUMP\_CMD\_VERIFY\_STORED\_DUMP | Verify that the stored coredump is valid.  Returns:   - 1 if valid. - 0 if not valid or no stored coredump. - -ENOTSUP if this command is not supported. - Otherwise, error code from backend. |
| COREDUMP\_CMD\_ERASE\_STORED\_DUMP | Erase the stored coredump.  Returns:   - 0 if successful. - -ENOTSUP if this command is not supported. - Otherwise, error code from backend. |
| COREDUMP\_CMD\_COPY\_STORED\_DUMP | Copy the raw stored coredump.  Returns:   - copied size if successful - 0 if stored coredump is not found - -ENOTSUP if this command is not supported. - Otherwise, error code from backend. |
| COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP | Invalidate the stored coredump.  This is faster than erasing the whole partition.  Returns:   - 0 if successful. - -ENOTSUP if this command is not supported. - Otherwise, error code from backend. |
| COREDUMP\_CMD\_MAX | Max value for command ID. |

## [◆ ](#ga26360cadb6b43f5c86b59332e66008f5)coredump\_query\_id

| enum [coredump\_query\_id](#ga26360cadb6b43f5c86b59332e66008f5) |
| --- |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Query ID.

| Enumerator | |
| --- | --- |
| COREDUMP\_QUERY\_GET\_ERROR | Returns error code from backend. |
| COREDUMP\_QUERY\_HAS\_STORED\_DUMP | Check if there is a stored coredump from backend.  Returns:   - 1 if there is a stored coredump, 0 if none. - -ENOTSUP if this query is not supported. - Otherwise, error code from backend. |
| COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE | Returns:   - coredump raw size from backend, 0 if none. - -ENOTSUP if this query is not supported. - Otherwise, error code from backend. |
| COREDUMP\_QUERY\_MAX | Max value for query ID. |

## Function Documentation

## [◆ ](#gac8e7b27f4bbef5120b745677d5c64200)coredump()

| void coredump | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason*, |
| --- | --- | --- | --- |
|  |  | const z\_arch\_esf\_t \* | *esf*, |
|  |  | struct [k\_thread](structk__thread.md) \* | *thread* ) |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Perform coredump.

Normally, this is called inside z\_fatal\_error() to generate coredump when a fatal error is encountered. This can also be called on demand whenever a coredump is desired.

Parameters
:   | reason | Reason for the fatal error |
    | --- | --- |
    | esf | Exception context |
    | thread | Thread information to dump |

## [◆ ](#ga00bc832d1a9fb7d23d63c09abcf313eb)coredump\_buffer\_output()

| void coredump\_buffer\_output | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buflen* ) |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Output the buffer via coredump.

This outputs the buffer of byte array to the coredump backend. For example, this can be called to output the coredump section containing registers, or a section for memory dump.

Parameters
:   | buf | Buffer to be send to coredump output |
    | --- | --- |
    | buflen | Buffer length |

## [◆ ](#ga9ebe60f88decfba5b798736984b4c496)coredump\_cmd()

| int coredump\_cmd | ( | enum [coredump\_cmd\_id](#ga48765a88d430aaec373a2ce6e4796578) | *cmd\_id*, |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Perform command on coredump subsystem.

Perform command on coredump subsystem, for example, output the stored coredump via logging.

Parameters
:   | [in] | cmd\_id | Command ID |
    | --- | --- | --- |
    | [in,out] | arg | Pointer to argument for exchanging information |

Returns
:   Depends on the command

## [◆ ](#ga835467b2517f871b0092f0dd7757f14b)coredump\_memory\_dump()

| void coredump\_memory\_dump | ( | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *start\_addr*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *end\_addr* ) |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Dump memory region.

Parameters
:   | start\_addr | Start address of memory region to be dumped |
    | --- | --- |
    | end\_addr | End address of memory region to be dumped |

## [◆ ](#gad521f35e7b487cbaed553f8f8e4a9e27)coredump\_query()

| int coredump\_query | ( | enum [coredump\_query\_id](#ga26360cadb6b43f5c86b59332e66008f5) | *query\_id*, |
| --- | --- | --- | --- |
|  |  | void \* | *arg* ) |

`#include <[coredump.h](debug_2coredump_8h.md)>`

Perform query on coredump subsystem.

Query the coredump subsystem for information, for example, if there is an error.

Parameters
:   | [in] | query\_id | Query ID |
    | --- | --- | --- |
    | [in,out] | arg | Pointer to argument for exchanging information |

Returns
:   Depends on the query

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
