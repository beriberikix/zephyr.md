---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2console_2console_8h_source.html
original_path: doxygen/html/drivers_2console_2console_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

console.h

[Go to the documentation of this file.](drivers_2console_2console_8h.md)

1/\*

2 \* Copyright (c) 2017 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_CONSOLE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_CONSOLE\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 14](drivers_2console_2console_8h.md#ae5aa23edbc2609d1b766340c14fd5a68)#define CONSOLE\_MAX\_LINE\_LEN CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN

15

[ 21](structconsole__input.md)struct [console\_input](structconsole__input.md) {

23 [intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c) \_unused;

[ 25](structconsole__input.md#a2c13a1e2a4895cf1d51c8ce7879af927) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_mcumgr](structconsole__input.md#a2c13a1e2a4895cf1d51c8ce7879af927) : 1;

[ 27](structconsole__input.md#a33bf8ba6d114ec99219c134c0f6c3474) char [line](structconsole__input.md#a33bf8ba6d114ec99219c134c0f6c3474)[[CONSOLE\_MAX\_LINE\_LEN](drivers_2console_2console_8h.md#ae5aa23edbc2609d1b766340c14fd5a68)];

28};

29

[ 42](drivers_2console_2console_8h.md#a0dab6d89950bb4c2bbb17571b9b1461f)typedef void (\*[console\_input\_fn](drivers_2console_2console_8h.md#a0dab6d89950bb4c2bbb17571b9b1461f))(struct [k\_fifo](structk__fifo.md) \*avail, struct [k\_fifo](structk__fifo.md) \*lines,

43 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*completion)(char \*str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len));

44

45#ifdef \_\_cplusplus

46}

47#endif

48

49#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_CONSOLE\_CONSOLE\_H\_ \*/

[console\_input\_fn](drivers_2console_2console_8h.md#a0dab6d89950bb4c2bbb17571b9b1461f)

void(\* console\_input\_fn)(struct k\_fifo \*avail, struct k\_fifo \*lines, uint8\_t(\*completion)(char \*str, uint8\_t len))

Console input processing handler signature.

**Definition** console.h:42

[CONSOLE\_MAX\_LINE\_LEN](drivers_2console_2console_8h.md#ae5aa23edbc2609d1b766340c14fd5a68)

#define CONSOLE\_MAX\_LINE\_LEN

**Definition** console.h:14

[intptr\_t](stdint_8h.md#a0bd5dec00e345e69027427f8621d6a6c)

\_\_INTPTR\_TYPE\_\_ intptr\_t

**Definition** stdint.h:104

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[console\_input](structconsole__input.md)

Console input representation.

**Definition** console.h:21

[console\_input::is\_mcumgr](structconsole__input.md#a2c13a1e2a4895cf1d51c8ce7879af927)

uint8\_t is\_mcumgr

Whether this is an mcumgr command.

**Definition** console.h:25

[console\_input::line](structconsole__input.md#a33bf8ba6d114ec99219c134c0f6c3474)

char line[CONFIG\_CONSOLE\_INPUT\_MAX\_LINE\_LEN]

Buffer where the input line is recorded.

**Definition** console.h:27

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2495

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [console](dir_5678202c8994e72aafde82bf91697a82.md)
- [console.h](drivers_2console_2console_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
