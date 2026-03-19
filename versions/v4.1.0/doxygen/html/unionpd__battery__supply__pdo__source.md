---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionpd__battery__supply__pdo__source.html
original_path: doxygen/html/unionpd__battery__supply__pdo__source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_battery\_supply\_pdo\_source Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Battery Supply PDO Source value See Table 6-12 Battery Supply PDO - Source.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_power](#a00ea9931d839cf83b56513f77aa7d5b9): 10 |  |
|  | Maximum Allowable Power in 250mW units. [More...](#a00ea9931d839cf83b56513f77aa7d5b9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#afa2335788e7fde01b90afd95bccf6d5f): 10 |  |
|  | Minimum Voltage in 50mV units. [More...](#afa2335788e7fde01b90afd95bccf6d5f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#a673ea076da8810bc694b2dc82bbede67): 10 |  |
|  | Maximum Voltage in 50mV units. [More...](#a673ea076da8810bc694b2dc82bbede67) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#ab546fd1a6caa77a57b5d5420a8ee31d7): 2 |  |
|  | Battery supply. [More...](#ab546fd1a6caa77a57b5d5420a8ee31d7) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#a1e775dc0082b531216c154724be360b0) |
|  | Raw PDO value. |

## Detailed Description

Create a Battery Supply PDO Source value See Table 6-12 Battery Supply PDO - Source.

## Field Documentation

## [◆ ](#a0d1db555b693d55a5f8b7e007be2d422)[struct]

| struct { ... } [pd\_battery\_supply\_pdo\_source](unionpd__battery__supply__pdo__source.md) |
| --- |

## [◆ ](#a00ea9931d839cf83b56513f77aa7d5b9)max\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_source::max\_power |
| --- |

Maximum Allowable Power in 250mW units.

## [◆ ](#a673ea076da8810bc694b2dc82bbede67)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_source::max\_voltage |
| --- |

Maximum Voltage in 50mV units.

## [◆ ](#afa2335788e7fde01b90afd95bccf6d5f)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_source::min\_voltage |
| --- |

Minimum Voltage in 50mV units.

## [◆ ](#a1e775dc0082b531216c154724be360b0)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_source::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#ab546fd1a6caa77a57b5d5420a8ee31d7)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_battery\_supply\_pdo\_source::type |
| --- |

Battery supply.

SET TO PDO\_BATTERY

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_battery\_supply\_pdo\_source](unionpd__battery__supply__pdo__source.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
