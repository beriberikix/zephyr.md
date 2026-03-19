---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/collector_8h_source.html
original_path: doxygen/html/collector_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

collector.h

[Go to the documentation of this file.](collector_8h.md)

1/\*

2 \* Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology

3 \* Copyright (c) 2024 Nordic Semiconductor

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_

9#define ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_

10

22

23#include <[zephyr/kernel.h](kernel_8h.md)>

24#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

25#include <[zephyr/net/prometheus/metric.h](metric_8h.md)>

26

27#include <stddef.h>

28

29struct [prometheus\_collector](structprometheus__collector.md);

30

[ 41](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5)typedef int (\*[prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5))(struct [prometheus\_collector](structprometheus__collector.md) \*collector,

42 struct [prometheus\_metric](structprometheus__metric.md) \*[metric](structprometheus__metric.md#a67e8d38a696f2b20a076b8da6b1250e3),

43 void \*[user\_data](structprometheus__metric.md#ae2db853cae2c49634fda25eb23b825da));

44

[ 50](structprometheus__collector.md)struct [prometheus\_collector](structprometheus__collector.md) {

[ 52](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476) const char \*[name](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476);

[ 54](structprometheus__collector.md#a389528dad4e2ada62ca85650b6be5972) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [metrics](structprometheus__collector.md#a389528dad4e2ada62ca85650b6be5972);

[ 56](structprometheus__collector.md#a43e08aa447c0388d80771c33f59992b7) struct [k\_mutex](structk__mutex.md) [lock](structprometheus__collector.md#a43e08aa447c0388d80771c33f59992b7);

[ 60](structprometheus__collector.md#ae131dcdd35fbacd30a210b547718c6be) [prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5) [user\_cb](structprometheus__collector.md#ae131dcdd35fbacd30a210b547718c6be);

[ 62](structprometheus__collector.md#acd2c684c0c920f75e86d2560b4bb29e2) void \*[user\_data](structprometheus__collector.md#acd2c684c0c920f75e86d2560b4bb29e2);

63};

64

[ 76](group__prometheus.md#gaab3a797c867c6492dedb2b51774a48e5)#define PROMETHEUS\_COLLECTOR\_DEFINE(\_name, ...) \

77 STRUCT\_SECTION\_ITERABLE(prometheus\_collector, \_name) = { \

78 .name = STRINGIFY(\_name), \

79 .metrics = SYS\_SLIST\_STATIC\_INIT(&\_name.metrics), \

80 .lock = Z\_MUTEX\_INITIALIZER(\_name.lock), \

81 .user\_cb = COND\_CODE\_0( \

82 NUM\_VA\_ARGS\_LESS\_1( \

83 LIST\_DROP\_EMPTY(\_\_VA\_ARGS\_\_, \_)), \

84 (NULL), \

85 (GET\_ARG\_N(1, \_\_VA\_ARGS\_\_))), \

86 .user\_data = COND\_CODE\_0( \

87 NUM\_VA\_ARGS\_LESS\_1(\_\_VA\_ARGS\_\_), (NULL), \

88 (GET\_ARG\_N(1, \

89 GET\_ARGS\_LESS\_N(1, \_\_VA\_ARGS\_\_)))), \

90 }

91

[ 104](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)int [prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)(struct [prometheus\_collector](structprometheus__collector.md) \*collector,

105 struct [prometheus\_metric](structprometheus__metric.md) \*metric);

106

[ 116](group__prometheus.md#ga757252a9157538870b1360924b16d0e0)const void \*[prometheus\_collector\_get\_metric](group__prometheus.md#ga757252a9157538870b1360924b16d0e0)(struct [prometheus\_collector](structprometheus__collector.md) \*collector,

117 const char \*name);

118

120

121enum prometheus\_walk\_state {

122 PROMETHEUS\_WALK\_START,

123 PROMETHEUS\_WALK\_CONTINUE,

124 PROMETHEUS\_WALK\_STOP,

125};

126

127struct prometheus\_collector\_walk\_context {

128 struct prometheus\_collector \*collector;

129 struct prometheus\_metric \*metric;

130 struct prometheus\_metric \*tmp;

131 enum prometheus\_walk\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

132};

133

135

[ 147](group__prometheus.md#ga1bbdd8d5447144b21d3cda1ddac38ff0)int [prometheus\_collector\_walk\_metrics](group__prometheus.md#ga1bbdd8d5447144b21d3cda1ddac38ff0)(struct prometheus\_collector\_walk\_context \*ctx,

148 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, size\_t buffer\_size);

149

[ 158](group__prometheus.md#ga1c70215409029bbe163bdfdb03bfba43)static inline int [prometheus\_collector\_walk\_init](group__prometheus.md#ga1c70215409029bbe163bdfdb03bfba43)(struct prometheus\_collector\_walk\_context \*ctx,

159 struct [prometheus\_collector](structprometheus__collector.md) \*[collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a))

160{

161 if ([collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

162 return -[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4);

163 }

164

165 ctx->collector = [collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a);

166 ctx->state = PROMETHEUS\_WALK\_START;

167 ctx->metric = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

168 ctx->tmp = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4);

169

170 return 0;

171}

172

176

177#endif /\* ZEPHYR\_INCLUDE\_PROMETHEUS\_COLLECTOR\_H\_ \*/

[prometheus\_collector\_walk\_metrics](group__prometheus.md#ga1bbdd8d5447144b21d3cda1ddac38ff0)

int prometheus\_collector\_walk\_metrics(struct prometheus\_collector\_walk\_context \*ctx, uint8\_t \*buffer, size\_t buffer\_size)

Walk through all metrics in a Prometheus collector and format them into a buffer.

[prometheus\_collector\_walk\_init](group__prometheus.md#ga1c70215409029bbe163bdfdb03bfba43)

static int prometheus\_collector\_walk\_init(struct prometheus\_collector\_walk\_context \*ctx, struct prometheus\_collector \*collector)

Initialize the walker context to walk through all metrics.

**Definition** collector.h:158

[prometheus\_scrape\_cb\_t](group__prometheus.md#ga4e2541cb094915187157d44a29e2d6b5)

int(\* prometheus\_scrape\_cb\_t)(struct prometheus\_collector \*collector, struct prometheus\_metric \*metric, void \*user\_data)

Callback used to scrape a collector for a specific metric.

**Definition** collector.h:41

[prometheus\_collector\_get\_metric](group__prometheus.md#ga757252a9157538870b1360924b16d0e0)

const void \* prometheus\_collector\_get\_metric(struct prometheus\_collector \*collector, const char \*name)

Get a metric from a Prometheus collector.

[prometheus\_collector\_register\_metric](group__prometheus.md#ga976b9e82d747570cde631b03ee805a26)

int prometheus\_collector\_register\_metric(struct prometheus\_collector \*collector, struct prometheus\_metric \*metric)

Register a metric with a Prometheus collector.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[EINVAL](group__system__errno.md#ga2d1678d5a7cc8ce499643f3b8957def4)

#define EINVAL

Invalid argument.

**Definition** errno.h:60

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[kernel.h](kernel_8h.md)

Public kernel APIs.

[metric.h](metric_8h.md)

Prometheus metric interface.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:50

[prometheus\_collector::name](structprometheus__collector.md#a050b6094f92369225dce734ef9f50476)

const char \* name

Name of the collector.

**Definition** collector.h:52

[prometheus\_collector::metrics](structprometheus__collector.md#a389528dad4e2ada62ca85650b6be5972)

sys\_slist\_t metrics

Array of metrics associated with the collector.

**Definition** collector.h:54

[prometheus\_collector::lock](structprometheus__collector.md#a43e08aa447c0388d80771c33f59992b7)

struct k\_mutex lock

Mutex to protect the metrics list manipulation.

**Definition** collector.h:56

[prometheus\_collector::user\_data](structprometheus__collector.md#acd2c684c0c920f75e86d2560b4bb29e2)

void \* user\_data

User data.

**Definition** collector.h:62

[prometheus\_collector::user\_cb](structprometheus__collector.md#ae131dcdd35fbacd30a210b547718c6be)

prometheus\_scrape\_cb\_t user\_cb

User callback function.

**Definition** collector.h:60

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:47

[prometheus\_metric::collector](structprometheus__metric.md#a1138f189a5bdd44639dace426ef8f55a)

struct prometheus\_collector \* collector

Back pointer to the collector that this metric belongs to.

**Definition** metric.h:51

[prometheus\_metric::metric](structprometheus__metric.md#a67e8d38a696f2b20a076b8da6b1250e3)

void \* metric

Back pointer to the actual metric (counter, gauge, etc.).

**Definition** metric.h:56

[prometheus\_metric::user\_data](structprometheus__metric.md#ae2db853cae2c49634fda25eb23b825da)

void \* user\_data

User defined data.

**Definition** metric.h:68

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [prometheus](dir_2ecc9bf89aaa04d2ac23a37aff1f7dde.md)
- [collector.h](collector_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
