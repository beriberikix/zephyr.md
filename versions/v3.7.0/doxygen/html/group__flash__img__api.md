---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__flash__img__api.html
original_path: doxygen/html/group__flash__img__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Flash image API

[Operating System Services](group__os__services.md)

Abstraction layer to write firmware images to flash.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [flash\_img\_context](structflash__img__context.md) |
| struct | [flash\_img\_check](structflash__img__check.md) |
|  | Structure for verify flash region integrity. [More...](structflash__img__check.md#details) |

| Functions | |
| --- | --- |
| int | [flash\_img\_init\_id](#ga1b194edcb7e4ae34717d011f08d93e0c) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Initialize context needed for writing the image to the flash. |
| int | [flash\_img\_init](#gac6d1d7811516493242b318be2ecd82df) (struct [flash\_img\_context](structflash__img__context.md) \*ctx) |
|  | Initialize context needed for writing the image to the flash. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_img\_bytes\_written](#gac1ef017d400bda921ca894d13126b390) (struct [flash\_img\_context](structflash__img__context.md) \*ctx) |
|  | Read number of bytes of the image written to the flash. |
| int | [flash\_img\_buffered\_write](#gae3cb2d6be9f993bcf5a97931475d9a6d) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) flush) |
|  | Process input buffers to be written to the image slot 1. |
| int | [flash\_img\_check](#ga5a025255d8bf4a94f9e8d315d5502e88) (struct [flash\_img\_context](structflash__img__context.md) \*ctx, const struct flash\_img\_check \*fic, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Verify flash memory length bytes integrity from a flash area. |

## Detailed Description

Abstraction layer to write firmware images to flash.

## Function Documentation

## [◆ ](#gae3cb2d6be9f993bcf5a97931475d9a6d)flash\_img\_buffered\_write()

| int flash\_img\_buffered\_write | ( | struct [flash\_img\_context](structflash__img__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *flush* ) |

`#include <[flash_img.h](flash__img_8h.md)>`

Process input buffers to be written to the image slot 1.

flash memory in single blocks. Will store remainder between calls.

A final call to this function with flush set to true will write out the remaining block buffer to flash. Since flash is written to in blocks, the contents of flash from the last byte written up to the next multiple of CONFIG\_IMG\_BLOCK\_BUF\_SIZE is padded with 0xff.

Parameters
:   | ctx | context |
    | --- | --- |
    | data | data to write |
    | len | Number of bytes to write |
    | flush | when true this forces any buffered data to be written to flash |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gac1ef017d400bda921ca894d13126b390)flash\_img\_bytes\_written()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_img\_bytes\_written | ( | struct [flash\_img\_context](structflash__img__context.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_img.h](flash__img_8h.md)>`

Read number of bytes of the image written to the flash.

Parameters
:   | ctx | context |
    | --- | --- |

Returns
:   Number of bytes written to the image flash.

## [◆ ](#ga5a025255d8bf4a94f9e8d315d5502e88)flash\_img\_check()

| int flash\_img\_check | ( | struct [flash\_img\_context](structflash__img__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct flash\_img\_check \* | *fic*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id* ) |

`#include <[flash_img.h](flash__img_8h.md)>`

Verify flash memory length bytes integrity from a flash area.

The start point is indicated by an offset value.

The function is enabled via CONFIG\_IMG\_ENABLE\_IMAGE\_CHECK Kconfig options.

Parameters
:   | [in] | ctx | context. |
    | --- | --- | --- |
    | [in] | fic | flash img check data. |
    | [in] | area\_id | flash area id of partition where the image should be verified. |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gac6d1d7811516493242b318be2ecd82df)flash\_img\_init()

| int flash\_img\_init | ( | struct [flash\_img\_context](structflash__img__context.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash_img.h](flash__img_8h.md)>`

Initialize context needed for writing the image to the flash.

Parameters
:   | ctx | context to be initialized |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga1b194edcb7e4ae34717d011f08d93e0c)flash\_img\_init\_id()

| int flash\_img\_init\_id | ( | struct [flash\_img\_context](structflash__img__context.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id* ) |

`#include <[flash_img.h](flash__img_8h.md)>`

Initialize context needed for writing the image to the flash.

Parameters
:   | ctx | context to be initialized |
    | --- | --- |
    | area\_id | flash area id of partition where the image should be written |

Returns
:   0 on success, negative errno code on fail

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
