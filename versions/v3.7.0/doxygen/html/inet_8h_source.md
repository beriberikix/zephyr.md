---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/inet_8h_source.html
original_path: doxygen/html/inet_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inet.h

[Go to the documentation of this file.](inet_8h.md)

1/\*

2 \* Copyright (c) 2019 Linaro Limited

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_

7#define ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_

8

9#include <stddef.h>

10

11#include <[zephyr/posix/netinet/in.h](in_8h.md)>

12#include <[zephyr/posix/sys/socket.h](posix_2sys_2socket_8h.md)>

13

14#include <[zephyr/net/socket.h](net_2socket_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](inet_8h.md#a98b38134a62f24554da0ffcabde8062c)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [in\_addr\_t](inet_8h.md#a98b38134a62f24554da0ffcabde8062c);

21

[ 22](inet_8h.md#a3e3b8f43e05dc3b87977b6a7a2ed09ca)[in\_addr\_t](inet_8h.md#a98b38134a62f24554da0ffcabde8062c) [inet\_addr](inet_8h.md#a3e3b8f43e05dc3b87977b6a7a2ed09ca)(const char \*cp);

[ 23](inet_8h.md#ab1d195e3682f88d1cea726e8c1de08d2)char \*[inet\_ntoa](inet_8h.md#ab1d195e3682f88d1cea726e8c1de08d2)(struct [in\_addr](structin__addr.md) in);

[ 24](inet_8h.md#ae93e32740fb355baef0cab02133e7ff4)char \*[inet\_ntop](inet_8h.md#ae93e32740fb355baef0cab02133e7ff4)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const void \*src, char \*dst, size\_t size);

[ 25](inet_8h.md#aabfaede889b4bc47241ab0c49a7a3cab)int [inet\_pton](inet_8h.md#aabfaede889b4bc47241ab0c49a7a3cab)([sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda) family, const char \*src, void \*dst);

26

27#ifdef \_\_cplusplus

28}

29#endif

30

31#endif /\* ZEPHYR\_INCLUDE\_POSIX\_ARPA\_INET\_H\_ \*/

[sa\_family\_t](group__ip__4__6.md#ga2d9e094abb99ebd0874373edf1c45eda)

unsigned short int sa\_family\_t

Socket address family type.

**Definition** net\_ip.h:164

[in.h](in_8h.md)

[inet\_addr](inet_8h.md#a3e3b8f43e05dc3b87977b6a7a2ed09ca)

in\_addr\_t inet\_addr(const char \*cp)

[in\_addr\_t](inet_8h.md#a98b38134a62f24554da0ffcabde8062c)

uint32\_t in\_addr\_t

**Definition** inet.h:20

[inet\_pton](inet_8h.md#aabfaede889b4bc47241ab0c49a7a3cab)

int inet\_pton(sa\_family\_t family, const char \*src, void \*dst)

[inet\_ntoa](inet_8h.md#ab1d195e3682f88d1cea726e8c1de08d2)

char \* inet\_ntoa(struct in\_addr in)

[inet\_ntop](inet_8h.md#ae93e32740fb355baef0cab02133e7ff4)

char \* inet\_ntop(sa\_family\_t family, const void \*src, char \*dst, size\_t size)

[socket.h](net_2socket_8h.md)

BSD Sockets compatible API definitions.

[socket.h](posix_2sys_2socket_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[in\_addr](structin__addr.md)

IPv4 address struct.

**Definition** net\_ip.h:151

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [posix](dir_cc2c191bc57cea4eaf0dbdf53c4fb6c6.md)
- [arpa](dir_600f14fff2b86b8fd0090e7f273e0e80.md)
- [inet.h](inet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
