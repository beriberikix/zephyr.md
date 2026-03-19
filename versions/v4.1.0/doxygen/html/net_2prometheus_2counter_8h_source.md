---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net_2prometheus_2counter_8h_source.html
original_path: doxygen/html/net_2prometheus_2counter_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

counter.h

[Go to the documentation of this file.](net_2prometheus_2counter_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_

10

19

20#include <[stdint.h](stdint_8h.md)>

21

22#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

23#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

24

[ 31](structprometheus__counter.md)struct [prometheus\_counter](structprometheus__counter.md) {

[ 33](structprometheus__counter.md#a33714d75e20f8a69a7068c5c57fe3a37) struct [prometheus\_metric](structprometheus__metric.md) [base](structprometheus__counter.md#a33714d75e20f8a69a7068c5c57fe3a37);

[ 35](structprometheus__counter.md#a048376a671e83df41034908b85e9e234) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structprometheus__counter.md#a048376a671e83df41034908b85e9e234);

[ 37](structprometheus__counter.md#a28793edc31342bd6572493d7aa72eaca) void \*[user\_data](structprometheus__counter.md#a28793edc31342bd6572493d7aa72eaca);

38};

39

[ 60](group__prometheus.md#gadbfcfc7904d6388d2c9dc81d4803264c)#define PROMETHEUS\_COUNTER\_DEFINE(\_name, \_desc, \_label, \_collector, ...) \

61 STRUCT\_SECTION\_ITERABLE(prometheus\_counter, \_name) = { \

62 .base.name = STRINGIFY(\_name), \

63 .base.type = PROMETHEUS\_COUNTER, \

64 .base.description = \_desc, \

65 .base.labels[0] = \_\_DEBRACKET \_label, \

66 .base.num\_labels = 1, \

67 .base.collector = \_collector, \

68 .value = 0ULL, \

69 .user\_data = COND\_CODE\_0( \

70 NUM\_VA\_ARGS\_LESS\_1(LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

71 (NULL), \

72 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

73 }

74

[ 82](group__prometheus.md#ga9b7461d625acc075c9511249c67741ab)int [prometheus\_counter\_add](group__prometheus.md#ga9b7461d625acc075c9511249c67741ab)(struct [prometheus\_counter](structprometheus__counter.md) \*counter, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

83

[ 90](group__prometheus.md#gad2220d089050bc5db1e5866429d515b3)static inline int [prometheus\_counter\_inc](group__prometheus.md#gad2220d089050bc5db1e5866429d515b3)(struct [prometheus\_counter](structprometheus__counter.md) \*counter)

91{

92 return [prometheus\_counter\_add](group__prometheus.md#ga9b7461d625acc075c9511249c67741ab)(counter, 1ULL);

93}

94

[ 105](group__prometheus.md#ga8621228b7a66a6a42fb2cb838ec94dfe)int [prometheus\_counter\_set](group__prometheus.md#ga8621228b7a66a6a42fb2cb838ec94dfe)(struct [prometheus\_counter](structprometheus__counter.md) \*counter, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value);

106

110

111#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_COUNTER\_H\_ \*/

[prometheus\_counter\_set](group__prometheus.md#ga8621228b7a66a6a42fb2cb838ec94dfe)

int prometheus\_counter\_set(struct prometheus\_counter \*counter, uint64\_t value)

Set the counter value to specific value.

[prometheus\_counter\_add](group__prometheus.md#ga9b7461d625acc075c9511249c67741ab)

int prometheus\_counter\_add(struct prometheus\_counter \*counter, uint64\_t value)

Increment the value of a Prometheus counter metric Increments the value of the specified counter metr...

[prometheus\_counter\_inc](group__prometheus.md#gad2220d089050bc5db1e5866429d515b3)

static int prometheus\_counter\_inc(struct prometheus\_counter \*counter)

Increment the value of a Prometheus counter metric Increments the value of the specified counter metr...

**Definition** counter.h:90

[metric.h](metric_8h.md)

Prometheus metric interface.

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[prometheus\_counter](structprometheus__counter.md)

Type used to represent a Prometheus counter metric.

**Definition** counter.h:31

[prometheus\_counter::value](structprometheus__counter.md#a048376a671e83df41034908b85e9e234)

uint64\_t value

Value of the Prometheus counter metric.

**Definition** counter.h:35

[prometheus\_counter::user\_data](structprometheus__counter.md#a28793edc31342bd6572493d7aa72eaca)

void \* user\_data

User data.

**Definition** counter.h:37

[prometheus\_counter::base](structprometheus__counter.md#a33714d75e20f8a69a7068c5c57fe3a37)

struct prometheus\_metric base

Base of the Prometheus counter metric.

**Definition** counter.h:33

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [counter.h](net_2prometheus_2counter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
