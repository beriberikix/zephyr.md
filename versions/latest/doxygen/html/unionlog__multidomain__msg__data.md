---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/unionlog__multidomain__msg__data.html
original_path: doxygen/html/unionlog__multidomain__msg__data.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_msg\_data Union Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Union with all message types.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md) | [log\_msg](#a80c35854603c64c5ee60e5a0e30164b6) |
| struct [log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md) | [domain\_cnt](#a8668d1a976506c3b07a700ac690375e8) |
| struct [log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md) | [source\_cnt](#a35da6c6681a216548d39701faa088bbd) |
| struct [log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md) | [domain\_name](#ab1481ec75f3951cb961cd9afbc557ba4) |
| struct [log\_multidomain\_source\_name](structlog__multidomain__source__name.md) | [source\_name](#aa6e542307344fab6b680c61e2706fdcd) |
| struct [log\_multidomain\_levels](structlog__multidomain__levels.md) | [levels](#ac34206c874a0fe122262e2fb3a016cf1) |
| struct [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md) | [set\_rt\_level](#ace983b529bdc0871ea5e6a7b3bda928f) |
| struct [log\_multidomain\_dropped](structlog__multidomain__dropped.md) | [dropped](#ab31567cd19b076ba80a284903349837f) |

## Detailed Description

Union with all message types.

## Field Documentation

## [◆ ](#a8668d1a976506c3b07a700ac690375e8)domain\_cnt

| struct [log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md) log\_multidomain\_msg\_data::domain\_cnt |
| --- |

## [◆ ](#ab1481ec75f3951cb961cd9afbc557ba4)domain\_name

| struct [log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md) log\_multidomain\_msg\_data::domain\_name |
| --- |

## [◆ ](#ab31567cd19b076ba80a284903349837f)dropped

| struct [log\_multidomain\_dropped](structlog__multidomain__dropped.md) log\_multidomain\_msg\_data::dropped |
| --- |

## [◆ ](#ac34206c874a0fe122262e2fb3a016cf1)levels

| struct [log\_multidomain\_levels](structlog__multidomain__levels.md) log\_multidomain\_msg\_data::levels |
| --- |

## [◆ ](#a80c35854603c64c5ee60e5a0e30164b6)log\_msg

| struct [log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md) log\_multidomain\_msg\_data::log\_msg |
| --- |

## [◆ ](#ace983b529bdc0871ea5e6a7b3bda928f)set\_rt\_level

| struct [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md) log\_multidomain\_msg\_data::set\_rt\_level |
| --- |

## [◆ ](#a35da6c6681a216548d39701faa088bbd)source\_cnt

| struct [log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md) log\_multidomain\_msg\_data::source\_cnt |
| --- |

## [◆ ](#aa6e542307344fab6b680c61e2706fdcd)source\_name

| struct [log\_multidomain\_source\_name](structlog__multidomain__source__name.md) log\_multidomain\_msg\_data::source\_name |
| --- |

---

The documentation for this union was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
