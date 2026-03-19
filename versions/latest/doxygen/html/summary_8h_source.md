---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/summary_8h_source.html
original_path: doxygen/html/summary_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

summary.h

[Go to the documentation of this file.](summary_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_

10

19

20#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

21#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

22

23#include <stddef.h>

24

[ 30](structprometheus__summary__quantile.md)struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) {

[ 32](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92) double [quantile](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92);

[ 34](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037) double [value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037);

[ 36](structprometheus__summary__quantile.md#a788d30204d7ce61940741cefd2c073f6) void \*[user\_data](structprometheus__summary__quantile.md#a788d30204d7ce61940741cefd2c073f6);

37};

38

[ 45](structprometheus__summary.md)struct [prometheus\_summary](structprometheus__summary.md) {

[ 47](structprometheus__summary.md#aaef55d38ed7a9a8477d6e5ffeb748cbe) struct [prometheus\_metric](structprometheus__metric.md) [base](structprometheus__summary.md#aaef55d38ed7a9a8477d6e5ffeb748cbe);

[ 49](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7) struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) \*[quantiles](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7);

[ 51](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59) size\_t [num\_quantiles](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59);

[ 53](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7) double [sum](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7);

[ 55](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87) unsigned long [count](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87);

[ 57](structprometheus__summary.md#ab9ba58c106f9dd73c425976b0680b785) void \*[user\_data](structprometheus__summary.md#ab9ba58c106f9dd73c425976b0680b785);

58};

59

82

[ 83](group__prometheus.md#gaa3c043be86118ff9e8122136edc89cc4)#define PROMETHEUS\_SUMMARY\_DEFINE(\_name, \_desc, \_label, \_collector, ...) \

84 STRUCT\_SECTION\_ITERABLE(prometheus\_summary, \_name) = { \

85 .base.name = STRINGIFY(\_name), \

86 .base.type = PROMETHEUS\_SUMMARY, \

87 .base.description = \_desc, \

88 .base.labels[0] = \_\_DEBRACKET \_label, \

89 .base.num\_labels = 1, \

90 .base.collector = \_collector, \

91 .quantiles = NULL, \

92 .num\_quantiles = 0, \

93 .sum = 0.0, \

94 .count = 0U, \

95 .user\_data = COND\_CODE\_0( \

96 NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

97 (NULL), \

98 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

99 }

100

[ 110](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)int [prometheus\_summary\_observe](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)(struct [prometheus\_summary](structprometheus__summary.md) \*summary, double [value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037));

111

[ 123](group__prometheus.md#ga98369eb2a7c8ce36f7570ed5b55410d8)int [prometheus\_summary\_observe\_set](group__prometheus.md#ga98369eb2a7c8ce36f7570ed5b55410d8)(struct [prometheus\_summary](structprometheus__summary.md) \*summary,

124 double [value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037), unsigned long count);

125

129

130#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_ \*/

[prometheus\_summary\_observe](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)

int prometheus\_summary\_observe(struct prometheus\_summary \*summary, double value)

Observes a value in a Prometheus summary metric.

[prometheus\_summary\_observe\_set](group__prometheus.md#ga98369eb2a7c8ce36f7570ed5b55410d8)

int prometheus\_summary\_observe\_set(struct prometheus\_summary \*summary, double value, unsigned long count)

Set the summary value to specific value.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[prometheus\_summary\_quantile](structprometheus__summary__quantile.md)

Prometheus summary quantile definition.

**Definition** summary.h:30

[prometheus\_summary\_quantile::value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037)

double value

Value of the quantile.

**Definition** summary.h:34

[prometheus\_summary\_quantile::user\_data](structprometheus__summary__quantile.md#a788d30204d7ce61940741cefd2c073f6)

void \* user\_data

User data.

**Definition** summary.h:36

[prometheus\_summary\_quantile::quantile](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92)

double quantile

Quantile of the summary.

**Definition** summary.h:32

[prometheus\_summary](structprometheus__summary.md)

Type used to represent a Prometheus summary metric.

**Definition** summary.h:45

[prometheus\_summary::quantiles](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7)

struct prometheus\_summary\_quantile \* quantiles

Array of quantiles associated with the Prometheus summary metric.

**Definition** summary.h:49

[prometheus\_summary::count](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87)

unsigned long count

Total count of observations in the summary metric.

**Definition** summary.h:55

[prometheus\_summary::num\_quantiles](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59)

size\_t num\_quantiles

Number of quantiles associated with the Prometheus summary metric.

**Definition** summary.h:51

[prometheus\_summary::base](structprometheus__summary.md#aaef55d38ed7a9a8477d6e5ffeb748cbe)

struct prometheus\_metric base

Base of the Prometheus summary metric.

**Definition** summary.h:47

[prometheus\_summary::user\_data](structprometheus__summary.md#ab9ba58c106f9dd73c425976b0680b785)

void \* user\_data

User data.

**Definition** summary.h:57

[prometheus\_summary::sum](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7)

double sum

Sum of all observed values in the summary metric.

**Definition** summary.h:53

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [summary.h](summary_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
