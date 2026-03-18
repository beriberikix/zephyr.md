---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structjson__obj__descr.html
original_path: doxygen/html/structjson__obj__descr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

json\_obj\_descr Struct Reference

[Utilities](group__utilities.md) » [JSON](group__json.md)

`#include <[json.h](json_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [field\_name](#a2120b7752253ece0beddcaf4c57d3ed8) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [align\_shift](#a475717ac4dd01296c01468450e50f75b): 2 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [field\_name\_len](#a602bf4d8bb5d47c8edb40963ea8ba42f): 7 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [type](#a975e998d3ec36f234f09aa2d0d116c9c): 7 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [offset](#a8c6f3eae5e678b8b8ef1957c46f488f1): 16 |
| union { |  |
| struct { |  |
| const struct [json\_obj\_descr](structjson__obj__descr.md) \*   [sub\_descr](#a4f5e97c654d0c5e21f1efb5a01966e56) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [sub\_descr\_len](#adea0b44d1552305df9dce70074044ba1) |  |
| }   [object](#a5d5df7aab020feb3eeb59a7f6089b066) |
| struct { |  |
| const struct [json\_obj\_descr](structjson__obj__descr.md) \*   [element\_descr](#a0a459bf5ad8a210395fe80c5edd72d93) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [n\_elements](#ace6558c5156a76658d8835fd5e65ee52) |  |
| }   [array](#ac12783b89f5507bef7fa3da2c56d1d61) |
| }; |  |

## Field Documentation

## [◆ ](#ab3fcd26cb6bbca104db63560c310ea8c)[union]

| union { ... } [json\_obj\_descr](structjson__obj__descr.md) |
| --- |

## [◆ ](#a475717ac4dd01296c01468450e50f75b)align\_shift

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) json\_obj\_descr::align\_shift |
| --- |

## [◆ ](#ac12783b89f5507bef7fa3da2c56d1d61)[struct]

| struct { ... } json\_obj\_descr::array |
| --- |

## [◆ ](#a0a459bf5ad8a210395fe80c5edd72d93)element\_descr

| const struct [json\_obj\_descr](structjson__obj__descr.md)\* json\_obj\_descr::element\_descr |
| --- |

## [◆ ](#a2120b7752253ece0beddcaf4c57d3ed8)field\_name

| const char\* json\_obj\_descr::field\_name |
| --- |

## [◆ ](#a602bf4d8bb5d47c8edb40963ea8ba42f)field\_name\_len

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) json\_obj\_descr::field\_name\_len |
| --- |

## [◆ ](#ace6558c5156a76658d8835fd5e65ee52)n\_elements

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) json\_obj\_descr::n\_elements |
| --- |

## [◆ ](#a5d5df7aab020feb3eeb59a7f6089b066)[struct]

| struct { ... } json\_obj\_descr::object |
| --- |

## [◆ ](#a8c6f3eae5e678b8b8ef1957c46f488f1)offset

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) json\_obj\_descr::offset |
| --- |

## [◆ ](#a4f5e97c654d0c5e21f1efb5a01966e56)sub\_descr

| const struct [json\_obj\_descr](structjson__obj__descr.md)\* json\_obj\_descr::sub\_descr |
| --- |

## [◆ ](#adea0b44d1552305df9dce70074044ba1)sub\_descr\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) json\_obj\_descr::sub\_descr\_len |
| --- |

## [◆ ](#a975e998d3ec36f234f09aa2d0d116c9c)type

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) json\_obj\_descr::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/data/[json.h](json_8h_source.md)

- [json\_obj\_descr](structjson__obj__descr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
