---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__udc__buf.html
original_path: doxygen/html/group__udc__buf.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Buffer macros and definitions used in USB device support

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

Buffer macros and definitions used in USB device support.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc)   Z\_UDC\_BUF\_ALIGN |
|  | Buffer alignment required by the UDC driver. |
| #define | [UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e)   Z\_UDC\_BUF\_GRANULARITY |
|  | Buffer granularity required by the UDC driver. |
| #define | [UDC\_STATIC\_BUF\_DEFINE](#gae5cb6affd574da5f4cd0c25e9178a0eb)(name, size) |
|  | Define a UDC driver-compliant static buffer. |
| #define | [IS\_UDC\_ALIGNED](#ga4e77ceb9142c9d414966f0c4e0eb7710)(buf) |
|  | Verify that the buffer is aligned as required by the UDC driver. |
| #define | [UDC\_BUF\_POOL\_VAR\_DEFINE](#ga064d3f73dbde0f98479ffdad5141e8c0)(pname, count, size, ud\_size, fdestroy) |
|  | Define a new pool for UDC buffers with variable-size payloads. |
| #define | [UDC\_BUF\_POOL\_DEFINE](#gac96f1518df5748927c3377cb3abc222d)(pname, count, size, ud\_size, fdestroy) |
|  | Define a new pool for UDC buffers based on fixed-size data. |

## Detailed Description

Buffer macros and definitions used in USB device support.

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga4e77ceb9142c9d414966f0c4e0eb7710)IS\_UDC\_ALIGNED

| #define IS\_UDC\_ALIGNED | ( |  | *buf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[udc_buf.h](udc__buf_8h.md)>`

**Value:**

[IS\_ALIGNED](group__sys-util.md#gabf601ce26a569512a4e422a074934660)(buf, [UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc))

[IS\_ALIGNED](group__sys-util.md#gabf601ce26a569512a4e422a074934660)

#define IS\_ALIGNED(ptr, align)

Check if ptr is aligned to align alignment.

**Definition** util.h:317

[UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc)

#define UDC\_BUF\_ALIGN

Buffer alignment required by the UDC driver.

**Definition** udc\_buf.h:57

Verify that the buffer is aligned as required by the UDC driver.

See also
:   [IS\_ALIGNED](group__sys-util.md#gabf601ce26a569512a4e422a074934660 "Check if ptr is aligned to align alignment.")

Parameters
:   | buf | Buffer pointer |
    | --- | --- |

## [◆ ](#gaf53404357b1184c1eda430e92cd696dc)UDC\_BUF\_ALIGN

| #define UDC\_BUF\_ALIGN   Z\_UDC\_BUF\_ALIGN |
| --- |

`#include <[udc_buf.h](udc__buf_8h.md)>`

Buffer alignment required by the UDC driver.

## [◆ ](#ga87ea6bf98e8be1ca3378928fbf03bf8e)UDC\_BUF\_GRANULARITY

| #define UDC\_BUF\_GRANULARITY   Z\_UDC\_BUF\_GRANULARITY |
| --- |

`#include <[udc_buf.h](udc__buf_8h.md)>`

Buffer granularity required by the UDC driver.

## [◆ ](#gac96f1518df5748927c3377cb3abc222d)UDC\_BUF\_POOL\_DEFINE

| #define UDC\_BUF\_POOL\_DEFINE | ( |  | *pname*, |
| --- | --- | --- | --- |
|  |  |  | *count*, |
|  |  |  | *size*, |
|  |  |  | *ud\_size*, |
|  |  |  | *fdestroy* ) |

`#include <[udc_buf.h](udc__buf_8h.md)>`

**Value:**

\_NET\_BUF\_ARRAY\_DEFINE(pname, count, ud\_size); \

BUILD\_ASSERT(([UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e)) % ([UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc)) == 0, \

"Code assumes granurality is multiple of alignment"); \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Z\_UDC\_BUF\_SECTION \_\_aligned([UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc)) \

net\_buf\_data\_##pname[count][[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(size, [UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e))];\

static const struct net\_buf\_pool\_fixed net\_buf\_fixed\_##pname = { \

.data\_pool = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)net\_buf\_data\_##pname, \

}; \

static const struct net\_buf\_data\_alloc net\_buf\_fixed\_alloc\_##pname = { \

.cb = &net\_buf\_fixed\_cb, \

