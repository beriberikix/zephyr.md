---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__log__link.html
original_path: doxygen/html/group__log__link.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Log link API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Log link API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [log\_link\_config](structlog__link__config.md) |
| struct | [log\_link\_api](structlog__link__api.md) |
| struct | [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) |
| struct | [log\_link](structlog__link.md) |

| Macros | |
| --- | --- |
| #define | [LOG\_LINK\_DEF](#ga9cf22f4fc8fb8c964396d6502fb20522)(\_name, \_api, \_buf\_wlen, \_ctx) |
|  | Create instance of a log link. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [log\_link\_callback\_t](#gadc72a0abf0311deb3bece478a43e5745)) (const struct [log\_link](structlog__link.md) \*link, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
| typedef void(\* | [log\_link\_dropped\_cb\_t](#ga63dc4a2ad58b754beb259d1748c8ab79)) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dropped) |

| Functions | |
| --- | --- |
| static int | [log\_link\_initiate](#gaff08dcc178a95e3a1e28aeba7ccfe189) (const struct [log\_link](structlog__link.md) \*link, struct [log\_link\_config](structlog__link__config.md) \*config) |
|  | Initiate log link. |
| static int | [log\_link\_activate](#ga5659a791d3336f05bc614b31ba2ce798) (const struct [log\_link](structlog__link.md) \*link) |
|  | Activate log link. |
| static int | [log\_link\_is\_active](#ga855a02a7a3282ca85e0f44004e924bc3) (const struct [log\_link](structlog__link.md) \*link) |
|  | Check if link is activated. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_link\_domains\_count](#gac8f066b2a0509935ef2c3f950928495a) (const struct [log\_link](structlog__link.md) \*link) |
|  | Get number of domains in the link. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [log\_link\_sources\_count](#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get number of sources in the domain. |
| static int | [log\_link\_get\_domain\_name](#ga3aa0a15b8dbb52fb3550826277801835) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
|  | Get domain name. |
| static int | [log\_link\_get\_source\_name](#gad097d791057b9826aa7f2c4077506673) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*length) |
|  | Get source name. |
| static int | [log\_link\_get\_levels](#ga2fc15a236cdf8dd0193df9754394d5db) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*runtime\_level) |
|  | Get level settings of the given source. |
| static int | [log\_link\_set\_runtime\_level](#ga56655f534c45dbc777b1500bafd9a0d7) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Set runtime level of the given source. |

## Detailed Description

Log link API.

## Macro Definition Documentation

## [◆ ](#ga9cf22f4fc8fb8c964396d6502fb20522)LOG\_LINK\_DEF

| #define LOG\_LINK\_DEF | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_api*, |
|  |  |  | *\_buf\_wlen*, |
|  |  |  | *\_ctx* ) |

`#include <[log_link.h](log__link_8h.md)>`

**Value:**

static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_\_aligned(Z\_LOG\_MSG\_ALIGNMENT) \_name##\_buf32[\_buf\_wlen]; \

static const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \_name##\_mpsc\_pbuf\_config = { \

.buf = ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*)\_name##\_buf32, \

.size = \_buf\_wlen, \

.notify\_drop = z\_log\_notify\_drop, \

.get\_wlen = [log\_msg\_generic\_get\_wlen](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7), \

.[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) = [IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_LOG\_MODE\_OVERFLOW) ? \

[MPSC\_PBUF\_MODE\_OVERWRITE](group__MPSC__PBUF__FLAGS.md#ga983332f7aff31ed7b7e62cacf7960497) : 0 \

}; \

COND\_CODE\_0(\_buf\_wlen, (), (static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([log\_msg\_ptr](structlog__msg__ptr.md), \

\_name##\_log\_msg\_ptr);)) \

static [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)([log\_mpsc\_pbuf](structlog__mpsc__pbuf.md), \

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md), \

\_name##\_log\_mpsc\_pbuf); \

static struct [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) \_name##\_ctrl\_blk; \

static const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([log\_link](structlog__link.md), \_name) = \

{ \

.api = &\_api, \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(\_name), \

.ctrl\_blk = &\_name##\_ctrl\_blk, \

.ctx = \_ctx, \

.mpsc\_pbuf = \_buf\_wlen ? &\_name##\_log\_mpsc\_pbuf : NULL, \

.mpsc\_pbuf\_config = \_buf\_wlen ? &\_name##\_mpsc\_pbuf\_config : NULL \

}

[MPSC\_PBUF\_MODE\_OVERWRITE](group__MPSC__PBUF__FLAGS.md#ga983332f7aff31ed7b7e62cacf7960497)

#define MPSC\_PBUF\_MODE\_OVERWRITE

Flag indicating buffer full policy.

**Definition** mpsc\_pbuf.h:59

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

[log\_msg\_generic\_get\_wlen](group__log__msg.md#gaaf2e1b6af3957a1d23898ec8ad94e7f7)

static uint32\_t log\_msg\_generic\_get\_wlen(const union mpsc\_pbuf\_generic \*item)

Get length of the log item.

**Definition** log\_msg.h:741

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:140

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md)

**Definition** log\_link.h:53

[log\_link](structlog__link.md)

**Definition** log\_link.h:62

[log\_mpsc\_pbuf](structlog__mpsc__pbuf.md)

Structure wrapper to be used for memory section.

**Definition** log\_internal.h:24

[log\_msg\_ptr](structlog__msg__ptr.md)

Structure wrapper to be used for memory section.

**Definition** log\_internal.h:29

[mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)

MPSC packet buffer configuration.

**Definition** mpsc\_pbuf.h:131

[mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)

MPSC packet buffer structure.

**Definition** mpsc\_pbuf.h:90

Create instance of a log link.

Link can have dedicated buffer for messages if `_buf_len` is positive. In that case messages will be processed in an order since logging core will attempt to fetch message from all available buffers (default and links) and process the one with the earliest timestamp. If strict ordering is not needed then dedicated buffer may be omitted (`_buf_len` set to 0). That results in better memory utilization but unordered messages passed to backends.

Parameters
:   | \_name | Instance name. |
    | --- | --- |
    | \_api | API list. See [log\_link\_api](structlog__link__api.md "log_link_api"). |
    | \_buf\_wlen | Size (in words) of dedicated buffer for messages from this buffer. If 0 default buffer is used. |
    | \_ctx | Context (void \*) associated with the link. |

## Typedef Documentation

## [◆ ](#gadc72a0abf0311deb3bece478a43e5745)log\_link\_callback\_t

| typedef void(\* log\_link\_callback\_t) (const struct [log\_link](structlog__link.md) \*link, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
| --- |

`#include <[log_link.h](log__link_8h.md)>`

## [◆ ](#ga63dc4a2ad58b754beb259d1748c8ab79)log\_link\_dropped\_cb\_t

| typedef void(\* log\_link\_dropped\_cb\_t) (const struct [log\_link](structlog__link.md) \*link, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dropped) |
| --- |

`#include <[log_link.h](log__link_8h.md)>`

## Function Documentation

## [◆ ](#ga5659a791d3336f05bc614b31ba2ce798)log\_link\_activate()

| | int log\_link\_activate | ( | const struct [log\_link](structlog__link.md) \* | *link* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Activate log link.

Function checks if link is initialized and completes initialization process. When successfully returns, link is ready with domain and sources count fetched and timestamp details updated.

Parameters
:   | link | Log link instance. |
    | --- | --- |

Return values
:   | 0 | When successfully activated. |
    | --- | --- |
    | -EINPROGRESS | Activation in progress. |

## [◆ ](#gac8f066b2a0509935ef2c3f950928495a)log\_link\_domains\_count()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_link\_domains\_count | ( | const struct [log\_link](structlog__link.md) \* | *link* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Get number of domains in the link.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |

Returns
:   Number of domains.

## [◆ ](#ga3aa0a15b8dbb52fb3550826277801835)log\_link\_get\_domain\_name()

| | int log\_link\_get\_domain\_name | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, | |  |  | char \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Get domain name.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |
    | [in] | domain\_id | Relative domain ID. |
    | [out] | buf | Output buffer filled with domain name. If NULL then name length is returned. |
    | [in,out] | length | Buffer size. Name is trimmed if it does not fit in the buffer and field is set to actual name length. |

Returns
:   0 on success or error code.

## [◆ ](#ga2fc15a236cdf8dd0193df9754394d5db)log\_link\_get\_levels()

| | int log\_link\_get\_levels | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *source\_id*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *level*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *runtime\_level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Get level settings of the given source.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |
    | [in] | domain\_id | Relative domain ID. |
    | [in] | source\_id | Source ID. |
    | [out] | level | Location to store requested compile time level. |
    | [out] | runtime\_level | Location to store requested runtime time level. |

Returns
:   0 on success or error code.

## [◆ ](#gad097d791057b9826aa7f2c4077506673)log\_link\_get\_source\_name()

| | int log\_link\_get\_source\_name | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *source\_id*, | |  |  | char \* | *buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Get source name.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |
    | [in] | domain\_id | Relative domain ID. |
    | [in] | source\_id | Source ID. |
    | [out] | buf | Output buffer filled with source name. |
    | [in,out] | length | Buffer size. Name is trimmed if it does not fit in the buffer and field is set to actual name length. |

Returns
:   0 on success or error code.

## [◆ ](#gaff08dcc178a95e3a1e28aeba7ccfe189)log\_link\_initiate()

| | int log\_link\_initiate | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | struct [log\_link\_config](structlog__link__config.md) \* | *config* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Initiate log link.

Function initiates the link. Since initialization procedure may be time consuming, function returns before link is ready to not block logging initialization. [log\_link\_activate](#ga5659a791d3336f05bc614b31ba2ce798) is called to complete link initialization.

Parameters
:   | link | Log link instance. |
    | --- | --- |
    | config | Configuration. |

Returns
:   0 on success or error code.

## [◆ ](#ga855a02a7a3282ca85e0f44004e924bc3)log\_link\_is\_active()

| | int log\_link\_is\_active | ( | const struct [log\_link](structlog__link.md) \* | *link* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Check if link is activated.

Parameters
:   | link | Log link instance. |
    | --- | --- |

Return values
:   | 0 | When successfully activated. |
    | --- | --- |
    | -EINPROGRESS | Activation in progress. |

## [◆ ](#ga56655f534c45dbc777b1500bafd9a0d7)log\_link\_set\_runtime\_level()

| | int log\_link\_set\_runtime\_level | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *source\_id*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Set runtime level of the given source.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |
    | [in] | domain\_id | Relative domain ID. |
    | [in] | source\_id | Source ID. |
    | [out] | level | Requested level. |

Returns
:   0 on success or error code.

## [◆ ](#ga694e4b69f46f1dbd6d1cda9a7d4cf3c4)log\_link\_sources\_count()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_link\_sources\_count | ( | const struct [log\_link](structlog__link.md) \* | *link*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *domain\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_link.h](log__link_8h.md)>`

Get number of sources in the domain.

Parameters
:   | [in] | link | Log link instance. |
    | --- | --- | --- |
    | [in] | domain\_id | Relative domain ID. |

Returns
:   Source count.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
