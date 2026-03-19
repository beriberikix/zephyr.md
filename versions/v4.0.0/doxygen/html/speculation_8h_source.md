---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/speculation_8h_source.html
original_path: doxygen/html/speculation_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

speculation.h

[Go to the documentation of this file.](speculation_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_MISC\_SPECULATION\_H

8#define ZEPHYR\_MISC\_SPECULATION\_H

9

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11

[ 33](speculation_8h.md#aa677f654a5febe3a9b7525e4306ede09)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [k\_array\_index\_sanitize](speculation_8h.md#aa677f654a5febe3a9b7525e4306ede09)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) index, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) array\_size)

34{

35#ifdef CONFIG\_BOUNDS\_CHECK\_BYPASS\_MITIGATION

36 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) signed\_index = index, signed\_array\_size = array\_size;

37

38 /\* Take the difference between index and max.

39 \* A proper value will result in a negative result. We also AND in

40 \* the complement of index, so that we automatically reject any large

41 \* indexes which would wrap around the difference calculation.

42 \*

43 \* Sign-extend just the sign bit to produce a mask of all 1s (accept)

44 \* or all 0s (truncate).

45 \*/

46 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mask = ((signed\_index - signed\_array\_size) & ~signed\_index) >> 31;

47

48 return index & mask;

49#else

50 ARG\_UNUSED(array\_size);

51

52 return index;

53#endif /\* CONFIG\_BOUNDS\_CHECK\_BYPASS\_MITIGATION \*/

54}

55#endif /\* ZEPHYR\_MISC\_SPECULATION\_H \*/

[types.h](include_2zephyr_2types_8h.md)

[k\_array\_index\_sanitize](speculation_8h.md#aa677f654a5febe3a9b7525e4306ede09)

static uint32\_t k\_array\_index\_sanitize(uint32\_t index, uint32\_t array\_size)

Sanitize an array index against bounds check bypass attacks aka the Spectre V1 vulnerability.

**Definition** speculation.h:33

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [speculation.h](speculation_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
