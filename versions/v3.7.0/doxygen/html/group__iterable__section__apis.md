---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__iterable__section__apis.html
original_path: doxygen/html/group__iterable__section__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Iterable Sections APIs

[Operating System Services](group__os__services.md)

Iterable Sections APIs.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [ITERABLE\_SECTION\_ROM](#gaa83030f309052399a7d1f61c56a0c901)(struct\_type, subalign) |
|  | Define a read-only iterable section output. |
| #define | [ITERABLE\_SECTION\_ROM\_NUMERIC](#ga2e525d689b958775ad0e1d2c8e61066a)(struct\_type, subalign) |
|  | Define a read-only iterable section output, sorted numerically. |
| #define | [ITERABLE\_SECTION\_ROM\_GC\_ALLOWED](#gaeecef08064fc4329ba5049f198cbb757)(struct\_type, subalign) |
|  | Define a garbage collectable read-only iterable section output. |
| #define | [ITERABLE\_SECTION\_RAM](#ga50d995ef13e80eb36cfc8556e39056d0)(struct\_type, subalign) |
|  | Define a read-write iterable section output. |
| #define | [ITERABLE\_SECTION\_RAM\_NUMERIC](#gae8ce765d1e5ac0e2ba02e33abdbdb63e)(struct\_type, subalign) |
|  | Define a read-write iterable section output, sorted numerically. |
| #define | [ITERABLE\_SECTION\_RAM\_GC\_ALLOWED](#gae9ffbe8beed14a543d170e96c39851e5)(struct\_type, subalign) |
|  | Define a garbage collectable read-write iterable section output. |
| #define | [TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)(type, varname, secname, section\_postfix) |
|  | Defines a new element for an iterable section for a generic type. |
| #define | [TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname) |
|  | iterable section start symbol for a generic type |
| #define | [TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(secname) |
|  | iterable section end symbol for a generic type |
| #define | [TYPE\_SECTION\_START\_EXTERN](#ga40c6ba05d5bcb848a530bdc17bbff5be)(type, secname) |
|  | iterable section extern for start symbol for a generic type |
| #define | [TYPE\_SECTION\_END\_EXTERN](#gaf009fe4b90f7b338c3bf85bb4cd682e5)(type, secname) |
|  | iterable section extern for end symbol for a generic type |
| #define | [TYPE\_SECTION\_FOREACH](#gac74c8d3f92304a7082d5c5c7c62dace7)(type, secname, iterator) |
|  | Iterate over a specified iterable section for a generic type. |
| #define | [TYPE\_SECTION\_GET](#gae0f61156fa152ff5604087e2849caeb0)(type, secname, i, dst) |
|  | Get element from section for a generic type. |
| #define | [TYPE\_SECTION\_COUNT](#ga0c3da72ee4432a94242aaccf5cd5e9fb)(type, secname, dst) |
|  | Count elements in a section for a generic type. |
| #define | [STRUCT\_SECTION\_START](#ga53b4dd9b989b54d62254b425a23620f0)(struct\_type) |
|  | iterable section start symbol for a struct type |
| #define | [STRUCT\_SECTION\_START\_EXTERN](#ga4d61ce2fdd6e8d2881038e521d7aed54)(struct\_type) |
|  | iterable section extern for start symbol for a struct |
| #define | [STRUCT\_SECTION\_END](#ga3170a115129c683811181615661bc298)(struct\_type) |
|  | iterable section end symbol for a struct type |
| #define | [STRUCT\_SECTION\_END\_EXTERN](#ga190b01770f323bfc7acfd50312b83a91)(struct\_type) |
|  | iterable section extern for end symbol for a struct |
| #define | [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](#gae08ef16db3e04967fdca69a19ca4c70b)(secname, struct\_type, varname) |
|  | Defines a new element of alternate data type for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE](#ga2013cfe23c77c472f6fc43ccc99ac228)(secname, struct\_type, varname, size) |
|  | Defines an array of elements of alternate data type for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE](#ga9104f42cbe4a67a931bed7f7cc8f600f)(struct\_type, varname) |
|  | Defines a new element for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_ARRAY](#ga1d9ed5b5006579e7c452a6f15418849b)(struct\_type, varname, size) |
|  | Defines an array of elements for an iterable section. |
| #define | [STRUCT\_SECTION\_ITERABLE\_NAMED](#gada3ff915b4ed4881a61b79d8877131e2)(struct\_type, name, varname) |
|  | Defines a new element for an iterable section with a custom name. |
| #define | [STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE](#ga5c2441634885ac7c5c15e5cfe159b2fd)(struct\_type, secname, name, varname) |
|  | Defines a new element for an iterable section with a custom name, placed in a custom section. |
| #define | [STRUCT\_SECTION\_FOREACH\_ALTERNATE](#ga06fb73cfb2dd5036a6e0f7098105ccd4)(secname, struct\_type, iterator) |
|  | Iterate over a specified iterable section (alternate). |
| #define | [STRUCT\_SECTION\_FOREACH](#gad723296f2650c25dd278e8586bfaf0ab)(struct\_type, iterator) |
|  | Iterate over a specified iterable section. |
| #define | [STRUCT\_SECTION\_GET](#ga583e57b527884034116bf0b27a942b50)(struct\_type, i, dst) |
|  | Get element from section. |
| #define | [STRUCT\_SECTION\_COUNT](#ga5f3ecbd953df825cadb2d08f55bc505c)(struct\_type, dst) |
|  | Count elements in a section. |

## Detailed Description

Iterable Sections APIs.

## Macro Definition Documentation

## [◆ ](#ga50d995ef13e80eb36cfc8556e39056d0)ITERABLE\_SECTION\_RAM

| #define ITERABLE\_SECTION\_RAM | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_DATA\_PROLOGUE](linker-tool-gcc_8h.md#a0d8981d3817b2563846735c90d50240c)(struct\_type##\_area,,[SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE(struct\_type); \

} [GROUP\_DATA\_LINK\_IN](linker-tool-gcc_8h.md#a639d450cbafa51e8937d90df449b797f)(RAMABLE\_REGION, ROMABLE\_REGION)

[SECTION\_DATA\_PROLOGUE](linker-tool-gcc_8h.md#a0d8981d3817b2563846735c90d50240c)

#define SECTION\_DATA\_PROLOGUE(name, options, align)

Same as for SECTION\_PROLOGUE(), except that this one must be used for data sections which on XIP plat...

**Definition** linker-tool-gcc.h:205

[GROUP\_DATA\_LINK\_IN](linker-tool-gcc_8h.md#a639d450cbafa51e8937d90df449b797f)

#define GROUP\_DATA\_LINK\_IN(vregion, lregion)

Route memory for read-write sections that are loaded.

**Definition** linker-tool-gcc.h:139

[SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)

#define SUBALIGN(x)

**Definition** linker-tool-mwdt.h:22

Define a read-write iterable section output.

Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld's SORT\_BY\_NAME.

This macro should be used for read-write data that is modified at runtime.

Note that this keeps the symbols in the image even though they are not being directly referenced. Use this when symbols are indirectly referenced by iterating through the section.

## [◆ ](#gae9ffbe8beed14a543d170e96c39851e5)ITERABLE\_SECTION\_RAM\_GC\_ALLOWED

| #define ITERABLE\_SECTION\_RAM\_GC\_ALLOWED | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_DATA\_PROLOGUE](linker-tool-gcc_8h.md#a0d8981d3817b2563846735c90d50240c)(struct\_type##\_area,,[SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

} [GROUP\_DATA\_LINK\_IN](linker-tool-gcc_8h.md#a639d450cbafa51e8937d90df449b797f)(RAMABLE\_REGION, ROMABLE\_REGION)

Define a garbage collectable read-write iterable section output.

Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld's SORT\_BY\_NAME.

This macro should be used for read-write data that is modified at runtime.

Note that the symbols within the section can be garbage collected.

## [◆ ](#gae8ce765d1e5ac0e2ba02e33abdbdb63e)ITERABLE\_SECTION\_RAM\_NUMERIC

| #define ITERABLE\_SECTION\_RAM\_NUMERIC | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)(struct\_type##\_area, [EMPTY](group__sys-util.md#ga2b7cf2a3641be7b89138615764d60ba3), [SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

} [GROUP\_DATA\_LINK\_IN](linker-tool-gcc_8h.md#a639d450cbafa51e8937d90df449b797f)(RAMABLE\_REGION, ROMABLE\_REGION)

[EMPTY](group__sys-util.md#ga2b7cf2a3641be7b89138615764d60ba3)

#define EMPTY

Macro with an empty expansion.

**Definition** util\_macro.h:335

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)

#define SECTION\_PROLOGUE(name, options, align)

The SECTION\_PROLOGUE() macro is used to define the beginning of a section.

**Definition** linker-tool-gcc.h:180

Define a read-write iterable section output, sorted numerically.

This version of [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0) sorts the entries numerically, that is, SECNAME10 will come after SECNAME2. Up to 2 numeric digits are handled (0-99).

See also
:   [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0)

## [◆ ](#gaa83030f309052399a7d1f61c56a0c901)ITERABLE\_SECTION\_ROM

| #define ITERABLE\_SECTION\_ROM | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)(struct\_type##\_area,,[SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE(struct\_type); \

} [GROUP\_ROM\_LINK\_IN](linker-tool-gcc_8h.md#a0cf8819559a7d33944b47130f478e116)(RAMABLE\_REGION, ROMABLE\_REGION)

[GROUP\_ROM\_LINK\_IN](linker-tool-gcc_8h.md#a0cf8819559a7d33944b47130f478e116)

#define GROUP\_ROM\_LINK\_IN(vregion, lregion)

Route memory for a read-only section.

Define a read-only iterable section output.

Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld's SORT\_BY\_NAME.

This macro should be used for read-only data.

Note that this keeps the symbols in the image even though they are not being directly referenced. Use this when symbols are indirectly referenced by iterating through the section.

## [◆ ](#gaeecef08064fc4329ba5049f198cbb757)ITERABLE\_SECTION\_ROM\_GC\_ALLOWED

| #define ITERABLE\_SECTION\_ROM\_GC\_ALLOWED | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)(struct\_type##\_area,,[SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE\_GC\_ALLOWED(struct\_type); \

} [GROUP\_LINK\_IN](linker-tool-gcc_8h.md#a9250789b7dcbb7afd371010fb3a6031d)(ROMABLE\_REGION)

[GROUP\_LINK\_IN](linker-tool-gcc_8h.md#a9250789b7dcbb7afd371010fb3a6031d)

#define GROUP\_LINK\_IN(where)

Route memory to a specified memory area.

**Definition** linker-tool-gcc.h:93

Define a garbage collectable read-only iterable section output.

Define an output section which will set up an iterable area of equally-sized data structures. For use with [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). Input sections will be sorted by name, per ld's SORT\_BY\_NAME.

This macro should be used for read-only data.

Note that the symbols within the section can be garbage collected.

## [◆ ](#ga2e525d689b958775ad0e1d2c8e61066a)ITERABLE\_SECTION\_ROM\_NUMERIC

| #define ITERABLE\_SECTION\_ROM\_NUMERIC | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *subalign* ) |

`#include <[iterable_sections.h](linker_2iterable__sections_8h.md)>`

**Value:**

[SECTION\_PROLOGUE](linker-tool-gcc_8h.md#a784c696b95848c5f070e257a50fbe23a)(struct\_type##\_area, [EMPTY](group__sys-util.md#ga2b7cf2a3641be7b89138615764d60ba3), [SUBALIGN](linker-tool-mwdt_8h.md#aeec277ba79a2ce60397be71ac2efbe33)(subalign)) \

{ \

Z\_LINK\_ITERABLE\_NUMERIC(struct\_type); \

} [GROUP\_ROM\_LINK\_IN](linker-tool-gcc_8h.md#a0cf8819559a7d33944b47130f478e116)(RAMABLE\_REGION, ROMABLE\_REGION)

Define a read-only iterable section output, sorted numerically.

This version of [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) sorts the entries numerically, that is, SECNAME\_10 will come after SECNAME\_2. \_ separator is required, and up to 2 numeric digits are handled (0-99).

See also
:   [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901)

## [◆ ](#ga5f3ecbd953df825cadb2d08f55bc505c)STRUCT\_SECTION\_COUNT

| #define STRUCT\_SECTION\_COUNT | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *dst* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_COUNT](#ga0c3da72ee4432a94242aaccf5cd5e9fb)(struct struct\_type, struct\_type, dst);

[TYPE\_SECTION\_COUNT](#ga0c3da72ee4432a94242aaccf5cd5e9fb)

#define TYPE\_SECTION\_COUNT(type, secname, dst)

Count elements in a section for a generic type.

**Definition** iterable\_sections.h:137

Count elements in a section.

Parameters
:   | [in] | struct\_type | Struct type |
    | --- | --- | --- |
    | [out] | dst | Pointer to location where result is written. |

## [◆ ](#ga3170a115129c683811181615661bc298)STRUCT\_SECTION\_END

| #define STRUCT\_SECTION\_END | ( |  | *struct\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(struct\_type)

[TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)

#define TYPE\_SECTION\_END(secname)

iterable section end symbol for a generic type

**Definition** iterable\_sections.h:65

iterable section end symbol for a struct type

Parameters
:   | [in] | struct\_type | data type of section |
    | --- | --- | --- |

## [◆ ](#ga190b01770f323bfc7acfd50312b83a91)STRUCT\_SECTION\_END\_EXTERN

| #define STRUCT\_SECTION\_END\_EXTERN | ( |  | *struct\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_END\_EXTERN](#gaf009fe4b90f7b338c3bf85bb4cd682e5)(struct struct\_type, struct\_type)

[TYPE\_SECTION\_END\_EXTERN](#gaf009fe4b90f7b338c3bf85bb4cd682e5)

#define TYPE\_SECTION\_END\_EXTERN(type, secname)

iterable section extern for end symbol for a generic type

**Definition** iterable\_sections.h:92

iterable section extern for end symbol for a struct

Helper macro to give extern for end of iterable section.

Parameters
:   | [in] | struct\_type | data type of section |
    | --- | --- | --- |

## [◆ ](#gad723296f2650c25dd278e8586bfaf0ab)STRUCT\_SECTION\_FOREACH

| #define STRUCT\_SECTION\_FOREACH | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *iterator* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](#ga06fb73cfb2dd5036a6e0f7098105ccd4)(struct\_type, struct\_type, iterator)

[STRUCT\_SECTION\_FOREACH\_ALTERNATE](#ga06fb73cfb2dd5036a6e0f7098105ccd4)

#define STRUCT\_SECTION\_FOREACH\_ALTERNATE(secname, struct\_type, iterator)

Iterate over a specified iterable section (alternate).

**Definition** iterable\_sections.h:257

Iterate over a specified iterable section.

Iterator for structure instances gathered by [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). The linker must provide a \_<struct\_type>\_list\_start symbol and a \_<struct\_type>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

## [◆ ](#ga06fb73cfb2dd5036a6e0f7098105ccd4)STRUCT\_SECTION\_FOREACH\_ALTERNATE

| #define STRUCT\_SECTION\_FOREACH\_ALTERNATE | ( |  | *secname*, |
| --- | --- | --- | --- |
|  |  |  | *struct\_type*, |
|  |  |  | *iterator* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_FOREACH](#gac74c8d3f92304a7082d5c5c7c62dace7)(struct struct\_type, secname, iterator)

[TYPE\_SECTION\_FOREACH](#gac74c8d3f92304a7082d5c5c7c62dace7)

#define TYPE\_SECTION\_FOREACH(type, secname, iterator)

Iterate over a specified iterable section for a generic type.

**Definition** iterable\_sections.h:105

Iterate over a specified iterable section (alternate).

Iterator for structure instances gathered by [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f). The linker must provide a \_<SECNAME>\_list\_start symbol and a \_<SECNAME>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

## [◆ ](#ga583e57b527884034116bf0b27a942b50)STRUCT\_SECTION\_GET

| #define STRUCT\_SECTION\_GET | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *i*, |
|  |  |  | *dst* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_GET](#gae0f61156fa152ff5604087e2849caeb0)(struct struct\_type, struct\_type, i, dst)

[TYPE\_SECTION\_GET](#gae0f61156fa152ff5604087e2849caeb0)

#define TYPE\_SECTION\_GET(type, secname, i, dst)

Get element from section for a generic type.

**Definition** iterable\_sections.h:125

Get element from section.

Note
:   There is no protection against reading beyond the section.

Parameters
:   | [in] | struct\_type | Struct type. |
    | --- | --- | --- |
    | [in] | i | Index. |
    | [out] | dst | Pointer to location where pointer to element is written. |

## [◆ ](#ga9104f42cbe4a67a931bed7f7cc8f600f)STRUCT\_SECTION\_ITERABLE

| #define STRUCT\_SECTION\_ITERABLE | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *varname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](#gae08ef16db3e04967fdca69a19ca4c70b)(struct\_type, struct\_type, varname)

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

Defines a new element for an iterable section.

Convenience helper combining \_\_in\_section() and Z\_DECL\_ALIGN(). The section name is the struct type prepended with an underscore. The subsection is "static" and the subsubsection is the variable name.

In the linker script, create output sections for these using [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0).

Note
:   In order to store the element in ROM, a const specifier has to be added to the declaration: const [STRUCT\_SECTION\_ITERABLE(...)](#ga9104f42cbe4a67a931bed7f7cc8f600f);

## [◆ ](#gae08ef16db3e04967fdca69a19ca4c70b)STRUCT\_SECTION\_ITERABLE\_ALTERNATE

| #define STRUCT\_SECTION\_ITERABLE\_ALTERNATE | ( |  | *secname*, |
| --- | --- | --- | --- |
|  |  |  | *struct\_type*, |
|  |  |  | *varname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)(struct struct\_type, varname, secname, varname)

[TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)

#define TYPE\_SECTION\_ITERABLE(type, varname, secname, section\_postfix)

Defines a new element for an iterable section for a generic type.

**Definition** iterable\_sections.h:42

Defines a new element of alternate data type for an iterable section.

Special variant of [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f), for placing alternate data types within the iterable section of a specific data type. The data type sizes and semantics must be equivalent!

## [◆ ](#ga1d9ed5b5006579e7c452a6f15418849b)STRUCT\_SECTION\_ITERABLE\_ARRAY

| #define STRUCT\_SECTION\_ITERABLE\_ARRAY | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *varname*, |
|  |  |  | *size* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE](#ga2013cfe23c77c472f6fc43ccc99ac228)(struct\_type, struct\_type, \

varname, size)

[STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE](#ga2013cfe23c77c472f6fc43ccc99ac228)

#define STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE(secname, struct\_type, varname, size)

Defines an array of elements of alternate data type for an iterable section.

**Definition** iterable\_sections.h:197

Defines an array of elements for an iterable section.

See also
:   [STRUCT\_SECTION\_ITERABLE](#ga9104f42cbe4a67a931bed7f7cc8f600f)

## [◆ ](#ga2013cfe23c77c472f6fc43ccc99ac228)STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE

| #define STRUCT\_SECTION\_ITERABLE\_ARRAY\_ALTERNATE | ( |  | *secname*, |
| --- | --- | --- | --- |
|  |  |  | *struct\_type*, |
|  |  |  | *varname*, |
|  |  |  | *size* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)(struct struct\_type, varname[size], secname, \

varname)

Defines an array of elements of alternate data type for an iterable section.

See also
:   [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](#gae08ef16db3e04967fdca69a19ca4c70b)

## [◆ ](#gada3ff915b4ed4881a61b79d8877131e2)STRUCT\_SECTION\_ITERABLE\_NAMED

| #define STRUCT\_SECTION\_ITERABLE\_NAMED | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *varname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)(struct struct\_type, varname, struct\_type, name)

Defines a new element for an iterable section with a custom name.

The name can be used to customize how iterable section entries are sorted.

See also
:   [STRUCT\_SECTION\_ITERABLE()](#ga9104f42cbe4a67a931bed7f7cc8f600f)

## [◆ ](#ga5c2441634885ac7c5c15e5cfe159b2fd)STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE

| #define STRUCT\_SECTION\_ITERABLE\_NAMED\_ALTERNATE | ( |  | *struct\_type*, |
| --- | --- | --- | --- |
|  |  |  | *secname*, |
|  |  |  | *name*, |
|  |  |  | *varname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_ITERABLE](#gac5177fefd615bdd3025fac742d414808)(struct struct\_type, varname, secname, name)

Defines a new element for an iterable section with a custom name, placed in a custom section.

The name can be used to customize how iterable section entries are sorted.

See also
:   [STRUCT\_SECTION\_ITERABLE\_NAMED()](#gada3ff915b4ed4881a61b79d8877131e2)

## [◆ ](#ga53b4dd9b989b54d62254b425a23620f0)STRUCT\_SECTION\_START

| #define STRUCT\_SECTION\_START | ( |  | *struct\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(struct\_type)

[TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)

#define TYPE\_SECTION\_START(secname)

iterable section start symbol for a generic type

**Definition** iterable\_sections.h:55

iterable section start symbol for a struct type

Parameters
:   | [in] | struct\_type | data type of section |
    | --- | --- | --- |

## [◆ ](#ga4d61ce2fdd6e8d2881038e521d7aed54)STRUCT\_SECTION\_START\_EXTERN

| #define STRUCT\_SECTION\_START\_EXTERN | ( |  | *struct\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_START\_EXTERN](#ga40c6ba05d5bcb848a530bdc17bbff5be)(struct struct\_type, struct\_type)

[TYPE\_SECTION\_START\_EXTERN](#ga40c6ba05d5bcb848a530bdc17bbff5be)

#define TYPE\_SECTION\_START\_EXTERN(type, secname)

iterable section extern for start symbol for a generic type

**Definition** iterable\_sections.h:78

iterable section extern for start symbol for a struct

Helper macro to give extern for start of iterable section.

Parameters
:   | [in] | struct\_type | data type of section |
    | --- | --- | --- |

## [◆ ](#ga0c3da72ee4432a94242aaccf5cd5e9fb)TYPE\_SECTION\_COUNT

| #define TYPE\_SECTION\_COUNT | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *secname*, |
|  |  |  | *dst* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

do { \

TYPE\_SECTION\_START\_EXTERN(type, secname); \

TYPE\_SECTION\_END\_EXTERN(type, secname); \

\*(dst) = (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(secname) - \

([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname)) / sizeof(type); \

} while (0)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

Count elements in a section for a generic type.

Parameters
:   | [in] | type | type of element |
    | --- | --- | --- |
    | [in] | secname | name of output section |
    | [out] | dst | Pointer to location where result is written. |

## [◆ ](#ga14d6bc375423775e5484183eeadd1fad)TYPE\_SECTION\_END

| #define TYPE\_SECTION\_END | ( |  | *secname* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

\_CONCAT(\_##secname, \_list\_end)

iterable section end symbol for a generic type

will return '\_<SECNAME>\_list\_end'.

Parameters
:   | [in] | secname | type name of iterable section. For 'struct foobar' this would be [TYPE\_SECTION\_START(foobar)](#gac97b7f4fd42a2d9e11b6a585bc716a05) |
    | --- | --- | --- |

## [◆ ](#gaf009fe4b90f7b338c3bf85bb4cd682e5)TYPE\_SECTION\_END\_EXTERN

| #define TYPE\_SECTION\_END\_EXTERN | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *secname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

extern type [TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(secname)[]

iterable section extern for end symbol for a generic type

Helper macro to give extern for end of iterable section. The macro typically will be called [TYPE\_SECTION\_END\_EXTERN(struct foobar, foobar)](#gaf009fe4b90f7b338c3bf85bb4cd682e5). This allows the macro to hand different types as well as cases where the type and section name may differ.

Parameters
:   | [in] | type | data type of section |
    | --- | --- | --- |
    | [in] | secname | name of output section |

## [◆ ](#gac74c8d3f92304a7082d5c5c7c62dace7)TYPE\_SECTION\_FOREACH

| #define TYPE\_SECTION\_FOREACH | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *secname*, |
|  |  |  | *iterator* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

[TYPE\_SECTION\_START\_EXTERN](#ga40c6ba05d5bcb848a530bdc17bbff5be)(type, secname); \

TYPE\_SECTION\_END\_EXTERN(type, secname); \

for (type \* iterator = [TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname); ({ \

\_\_ASSERT(iterator <= [TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(secname),\

"unexpected list end location"); \

iterator < [TYPE\_SECTION\_END](#ga14d6bc375423775e5484183eeadd1fad)(secname); \

}); \

iterator++)

Iterate over a specified iterable section for a generic type.

Iterator for structure instances gathered by [TYPE\_SECTION\_ITERABLE()](#gac5177fefd615bdd3025fac742d414808). The linker must provide a \_<SECNAME>\_list\_start symbol and a \_<SECNAME>\_list\_end symbol to mark the start and the end of the list of struct objects to iterate over. This is normally done using [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0) in the linker script.

## [◆ ](#gae0f61156fa152ff5604087e2849caeb0)TYPE\_SECTION\_GET

| #define TYPE\_SECTION\_GET | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *secname*, |
|  |  |  | *i*, |
|  |  |  | *dst* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

do { \

TYPE\_SECTION\_START\_EXTERN(type, secname); \

\*(dst) = &[TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname)[i]; \

} while (0)

Get element from section for a generic type.

Note
:   There is no protection against reading beyond the section.

Parameters
:   | [in] | type | type of element |
    | --- | --- | --- |
    | [in] | secname | name of output section |
    | [in] | i | Index. |
    | [out] | dst | Pointer to location where pointer to element is written. |

## [◆ ](#gac5177fefd615bdd3025fac742d414808)TYPE\_SECTION\_ITERABLE

| #define TYPE\_SECTION\_ITERABLE | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *varname*, |
|  |  |  | *secname*, |
|  |  |  | *section\_postfix* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

Z\_DECL\_ALIGN(type) varname \

\_\_in\_section(\_##secname, static, \_CONCAT(section\_postfix, \_)) \_\_used \_\_noasan

Defines a new element for an iterable section for a generic type.

Convenience helper combining \_\_in\_section() and Z\_DECL\_ALIGN(). The section name will be '.[SECNAME].static.[SECTION\_POSTFIX]'

In the linker script, create output sections for these using [ITERABLE\_SECTION\_ROM()](#gaa83030f309052399a7d1f61c56a0c901) or [ITERABLE\_SECTION\_RAM()](#ga50d995ef13e80eb36cfc8556e39056d0).

Note
:   In order to store the element in ROM, a const specifier has to be added to the declaration: const [TYPE\_SECTION\_ITERABLE(...)](#gac5177fefd615bdd3025fac742d414808);

Parameters
:   | [in] | type | data type of variable |
    | --- | --- | --- |
    | [in] | varname | name of variable to place in section |
    | [in] | secname | type name of iterable section. |
    | [in] | section\_postfix | postfix to use in section name |

## [◆ ](#gac97b7f4fd42a2d9e11b6a585bc716a05)TYPE\_SECTION\_START

| #define TYPE\_SECTION\_START | ( |  | *secname* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

\_CONCAT(\_##secname, \_list\_start)

iterable section start symbol for a generic type

will return '\_[OUT\_TYPE]\_list\_start'.

Parameters
:   | [in] | secname | type name of iterable section. For 'struct foobar' this would be [TYPE\_SECTION\_START(foobar)](#gac97b7f4fd42a2d9e11b6a585bc716a05) |
    | --- | --- | --- |

## [◆ ](#ga40c6ba05d5bcb848a530bdc17bbff5be)TYPE\_SECTION\_START\_EXTERN

| #define TYPE\_SECTION\_START\_EXTERN | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *secname* ) |

`#include <[iterable_sections.h](sys_2iterable__sections_8h.md)>`

**Value:**

extern type [TYPE\_SECTION\_START](#gac97b7f4fd42a2d9e11b6a585bc716a05)(secname)[]

iterable section extern for start symbol for a generic type

Helper macro to give extern for start of iterable section. The macro typically will be called [TYPE\_SECTION\_START\_EXTERN(struct foobar, foobar)](#ga40c6ba05d5bcb848a530bdc17bbff5be). This allows the macro to hand different types as well as cases where the type and section name may differ.

Parameters
:   | [in] | type | data type of section |
    | --- | --- | --- |
    | [in] | secname | name of output section |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
