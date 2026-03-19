---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__prometheus.html
original_path: doxygen/html/group__prometheus.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| #define | [PROMETHEUS\_COLLECTOR\_DEFINE](#ga789b8557d1db7ad10133904e80e7f81c)(\_name) |
|  | Prometheus Collector definition. |
| #define | [PROMETHEUS\_COUNTER\_DEFINE](#ga467bbac42b48995598dbd370277b243b)(\_name, \_detail) |
|  | Prometheus Counter definition. |
| #define | [PROMETHEUS\_GAUGE\_DEFINE](#ga5398af0cd3d15ced8053b621170a4565)(\_name, \_detail) |
|  | Prometheus Gauge definition. |
| #define | [PROMETHEUS\_HISTOGRAM\_DEFINE](#gada4920e35290a96a76566cc6b4ab5a60)(\_name, \_detail) |
|  | Prometheus Histogram definition. |
| #define | [MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH](#gab8e197380d5a91070f5961fb8ab6a78a)   16 |
| #define | [MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH](#ga2abf70d0af09aa933ee7e57cf13b8c19)   16 |
| #define | [MAX\_PROMETHEUS\_LABELS\_PER\_METRIC](#ga5fd572e5351cda0855cb587e88c3a247)   5 |
| #define | [MAX\_METRIC\_NAME\_LENGTH](#ga0c2758847b60dece283eda02678edce8)   32 |
| #define | [MAX\_METRIC\_DESCRIPTION\_LENGTH](#ga9b788e35d8854a54faff830295b5b6ab)   64 |
| #define | [PROMETHEUS\_SUMMARY\_DEFINE](#ga05b125af8b981e61894a16d147f8ba2b)(\_name, \_detail) |
|  | Prometheus Summary definition. |

