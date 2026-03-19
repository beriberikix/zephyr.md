---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfs__mgmt__hash__checksum__group.html
original_path: doxygen/html/structfs__mgmt__hash__checksum__group.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_mgmt\_hash\_checksum\_group Struct Reference

A collection of handlers for an entire hash/checksum group.
[More...](#details)

`#include <[fs_mgmt_hash_checksum.h](fs__mgmt__hash__checksum_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a620d92183c78b36ad83793b9ceb9d098) |
|  | Entry list node. |
| const char \* | [group\_name](#a5f55c7a9e8905b3ca497cc4711527a2a) |
|  | Array of handlers; one entry per name. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [byte\_string](#aa9bb8702720e6a8287ec6c88da46afff) |
|  | Byte string or numerical output. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [output\_size](#a8f6ef7d183c6b41c067b2a8544e79e7e) |
|  | Size (in bytes) of output. |
| [fs\_mgmt\_hash\_checksum\_handler\_fn](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62) | [function](#a003712f5384e918e5d7d51d9b7acfcb4) |
|  | Hash/checksum function pointer. |

## Detailed Description

A collection of handlers for an entire hash/checksum group.

## Field Documentation

## [◆ ](#aa9bb8702720e6a8287ec6c88da46afff)byte\_string

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) fs\_mgmt\_hash\_checksum\_group::byte\_string |
| --- |

Byte string or numerical output.

## [◆ ](#a003712f5384e918e5d7d51d9b7acfcb4)function

| [fs\_mgmt\_hash\_checksum\_handler\_fn](fs__mgmt__hash__checksum_8h.md#a1a3db209871cb21f90c7feb5fda4db62) fs\_mgmt\_hash\_checksum\_group::function |
| --- |

Hash/checksum function pointer.

## [◆ ](#a5f55c7a9e8905b3ca497cc4711527a2a)group\_name

| const char\* fs\_mgmt\_hash\_checksum\_group::group\_name |
| --- |

Array of handlers; one entry per name.

## [◆ ](#a620d92183c78b36ad83793b9ceb9d098)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) fs\_mgmt\_hash\_checksum\_group::node |
| --- |

Entry list node.

## [◆ ](#a8f6ef7d183c6b41c067b2a8544e79e7e)output\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fs\_mgmt\_hash\_checksum\_group::output\_size |
| --- |

Size (in bytes) of output.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/mcumgr/grp/fs\_mgmt/[fs\_mgmt\_hash\_checksum.h](fs__mgmt__hash__checksum_8h_source.md)

- [fs\_mgmt\_hash\_checksum\_group](structfs__mgmt__hash__checksum__group.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
