---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/uart__altera_8h_source.html
original_path: doxygen/html/uart__altera_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_altera.h

[Go to the documentation of this file.](uart__altera_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_DRIVERS\_SERIAL\_UART\_ALTERA\_H\_

12#define ZEPHYR\_DRIVERS\_SERIAL\_UART\_ALTERA\_H\_

13

14/\* End of packet feature.

15 \* Driver will trigger interrupt upon receiving end of package character.

16 \* Please enable CONFIG\_UART\_DRV\_CMD and CONFIG\_UART\_ALTERA\_EOP to use this feature.

17 \* Use the api: uart\_drv\_cmd with CMD\_ENABLE\_EOP to enable the feature.

18 \* This cmd will write the ip register and also set a flag to the driver.

19 \* The flag will modify uart\_irq\_callback\_user\_data\_set

20 \* to set call back function for eop interrupt.

21 \* Flag is cleared after uart\_irq\_callback\_user\_data\_set is called.

22 \*/

[ 23](uart__altera_8h.md#acd0b56a568b2ee566e3749a07baa4ded)#define CMD\_ENABLE\_EOP 0x01

[ 24](uart__altera_8h.md#adcc3a86b997151efa6970b2a12d4ecc2)#define CMD\_DISABLE\_EOP 0x02

25

26#endif /\* ZEPHYR\_DRIVERS\_SERIAL\_UART\_ALTERA\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [serial](dir_19e6ea47bd3dc215ff4232c3392e0b57.md)
- [uart\_altera.h](uart__altera_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
