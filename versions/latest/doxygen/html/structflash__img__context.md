---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structflash__img__context.html
original_path: doxygen/html/structflash__img__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_img\_context Struct Reference

[Operating System Services](group__os__services.md) » [Flash image API](group__flash__img__api.md)

`#include <[flash_img.h](flash__img_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [buf](#a80fb0afaa391d3242c7de9ffe0f10675) [CONFIG\_IMG\_BLOCK\_BUF\_SIZE] |
| const struct [flash\_area](structflash__area.md) \* | [flash\_area](#ae98e6408fe707543f30094f89ae43bdd) |
| struct [stream\_flash\_ctx](structstream__flash__ctx.md) | [stream](#a9bdb531f92f32957ab78e6cfcced6a3b) |

## Field Documentation

## [◆ ](#a80fb0afaa391d3242c7de9ffe0f10675)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flash\_img\_context::buf[CONFIG\_IMG\_BLOCK\_BUF\_SIZE] |
| --- |

## [◆ ](#ae98e6408fe707543f30094f89ae43bdd)flash\_area

| const struct [flash\_area](structflash__area.md)\* flash\_img\_context::flash\_area |
| --- |

## [◆ ](#a9bdb531f92f32957ab78e6cfcced6a3b)stream

| struct [stream\_flash\_ctx](structstream__flash__ctx.md) flash\_img\_context::stream |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/dfu/[flash\_img.h](flash__img_8h_source.md)

- [flash\_img\_context](structflash__img__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
