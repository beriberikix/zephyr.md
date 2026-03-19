---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structtee__version__info.html
original_path: doxygen/html/structtee__version__info.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee\_version\_info Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [TEE Interface](group__tee__interface.md)

TEE version.
[More...](#details)

`#include <[tee.h](tee_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [impl\_id](#aaf74a1ff5fb899a0675724669a7d7e36) |
|  | [out] TEE implementation id |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [impl\_caps](#a6cbf12676e5cfc1bdf4221a8188bf055) |
|  | [out] implementation specific capabilities |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gen\_caps](#a56a3c50a69f125428dfbf7a867cb7177) |
|  | Generic capabilities, defined by TEE\_GEN\_CAPS\_\* above. |

## Detailed Description

TEE version.

Identifies the TEE implementation,[impl\_id](#aaf74a1ff5fb899a0675724669a7d7e36) is one of TEE\_IMPL\_ID\_\* above. [impl\_caps](#a6cbf12676e5cfc1bdf4221a8188bf055) is implementation specific, for example TEE\_OPTEE\_CAP\_\* is valid when [impl\_id](#aaf74a1ff5fb899a0675724669a7d7e36) == TEE\_IMPL\_ID\_OPTEE.

## Field Documentation

## [◆ ](#a56a3c50a69f125428dfbf7a867cb7177)gen\_caps

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_version\_info::gen\_caps |
| --- |

Generic capabilities, defined by TEE\_GEN\_CAPS\_\* above.

## [◆ ](#a6cbf12676e5cfc1bdf4221a8188bf055)impl\_caps

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_version\_info::impl\_caps |
| --- |

[out] implementation specific capabilities

## [◆ ](#aaf74a1ff5fb899a0675724669a7d7e36)impl\_id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tee\_version\_info::impl\_id |
| --- |

[out] TEE implementation id

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[tee.h](tee_8h_source.md)

- [tee\_version\_info](structtee__version__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
