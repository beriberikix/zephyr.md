---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/gpio__utils_8h.html
original_path: doxygen/html/gpio__utils_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio\_utils.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/drivers/gpio.h](drivers_2gpio_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/tracing/tracing.h](tracing_8h_source.md)>`

[Go to the source code of this file.](gpio__utils_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GPIO\_PORT\_PIN\_MASK\_FROM\_NGPIOS](#a696fbe0e6868902fbec77afc06f55e0a)(ngpios) |
| #define | [GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE](#a570c8e724c799b1bb0edeafa249d9730)(node\_id) |
|  | Makes a bitmask of allowed GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values. |
| #define | [GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_INST](#a34528b682ca57bfc77cef745ed235e04)(inst) |
|  | Make a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance's GPIO `"gpio-reserved-ranges"` and `"ngpios"` DT properties values. |

| Functions | |
| --- | --- |
| static int | [gpio\_manage\_callback](#ac9d36599625b79bd2ebb9f3603a2a122) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*callbacks, struct [gpio\_callback](structgpio__callback.md) \*callback, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) set) |
|  | Generic function to insert or remove a callback from a callback list. |
| static void | [gpio\_fire\_callbacks](#ac7193ccc60e2f1c62569f80cd9973702) ([sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*list, const struct [device](structdevice.md) \*port, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins) |
|  | Generic function to go through and fire callback from a callback list. |

## Macro Definition Documentation

## [◆ ](#a34528b682ca57bfc77cef745ed235e04)GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_INST

| #define GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE](#a570c8e724c799b1bb0edeafa249d9730)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE](#a570c8e724c799b1bb0edeafa249d9730)

#define GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE(node\_id)

Makes a bitmask of allowed GPIOs from the "gpio-reserved-ranges" and "ngpios" DT properties values.

**Definition** gpio\_utils.h:36

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Make a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance's GPIO `"gpio-reserved-ranges"` and `"ngpios"` DT properties values.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the bitmask of allowed gpios

See also
:   [GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC()](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49 "Makes a bitmask of allowed GPIOs from DT "gpio-reserved-ranges" property and "ngpios" argument.")

## [◆ ](#a570c8e724c799b1bb0edeafa249d9730)GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE

| #define GPIO\_PORT\_PIN\_MASK\_FROM\_DT\_NODE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)(node\_id, [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, ngpios))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)

#define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios)

Makes a bitmask of allowed GPIOs from DT "gpio-reserved-ranges" property and "ngpios" argument.

**Definition** gpio.h:658

Makes a bitmask of allowed GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values.

Parameters
:   | node\_id | GPIO controller node identifier. |
    | --- | --- |

Returns
:   the bitmask of allowed gpios

See also
:   [GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC()](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49 "Makes a bitmask of allowed GPIOs from DT "gpio-reserved-ranges" property and "ngpios" argument.")

## [◆ ](#a696fbe0e6868902fbec77afc06f55e0a)GPIO\_PORT\_PIN\_MASK\_FROM\_NGPIOS

| #define GPIO\_PORT\_PIN\_MASK\_FROM\_NGPIOS | ( |  | *ngpios* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f))((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1))1 << (ngpios)) - 1U))

[gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:234

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## Function Documentation

## [◆ ](#ac7193ccc60e2f1c62569f80cd9973702)gpio\_fire\_callbacks()

| | void gpio\_fire\_callbacks | ( | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | *list*, | | --- | --- | --- | --- | |  |  | const struct [device](structdevice.md) \* | *port*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *pins* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Generic function to go through and fire callback from a callback list.

Parameters
:   | list | A pointer on the gpio callback list |
    | --- | --- |
    | port | A pointer on the gpio driver instance |
    | pins | The actual pin mask that triggered the interrupt |

## [◆ ](#ac9d36599625b79bd2ebb9f3603a2a122)gpio\_manage\_callback()

| | int gpio\_manage\_callback | ( | [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \* | *callbacks*, | | --- | --- | --- | --- | |  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *set* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Generic function to insert or remove a callback from a callback list.

Parameters
:   | callbacks | A pointer to the original list of callbacks (can be NULL) |
    | --- | --- |
    | callback | A pointer of the callback to insert or remove from the list |
    | set | A boolean indicating insertion or removal of the callback |

Returns
:   0 on success, negative errno otherwise.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio](dir_8ea93591dc4d2721ca60eb3d6154d84b.md)
- [gpio\_utils.h](gpio__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
