---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__log__msg.html
original_path: doxygen/html/group__log__msg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Log message API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Log message API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [log\_msg\_desc](structlog__msg__desc.md) |
| union | [log\_msg\_source](unionlog__msg__source.md) |
| struct | [log\_msg\_hdr](structlog__msg__hdr.md) |
| struct | [log\_msg](structlog__msg.md) |
| struct | [log\_msg\_generic\_hdr](structlog__msg__generic__hdr.md) |
| union | [log\_msg\_generic](unionlog__msg__generic.md) |

| Macros | |
| --- | --- |
| #define | [LOG\_MSG\_GENERIC\_HDR](#gaba2b53ea6e29c20d452322d664ed4f18) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK](#ga92c57ed7438185ade7d2aaf6fc13f218)(...) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0](#ga930a906d0564298231f04d0290d7079f)(fmt) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1](#gaddf1c7085315ef0154d0d4d9fe04a742)(fmt, arg) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2](#gaf416ebb73b5b66df011024b9284cec12)(fmt, arg0, arg1) |
| #define | [LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK](#gafe4a2adbb6cf19bf4df58311ad6beac8)(...) |
|  | brief Determine if string arguments types allow to use simplified message creation mode. |
| #define | [LOG\_MSG\_SIMPLE\_CHECK](#ga90e5d1e83ce78f638f35add7b98bf7ae)(...) |
|  | Check if message can be handled using simplified method. |
| #define | [LOG\_MSG\_SIMPLE\_FUNC](#gaf39825bcdef376cf77e9844aa87b426c)(\_source, \_level, ...) |
|  | Call specific function to create a log message. |

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_msg\_get\_total\_wlen](#gac26779a741754cfb0f79f1cd78ece856) (const struct [log\_msg\_desc](structlog__msg__desc.md) desc) |
|  | Get total length (in 32 bit words) of a log message. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_msg\_generic\_get\_wlen](#gaaf2e1b6af3957a1d23898ec8ad94e7f7) (const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \*item) |
|  | Get length of the log item. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_msg\_get\_domain](#gaa4f92e19f94212a8a580d19b587fcbb1) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message domain ID. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_msg\_get\_level](#ga952503e8252dc60f5920e473b76cfb47) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message level. |
| static const void \* | [log\_msg\_get\_source](#ga2e65669fe7fb9cbb357bdcab0eda02df) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get message source data. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [log\_msg\_get\_source\_id](#ga5ca82bb442eededbfd3e06196e7ea412) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get log message source ID. |
| static [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) | [log\_msg\_get\_timestamp](#gae0541cad3c66df189a5c6e454459b3b0) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get timestamp. |
| static void \* | [log\_msg\_get\_tid](#ga9750b8652b310e5292f1e510e5bf0ef5) (struct [log\_msg](structlog__msg.md) \*msg) |
|  | Get Thread ID. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [log\_msg\_get\_data](#gaed59653e68c2076a3add6abb52471a9e) (struct [log\_msg](structlog__msg.md) \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get data buffer. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [log\_msg\_get\_package](#gad433f993ebc12644f9e3476c3d542c58) (struct [log\_msg](structlog__msg.md) \*msg, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*len) |
|  | Get string package. |

## Detailed Description

Log message API.

## Macro Definition Documentation

## [◆ ](#gaba2b53ea6e29c20d452322d664ed4f18)LOG\_MSG\_GENERIC\_HDR

| #define LOG\_MSG\_GENERIC\_HDR |
| --- |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

[MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828);\

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type:1

[MPSC\_PBUF\_HDR](group__mpsc__packet.md#ga643932633f40ecdcfb9120662221d828)

#define MPSC\_PBUF\_HDR

Header that must be added to the first word in each packet.

**Definition** mpsc\_packet.h:32

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#ga92c57ed7438185ade7d2aaf6fc13f218)LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK

| #define LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(\_LOG\_MSG\_SIMPLE\_XXXX, [NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_)), (1), (0))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:647

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

## [◆ ](#gafe4a2adbb6cf19bf4df58311ad6beac8)LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK

| #define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_, [NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_))(\_\_VA\_ARGS\_\_)

brief Determine if string arguments types allow to use simplified message creation mode.

Parameters
:   | ... | String with arguments. |
    | --- | --- |

## [◆ ](#ga930a906d0564298231f04d0290d7079f)LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0

| #define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_0 | ( |  | *fmt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

1

## [◆ ](#gaddf1c7085315ef0154d0d4d9fe04a742)LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1

| #define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_1 | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | *arg* ) |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

Z\_CBPRINTF\_IS\_WORD\_NUM(arg)

## [◆ ](#gaf416ebb73b5b66df011024b9284cec12)LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2

| #define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK\_2 | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | *arg0*, |
|  |  |  | *arg1* ) |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

Z\_CBPRINTF\_IS\_WORD\_NUM(arg0) && Z\_CBPRINTF\_IS\_WORD\_NUM(arg1)

## [◆ ](#ga90e5d1e83ce78f638f35add7b98bf7ae)LOG\_MSG\_SIMPLE\_CHECK

| #define LOG\_MSG\_SIMPLE\_CHECK | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_64BIT, (0), (\

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK](#ga92c57ed7438185ade7d2aaf6fc13f218)(\_\_VA\_ARGS\_\_), ( \

[LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK](#gafe4a2adbb6cf19bf4df58311ad6beac8)(\_\_VA\_ARGS\_\_)), (0))))

[LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK](#ga92c57ed7438185ade7d2aaf6fc13f218)

#define LOG\_MSG\_SIMPLE\_ARG\_CNT\_CHECK(...)

**Definition** log\_msg.h:237

[LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK](#gafe4a2adbb6cf19bf4df58311ad6beac8)

#define LOG\_MSG\_SIMPLE\_ARG\_TYPE\_CHECK(...)

brief Determine if string arguments types allow to use simplified message creation mode.

**Definition** log\_msg.h:250

Check if message can be handled using simplified method.

Following conditions must be met:

- 32 bit platform
- Number of arguments from 0 to 2
- Type of an argument must be a numeric value that fits in 32 bit word.

Parameters
:   | ... | String with arguments. |
    | --- | --- |

Return values
:   | 1 | if message qualifies. |
    | --- | --- |
    | 0 | if message does not qualify. |

## [◆ ](#gaf39825bcdef376cf77e9844aa87b426c)LOG\_MSG\_SIMPLE\_FUNC

| #define LOG\_MSG\_SIMPLE\_FUNC | ( |  | *\_source*, |
| --- | --- | --- | --- |
|  |  |  | *\_level*, |
|  |  |  | ... ) |

`#include <[log_msg.h](log__msg_8h.md)>`

**Value:**

Z\_LOG\_MSG\_SIMPLE\_FUNC2([NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_\_VA\_ARGS\_\_), \_source, \_level, \_\_VA\_ARGS\_\_)

Call specific function to create a log message.

Macro picks matching function (based on number of arguments) and calls it. String arguments are casted to [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f).

Parameters
:   | \_source | Source. |
    | --- | --- |
    | \_level | Severity level. |
    | ... | String with arguments. |

## Function Documentation

## [◆ ](#gaaf2e1b6af3957a1d23898ec8ad94e7f7)log\_msg\_generic\_get\_wlen()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_generic\_get\_wlen | ( | const union [mpsc\_pbuf\_generic](unionmpsc__pbuf__generic.md) \* | *item* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get length of the log item.

Parameters
:   | item | Item. |
    | --- | --- |

Returns
:   Length in 32 bit words.

## [◆ ](#gaed59653e68c2076a3add6abb52471a9e)log\_msg\_get\_data()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* log\_msg\_get\_data | ( | struct [log\_msg](structlog__msg.md) \* | *msg*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get data buffer.

Parameters
:   | msg | log message. |
    | --- | --- |
    | len | location where data length is written. |

Returns
:   pointer to the data buffer.

## [◆ ](#gaa4f92e19f94212a8a580d19b587fcbb1)log\_msg\_get\_domain()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_msg\_get\_domain | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get log message domain ID.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Domain ID

## [◆ ](#ga952503e8252dc60f5920e473b76cfb47)log\_msg\_get\_level()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_msg\_get\_level | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get log message level.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Log level.

## [◆ ](#gad433f993ebc12644f9e3476c3d542c58)log\_msg\_get\_package()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* log\_msg\_get\_package | ( | struct [log\_msg](structlog__msg.md) \* | *msg*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get string package.

Parameters
:   | msg | log message. |
    | --- | --- |
    | len | location where string package length is written. |

Returns
:   pointer to the package.

## [◆ ](#ga2e65669fe7fb9cbb357bdcab0eda02df)log\_msg\_get\_source()

| | const void \* log\_msg\_get\_source | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get message source data.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Pointer to the source data.

## [◆ ](#ga5ca82bb442eededbfd3e06196e7ea412)log\_msg\_get\_source\_id()

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) log\_msg\_get\_source\_id | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get log message source ID.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Source ID, or -1 if not available.

## [◆ ](#ga9750b8652b310e5292f1e510e5bf0ef5)log\_msg\_get\_tid()

| | void \* log\_msg\_get\_tid | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get Thread ID.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Thread ID.

## [◆ ](#gae0541cad3c66df189a5c6e454459b3b0)log\_msg\_get\_timestamp()

| | [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8) log\_msg\_get\_timestamp | ( | struct [log\_msg](structlog__msg.md) \* | *msg* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get timestamp.

Parameters
:   | msg | Log message. |
    | --- | --- |

Returns
:   Timestamp.

## [◆ ](#gac26779a741754cfb0f79f1cd78ece856)log\_msg\_get\_total\_wlen()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_msg\_get\_total\_wlen | ( | const struct [log\_msg\_desc](structlog__msg__desc.md) | *desc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_msg.h](log__msg_8h.md)>`

Get total length (in 32 bit words) of a log message.

Parameters
:   | desc | Log message descriptor. |
    | --- | --- |

Returns
:   Length.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
