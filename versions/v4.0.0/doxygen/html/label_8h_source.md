---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/label_8h_source.html
original_path: doxygen/html/label_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

19/\* maximum length of label key \*/

[ 20](group__prometheus.md#gab8e197380d5a91070f5961fb8ab6a78a)#define MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH 16

21/\* maximum length of label value \*/

[ 22](group__prometheus.md#ga2abf70d0af09aa933ee7e57cf13b8c19)#define MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH 16

23/\* maximum namber of labels per metric \*/

[ 24](group__prometheus.md#ga5fd572e5351cda0855cb587e88c3a247)#define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC 5

25

[ 31](structprometheus__label.md)struct [prometheus\_label](structprometheus__label.md) {

[ 33](structprometheus__label.md#a7abd6764903181f17ba88bd1745de72c) char [key](structprometheus__label.md#a7abd6764903181f17ba88bd1745de72c)[[MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH](group__prometheus.md#gab8e197380d5a91070f5961fb8ab6a78a)];

[ 35](structprometheus__label.md#a4e5ef1b230708ad9bfc4f61a933fbc36) char [value](structprometheus__label.md#a4e5ef1b230708ad9bfc4f61a933fbc36)[[MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH](group__prometheus.md#ga2abf70d0af09aa933ee7e57cf13b8c19)];

36};

37

41

42#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_LABEL\_H\_ \*/

[MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH](group__prometheus.md#ga2abf70d0af09aa933ee7e57cf13b8c19)

#define MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH

**Definition** label.h:22

[MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH](group__prometheus.md#gab8e197380d5a91070f5961fb8ab6a78a)

#define MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH

**Definition** label.h:20

[prometheus\_label](structprometheus__label.md)

Prometheus label definition.

**Definition** label.h:31

[prometheus\_label::value](structprometheus__label.md#a4e5ef1b230708ad9bfc4f61a933fbc36)

char value[16]

Prometheus metric label value.

**Definition** label.h:35

[prometheus\_label::key](structprometheus__label.md#a7abd6764903181f17ba88bd1745de72c)

char key[16]

Prometheus metric label key.

**Definition** label.h:33

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [label.h](label_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
