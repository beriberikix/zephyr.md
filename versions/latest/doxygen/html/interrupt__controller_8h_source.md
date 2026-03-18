---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/interrupt__controller_8h_source.html
original_path: doxygen/html/interrupt__controller_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

interrupt\_controller.h

[Go to the documentation of this file.](interrupt__controller_8h.md)

1/\*

2 \* Copyright (c) 2024 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_INTERRUPT\_CONTROLLER\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_INTERRUPT\_CONTROLLER\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19#include <[zephyr/devicetree.h](devicetree_8h.md)>

20#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

21

27

[ 38](group__devicetree-interrupt__controller.md#ga4eebef2c5e75d6a6c87d0cea03ac1bee)#define DT\_INTC\_GET\_AGGREGATOR\_LEVEL(node\_id) UTIL\_INC(DT\_IRQ\_LEVEL(node\_id))

39

[ 50](group__devicetree-interrupt__controller.md#ga914952a10c55fecc1f6e7c0cc3685b1b)#define DT\_INST\_INTC\_GET\_AGGREGATOR\_LEVEL(inst) DT\_INTC\_GET\_AGGREGATOR\_LEVEL(DT\_DRV\_INST(inst))

51

55

56#ifdef \_\_cplusplus

57}

58#endif

59

60#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_INTERRUPT\_CONTROLLER\_H\_ \*/

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [interrupt\_controller.h](interrupt__controller_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
