---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionpd__augmented__supply__pdo__source.html
original_path: doxygen/html/unionpd__augmented__supply__pdo__source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_augmented\_supply\_pdo\_source Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create Augmented Supply PDO Source value See Table 6-13 Programmable Power Supply APDO - Source.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_current](#a7ef0b26951ce2683c9c4ca0f19b73d6d): 7 |  |
|  | Maximum Current in 50mA increments. [More...](#a7ef0b26951ce2683c9c4ca0f19b73d6d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#ac046ddf128416ecbb8f3a26185d03e03): 1 |  |
|  | Reserved – Shall be set to zero. [More...](#ac046ddf128416ecbb8f3a26185d03e03) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#a56e1af2acda73fee7e40449b7c39745d): 8 |  |
|  | Minimum Voltage in 100mV increments. [More...](#a56e1af2acda73fee7e40449b7c39745d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#ae79eb7473040058c0b8572cfe4fa4dce): 1 |  |
|  | Reserved – Shall be set to zero. [More...](#ae79eb7473040058c0b8572cfe4fa4dce) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#aba6df91a8c5da92517f885fa89af8747): 8 |  |
|  | Maximum Voltage in 100mV increments. [More...](#aba6df91a8c5da92517f885fa89af8747) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved2](#ab5868f6ba91821d56ddb419e895a05fa): 2 |  |
|  | Reserved – Shall be set to zero. [More...](#ab5868f6ba91821d56ddb419e895a05fa) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [pps\_power\_limited](#abfac34ee5da0b1700b784c7bfe925c19): 1 |  |
|  | PPS Power Limited. [More...](#abfac34ee5da0b1700b784c7bfe925c19) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved3](#aa59ad8a8eb4e2343c14bbe54937aa93d): 2 |  |
|  | 00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set. [More...](#aa59ad8a8eb4e2343c14bbe54937aa93d) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#aaea2842b628bde92bb74ab0eb7d5aad4): 2 |  |
|  | Augmented Power Data Object (APDO). [More...](#aaea2842b628bde92bb74ab0eb7d5aad4) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#a093a674e538dcc2541ff86f50d0156df) |
|  | Raw PDO value. |

## Detailed Description

Create Augmented Supply PDO Source value See Table 6-13 Programmable Power Supply APDO - Source.

## Field Documentation

## [◆ ](#a18a6704de9b5557824d63e52abef8b20)[struct]

| struct { ... } [pd\_augmented\_supply\_pdo\_source](unionpd__augmented__supply__pdo__source.md) |
| --- |

## [◆ ](#a7ef0b26951ce2683c9c4ca0f19b73d6d)max\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::max\_current |
| --- |

Maximum Current in 50mA increments.

## [◆ ](#aba6df91a8c5da92517f885fa89af8747)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::max\_voltage |
| --- |

Maximum Voltage in 100mV increments.

## [◆ ](#a56e1af2acda73fee7e40449b7c39745d)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::min\_voltage |
| --- |

Minimum Voltage in 100mV increments.

## [◆ ](#abfac34ee5da0b1700b784c7bfe925c19)pps\_power\_limited

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::pps\_power\_limited |
| --- |

PPS Power Limited.

## [◆ ](#a093a674e538dcc2541ff86f50d0156df)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#ac046ddf128416ecbb8f3a26185d03e03)reserved0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::reserved0 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#ae79eb7473040058c0b8572cfe4fa4dce)reserved1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::reserved1 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#ab5868f6ba91821d56ddb419e895a05fa)reserved2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::reserved2 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#aa59ad8a8eb4e2343c14bbe54937aa93d)reserved3

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_source::reserved3 |
| --- |

00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set.

## [◆ ](#aaea2842b628bde92bb74ab0eb7d5aad4)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_augmented\_supply\_pdo\_source::type |
| --- |

Augmented Power Data Object (APDO).

SET TO PDO\_AUGMENTED

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_augmented\_supply\_pdo\_source](unionpd__augmented__supply__pdo__source.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
