---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/histogram_8h_source.html
original_path: doxygen/html/histogram_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

histogram.h

[Go to the documentation of this file.](histogram_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_

10

19

20#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

21#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

22

23#include <stddef.h>

24

[ 30](structprometheus__histogram__bucket.md)struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) {

[ 32](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3) double [upper\_bound](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3);

[ 34](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4) unsigned long [count](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4);

35};

36

[ 43](structprometheus__histogram.md)struct [prometheus\_histogram](structprometheus__histogram.md) {

[ 45](structprometheus__histogram.md#adc3ad0fe48cad15282a907e977bbf16b) struct [prometheus\_metric](structprometheus__metric.md) [base](structprometheus__histogram.md#adc3ad0fe48cad15282a907e977bbf16b);

[ 47](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb) struct [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) \*[buckets](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb);

[ 49](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785) size\_t [num\_buckets](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785);

[ 51](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787) double [sum](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787);

[ 53](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873) unsigned long [count](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873);

[ 55](structprometheus__histogram.md#a1ef93a8a5d7a934cf207041d461ce8ec) void \*[user\_data](structprometheus__histogram.md#a1ef93a8a5d7a934cf207041d461ce8ec);

56};

57

[ 79](group__prometheus.md#gaf2ddb4e016104faaf543d9a028756a0c)#define PROMETHEUS\_HISTOGRAM\_DEFINE(\_name, \_desc, \_label, \_collector, ...) \

80 STRUCT\_SECTION\_ITERABLE(prometheus\_histogram, \_name) = { \

81 .base.name = STRINGIFY(\_name), \

82 .base.type = PROMETHEUS\_HISTOGRAM, \

83 .base.description = \_desc, \

84 .base.labels[0] = \_\_DEBRACKET \_label, \

85 .base.num\_labels = 1, \

86 .base.collector = \_collector, \

87 .buckets = NULL, \

88 .num\_buckets = 0, \

89 .sum = 0.0, \

90 .count = 0U, \

91 .user\_data = COND\_CODE\_0( \

92 NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

93 (NULL), \

94 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

95 }

96

[ 106](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)int [prometheus\_histogram\_observe](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)(struct [prometheus\_histogram](structprometheus__histogram.md) \*histogram, double value);

107

111

112#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_HISTOGRAM\_H\_ \*/

[prometheus\_histogram\_observe](group__prometheus.md#gaf0f24e64833302b74397654001ca5026)

int prometheus\_histogram\_observe(struct prometheus\_histogram \*histogram, double value)

Observe a value in a Prometheus histogram metric.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md)

Prometheus histogram bucket definition.

**Definition** histogram.h:30

[prometheus\_histogram\_bucket::count](structprometheus__histogram__bucket.md#a93865334a397013506d39a28505586c4)

unsigned long count

Cumulative count of observations in the bucket.

**Definition** histogram.h:34

[prometheus\_histogram\_bucket::upper\_bound](structprometheus__histogram__bucket.md#aa18e37384ee094972b6a330bb4323fa3)

double upper\_bound

Upper bound value of bucket.

**Definition** histogram.h:32

[prometheus\_histogram](structprometheus__histogram.md)

Type used to represent a Prometheus histogram metric.

**Definition** histogram.h:43

[prometheus\_histogram::num\_buckets](structprometheus__histogram.md#a01cfda4eab91d6776b7f7b11279d2785)

size\_t num\_buckets

Number of buckets in the histogram.

**Definition** histogram.h:49

[prometheus\_histogram::user\_data](structprometheus__histogram.md#a1ef93a8a5d7a934cf207041d461ce8ec)

void \* user\_data

User data.

**Definition** histogram.h:55

[prometheus\_histogram::buckets](structprometheus__histogram.md#a2f37871231727963173b7336ea8cfafb)

struct prometheus\_histogram\_bucket \* buckets

Array of buckets in the histogram.

**Definition** histogram.h:47

[prometheus\_histogram::sum](structprometheus__histogram.md#a65616857524ef4eeb09a577e0432e787)

double sum

Sum of all observed values in the histogram.

**Definition** histogram.h:51

[prometheus\_histogram::count](structprometheus__histogram.md#a6ae0aad29b927a729263324704917873)

unsigned long count

Total count of observations in the histogram.

**Definition** histogram.h:53

[prometheus\_histogram::base](structprometheus__histogram.md#adc3ad0fe48cad15282a907e977bbf16b)

struct prometheus\_metric base

Base of the Prometheus histogram metric.

**Definition** histogram.h:45

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [histogram.h](histogram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
