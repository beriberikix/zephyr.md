---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/memmap_8h.html
original_path: doxygen/html/memmap_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

memmap.h File Reference

[Go to the source code of this file.](memmap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [x86\_memmap\_entry](structx86__memmap__entry.md) |
| struct | [x86\_memmap\_exclusion](structx86__memmap__exclusion.md) |

| Enumerations | |
| --- | --- |
| enum | [x86\_memmap\_source](#ae4f3b51d56ed1ddb36a78d0238a8bdc5) { [X86\_MEMMAP\_SOURCE\_DEFAULT](#ae4f3b51d56ed1ddb36a78d0238a8bdc5a68b60d7825f63c9a7f973a5ba63b7fe9) , [X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MEM](#ae4f3b51d56ed1ddb36a78d0238a8bdc5a7d9550deb6b27b6c720cbcb7dd48dc63) , [X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MMAP](#ae4f3b51d56ed1ddb36a78d0238a8bdc5a65183e6b869d16a0b1daf4b5d0c9b3f5) , [X86\_MEMMAP\_SOURCE\_MANUAL](#ae4f3b51d56ed1ddb36a78d0238a8bdc5a4718538763c5b75bb121fdeb8b2b5ffc) } |
| enum | [x86\_memmap\_entry\_type](#af5da5d5ee62dc74e3ea4bf1f5db757ef) {     [X86\_MEMMAP\_ENTRY\_UNUSED](#af5da5d5ee62dc74e3ea4bf1f5db757efa7639598e6c11cde301d4aacea99b3fd6) , [X86\_MEMMAP\_ENTRY\_RAM](#af5da5d5ee62dc74e3ea4bf1f5db757efae6c7073699a49c3e74fb91c45ea24a0a) , [X86\_MEMMAP\_ENTRY\_ACPI](#af5da5d5ee62dc74e3ea4bf1f5db757efaa2f86b365795a0f0fc419121f2bdf417) , [X86\_MEMMAP\_ENTRY\_NVS](#af5da5d5ee62dc74e3ea4bf1f5db757efa1ec11c2afcb03537e072273a6fbb2e61) ,     [X86\_MEMMAP\_ENTRY\_DEFECTIVE](#af5da5d5ee62dc74e3ea4bf1f5db757efa5e3f2de2b434f036b6fff8aaa63e55dd) , [X86\_MEMMAP\_ENTRY\_UNKNOWN](#af5da5d5ee62dc74e3ea4bf1f5db757efad26cdfad068828bce9185ebb9908b368)   } |

| Variables | |
| --- | --- |
| enum [x86\_memmap\_source](#ae4f3b51d56ed1ddb36a78d0238a8bdc5) | [x86\_memmap\_source](#a14c4d7f538e9ae4f993c75e5e0410bf9) |
| struct [x86\_memmap\_entry](structx86__memmap__entry.md) | [x86\_memmap](#a8b8229cdb36bf23f8257958fda84be4b) [] |
| struct [x86\_memmap\_exclusion](structx86__memmap__exclusion.md) | [x86\_memmap\_exclusions](#ab1723f77a7879fd1cc4723091241d099) [] |
| int | [x86\_nr\_memmap\_exclusions](#abb046960eea27faacf7a08d18b9a57eb) |

## Enumeration Type Documentation

## [◆ ](#af5da5d5ee62dc74e3ea4bf1f5db757ef)x86\_memmap\_entry\_type

| enum [x86\_memmap\_entry\_type](#af5da5d5ee62dc74e3ea4bf1f5db757ef) |
| --- |

| Enumerator | |
| --- | --- |
| X86\_MEMMAP\_ENTRY\_UNUSED |  |
| X86\_MEMMAP\_ENTRY\_RAM |  |
| X86\_MEMMAP\_ENTRY\_ACPI |  |
| X86\_MEMMAP\_ENTRY\_NVS |  |
| X86\_MEMMAP\_ENTRY\_DEFECTIVE |  |
| X86\_MEMMAP\_ENTRY\_UNKNOWN |  |

## [◆ ](#ae4f3b51d56ed1ddb36a78d0238a8bdc5)x86\_memmap\_source

| enum [x86\_memmap\_source](#ae4f3b51d56ed1ddb36a78d0238a8bdc5) |
| --- |

| Enumerator | |
| --- | --- |
| X86\_MEMMAP\_SOURCE\_DEFAULT |  |
| X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MEM |  |
| X86\_MEMMAP\_SOURCE\_MULTIBOOT\_MMAP |  |
| X86\_MEMMAP\_SOURCE\_MANUAL |  |

## Variable Documentation

## [◆ ](#a8b8229cdb36bf23f8257958fda84be4b)x86\_memmap

| | struct [x86\_memmap\_entry](structx86__memmap__entry.md) x86\_memmap[] | | --- | | extern |
| --- | --- | --- |

## [◆ ](#ab1723f77a7879fd1cc4723091241d099)x86\_memmap\_exclusions

| | struct [x86\_memmap\_exclusion](structx86__memmap__exclusion.md) x86\_memmap\_exclusions[] | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a14c4d7f538e9ae4f993c75e5e0410bf9)x86\_memmap\_source

| | enum [x86\_memmap\_source](#ae4f3b51d56ed1ddb36a78d0238a8bdc5) [x86\_memmap\_source](#ae4f3b51d56ed1ddb36a78d0238a8bdc5) | | --- | | extern |
| --- | --- | --- |

## [◆ ](#abb046960eea27faacf7a08d18b9a57eb)x86\_nr\_memmap\_exclusions

| | int x86\_nr\_memmap\_exclusions | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [memmap.h](memmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
