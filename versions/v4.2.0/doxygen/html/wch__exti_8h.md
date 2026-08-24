---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/wch__exti_8h.html
original_path: doxygen/html/wch__exti_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wch\_exti.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](wch__exti_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [wch\_exti\_callback\_handler\_t](#aa1c9d73d6337b6fd8dc95187f739b768)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user) |

| Enumerations | |
| --- | --- |
| enum | [wch\_exti\_trigger](#ab41aa3ea720735eb77fc4aaa59659db1) { [WCH\_EXTI\_TRIGGER\_RISING\_EDGE](#ab41aa3ea720735eb77fc4aaa59659db1ac64106e333e2172f25bcbf5c201acb28) = BIT(0) , [WCH\_EXTI\_TRIGGER\_FALLING\_EDGE](#ab41aa3ea720735eb77fc4aaa59659db1a3b2c0bd85bbfed5d0bed4d495534e518) = BIT(1) } |

| Functions | |
| --- | --- |
| void | [wch\_exti\_enable](#a36723b918e6ddb225e05c041a6127369) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
| void | [wch\_exti\_disable](#a2b90b358d0ee8445e1257c636cfbd931) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line) |
| void | [wch\_exti\_set\_trigger](#aa7c5d9dff440158faad0c33da28f8777) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, enum [wch\_exti\_trigger](#ab41aa3ea720735eb77fc4aaa59659db1) trigger) |
| int | [wch\_exti\_configure](#a7ff8c5c40b36a6974c535e54fbff311f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, [wch\_exti\_callback\_handler\_t](#aa1c9d73d6337b6fd8dc95187f739b768) callback, void \*user) |

## Typedef Documentation

## [◆ ](#aa1c9d73d6337b6fd8dc95187f739b768)wch\_exti\_callback\_handler\_t

| typedef void(\* wch\_exti\_callback\_handler\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) line, void \*user) |
| --- |

## Enumeration Type Documentation

## [◆ ](#ab41aa3ea720735eb77fc4aaa59659db1)wch\_exti\_trigger

| enum [wch\_exti\_trigger](#ab41aa3ea720735eb77fc4aaa59659db1) |
| --- |

| Enumerator | |
| --- | --- |
| WCH\_EXTI\_TRIGGER\_RISING\_EDGE |  |
| WCH\_EXTI\_TRIGGER\_FALLING\_EDGE |  |

## Function Documentation

## [◆ ](#a7ff8c5c40b36a6974c535e54fbff311f)wch\_exti\_configure()

| int wch\_exti\_configure | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
| --- | --- | --- | --- |
|  |  | [wch\_exti\_callback\_handler\_t](#aa1c9d73d6337b6fd8dc95187f739b768) | *callback*, |
|  |  | void \* | *user* ) |

## [◆ ](#a2b90b358d0ee8445e1257c636cfbd931)wch\_exti\_disable()

| void wch\_exti\_disable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a36723b918e6ddb225e05c041a6127369)wch\_exti\_enable()

| void wch\_exti\_enable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aa7c5d9dff440158faad0c33da28f8777)wch\_exti\_set\_trigger()

| void wch\_exti\_set\_trigger | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *line*, |
| --- | --- | --- | --- |
|  |  | enum [wch\_exti\_trigger](#ab41aa3ea720735eb77fc4aaa59659db1) | *trigger* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wch\_exti.h](wch__exti_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
