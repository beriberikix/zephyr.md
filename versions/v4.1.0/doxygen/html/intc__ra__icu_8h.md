---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/intc__ra__icu_8h.html
original_path: doxygen/html/intc__ra__icu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intc\_ra\_icu.h File Reference

`#include <[zephyr/dt-bindings/interrupt-controller/renesas-ra-icu.h](renesas-ra-icu_8h_source.md)>`

[Go to the source code of this file.](intc__ra__icu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_](#a28f51943d0ae322da596758f4134a7b6) |
| #define | [RA\_ICU\_FLAG\_EVENT\_OFFSET](#a1811342f456c5d4ea6d84b22fabb6c91)   8 |
| #define | [RA\_ICU\_FLAG\_EVENT\_MASK](#a1e1233fb119146e36c549b816f6b495a)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) << [RA\_ICU\_FLAG\_EVENT\_OFFSET](#a1811342f456c5d4ea6d84b22fabb6c91)) |
| #define | [RA\_ICU\_FLAG\_INTCFG\_OFFSET](#add34bc98468f4e6dd02308b5a285d8e7)   16 |
| #define | [RA\_ICU\_FLAG\_INTCFG\_MASK](#a3956755910b2fb1bcb1e0fe747853b4d)   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) << [RA\_ICU\_FLAG\_INTCFG\_OFFSET](#add34bc98468f4e6dd02308b5a285d8e7)) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ra\_isr\_handler](#aebf359fac4cee1cc97b3ef726fb2c8b9)) (const void \*) |

| Enumerations | |
| --- | --- |
| enum | [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) { [ICU\_FALLING](#aea25818bb1e7cf4bc3d1a6fce309207eaf18832e32784f7f1a0291da77a31a432) , [ICU\_RISING](#aea25818bb1e7cf4bc3d1a6fce309207ea0d5c2ec086858519e4457ac46015d1a3) , [ICU\_BOTH\_EDGE](#aea25818bb1e7cf4bc3d1a6fce309207ea3d05da80f76b235919b656535bf83650) , [ICU\_LOW\_LEVEL](#aea25818bb1e7cf4bc3d1a6fce309207eae3add732d10a107ec6be56d181e4cad4) } |

| Functions | |
| --- | --- |
| void | [ra\_icu\_clear\_int\_flag](#a10a9501f6a1e51173851ebc569d50ecb) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irqn) |
| int | [ra\_icu\_query\_available\_irq](#a012a14c9b65ef744eed4c854d5376e07) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
| int | [ra\_icu\_query\_exists\_irq](#ad2f7c4299dced5b919bcc310abea17bd) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
| void | [ra\_icu\_query\_irq\_config](#af30844ef3589626f9e200f11c821c07e) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*intcfg, [ra\_isr\_handler](#aebf359fac4cee1cc97b3ef726fb2c8b9) \*pisr, const void \*\*cbarg) |
| int | [ra\_icu\_irq\_connect\_dynamic](#ad854b5c872869e0d982f8af4279ae81f) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| int | [ra\_icu\_irq\_disconnect\_dynamic](#aba7fd8b061cc37d1525bf07b6aeae2f1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |

## Macro Definition Documentation

## [◆ ](#a1e1233fb119146e36c549b816f6b495a)RA\_ICU\_FLAG\_EVENT\_MASK

| #define RA\_ICU\_FLAG\_EVENT\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) << [RA\_ICU\_FLAG\_EVENT\_OFFSET](#a1811342f456c5d4ea6d84b22fabb6c91)) |
| --- |

## [◆ ](#a1811342f456c5d4ea6d84b22fabb6c91)RA\_ICU\_FLAG\_EVENT\_OFFSET

| #define RA\_ICU\_FLAG\_EVENT\_OFFSET   8 |
| --- |

## [◆ ](#a3956755910b2fb1bcb1e0fe747853b4d)RA\_ICU\_FLAG\_INTCFG\_MASK

| #define RA\_ICU\_FLAG\_INTCFG\_MASK   ([BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(8) << [RA\_ICU\_FLAG\_INTCFG\_OFFSET](#add34bc98468f4e6dd02308b5a285d8e7)) |
| --- |

## [◆ ](#add34bc98468f4e6dd02308b5a285d8e7)RA\_ICU\_FLAG\_INTCFG\_OFFSET

| #define RA\_ICU\_FLAG\_INTCFG\_OFFSET   16 |
| --- |

## [◆ ](#a28f51943d0ae322da596758f4134a7b6)ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_

| #define ZEPHYR\_DRIVERS\_INTERRUPT\_CONTROLLER\_INTC\_RA\_ICU\_H\_ |
| --- |

## Typedef Documentation

## [◆ ](#aebf359fac4cee1cc97b3ef726fb2c8b9)ra\_isr\_handler

| typedef void(\* ra\_isr\_handler) (const void \*) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aea25818bb1e7cf4bc3d1a6fce309207e)icu\_irq\_mode

| enum [icu\_irq\_mode](#aea25818bb1e7cf4bc3d1a6fce309207e) |
| --- |

| Enumerator | |
| --- | --- |
| ICU\_FALLING |  |
| ICU\_RISING |  |
| ICU\_BOTH\_EDGE |  |
| ICU\_LOW\_LEVEL |  |

## Function Documentation

## [◆ ](#a10a9501f6a1e51173851ebc569d50ecb)ra\_icu\_clear\_int\_flag()

| | void ra\_icu\_clear\_int\_flag | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irqn* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad854b5c872869e0d982f8af4279ae81f)ra\_icu\_irq\_connect\_dynamic()

| | int ra\_icu\_irq\_connect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, | |  |  | void(\* | *routine*)(const void \*parameter), | |  |  | const void \* | *parameter*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aba7fd8b061cc37d1525bf07b6aeae2f1)ra\_icu\_irq\_disconnect\_dynamic()

| | int ra\_icu\_irq\_disconnect\_dynamic | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, | |  |  | void(\* | *routine*)(const void \*parameter), | |  |  | const void \* | *parameter*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a012a14c9b65ef744eed4c854d5376e07)ra\_icu\_query\_available\_irq()

| | int ra\_icu\_query\_available\_irq | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad2f7c4299dced5b919bcc310abea17bd)ra\_icu\_query\_exists\_irq()

| | int ra\_icu\_query\_exists\_irq | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af30844ef3589626f9e200f11c821c07e)ra\_icu\_query\_irq\_config()

| | void ra\_icu\_query\_irq\_config | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *intcfg*, | |  |  | [ra\_isr\_handler](#aebf359fac4cee1cc97b3ef726fb2c8b9) \* | *pisr*, | |  |  | const void \*\* | *cbarg* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intc\_ra\_icu.h](intc__ra__icu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
