---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structzms__fs.html
original_path: doxygen/html/structzms__fs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zms\_fs Struct Reference

[Operating System Services](group__os__services.md) » [File System Storage](group__file__system__storage.md) » [Zephyr Memory Storage (ZMS)](group__zms.md) » [ZMS data structures](group__zms__data__structures.md)

Zephyr Memory Storage file system structure.
[More...](#details)

`#include <[zms.h](zms_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [offset](#af2dfcc5d0e8eabc5f116e2964668b05f) |
|  | File system offset in flash. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [ate\_wra](#a6c28786531454a050f81981d32ca3640) |
|  | Allocation Table Entry (ATE) write address. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [data\_wra](#a25f2b002e4189ee29432198991061b7a) |
|  | Data write address. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sector\_size](#aae1ffd5eebd0bfb4c898719c221a239f) |
|  | Storage system is split into sectors. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sector\_count](#ad8960c2cee8e03446aca96697c0c9e4a) |
|  | Number of sectors in the file system. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sector\_cycle](#ab3b4551a3007e4b36bfd8a2fc209b543) |
|  | Current cycle counter of the active sector (pointed to by [ate\_wra](#a6c28786531454a050f81981d32ca3640)). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#af46a398f15fbb933d46c0b16283dae16) |
|  | Flag indicating if the file system is initialized. |
| struct [k\_mutex](structk__mutex.md) | [zms\_lock](#af524e7a105749a3dbff41a229c20443b) |
|  | Mutex used to lock flash writes. |
| const struct [device](structdevice.md) \* | [flash\_device](#a2628eaff292518933e037b871179b8ea) |
|  | Flash device runtime structure. |
| const struct [flash\_parameters](structflash__parameters.md) \* | [flash\_parameters](#a19baa487b73542d4075eeb4ea24c303f) |
|  | Flash memory parameters structure. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ate\_size](#a939f1c9100dc9d2efdc163aea61e38a3) |
|  | Size of an Allocation Table Entry. |

## Detailed Description

Zephyr Memory Storage file system structure.

## Field Documentation

## [◆ ](#a939f1c9100dc9d2efdc163aea61e38a3)ate\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) zms\_fs::ate\_size |
| --- |

Size of an Allocation Table Entry.

## [◆ ](#a6c28786531454a050f81981d32ca3640)ate\_wra

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) zms\_fs::ate\_wra |
| --- |

Allocation Table Entry (ATE) write address.

Addresses are stored as [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1):

- high 4 bytes correspond to the sector
- low 4 bytes are the offset in the sector

## [◆ ](#a25f2b002e4189ee29432198991061b7a)data\_wra

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) zms\_fs::data\_wra |
| --- |

Data write address.

## [◆ ](#a2628eaff292518933e037b871179b8ea)flash\_device

| const struct [device](structdevice.md)\* zms\_fs::flash\_device |
| --- |

Flash device runtime structure.

## [◆ ](#a19baa487b73542d4075eeb4ea24c303f)flash\_parameters

| const struct [flash\_parameters](structflash__parameters.md)\* zms\_fs::flash\_parameters |
| --- |

Flash memory parameters structure.

## [◆ ](#af2dfcc5d0e8eabc5f116e2964668b05f)offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) zms\_fs::offset |
| --- |

File system offset in flash.

## [◆ ](#af46a398f15fbb933d46c0b16283dae16)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) zms\_fs::ready |
| --- |

Flag indicating if the file system is initialized.

## [◆ ](#ad8960c2cee8e03446aca96697c0c9e4a)sector\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_fs::sector\_count |
| --- |

Number of sectors in the file system.

## [◆ ](#ab3b4551a3007e4b36bfd8a2fc209b543)sector\_cycle

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) zms\_fs::sector\_cycle |
| --- |

Current cycle counter of the active sector (pointed to by [ate\_wra](#a6c28786531454a050f81981d32ca3640)).

## [◆ ](#aae1ffd5eebd0bfb4c898719c221a239f)sector\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) zms\_fs::sector\_size |
| --- |

Storage system is split into sectors.

The sector size must be a multiple of erase-block-size if the device has erase capabilities

## [◆ ](#af524e7a105749a3dbff41a229c20443b)zms\_lock

| struct [k\_mutex](structk__mutex.md) zms\_fs::zms\_lock |
| --- |

Mutex used to lock flash writes.

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[zms.h](zms_8h_source.md)

- [zms\_fs](structzms__fs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
