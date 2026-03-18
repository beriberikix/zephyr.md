---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unionpd__augmented__supply__pdo__sink.html
original_path: doxygen/html/unionpd__augmented__supply__pdo__sink.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_augmented\_supply\_pdo\_sink Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create Augmented Supply PDO Sink value See Table 6-17 Programmable Power Supply APDO - Sink.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_current](#a0a5da0df48dff5fae42159026c91c7af): 7 |  |
|  | Maximum Current in 50mA increments. [More...](#a0a5da0df48dff5fae42159026c91c7af) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#a3320455a4c7673d3db95f585b07cc319): 1 |  |
|  | Reserved – Shall be set to zero. [More...](#a3320455a4c7673d3db95f585b07cc319) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [min\_voltage](#ad83710136d9dcad3644ec36c1eee9cb0): 8 |  |
|  | Minimum Voltage in 100mV increments. [More...](#ad83710136d9dcad3644ec36c1eee9cb0) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved1](#a2f1f6094af7449619ab626476fa51698): 1 |  |
|  | Reserved – Shall be set to zero. [More...](#a2f1f6094af7449619ab626476fa51698) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_voltage](#af5eca8ab38a3eaaaecd10cdc1092ce3c): 8 |  |
|  | Maximum Voltage in 100mV increments. [More...](#af5eca8ab38a3eaaaecd10cdc1092ce3c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved2](#adfa0b8ab656255cfecc9ca5e1ee05d49): 3 |  |
|  | Reserved – Shall be set to zero. [More...](#adfa0b8ab656255cfecc9ca5e1ee05d49) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved3](#a22e63fa7e83af25d9822dcf3d9b35f40): 2 |  |
|  | 00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set. [More...](#a22e63fa7e83af25d9822dcf3d9b35f40) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#ad9d2fe810bd3959b99b38180c93a71c0): 2 |  |
|  | Augmented Power Data Object (APDO). [More...](#ad9d2fe810bd3959b99b38180c93a71c0) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#ae28a74642ffcdf1100f37e3542e1ca96) |
|  | Raw PDO value. |

## Detailed Description

Create Augmented Supply PDO Sink value See Table 6-17 Programmable Power Supply APDO - Sink.

## Field Documentation

## [◆ ](#ac395997261c3cf223c5440c3cdf630bf)[struct]

| struct { ... } [pd\_augmented\_supply\_pdo\_sink](unionpd__augmented__supply__pdo__sink.md) |
| --- |

## [◆ ](#a0a5da0df48dff5fae42159026c91c7af)max\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::max\_current |
| --- |

Maximum Current in 50mA increments.

## [◆ ](#af5eca8ab38a3eaaaecd10cdc1092ce3c)max\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::max\_voltage |
| --- |

Maximum Voltage in 100mV increments.

## [◆ ](#ad83710136d9dcad3644ec36c1eee9cb0)min\_voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::min\_voltage |
| --- |

Minimum Voltage in 100mV increments.

## [◆ ](#ae28a74642ffcdf1100f37e3542e1ca96)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#a3320455a4c7673d3db95f585b07cc319)reserved0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::reserved0 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#a2f1f6094af7449619ab626476fa51698)reserved1

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::reserved1 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#adfa0b8ab656255cfecc9ca5e1ee05d49)reserved2

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::reserved2 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#a22e63fa7e83af25d9822dcf3d9b35f40)reserved3

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_augmented\_supply\_pdo\_sink::reserved3 |
| --- |

00b – Programmable Power Supply 01b…11b - Reserved, Shall Not be used Setting as reserved because it defaults to 0 when not set.

## [◆ ](#ad9d2fe810bd3959b99b38180c93a71c0)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_augmented\_supply\_pdo\_sink::type |
| --- |

Augmented Power Data Object (APDO).

SET TO PDO\_AUGMENTED

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_augmented\_supply\_pdo\_sink](unionpd__augmented__supply__pdo__sink.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
