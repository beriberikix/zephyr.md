---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lp50xx_8h_source.html
original_path: doxygen/html/lp50xx_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lp50xx.h

[Go to the documentation of this file.](lp50xx_8h.md)

1/\*

2 \* Copyright (c) 2020 Seagate Technology LLC

3 \* Copyright (c) 2022 Grinn

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_LED\_LP50XX\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_LED\_LP50XX\_H\_

11

[ 12](lp50xx_8h.md#a97594c95d9c99b55de0ef7e1624e44e4)#define LP50XX\_COLORS\_PER\_LED 3

13

[ 14](lp50xx_8h.md#a0cc3344b5a859f2463bda44624cdac6a)#define LP5009\_MAX\_LEDS 3

[ 15](lp50xx_8h.md#ad668908bcff262bf5a27c72cebeabb65)#define LP5012\_MAX\_LEDS 4

[ 16](lp50xx_8h.md#a2ca3a6eb319ad14279fca6115f5d4fca)#define LP5018\_MAX\_LEDS 6

[ 17](lp50xx_8h.md#a45b1d97cb6478e9231a2e22c99d27e6f)#define LP5024\_MAX\_LEDS 8

[ 18](lp50xx_8h.md#ad1c6c734b5222d0d96579c7efd96288f)#define LP5030\_MAX\_LEDS 10

[ 19](lp50xx_8h.md#a45f40ffa12fa78919030081bc158bdf5)#define LP5036\_MAX\_LEDS 12

20

21/\*

22 \* LED channels mapping.

23 \*/

24

25/\* Bank channels \*/

[ 26](lp50xx_8h.md#ad660acc79b6312608072cb21edc902d8)#define LP50XX\_BANK\_CHAN\_BASE 0

[ 27](lp50xx_8h.md#ac26b03a074670393b10826e35acc92e3)#define LP50XX\_BANK\_BRIGHT\_CHAN LP50XX\_BANK\_CHAN\_BASE

[ 28](lp50xx_8h.md#a3220c920a91992087a21fbbf160b5a71)#define LP50XX\_BANK\_COL1\_CHAN(led) (LP50XX\_BANK\_CHAN\_BASE + 1)

[ 29](lp50xx_8h.md#a17f11dcbce0cea164a4a506566ee81b9)#define LP50XX\_BANK\_COL2\_CHAN(led) (LP50XX\_BANK\_CHAN\_BASE + 2)

[ 30](lp50xx_8h.md#a9292372cafb9882f6e573063bdbaf99a)#define LP50XX\_BANK\_COL3\_CHAN(led) (LP50XX\_BANK\_CHAN\_BASE + 3)

31

32/\* LED brightness channels. \*/

[ 33](lp50xx_8h.md#aedaed7d9a9feb6c2e18ff646dd4f0741)#define LP50XX\_LED\_BRIGHT\_CHAN\_BASE 4

[ 34](lp50xx_8h.md#a7421dfa3aa4a135fa6d937d467ee7b44)#define LP50XX\_LED\_BRIGHT\_CHAN(led) (LP50XX\_LED\_BRIGHT\_CHAN\_BASE + led)

35

36/\*

37 \* LED color channels.

38 \*

39 \* Each channel definition is compatible with the following chips:

40 \* - LP5012\_XXX => LP5009 / LP5012

41 \* - LP5024\_XXX => LP5018 / LP5024

42 \* - LP5036\_XXX => LP5030 / LP5036

43 \*/

[ 44](lp50xx_8h.md#a46f005a17ecfeb7ea241d18ed2503029)#define LP5012\_LED\_COL\_CHAN\_BASE 8

[ 45](lp50xx_8h.md#ae1461195d755ea951b6bb2ce3f45392d)#define LP5012\_LED\_COL1\_CHAN(led) \

46 (LP5012\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED)

[ 47](lp50xx_8h.md#ab70cfd7eb411f1f2f6d8370452775ccd)#define LP5012\_LED\_COL2\_CHAN(led) \

48 (LP5012\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 1)

[ 49](lp50xx_8h.md#ae24a2d64b31fb8de59a119b6c1f63b15)#define LP5012\_LED\_COL3\_CHAN(led) \

50 (LP5012\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 2)

51

[ 52](lp50xx_8h.md#ac48720b13bd1aa213a4d4951ed96066a)#define LP5024\_LED\_COL\_CHAN\_BASE 12

[ 53](lp50xx_8h.md#ab86853d9f0417c2f1afba73cfacdfcd2)#define LP5024\_LED\_COL1\_CHAN(led) \

54 (LP5024\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED)

[ 55](lp50xx_8h.md#af0e0393357be9850c1944210f28aa32a)#define LP5024\_LED\_COL2\_CHAN(led) \

56 (LP5024\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 1)

[ 57](lp50xx_8h.md#a1df2b6f63b73b1b555a08e06f4da0c2d)#define LP5024\_LED\_COL3\_CHAN(led) \

58 (LP5024\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 2)

59

[ 60](lp50xx_8h.md#ae3dcf20db935d5cb64e62bffd44693d1)#define LP5036\_LED\_COL\_CHAN\_BASE 16

[ 61](lp50xx_8h.md#a24f8253051a6c6622c3c9d8c938a1c44)#define LP5036\_LED\_COL1\_CHAN(led) \

62 (LP5036\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED)

[ 63](lp50xx_8h.md#a72cfa3e69e9b9a7ee16a8dd243cc0782)#define LP5036\_LED\_COL2\_CHAN(led) \

64 (LP5036\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 1)

[ 65](lp50xx_8h.md#a4d4d92b15651f34f7c1d9747b10f4267)#define LP5036\_LED\_COL3\_CHAN(led) \

66 (LP5036\_LED\_COL\_CHAN\_BASE + led \* LP50XX\_COLORS\_PER\_LED + 2)

67

68#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_LED\_LP50XX\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [led](dir_c34d419ad899f160d883f47e8e6b2aca.md)
- [lp50xx.h](lp50xx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
