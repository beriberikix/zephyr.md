---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlog__link.html
original_path: doxygen/html/structlog__link.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_link Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Log link API](group__log__link.md)

`#include <[log_link.h](log__link_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [log\_link\_api](structlog__link__api.md) \* | [api](#a1df7a4c08d3488a68b7058a018c92e46) |
| const char \* | [name](#a46a2eafdb546ec8a5f7b5fc9102121c7) |
| struct [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md) \* | [ctrl\_blk](#aaa4f473c397f6b90d73b395a62cfbc7e) |
| void \* | [ctx](#a1a1adfb2d621ba37d2dd8c814fce659e) |
| struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md) \* | [mpsc\_pbuf](#ae06e6147fc50e18a277b3610016c10a8) |
| const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md) \* | [mpsc\_pbuf\_config](#a312ff38285a989e56d6f59b9bc1429cf) |

## Field Documentation

## [◆ ](#a1df7a4c08d3488a68b7058a018c92e46)api

| const struct [log\_link\_api](structlog__link__api.md)\* log\_link::api |
| --- |

## [◆ ](#aaa4f473c397f6b90d73b395a62cfbc7e)ctrl\_blk

| struct [log\_link\_ctrl\_blk](structlog__link__ctrl__blk.md)\* log\_link::ctrl\_blk |
| --- |

## [◆ ](#a1a1adfb2d621ba37d2dd8c814fce659e)ctx

| void\* log\_link::ctx |
| --- |

## [◆ ](#ae06e6147fc50e18a277b3610016c10a8)mpsc\_pbuf

| struct [mpsc\_pbuf\_buffer](structmpsc__pbuf__buffer.md)\* log\_link::mpsc\_pbuf |
| --- |

## [◆ ](#a312ff38285a989e56d6f59b9bc1429cf)mpsc\_pbuf\_config

| const struct [mpsc\_pbuf\_buffer\_config](structmpsc__pbuf__buffer__config.md)\* log\_link::mpsc\_pbuf\_config |
| --- |

## [◆ ](#a46a2eafdb546ec8a5f7b5fc9102121c7)name

| const char\* log\_link::name |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_link.h](log__link_8h_source.md)

- [log\_link](structlog__link.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
