---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/summary_8h_source.html
original_path: doxygen/html/summary_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

summary.h

[Go to the documentation of this file.](summary_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_

8#define ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_

9

18

19#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

20#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

21

22#include <stddef.h>

23

[ 29](structprometheus__summary__quantile.md)struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) {

[ 31](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92) double [quantile](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92);

[ 33](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037) double [value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037);

34};

35

[ 42](structprometheus__summary.md)struct [prometheus\_summary](structprometheus__summary.md) {

[ 44](structprometheus__summary.md#a4af4a8982ac633944e97480c9dbc0119) struct [prometheus\_metric](structprometheus__metric.md) \*[base](structprometheus__summary.md#a4af4a8982ac633944e97480c9dbc0119);

[ 46](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7) struct [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) \*[quantiles](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7);

[ 48](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59) size\_t [num\_quantiles](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59);

[ 50](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7) double [sum](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7);

[ 52](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87) unsigned long [count](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87);

53};

54

80

[ 81](group__prometheus.md#ga05b125af8b981e61894a16d147f8ba2b)#define PROMETHEUS\_SUMMARY\_DEFINE(\_name, \_detail) \

82 static STRUCT\_SECTION\_ITERABLE(prometheus\_summary, \_name) = {.base = (void \*)(\_detail), \

83 .quantiles = NULL, \

84 .num\_quantiles = 0, \

85 .sum = 0, \

86 .count = 0}

87

[ 97](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)int [prometheus\_summary\_observe](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)(struct [prometheus\_summary](structprometheus__summary.md) \*summary, double [value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037));

98

102

103#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_SUMMARY\_H\_ \*/

[prometheus\_summary\_observe](group__prometheus.md#ga7683de05e8b135161120ad5d3f2edc2c)

int prometheus\_summary\_observe(struct prometheus\_summary \*summary, double value)

Observes a value in a Prometheus summary metric.

[metric.h](metric_8h.md)

Prometheus metric interface.

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

[prometheus\_summary\_quantile](structprometheus__summary__quantile.md)

Prometheus summary quantile definition.

**Definition** summary.h:29

[prometheus\_summary\_quantile::value](structprometheus__summary__quantile.md#a53fb78e35a0748f568d7bb15b083b037)

double value

Value of the quantile.

**Definition** summary.h:33

[prometheus\_summary\_quantile::quantile](structprometheus__summary__quantile.md#a811db0cddd6fd444a899be83e4116b92)

double quantile

Quantile of the summary.

**Definition** summary.h:31

[prometheus\_summary](structprometheus__summary.md)

Type used to represent a Prometheus summary metric.

**Definition** summary.h:42

[prometheus\_summary::quantiles](structprometheus__summary.md#a2fa33910c03339df68c33b54d5f267d7)

struct prometheus\_summary\_quantile \* quantiles

Array of quantiles associated with the Prometheus summary metric.

**Definition** summary.h:46

[prometheus\_summary::base](structprometheus__summary.md#a4af4a8982ac633944e97480c9dbc0119)

struct prometheus\_metric \* base

Base of the Prometheus summary metric.

**Definition** summary.h:44

[prometheus\_summary::count](structprometheus__summary.md#a6cd8daf6014b485ccbca0dd3194e5d87)

unsigned long count

Total count of observations in the summary metric.

**Definition** summary.h:52

[prometheus\_summary::num\_quantiles](structprometheus__summary.md#a7e2604e9c9891137e7232ccaa9014c59)

size\_t num\_quantiles

Number of quantiles associated with the Prometheus summary metric.

**Definition** summary.h:48

[prometheus\_summary::sum](structprometheus__summary.md#aead1e2754a146d36564472f8a1867da7)

double sum

Sum of all observed values in the summary metric.

**Definition** summary.h:50

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [summary.h](summary_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
