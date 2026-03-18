---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/loader_8h.html
original_path: doxygen/html/loader_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

loader.h File Reference

`#include <[zephyr/llext/elf.h](elf_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/llext/llext.h](llext_8h_source.md)>`

[Go to the source code of this file.](loader_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [llext\_loader](structllext__loader.md) |
|  | Linkable loadable extension loader context. [More...](structllext__loader.md#details) |

| Functions | |
| --- | --- |
| static int | [llext\_read](group__llext__loader.md#gaf3d8bb89579039b77b10e6d15ff8a712) (struct [llext\_loader](structllext__loader.md) \*l, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| static int | [llext\_seek](group__llext__loader.md#gabbf3d285c9787cebe7bb105bacce15fa) (struct [llext\_loader](structllext__loader.md) \*l, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |
| static void \* | [llext\_peek](group__llext__loader.md#ga241589ea6309b55ceb59f7e4b583600f) (struct [llext\_loader](structllext__loader.md) \*l, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) pos) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [llext](dir_d35526af36d7b5daa0761e4cf61cfe4a.md)
- [loader.h](loader_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
