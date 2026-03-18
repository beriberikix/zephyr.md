---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__fcb__data__structures.html
original_path: doxygen/html/group__fcb__data__structures.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Flash Circular Buffer Data Structures

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md)

| Data Structures | |
| --- | --- |
| struct | [fcb\_entry](structfcb__entry.md) |
|  | FCB entry info structure. [More...](structfcb__entry.md#details) |
| struct | [fcb\_entry\_ctx](structfcb__entry__ctx.md) |
|  | Structure for transferring complete information about FCB entry location within flash memory. [More...](structfcb__entry__ctx.md#details) |
| struct | [fcb](structfcb.md) |
|  | FCB instance structure. [More...](structfcb.md#details) |

| Macros | |
| --- | --- |
| #define | [FCB\_MAX\_LEN](#gaccabb1cb7f83c0d8919571cf3de7ee47)   (0x3fffu) |
|  | Max length of element (16,383). |
| #define | [FCB\_ENTRY\_FA\_DATA\_OFF](#ga9b47a1aa59039995107c8e23dfacf43f)(entry) |
|  | Helper macro for calculating the data offset related to the fcb [flash\_area](structflash__area.md "Flash partition.") start offset. |
| #define | [FCB\_FLAGS\_CRC\_DISABLED](#ga2fc8801bea1d91a422aa622bcf4cb6e0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Flag to disable CRC for the fcb\_entries in flash. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga9b47a1aa59039995107c8e23dfacf43f)FCB\_ENTRY\_FA\_DATA\_OFF

| #define FCB\_ENTRY\_FA\_DATA\_OFF | ( |  | *entry* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[fcb.h](fcb_8h.md)>`

**Value:**

(entry.fe\_sector->fs\_off +\

entry.fe\_data\_off)

Helper macro for calculating the data offset related to the fcb [flash\_area](structflash__area.md "Flash partition.") start offset.

Parameters
:   | entry | fcb entry structure |
    | --- | --- |

## [◆ ](#ga2fc8801bea1d91a422aa622bcf4cb6e0)FCB\_FLAGS\_CRC\_DISABLED

| #define FCB\_FLAGS\_CRC\_DISABLED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[fcb.h](fcb_8h.md)>`

Flag to disable CRC for the fcb\_entries in flash.

## [◆ ](#gaccabb1cb7f83c0d8919571cf3de7ee47)FCB\_MAX\_LEN

| #define FCB\_MAX\_LEN   (0x3fffu) |
| --- |

`#include <[fcb.h](fcb_8h.md)>`

Max length of element (16,383).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
