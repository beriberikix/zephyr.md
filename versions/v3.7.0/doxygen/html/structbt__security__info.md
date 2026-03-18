---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__security__info.html
original_path: doxygen/html/structbt__security__info.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_security\_info Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

Security Info Structure.
[More...](#details)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [level](#a7b18849fad25b3f2da6b8c85a56d86e1) |
|  | Security Level. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [enc\_key\_size](#a6567ffb82b7fa8093cc57ef4662873ba) |
|  | Encryption Key Size. |
| enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) | [flags](#a99cb4af08bfa1dab182821d956368526) |
|  | Flags. |

## Detailed Description

Security Info Structure.

## Field Documentation

## [◆ ](#a6567ffb82b7fa8093cc57ef4662873ba)enc\_key\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_security\_info::enc\_key\_size |
| --- |

Encryption Key Size.

## [◆ ](#a99cb4af08bfa1dab182821d956368526)flags

| enum [bt\_security\_flag](group__bt__conn.md#ga2f8712bbf3410de5cbe6ce489fe30e5e) bt\_security\_info::flags |
| --- |

Flags.

## [◆ ](#a7b18849fad25b3f2da6b8c85a56d86e1)level

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_security\_info::level |
| --- |

Security Level.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_security\_info](structbt__security__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
