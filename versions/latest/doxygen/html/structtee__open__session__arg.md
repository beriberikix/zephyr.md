---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structtee__open__session__arg.html
original_path: doxygen/html/structtee__open__session__arg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee\_open\_session\_arg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [TEE Interface](group__tee__interface.md)

- Open session argument

[More...](#details)

`#include <[tee.h](tee_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [uuid](#a9f4c56fe45f5ad9313bdc1f457d31f9a) [16] |
|  | [in] UUID of the Trusted Application |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clnt\_uuid](#aff38cc02e83936e23965ee2e4e44ff26) [16] |
|  | [in] UUID of client |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [clnt\_login](#a226c617eae1b959025a0232eed48aa41) |
|  | login class of client, TEE\_IOCTL\_LOGIN\_\* above |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cancel\_id](#adf8bfaaf5059de617a7139b5f06a0ac6) |
|  | [in] cancellation id, a unique value to identify this request |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [session](#a5e28bb77990ce6d050a57daa419760e1) |
|  | [out] session id |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ret](#a3be6d6ea6aeff1a8f27051fe30f21347) |
|  | [out] return value |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ret\_origin](#a73a7e82fb0b589eed327ab8f4217e6fc) |
|  | [out] origin of the return value |

## Detailed Description

- Open session argument

## Field Documentation

## [◆ ](#adf8bfaaf5059de617a7139b5f06a0ac6)cancel\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_open\_session\_arg::cancel\_id |
| --- |

[in] cancellation id, a unique value to identify this request

## [◆ ](#a226c617eae1b959025a0232eed48aa41)clnt\_login

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_open\_session\_arg::clnt\_login |
| --- |

login class of client, TEE\_IOCTL\_LOGIN\_\* above

## [◆ ](#aff38cc02e83936e23965ee2e4e44ff26)clnt\_uuid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tee\_open\_session\_arg::clnt\_uuid[16] |
| --- |

[in] UUID of client

## [◆ ](#a3be6d6ea6aeff1a8f27051fe30f21347)ret

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_open\_session\_arg::ret |
| --- |

[out] return value

## [◆ ](#a73a7e82fb0b589eed327ab8f4217e6fc)ret\_origin

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_open\_session\_arg::ret\_origin |
| --- |

[out] origin of the return value

## [◆ ](#a5e28bb77990ce6d050a57daa419760e1)session

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_open\_session\_arg::session |
| --- |

[out] session id

## [◆ ](#a9f4c56fe45f5ad9313bdc1f457d31f9a)uuid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tee\_open\_session\_arg::uuid[16] |
| --- |

[in] UUID of the Trusted Application

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[tee.h](tee_8h_source.md)

- [tee\_open\_session\_arg](structtee__open__session__arg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
