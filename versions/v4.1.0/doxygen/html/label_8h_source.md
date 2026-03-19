---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/label_8h_source.html
original_path: doxygen/html/label_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

label.h

[Go to the documentation of this file.](label_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_LABEL\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_LABEL\_H\_

9

18

19#if defined(CONFIG\_PROMETHEUS)

21#define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC CONFIG\_PROMETHEUS\_LABEL\_MAX\_COUNT

22#else

[ 23](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)#define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC 1

24#endif /\* CONFIG\_PROMETHEUS \*/

25

[ 31](structprometheus__label.md)struct [prometheus\_label](structprometheus__label.md) {

[ 33](structprometheus__label.md#a484ae44cbfdea3d66b010c765829da88) const char \*[key](structprometheus__label.md#a484ae44cbfdea3d66b010c765829da88);

[ 35](structprometheus__label.md#a0cf2605f8904b2cd7ad14273816681b6) const char \*[value](structprometheus__label.md#a0cf2605f8904b2cd7ad14273816681b6);

36};

37

41

42#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_LABEL\_H\_ \*/

[prometheus\_label](structprometheus__label.md)

Prometheus label definition.

**Definition** label.h:31

[prometheus\_label::value](structprometheus__label.md#a0cf2605f8904b2cd7ad14273816681b6)

const char \* value

Prometheus metric label value.

**Definition** label.h:35

[prometheus\_label::key](structprometheus__label.md#a484ae44cbfdea3d66b010c765829da88)

const char \* key

Prometheus metric label key.

**Definition** label.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [label.h](label_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
