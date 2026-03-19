---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/voltage__divider_8h.html
original_path: doxygen/html/voltage__divider_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

voltage\_divider.h File Reference

`#include <[zephyr/drivers/adc.h](drivers_2adc_8h_source.md)>`

[Go to the source code of this file.](voltage__divider_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) |

| Macros | |
| --- | --- |
| #define | [VOLTAGE\_DIVIDER\_DT\_SPEC\_GET](#a4ed91297930bbf6b865075a9e9ba2bce)(node\_id) |
|  | Get voltage divider information from devicetree. |

| Functions | |
| --- | --- |
| static int | [voltage\_divider\_scale\_dt](#a891c6ee6073582761e63cadeaf228563) (const struct [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) \*spec, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*v\_to\_v) |
|  | Calculates the actual voltage from the measured voltage. |

## Macro Definition Documentation

## [◆ ](#a4ed91297930bbf6b865075a9e9ba2bce)VOLTAGE\_DIVIDER\_DT\_SPEC\_GET

| #define VOLTAGE\_DIVIDER\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

.port = [ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)(node\_id), \

.full\_ohms = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, full\_ohms, 0), \

.output\_ohms = [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, output\_ohms), \

}

[ADC\_DT\_SPEC\_GET](group__adc__interface.md#gad05df3d329ba785c094ea4c32e2913b7)

#define ADC\_DT\_SPEC\_GET(node\_id)

Equivalent to ADC\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0).

**Definition** adc.h:516

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:907

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:745

Get voltage divider information from devicetree.

This returns a static initializer for a `[voltage_divider_dt_spec](structvoltage__divider__dt__spec.md)` structure given a devicetree node.

Parameters
:   | node\_id | Devicetree node identifier. |
    | --- | --- |

Returns
:   Static initializer for an [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) structure.

## Function Documentation

## [◆ ](#a891c6ee6073582761e63cadeaf228563)voltage\_divider\_scale\_dt()

| | int voltage\_divider\_scale\_dt | ( | const struct [voltage\_divider\_dt\_spec](structvoltage__divider__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *v\_to\_v* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Calculates the actual voltage from the measured voltage.

Parameters
:   | [in] | spec | voltage divider specification from Devicetree. |
    | --- | --- | --- |
    | [in,out] | v\_to\_v | Pointer to the measured voltage on input, and the corresponding scaled voltage value on output. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOTSUP | if "full\_ohms" is not specified |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [adc](dir_62d9a819ff274ddc8f9299d578f6ebce.md)
- [voltage\_divider.h](voltage__divider_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
