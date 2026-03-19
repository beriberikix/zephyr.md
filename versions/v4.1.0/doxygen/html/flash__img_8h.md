---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/flash__img_8h.html
original_path: doxygen/html/flash__img_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash\_img.h File Reference

Flash image header file.
[More...](#details)

`#include <[zephyr/storage/stream_flash.h](stream__flash_8h_source.md)>`

[Go to the source code of this file.](flash__img_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [flash\_img\_context](structflash__img__context.md) |
| struct | [flash\_img\_check](structflash__img__check.md) |
|  | Structure for verify flash region integrity. [More...](structflash__img__check.md#details) |

| Functions | |
| --- | --- |
| int | [flash\_img\_init\_id](group__flash__img__api.md#ga1b194edcb7e4ae34717d011f08d93e0c) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Initialize context needed for writing the image to the flash. |
| int | [flash\_img\_init](group__flash__img__api.md#gac6d1d7811516493242b318be2ecd82df) (struct [flash\_img\_context](structflash__img__context.md) \*ctx) |
|  | Initialize context needed for writing the image to the flash. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_img\_bytes\_written](group__flash__img__api.md#gac1ef017d400bda921ca894d13126b390) (struct [flash\_img\_context](structflash__img__context.md) \*ctx) |
|  | Read number of bytes of the image written to the flash. |
| int | [flash\_img\_buffered\_write](group__flash__img__api.md#gae3cb2d6be9f993bcf5a97931475d9a6d) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) flush) |
|  | Process input buffers to be written to the image slot 1. |
| int | [flash\_img\_check](group__flash__img__api.md#ga5a025255d8bf4a94f9e8d315d5502e88) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, const struct flash\_img\_check \*fic, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Verify flash memory length bytes integrity from a flash area. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flash\_img\_get\_upload\_slot](group__flash__img__api.md#gaeb242ed3d7654bf94e0dce7d6c24c2a0) (void) |
|  | Get the flash area id for the image upload slot. |

## Detailed Description

Flash image header file.

This header file declares prototypes for the flash image APIs used for DFU.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dfu](dir_b8bb0fd55a94366ea1f20beca08b160d.md)
- [flash\_img.h](flash__img_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
