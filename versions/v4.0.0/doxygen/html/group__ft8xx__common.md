---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ft8xx__common.html
original_path: doxygen/html/group__ft8xx__common.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx common functions

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [FT8xx driver APIs](group__ft8xx__interface.md)

FT8xx functions to write and read memory.
[More...](#details)

| Functions | |
| --- | --- |
| void | [ft8xx\_wr8](#ga7623499f328d820b1e84d2a3834a89a2) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write 1 byte (8 bits) to FT8xx memory. |
| void | [ft8xx\_wr16](#gadfbff24d8fb246081cefbc51190b32e5) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write 2 bytes (16 bits) to FT8xx memory. |
| void | [ft8xx\_wr32](#ga3158d2c2605f66fc22bbf336d780b8bf) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write 4 bytes (32 bits) to FT8xx memory. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ft8xx\_rd8](#gac7ed90cf4a51fc9139c49ce352a25385) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 1 byte (8 bits) from FT8xx memory. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ft8xx\_rd16](#gad52c57f65516917792cb07f6d2f2bf71) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 2 bytes (16 bits) from FT8xx memory. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ft8xx\_rd32](#ga9e78caa02181c65a5c5dac39438ca3e3) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 4 bytes (32 bits) from FT8xx memory. |

## Detailed Description

FT8xx functions to write and read memory.

## Function Documentation

## [◆ ](#gad52c57f65516917792cb07f6d2f2bf71)ft8xx\_rd16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ft8xx\_rd16 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 2 bytes (16 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#ga9e78caa02181c65a5c5dac39438ca3e3)ft8xx\_rd32()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ft8xx\_rd32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 4 bytes (32 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#gac7ed90cf4a51fc9139c49ce352a25385)ft8xx\_rd8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ft8xx\_rd8 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Read 1 byte (8 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#gadfbff24d8fb246081cefbc51190b32e5)ft8xx\_wr16()

| void ft8xx\_wr16 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 2 bytes (16 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Value to write |

## [◆ ](#ga3158d2c2605f66fc22bbf336d780b8bf)ft8xx\_wr32()

| void ft8xx\_wr32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 4 bytes (32 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Value to write |

## [◆ ](#ga7623499f328d820b1e84d2a3834a89a2)ft8xx\_wr8()

| void ft8xx\_wr8 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) |

`#include <[ft8xx_common.h](ft8xx__common_8h.md)>`

Write 1 byte (8 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Byte to write |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