.alloc\_data = (void \*)&net\_buf\_fixed\_##pname, \

.max\_alloc\_size = [ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(size, [UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e)), \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(net\_buf\_pool, pname) = \

NET\_BUF\_POOL\_INITIALIZER(pname, &net\_buf\_fixed\_alloc\_##pname, \

\_net\_buf\_##pname, count, ud\_size, \

fdestroy)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)

#define ROUND\_UP(x, align)

Value of x rounded up to the next multiple of align.

**Definition** util.h:322

[UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e)

#define UDC\_BUF\_GRANULARITY

Buffer granularity required by the UDC driver.

**Definition** udc\_buf.h:60

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Define a new pool for UDC buffers based on fixed-size data.

This macro is similar to [NET\_BUF\_POOL\_DEFINE](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc "Define a new pool for buffers."), but provides buffers with alignment and granularity suitable for use by UDC driver.

See also
:   [NET\_BUF\_POOL\_DEFINE](group__net__buf.md#ga810aba8ba321fd012edc238ea9fe19dc "Define a new pool for buffers.")

Parameters
:   | pname | Name of the pool variable. |
    | --- | --- |
    | count | Number of buffers in the pool. |
    | size | Maximum data payload per buffer. |
    | ud\_size | User data space to reserve per buffer. |
    | fdestroy | Optional destroy callback when buffer is freed. |

## [◆ ](#ga064d3f73dbde0f98479ffdad5141e8c0)UDC\_BUF\_POOL\_VAR\_DEFINE

| #define UDC\_BUF\_POOL\_VAR\_DEFINE | ( |  | *pname*, |
| --- | --- | --- | --- |
|  |  |  | *count*, |
|  |  |  | *size*, |
|  |  |  | *ud\_size*, |
|  |  |  | *fdestroy* ) |

`#include <[udc_buf.h](udc__buf_8h.md)>`

**Value:**

\_NET\_BUF\_ARRAY\_DEFINE(pname, count, ud\_size); \

UDC\_K\_HEAP\_DEFINE(net\_buf\_mem\_pool\_##pname, size); \

static const struct net\_buf\_data\_alloc net\_buf\_data\_alloc\_##pname = { \

.cb = &net\_buf\_dma\_cb, \

.alloc\_data = &net\_buf\_mem\_pool\_##pname, \

.max\_alloc\_size = 0, \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([net\_buf\_pool](structnet__buf__pool.md), pname) = \

NET\_BUF\_POOL\_INITIALIZER(pname, &net\_buf\_data\_alloc\_##pname, \

\_net\_buf\_##pname, count, ud\_size, \

fdestroy)

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

Define a new pool for UDC buffers with variable-size payloads.

This macro is similar to [NET\_BUF\_POOL\_VAR\_DEFINE](group__net__buf.md#ga90e691e793c964847d737f5ecf7646ec "Define a new pool for buffers with variable size payloads."), but provides buffers with alignment and granularity suitable for use by UDC driver.

See also
:   [NET\_BUF\_POOL\_VAR\_DEFINE](group__net__buf.md#ga90e691e793c964847d737f5ecf7646ec "Define a new pool for buffers with variable size payloads.")

Parameters
:   | pname | Name of the pool variable. |
    | --- | --- |
    | count | Number of buffers in the pool. |
    | size | Maximum data payload per buffer. |
    | ud\_size | User data space to reserve per buffer. |
    | fdestroy | Optional destroy callback when buffer is freed. |

## [◆ ](#gae5cb6affd574da5f4cd0c25e9178a0eb)UDC\_STATIC\_BUF\_DEFINE

| #define UDC\_STATIC\_BUF\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *size* ) |

`#include <[udc_buf.h](udc__buf_8h.md)>`

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) Z\_UDC\_BUF\_SECTION \_\_aligned([UDC\_BUF\_ALIGN](#gaf53404357b1184c1eda430e92cd696dc)) \

name[[ROUND\_UP](group__sys-util.md#gaada5610108b15d85c65d863b0c646ef3)(size, [UDC\_BUF\_GRANULARITY](#ga87ea6bf98e8be1ca3378928fbf03bf8e))];

Define a UDC driver-compliant static buffer.

This macro should be used if the application defines its own buffers to be used for USB transfers.

Parameters
:   | name | Buffer name |
    | --- | --- |
    | size | Buffer size |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
