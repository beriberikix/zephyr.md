---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sched__priq_8h_source.html
original_path: doxygen/html/sched__priq_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched\_priq.h

[Go to the documentation of this file.](sched__priq_8h.md)

1/\*

2 \* Copyright (c) 2018 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SCHED\_PRIQ\_H\_

7#define ZEPHYR\_INCLUDE\_SCHED\_PRIQ\_H\_

8

9#include <[zephyr/sys/util.h](util_8h.md)>

10#include <[zephyr/sys/dlist.h](dlist_8h.md)>

11#include <[zephyr/sys/rb.h](rb_8h.md)>

12

13/\* Two abstractions are defined here for "thread priority queues".

14 \*

15 \* One is a "dumb" list implementation appropriate for systems with

16 \* small numbers of threads and sensitive to code size. It is stored

17 \* in sorted order, taking an O(N) cost every time a thread is added

18 \* to the list. This corresponds to the way the original \_wait\_q\_t

19 \* abstraction worked and is very fast as long as the number of

20 \* threads is small.

21 \*

22 \* The other is a balanced tree "fast" implementation with rather

23 \* larger code size (due to the data structure itself, the code here

24 \* is just stubs) and higher constant-factor performance overhead, but

25 \* much better O(logN) scaling in the presence of large number of

26 \* threads.

27 \*

28 \* Each can be used for either the wait\_q or system ready queue,

29 \* configurable at build time.

30 \*/

31

32struct [k\_thread](structk__thread.md);

33

34struct [k\_thread](structk__thread.md) \*z\_priq\_dumb\_best([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*pq);

35void z\_priq\_dumb\_remove([sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) \*pq, struct [k\_thread](structk__thread.md) \*thread);

36

37struct \_priq\_rb {

38 struct rbtree tree;

39 int next\_order\_key;

40};

41

42void z\_priq\_rb\_add(struct \_priq\_rb \*pq, struct [k\_thread](structk__thread.md) \*thread);

43void z\_priq\_rb\_remove(struct \_priq\_rb \*pq, struct [k\_thread](structk__thread.md) \*thread);

44struct [k\_thread](structk__thread.md) \*z\_priq\_rb\_best(struct \_priq\_rb \*pq);

45

46/\* Traditional/textbook "multi-queue" structure. Separate lists for a

47 \* small number (max 32 here) of fixed priorities. This corresponds

48 \* to the original Zephyr scheduler. RAM requirements are

49 \* comparatively high, but performance is very fast. Won't work with

50 \* features like deadline scheduling which need large priority spaces

51 \* to represent their requirements.

52 \*/

53struct \_priq\_mq {

54 [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) queues[32];

55 unsigned int bitmask; /\* bit 1<<i set if queues[i] is non-empty \*/

56};

57

58struct [k\_thread](structk__thread.md) \*z\_priq\_mq\_best(struct \_priq\_mq \*pq);

59

60#endif /\* ZEPHYR\_INCLUDE\_SCHED\_PRIQ\_H\_ \*/

[dlist.h](dlist_8h.md)

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[rb.h](rb_8h.md)

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[util.h](util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [kernel](dir_87084789f4f879979d9b1b0acd11eedc.md)
- [internal](dir_5a28aaecc3642d39af859931377173ec.md)
- [sched\_priq.h](sched__priq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
