---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/unionpd__battery__supply__pdo__sink.html
original_path: doxygen/html/unionpd__battery__supply__pdo__sink.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_battery\_supply\_pdo\_sink Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Battery Supply PDO Sink value See Table 6-16 Battery Supply PDO - Sink.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operational\_power](#a3f1072c4ca168aaedd13257f01f410aa): 10 |  |
|  | Operational Power in 250mW units. [More...](#a3f1072c4ca168aaedd13257f01f410aa) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#a5a588a46ae8bef2dc10445c2f5422246): 10 |  |
|  | Minimum Voltage in 50mV units. [More...](#a5a588a46ae8bef2dc10445c2f5422246) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#a858efb23a0c143917b88e5596b899c79): 10 |  |
|  | Maximum Voltage in 50mV units. [More...](#a858efb23a0c143917b88e5596b899c79) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#acb8b674a789f0a5b397d7ab93d443543): 2 |  |
|  | Battery supply. [More...](#acb8b674a789f0a5b397d7ab93d443543) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#aa973b26972c1e1a96c7e0c09dbed08f3) |
|  | Raw PDO value. |

## Detailed Description

Create a Battery Supply PDO Sink value See Table 6-16 Battery Supply PDO - Sink.

## Field Documentation

## [◆ ](#a33d6a0746f05343c0d7fdab4a5f27917)[struct]

| struct { ... } [pd\_battery\_supply\_pdo\_sink](unionpd__battery__supply__pdo__sink.md) |
| --- |

## [◆ ](#a858efb23a0c143917b88e5596b899c79)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_sink::max\_voltage |
| --- |

Maximum Voltage in 50mV units.

## [◆ ](#a5a588a46ae8bef2dc10445c2f5422246)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_sink::min\_voltage |
| --- |

Minimum Voltage in 50mV units.

## [◆ ](#a3f1072c4ca168aaedd13257f01f410aa)operational\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_sink::operational\_power |
| --- |

Operational Power in 250mW units.

## [◆ ](#aa973b26972c1e1a96c7e0c09dbed08f3)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_battery\_supply\_pdo\_sink::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#acb8b674a789f0a5b397d7ab93d443543)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_battery\_supply\_pdo\_sink::type |
| --- |

Battery supply.

SET TO PDO\_BATTERY

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_battery\_supply\_pdo\_sink](unionpd__battery__supply__pdo__sink.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
