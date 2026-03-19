---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__battery__apis.html
original_path: doxygen/html/group__battery__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

battery APIs

battery API
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BATTERY\_OCV\_TABLE\_LEN](#ga02de0e4f76b8e5804b82cd397c13ef86)   11 |
| #define | [BATTERY\_CHEMISTRY\_DT\_GET](#gae2c365581f7c8c71e1ec31b223545711)(node\_id) |
|  | Get the battery chemistry enum value. |
| #define | [BATTERY\_OCV\_TABLE\_DT\_GET](#ga833bf8bf88136fd277a69fb41ad0fb7f)(node\_id, table) |
|  | Get the OCV curve for a given table. |

| Enumerations | |
| --- | --- |
| enum | [battery\_chemistry](#gaf7ee6b6e85da9f31231cac577428de01) {     [BATTERY\_CHEMISTRY\_UNKNOWN](#ggaf7ee6b6e85da9f31231cac577428de01a52bae762c2ef4ca140c1e7f89440b007) = 0 , [BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM](#ggaf7ee6b6e85da9f31231cac577428de01a00f07b177e6246e139b469386064698f) , [BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE](#ggaf7ee6b6e85da9f31231cac577428de01a377834c71930068b6a822d4afd2112f4) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION](#ggaf7ee6b6e85da9f31231cac577428de01a450162d694da85864af48712cb05badd) ,     [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER](#ggaf7ee6b6e85da9f31231cac577428de01ab21f5e769426047924d83e5301b8a19f) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE](#ggaf7ee6b6e85da9f31231cac577428de01a951b3bea1c503ce6f1d78e8cc1ed9e37) , [BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE](#ggaf7ee6b6e85da9f31231cac577428de01a30cd5d02bb416248b9380ab953836e96)   } |

| Functions | |
| --- | --- |
| static [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [battery\_soc\_lookup](#gaea81fb0c63b85654005b6f65521c3345) (const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ocv\_table[11], [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) voltage\_uv) |
|  | Convert an OCV table and battery voltage to a charge percentage. |

## Detailed Description

battery API

## Macro Definition Documentation

## [◆ ](#gae2c365581f7c8c71e1ec31b223545711)BATTERY\_CHEMISTRY\_DT\_GET

| #define BATTERY\_CHEMISTRY\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[battery.h](drivers_2sensor_2battery_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(BATTERY\_CHEMISTRY\_, [DT\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)(node\_id, device\_chemistry, UNKNOWN))

[DT\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)

#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value)

Like DT\_STRING\_UPPER\_TOKEN(), but with a fallback to default\_value.

**Definition** devicetree.h:1210

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Get the battery chemistry enum value.

Parameters
:   | node\_id | node identifier |
    | --- | --- |

## [◆ ](#ga833bf8bf88136fd277a69fb41ad0fb7f)BATTERY\_OCV\_TABLE\_DT\_GET

| #define BATTERY\_OCV\_TABLE\_DT\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *table* ) |

`#include <[battery.h](drivers_2sensor_2battery_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, table), \

({[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, table, [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461), (,))}), ({-1}))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3784

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3367

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:908

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get the OCV curve for a given table.

Parameters
:   | node\_id | node identifier |
    | --- | --- |
    | table | table to retrieve |

## [◆ ](#ga02de0e4f76b8e5804b82cd397c13ef86)BATTERY\_OCV\_TABLE\_LEN

| #define BATTERY\_OCV\_TABLE\_LEN   11 |
| --- |

`#include <[battery.h](drivers_2sensor_2battery_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gaf7ee6b6e85da9f31231cac577428de01)battery\_chemistry

| enum [battery\_chemistry](#gaf7ee6b6e85da9f31231cac577428de01) |
| --- |

`#include <[battery.h](drivers_2sensor_2battery_8h.md)>`

| Enumerator | |
| --- | --- |
| BATTERY\_CHEMISTRY\_UNKNOWN |  |
| BATTERY\_CHEMISTRY\_NICKEL\_CADMIUM |  |
| BATTERY\_CHEMISTRY\_NICKEL\_METAL\_HYDRIDE |  |
| BATTERY\_CHEMISTRY\_LITHIUM\_ION |  |
| BATTERY\_CHEMISTRY\_LITHIUM\_ION\_POLYMER |  |
| BATTERY\_CHEMISTRY\_LITHIUM\_ION\_IRON\_PHOSPHATE |  |
| BATTERY\_CHEMISTRY\_LITHIUM\_ION\_MANGANESE\_OXIDE |  |

## Function Documentation

## [◆ ](#gaea81fb0c63b85654005b6f65521c3345)battery\_soc\_lookup()

| | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) battery\_soc\_lookup | ( | const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *ocv\_table*[11], | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *voltage\_uv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[battery.h](drivers_2sensor_2battery_8h.md)>`

Convert an OCV table and battery voltage to a charge percentage.

Parameters
:   | ocv\_table | Open circuit voltage curve |
    | --- | --- |
    | voltage\_uv | Battery voltage in microVolts |

Returns
:   Battery state of charge in milliPercent

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
