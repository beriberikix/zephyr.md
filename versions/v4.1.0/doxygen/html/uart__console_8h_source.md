---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uart__console_8h_source.html
original_path: doxygen/html/uart__console_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_console.h

[Go to the documentation of this file.](uart__console_8h.md)

1/\* uart\_console.h - uart console driver \*/

2

3/\*

4 \* Copyright (c) 2011, 2014 Wind River Systems, Inc.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_UART\_CONSOLE\_H\_

10#define ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_UART\_CONSOLE\_H\_

11

12#include <[zephyr/kernel.h](kernel_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 30](uart__console_8h.md#a090eed88ce36e49ecea535d61746abd5)void [uart\_register\_input](uart__console_8h.md#a090eed88ce36e49ecea535d61746abd5)(struct [k\_fifo](structk__fifo.md) \*avail, struct [k\_fifo](structk__fifo.md) \*lines,

31 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*completion)(char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len));

32

33/\*

34 \* Allows having debug hooks in the console driver for handling incoming

35 \* control characters, and letting other ones through.

36 \*/

37#ifdef CONFIG\_UART\_CONSOLE\_DEBUG\_SERVER\_HOOKS

38#define UART\_CONSOLE\_DEBUG\_HOOK\_HANDLED 1

39#define UART\_CONSOLE\_OUT\_DEBUG\_HOOK\_SIG(x) int(x)(char c)

40typedef UART\_CONSOLE\_OUT\_DEBUG\_HOOK\_SIG(uart\_console\_out\_debug\_hook\_t);

41

42void uart\_console\_out\_debug\_hook\_install(

43 uart\_console\_out\_debug\_hook\_t \*hook);

44

45typedef int (\*uart\_console\_in\_debug\_hook\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d));

46

47void uart\_console\_in\_debug\_hook\_install(uart\_console\_in\_debug\_hook\_t hook);

48

49#endif

50

51#ifdef \_\_cplusplus

52}

53#endif

54

55#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_UART\_CONSOLE\_H\_ \*/

[kernel.h](kernel_8h.md)

Public kernel APIs.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2495

[uart\_register\_input](uart__console_8h.md#a090eed88ce36e49ecea535d61746abd5)

void uart\_register\_input(struct k\_fifo \*avail, struct k\_fifo \*lines, uint8\_t(\*completion)(char \*str, uint8\_t len))

Register uart input processing.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_console.h](uart__console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
