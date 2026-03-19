---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmspi__cfg.html
original_path: doxygen/html/structmspi__cfg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspi\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [MSPI Driver APIs](group__mspi__interface.md) » [MSPI Configure API](group__mspi__configure__api.md)

MSPI controller configuration.
[More...](#details)

`#include <[mspi.h](mspi_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_num](#af54bbbfbe07d88325117131fefe265ef) |
|  | mspi channel number |
| enum [mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) | [op\_mode](#ab33e45d7802cf777a595d87058e8bfb5) |
|  | Configure operation mode. |
| enum [mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) | [duplex](#a449894e0e58f96b775b4cc1c1eb83e77) |
|  | Configure duplex mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dqs\_support](#a2cf6e063074f86973cf03324637d656a) |
|  | DQS support flag. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sw\_multi\_periph](#a1192af56f714a42aa667a40e369b185e) |
|  | Software managed multi peripheral enable. |
| struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | [ce\_group](#a4053a398f6390e45ef6da385756f14bf) |
|  | GPIO chip select lines (optional). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_ce\_gpios](#a20f6e453165b6ac22a42906604a3258a) |
|  | GPIO chip-select line numbers (optional). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num\_periph](#a6d24969046f175f158a5dae05e9284b1) |
|  | Peripheral number from 0 to host controller peripheral limit. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_freq](#a9a76198688b4acac9101274a71bfbf9c) |
|  | Maximum supported frequency in MHz. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [re\_init](#afef0fe6991e28a4496e51333963fd3d1) |
|  | Whether to re-initialize controller. |

## Detailed Description

MSPI controller configuration.

## Field Documentation

## [◆ ](#a4053a398f6390e45ef6da385756f14bf)ce\_group

| struct [gpio\_dt\_spec](structgpio__dt__spec.md)\* mspi\_cfg::ce\_group |
| --- |

GPIO chip select lines (optional).

## [◆ ](#af54bbbfbe07d88325117131fefe265ef)channel\_num

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mspi\_cfg::channel\_num |
| --- |

mspi channel number

## [◆ ](#a2cf6e063074f86973cf03324637d656a)dqs\_support

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_cfg::dqs\_support |
| --- |

DQS support flag.

## [◆ ](#a449894e0e58f96b775b4cc1c1eb83e77)duplex

| enum [mspi\_duplex](group__mspi__interface.md#ga20e348d7a9f1f9b32078a3bf6c4e82b9) mspi\_cfg::duplex |
| --- |

Configure duplex mode.

## [◆ ](#a9a76198688b4acac9101274a71bfbf9c)max\_freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_cfg::max\_freq |
| --- |

Maximum supported frequency in MHz.

## [◆ ](#a20f6e453165b6ac22a42906604a3258a)num\_ce\_gpios

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_cfg::num\_ce\_gpios |
| --- |

GPIO chip-select line numbers (optional).

## [◆ ](#a6d24969046f175f158a5dae05e9284b1)num\_periph

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mspi\_cfg::num\_periph |
| --- |

Peripheral number from 0 to host controller peripheral limit.

## [◆ ](#ab33e45d7802cf777a595d87058e8bfb5)op\_mode

| enum [mspi\_op\_mode](group__mspi__interface.md#ga3f211cd81e05cb9ee073a2722f6b22d8) mspi\_cfg::op\_mode |
| --- |

Configure operation mode.

## [◆ ](#afef0fe6991e28a4496e51333963fd3d1)re\_init

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_cfg::re\_init |
| --- |

Whether to re-initialize controller.

## [◆ ](#a1192af56f714a42aa667a40e369b185e)sw\_multi\_periph

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mspi\_cfg::sw\_multi\_periph |
| --- |

Software managed multi peripheral enable.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[mspi.h](mspi_8h_source.md)

- [mspi\_cfg](structmspi__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
