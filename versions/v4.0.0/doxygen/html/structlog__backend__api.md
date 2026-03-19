---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structlog__backend__api.html
original_path: doxygen/html/structlog__backend__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_api Struct Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md)

Logger backend API.
[More...](#details)

`#include <[log_backend.h](log__backend_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [process](#a5d2d50961d28d0e2d2fdaacf79e5e9c8) )(const struct [log\_backend](structlog__backend.md) \*const backend, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
| void(\* | [dropped](#a849b25667c299c4a7a97f598a1b2fbd7) )(const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
| void(\* | [panic](#a04bdb8030ad4e70000d8572a6b7e07b1) )(const struct [log\_backend](structlog__backend.md) \*const backend) |
| void(\* | [init](#addc850f99813854df8083a5ee93a36c8) )(const struct [log\_backend](structlog__backend.md) \*const backend) |
| int(\* | [is\_ready](#ac0b3ea89a08df5d4d81b75075c876a18) )(const struct [log\_backend](structlog__backend.md) \*const backend) |
| int(\* | [format\_set](#ae23c17899721f8254a9f50bedd667226) )(const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
| void(\* | [notify](#a656e284fd28781a582072bf39ab2ea40) )(const struct [log\_backend](structlog__backend.md) \*const backend, enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) event, union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg) |

## Detailed Description

Logger backend API.

## Field Documentation

## [◆ ](#a849b25667c299c4a7a97f598a1b2fbd7)dropped

| void(\* log\_backend\_api::dropped) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
| --- |

## [◆ ](#ae23c17899721f8254a9f50bedd667226)format\_set

| int(\* log\_backend\_api::format\_set) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
| --- |

## [◆ ](#addc850f99813854df8083a5ee93a36c8)init

| void(\* log\_backend\_api::init) (const struct [log\_backend](structlog__backend.md) \*const backend) |
| --- |

## [◆ ](#ac0b3ea89a08df5d4d81b75075c876a18)is\_ready

| int(\* log\_backend\_api::is\_ready) (const struct [log\_backend](structlog__backend.md) \*const backend) |
| --- |

## [◆ ](#a656e284fd28781a582072bf39ab2ea40)notify

| void(\* log\_backend\_api::notify) (const struct [log\_backend](structlog__backend.md) \*const backend, enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) event, union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg) |
| --- |

## [◆ ](#a04bdb8030ad4e70000d8572a6b7e07b1)panic

| void(\* log\_backend\_api::panic) (const struct [log\_backend](structlog__backend.md) \*const backend) |
| --- |

## [◆ ](#a5d2d50961d28d0e2d2fdaacf79e5e9c8)process

| void(\* log\_backend\_api::process) (const struct [log\_backend](structlog__backend.md) \*const backend, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/logging/[log\_backend.h](log__backend_8h_source.md)

- [log\_backend\_api](structlog__backend__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
