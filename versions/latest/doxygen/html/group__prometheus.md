---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__prometheus.html
original_path: doxygen/html/group__prometheus.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Prometheus API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Data Structures | |
| --- | --- |
| struct | [prometheus\_collector](structprometheus__collector.md) |
|  | Prometheus collector definition. [More...](structprometheus__collector.md#details) |
| struct | [prometheus\_counter](structprometheus__counter.md) |
|  | Type used to represent a Prometheus counter metric. [More...](structprometheus__counter.md#details) |
| struct | [prometheus\_gauge](structprometheus__gauge.md) |
|  | Type used to represent a Prometheus gauge metric. [More...](structprometheus__gauge.md#details) |
| struct | [prometheus\_histogram\_bucket](structprometheus__histogram__bucket.md) |
|  | Prometheus histogram bucket definition. [More...](structprometheus__histogram__bucket.md#details) |
| struct | [prometheus\_histogram](structprometheus__histogram.md) |
|  | Type used to represent a Prometheus histogram metric. [More...](structprometheus__histogram.md#details) |
| struct | [prometheus\_label](structprometheus__label.md) |
|  | Prometheus label definition. [More...](structprometheus__label.md#details) |
| struct | [prometheus\_metric](structprometheus__metric.md) |
|  | Type used to represent a Prometheus metric base. [More...](structprometheus__metric.md#details) |
| struct | [prometheus\_summary\_quantile](structprometheus__summary__quantile.md) |
|  | Prometheus summary quantile definition. [More...](structprometheus__summary__quantile.md#details) |
| struct | [prometheus\_summary](structprometheus__summary.md) |
|  | Type used to represent a Prometheus summary metric. [More...](structprometheus__summary.md#details) |

| Macros | |
| --- | --- |
| #define | [PROMETHEUS\_COLLECTOR\_DEFINE](#gaab3a797c867c6492dedb2b51774a48e5)(\_name, ...) |
|  | Prometheus Collector definition. |
| #define | [PROMETHEUS\_COUNTER\_DEFINE](#gadbfcfc7904d6388d2c9dc81d4803264c)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Counter definition. |
| #define | [PROMETHEUS\_GAUGE\_DEFINE](#ga362e708722846a3ca9299e8994becd13)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Gauge definition. |
| #define | [PROMETHEUS\_HISTOGRAM\_DEFINE](#gaf2ddb4e016104faaf543d9a028756a0c)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Histogram definition. |
| #define | [MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](#ga5fd572e5351cda0855cb587e88c3a247)   1 |
| #define | [PROMETHEUS\_SUMMARY\_DEFINE](#gaa3c043be86118ff9e8122136edc89cc4)(\_name, \_desc, \_label, \_collector, ...) |
|  | Prometheus Summary definition. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [prometheus\_scrape\_cb\_t](#ga4e2541cb094915187157d44a29e2d6b5)) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric, void \*user\_data) |
|  | Callback used to scrape a collector for a specific metric. |

| Enumerations | |
| --- | --- |
| enum | [prometheus\_metric\_type](#ga3499408dda4e539634c332c797651932) { [PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) = 0 , [PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd) , [PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074) , [PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf) } |
|  | Prometheus metric types. [More...](#ga3499408dda4e539634c332c797651932) |

| Functions | |
| --- | --- |
| int | [prometheus\_collector\_register\_metric](#ga976b9e82d747570cde631b03ee805a26) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric) |
|  | Register a metric with a Prometheus collector. |
| const void \* | [prometheus\_collector\_get\_metric](#ga757252a9157538870b1360924b16d0e0) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, const char \*name) |
|  | Get a metric from a Prometheus collector. |
| int | [prometheus\_collector\_walk\_metrics](#ga1bbdd8d5447144b21d3cda1ddac38ff0) (struct prometheus\_collector\_walk\_context \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Walk through all metrics in a Prometheus collector and format them into a buffer. |
| static int | [prometheus\_collector\_walk\_init](#ga1c70215409029bbe163bdfdb03bfba43) (struct prometheus\_collector\_walk\_context \*ctx, struct [prometheus\_collector](structprometheus__collector.md) \*collector) |
|  | Initialize the walker context to walk through all metrics. |
| int | [prometheus\_counter\_add](#ga9b7461d625acc075c9511249c67741ab) (struct [prometheus\_counter](structprometheus__counter.md) \*counter, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by arbitrary amount. |
| static int | [prometheus\_counter\_inc](#gad2220d089050bc5db1e5866429d515b3) (struct [prometheus\_counter](structprometheus__counter.md) \*counter) |
|  | Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by one. |
| int | [prometheus\_counter\_set](#ga8621228b7a66a6a42fb2cb838ec94dfe) (struct [prometheus\_counter](structprometheus__counter.md) \*counter, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set the counter value to specific value. |
| int | [prometheus\_format\_exposition](#ga7d219be7f2b3b49a2f936489bdf68fe8) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Format exposition data for Prometheus. |
| int | [prometheus\_format\_one\_metric](#ga2240cf4f807fe7180f21c8fab3fbbd66) (struct [prometheus\_metric](structprometheus__metric.md) \*metric, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size, int \*written) |
|  | Format exposition data for one metric for Prometheus. |
| int | [prometheus\_gauge\_set](#ga3ddc5efbdb9639486862f3df4b845fce) (struct [prometheus\_gauge](structprometheus__gauge.md) \*gauge, double value) |
|  | Set the value of a Prometheus gauge metric. |
| int | [prometheus\_histogram\_observe](#gaf0f24e64833302b74397654001ca5026) (struct [prometheus\_histogram](structprometheus__histogram.md) \*histogram, double value) |
|  | Observe a value in a Prometheus histogram metric. |
| int | [prometheus\_summary\_observe](#ga7683de05e8b135161120ad5d3f2edc2c) (struct [prometheus\_summary](structprometheus__summary.md) \*summary, double value) |
|  | Observes a value in a Prometheus summary metric. |
| int | [prometheus\_summary\_observe\_set](#ga98369eb2a7c8ce36f7570ed5b55410d8) (struct [prometheus\_summary](structprometheus__summary.md) \*summary, double value, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long count) |
|  | Set the summary value to specific value. |

## Detailed Description

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga5fd572e5351cda0855cb587e88c3a247)MAX\_PROMETHEUS\_LABELS\_PER\_METRIC

| #define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC   1 |
| --- |

`#include <[label.h](label_8h.md)>`

## [◆ ](#gaab3a797c867c6492dedb2b51774a48e5)PROMETHEUS\_COLLECTOR\_DEFINE

| #define PROMETHEUS\_COLLECTOR\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[collector.h](collector_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_collector](structprometheus__collector.md), \_name) = { \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.metrics = [SYS\_SLIST\_STATIC\_INIT](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)(&\_name.metrics), \

.lock = Z\_MUTEX\_INITIALIZER(\_name.lock), \

.user\_cb = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)( \

[LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_))), \

.user\_data = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_), ([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \

[GET\_ARGS\_LESS\_N](group__sys-util.md#ga01e1dc9b92e5be6895528d1da5f0c88b)(1, \_\_VA\_ARGS\_\_)))), \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[SYS\_SLIST\_STATIC\_INIT](group__single-linked-list__apis.md#ga7f4710125f45643b7acdaa58dbfff225)

#define SYS\_SLIST\_STATIC\_INIT(ptr\_to\_list)

Statically initialize a single-linked list.

**Definition** slist.h:209

[GET\_ARGS\_LESS\_N](group__sys-util.md#ga01e1dc9b92e5be6895528d1da5f0c88b)

#define GET\_ARGS\_LESS\_N(N,...)

Strips n first arguments from the argument list.

**Definition** util\_macro.h:401

[COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)

#define COND\_CODE\_0(\_flag, \_if\_0\_code, \_else\_code)

Like COND\_CODE\_1() except tests if \_flag is 0.

**Definition** util\_macro.h:219

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:667

[LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)

#define LIST\_DROP\_EMPTY(...)

Remove empty arguments from list.

**Definition** util\_macro.h:351

[GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)

#define GET\_ARG\_N(N,...)

Get nth argument from argument list.

**Definition** util\_macro.h:391

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:50

Prometheus Collector definition.

This macro defines a Collector.

Parameters
:   | \_name | The collector's name. |
    | --- | --- |
    | ... | Optional user callback function. If set, this function is called when the collector is scraped. The function should be of type [prometheus\_scrape\_cb\_t](#ga4e2541cb094915187157d44a29e2d6b5). Optional user data to pass to the user callback function. |

## [◆ ](#gadbfcfc7904d6388d2c9dc81d4803264c)PROMETHEUS\_COUNTER\_DEFINE

| #define PROMETHEUS\_COUNTER\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_desc*, |
|  |  |  | *\_label*, |
|  |  |  | *\_collector*, |
|  |  |  | ... ) |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_counter](structprometheus__counter.md), \_name) = { \

.base.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.base.type = [PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b), \

.base.description = \_desc, \

.base.labels[0] = \_\_DEBRACKET \_label, \

.base.num\_labels = 1, \

.base.collector = \_collector, \

.value = 0ULL, \

.user\_data = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)([LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_))), \

}

[PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)

@ PROMETHEUS\_COUNTER

Prometheus Counter.

**Definition** metric.h:32

[prometheus\_counter](structprometheus__counter.md)

Type used to represent a Prometheus counter metric.

**Definition** counter.h:31

Prometheus Counter definition.

This macro defines a Counter metric. If you want to make the counter static, then add "static" keyword before the PROMETHEUS\_COUNTER\_DEFINE.

Parameters
:   | \_name | The counter metric name |
    | --- | --- |
    | \_desc | Counter description |
    | \_label | Label for the metric. Additional labels can be added at runtime. |
    | \_collector | Collector to map this metric. Can be set to NULL if it not yet known. |
    | ... | Optional user data specific to this metric instance. |

Example usage:

[PROMETHEUS\_COUNTER\_DEFINE](#gadbfcfc7904d6388d2c9dc81d4803264c)(http\_request\_counter, "HTTP request counter",

({ .key = "http\_request", .value = "request\_count" }),

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

[PROMETHEUS\_COUNTER\_DEFINE](#gadbfcfc7904d6388d2c9dc81d4803264c)

#define PROMETHEUS\_COUNTER\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Counter definition.

**Definition** counter.h:60

## [◆ ](#ga362e708722846a3ca9299e8994becd13)PROMETHEUS\_GAUGE\_DEFINE

| #define PROMETHEUS\_GAUGE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_desc*, |
|  |  |  | *\_label*, |
|  |  |  | *\_collector*, |
|  |  |  | ... ) |

`#include <[gauge.h](gauge_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_gauge](structprometheus__gauge.md), \_name) = { \

.base.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.base.type = [PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd), \

.base.description = \_desc, \

.base.labels[0] = \_\_DEBRACKET \_label, \

.base.num\_labels = 1, \

.base.collector = \_collector, \

.value = 0.0, \

.user\_data = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)([LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_))), \

}

[PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)

@ PROMETHEUS\_GAUGE

Prometheus Gauge.

**Definition** metric.h:34

[prometheus\_gauge](structprometheus__gauge.md)

Type used to represent a Prometheus gauge metric.

**Definition** gauge.h:29

Prometheus Gauge definition.

This macro defines a Gauge metric. If you want to make the gauge static, then add "static" keyword before the PROMETHEUS\_GAUGE\_DEFINE.

Parameters
:   | \_name | The gauge metric name. |
    | --- | --- |
    | \_desc | Gauge description |
    | \_label | Label for the metric. Additional labels can be added at runtime. |
    | \_collector | Collector to map this metric. Can be set to NULL if it not yet known. |
    | ... | Optional user data specific to this metric instance. |

Example usage:

[PROMETHEUS\_GAUGE\_DEFINE](#ga362e708722846a3ca9299e8994becd13)(http\_request\_gauge, "HTTP request gauge",

({ .key = "http\_request", .value = "request\_count" }),

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

[PROMETHEUS\_GAUGE\_DEFINE](#ga362e708722846a3ca9299e8994becd13)

#define PROMETHEUS\_GAUGE\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Gauge definition.

**Definition** gauge.h:59

## [◆ ](#gaf2ddb4e016104faaf543d9a028756a0c)PROMETHEUS\_HISTOGRAM\_DEFINE

| #define PROMETHEUS\_HISTOGRAM\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_desc*, |
|  |  |  | *\_label*, |
|  |  |  | *\_collector*, |
|  |  |  | ... ) |

`#include <[histogram.h](histogram_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_histogram](structprometheus__histogram.md), \_name) = { \

.base.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.base.type = [PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf), \

.base.description = \_desc, \

.base.labels[0] = \_\_DEBRACKET \_label, \

.base.num\_labels = 1, \

.base.collector = \_collector, \

.buckets = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

.num\_buckets = 0, \

.sum = 0.0, \

.count = 0U, \

.user\_data = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)([LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_))), \

}

[PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)

@ PROMETHEUS\_HISTOGRAM

Prometheus Histogram.

**Definition** metric.h:38

[prometheus\_histogram](structprometheus__histogram.md)

Type used to represent a Prometheus histogram metric.

**Definition** histogram.h:43

Prometheus Histogram definition.

This macro defines a Histogram metric. If you want to make the histogram static, then add "static" keyword before the PROMETHEUS\_HISTOGRAM\_DEFINE.

Parameters
:   | \_name | The histogram metric name. |
    | --- | --- |
    | \_desc | Histogram description |
    | \_label | Label for the metric. Additional labels can be added at runtime. |
    | \_collector | Collector to map this metric. Can be set to NULL if it not yet known. |
    | ... | Optional user data specific to this metric instance. |

Example usage:

[PROMETHEUS\_HISTOGRAM\_DEFINE](#gaf2ddb4e016104faaf543d9a028756a0c)(http\_request\_histogram, "HTTP request histogram",

({ .key = "request\_latency", .value = "request\_latency\_seconds" }),

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

[PROMETHEUS\_HISTOGRAM\_DEFINE](#gaf2ddb4e016104faaf543d9a028756a0c)

#define PROMETHEUS\_HISTOGRAM\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Histogram definition.

**Definition** histogram.h:79

## [◆ ](#gaa3c043be86118ff9e8122136edc89cc4)PROMETHEUS\_SUMMARY\_DEFINE

| #define PROMETHEUS\_SUMMARY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_desc*, |
|  |  |  | *\_label*, |
|  |  |  | *\_collector*, |
|  |  |  | ... ) |

`#include <[summary.h](summary_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_summary](structprometheus__summary.md), \_name) = { \

.base.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.base.type = [PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074), \

.base.description = \_desc, \

.base.labels[0] = \_\_DEBRACKET \_label, \

.base.num\_labels = 1, \

.base.collector = \_collector, \

.quantiles = [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

.num\_quantiles = 0, \

.sum = 0.0, \

.count = 0U, \

.user\_data = [COND\_CODE\_0](group__sys-util.md#ga5483ea38af79bc6c4509936288705377)( \

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)([LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(\_\_VA\_ARGS\_\_, \_)), \

([NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)), \

([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_))), \

}

[PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)

@ PROMETHEUS\_SUMMARY

Prometheus Summary.

**Definition** metric.h:36

[prometheus\_summary](structprometheus__summary.md)

Type used to represent a Prometheus summary metric.

**Definition** summary.h:45

Prometheus Summary definition.

This macro defines a Summary metric. If you want to make the summary static, then add "static" keyword before the PROMETHEUS\_SUMMARY\_DEFINE.

Parameters
:   | \_name | The summary metric name. |
    | --- | --- |
    | \_desc | Summary description |
    | \_label | Label for the metric. Additional labels can be added at runtime. |
    | \_collector | Collector to map this metric. Can be set to NULL if it not yet known. |
    | ... | Optional user data specific to this metric instance. |

Example usage:

[PROMETHEUS\_SUMMARY\_DEFINE](#gaa3c043be86118ff9e8122136edc89cc4)(http\_request\_summary, "HTTP request summary",

({ .key = "request\_latency",

.value = "request\_latency\_seconds" }), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

[PROMETHEUS\_SUMMARY\_DEFINE](#gaa3c043be86118ff9e8122136edc89cc4)

#define PROMETHEUS\_SUMMARY\_DEFINE(\_name, \_desc, \_label, \_collector,...)

Prometheus Summary definition.

**Definition** summary.h:83

## Typedef Documentation

## [◆ ](#ga4e2541cb094915187157d44a29e2d6b5)prometheus\_scrape\_cb\_t

| typedef int(\* prometheus\_scrape\_cb\_t) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric, void \*user\_data) |
| --- |

`#include <[collector.h](collector_8h.md)>`

Callback used to scrape a collector for a specific metric.

Parameters
:   | collector | A valid pointer on the collector to scrape |
    | --- | --- |
    | metric | A valid pointer on the metric to scrape |
    | user\_data | A valid pointer to a user data or NULL |

Returns
:   0 if successful, otherwise a negative error code.

## Enumeration Type Documentation

## [◆ ](#ga3499408dda4e539634c332c797651932)prometheus\_metric\_type

| enum [prometheus\_metric\_type](#ga3499408dda4e539634c332c797651932) |
| --- |

`#include <[metric.h](metric_8h.md)>`

Prometheus metric types.

- References
- See [https://prometheus.io/docs/concepts/metric\_types](https://prometheus.io/docs/concepts/metric_types)

| Enumerator | |
| --- | --- |
| PROMETHEUS\_COUNTER | Prometheus Counter. |
| PROMETHEUS\_GAUGE | Prometheus Gauge. |
| PROMETHEUS\_SUMMARY | Prometheus Summary. |
| PROMETHEUS\_HISTOGRAM | Prometheus Histogram. |

## Function Documentation

## [◆ ](#ga757252a9157538870b1360924b16d0e0)prometheus\_collector\_get\_metric()

| const void \* prometheus\_collector\_get\_metric | ( | struct [prometheus\_collector](structprometheus__collector.md) \* | *collector*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

`#include <[collector.h](collector_8h.md)>`

Get a metric from a Prometheus collector.

Retrieves the metric with the specified name from the given collector.

Parameters
:   | collector | Pointer to the collector to retrieve the metric from. |
    | --- | --- |
    | name | Name of the metric to retrieve. |

Returns
:   Pointer to the retrieved metric, or NULL if not found.

## [◆ ](#ga976b9e82d747570cde631b03ee805a26)prometheus\_collector\_register\_metric()

| int prometheus\_collector\_register\_metric | ( | struct [prometheus\_collector](structprometheus__collector.md) \* | *collector*, |
| --- | --- | --- | --- |
|  |  | struct [prometheus\_metric](structprometheus__metric.md) \* | *metric* ) |

`#include <[collector.h](collector_8h.md)>`

Register a metric with a Prometheus collector.

Registers the specified metric with the given collector.

Parameters
:   | collector | Pointer to the collector to register the metric with. |
    | --- | --- |
    | metric | Pointer to the metric to register. |

Returns
:   0 if successful, otherwise a negative error code.

Return values
:   | -EINVAL | Invalid arguments. |
    | --- | --- |
    | -ENOMEM | Not enough memory to register the metric. |

## [◆ ](#ga1c70215409029bbe163bdfdb03bfba43)prometheus\_collector\_walk\_init()

| | int prometheus\_collector\_walk\_init | ( | struct prometheus\_collector\_walk\_context \* | *ctx*, | | --- | --- | --- | --- | |  |  | struct [prometheus\_collector](structprometheus__collector.md) \* | *collector* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[collector.h](collector_8h.md)>`

Initialize the walker context to walk through all metrics.

Parameters
:   | ctx | Pointer to the walker context. |
    | --- | --- |
    | collector | Pointer to the collector to walk through. |

Returns
:   0 if successful, otherwise a negative error code.

## [◆ ](#ga1bbdd8d5447144b21d3cda1ddac38ff0)prometheus\_collector\_walk\_metrics()

| int prometheus\_collector\_walk\_metrics | ( | struct prometheus\_collector\_walk\_context \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size* ) |

`#include <[collector.h](collector_8h.md)>`

Walk through all metrics in a Prometheus collector and format them into a buffer.

Parameters
:   | ctx | Pointer to the walker context. |
    | --- | --- |
    | buffer | Pointer to the buffer to store the formatted metrics. |
    | buffer\_size | Size of the buffer. |

Returns
:   0 if successful and we went through all metrics, -EAGAIN if we need to call this function again, any other negative error code means an error occurred.

## [◆ ](#ga9b7461d625acc075c9511249c67741ab)prometheus\_counter\_add()

| int prometheus\_counter\_add | ( | struct [prometheus\_counter](structprometheus__counter.md) \* | *counter*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by arbitrary amount.

Parameters
:   | counter | Pointer to the counter metric to increment. |
    | --- | --- |
    | value | Amount to increment the counter by. |

Returns
:   0 on success, negative errno on error.

## [◆ ](#gad2220d089050bc5db1e5866429d515b3)prometheus\_counter\_inc()

| | int prometheus\_counter\_inc | ( | struct [prometheus\_counter](structprometheus__counter.md) \* | *counter* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by one.

Parameters
:   | counter | Pointer to the counter metric to increment. |
    | --- | --- |

Returns
:   0 on success, negative errno on error.

## [◆ ](#ga8621228b7a66a6a42fb2cb838ec94dfe)prometheus\_counter\_set()

| int prometheus\_counter\_set | ( | struct [prometheus\_counter](structprometheus__counter.md) \* | *counter*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *value* ) |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

Set the counter value to specific value.

The new value must be higher than the current value. This function can be used if we cannot add individual increments to the counter but need to periodically update the counter value. This function will add the difference between the new value and the old value to the counter.

Parameters
:   | counter | Pointer to the counter metric to increment. |
    | --- | --- |
    | value | New value of the counter. |

Returns
:   0 on success, negative errno on error.

## [◆ ](#ga7d219be7f2b3b49a2f936489bdf68fe8)prometheus\_format\_exposition()

| int prometheus\_format\_exposition | ( | struct [prometheus\_collector](structprometheus__collector.md) \* | *collector*, |
| --- | --- | --- | --- |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size* ) |

`#include <[formatter.h](formatter_8h.md)>`

Format exposition data for Prometheus.

Formats the exposition data collected by the specified collector into the provided buffer. Function will format metric data according to Prometheus text-based format

Parameters
:   | collector | Pointer to the collector containing the data to format. |
    | --- | --- |
    | buffer | Pointer to the buffer where the formatted exposition data will be stored. |
    | buffer\_size | Size of the buffer. |

Returns
:   0 on success, negative errno on error.

## [◆ ](#ga2240cf4f807fe7180f21c8fab3fbbd66)prometheus\_format\_one\_metric()

| int prometheus\_format\_one\_metric | ( | struct [prometheus\_metric](structprometheus__metric.md) \* | *metric*, |
| --- | --- | --- | --- |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size*, |
|  |  | int \* | *written* ) |

`#include <[formatter.h](formatter_8h.md)>`

Format exposition data for one metric for Prometheus.

Formats the exposition data of one specific metric into the provided buffer. Function will format metric data according to Prometheus text-based format.

Parameters
:   | metric | Pointer to the metric containing the data to format. |
    | --- | --- |
    | buffer | Pointer to the buffer where the formatted exposition data will be stored. |
    | buffer\_size | Size of the buffer. |
    | written | How many bytes have been written to the buffer. |

Returns
:   0 on success, negative errno on error.

## [◆ ](#ga3ddc5efbdb9639486862f3df4b845fce)prometheus\_gauge\_set()

| int prometheus\_gauge\_set | ( | struct [prometheus\_gauge](structprometheus__gauge.md) \* | *gauge*, |
| --- | --- | --- | --- |
|  |  | double | *value* ) |

`#include <[gauge.h](gauge_8h.md)>`

Set the value of a Prometheus gauge metric.

Sets the value of the specified gauge metric to the given value.

Parameters
:   | gauge | Pointer to the gauge metric to set. |
    | --- | --- |
    | value | Value to set the gauge metric to. |

Returns
:   0 on success, -EINVAL if the value is negative.

## [◆ ](#gaf0f24e64833302b74397654001ca5026)prometheus\_histogram\_observe()

| int prometheus\_histogram\_observe | ( | struct [prometheus\_histogram](structprometheus__histogram.md) \* | *histogram*, |
| --- | --- | --- | --- |
|  |  | double | *value* ) |

`#include <[histogram.h](histogram_8h.md)>`

Observe a value in a Prometheus histogram metric.

Observes the specified value in the given histogram metric.

Parameters
:   | histogram | Pointer to the histogram metric to observe. |
    | --- | --- |
    | value | Value to observe in the histogram metric. |

Returns
:   0 on success, -EINVAL if the value is negative.

## [◆ ](#ga7683de05e8b135161120ad5d3f2edc2c)prometheus\_summary\_observe()

| int prometheus\_summary\_observe | ( | struct [prometheus\_summary](structprometheus__summary.md) \* | *summary*, |
| --- | --- | --- | --- |
|  |  | double | *value* ) |

`#include <[summary.h](summary_8h.md)>`

Observes a value in a Prometheus summary metric.

Observes the specified value in the given summary metric.

Parameters
:   | summary | Pointer to the summary metric to observe. |
    | --- | --- |
    | value | Value to observe in the summary metric. |

Returns
:   0 on success, -EINVAL if the value is negative.

## [◆ ](#ga98369eb2a7c8ce36f7570ed5b55410d8)prometheus\_summary\_observe\_set()

| int prometheus\_summary\_observe\_set | ( | struct [prometheus\_summary](structprometheus__summary.md) \* | *summary*, |
| --- | --- | --- | --- |
|  |  | double | *value*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *count* ) |

`#include <[summary.h](summary_8h.md)>`

Set the summary value to specific value.

The new value must be higher than the current value. This function can be used if we cannot add individual increments to the summary but need to periodically update the counter value. This function will add the difference between the new value and the old value to the summary fields.

Parameters
:   | summary | Pointer to the summary metric to increment. |
    | --- | --- |
    | value | New value of the summary. |
    | count | New counter value of the summary. |

Returns
:   0 on success, negative errno on error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
