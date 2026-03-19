---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fake__comp_8h_source.html
original_path: doxygen/html/fake__comp_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_comp.h

[Go to the documentation of this file.](fake__comp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_FAKE\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_FAKE\_H\_

9

10#include <[zephyr/drivers/comparator.h](comparator_8h.md)>

11#include <[zephyr/fff.h](fff_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

[ 17](fake__comp_8h.md#a2c5d4864a0a2f27f0e612eeb5021238a)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int,

18 comp\_fake\_comp\_get\_output,

19 const struct [device](structdevice.md) \*);

20

[ 21](fake__comp_8h.md#a87eda8131b9665071bb533088704478c)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int,

22 comp\_fake\_comp\_set\_trigger,

23 const struct [device](structdevice.md) \*,

24 enum [comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674));

25

[ 26](fake__comp_8h.md#a75a4f06e86d3ea886fd512c26c376dfa)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int,

27 comp\_fake\_comp\_set\_trigger\_callback,

28 const struct [device](structdevice.md) \*,

29 [comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31),

30 void \*);

31

[ 32](fake__comp_8h.md#a3851a9b2f4fa854329cb7e43dc74323e)[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)(int,

33 comp\_fake\_comp\_trigger\_is\_pending,

34 const struct [device](structdevice.md) \*);

35

36#ifdef \_\_cplusplus

37}

38#endif

39

40#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COMPARATOR\_FAKE\_H\_ \*/

[comparator.h](comparator_8h.md)

[fff.h](fff_8h.md)

[DECLARE\_FAKE\_VALUE\_FUNC](fff_8h.md#abe755adc69a66dab496ea7583050d3fd)

#define DECLARE\_FAKE\_VALUE\_FUNC(...)

**Definition** fff.h:8684

[comparator\_callback\_t](group__comparator__interface.md#ga409308b8ba2efdca4a6ec4bdc4d3bc31)

void(\* comparator\_callback\_t)(const struct device \*dev, void \*user\_data)

Comparator callback template.

**Definition** comparator.h:39

[comparator\_trigger](group__comparator__interface.md#gab02743771baf02ee0105aa1303931674)

comparator\_trigger

Comparator trigger enumerations.

**Definition** comparator.h:27

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [fake\_comp.h](fake__comp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
