---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bas_8h_source.html
original_path: doxygen/html/bas_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bas.h

[Go to the documentation of this file.](bas_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \* Copyright (c) 2016 Intel Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_

9#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_

10

20

21#include <[stdint.h](stdint_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 33](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_bas\_get\_battery\_level](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)(void);

34

[ 44](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)int [bt\_bas\_set\_battery\_level](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

45

46

47#ifdef \_\_cplusplus

48}

49#endif

50

54

55#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_BAS\_H\_ \*/

[bt\_bas\_set\_battery\_level](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba)

int bt\_bas\_set\_battery\_level(uint8\_t level)

Update battery level value.

[bt\_bas\_get\_battery\_level](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980)

uint8\_t bt\_bas\_get\_battery\_level(void)

Read battery level value.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [bas.h](bas_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
