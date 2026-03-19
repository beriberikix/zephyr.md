---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__multidomain__helper_8h.html
original_path: doxygen/html/log__multidomain__helper_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_helper.h File Reference

[Go to the source code of this file.](log__multidomain__helper_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_multidomain\_log\_msg](structlog__multidomain__log__msg.md) |
|  | Content of the logging message. [More...](structlog__multidomain__log__msg.md#details) |
| struct | [log\_multidomain\_domain\_cnt](structlog__multidomain__domain__cnt.md) |
|  | Content of the domain count message. [More...](structlog__multidomain__domain__cnt.md#details) |
| struct | [log\_multidomain\_source\_cnt](structlog__multidomain__source__cnt.md) |
|  | Content of the source count message. [More...](structlog__multidomain__source__cnt.md#details) |
| struct | [log\_multidomain\_domain\_name](structlog__multidomain__domain__name.md) |
|  | Content of the domain name message. [More...](structlog__multidomain__domain__name.md#details) |
| struct | [log\_multidomain\_source\_name](structlog__multidomain__source__name.md) |
|  | Content of the source name message. [More...](structlog__multidomain__source__name.md#details) |
| struct | [log\_multidomain\_levels](structlog__multidomain__levels.md) |
|  | Content of the message for getting logging levels. [More...](structlog__multidomain__levels.md#details) |
| struct | [log\_multidomain\_set\_runtime\_level](structlog__multidomain__set__runtime__level.md) |
|  | Content of the message for setting logging level. [More...](structlog__multidomain__set__runtime__level.md#details) |
| struct | [log\_multidomain\_dropped](structlog__multidomain__dropped.md) |
|  | Content of the message for getting amount of dropped messages. [More...](structlog__multidomain__dropped.md#details) |
| union | [log\_multidomain\_msg\_data](unionlog__multidomain__msg__data.md) |
|  | Union with all message types. [More...](unionlog__multidomain__msg__data.md#details) |
| struct | [log\_multidomain\_msg](structlog__multidomain__msg.md) |
|  | Message. [More...](structlog__multidomain__msg.md#details) |
| struct | [log\_multidomain\_link\_transport\_api](structlog__multidomain__link__transport__api.md) |
|  | Structure with link transport API. [More...](structlog__multidomain__link__transport__api.md#details) |
| union | [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md) |
|  | Union for holding data returned by associated remote backend. [More...](unionlog__multidomain__link__dst.md#details) |
| struct | [log\_multidomain\_link](structlog__multidomain__link.md) |
|  | Remote link structure. [More...](structlog__multidomain__link.md#details) |
| struct | [log\_multidomain\_backend\_transport\_api](structlog__multidomain__backend__transport__api.md) |
|  | Backend transport API. [More...](structlog__multidomain__backend__transport__api.md#details) |
| struct | [log\_multidomain\_backend](structlog__multidomain__backend.md) |
|  | Remote backend structure. [More...](structlog__multidomain__backend.md#details) |

| Functions | |
| --- | --- |
| void | [log\_multidomain\_link\_on\_recv\_cb](group__log__backend__multidomain.md#ga887c2f6f7d6a6d65aef2fe63aa4b6d99) (struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function to be called when data is received from remote. |
| void | [log\_multidomain\_link\_on\_error](group__log__backend__multidomain.md#gafb21f03e5f562358babd50ac8d7c1b48) (struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, int err) |
|  | Function called on error reported by transport layer. |
| void | [log\_multidomain\_link\_on\_started](group__log__backend__multidomain.md#gad045bde79b043dfc38e807f90b9ab5f6) (struct [log\_multidomain\_link](structlog__multidomain__link.md) \*link, int err) |
|  | Function called when connection with remote is established. |
| void | [log\_multidomain\_backend\_on\_recv\_cb](group__log__backend__multidomain.md#ga2aabae271c90e5475356d5aaad5bd2cf) (struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Function to be called when data is received from remote. |
| void | [log\_multidomain\_backend\_on\_error](group__log__backend__multidomain.md#ga29a29c0e7a373f055fcbbdbed6ba24e5) (struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, int err) |
|  | Function called on error reported by transport layer. |
| void | [log\_multidomain\_backend\_on\_started](group__log__backend__multidomain.md#gada2e91cb204ba8e09a6f3a0e69b40d4d) (struct [log\_multidomain\_backend](structlog__multidomain__backend.md) \*backend, int err) |
|  | Function called when connection with remote is established. |

| Variables | |
| --- | --- |
| struct [log\_link\_api](structlog__link__api.md) | [log\_multidomain\_link\_api](group__log__backend__multidomain.md#ga64e0fb3d32e2aa1e3353ffe28c05befa) |
|  | Remote link API. |
| const struct [log\_backend\_api](structlog__backend__api.md) | [log\_multidomain\_backend\_api](group__log__backend__multidomain.md#ga8e4e6908b6533b11d8cc351f67a5f976) |
|  | Remote backend API. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_multidomain\_helper.h](log__multidomain__helper_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
