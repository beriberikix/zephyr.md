---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/smp__shell_8h.html
original_path: doxygen/html/smp__shell_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_shell.h File Reference

Shell transport for the mcumgr SMP protocol.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](smp__shell_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smp\_shell\_data](structsmp__shell__data.md) |
|  | Data used by SMP shell. [More...](structsmp__shell__data.md#details) |

| Macros | |
| --- | --- |
| #define | [SMP\_SHELL\_RX\_BUF\_SIZE](#a472d6f81315fea4827be0a91557832eb)   127 |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [smp\_shell\_rx\_bytes](#a785293b670fcc10190e6c3d480a7d6d6) (struct [smp\_shell\_data](structsmp__shell__data.md) \*data, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bytes, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Attempt to process received bytes as part of an SMP frame. |
| void | [smp\_shell\_process](#a44b90f6ba276d8d7a89d6b90c8bb0341) (struct [smp\_shell\_data](structsmp__shell__data.md) \*data) |
|  | Processes SMP data and executes command if full frame was received. |
| int | [smp\_shell\_init](#a1b71c4da07049b47269002ef6ec2b256) (void) |
|  | Initializes SMP transport over shell. |

## Detailed Description

Shell transport for the mcumgr SMP protocol.

## Macro Definition Documentation

## [◆ ](#a472d6f81315fea4827be0a91557832eb)SMP\_SHELL\_RX\_BUF\_SIZE

| #define SMP\_SHELL\_RX\_BUF\_SIZE   127 |
| --- |

## Function Documentation

## [◆ ](#a1b71c4da07049b47269002ef6ec2b256)smp\_shell\_init()

| int smp\_shell\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initializes SMP transport over shell.

This function should be called before feeding SMP transport with received data.

Returns
:   0 on success

## [◆ ](#a44b90f6ba276d8d7a89d6b90c8bb0341)smp\_shell\_process()

| void smp\_shell\_process | ( | struct [smp\_shell\_data](structsmp__shell__data.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

Processes SMP data and executes command if full frame was received.

This function should be called from thread context.

Parameters
:   | data | SMP shell transfer data. |
    | --- | --- |

## [◆ ](#a785293b670fcc10190e6c3d480a7d6d6)smp\_shell\_rx\_bytes()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) smp\_shell\_rx\_bytes | ( | struct [smp\_shell\_data](structsmp__shell__data.md) \* | *data*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *bytes*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Attempt to process received bytes as part of an SMP frame.

Called to scan buffer from the beginning and consume all bytes that are part of SMP frame until frame or buffer ends.

Parameters
:   | data | SMP shell transfer data. |
    | --- | --- |
    | bytes | Buffer with bytes to process |
    | size | Number of bytes to process |

Returns
:   number of bytes consumed by the SMP

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_shell.h](smp__shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
