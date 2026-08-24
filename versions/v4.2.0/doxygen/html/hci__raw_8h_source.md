---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/hci__raw_8h_source.html
original_path: doxygen/html/hci__raw_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_raw.h

[Go to the documentation of this file.](hci__raw_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_

12

19

20#include <[stdint.h](stdint_8h.md)>

21#include <stddef.h>

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/net\_buf.h](net__buf_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

[ 39](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)int [bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)(struct [net\_buf](structnet__buf.md) \*buf);

40

[ 51](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)int [bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)(struct [k\_fifo](structk__fifo.md) \*rx\_queue);

52

53#ifdef \_\_cplusplus

54}

55#endif

59

60#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_HCI\_RAW\_H\_ \*/

[bt\_send](group__hci__raw.md#ga8de934e01eb9a16a3c9d096151e58313)

int bt\_send(struct net\_buf \*buf)

Send packet to the Bluetooth controller.

[bt\_enable\_raw](group__hci__raw.md#gaae30308fe69b1b2fd2972dbcd5a34d9f)

int bt\_enable\_raw(struct k\_fifo \*rx\_queue)

Enable Bluetooth RAW channel:

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[stdint.h](stdint_8h.md)

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2540

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_raw.h](hci__raw_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
