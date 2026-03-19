---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/input__touch_8h.html
original_path: doxygen/html/input__touch_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

input\_touch.h File Reference

`#include <[zephyr/input/input.h](input_8h_source.md)>`

[Go to the source code of this file.](input__touch_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [input\_touchscreen\_common\_config](structinput__touchscreen__common__config.md) |
|  | Common touchscreen config. [More...](structinput__touchscreen__common__config.md#details) |

| Macros | |
| --- | --- |
| #define | [INPUT\_TOUCH\_DT\_COMMON\_CONFIG\_INIT](group__touch__events.md#gae19dc2c40a8e14d28db614dfd4c5e32b)(node\_id) |
|  | Initialize common touchscreen config from devicetree. |
| #define | [INPUT\_TOUCH\_DT\_INST\_COMMON\_CONFIG\_INIT](group__touch__events.md#ga354195b719d526cebd63a061e8dc408b)(inst) |
|  | Initialize common touchscreen config from devicetree instance. |
| #define | [INPUT\_TOUCH\_STRUCT\_CHECK](group__touch__events.md#ga0b82cc636a4b686ee2948dc704fd06f0)(config) |
|  | Validate the offset of the common config structure. |

| Functions | |
| --- | --- |
| void | [input\_touchscreen\_report\_pos](group__touch__events.md#ga646bb86aa9f942fc3065381bd19e545c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) y, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Common utility for reporting touchscreen position events. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [input](dir_ecfb5c4fcc1ee7a8808d709654432824.md)
- [input\_touch.h](input__touch_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
