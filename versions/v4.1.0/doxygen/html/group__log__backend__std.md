---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__log__backend__std.html
original_path: doxygen/html/group__log__backend__std.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Logger backend standard interface

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Logger backend interface for forwarding to standard backend.
[More...](#details)

| Functions | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_backend\_std\_get\_flags](#ga187212f5bcf701e57f3859338afa04ac) (void) |
| static void | [log\_backend\_std\_panic](#gae64f537029b579ae947a8ba4c5b2634d) (const struct [log\_output](structlog__output.md) \*const output) |
|  | Put a standard logger backend into panic mode. |
| static void | [log\_backend\_std\_dropped](#gac79c5ea2d5f7a952f55ba21621120805) (const struct [log\_output](structlog__output.md) \*const output, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Report dropped messages to a standard logger backend. |

## Detailed Description

Logger backend interface for forwarding to standard backend.

## Function Documentation

## [◆ ](#gac79c5ea2d5f7a952f55ba21621120805)log\_backend\_std\_dropped()

| | void log\_backend\_std\_dropped | ( | const struct [log\_output](structlog__output.md) \*const | *output*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cnt* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend_std.h](log__backend__std_8h.md)>`

Report dropped messages to a standard logger backend.

Parameters
:   | output | Log output instance. |
    | --- | --- |
    | cnt | Number of dropped messages. |

## [◆ ](#ga187212f5bcf701e57f3859338afa04ac)log\_backend\_std\_get\_flags()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_backend\_std\_get\_flags | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend_std.h](log__backend__std_8h.md)>`

## [◆ ](#gae64f537029b579ae947a8ba4c5b2634d)log\_backend\_std\_panic()

| | void log\_backend\_std\_panic | ( | const struct [log\_output](structlog__output.md) \*const | *output* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[log_backend_std.h](log__backend__std_8h.md)>`

Put a standard logger backend into panic mode.

Parameters
:   | output | Log output instance. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
