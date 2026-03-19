---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/current__sense__amplifier_8h.html
original_path: doxygen/html/current__sense__amplifier_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

current\_sense\_amplifier.h File Reference

`#include <[zephyr/drivers/adc.h](drivers_2adc_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`

[Go to the source code of this file.](current__sense__amplifier_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) |

| Macros | |
| --- | --- |
| #define | [CURRENT\_SENSE\_AMPLIFIER\_DT\_SPEC\_GET](#a17093e63c3ccd1e08e38ad1e0aeb9d8c)(node\_id) |
|  | Get current sensor information from devicetree. |

| Functions | |
| --- | --- |
| static void | [current\_sense\_amplifier\_scale\_dt](#aeaa2149527103e5c0e6a636cb3e9aad4) (const struct [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_i) |
|  | Calculates the actual amperage from the measured voltage. |

## Macro Definition Documentation

## [◆ ](#a17093e63c3ccd1e08e38ad1e0aeb9d8c)CURRENT\_SENSE\_AMPLIFIER\_DT\_SPEC\_GET

| #define CURRENT\_SENSE\_AMPLIFIER\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.port = [ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)(node\_id), \

.sense\_milli\_ohms = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, sense\_resistor\_milli\_ohms), \

.sense\_gain\_mult = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, sense\_gain\_mult), \

.sense\_gain\_div = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, sense\_gain\_div), \

.power\_gpio = [GPIO\_DT\_SPEC\_GET\_OR](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)(node\_id, power\_gpios, {0}), \

}

[ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)

#define ADC\_DT\_SPEC\_GET(node\_id)

Equivalent to ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0).

**Definition** adc.h:517

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[GPIO\_DT\_SPEC\_GET\_OR](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)

#define GPIO\_DT\_SPEC\_GET\_OR(node\_id, prop, default\_value)

Equivalent to GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value).

**Definition** gpio.h:382

Get current sensor information from devicetree.

This returns a static initializer for a `[current_sense_amplifier_dt_spec](structcurrent__sense__amplifier__dt__spec.md)` structure given a devicetree node.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for an [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) structure.

## Function Documentation

## [◆ ](#aeaa2149527103e5c0e6a636cb3e9aad4)current\_sense\_amplifier\_scale\_dt()

| | void current\_sense\_amplifier\_scale\_dt | ( | const struct [current\_sense\_amplifier\_dt\_spec](structcurrent__sense__amplifier__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *v\_to\_i* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Calculates the actual amperage from the measured voltage.

Parameters
:   | [in] | spec | current sensor specification from Devicetree. |
    | --- | --- | --- |
    | [in,out] | v\_to\_i | Pointer to the measured voltage in millivolts on input, and the corresponding scaled current value in milliamps on output. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [current\_sense\_amplifier.h](current__sense__amplifier_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
