---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structosdp__cmd__keyset.html
original_path: doxygen/html/structosdp__cmd__keyset.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd\_keyset Struct Reference

This command transfers an encryption key from the CP to a PD.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#add89930f6c3b88355fcd2f95573080e6) |
|  | Type of keys: |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [length](#a673a4897ae2ff6aa9b88af6440fdc5a6) |
|  | Number of bytes of key data - (Key Length in bits + 7) / 8. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#af85adb3e9c4f73a91fb7a430ff17f6df) [32] |
|  | Key data. |

## Detailed Description

This command transfers an encryption key from the CP to a PD.

Parameters
:   | [type](#add89930f6c3b88355fcd2f95573080e6) | Type of keys:  - 0x01 – Secure Channel Base Key |
    | --- | --- |
    | [length](#a673a4897ae2ff6aa9b88af6440fdc5a6) | Number of bytes of key data - (Key Length in bits + 7) / 8 |
    | [data](#af85adb3e9c4f73a91fb7a430ff17f6df) | Key data |

## Field Documentation

## [◆ ](#af85adb3e9c4f73a91fb7a430ff17f6df)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_keyset::data[32] |
| --- |

Key data.

## [◆ ](#a673a4897ae2ff6aa9b88af6440fdc5a6)length

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_keyset::length |
| --- |

Number of bytes of key data - (Key Length in bits + 7) / 8.

## [◆ ](#add89930f6c3b88355fcd2f95573080e6)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) osdp\_cmd\_keyset::type |
| --- |

Type of keys:

- 0x01 – Secure Channel Base Key

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd\_keyset](structosdp__cmd__keyset.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
