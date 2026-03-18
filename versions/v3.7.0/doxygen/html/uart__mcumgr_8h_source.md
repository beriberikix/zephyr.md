---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/uart__mcumgr_8h_source.html
original_path: doxygen/html/uart__mcumgr_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart\_mcumgr.h

[Go to the documentation of this file.](uart__mcumgr_8h.md)

1/\*

2 \* Copyright Runtime.io 2018. All rights reserved.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_UART\_MCUMGR\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_UART\_MCUMGR\_H\_

15

16#include <[stdlib.h](stdlib_8h.md)>

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 26](structuart__mcumgr__rx__buf.md)struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) {

[ 27](structuart__mcumgr__rx__buf.md#a8484b842ce240d35dff22f704617d22d) void \*[fifo\_reserved](structuart__mcumgr__rx__buf.md#a8484b842ce240d35dff22f704617d22d); /\* 1st word reserved for use by fifo \*/

[ 28](structuart__mcumgr__rx__buf.md#a81696c833e2955e6888fcd439a59f786) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structuart__mcumgr__rx__buf.md#a81696c833e2955e6888fcd439a59f786)[CONFIG\_UART\_MCUMGR\_RX\_BUF\_SIZE];

[ 29](structuart__mcumgr__rx__buf.md#a6495e78b7f249c6b073c4b0e1c25160a) int [length](structuart__mcumgr__rx__buf.md#a6495e78b7f249c6b073c4b0e1c25160a);

30};

31

[ 41](uart__mcumgr_8h.md#a0173a370be3e424b56cdfbb3d4174da1)typedef void [uart\_mcumgr\_recv\_fn](uart__mcumgr_8h.md#a0173a370be3e424b56cdfbb3d4174da1)(struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \*rx\_buf);

42

[ 51](uart__mcumgr_8h.md#acf906a316bf77fc5cc8768130ce82e66)int [uart\_mcumgr\_send](uart__mcumgr_8h.md#acf906a316bf77fc5cc8768130ce82e66)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, int len);

52

[ 58](uart__mcumgr_8h.md#ae173ad28a0301c8ddfdd9b8bc5583ba3)void [uart\_mcumgr\_free\_rx\_buf](uart__mcumgr_8h.md#ae173ad28a0301c8ddfdd9b8bc5583ba3)(struct [uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md) \*rx\_buf);

59

[ 69](uart__mcumgr_8h.md#a2b31278c4e600bcd10d1a069cc6f5655)void [uart\_mcumgr\_register](uart__mcumgr_8h.md#a2b31278c4e600bcd10d1a069cc6f5655)([uart\_mcumgr\_recv\_fn](uart__mcumgr_8h.md#a0173a370be3e424b56cdfbb3d4174da1) \*cb);

70

71#ifdef \_\_cplusplus

72}

73#endif

74

75#endif

[types.h](include_2zephyr_2types_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[stdlib.h](stdlib_8h.md)

[uart\_mcumgr\_rx\_buf](structuart__mcumgr__rx__buf.md)

Contains an mcumgr fragment received over UART.

**Definition** uart\_mcumgr.h:26

[uart\_mcumgr\_rx\_buf::length](structuart__mcumgr__rx__buf.md#a6495e78b7f249c6b073c4b0e1c25160a)

int length

**Definition** uart\_mcumgr.h:29

[uart\_mcumgr\_rx\_buf::data](structuart__mcumgr__rx__buf.md#a81696c833e2955e6888fcd439a59f786)

uint8\_t data[CONFIG\_UART\_MCUMGR\_RX\_BUF\_SIZE]

**Definition** uart\_mcumgr.h:28

[uart\_mcumgr\_rx\_buf::fifo\_reserved](structuart__mcumgr__rx__buf.md#a8484b842ce240d35dff22f704617d22d)

void \* fifo\_reserved

**Definition** uart\_mcumgr.h:27

[uart\_mcumgr\_recv\_fn](uart__mcumgr_8h.md#a0173a370be3e424b56cdfbb3d4174da1)

void uart\_mcumgr\_recv\_fn(struct uart\_mcumgr\_rx\_buf \*rx\_buf)

Function that gets called when an mcumgr packet is received.

**Definition** uart\_mcumgr.h:41

[uart\_mcumgr\_register](uart__mcumgr_8h.md#a2b31278c4e600bcd10d1a069cc6f5655)

void uart\_mcumgr\_register(uart\_mcumgr\_recv\_fn \*cb)

Registers an mcumgr UART receive handler.

[uart\_mcumgr\_send](uart__mcumgr_8h.md#acf906a316bf77fc5cc8768130ce82e66)

int uart\_mcumgr\_send(const uint8\_t \*data, int len)

Sends an mcumgr packet over UART.

[uart\_mcumgr\_free\_rx\_buf](uart__mcumgr_8h.md#ae173ad28a0301c8ddfdd9b8bc5583ba3)

void uart\_mcumgr\_free\_rx\_buf(struct uart\_mcumgr\_rx\_buf \*rx\_buf)

Frees the supplied receive buffer.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [uart\_mcumgr.h](uart__mcumgr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
