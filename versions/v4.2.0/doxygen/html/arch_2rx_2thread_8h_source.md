---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arch_2rx_2thread_8h_source.html
original_path: doxygen/html/arch_2rx_2thread_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

thread.h

[Go to the documentation of this file.](arch_2rx_2thread_8h.md)

1/\*

2 \* Copyright (c) 2021 KT-Elektronik, Klaucke und Partner GmbH

3 \* Copyright (c) 2024 Renesas Electronics Corporation

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_ARCH\_RX\_THREAD\_H\_

9#define ZEPHYR\_INCLUDE\_ARCH\_RX\_THREAD\_H\_

10

11#ifndef \_ASMLANGUAGE

12#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18struct \_callee\_saved {

19 /\* General purpose callee-saved registers \*/

20};

21

22typedef struct \_callee\_saved \_callee\_saved\_t;

23

24struct \_thread\_arch {

25 /\* empty \*/

26};

27

28typedef struct \_thread\_arch \_thread\_arch\_t;

29

30#ifdef \_\_cplusplus

31}

32#endif

33

34#endif /\* \_ASMLANGUAGE \*/

35

36#endif /\* ZEPHYR\_INCLUDE\_ARCH\_RX\_THREAD\_H\_ \*/

[types.h](include_2zephyr_2types_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [rx](dir_eb52b7f9d95392aedf108916f743bdaf.md)
- [thread.h](arch_2rx_2thread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
