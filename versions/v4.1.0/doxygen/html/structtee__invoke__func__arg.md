---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structtee__invoke__func__arg.html
original_path: doxygen/html/structtee__invoke__func__arg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee\_invoke\_func\_arg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [TEE Interface](group__tee__interface.md)

Invokes a function in a Trusted Application.
[More...](#details)

`#include <[tee.h](tee_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [func](#a17aa094ca0a6c6d9a72d2fae9c0c66ef) |
|  | [in] Trusted Application function, specific to the TA |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [session](#af110327354b1ca48dedf22855c3a7afc) |
|  | [in] session id |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cancel\_id](#a457daf2221f9520aecb42667acc4ccd1) |
|  | [in] cancellation id, a unique value to identify this request |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ret](#af63bd284a7397d4086ac17f83d6b1e93) |
|  | [out] return value |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ret\_origin](#ae806e940e463321b3de31bad2e05bf60) |
|  | [out] origin of the return value |

## Detailed Description

Invokes a function in a Trusted Application.

## Field Documentation

## [◆ ](#a457daf2221f9520aecb42667acc4ccd1)cancel\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_invoke\_func\_arg::cancel\_id |
| --- |

[in] cancellation id, a unique value to identify this request

## [◆ ](#a17aa094ca0a6c6d9a72d2fae9c0c66ef)func

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_invoke\_func\_arg::func |
| --- |

[in] Trusted Application function, specific to the TA

## [◆ ](#af63bd284a7397d4086ac17f83d6b1e93)ret

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_invoke\_func\_arg::ret |
| --- |

[out] return value

## [◆ ](#ae806e940e463321b3de31bad2e05bf60)ret\_origin

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_invoke\_func\_arg::ret\_origin |
| --- |

[out] origin of the return value

## [◆ ](#af110327354b1ca48dedf22855c3a7afc)session

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_invoke\_func\_arg::session |
| --- |

[in] session id

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[tee.h](tee_8h_source.md)

- [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
