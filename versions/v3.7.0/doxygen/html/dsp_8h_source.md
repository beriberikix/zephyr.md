---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dsp_8h_source.html
original_path: doxygen/html/dsp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsp.h

[Go to the documentation of this file.](dsp_8h.md)

1/\* Copyright (c) 2022 Google LLC

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4

10

11#ifndef INCLUDE\_ZEPHYR\_DSP\_DSP\_H\_

12#define INCLUDE\_ZEPHYR\_DSP\_DSP\_H\_

13

14#ifdef CONFIG\_DSP\_BACKEND\_HAS\_STATIC

15#define DSP\_FUNC\_SCOPE static

16#else

[ 17](dsp_8h.md#a88feaebec50a9dcd42836439a9849bc7)#define DSP\_FUNC\_SCOPE

18#endif

19

20#ifdef CONFIG\_DSP\_BACKEND\_HAS\_AGU

21#define DSP\_DATA \_\_agu

22#else

[ 23](dsp_8h.md#a2ba5cab25d6c097e55bbe14094a06c7c)#define DSP\_DATA

24#endif

25

26#ifdef CONFIG\_DSP\_BACKEND\_HAS\_XDATA\_SECTION

27#define DSP\_STATIC\_DATA DSP\_DATA \_\_attribute\_\_((section(".Xdata")))

28#else

[ 29](dsp_8h.md#aab42290c42efbdc1d93c5530da099911)#define DSP\_STATIC\_DATA DSP\_DATA

30#endif

31

38

39#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

40

41#include <[zephyr/dsp/basicmath.h](basicmath_8h.md)>

42

43#include <[zephyr/dsp/print\_format.h](print__format_8h.md)>

44

45#include "zdsp\_backend.h"

46

47#endif /\* INCLUDE\_ZEPHYR\_DSP\_DSP\_H\_ \*/

[basicmath.h](basicmath_8h.md)

Public APIs for DSP basicmath.

[types.h](include_2zephyr_2dsp_2types_8h.md)

[print\_format.h](print__format_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dsp](dir_33029109ed37fedc3a135c3293a7868a.md)
- [dsp.h](dsp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
