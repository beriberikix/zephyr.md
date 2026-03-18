---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/current__sense__shunt_8h.html
original_path: doxygen/html/current__sense__shunt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_shunt.h File Reference

`#include <[zephyr/drivers/adc.h](drivers_2adc_8h_source.md)>`

[Go to the source code of this file.](current__sense__shunt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) |

| Macros | |
| --- | --- |
| #define | [CURRENT\_SENSE\_SHUNT\_DT\_SPEC\_GET](#a104c330fc7acfd17c7778aef24f399b8)(node\_id) |
|  | Get current sensor information from devicetree. |

| Functions | |
| --- | --- |
| static void | [current\_sense\_shunt\_scale\_dt](#a2315a1aa2db9dafaff8c272b06d2c6b0) (const struct [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_i) |
|  | Calculates the actual amperage from the measured voltage. |

## Macro Definition Documentation

## [◆ ](#a104c330fc7acfd17c7778aef24f399b8)CURRENT\_SENSE\_SHUNT\_DT\_SPEC\_GET

| #define CURRENT\_SENSE\_SHUNT\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.port = [ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)(node\_id), \

.shunt\_micro\_ohms = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, shunt\_resistor\_micro\_ohms), \

}

[ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)

#define ADC\_DT\_SPEC\_GET(node\_id)

Equivalent to ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0).

**Definition** adc.h:414

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

Get current sensor information from devicetree.

This returns a static initializer for a `[current_sense_shunt_dt_spec](structcurrent__sense__shunt__dt__spec.md)` structure given a devicetree node.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for an [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) structure.

## Function Documentation

## [◆ ](#a2315a1aa2db9dafaff8c272b06d2c6b0)current\_sense\_shunt\_scale\_dt()

| | void current\_sense\_shunt\_scale\_dt | ( | const struct [current\_sense\_shunt\_dt\_spec](structcurrent__sense__shunt__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *v\_to\_i* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Calculates the actual amperage from the measured voltage.

Parameters
:   | [in] | spec | current sensor specification from Devicetree. |
    | --- | --- | --- |
    | [in,out] | v\_to\_i | Pointer to the measured voltage in millivolts on input, and the corresponding scaled current value in milliamps on output. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [current\_sense\_shunt.h](current__sense__shunt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
