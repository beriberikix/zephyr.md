---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mcuboot__api.html
original_path: doxygen/html/group__mcuboot__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUboot image control API

[Third-party](group__third__party.md)

MCUboot public API for MCUboot control of image boot process.
[More...](#details)

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
| #define | [BOOT\_SWAP\_TYPE\_NONE](#gabb6482b898e8307074d8aef01b1102b7)   1 |
|  | Attempt to boot the contents of slot 0. |
| #define | [BOOT\_SWAP\_TYPE\_TEST](#ga3aa4415c47231a120c4cab455ea0beef)   2 |
|  | Swap to slot 1. |
| #define | [BOOT\_SWAP\_TYPE\_PERM](#ga09ebc9ba28e294e71388480bb9e4f677)   3 |
|  | Swap to slot 1, and permanently switch to booting its contents. |
| #define | [BOOT\_SWAP\_TYPE\_REVERT](#ga8ca7bd765c6ab669db0774c0b0122494)   4 |
|  | Swap back to alternate slot. |
| #define | [BOOT\_SWAP\_TYPE\_FAIL](#ga28cb43e6bfacdd285d95751cda80de13)   5 |
|  | Swap failed because image to be run is not valid. |
| #define | [BOOT\_IMG\_VER\_STRLEN\_MAX](#ga1e697351ff503f9a53b17916e63cce06)   25 /\* 255.255.65535.4294967295\0 \*/ |
| #define | [BOOT\_UPGRADE\_TEST](#ga9ed69fcd1ebf57cc356ce2bb835853f7)   0 |
|  | Boot upgrade request modes. |
| #define | [BOOT\_UPGRADE\_PERMANENT](#gab48b79d246df6ebc712040c5ee00aa73)   1 |

| Functions | |
| --- | --- |
| int | [boot\_read\_bank\_header](#ga652ffad55e2917c62a62f6463935fe59) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id, struct [mcuboot\_img\_header](structmcuboot__img__header.md) \*header, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) header\_size) |
|  | Read the MCUboot image header information from an image bank. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [boot\_is\_img\_confirmed](#ga2eadd700521a8b94dea3d3d04c9f5bd8) (void) |
|  | Check if the currently running image is confirmed as OK. |
| int | [boot\_write\_img\_confirmed](#ga95ccc9e1c7460fec16b9ce9ac8ad7a72) (void) |
|  | Marks the currently running image as confirmed. |
| int | [boot\_write\_img\_confirmed\_multi](#gaa0f2410f520ef57e6d793c169639a6f8) (int image\_index) |
|  | Marks the image with the given index in the primary slot as confirmed. |
| int | [mcuboot\_swap\_type](#gaa0ce517ba1c0b21c4898762fab959b12) (void) |
|  | Determines the action, if any, that mcuboot will take on the next reboot. |
| int | [mcuboot\_swap\_type\_multi](#ga1e679c6fefe7deaaed9a2265ce69cf1e) (int image\_index) |
|  | Determines the action, if any, that mcuboot will take on the next reboot. |
| int | [boot\_request\_upgrade](#gad47f2356938a7b5acf8e0bbe4d9e4494) (int permanent) |
|  | Marks the image in slot 1 as pending. |
| int | [boot\_request\_upgrade\_multi](#gae9e0e43663c3671aa4b4df6d30511d39) (int image\_index, int permanent) |
|  | Marks the image with the given index in the secondary slot as pending. |
| int | [boot\_erase\_img\_bank](#ga03b691762d00e4cab6a5bd91979d8d80) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Erase the image Bank. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [boot\_get\_area\_trailer\_status\_offset](#ga6fa12d4058bbb78b7d8f35b436f0009c) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id) |
|  | Get the offset of the status in the image bank. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [boot\_get\_trailer\_status\_offset](#ga7b4443f339f2935895f01dfb80c6b460) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) area\_size) |
|  | Get the offset of the status from an image bank size. |

## Detailed Description

MCUboot public API for MCUboot control of image boot process.

## Macro Definition Documentation

## [◆ ](#ga1e697351ff503f9a53b17916e63cce06)BOOT\_IMG\_VER\_STRLEN\_MAX

| #define BOOT\_IMG\_VER\_STRLEN\_MAX   25 /\* 255.255.65535.4294967295\0 \*/ |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

## [◆ ](#ga28cb43e6bfacdd285d95751cda80de13)BOOT\_SWAP\_TYPE\_FAIL

| #define BOOT\_SWAP\_TYPE\_FAIL   5 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Swap failed because image to be run is not valid.

## [◆ ](#gabb6482b898e8307074d8aef01b1102b7)BOOT\_SWAP\_TYPE\_NONE

| #define BOOT\_SWAP\_TYPE\_NONE   1 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Attempt to boot the contents of slot 0.

## [◆ ](#ga09ebc9ba28e294e71388480bb9e4f677)BOOT\_SWAP\_TYPE\_PERM

| #define BOOT\_SWAP\_TYPE\_PERM   3 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Swap to slot 1, and permanently switch to booting its contents.

## [◆ ](#ga8ca7bd765c6ab669db0774c0b0122494)BOOT\_SWAP\_TYPE\_REVERT

| #define BOOT\_SWAP\_TYPE\_REVERT   4 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Swap back to alternate slot.

A confirm changes this state to NONE.

## [◆ ](#ga3aa4415c47231a120c4cab455ea0beef)BOOT\_SWAP\_TYPE\_TEST

| #define BOOT\_SWAP\_TYPE\_TEST   2 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Swap to slot 1.

Absent a confirm command, revert back on next boot.

## [◆ ](#gab48b79d246df6ebc712040c5ee00aa73)BOOT\_UPGRADE\_PERMANENT

| #define BOOT\_UPGRADE\_PERMANENT   1 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

## [◆ ](#ga9ed69fcd1ebf57cc356ce2bb835853f7)BOOT\_UPGRADE\_TEST

| #define BOOT\_UPGRADE\_TEST   0 |
| --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Boot upgrade request modes.

## Function Documentation

## [◆ ](#ga03b691762d00e4cab6a5bd91979d8d80)boot\_erase\_img\_bank()

| int boot\_erase\_img\_bank | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Erase the image Bank.

Parameters
:   | area\_id | [flash\_area](structflash__area.md "Flash partition.") ID of image bank to be erased. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga6fa12d4058bbb78b7d8f35b436f0009c)boot\_get\_area\_trailer\_status\_offset()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) boot\_get\_area\_trailer\_status\_offset | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Get the offset of the status in the image bank.

Parameters
:   | area\_id | [flash\_area](structflash__area.md "Flash partition.") ID of image bank to get the status offset |
    | --- | --- |

Returns
:   a positive offset on success, negative errno code on fail

## [◆ ](#ga7b4443f339f2935895f01dfb80c6b460)boot\_get\_trailer\_status\_offset()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) boot\_get\_trailer\_status\_offset | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *area\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Get the offset of the status from an image bank size.

Parameters
:   | area\_size | size of image bank |
    | --- | --- |

Returns
:   offset of the status. When negative the status will not fit the given size

## [◆ ](#ga2eadd700521a8b94dea3d3d04c9f5bd8)boot\_is\_img\_confirmed()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) boot\_is\_img\_confirmed | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Check if the currently running image is confirmed as OK.

MCUboot can perform "test" upgrades. When these occur, a new firmware image is installed and booted, but the old version will be reverted at the next reset unless the new image explicitly marks itself OK.

This routine can be used to check if the currently running image has been marked as OK.

Returns
:   True if the image is confirmed as OK, false otherwise.

See also
:   [boot\_write\_img\_confirmed()](#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)

## [◆ ](#ga652ffad55e2917c62a62f6463935fe59)boot\_read\_bank\_header()

| int boot\_read\_bank\_header | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *area\_id*, |
| --- | --- | --- | --- |
|  |  | struct [mcuboot\_img\_header](structmcuboot__img__header.md) \* | *header*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *header\_size* ) |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Read the MCUboot image header information from an image bank.

This attempts to parse the image header, From the start of the *area\_id* image.

Parameters
:   | area\_id | [flash\_area](structflash__area.md "Flash partition.") ID of image bank which stores the image. |
    | --- | --- |
    | header | On success, the returned header information is available in this structure. |
    | header\_size | Size of the header structure passed by the caller. If this is not large enough to contain all of the necessary information, an error is returned. |

Returns
:   Zero on success, a negative value on error.

## [◆ ](#gad47f2356938a7b5acf8e0bbe4d9e4494)boot\_request\_upgrade()

| int boot\_request\_upgrade | ( | int | *permanent* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Marks the image in slot 1 as pending.

On the next reboot, the system will perform a boot of the slot 1 image.

Parameters
:   | permanent | Whether the image should be used permanently or only tested once: BOOT\_UPGRADE\_TEST=run image once, then confirm or revert. BOOT\_UPGRADE\_PERMANENT=run image forever. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gae9e0e43663c3671aa4b4df6d30511d39)boot\_request\_upgrade\_multi()

| int boot\_request\_upgrade\_multi | ( | int | *image\_index*, |
| --- | --- | --- | --- |
|  |  | int | *permanent* ) |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Marks the image with the given index in the secondary slot as pending.

On the next reboot, the system will perform a boot of the secondary slot image.

Parameters
:   | image\_index | Image pair index. |
    | --- | --- |
    | permanent | Whether the image should be used permanently or only tested once: BOOT\_UPGRADE\_TEST=run image once, then confirm or revert. BOOT\_UPGRADE\_PERMANENT=run image forever. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)boot\_write\_img\_confirmed()

| int boot\_write\_img\_confirmed | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Marks the currently running image as confirmed.

This routine attempts to mark the currently running firmware image as OK, which will install it permanently, preventing MCUboot from reverting it for an older image at the next reset.

This routine is safe to call if the current image has already been confirmed. It will return a successful result in this case.

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaa0f2410f520ef57e6d793c169639a6f8)boot\_write\_img\_confirmed\_multi()

| int boot\_write\_img\_confirmed\_multi | ( | int | *image\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Marks the image with the given index in the primary slot as confirmed.

This routine attempts to mark the firmware image in the primary slot as OK, which will install it permanently, preventing MCUboot from reverting it for an older image at the next reset.

This routine is safe to call if the current image has already been confirmed. It will return a successful result in this case.

Parameters
:   | image\_index | Image pair index. |
    | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaa0ce517ba1c0b21c4898762fab959b12)mcuboot\_swap\_type()

| int mcuboot\_swap\_type | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Determines the action, if any, that mcuboot will take on the next reboot.

Returns
:   a BOOT\_SWAP\_TYPE\_[...] constant on success, negative errno code on fail.

## [◆ ](#ga1e679c6fefe7deaaed9a2265ce69cf1e)mcuboot\_swap\_type\_multi()

| int mcuboot\_swap\_type\_multi | ( | int | *image\_index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mcuboot.h](mcuboot_8h.md)>`

Determines the action, if any, that mcuboot will take on the next reboot.

Parameters
:   | image\_index | Image pair index. |
    | --- | --- |

Returns
:   a BOOT\_SWAP\_TYPE\_[...] constant on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
