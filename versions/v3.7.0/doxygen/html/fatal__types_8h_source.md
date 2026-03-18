---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/fatal__types_8h_source.html
original_path: doxygen/html/fatal__types_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fatal\_types.h

[Go to the documentation of this file.](fatal__types_8h.md)

1/\*

2 \* Copyright (c) 2023 CSIRO.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_FATAL\_TYPES\_H

12#define ZEPHYR\_INCLUDE\_FATAL\_TYPES\_H

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

23

[ 24](group__fatal__types.md#ga5b7e799fa19549ef9416a2d6cba29b52)enum [k\_fatal\_error\_reason](group__fatal__types.md#ga5b7e799fa19549ef9416a2d6cba29b52) {

[ 26](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52af9ac087d07f036fae2e689a2afc8d88b) [K\_ERR\_CPU\_EXCEPTION](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52af9ac087d07f036fae2e689a2afc8d88b),

27

[ 29](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a473dca11c5f93f5059a119a8e66e2db3) [K\_ERR\_SPURIOUS\_IRQ](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a473dca11c5f93f5059a119a8e66e2db3),

30

[ 32](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a4156a6495ca0fe0867a17a91efc42e91) [K\_ERR\_STACK\_CHK\_FAIL](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a4156a6495ca0fe0867a17a91efc42e91),

33

[ 35](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3) [K\_ERR\_KERNEL\_OOPS](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3),

36

[ 38](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617) [K\_ERR\_KERNEL\_PANIC](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617),

39

[ 41](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1) [K\_ERR\_ARCH\_START](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1) = 16

42};

43

45

46#ifdef \_\_cplusplus

47}

48#endif

49

50#endif /\* ZEPHYR\_INCLUDE\_FATAL\_TYPES\_H \*/

[k\_fatal\_error\_reason](group__fatal__types.md#ga5b7e799fa19549ef9416a2d6cba29b52)

k\_fatal\_error\_reason

**Definition** fatal\_types.h:24

[K\_ERR\_STACK\_CHK\_FAIL](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a4156a6495ca0fe0867a17a91efc42e91)

@ K\_ERR\_STACK\_CHK\_FAIL

Faulting context overflowed its stack buffer.

**Definition** fatal\_types.h:32

[K\_ERR\_ARCH\_START](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1)

@ K\_ERR\_ARCH\_START

Arch specific fatal errors.

**Definition** fatal\_types.h:41

[K\_ERR\_SPURIOUS\_IRQ](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a473dca11c5f93f5059a119a8e66e2db3)

@ K\_ERR\_SPURIOUS\_IRQ

Unhandled hardware interrupt.

**Definition** fatal\_types.h:29

[K\_ERR\_KERNEL\_PANIC](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617)

@ K\_ERR\_KERNEL\_PANIC

High severity software error.

**Definition** fatal\_types.h:38

[K\_ERR\_KERNEL\_OOPS](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3)

@ K\_ERR\_KERNEL\_OOPS

Moderate severity software error.

**Definition** fatal\_types.h:35

[K\_ERR\_CPU\_EXCEPTION](group__fatal__types.md#gga5b7e799fa19549ef9416a2d6cba29b52af9ac087d07f036fae2e689a2afc8d88b)

@ K\_ERR\_CPU\_EXCEPTION

Generic CPU exception, not covered by other codes.

**Definition** fatal\_types.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [fatal\_types.h](fatal__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
