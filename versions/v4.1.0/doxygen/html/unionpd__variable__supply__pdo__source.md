---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionpd__variable__supply__pdo__source.html
original_path: doxygen/html/unionpd__variable__supply__pdo__source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_variable\_supply\_pdo\_source Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Variable Supply PDO Source value See Table 6-11 Variable Supply (non-Battery) PDO - Source.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_current](#a8193ca96084db5901bb30195113ff01f): 10 |  |
|  | Maximum Current in 10mA units. [More...](#a8193ca96084db5901bb30195113ff01f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#a67d86c71997a7c0605b8a199cd51c920): 10 |  |
|  | Minimum Voltage in 50mV units. [More...](#a67d86c71997a7c0605b8a199cd51c920) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#a008cf5201ea6d3e238d547b738570c45): 10 |  |
|  | Maximum Voltage in 50mV units. [More...](#a008cf5201ea6d3e238d547b738570c45) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#a5da7eb69fc69a58662f09690fba92633): 2 |  |
|  | Variable supply. [More...](#a5da7eb69fc69a58662f09690fba92633) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#af00512126f128bf1cf31e802652af1bf) |
|  | Raw PDO value. |

## Detailed Description

Create a Variable Supply PDO Source value See Table 6-11 Variable Supply (non-Battery) PDO - Source.

## Field Documentation

## [◆ ](#a800c4153acb2eee7915e559eb2cf0ac8)[struct]

| struct { ... } [pd\_variable\_supply\_pdo\_source](unionpd__variable__supply__pdo__source.md) |
| --- |

## [◆ ](#a8193ca96084db5901bb30195113ff01f)max\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_source::max\_current |
| --- |

Maximum Current in 10mA units.

## [◆ ](#a008cf5201ea6d3e238d547b738570c45)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_source::max\_voltage |
| --- |

Maximum Voltage in 50mV units.

## [◆ ](#a67d86c71997a7c0605b8a199cd51c920)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_source::min\_voltage |
| --- |

Minimum Voltage in 50mV units.

## [◆ ](#af00512126f128bf1cf31e802652af1bf)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_variable\_supply\_pdo\_source::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#a5da7eb69fc69a58662f09690fba92633)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_variable\_supply\_pdo\_source::type |
| --- |

Variable supply.

SET TO PDO\_VARIABLE

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_variable\_supply\_pdo\_source](unionpd__variable__supply__pdo__source.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
