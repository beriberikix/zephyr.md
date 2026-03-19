---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/in_8h_source.html
original_path: doxygen/html/in_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

in.h

[Go to the documentation of this file.](in_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_NETINET\_IN\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_NETINET\_IN\_H\_

8

9#include <[stdint.h](stdint_8h.md)>

10

11#include <[zephyr/net/socket.h](net_2socket_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](in_8h.md#a979d51fa99f7145221b3ed1afff5b827)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [in\_port\_t](in_8h.md#a979d51fa99f7145221b3ed1afff5b827);

18typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [in\_addr\_t](inet_8h.md#a98b38134a62f24554da0ffcabde8062c);

19

20#ifdef \_\_cplusplus

21}

22#endif

23

24#endif /\* ZEPHYR\_INCLUDE\_POSIX\_NETINET\_IN\_H\_ \*/

[in\_port\_t](in_8h.md#a979d51fa99f7145221b3ed1afff5b827)

uint16\_t in\_port\_t

**Definition** in.h:17

[in\_addr\_t](inet_8h.md#a98b38134a62f24554da0ffcabde8062c)

uint32\_t in\_addr\_t

**Definition** inet.h:20

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [netinet](dir_9639d2a614ba5557e7c5696902b963eb.md)
- [in.h](in_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
