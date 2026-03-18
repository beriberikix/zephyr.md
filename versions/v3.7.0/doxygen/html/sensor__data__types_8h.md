---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sensor__data__types_8h.html
original_path: doxygen/html/sensor__data__types_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_data\_types.h File Reference

`#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h_source.md)>`  
`#include <[zephyr/dsp/print_format.h](print__format_8h_source.md)>`  
`#include <[inttypes.h](inttypes_8h_source.md)>`

[Go to the source code of this file.](sensor__data__types_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sensor\_data\_header](structsensor__data__header.md) |
| struct | [sensor\_three\_axis\_data](structsensor__three__axis__data.md) |
|  | Data for a sensor channel which reports on three axes. [More...](structsensor__three__axis__data.md#details) |
| struct | [sensor\_three\_axis\_data::sensor\_three\_axis\_sample\_data](structsensor__three__axis__data_1_1sensor__three__axis__sample__data.md) |
| struct | [sensor\_occurrence\_data](structsensor__occurrence__data.md) |
|  | Data from a sensor where we only care about an event occurring. [More...](structsensor__occurrence__data.md#details) |
| struct | [sensor\_occurrence\_data::sensor\_occurrence\_sample\_data](structsensor__occurrence__data_1_1sensor__occurrence__sample__data.md) |
| struct | [sensor\_q31\_data](structsensor__q31__data.md) |
| struct | [sensor\_q31\_data::sensor\_q31\_sample\_data](structsensor__q31__data_1_1sensor__q31__sample__data.md) |
| struct | [sensor\_byte\_data](structsensor__byte__data.md) |
|  | Data from a sensor that produces a byte of data. [More...](structsensor__byte__data.md#details) |
| struct | [sensor\_byte\_data::sensor\_byte\_sample\_data](structsensor__byte__data_1_1sensor__byte__sample__data.md) |
| struct | [sensor\_uint64\_data](structsensor__uint64__data.md) |
|  | Data from a sensor that produces a count like value. [More...](structsensor__uint64__data.md#details) |
| struct | [sensor\_uint64\_data::sensor\_uint64\_sample\_data](structsensor__uint64__data_1_1sensor__uint64__sample__data.md) |

| Macros | |
| --- | --- |
| #define | [PRIsensor\_three\_axis\_data](#a0c6a78118f9360ed97b1327cf3a3fa9a)   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns, (%" PRIq(6) ", %" [PRIq](group__math__printing.md#ga08618ad8449ee21f0a57c151541e8ef8)(6) ", %" [PRIq](group__math__printing.md#ga08618ad8449ee21f0a57c151541e8ef8)(6) ")" |
| #define | [PRIsensor\_three\_axis\_data\_arg](#af8c5897a6515c73ec1795b800590a7b4)(data\_, readings\_offset\_) |
| #define | [PRIsensor\_occurrence\_data](#a9862e4197bb6146b3e41958f427c9f9a)   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns" |
| #define | [PRIsensor\_occurrence\_data\_arg](#a3f8a660a28578bbb7baf08fefbca7ac4)(data\_, readings\_offset\_) |
| #define | [PRIsensor\_q31\_data](#a92ae9197089ece9de51db496c9ed5ed6)   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns (%" PRIq(6) ")" |
| #define | [PRIsensor\_q31\_data\_arg](#aac3d2a0c462c05c26f7dee0fa0e1ef62)(data\_, readings\_offset\_) |
| #define | [PRIsensor\_byte\_data](#af73f68f6b94dc1251dfeeb5caf141e94)(field\_name\_) |
| #define | [PRIsensor\_byte\_data\_arg](#a36cfa50e20150d44c6a254afc149eb5b)(data\_, readings\_offset\_, field\_name\_) |
| #define | [PRIsensor\_uint64\_data](#abc9a284dcd602d240f9bd9b097703634)   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns (%" PRIu64 ")" |
| #define | [PRIsensor\_uint64\_data\_arg](#a06ef9de1e3821289cd22575410edc80f)(data\_, readings\_offset\_) |

## Macro Definition Documentation

## [◆ ](#af73f68f6b94dc1251dfeeb5caf141e94)PRIsensor\_byte\_data

| #define PRIsensor\_byte\_data | ( |  | *field\_name\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns (" [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(field\_name\_) " = %" [PRIu8](inttypes_8h.md#a8673208d2d48018fcce020ef59f8ec4f) ")"

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[PRIu8](inttypes_8h.md#a8673208d2d48018fcce020ef59f8ec4f)

#define PRIu8

**Definition** inttypes.h:58

[PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5)

#define PRIu64

**Definition** inttypes.h:61

## [◆ ](#a36cfa50e20150d44c6a254afc149eb5b)PRIsensor\_byte\_data\_arg

| #define PRIsensor\_byte\_data\_arg | ( |  | *data\_*, |
| --- | --- | --- | --- |
|  |  |  | *readings\_offset\_*, |
|  |  |  | *field\_name\_* ) |

**Value:**

(data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

(data\_).readings[(readings\_offset\_)].field\_name\_

## [◆ ](#a9862e4197bb6146b3e41958f427c9f9a)PRIsensor\_occurrence\_data

| #define PRIsensor\_occurrence\_data   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns" |
| --- |

## [◆ ](#a3f8a660a28578bbb7baf08fefbca7ac4)PRIsensor\_occurrence\_data\_arg

| #define PRIsensor\_occurrence\_data\_arg | ( |  | *data\_*, |
| --- | --- | --- | --- |
|  |  |  | *readings\_offset\_* ) |

**Value:**

(data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta

## [◆ ](#a92ae9197089ece9de51db496c9ed5ed6)PRIsensor\_q31\_data

| #define PRIsensor\_q31\_data   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns (%" PRIq(6) ")" |
| --- |

## [◆ ](#aac3d2a0c462c05c26f7dee0fa0e1ef62)PRIsensor\_q31\_data\_arg

| #define PRIsensor\_q31\_data\_arg | ( |  | *data\_*, |
| --- | --- | --- | --- |
|  |  |  | *readings\_offset\_* ) |

**Value:**

(data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

[PRIq\_arg](group__math__printing.md#gad0393d2bb183784a9c09f2c05d7987f9)((data\_).readings[(readings\_offset\_)].value, 6, (data\_).shift)

[PRIq\_arg](group__math__printing.md#gad0393d2bb183784a9c09f2c05d7987f9)

#define PRIq\_arg(q, precision, shift)

Insert Q value arguments to print format.

**Definition** print\_format.h:58

## [◆ ](#a0c6a78118f9360ed97b1327cf3a3fa9a)PRIsensor\_three\_axis\_data

| #define PRIsensor\_three\_axis\_data   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns, (%" PRIq(6) ", %" [PRIq](group__math__printing.md#ga08618ad8449ee21f0a57c151541e8ef8)(6) ", %" [PRIq](group__math__printing.md#ga08618ad8449ee21f0a57c151541e8ef8)(6) ")" |
| --- |

## [◆ ](#af8c5897a6515c73ec1795b800590a7b4)PRIsensor\_three\_axis\_data\_arg

| #define PRIsensor\_three\_axis\_data\_arg | ( |  | *data\_*, |
| --- | --- | --- | --- |
|  |  |  | *readings\_offset\_* ) |

**Value:**

(data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

[PRIq\_arg](group__math__printing.md#gad0393d2bb183784a9c09f2c05d7987f9)((data\_).readings[(readings\_offset\_)].x, 6, (data\_).shift), \

PRIq\_arg((data\_).readings[(readings\_offset\_)].y, 6, (data\_).shift), \

PRIq\_arg((data\_).readings[(readings\_offset\_)].z, 6, (data\_).shift)

## [◆ ](#abc9a284dcd602d240f9bd9b097703634)PRIsensor\_uint64\_data

| #define PRIsensor\_uint64\_data   [PRIu64](inttypes_8h.md#ac582131d7a7c8ee57e73180d1714f9d5) "ns (%" PRIu64 ")" |
| --- |

## [◆ ](#a06ef9de1e3821289cd22575410edc80f)PRIsensor\_uint64\_data\_arg

| #define PRIsensor\_uint64\_data\_arg | ( |  | *data\_*, |
| --- | --- | --- | --- |
|  |  |  | *readings\_offset\_* ) |

**Value:**

(data\_).header.base\_timestamp\_ns + (data\_).readings[(readings\_offset\_)].timestamp\_delta, \

(data\_).readings[(readings\_offset\_)].value

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor\_data\_types.h](sensor__data__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
