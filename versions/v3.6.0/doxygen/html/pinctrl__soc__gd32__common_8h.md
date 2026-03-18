---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pinctrl__soc__gd32__common_8h.html
original_path: doxygen/html/pinctrl__soc__gd32__common_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl\_soc\_gd32\_common.h File Reference

Gigadevice SoC specific helpers for pinctrl driver.
[More...](#details)

`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <dt-bindings/pinctrl/gd32-afio.h>`

[Go to the source code of this file.](pinctrl__soc__gd32__common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GD32\_PUPD\_GET](#aa92c3af616f86950a0c2182670532f60)(pincfg) |
|  | Obtain PUPD field from pinctrl\_soc\_pin\_t configuration. |
| #define | [GD32\_OTYPE\_GET](#ab818f40b6797fdcbcaec0e8e60a81479)(pincfg) |
|  | Obtain OTYPE field from pinctrl\_soc\_pin\_t configuration. |
| #define | [GD32\_OSPEED\_GET](#a786b5e81f3643ffcc0f27bbbe467401b)(pincfg) |
|  | Obtain OSPEED field from pinctrl\_soc\_pin\_t configuration. |
| GD32 PUPD (values match the ones in the HAL for AF model). | |
| #define | [GD32\_PUPD\_NONE](#a6d65e0d22b11faef8c661c1f64698085)   0U |
|  | No pull-up/down. |
| #define | [GD32\_PUPD\_PULLUP](#af4c1b103266889ab30f5c83e2936892d)   1U |
|  | Pull-up. |
| #define | [GD32\_PUPD\_PULLDOWN](#a04dd91ec07a12774db8f4b5835c47d39)   2U |
|  | Pull-down. |
| GD32 OTYPE (values match the ones in the HAL for AF model). | |
| #define | [GD32\_OTYPE\_PP](#ac0a262538fd3143987bf9abc17804db6)   0U |
|  | Push-pull. |
| #define | [GD32\_OTYPE\_OD](#af6ce59bcdd18128905acc9982fa20bdd)   1U |
|  | Open-drain. |
| GD32 OSPEED (values match the ones in the HAL for AF model, mode minus | |
| one for AFIO model). | |
| #define | [GD32\_OSPEED\_10MHZ](#a9ebb7800a833966707ae14cf62b8acce)   0U |
|  | Maximum 10MHz. |
| #define | [GD32\_OSPEED\_2MHZ](#aac13ae160bc3d73661a4b8ca100cb013)   1U |
|  | Maximum 2MHz. |
| #define | [GD32\_OSPEED\_50MHZ](#a177ba012fcf27e7a635f1148a63dd51c)   2U |
|  | Maximum 50MHz. |
| #define | [GD32\_OSPEED\_MAX](#a93145148efe045ec2df4ecebb91ebd8d)   3U |
|  | Maximum speed. |
| GD32 pin configuration bit field mask and positions. | |
| Fields:   - 31..29: Pull-up/down - 28: Output type - 27..26: Output speed | |
| #define | [GD32\_PUPD\_MSK](#aaf70ca09229da5704f8178fd12587efc)   0x3U |
|  | PUPD field mask. |
| #define | [GD32\_PUPD\_POS](#a57dc4bab7677e156ba09bbb655135104)   29U |
|  | PUPD field position. |
| #define | [GD32\_OTYPE\_MSK](#a76f8f5d1fe9a6e255463918e3865d616)   0x1U |
|  | OTYPE field mask. |
| #define | [GD32\_OTYPE\_POS](#a5bb9edb771fae4128fa78e1743d73c70)   28U |
|  | OTYPE field position. |
| #define | [GD32\_OSPEED\_MSK](#a7f8504427d9138b30b600f023cd653e3)   0x3U |
|  | OSPEED field mask. |
| #define | [GD32\_OSPEED\_POS](#a9662e875d2fea130c2027a3b0d84e4ef)   26U |
|  | OSPEED field position. |

## Detailed Description

Gigadevice SoC specific helpers for pinctrl driver.

## Macro Definition Documentation

## [◆ ](#a9ebb7800a833966707ae14cf62b8acce)GD32\_OSPEED\_10MHZ

| #define GD32\_OSPEED\_10MHZ   0U |
| --- |

Maximum 10MHz.

## [◆ ](#aac13ae160bc3d73661a4b8ca100cb013)GD32\_OSPEED\_2MHZ

| #define GD32\_OSPEED\_2MHZ   1U |
| --- |

Maximum 2MHz.

## [◆ ](#a177ba012fcf27e7a635f1148a63dd51c)GD32\_OSPEED\_50MHZ

| #define GD32\_OSPEED\_50MHZ   2U |
| --- |

Maximum 50MHz.

## [◆ ](#a786b5e81f3643ffcc0f27bbbe467401b)GD32\_OSPEED\_GET

| #define GD32\_OSPEED\_GET | ( |  | *pincfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pincfg) >> [GD32\_OSPEED\_POS](#a9662e875d2fea130c2027a3b0d84e4ef)) & [GD32\_OSPEED\_MSK](#a7f8504427d9138b30b600f023cd653e3))

[GD32\_OSPEED\_MSK](#a7f8504427d9138b30b600f023cd653e3)

#define GD32\_OSPEED\_MSK

OSPEED field mask.

**Definition** pinctrl\_soc\_gd32\_common.h:160

[GD32\_OSPEED\_POS](#a9662e875d2fea130c2027a3b0d84e4ef)

#define GD32\_OSPEED\_POS

OSPEED field position.

**Definition** pinctrl\_soc\_gd32\_common.h:162

Obtain OSPEED field from pinctrl\_soc\_pin\_t configuration.

Parameters
:   | pincfg | pinctrl\_soc\_pin\_t bit field value. |
    | --- | --- |

## [◆ ](#a93145148efe045ec2df4ecebb91ebd8d)GD32\_OSPEED\_MAX

| #define GD32\_OSPEED\_MAX   3U |
| --- |

Maximum speed.

## [◆ ](#a7f8504427d9138b30b600f023cd653e3)GD32\_OSPEED\_MSK

| #define GD32\_OSPEED\_MSK   0x3U |
| --- |

OSPEED field mask.

## [◆ ](#a9662e875d2fea130c2027a3b0d84e4ef)GD32\_OSPEED\_POS

| #define GD32\_OSPEED\_POS   26U |
| --- |

OSPEED field position.

## [◆ ](#ab818f40b6797fdcbcaec0e8e60a81479)GD32\_OTYPE\_GET

| #define GD32\_OTYPE\_GET | ( |  | *pincfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pincfg) >> [GD32\_OTYPE\_POS](#a5bb9edb771fae4128fa78e1743d73c70)) & [GD32\_OTYPE\_MSK](#a76f8f5d1fe9a6e255463918e3865d616))

[GD32\_OTYPE\_POS](#a5bb9edb771fae4128fa78e1743d73c70)

#define GD32\_OTYPE\_POS

OTYPE field position.

**Definition** pinctrl\_soc\_gd32\_common.h:158

[GD32\_OTYPE\_MSK](#a76f8f5d1fe9a6e255463918e3865d616)

#define GD32\_OTYPE\_MSK

OTYPE field mask.

**Definition** pinctrl\_soc\_gd32\_common.h:156

Obtain OTYPE field from pinctrl\_soc\_pin\_t configuration.

Parameters
:   | pincfg | pinctrl\_soc\_pin\_t bit field value. |
    | --- | --- |

## [◆ ](#a76f8f5d1fe9a6e255463918e3865d616)GD32\_OTYPE\_MSK

| #define GD32\_OTYPE\_MSK   0x1U |
| --- |

OTYPE field mask.

## [◆ ](#af6ce59bcdd18128905acc9982fa20bdd)GD32\_OTYPE\_OD

| #define GD32\_OTYPE\_OD   1U |
| --- |

Open-drain.

## [◆ ](#a5bb9edb771fae4128fa78e1743d73c70)GD32\_OTYPE\_POS

| #define GD32\_OTYPE\_POS   28U |
| --- |

OTYPE field position.

## [◆ ](#ac0a262538fd3143987bf9abc17804db6)GD32\_OTYPE\_PP

| #define GD32\_OTYPE\_PP   0U |
| --- |

Push-pull.

## [◆ ](#aa92c3af616f86950a0c2182670532f60)GD32\_PUPD\_GET

| #define GD32\_PUPD\_GET | ( |  | *pincfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pincfg) >> [GD32\_PUPD\_POS](#a57dc4bab7677e156ba09bbb655135104)) & [GD32\_PUPD\_MSK](#aaf70ca09229da5704f8178fd12587efc))

[GD32\_PUPD\_POS](#a57dc4bab7677e156ba09bbb655135104)

#define GD32\_PUPD\_POS

PUPD field position.

**Definition** pinctrl\_soc\_gd32\_common.h:154

[GD32\_PUPD\_MSK](#aaf70ca09229da5704f8178fd12587efc)

#define GD32\_PUPD\_MSK

PUPD field mask.

**Definition** pinctrl\_soc\_gd32\_common.h:152

Obtain PUPD field from pinctrl\_soc\_pin\_t configuration.

Parameters
:   | pincfg | pinctrl\_soc\_pin\_t bit field value. |
    | --- | --- |

## [◆ ](#aaf70ca09229da5704f8178fd12587efc)GD32\_PUPD\_MSK

| #define GD32\_PUPD\_MSK   0x3U |
| --- |

PUPD field mask.

## [◆ ](#a6d65e0d22b11faef8c661c1f64698085)GD32\_PUPD\_NONE

| #define GD32\_PUPD\_NONE   0U |
| --- |

No pull-up/down.

## [◆ ](#a57dc4bab7677e156ba09bbb655135104)GD32\_PUPD\_POS

| #define GD32\_PUPD\_POS   29U |
| --- |

PUPD field position.

## [◆ ](#a04dd91ec07a12774db8f4b5835c47d39)GD32\_PUPD\_PULLDOWN

| #define GD32\_PUPD\_PULLDOWN   2U |
| --- |

Pull-down.

## [◆ ](#af4c1b103266889ab30f5c83e2936892d)GD32\_PUPD\_PULLUP

| #define GD32\_PUPD\_PULLUP   1U |
| --- |

Pull-up.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pinctrl](dir_c0bb3bf986f9412b3a6b9d85dc06c157.md)
- [pinctrl\_soc\_gd32\_common.h](pinctrl__soc__gd32__common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
