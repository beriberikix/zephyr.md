---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/shell__fprintf_8h.html
original_path: doxygen/html/shell__fprintf_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_fprintf.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`

[Go to the source code of this file.](shell__fprintf_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [shell\_fprintf\_control\_block](structshell__fprintf__control__block.md) |
| struct | [shell\_fprintf](structshell__fprintf.md) |
|  | fprintf context [More...](structshell__fprintf.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [shell\_fprintf\_fwrite](#a2ea67ad2a9eeffdcfbfe460e4cfe6b34)) (const void \*user\_ctx, const char \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |

## Typedef Documentation

## [◆ ](#a2ea67ad2a9eeffdcfbfe460e4cfe6b34)shell\_fprintf\_fwrite

| typedef void(\* shell\_fprintf\_fwrite) (const void \*user\_ctx, const char \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_fprintf.h](shell__fprintf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
