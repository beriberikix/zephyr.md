---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structext2__cfg.html
original_path: doxygen/html/structext2__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ext2\_cfg Struct Reference

Configuration used to format ext2 file system.
[More...](#details)

`#include <[ext2.h](ext2_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [block\_size](#a3eb5587725f3fee4dd8ea86a7077e662) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fs\_size](#ab8b546e8256994362261085fb4e826df) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [bytes\_per\_inode](#a04309de819dc1b31a7578667c82678b6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uuid](#ad11fad3e7fd7088263b578babd60c77d) [16] |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [volume\_name](#a2f0bbc643995eb206f59625dff84b4e9) [17] |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [set\_uuid](#a63d3fca7ab9c60da4457569c51e3a511) |

## Detailed Description

Configuration used to format ext2 file system.

If a field is set to 0 then default value is used. (In volume name the first cell of an array must be 0 to use default value.)

Parameters
:   | [block\_size](#a3eb5587725f3fee4dd8ea86a7077e662) | Requested size of block. |
    | --- | --- |
    | [fs\_size](#ab8b546e8256994362261085fb4e826df) | Requested size of file system. If 0 then whole available memory is used. |
    | [bytes\_per\_inode](#a04309de819dc1b31a7578667c82678b6) | Requested memory for one inode. It is used to calculate number of inodes in created file system. |
    | [uuid](#ad11fad3e7fd7088263b578babd60c77d) | UUID for created file system. Used when set\_uuid is true. |
    | [volume\_name](#a2f0bbc643995eb206f59625dff84b4e9) | Name for created file system. |
    | [set\_uuid](#a63d3fca7ab9c60da4457569c51e3a511) | If true then UUID from that structure is used in created file system. If false then UUID (ver4) is generated. |

## Field Documentation

## [◆ ](#a3eb5587725f3fee4dd8ea86a7077e662)block\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ext2\_cfg::block\_size |
| --- |

## [◆ ](#a04309de819dc1b31a7578667c82678b6)bytes\_per\_inode

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ext2\_cfg::bytes\_per\_inode |
| --- |

## [◆ ](#ab8b546e8256994362261085fb4e826df)fs\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ext2\_cfg::fs\_size |
| --- |

## [◆ ](#a63d3fca7ab9c60da4457569c51e3a511)set\_uuid

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ext2\_cfg::set\_uuid |
| --- |

## [◆ ](#ad11fad3e7fd7088263b578babd60c77d)uuid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ext2\_cfg::uuid[16] |
| --- |

## [◆ ](#a2f0bbc643995eb206f59625dff84b4e9)volume\_name

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ext2\_cfg::volume\_name[17] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[ext2.h](ext2_8h_source.md)

- [ext2\_cfg](structext2__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
