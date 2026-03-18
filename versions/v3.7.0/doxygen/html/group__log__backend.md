---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__log__backend.html
original_path: doxygen/html/group__log__backend.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Logger backend interface

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Logger backend interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Logger multidomain backend helpers](group__log__backend__multidomain.md) |
|  | Logger multidomain backend helpers. |

| Data Structures | |
| --- | --- |
| union | [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) |
|  | Argument(s) for backend events. [More...](unionlog__backend__evt__arg.md#details) |
| struct | [log\_backend\_api](structlog__backend__api.md) |
|  | Logger backend API. [More...](structlog__backend__api.md#details) |
| struct | [log\_backend\_control\_block](structlog__backend__control__block.md) |
|  | Logger backend control block. [More...](structlog__backend__control__block.md#details) |
| struct | [log\_backend](structlog__backend.md) |
|  | Logger backend structure. [More...](structlog__backend.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_BACKEND\_DEFINE](#ga3a4cc530530d1a8b33dc787842bba119)(\_name, \_api, \_autostart, ...) |
|  | Macro for creating a logger backend instance. |

| Enumerations | |
| --- | --- |
| enum | [log\_backend\_evt](#ga04ebbd4416c907e60e05f0364f3bd2f6) { [LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE](#gga04ebbd4416c907e60e05f0364f3bd2f6a559c37c58daf13a14f7b43440556f3d3) , [LOG\_BACKEND\_EVT\_MAX](#gga04ebbd4416c907e60e05f0364f3bd2f6abbc925931ad8098f3cee651fadd5432a) } |
|  | Backend events. [More...](#ga04ebbd4416c907e60e05f0364f3bd2f6) |

| Functions | |
| --- | --- |
| static void | [log\_backend\_init](#ga017a2b54d367db037cce31b2693af98c) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Initialize or initiate the logging backend. |
| static int | [log\_backend\_is\_ready](#gaf57e7a27a1337815338410db93603e0b) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Poll for backend readiness. |
| static void | [log\_backend\_msg\_process](#ga388b0f33208ef1389640836d0bc23d17) (const struct [log\_backend](structlog__backend.md) \*const backend, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
|  | Process message. |
| static void | [log\_backend\_dropped](#gab300348c43168de1e7eaae8c770b6950) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Notify backend about dropped log messages. |
| static void | [log\_backend\_panic](#gad12906ffa810514c1d43cb26bba5ea4b) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Reconfigure backend to panic mode. |
| static void | [log\_backend\_id\_set](#ga8f263b24140229e5cf8e98b322501bca) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Set backend id. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_backend\_id\_get](#gae3e1d6eaf21dcc1d0961e85271d5e5f3) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Get backend id. |
| static const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_get](#gaf419f3590f42893b7091beed57763c7c) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx) |
|  | Get backend. |
| static int | [log\_backend\_count\_get](#gad055c1dc8e0236b604cb553df3e16a52) (void) |
|  | Get number of backends. |
| static void | [log\_backend\_activate](#ga3ef0b88b4118f7ee04749ace2646c99b) (const struct [log\_backend](structlog__backend.md) \*const backend, void \*ctx) |
|  | Activate backend. |
| static void | [log\_backend\_deactivate](#ga1534fdfabce1e97c829aa79d57739589) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Deactivate backend. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_backend\_is\_active](#ga54dd06d48edf92ef191dab946aead216) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Check state of the backend. |
| static int | [log\_backend\_format\_set](#gac0a4dc476c3b641ab570ca2dd4f2096f) (const struct [log\_backend](structlog__backend.md) \*backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
|  | Set logging format. |
| static void | [log\_backend\_notify](#gae8203fcde52fee405a4b2e973c989ec7) (const struct [log\_backend](structlog__backend.md) \*const backend, enum [log\_backend\_evt](#ga04ebbd4416c907e60e05f0364f3bd2f6) event, union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg) |
|  | Notify a backend of an event. |

## Detailed Description

Logger backend interface.

## Macro Definition Documentation

## [◆ ](#ga3a4cc530530d1a8b33dc787842bba119)LOG\_BACKEND\_DEFINE

| #define LOG\_BACKEND\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_api*, |
|  |  |  | *\_autostart*, |
|  |  |  | ... ) |

`#include <[log_backend.h](log__backend_8h.md)>`

**Value:**

static struct [log\_backend\_control\_block](structlog__backend__control__block.md) [UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(backend\_cb\_, \_name) = \

{ \

COND\_CODE\_0([NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)(\_, ##\_\_VA\_ARGS\_\_), \

(), (.ctx = \_\_VA\_ARGS\_\_,)) \

.id = 0, \

.active = false, \

}; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([log\_backend](structlog__backend.md), \_name) = \

{ \

.api = &\_api, \

.cb = &[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(backend\_cb\_, \_name), \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.autostart = \_autostart \

}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[NUM\_VA\_ARGS\_LESS\_1](group__sys-util.md#ga8a0e9835e0a8f864ffc2359b9c419cc2)

#define NUM\_VA\_ARGS\_LESS\_1(...)

Number of arguments in the variable arguments list minus one.

**Definition** util\_macro.h:631

[log\_backend\_control\_block](structlog__backend__control__block.md)

Logger backend control block.

**Definition** log\_backend.h:82

[log\_backend](structlog__backend.md)

Logger backend structure.

**Definition** log\_backend.h:94

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Macro for creating a logger backend instance.

Parameters
:   | \_name | Name of the backend instance. |
    | --- | --- |
    | \_api | Logger backend API. |
    | \_autostart | If true backend is initialized and activated together with the logger subsystem. |
    | ... | Optional context. |

## Enumeration Type Documentation

## [◆ ](#ga04ebbd4416c907e60e05f0364f3bd2f6)log\_backend\_evt

| enum [log\_backend\_evt](#ga04ebbd4416c907e60e05f0364f3bd2f6) |
| --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Backend events.

| Enumerator | |
| --- | --- |
| LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE | Event when process thread finishes processing.  This event is emitted when the process thread finishes processing pending log messages.  Note  This is not emitted when there are no pending log messages being processed.  Deferred mode only. |
| LOG\_BACKEND\_EVT\_MAX | Maximum number of backend events. |

## Function Documentation

## [◆ ](#ga3ef0b88b4118f7ee04749ace2646c99b)log\_backend\_activate()

| | void log\_backend\_activate | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend*, | | --- | --- | --- | --- | |  |  | void \* | *ctx* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Activate backend.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |
    | [in] | ctx | User context. |

## [◆ ](#gad055c1dc8e0236b604cb553df3e16a52)log\_backend\_count\_get()

| | int log\_backend\_count\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Get number of backends.

Returns
:   Number of backends.

## [◆ ](#ga1534fdfabce1e97c829aa79d57739589)log\_backend\_deactivate()

| | void log\_backend\_deactivate | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Deactivate backend.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

## [◆ ](#gab300348c43168de1e7eaae8c770b6950)log\_backend\_dropped()

| | void log\_backend\_dropped | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cnt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Notify backend about dropped log messages.

Function is optional.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |
    | [in] | cnt | Number of dropped logs since last notification. |

## [◆ ](#gac0a4dc476c3b641ab570ca2dd4f2096f)log\_backend\_format\_set()

| | int log\_backend\_format\_set | ( | const struct [log\_backend](structlog__backend.md) \* | *backend*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *log\_type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Set logging format.

Parameters
:   | backend | Pointer to the backend instance. |
    | --- | --- |
    | log\_type | Log format. |

Return values
:   | -ENOTSUP | If the backend does not support changing format types. |
    | --- | --- |
    | -EINVAL | If the input is invalid. |
    | 0 | for success. |

## [◆ ](#gaf419f3590f42893b7091beed57763c7c)log\_backend\_get()

| | const struct [log\_backend](structlog__backend.md) \* log\_backend\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *idx* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Get backend.

Parameters
:   | [in] | idx | Pointer to the backend instance. |
    | --- | --- | --- |

Returns
:   Pointer to the backend instance.

## [◆ ](#gae3e1d6eaf21dcc1d0961e85271d5e5f3)log\_backend\_id\_get()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_backend\_id\_get | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Get backend id.

Note
:   It is used internally by the logger.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

Returns
:   Id.

## [◆ ](#ga8f263b24140229e5cf8e98b322501bca)log\_backend\_id\_set()

| | void log\_backend\_id\_set | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Set backend id.

Note
:   It is used internally by the logger.

Parameters
:   | backend | Pointer to the backend instance. |
    | --- | --- |
    | id | ID. |

## [◆ ](#ga017a2b54d367db037cce31b2693af98c)log\_backend\_init()

| | void log\_backend\_init | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Initialize or initiate the logging backend.

If backend initialization takes longer time it could block logging thread if backend is autostarted. That is because all backends are initialized in the context of the logging thread. In that case, backend shall provide function for polling for readiness ([log\_backend\_is\_ready](#gaf57e7a27a1337815338410db93603e0b)).

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

## [◆ ](#ga54dd06d48edf92ef191dab946aead216)log\_backend\_is\_active()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_backend\_is\_active | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Check state of the backend.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

Returns
:   True if backend is active, false otherwise.

## [◆ ](#gaf57e7a27a1337815338410db93603e0b)log\_backend\_is\_ready()

| | int log\_backend\_is\_ready | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Poll for backend readiness.

If backend is ready immediately after initialization then backend may not provide this function.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

Return values
:   | 0 | if backend is ready. |
    | --- | --- |
    | -EBUSY | if backend is not yet ready. |

## [◆ ](#ga388b0f33208ef1389640836d0bc23d17)log\_backend\_msg\_process()

| | void log\_backend\_msg\_process | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend*, | | --- | --- | --- | --- | |  |  | union [log\_msg\_generic](unionlog__msg__generic.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Process message.

Function is used in deferred and immediate mode. On return, message content is processed by the backend and memory can be freed.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |
    | [in] | msg | Pointer to message with log entry. |

## [◆ ](#gae8203fcde52fee405a4b2e973c989ec7)log\_backend\_notify()

| | void log\_backend\_notify | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend*, | | --- | --- | --- | --- | |  |  | enum [log\_backend\_evt](#ga04ebbd4416c907e60e05f0364f3bd2f6) | *event*, | |  |  | union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \* | *arg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Notify a backend of an event.

Parameters
:   | backend | Pointer to the backend instance. |
    | --- | --- |
    | event | Event to be notified. |
    | arg | Pointer to the argument(s). |

## [◆ ](#gad12906ffa810514c1d43cb26bba5ea4b)log\_backend\_panic()

| | void log\_backend\_panic | ( | const struct [log\_backend](structlog__backend.md) \*const | *backend* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend.h](log__backend_8h.md)>`

Reconfigure backend to panic mode.

Parameters
:   | [in] | backend | Pointer to the backend instance. |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
