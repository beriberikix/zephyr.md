---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfcb__entry__ctx.html
original_path: doxygen/html/structfcb__entry__ctx.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb\_entry\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md) » [Flash Circular Buffer Data Structures](group__fcb__data__structures.md)

Structure for transferring complete information about FCB entry location within flash memory.
[More...](#details)

`#include <[fcb.h](fcb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [fcb\_entry](structfcb__entry.md) | [loc](#a0da5217647b82c8799a6cde221253680) |
|  | FCB entry info. |
| const struct [flash\_area](structflash__area.md) \* | [fap](#a8b491cd670e609c2b4d897d15e37eb2b) |
|  | Flash area where the entry is placed. |

## Detailed Description

Structure for transferring complete information about FCB entry location within flash memory.

## Field Documentation

## [◆ ](#a8b491cd670e609c2b4d897d15e37eb2b)fap

| const struct [flash\_area](structflash__area.md)\* fcb\_entry\_ctx::fap |
| --- |

Flash area where the entry is placed.

## [◆ ](#a0da5217647b82c8799a6cde221253680)loc

| struct [fcb\_entry](structfcb__entry.md) fcb\_entry\_ctx::loc |
| --- |

FCB entry info.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fcb.h](fcb_8h_source.md)

- [fcb\_entry\_ctx](structfcb__entry__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
