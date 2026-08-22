---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cobs_8h_source.html
original_path: doxygen/html/cobs_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cobs.h

[Go to the documentation of this file.](cobs_8h.md)

1/\*

2 \* Copyright (c) 2024 Kelly Helmut Lord

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DATA\_COBS\_H\_

8#define ZEPHYR\_INCLUDE\_DATA\_COBS\_H\_

9

10#include <stddef.h>

11#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

12#include <[zephyr/sys/util.h](sys_2util_8h.md)>

13#include <[zephyr/net\_buf.h](net__buf_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 19](cobs_8h.md#a67d201df9cea6c681ed537516dd1d35e)#define COBS\_DEFAULT\_DELIMITER 0x00

20

[ 24](cobs_8h.md#a016e001ca84dae52391b5bc22b5c92ad)#define COBS\_FLAG\_TRAILING\_DELIMITER BIT(8)

25

[ 31](cobs_8h.md#a5e05dfb0ac63e51372805f2241c90491)#define COBS\_FLAG\_CUSTOM\_DELIMITER(x) ((x) & 0xff)

32

44

[ 53](group__cobs.md#ga71047f135e408e95d83828e898e823b0)static inline size\_t [cobs\_max\_encoded\_len](group__cobs.md#ga71047f135e408e95d83828e898e823b0)(size\_t decoded\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

54{

55 if ([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) & [COBS\_FLAG\_TRAILING\_DELIMITER](cobs_8h.md#a016e001ca84dae52391b5bc22b5c92ad)) {

56 return decoded\_size + decoded\_size / 254 + 1 + 1;

57 } else {

58 return decoded\_size + decoded\_size / 254 + 1;

59 }

60}

61

73

[ 74](group__cobs.md#gadf39d47a13fe1e3b10bcc9208f5b4786)int [cobs\_encode](group__cobs.md#gadf39d47a13fe1e3b10bcc9208f5b4786)(struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

75

[ 87](group__cobs.md#gabb6193b8d15b33e5c739c9609376950f)int [cobs\_decode](group__cobs.md#gabb6193b8d15b33e5c739c9609376950f)(struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

88

90

91#ifdef \_\_cplusplus

92}

93#endif

94

95#endif /\* ZEPHYR\_INCLUDE\_DATA\_COBS\_H\_ \*/

[COBS\_FLAG\_TRAILING\_DELIMITER](cobs_8h.md#a016e001ca84dae52391b5bc22b5c92ad)

#define COBS\_FLAG\_TRAILING\_DELIMITER

Flag indicating that encode and decode should include an implicit end delimiter.

**Definition** cobs.h:24

[cobs\_max\_encoded\_len](group__cobs.md#ga71047f135e408e95d83828e898e823b0)

static size\_t cobs\_max\_encoded\_len(size\_t decoded\_size, uint32\_t flags)

Calculate maximum encoded buffer size.

**Definition** cobs.h:53

[cobs\_decode](group__cobs.md#gabb6193b8d15b33e5c739c9609376950f)

int cobs\_decode(struct net\_buf \*src, struct net\_buf \*dst, uint32\_t flags)

Standard COBS decoding.

[cobs\_encode](group__cobs.md#gadf39d47a13fe1e3b10bcc9208f5b4786)

int cobs\_encode(struct net\_buf \*src, struct net\_buf \*dst, uint32\_t flags)

Standard COBS encoding.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [data](dir_f6906818b29bc0a2a087f651f21ae7e0.md)
- [cobs.h](cobs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
