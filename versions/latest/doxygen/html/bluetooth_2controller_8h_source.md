---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bluetooth_2controller_8h_source.html
original_path: doxygen/html/bluetooth_2controller_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

controller.h

[Go to the documentation of this file.](bluetooth_2controller_8h.md)

1

4

5/\*

6 \* Copyright (c) 2018 Codecoup

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_CONTROLLER\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_CONTROLLER\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 32](group__bt__ctrl.md#ga541cabe76fd3cb019aae2fe01d45cbfc)void [bt\_ctlr\_set\_public\_addr](group__bt__ctrl.md#ga541cabe76fd3cb019aae2fe01d45cbfc)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr);

33

34#ifdef \_\_cplusplus

35}

36#endif

40

41#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_CONTROLLER\_H\_ \*/

[bt\_ctlr\_set\_public\_addr](group__bt__ctrl.md#ga541cabe76fd3cb019aae2fe01d45cbfc)

void bt\_ctlr\_set\_public\_addr(const uint8\_t \*addr)

Set public address for controller.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [controller.h](bluetooth_2controller_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
