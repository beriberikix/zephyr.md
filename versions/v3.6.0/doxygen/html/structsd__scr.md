---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsd__scr.html
original_path: doxygen/html/structsd__scr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sd\_scr Struct Reference

SD card configuration register.
[More...](#details)

`#include <[sd_spec.h](sd__spec_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [scr\_structure](#a3fc37c731dfb5c5596b6389152479c07) |
|  | SCR Structure [63:60]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sd\_spec](#ae6201af1083efa828cced000874bf197) |
|  | SD memory card specification version [59:56]. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#abda65da85e20979a1fc71f2aea1f947b) |
|  | SCR flags in \_sd\_scr\_flag. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sd\_sec](#a9f8254b5fe6911156bae727e29262f5a) |
|  | Security specification supported [54:52]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sd\_width](#a40d30ccc4daf2c32f2ac162b402f3887) |
|  | Data bus widths supported [51:48]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sd\_ext\_sec](#a15f60bc2115b943ce938f3a96dd8e547) |
|  | Extended security support [46:43]. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [cmd\_support](#a9016ca73a668499289c52355ebb83cb1) |
|  | Command support bits [33:32] 33-support CMD23, 32-support cmd20. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rsvd](#aba20efcf752335f1a86d0a86607d92d0) |
|  | reserved for manufacturer usage [31:0] |

## Detailed Description

SD card configuration register.

Even more SD card data.

## Field Documentation

## [◆ ](#a9016ca73a668499289c52355ebb83cb1)cmd\_support

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::cmd\_support |
| --- |

Command support bits [33:32] 33-support CMD23, 32-support cmd20.

## [◆ ](#abda65da85e20979a1fc71f2aea1f947b)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sd\_scr::flags |
| --- |

SCR flags in \_sd\_scr\_flag.

## [◆ ](#aba20efcf752335f1a86d0a86607d92d0)rsvd

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sd\_scr::rsvd |
| --- |

reserved for manufacturer usage [31:0]

## [◆ ](#a3fc37c731dfb5c5596b6389152479c07)scr\_structure

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::scr\_structure |
| --- |

SCR Structure [63:60].

## [◆ ](#a15f60bc2115b943ce938f3a96dd8e547)sd\_ext\_sec

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::sd\_ext\_sec |
| --- |

Extended security support [46:43].

## [◆ ](#a9f8254b5fe6911156bae727e29262f5a)sd\_sec

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::sd\_sec |
| --- |

Security specification supported [54:52].

## [◆ ](#ae6201af1083efa828cced000874bf197)sd\_spec

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::sd\_spec |
| --- |

SD memory card specification version [59:56].

## [◆ ](#a40d30ccc4daf2c32f2ac162b402f3887)sd\_width

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sd\_scr::sd\_width |
| --- |

Data bus widths supported [51:48].

---

The documentation for this struct was generated from the following file:

- zephyr/sd/[sd\_spec.h](sd__spec_8h_source.md)

- [sd\_scr](structsd__scr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
