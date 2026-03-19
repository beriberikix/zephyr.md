---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/unionpd__fixed__supply__pdo__sink.html
original_path: doxygen/html/unionpd__fixed__supply__pdo__sink.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pd\_fixed\_supply\_pdo\_sink Union Reference

[Device Driver APIs](group__io__interfaces.md) » [USB Power Delivery](group__usb__power__delivery.md)

Create a Fixed Supply PDO Sink value See Table 6-14 Fixed Supply PDO - Sink.
[More...](#details)

`#include <[usbc_pd.h](usbc__pd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [operational\_current](#a2ac4005b0cf3e28ade8f508d2c6f5e20): 10 |  |
|  | Operational Current in 10mA units. [More...](#a2ac4005b0cf3e28ade8f508d2c6f5e20) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [voltage](#ac47dcf98dfca90eb0e6013a3e1c5eb18): 10 |  |
|  | Voltage in 50mV units. [More...](#ac47dcf98dfca90eb0e6013a3e1c5eb18) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [reserved0](#a22f9763652560dbd215324f1bb878a96): 3 |  |
|  | Reserved – Shall be set to zero. [More...](#a22f9763652560dbd215324f1bb878a96) |
| enum [pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358)   [frs\_required](#a7138e45345fc2cd486186190f11e847d): 2 |  |
|  | Fast Role Swap required USB Type-C Current. [More...](#a7138e45345fc2cd486186190f11e847d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [dual\_role\_data](#a5c6bfb21c4d8e70a04895dd31a58885e): 1 |  |
|  | Dual-Role Data. [More...](#a5c6bfb21c4d8e70a04895dd31a58885e) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [usb\_comms\_capable](#a0559272067e2d0c33f52274fb59ea18d): 1 |  |
|  | USB Communications Capable. [More...](#a0559272067e2d0c33f52274fb59ea18d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [unconstrained\_power](#ab406f1f36e5fe6f7acb9abc91991a803): 1 |  |
|  | Unconstrained Power. [More...](#ab406f1f36e5fe6f7acb9abc91991a803) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [higher\_capability](#a3086d57313f05b8bc91fb3590e51c657): 1 |  |
|  | Higher Capability. [More...](#a3086d57313f05b8bc91fb3590e51c657) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [dual\_role\_power](#aad255dbee3452bf3276464c59f113cb2): 1 |  |
|  | Dual-Role Power. [More...](#aad255dbee3452bf3276464c59f113cb2) |
| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328)   [type](#ac505fdd24064de98c5c17088b2c88c5c): 2 |  |
|  | Fixed supply. [More...](#ac505fdd24064de98c5c17088b2c88c5c) |
| }; |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [raw\_value](#aebdeb854bcac0d20efcbe3be56dcc9f8) |
|  | Raw PDO value. |

## Detailed Description

Create a Fixed Supply PDO Sink value See Table 6-14 Fixed Supply PDO - Sink.

## Field Documentation

## [◆ ](#a65a59e06174e0ad8acb90693fe131d30)[struct]

| struct { ... } [pd\_fixed\_supply\_pdo\_sink](unionpd__fixed__supply__pdo__sink.md) |
| --- |

## [◆ ](#a5c6bfb21c4d8e70a04895dd31a58885e)dual\_role\_data

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::dual\_role\_data |
| --- |

Dual-Role Data.

## [◆ ](#aad255dbee3452bf3276464c59f113cb2)dual\_role\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::dual\_role\_power |
| --- |

Dual-Role Power.

## [◆ ](#a7138e45345fc2cd486186190f11e847d)frs\_required

| enum [pd\_frs\_type](group__usb__power__delivery.md#ga48b33240e19524ea003052103d310358) pd\_fixed\_supply\_pdo\_sink::frs\_required |
| --- |

Fast Role Swap required USB Type-C Current.

## [◆ ](#a3086d57313f05b8bc91fb3590e51c657)higher\_capability

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::higher\_capability |
| --- |

Higher Capability.

## [◆ ](#a2ac4005b0cf3e28ade8f508d2c6f5e20)operational\_current

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::operational\_current |
| --- |

Operational Current in 10mA units.

## [◆ ](#aebdeb854bcac0d20efcbe3be56dcc9f8)raw\_value

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::raw\_value |
| --- |

Raw PDO value.

## [◆ ](#a22f9763652560dbd215324f1bb878a96)reserved0

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::reserved0 |
| --- |

Reserved – Shall be set to zero.

## [◆ ](#ac505fdd24064de98c5c17088b2c88c5c)type

| enum [pdo\_type](group__usb__power__delivery.md#ga316dca7ed0b85f1aa224d7a767896328) pd\_fixed\_supply\_pdo\_sink::type |
| --- |

Fixed supply.

SET TO PDO\_FIXED

## [◆ ](#ab406f1f36e5fe6f7acb9abc91991a803)unconstrained\_power

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::unconstrained\_power |
| --- |

Unconstrained Power.

## [◆ ](#a0559272067e2d0c33f52274fb59ea18d)usb\_comms\_capable

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::usb\_comms\_capable |
| --- |

USB Communications Capable.

## [◆ ](#ac47dcf98dfca90eb0e6013a3e1c5eb18)voltage

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pd\_fixed\_supply\_pdo\_sink::voltage |
| --- |

Voltage in 50mV units.

---

The documentation for this union was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_pd.h](usbc__pd_8h_source.md)

- [pd\_fixed\_supply\_pdo\_sink](unionpd__fixed__supply__pdo__sink.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
