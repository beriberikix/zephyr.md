---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/__types_8h_source.html
original_path: doxygen/html/__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

\_types.h

[Go to the documentation of this file.](__types_8h.md)

1/\*

2 \* Copyright (c) 2019 Peter Bigot Consulting, LLC

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\* Common header used to define underlying types for typedefs that

8 \* must appear in multiple headers independently.

9 \*/

10#ifndef ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_XTYPES\_H\_

11#define ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_XTYPES\_H\_

12

13#include <[stdint.h](stdint_8h.md)>

14

15typedef [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \_TIME\_T\_;

16typedef [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \_SUSECONDS\_T\_;

17

18#endif /\* ZEPHYR\_LIB\_LIBC\_MINIMAL\_INCLUDE\_SYS\_XTYPES\_H\_ \*/

[stdint.h](stdint_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

- [lib](dir_97aefd0d527b934f1d99a682da8fe6a9.md)
- [libc](dir_b38b009475962ec458a8a4ac1c89fad6.md)
- [minimal](dir_cb013e9b53665816a2b0a66572d8a7af.md)
- [include](dir_33cd71cddfb4d86c87a49ac212c07c64.md)
- [sys](dir_4d70b020f8f8c9ca462b8905bdfa3f4f.md)
- [\_types.h](__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
