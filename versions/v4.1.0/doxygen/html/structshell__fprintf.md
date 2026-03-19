---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structshell__fprintf.html
original_path: doxygen/html/structshell__fprintf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_fprintf Struct Reference

fprintf context
[More...](#details)

`#include <[shell_fprintf.h](shell__fprintf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buffer](#a60eb48520fa96fccdfe7a9f4a32729f7) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [buffer\_size](#a0055b09fb33072e035fca20a4dfd6d15) |
| [shell\_fprintf\_fwrite](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34) | [fwrite](#a8add85184dda7c002e7265baebe2112b) |
| const void \* | [user\_ctx](#ab1920b62893c411baea3e1ff35816185) |
| struct [shell\_fprintf\_control\_block](structshell__fprintf__control__block.md) \* | [ctrl\_blk](#a1bc59eaff9fe7e19c5b6db965c08bb67) |

## Detailed Description

fprintf context

## Field Documentation

## [◆ ](#a60eb48520fa96fccdfe7a9f4a32729f7)buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* shell\_fprintf::buffer |
| --- |

## [◆ ](#a0055b09fb33072e035fca20a4dfd6d15)buffer\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shell\_fprintf::buffer\_size |
| --- |

## [◆ ](#a1bc59eaff9fe7e19c5b6db965c08bb67)ctrl\_blk

| struct [shell\_fprintf\_control\_block](structshell__fprintf__control__block.md)\* shell\_fprintf::ctrl\_blk |
| --- |

## [◆ ](#a8add85184dda7c002e7265baebe2112b)fwrite

| [shell\_fprintf\_fwrite](shell__fprintf_8h.md#a2ea67ad2a9eeffdcfbfe460e4cfe6b34) shell\_fprintf::fwrite |
| --- |

## [◆ ](#ab1920b62893c411baea3e1ff35816185)user\_ctx

| const void\* shell\_fprintf::user\_ctx |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_fprintf.h](shell__fprintf_8h_source.md)

- [shell\_fprintf](structshell__fprintf.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
