---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rx__cgc_8h.html
original_path: doxygen/html/renesas__rx__cgc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rx\_cgc.h File Reference

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`  
`#include <[zephyr/dt-bindings/clock/rx_clock.h](rx__clock_8h_source.md)>`

[Go to the source code of this file.](renesas__rx__cgc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [clock\_control\_rx\_pclk\_cfg](structclock__control__rx__pclk__cfg.md) |
| struct | [clock\_control\_rx\_subsys\_cfg](structclock__control__rx__subsys__cfg.md) |
| struct | [clock\_control\_rx\_pll\_cfg](structclock__control__rx__pll__cfg.md) |
| struct | [clock\_control\_rx\_pll\_data](structclock__control__rx__pll__data.md) |
| struct | [clock\_control\_rx\_root\_cfg](structclock__control__rx__root__cfg.md) |

| Macros | |
| --- | --- |
| #define | [RX\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR](#a722b55a0a83757487eff84b93fe90964)(node\_id, prop, default\_value) |
| #define | [RX\_CGC\_CLK\_SRC](#a7a7b76c8c7318a073b4f43f72d1d412f)(node\_id) |

## Macro Definition Documentation

## [◆ ](#a7a7b76c8c7318a073b4f43f72d1d412f)RX\_CGC\_CLK\_SRC

| #define RX\_CGC\_CLK\_SRC | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, okay), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(RX\_CLOCKS\_SOURCE\_, [DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)(node\_id))), \

(RX\_CLOCKS\_CLOCK\_DISABLED))

[DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)

#define DT\_NODE\_HAS\_STATUS(node\_id, status)

Does a node identifier refer to a node with a status?

**Definition** devicetree.h:3667

[DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)

#define DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN(node\_id)

Like DT\_NODE\_FULL\_NAME\_TOKEN(), but uppercased.

**Definition** devicetree.h:623

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

## [◆ ](#a722b55a0a83757487eff84b93fe90964)RX\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR

| #define RX\_CGC\_PROP\_HAS\_STATUS\_OKAY\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, okay), ([DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, prop)), (default\_value))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [renesas\_rx\_cgc.h](renesas__rx__cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
