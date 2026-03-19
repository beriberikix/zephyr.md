---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcuboot_8h.html
original_path: doxygen/html/mcuboot_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcuboot.h File Reference

MCUboot public API for MCUboot control of image boot process.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](mcuboot_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md) |
|  | MCUboot image header representation for image version. [More...](structmcuboot__img__sem__ver.md#details) |
| struct | [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md) |
|  | Model for the MCUboot image header as of version 1. [More...](structmcuboot__img__header__v1.md#details) |
| struct | [mcuboot\_img\_header](structmcuboot__img__header.md) |
|  | Model for the MCUBoot image header. [More...](structmcuboot__img__header.md#details) |

| Macros | |
| --- | --- |
| #define | [BOOT\_SWAP\_TYPE\_NONE](group__mcuboot__api.md#gabb6482b898e8307074d8aef01b1102b7)   1 |
|  | Attempt to boot the contents of slot 0. |
| #define | [BOOT\_SWAP\_TYPE\_TEST](group__mcuboot__api.md#ga3aa4415c47231a120c4cab455ea0beef)   2 |
|  | Swap to slot 1. |
| #define | [BOOT\_SWAP\_TYPE\_PERM](group__mcuboot__api.md#ga09ebc9ba28e294e71388480bb9e4f677)   3 |
|  | Swap to slot 1, and permanently switch to booting its contents. |
| #define | [BOOT\_SWAP\_TYPE\_REVERT](group__mcuboot__api.md#ga8ca7bd765c6ab669db0774c0b0122494)   4 |
|  | Swap back to alternate slot. |
| #define | [BOOT\_SWAP\_TYPE\_FAIL](group__mcuboot__api.md#ga28cb43e6bfacdd285d95751cda80de13)   5 |
|  | Swap failed because image to be run is not valid. |
| #define | [BOOT\_IMG\_VER\_STRLEN\_MAX](group__mcuboot__api.md#ga1e697351ff503f9a53b17916e63cce06)   25 /\* 255.255.65535.4294967295\0 \*/ |
| #define | [SWAP\_USING\_OFFSET\_SECTOR\_UPDATE\_BEGIN](group__mcuboot__api.md#ga68aeea51973f08c06dc664f02b935ff7)   1 |
|  | Sector at which firmware update should be placed by application in swap using offset mode. |
| #define | [BOOT\_UPGRADE\_TEST](group__mcuboot__api.md#ga9ed69fcd1ebf57cc356ce2bb835853f7)   0 |
|  | Boot upgrade request modes. |
| #define | [BOOT\_UPGRADE\_PERMANENT](group__mcuboot__api.md#gab48b79d246df6ebc712040c5ee00aa73)   1 |

| Functions | |
| --- | --- |
| int | [boot\_read\_bank\_header](group__mcuboot__api.md#ga652ffad55e2917c62a62f6463935fe59) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id, struct [mcuboot\_img\_header](structmcuboot__img__header.md) \*header, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) header\_size) |
|  | Read the MCUboot image header information from an image bank. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [boot\_fetch\_active\_slot](group__mcuboot__api.md#ga4ce6857cd516204fba5f7fb5c1c6272c) (void) |
|  | Get the flash area id for the active image slot. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [boot\_is\_img\_confirmed](group__mcuboot__api.md#ga2eadd700521a8b94dea3d3d04c9f5bd8) (void) |
|  | Check if the currently running image is confirmed as OK. |
| int | [boot\_write\_img\_confirmed](group__mcuboot__api.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72) (void) |
|  | Marks the currently running image as confirmed. |
| int | [boot\_write\_img\_confirmed\_multi](group__mcuboot__api.md#gaa0f2410f520ef57e6d793c169639a6f8) (int image\_index) |
|  | Marks the image with the given index in the primary slot as confirmed. |
| int | [mcuboot\_swap\_type](group__mcuboot__api.md#gaa0ce517ba1c0b21c4898762fab959b12) (void) |
|  | Determines the action, if any, that mcuboot will take on the next reboot. |
| int | [mcuboot\_swap\_type\_multi](group__mcuboot__api.md#ga1e679c6fefe7deaaed9a2265ce69cf1e) (int image\_index) |
|  | Determines the action, if any, that mcuboot will take on the next reboot. |
| int | [boot\_request\_upgrade](group__mcuboot__api.md#gad47f2356938a7b5acf8e0bbe4d9e4494) (int permanent) |
|  | Marks the image in slot 1 as pending. |
| int | [boot\_request\_upgrade\_multi](group__mcuboot__api.md#gae9e0e43663c3671aa4b4df6d30511d39) (int image\_index, int permanent) |
|  | Marks the image with the given index in the secondary slot as pending. |
| int | [boot\_erase\_img\_bank](group__mcuboot__api.md#ga03b691762d00e4cab6a5bd91979d8d80) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Erase the image Bank. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [boot\_get\_area\_trailer\_status\_offset](group__mcuboot__api.md#ga6fa12d4058bbb78b7d8f35b436f0009c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Get the offset of the status in the image bank. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [boot\_get\_trailer\_status\_offset](group__mcuboot__api.md#ga7b4443f339f2935895f01dfb80c6b460) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) area\_size) |
|  | Get the offset of the status from an image bank size. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [boot\_get\_image\_start\_offset](group__mcuboot__api.md#ga85c68e5758724d541586f8a6d61869d0) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Get the offset of the image header, this should be used in swap using offset mode to account for the secondary slot data starting in the first or second sector, depending upon the current state. |

## Detailed Description

MCUboot public API for MCUboot control of image boot process.

The header declares API functions that can be used to get information on and select application images for boot.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dfu](dir_b8bb0fd55a94366ea1f20beca08b160d.md)
- [mcuboot.h](mcuboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
