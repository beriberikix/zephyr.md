---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/histogram_8h_source.html
original_path: doxygen/html/histogram_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

histogram.h

[Go to the documentation of this file.](histogram_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_

9

18

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

21

22#include <stddef.h>

23

[ 29](structprometheus__histogram__bucket.md)struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) {

[ 31](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3) double [upper\_bound](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3);

[ 33](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4) unsigned long [count](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4);

34};

35

[ 42](structprometheus__histogram.md)struct [prometheus\_histogram](structprometheus__histogram.md) {

[ 44](structprometheus__histogram.md#a951618ccaba4f4eac27efe21ea17fa90) struct [prometheus\_metric](structprometheus__metric.md) \*[base](structprometheus__histogram.md#a951618ccaba4f4eac27efe21ea17fa90);

[ 46](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb) struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) \*[buckets](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb);

[ 48](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785) size\_t [num\_buckets](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785);

[ 50](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787) double [sum](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787);

[ 52](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873) unsigned long [count](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873);

53};

54

[ 80](group__prometheus.md#gada4920e35290a96a76566cc6b4ab5a60)#define PROMETHEUS\_HISTOGRAM\_DEFINE(\_name, \_detail) \

81 static STRUCT\_SECTION\_ITERABLE(prometheus\_histogram, \_name) = {.base = (void \*)(\_detail), \

82 .buckets = NULL, \

83 .num\_buckets = 0, \

84 .sum = 0, \

85 .count = 0}

86

[ 96](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)int [prometheus\_histogram\_observe](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)(struct [prometheus\_histogram](structprometheus__histogram.md) \*histogram, double value);

97

101

102#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_ \*/

[prometheus\_histogram\_observe](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)

int prometheus\_histogram\_observe(struct prometheus\_histogram \*histogram, double value)

Observe a value in a Prometheus histogram metric.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md)

Prometheus histogram bucket definition.

**Definition** histogram.h:29

[prometheus\_histogram\_bucket::count](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4)

unsigned long count

Cumulative count of observations in the bucket.

**Definition** histogram.h:33

[prometheus\_histogram\_bucket::upper\_bound](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3)

double upper\_bound

Upper bound value of bucket.

**Definition** histogram.h:31

[prometheus\_histogram](structprometheus__histogram.md)

Type used to represent a Prometheus histogram metric.

**Definition** histogram.h:42

[prometheus\_histogram::num\_buckets](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785)

size\_t num\_buckets

Number of buckets in the histogram.

**Definition** histogram.h:48

[prometheus\_histogram::buckets](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb)

struct prometheus\_histogram\_bucket \* buckets

Array of buckets in the histogram.

**Definition** histogram.h:46

[prometheus\_histogram::sum](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787)

double sum

Sum of all observed values in the histogram.

**Definition** histogram.h:50

[prometheus\_histogram::count](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873)

unsigned long count

Total count of observations in the histogram.

**Definition** histogram.h:52

[prometheus\_histogram::base](structprometheus__histogram.md#a951618ccaba4f4eac27efe21ea17fa90)

struct prometheus\_metric \* base

Base of the Prometheus histogram metric.

**Definition** histogram.h:44

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [histogram.h](histogram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
