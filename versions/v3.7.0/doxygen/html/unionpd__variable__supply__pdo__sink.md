---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unionpd__variable__supply__pdo__sink.html
original_path: doxygen/html/unionpd__variable__supply__pdo__sink.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_variable\_supply\_pdo\_sink Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Variable Supply PDO Sink value See Table 6-15 Variable Supply (non-Battery) PDO - Sink.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operational\_current](#ad648f2400a495b37d8b9f995556419d0): 10 |  |
|  | operational Current in 10mA units [More...](#ad648f2400a495b37d8b9f995556419d0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#aaaa1cf3f08208966fb00093f910f70ab): 10 |  |
|  | Minimum Voltage in 50mV units. [More...](#aaaa1cf3f08208966fb00093f910f70ab) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#ae360e7c2335a4f6cf5d267c8c82fdc45): 10 |  |
|  | Maximum Voltage in 50mV units. [More...](#ae360e7c2335a4f6cf5d267c8c82fdc45) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#a4a09b8b5e2397925d5a433917378193e): 2 |  |
|  | Variable supply. [More...](#a4a09b8b5e2397925d5a433917378193e) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#a2ff80c049f98ab090b100b7f9877bffb) |
|  | Raw PDO value. |

## Detailed Description

Create a Variable Supply PDO Sink value See Table 6-15 Variable Supply (non-Battery) PDO - Sink.

## Field Documentation

## [◆ ](#af6496f290d7039095a7f3308cf87d8f9)[struct]

| struct { ... } [pd\_variable\_supply\_pdo\_sink](unionpd__variable__supply__pdo__sink.md) |
| --- |

## [◆ ](#ae360e7c2335a4f6cf5d267c8c82fdc45)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_sink::max\_voltage |
| --- |

Maximum Voltage in 50mV units.

## [◆ ](#aaaa1cf3f08208966fb00093f910f70ab)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_sink::min\_voltage |
| --- |

Minimum Voltage in 50mV units.

## [◆ ](#ad648f2400a495b37d8b9f995556419d0)operational\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_sink::operational\_current |
| --- |

operational Current in 10mA units

## [◆ ](#a2ff80c049f98ab090b100b7f9877bffb)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_sink::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#a4a09b8b5e2397925d5a433917378193e)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_variable\_supply\_pdo\_sink::type |
| --- |

Variable supply.

SET TO PDO\_VARIABLE

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_variable\_supply\_pdo\_sink](unionpd__variable__supply__pdo__sink.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
