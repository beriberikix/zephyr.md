---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2power_2atmel__sam__supc_8h_source.html
original_path: doxygen/html/drivers_2power_2atmel__sam__supc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

atmel\_sam\_supc.h

[Go to the documentation of this file.](drivers_2power_2atmel__sam__supc_8h.md)

1/\*

2 \* Copyright (c) 2023 Bjarki Arge Andreasen

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_POWER\_ATMEL\_SAM\_SUPC\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_POWER\_ATMEL\_SAM\_SUPC\_H\_

9

[ 10](drivers_2power_2atmel__sam__supc_8h.md#a694ffc7f2cd3ac2dad7a19111f983f5c)#define SAM\_DT\_SUPC\_CONTROLLER DEVICE\_DT\_GET(DT\_NODELABEL(supc))

11

[ 12](drivers_2power_2atmel__sam__supc_8h.md#a30156dd2f0f5f9a1daea631866f9fbb7)#define SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID(node\_id) \

13 DT\_PROP\_BY\_IDX(node\_id, wakeup\_source\_id wakeup\_source\_id)

14

[ 15](drivers_2power_2atmel__sam__supc_8h.md#ad12cd5eb9bcaea5ac08a39f1218dfff6)#define SAM\_DT\_INST\_SUPC\_WAKEUP\_SOURCE\_ID(inst) \

16 SAM\_DT\_SUPC\_WAKEUP\_SOURCE\_ID(DT\_DRV\_INST(inst))

17

18#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_POWER\_ATMEL\_SAM\_SUPC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [power](dir_0407a529497ae7b6e6f3b04cc7899a88.md)
- [atmel\_sam\_supc.h](drivers_2power_2atmel__sam__supc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
