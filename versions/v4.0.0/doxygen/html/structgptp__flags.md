---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structgptp__flags.html
original_path: doxygen/html/structgptp__flags.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp\_flags Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [gPTP support](group__gptp.md)

gPTP message flags
[More...](#details)

`#include <[gptp.h](gptp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [octets](#a90b2862e78ece1b9b7f5109f5cd5f0fd) [2] |  |
|  | Byte access. [More...](#a90b2862e78ece1b9b7f5109f5cd5f0fd) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [all](#a36871fbae0484379b00c415affdb3f9d) |  |
|  | Whole field access. [More...](#a36871fbae0484379b00c415affdb3f9d) |
| }; |  |

## Detailed Description

gPTP message flags

## Field Documentation

## [◆ ](#a525f7db2fc70195a8edc3dc0e46b5798)[union]

| union { ... } [gptp\_flags](structgptp__flags.md) |
| --- |

## [◆ ](#a36871fbae0484379b00c415affdb3f9d)all

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) gptp\_flags::all |
| --- |

Whole field access.

## [◆ ](#a90b2862e78ece1b9b7f5109f5cd5f0fd)octets

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) gptp\_flags::octets[2] |
| --- |

Byte access.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[gptp.h](gptp_8h_source.md)

- [gptp\_flags](structgptp__flags.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
