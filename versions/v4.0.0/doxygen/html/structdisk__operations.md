---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdisk__operations.html
original_path: doxygen/html/structdisk__operations.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

disk\_operations Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Disk Driver Interface](group__disk__driver__interface.md)

Disk operations.
[More...](#details)

`#include <[disk.h](disk_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [init](#ad944962a397c3427b4b6331518d6eb8b) )(struct [disk\_info](structdisk__info.md) \*disk) |
| int(\* | [status](#acd7d82f4d65ae8badd5005ae3a21bf44) )(struct [disk\_info](structdisk__info.md) \*disk) |
| int(\* | [read](#a2899499e982a861f41d02fa2e856b753) )(struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
| int(\* | [write](#ad74bec53a1ef7dc159b1ca90dd3c5a91) )(struct [disk\_info](structdisk__info.md) \*disk, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
| int(\* | [ioctl](#a890f3f9e912b7e0b56fa105f82608f97) )(struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff) |

## Detailed Description

Disk operations.

## Field Documentation

## [◆ ](#ad944962a397c3427b4b6331518d6eb8b)init

| int(\* disk\_operations::init) (struct [disk\_info](structdisk__info.md) \*disk) |
| --- |

## [◆ ](#a890f3f9e912b7e0b56fa105f82608f97)ioctl

| int(\* disk\_operations::ioctl) (struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buff) |
| --- |

## [◆ ](#a2899499e982a861f41d02fa2e856b753)read

| int(\* disk\_operations::read) (struct [disk\_info](structdisk__info.md) \*disk, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
| --- |

## [◆ ](#acd7d82f4d65ae8badd5005ae3a21bf44)status

| int(\* disk\_operations::status) (struct [disk\_info](structdisk__info.md) \*disk) |
| --- |

## [◆ ](#ad74bec53a1ef7dc159b1ca90dd3c5a91)write

| int(\* disk\_operations::write) (struct [disk\_info](structdisk__info.md) \*disk, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data\_buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) start\_sector, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_sector) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[disk.h](disk_8h_source.md)

- [disk\_operations](structdisk__operations.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
