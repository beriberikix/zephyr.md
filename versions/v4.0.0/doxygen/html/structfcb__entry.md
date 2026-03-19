---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfcb__entry.html
original_path: doxygen/html/structfcb__entry.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fcb\_entry Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Flash Circular Buffer (FCB)](group__fcb.md) » [Flash Circular Buffer Data Structures](group__fcb__data__structures.md)

FCB entry info structure.
[More...](#details)

`#include <[fcb.h](fcb_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [flash\_sector](structflash__sector.md) \* | [fe\_sector](#aa564f9f79012beb20265bc5e85816fea) |
|  | Pointer to info about sector where data are placed. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fe\_elem\_off](#a6d01cb2107949bf4f0a2779c9781261f) |
|  | Offset from the start of the sector to beginning of element. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fe\_data\_off](#a82cba5933875498c804f31722a6e90f9) |
|  | Offset from the start of the sector to the start of element. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fe\_data\_len](#aa207d21d51bc2c7aa838ca9dc3b52be7) |
|  | Size of data area in fcb entry. |

## Detailed Description

FCB entry info structure.

This data structure describes the element location in the flash.

You would use it to figure out what parameters to pass to [flash\_area\_read()](group__flash__area__api.md#ga7c55704b0c0061a4715470676114b127 "Read flash area data.") to read element contents. Or to [flash\_area\_write()](group__flash__area__api.md#gaa56052f8d6bf4f6966752bc21f5cceb8 "Write data to flash area.") when adding a new element. Entry location is pointer to area (within fcb->f\_sectors), and offset within that area.

## Field Documentation

## [◆ ](#aa207d21d51bc2c7aa838ca9dc3b52be7)fe\_data\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) fcb\_entry::fe\_data\_len |
| --- |

Size of data area in fcb entry.

## [◆ ](#a82cba5933875498c804f31722a6e90f9)fe\_data\_off

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fcb\_entry::fe\_data\_off |
| --- |

Offset from the start of the sector to the start of element.

## [◆ ](#a6d01cb2107949bf4f0a2779c9781261f)fe\_elem\_off

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fcb\_entry::fe\_elem\_off |
| --- |

Offset from the start of the sector to beginning of element.

## [◆ ](#aa564f9f79012beb20265bc5e85816fea)fe\_sector

| struct [flash\_sector](structflash__sector.md)\* fcb\_entry::fe\_sector |
| --- |

Pointer to info about sector where data are placed.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[fcb.h](fcb_8h_source.md)

- [fcb\_entry](structfcb__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
