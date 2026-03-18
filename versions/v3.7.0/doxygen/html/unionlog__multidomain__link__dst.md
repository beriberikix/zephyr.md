---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/unionlog__multidomain__link__dst.html
original_path: doxygen/html/unionlog__multidomain__link__dst.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_multidomain\_link\_dst Union Reference

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md) » [Logger multidomain backend helpers](group__log__backend__multidomain.md)

Union for holding data returned by associated remote backend.
[More...](#details)

`#include <[log_multidomain_helper.h](log__multidomain__helper_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [count](#a0935ff85447ef4fa199946783ba39add) |
| struct { |  |
| char \*   [dst](#aef0b581f40c3fcf86215ab12a32f456b) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*   [len](#ab03fb4ded05aae2300455d1270bd7d1e) |  |
| } | [name](#af4ed3dcb76571ed5bdb94ba57822332c) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [level](#ac92526ad2eafde97e6a18b8432594e15) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [runtime\_level](#acf6e86f74700d62d1b00f7feed7648a4) |  |
| } | [levels](#a2fc43ada44365dfdc44914b4f77cb9e3) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [level](#ac92526ad2eafde97e6a18b8432594e15) |  |
| } | [set\_runtime\_level](#ad2c1c1e1c456e6e9643f884b73a6bbb1) |

## Detailed Description

Union for holding data returned by associated remote backend.

## Field Documentation

## [◆ ](#a0935ff85447ef4fa199946783ba39add)count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) log\_multidomain\_link\_dst::count |
| --- |

## [◆ ](#aef0b581f40c3fcf86215ab12a32f456b)dst

| char\* log\_multidomain\_link\_dst::dst |
| --- |

## [◆ ](#ab03fb4ded05aae2300455d1270bd7d1e)len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)\* log\_multidomain\_link\_dst::len |
| --- |

## [◆ ](#ac92526ad2eafde97e6a18b8432594e15)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_link\_dst::level |
| --- |

## [◆ ](#a2fc43ada44365dfdc44914b4f77cb9e3)[struct]

| struct { ... } log\_multidomain\_link\_dst::levels |
| --- |

## [◆ ](#af4ed3dcb76571ed5bdb94ba57822332c)[struct]

| struct { ... } log\_multidomain\_link\_dst::name |
| --- |

## [◆ ](#acf6e86f74700d62d1b00f7feed7648a4)runtime\_level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) log\_multidomain\_link\_dst::runtime\_level |
| --- |

## [◆ ](#ad2c1c1e1c456e6e9643f884b73a6bbb1)[struct]

| struct { ... } log\_multidomain\_link\_dst::set\_runtime\_level |
| --- |

---

The documentation for this union was generated from the following file:

- zephyr/logging/[log\_multidomain\_helper.h](log__multidomain__helper_8h_source.md)

- [log\_multidomain\_link\_dst](unionlog__multidomain__link__dst.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
