---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sys_2iterable__sections_8h.html
original_path: doxygen/html/sys_2iterable__sections_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iterable\_sections.h File Reference

`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](sys_2iterable__sections_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TYPE\_SECTION\_ITERABLE](group__iterable__section__apis.md#gac5177fefd615bdd3025fac742d414808)(type, varname, secname, section\_postfix) |
|  | Defines a new element for an iterable section for a generic type. |
| #define | [TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname) |
|  | iterable section start symbol for a generic type |
| #define | [TYPE\_SECTION\_END](group__iterable__section__apis.md#ga14d6bc375423775e5484183eeadd1fad)(secname) |
|  | iterable section end symbol for a generic type |
| #define | [TYPE\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga40c6ba05d5bcb848a530bdc17bbff5be)(type, secname) |
|  | iterable section extern for start symbol for a generic type |
| #define | [TYPE\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#gaf009fe4b90f7b338c3bf85bb4cd682e5)(type, secname) |
|  | iterable section extern for end symbol for a generic type |
| #define | [TYPE\_SECTION\_FOREACH](group__iterable__section__apis.md#gac74c8d3f92304a7082d5c5c7c62dace7)(type, secname, iterator) |
|  | Iterate over a specified iterable section for a generic type. |
| #define | [TYPE\_SECTION\_GET](group__iterable__section__apis.md#gae0f61156fa152ff5604087e2849caeb0)(type, secname, i, dst) |
|  | Get element from section for a generic type. |
| #define | [TYPE\_SECTION\_COUNT](group__iterable__section__apis.md#ga0c3da72ee4432a94242aaccf5cd5e9fb)(type, secname, dst) |
|  | Count elements in a section for a generic type. |
| #define | [STRUCT\_SECTION\_START](group__iterable__section__apis.md#ga53b4dd9b989b54d62254b425a23620f0)(struct\_type) |
|  | iterable section start symbol for a struct type |
| #define | [STRUCT\_SECTION\_START\_EXTERN](group__iterable__section__apis.md#ga4d61ce2fdd6e8d2881038e521d7aed54)(struct\_type) |
|  | iterable section extern for start symbol for a struct |
| #define | [STRUCT\_SECTION\_END](group__iterable__section__apis.md#ga3170a115129c683811181615661bc298)(struct\_type) |
|  | iterable section end symbol for a struct type |
| #define | [STRUCT\_SECTION\_END\_EXTERN](group__iterable__section__apis.md#ga190b01770f323bfc7acfd50312b83a91)(struct\_type) |
|  | iterable section extern for end symbol for a struct |
| #define | [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)(secname, struct\_type, varname) |
|  | Defines a new element of alternate data type for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE](group__iterable__section__apis.md#ga2013cfe23c77c472f6fc43ccc99ac228)(secname, struct\_type, varname, size) |
|  | Defines an array of elements of alternate data type for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(struct\_type, varname) |
|  | Defines a new element for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_ARRAY](group__iterable__section__apis.md#ga1d9ed5b5006579e7c452a6f15418849b)(struct\_type, varname, size) |
|  | Defines an array of elements for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_NAMED](group__iterable__section__apis.md#gada3ff915b4ed4881a61b79d8877131e2)(struct\_type, name, varname) |
|  | Defines a new element for an iterable section with a custom name. |
| #define | [STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE](group__iterable__section__apis.md#ga5c2441634885ac7c5c15e5cfe159b2fd)(struct\_type, secname, name, varname) |
|  | Defines a new element for an iterable section with a custom name, placed in a custom section. |
| #define | [STRUCT\_SECTION\_FOREACH\_ALTERNATE](group__iterable__section__apis.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)(secname, struct\_type, iterator) |
|  | Iterate over a specified iterable section (alternate). |
| #define | [STRUCT\_SECTION\_FOREACH](group__iterable__section__apis.md#gad723296f2650c25dd278e8586bfaf0ab)(struct\_type, iterator) |
|  | Iterate over a specified iterable section. |
| #define | [STRUCT\_SECTION\_GET](group__iterable__section__apis.md#ga583e57b527884034116bf0b27a942b50)(struct\_type, i, dst) |
|  | Get element from section. |
| #define | [STRUCT\_SECTION\_COUNT](group__iterable__section__apis.md#ga5f3ecbd953df825cadb2d08f55bc505c)(struct\_type, dst) |
|  | Count elements in a section. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [iterable\_sections.h](sys_2iterable__sections_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