| Enumerations | |
| --- | --- |
| enum | [prometheus\_metric\_type](#ga3499408dda4e539634c332c797651932) { [PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b) = 0 , [PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd) , [PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074) , [PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf) } |
|  | Prometheus metric types. [More...](#ga3499408dda4e539634c332c797651932) |

| Functions | |
| --- | --- |
| int | [prometheus\_collector\_register\_metric](#ga976b9e82d747570cde631b03ee805a26) (struct [prometheus\_collector](structprometheus__collector.md) \*collector, struct [prometheus\_metric](structprometheus__metric.md) \*metric) |
|  | Register a metric with a Prometheus collector. |
| const void \* | [prometheus\_collector\_get\_metric](#ga428d008af1e84985bf7bce86ce0a408e) (const struct [prometheus\_collector](structprometheus__collector.md) \*collector, const char \*name) |
|  | Get a metric from a Prometheus collector. |
| int | [prometheus\_counter\_inc](#ga911670f61fa22d3834aecf5351c944e4) (struct [prometheus\_counter](structprometheus__counter.md) \*counter) |
|  | Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by one. |
| int | [prometheus\_format\_exposition](#ga23b33f57ee6ad1154f7903b505e604b1) (const struct [prometheus\_collector](structprometheus__collector.md) \*collector, char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | Format exposition data for Prometheus. |
| int | [prometheus\_gauge\_set](#ga3ddc5efbdb9639486862f3df4b845fce) (struct [prometheus\_gauge](structprometheus__gauge.md) \*gauge, double value) |
|  | Set the value of a Prometheus gauge metric. |
| int | [prometheus\_histogram\_observe](#gaf0f24e64833302b74397654001ca5026) (struct [prometheus\_histogram](structprometheus__histogram.md) \*histogram, double value) |
|  | Observe a value in a Prometheus histogram metric. |
| int | [prometheus\_summary\_observe](#ga7683de05e8b135161120ad5d3f2edc2c) (struct [prometheus\_summary](structprometheus__summary.md) \*summary, double value) |
|  | Observes a value in a Prometheus summary metric. |

## Detailed Description

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga9b788e35d8854a54faff830295b5b6ab)MAX\_METRIC\_DESCRIPTION\_LENGTH

| #define MAX\_METRIC\_DESCRIPTION\_LENGTH   64 |
| --- |

`#include <[metric.h](metric_8h.md)>`

## [◆ ](#ga0c2758847b60dece283eda02678edce8)MAX\_METRIC\_NAME\_LENGTH

| #define MAX\_METRIC\_NAME\_LENGTH   32 |
| --- |

`#include <[metric.h](metric_8h.md)>`

## [◆ ](#gab8e197380d5a91070f5961fb8ab6a78a)MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH

| #define MAX\_PROMETHEUS\_LABEL\_KEY\_LENGTH   16 |
| --- |

`#include <[label.h](label_8h.md)>`

## [◆ ](#ga2abf70d0af09aa933ee7e57cf13b8c19)MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH

| #define MAX\_PROMETHEUS\_LABEL\_VALUE\_LENGTH   16 |
| --- |

`#include <[label.h](label_8h.md)>`

## [◆ ](#ga5fd572e5351cda0855cb587e88c3a247)MAX\_PROMETHEUS\_LABELS\_PER\_METRIC

| #define MAX\_PROMETHEUS\_LABELS\_PER\_METRIC   5 |
| --- |

`#include <[label.h](label_8h.md)>`

## [◆ ](#ga789b8557d1db7ad10133904e80e7f81c)PROMETHEUS\_COLLECTOR\_DEFINE

| #define PROMETHEUS\_COLLECTOR\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[collector.h](collector_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_collector](structprometheus__collector.md), \_name) = { \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), .size = 0, .metric = {0}}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[prometheus\_collector](structprometheus__collector.md)

Prometheus collector definition.

**Definition** collector.h:32

Prometheus Collector definition.

This macro defines a Collector.

Parameters
:   | \_name | The collector's name. |
    | --- | --- |

## [◆ ](#ga467bbac42b48995598dbd370277b243b)PROMETHEUS\_COUNTER\_DEFINE

| #define PROMETHEUS\_COUNTER\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_detail* ) |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_counter](structprometheus__counter.md), \_name) = {.base = (void \*)(\_detail), \

.value = 0}

[prometheus\_counter](structprometheus__counter.md)

Type used to represent a Prometheus counter metric.

**Definition** counter.h:30

Prometheus Counter definition.

This macro defines a Counter metric.

Parameters
:   | \_name | The channel's name. |
    | --- | --- |
    | \_detail | The metric base. |

Example usage:

struct [prometheus\_metric](structprometheus__metric.md) http\_request\_counter = {

.type = [PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b),

.name = "http\_request\_counter",

.description = "HTTP request counter",

.num\_labels = 1,

.labels = {

{ .key = "http\_request", .value = "request\_count",}

},

};

[PROMETHEUS\_COUNTER\_DEFINE](#ga467bbac42b48995598dbd370277b243b)(test\_counter, &test\_counter\_metric);

[PROMETHEUS\_COUNTER\_DEFINE](#ga467bbac42b48995598dbd370277b243b)

#define PROMETHEUS\_COUNTER\_DEFINE(\_name, \_detail)

Prometheus Counter definition.

**Definition** counter.h:61

[PROMETHEUS\_COUNTER](#gga3499408dda4e539634c332c797651932aeeb062f6530e7defc38917215a22292b)

@ PROMETHEUS\_COUNTER

Prometheus Counter.

**Definition** metric.h:30

[prometheus\_metric](structprometheus__metric.md)

Type used to represent a Prometheus metric base.

**Definition** metric.h:48

## [◆ ](#ga5398af0cd3d15ced8053b621170a4565)PROMETHEUS\_GAUGE\_DEFINE

| #define PROMETHEUS\_GAUGE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_detail* ) |

`#include <[gauge.h](gauge_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_gauge](structprometheus__gauge.md), \_name) = {.base = (void \*)(\_detail), \

.value = 0}

[prometheus\_gauge](structprometheus__gauge.md)

Type used to represent a Prometheus gauge metric.

**Definition** gauge.h:28

Prometheus Gauge definition.

This macro defines a Gauge metric.

Parameters
:   | \_name | The channel's name. |
    | --- | --- |
    | \_detail | The metric base. |

Example usage:

struct [prometheus\_metric](structprometheus__metric.md) http\_request\_gauge = {

.type = [PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd),

.name = "http\_request\_gauge",

.description = "HTTP request gauge",

.num\_labels = 1,

.labels = {

{ .key = "http\_request", .value = "request\_count",}

},

};

[PROMETHEUS\_GAUGE\_DEFINE](#ga5398af0cd3d15ced8053b621170a4565)(test\_gauge, &test\_gauge\_metric);

[PROMETHEUS\_GAUGE\_DEFINE](#ga5398af0cd3d15ced8053b621170a4565)

#define PROMETHEUS\_GAUGE\_DEFINE(\_name, \_detail)

Prometheus Gauge definition.

**Definition** gauge.h:60

[PROMETHEUS\_GAUGE](#gga3499408dda4e539634c332c797651932ac941174554b0f81df0660fe3b4dde1dd)

@ PROMETHEUS\_GAUGE

Prometheus Gauge.

**Definition** metric.h:32

## [◆ ](#gada4920e35290a96a76566cc6b4ab5a60)PROMETHEUS\_HISTOGRAM\_DEFINE

| #define PROMETHEUS\_HISTOGRAM\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_detail* ) |

`#include <[histogram.h](histogram_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_histogram](structprometheus__histogram.md), \_name) = {.base = (void \*)(\_detail), \

.buckets = NULL, \

.num\_buckets = 0, \

.sum = 0, \

.count = 0}

[prometheus\_histogram](structprometheus__histogram.md)

Type used to represent a Prometheus histogram metric.

**Definition** histogram.h:42

Prometheus Histogram definition.

This macro defines a Histogram metric.

Parameters
:   | \_name | The channel's name. |
    | --- | --- |
    | \_detail | The metric base. |

Example usage:

struct [prometheus\_metric](structprometheus__metric.md) http\_request\_gauge = {

.type = [PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf),

.name = "http\_request\_histograms",

.description = "HTTP request histogram",

.num\_labels = 1,

.labels = {

{ .key = "request\_latency", .value = "request\_latency\_seconds",}

},

};

[PROMETHEUS\_HISTOGRAM\_DEFINE](#gada4920e35290a96a76566cc6b4ab5a60)(test\_histogram, &test\_histogram\_metric);

[PROMETHEUS\_HISTOGRAM\_DEFINE](#gada4920e35290a96a76566cc6b4ab5a60)

#define PROMETHEUS\_HISTOGRAM\_DEFINE(\_name, \_detail)

Prometheus Histogram definition.

**Definition** histogram.h:80

[PROMETHEUS\_HISTOGRAM](#gga3499408dda4e539634c332c797651932aa730ef807c2032aace17a2650a6023bf)

@ PROMETHEUS\_HISTOGRAM

Prometheus Histogram.

**Definition** metric.h:36

## [◆ ](#ga05b125af8b981e61894a16d147f8ba2b)PROMETHEUS\_SUMMARY\_DEFINE

| #define PROMETHEUS\_SUMMARY\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_detail* ) |

`#include <[summary.h](summary_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([prometheus\_summary](structprometheus__summary.md), \_name) = {.base = (void \*)(\_detail), \

.quantiles = NULL, \

.num\_quantiles = 0, \

.sum = 0, \

.count = 0}

[prometheus\_summary](structprometheus__summary.md)

Type used to represent a Prometheus summary metric.

**Definition** summary.h:42

Prometheus Summary definition.

This macro defines a Summary metric.

Parameters
:   | \_name | The channel's name. |
    | --- | --- |
    | \_detail | The metric base. |

Example usage:

struct [prometheus\_metric](structprometheus__metric.md) http\_request\_gauge = {

.type = [PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074),

.name = "http\_request\_summary",

.description = "HTTP request summary",

.num\_labels = 1,

.labels = {

{ .key = "request\_latency", .value = "request\_latency\_seconds",}

},

};

[PROMETHEUS\_SUMMARY\_DEFINE](#ga05b125af8b981e61894a16d147f8ba2b)(test\_summary, &test\_summary\_metric);

[PROMETHEUS\_SUMMARY\_DEFINE](#ga05b125af8b981e61894a16d147f8ba2b)

#define PROMETHEUS\_SUMMARY\_DEFINE(\_name, \_detail)

Prometheus Summary definition.

**Definition** summary.h:81

[PROMETHEUS\_SUMMARY](#gga3499408dda4e539634c332c797651932ad8b945aa5829b7915594856f7a4a1074)

@ PROMETHEUS\_SUMMARY

Prometheus Summary.

**Definition** metric.h:34

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

## [◆ ](#ga428d008af1e84985bf7bce86ce0a408e)prometheus\_collector\_get\_metric()

| const void \* prometheus\_collector\_get\_metric | ( | const struct [prometheus\_collector](structprometheus__collector.md) \* | *collector*, |
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

## [◆ ](#ga911670f61fa22d3834aecf5351c944e4)prometheus\_counter\_inc()

| int prometheus\_counter\_inc | ( | struct [prometheus\_counter](structprometheus__counter.md) \* | *counter* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[counter.h](net_2prometheus_2counter_8h.md)>`

Increment the value of a Prometheus counter metric Increments the value of the specified counter metric by one.

Parameters
:   | counter | Pointer to the counter metric to increment. |
    | --- | --- |

Returns
:   0 on success, negative errno on error.

## [◆ ](#ga23b33f57ee6ad1154f7903b505e604b1)prometheus\_format\_exposition()

| int prometheus\_format\_exposition | ( | const struct [prometheus\_collector](structprometheus__collector.md) \* | *collector*, |
| --- | --- | --- | --- |
|  |  | char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size* ) |

`#include <[formatter.h](formatter_8h.md)>`

Format exposition data for Prometheus.

Formats the exposition data collected by the specified collector into the provided buffer. Function to format metric data according to Prometheus text-based format

Parameters
:   | collector | Pointer to the collector containing the data to format. |
    | --- | --- |
    | buffer | Pointer to the buffer where the formatted exposition data will be stored. |
    | buffer\_size | Size of the buffer. |

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

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
