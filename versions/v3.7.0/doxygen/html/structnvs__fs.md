---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnvs__fs.html
original_path: doxygen/html/structnvs__fs.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nvs\_fs Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Non-volatile Storage (NVS)](group__nvs.md) » [Non-volatile Storage Data Structures](group__nvs__data__structures.md)

Non-volatile Storage File system structure.
[More...](#details)

`#include <[nvs.h](nvs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#a793b43b069d5e7a42963d84423ab5717) |
|  | File system offset in flash. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ate\_wra](#aba5caa7709d58fa018cbb91db085f140) |
|  | Allocation table entry write address. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [data\_wra](#ac6bc3719e803f27fc20de5ebc63d7707) |
|  | Data write address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sector\_size](#a036af291edc8d389b56fcb532e6738df) |
|  | File system is split into sectors, each sector must be multiple of erase-block-size. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sector\_count](#abf8ffaea29e3357ca6e897902fd49a63) |
|  | Number of sectors in the file system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#a2a167bd6a1698d2070dbe65b669ba0f4) |
|  | Flag indicating if the file system is initialized. |
| struct [k\_mutex](structk__mutex.md) | [nvs\_lock](#a6f49bb17819e3b78e0b3c1a1bc578f09) |
|  | Mutex. |
| const struct [device](structdevice.md) \* | [flash\_device](#a02381974223dfbd22fe50b2cfecb7da2) |
|  | Flash device runtime structure. |
| const struct [flash\_parameters](structflash__parameters.md) \* | [flash\_parameters](#a34f769be6fed7c81254501af207147df) |
|  | Flash memory parameters structure. |

## Detailed Description

Non-volatile Storage File system structure.

## Field Documentation

## [◆ ](#aba5caa7709d58fa018cbb91db085f140)ate\_wra

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nvs\_fs::ate\_wra |
| --- |

Allocation table entry write address.

Addresses are stored as [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f):

- high 2 bytes correspond to the sector
- low 2 bytes are the offset in the sector

## [◆ ](#ac6bc3719e803f27fc20de5ebc63d7707)data\_wra

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) nvs\_fs::data\_wra |
| --- |

Data write address.

## [◆ ](#a02381974223dfbd22fe50b2cfecb7da2)flash\_device

| const struct [device](structdevice.md)\* nvs\_fs::flash\_device |
| --- |

Flash device runtime structure.

## [◆ ](#a34f769be6fed7c81254501af207147df)flash\_parameters

| const struct [flash\_parameters](structflash__parameters.md)\* nvs\_fs::flash\_parameters |
| --- |

Flash memory parameters structure.

## [◆ ](#a6f49bb17819e3b78e0b3c1a1bc578f09)nvs\_lock

| struct [k\_mutex](structk__mutex.md) nvs\_fs::nvs\_lock |
| --- |

Mutex.

## [◆ ](#a793b43b069d5e7a42963d84423ab5717)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) nvs\_fs::offset |
| --- |

File system offset in flash.

## [◆ ](#a2a167bd6a1698d2070dbe65b669ba0f4)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) nvs\_fs::ready |
| --- |

Flag indicating if the file system is initialized.

## [◆ ](#abf8ffaea29e3357ca6e897902fd49a63)sector\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) nvs\_fs::sector\_count |
| --- |

Number of sectors in the file system.

## [◆ ](#a036af291edc8d389b56fcb532e6738df)sector\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) nvs\_fs::sector\_size |
| --- |

File system is split into sectors, each sector must be multiple of erase-block-size.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[nvs.h](nvs_8h_source.md)

- [nvs\_fs](structnvs__fs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
