---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbindesc__entry.html
original_path: doxygen/html/structbindesc__entry.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bindesc\_entry Struct Reference

`#include <[bindesc.h](bindesc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tag](#ab040a2e6d5370498f2a689ba172e4112) |
|  | Tag of the entry. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#ad756a440a8dfa9d396258707a1f681e4) |
|  | Length of the descriptor data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#a8cc383c8f7e11caff91912c8c2cc6b41) [] |
|  | Value of the entry. |

## Field Documentation

## [◆ ](#a8cc383c8f7e11caff91912c8c2cc6b41)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bindesc\_entry::data[] |
| --- |

Value of the entry.

This is either an integer or a string

## [◆ ](#ad756a440a8dfa9d396258707a1f681e4)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bindesc\_entry::len |
| --- |

Length of the descriptor data.

## [◆ ](#ab040a2e6d5370498f2a689ba172e4112)tag

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bindesc\_entry::tag |
| --- |

Tag of the entry.

---

The documentation for this struct was generated from the following file:

- zephyr/[bindesc.h](bindesc_8h_source.md)

- [bindesc\_entry](structbindesc__entry.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
