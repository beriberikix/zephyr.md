---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__clock__control_8h.html
original_path: doxygen/html/nrf__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_clock\_control.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/onoff.h](onoff_8h_source.md)>`  
`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](nrf__clock__control_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NRF\_PERIPH\_GET\_FREQUENCY](#aab71ee0624ed3d35e089d4c095a3bcfc)(node) |
|  | Get clock frequency that is used for the given node. |

## Macro Definition Documentation

## [◆ ](#aab71ee0624ed3d35e089d4c095a3bcfc)NRF\_PERIPH\_GET\_FREQUENCY

| #define NRF\_PERIPH\_GET\_FREQUENCY | ( |  | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)(node, 0), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)([DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)(node), clock\_frequency), \

([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)(node), clock\_frequency)), \

([DT\_PROP\_LAST](group__devicetree-generic-prop.md#ga05a04871d83b31834c134a64636dcd8a)([DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)(node), supported\_clock\_frequency)))), \

(NRFX\_MHZ\_TO\_HZ(16)))

[DT\_CLOCKS\_CTLR](group__devicetree-clocks.md#ga69795ece1f4a46e2c26a8e2dbb452f23)

#define DT\_CLOCKS\_CTLR(node\_id)

Equivalent to DT\_CLOCKS\_CTLR\_BY\_IDX(node\_id, 0).

**Definition** clocks.h:146

[DT\_CLOCKS\_HAS\_IDX](group__devicetree-clocks.md#gabfdf51e2b14c05e84366cff1bb056da0)

#define DT\_CLOCKS\_HAS\_IDX(node\_id, idx)

Test if a node has a clocks phandle-array property at a given index.

**Definition** clocks.h:52

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3784

[DT\_PROP\_LAST](group__devicetree-generic-prop.md#ga05a04871d83b31834c134a64636dcd8a)

#define DT\_PROP\_LAST(node\_id, prop)

Get the last element of an array type property.

**Definition** devicetree.h:919

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

Get clock frequency that is used for the given node.

Macro checks if node has clock property and if yes then if clock has clock\_frequency property then it is returned. If it has supported\_clock\_frequency property with the list of supported frequencies then the last one is returned with assumption that they are ordered and the last one is the highest. If node does not have clock then 16 MHz is returned which is the default frequency.

Parameters
:   | node | Devicetree node. |
    | --- | --- |

Returns
:   Frequency of the clock that is used for the node.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [nrf\_clock\_control.h](nrf__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
