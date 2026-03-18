---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/modem_2stats_8h_source.html
original_path: doxygen/html/modem_2stats_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stats.h

[Go to the documentation of this file.](modem_2stats_8h.md)

1/\*

2 \* Copyright (c) 2024 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

8#include <[zephyr/kernel.h](kernel_8h.md)>

9

10#ifndef ZEPHYR\_MODEM\_STATS\_

11#define ZEPHYR\_MODEM\_STATS\_

12

16

18struct modem\_stats\_buffer {

19 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

20 char name[CONFIG\_MODEM\_STATS\_BUFFER\_NAME\_SIZE];

21 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_used;

22 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size;

23};

24

28

[ 36](modem_2stats_8h.md#ac97a44071b31768bd2d39bef27bfd746)void [modem\_stats\_buffer\_init](modem_2stats_8h.md#ac97a44071b31768bd2d39bef27bfd746)(struct modem\_stats\_buffer \*buffer,

37 const char \*name, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size);

38

[ 48](modem_2stats_8h.md#af4ccdf8a97586021431d858565a8f28f)void [modem\_stats\_buffer\_advertise\_length](modem_2stats_8h.md#af4ccdf8a97586021431d858565a8f28f)(struct modem\_stats\_buffer \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length);

49

50#endif /\* ZEPHYR\_MODEM\_STATS\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[modem\_stats\_buffer\_init](modem_2stats_8h.md#ac97a44071b31768bd2d39bef27bfd746)

void modem\_stats\_buffer\_init(struct modem\_stats\_buffer \*buffer, const char \*name, uint32\_t size)

Initialize modem statistics buffer.

[modem\_stats\_buffer\_advertise\_length](modem_2stats_8h.md#af4ccdf8a97586021431d858565a8f28f)

void modem\_stats\_buffer\_advertise\_length(struct modem\_stats\_buffer \*buffer, uint32\_t length)

Advertise modem statistics buffer size.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [stats.h](modem_2stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
