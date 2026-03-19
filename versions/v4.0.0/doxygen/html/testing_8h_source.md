---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/testing_8h_source.html
original_path: doxygen/html/testing_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

testing.h

[Go to the documentation of this file.](testing_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor ASA

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_

14

15#include <[zephyr/net\_buf.h](net__buf_8h.md)>

16

[ 25](testing_8h.md#ad881c44e84d8ba4650a33ef6bae19c4c)void [bt\_testing\_trace\_event\_acl\_pool\_destroy](testing_8h.md#ad881c44e84d8ba4650a33ef6bae19c4c)(struct [net\_buf](structnet__buf.md) \*buf);

26

27#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_ \*/

[net\_buf.h](net__buf_8h.md)

Buffer management.

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[bt\_testing\_trace\_event\_acl\_pool\_destroy](testing_8h.md#ad881c44e84d8ba4650a33ef6bae19c4c)

void bt\_testing\_trace\_event\_acl\_pool\_destroy(struct net\_buf \*buf)

Hook for acl\_in\_pool.destroy.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [testing.h](testing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
