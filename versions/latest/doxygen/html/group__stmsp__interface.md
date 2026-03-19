---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__stmsp__interface.html
original_path: doxygen/html/group__stmsp__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Coresight STMESP interface

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md)

Coresight STMESP (STM Extended Stimulus Port) Interface.
[More...](#details)

| Functions | |
| --- | --- |
| static void | [stmesp\_flag](#ga2ffcc08b7d5c32c90b5d24982c0f6349) (STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write flag to STMESP. |
| static void | [stmesp\_data8](#ga4af9486d77c93a55f221c7647d69a9f2) (STMESP\_Type \*reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 8 bit data to STMESP. |
| static void | [stmesp\_data16](#gaef1918a9d15d8da34fb5f2d7a11ff5fd) (STMESP\_Type \*reg, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 16 bit data to STMESP. |
| static void | [stmesp\_data32](#gaa7885c5a7620e46a532dbf405bfc6034) (STMESP\_Type \*reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ts, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) marked, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) guaranteed) |
|  | Write 32 bit data to STMESP. |
| static int | [stmesp\_get\_port](#ga4350f5d201e3591221a932aa9fc3e94d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx, STMESP\_Type \*\*port) |
|  | Return address of a STM extended stimulus port. |

## Detailed Description

Coresight STMESP (STM Extended Stimulus Port) Interface.

## Function Documentation

## [◆ ](#gaef1918a9d15d8da34fb5f2d7a11ff5fd)stmesp\_data16()

| | void stmesp\_data16 | ( | STMESP\_Type \* | *reg*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ts*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *marked*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *guaranteed* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[stmesp.h](stmesp_8h.md)>`

Write 16 bit data to STMESP.

Parameters
:   | reg | STMESP register set. |
    | --- | --- |
    | data | Half word to write. |
    | ts | If true add timestamp. |
    | marked | If true marked write. |
    | guaranteed | If true guaranteed write and invariant if false. |

## [◆ ](#gaa7885c5a7620e46a532dbf405bfc6034)stmesp\_data32()

| | void stmesp\_data32 | ( | STMESP\_Type \* | *reg*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ts*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *marked*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *guaranteed* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[stmesp.h](stmesp_8h.md)>`

Write 32 bit data to STMESP.

Parameters
:   | reg | STMESP register set. |
    | --- | --- |
    | data | Word to write. |
    | ts | If true add timestamp. |
    | marked | If true marked write. |
    | guaranteed | If true guaranteed write and invariant if false. |

## [◆ ](#ga4af9486d77c93a55f221c7647d69a9f2)stmesp\_data8()

| | void stmesp\_data8 | ( | STMESP\_Type \* | *reg*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ts*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *marked*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *guaranteed* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[stmesp.h](stmesp_8h.md)>`

Write 8 bit data to STMESP.

Parameters
:   | reg | STMESP register set. |
    | --- | --- |
    | data | Byte to write. |
    | ts | If true add timestamp. |
    | marked | If true marked write. |
    | guaranteed | If true guaranteed write and invariant if false. |

## [◆ ](#ga2ffcc08b7d5c32c90b5d24982c0f6349)stmesp\_flag()

| | void stmesp\_flag | ( | STMESP\_Type \* | *reg*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ts*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *guaranteed* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[stmesp.h](stmesp_8h.md)>`

Write flag to STMESP.

Parameters
:   | reg | STMESP register set. |
    | --- | --- |
    | data | Data written to the flag register. |
    | ts | If true add timestamp. |
    | guaranteed | If true guaranteed write and invariant if false. |

## [◆ ](#ga4350f5d201e3591221a932aa9fc3e94d)stmesp\_get\_port()

| | int stmesp\_get\_port | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idx*, | | --- | --- | --- | --- | |  |  | STMESP\_Type \*\* | *port* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[stmesp.h](stmesp_8h.md)>`

Return address of a STM extended stimulus port.

Function return a port from the local STMESP instance.

Parameters
:   | [in] | idx | Index of the requested stimulus port. |
    | --- | --- | --- |
    | [out] | port | Location where pointer to the port is written. |

Return values
:   | -EINVAL | if `idx` or `port` is invalid. |
    | --- | --- |
    | 0 | on success. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
