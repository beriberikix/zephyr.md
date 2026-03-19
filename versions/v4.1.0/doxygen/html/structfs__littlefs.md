---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structfs__littlefs.html
original_path: doxygen/html/structfs__littlefs.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fs\_littlefs Struct Reference

Filesystem info structure for LittleFS mount.
[More...](#details)

`#include <[littlefs.h](littlefs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct lfs\_config | [cfg](#ab9b4cd8ce0aedfd071ea184d92b1224a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [read\_buffer](#ac1b102a94e6db2dfb4ca0d0bee5a561e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [prog\_buffer](#a239d1ac90cc0de3a9cca766d41180def) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | [lookahead\_buffer](#a7cd0dcd14e83138ba2ed698f55377e49) [CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE/[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))] |
| struct lfs | [lfs](#a3a1902a64f78b65743786d154b435439) |
| void \* | [backend](#a0ebbf427f161722fc269573d86e562c5) |
| struct [k\_mutex](structk__mutex.md) | [mutex](#a337c24352a8f39c1d1f55682126341b5) |

## Detailed Description

Filesystem info structure for LittleFS mount.

## Field Documentation

## [◆ ](#a0ebbf427f161722fc269573d86e562c5)backend

| void\* fs\_littlefs::backend |
| --- |

## [◆ ](#ab9b4cd8ce0aedfd071ea184d92b1224a)cfg

| struct lfs\_config fs\_littlefs::cfg |
| --- |

## [◆ ](#a3a1902a64f78b65743786d154b435439)lfs

| struct lfs fs\_littlefs::lfs |
| --- |

## [◆ ](#a7cd0dcd14e83138ba2ed698f55377e49)lookahead\_buffer

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)\* fs\_littlefs::lookahead\_buffer[CONFIG\_FS\_LITTLEFS\_LOOKAHEAD\_SIZE/[sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))] |
| --- |

## [◆ ](#a337c24352a8f39c1d1f55682126341b5)mutex

| struct [k\_mutex](structk__mutex.md) fs\_littlefs::mutex |
| --- |

## [◆ ](#a239d1ac90cc0de3a9cca766d41180def)prog\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* fs\_littlefs::prog\_buffer |
| --- |

## [◆ ](#ac1b102a94e6db2dfb4ca0d0bee5a561e)read\_buffer

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* fs\_littlefs::read\_buffer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/fs/[littlefs.h](littlefs_8h_source.md)

- [fs\_littlefs](structfs__littlefs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
