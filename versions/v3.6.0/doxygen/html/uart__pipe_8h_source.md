---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/uart__pipe_8h_source.html
original_path: doxygen/html/uart__pipe_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_pipe.h

[Go to the documentation of this file.](uart__pipe_8h.md)

1

7

8/\*

9 \* Copyright (c) 2015 Intel Corporation

10 \*

11 \* SPDX-License-Identifier: Apache-2.0

12 \*/

13

14#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_PIPE\_H\_

15#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_PIPE\_H\_

16

17#include <[stdlib.h](stdlib_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 35](uart__pipe_8h.md#a8a840645edad0e2ac3da6cfd6f09557f)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*(\*uart\_pipe\_recv\_cb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t \*[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394));

36

[ 45](uart__pipe_8h.md#a0ddac401c01681a22952ae792007b786)void [uart\_pipe\_register](uart__pipe_8h.md#a0ddac401c01681a22952ae792007b786)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len, [uart\_pipe\_recv\_cb](uart__pipe_8h.md#a8a840645edad0e2ac3da6cfd6f09557f) cb);

46

[ 56](uart__pipe_8h.md#a6136cfc4837939fd56243245f462cc0e)int [uart\_pipe\_send](uart__pipe_8h.md#a6136cfc4837939fd56243245f462cc0e)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len);

57

58#ifdef \_\_cplusplus

59}

60#endif

61

62#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_PIPE\_H\_ \*/

[off](asm-macro-32-bit-gnu_8h.md#adbc19a384ffe3a93866980a920b08394)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa off

**Definition** asm-macro-32-bit-gnu.h:17

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[stdlib.h](stdlib_8h.md)

[uart\_pipe\_register](uart__pipe_8h.md#a0ddac401c01681a22952ae792007b786)

void uart\_pipe\_register(uint8\_t \*buf, size\_t len, uart\_pipe\_recv\_cb cb)

Register UART application.

[uart\_pipe\_send](uart__pipe_8h.md#a6136cfc4837939fd56243245f462cc0e)

int uart\_pipe\_send(const uint8\_t \*data, int len)

Send data over UART.

[uart\_pipe\_recv\_cb](uart__pipe_8h.md#a8a840645edad0e2ac3da6cfd6f09557f)

uint8\_t \*(\* uart\_pipe\_recv\_cb)(uint8\_t \*buf, size\_t \*off)

Received data callback.

**Definition** uart\_pipe.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart\_pipe.h](uart__pipe_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
