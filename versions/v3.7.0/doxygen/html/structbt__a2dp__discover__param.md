---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__a2dp__discover__param.html
original_path: doxygen/html/structbt__a2dp__discover__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_discover\_param Struct Reference

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed) | [cb](#a806fdbaf6d26ad269608afaa21c2035f) |
|  | discover callback |
| struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) | [info](#a14b69e2449f1d2379183690246f55a88) |
|  | The discovered endpoint info that is callbacked by cb. |
| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) \* | [seps\_info](#ab4174f0b43d1804192cd4647d29779d3) |
|  | The max count of remote endpoints that can be got, it save endpoint info internally. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sep\_count](#a382ce8462958f69af19e325491c6f01b) |
|  | The max count of seps (stream endpoint) that can be got in this call route. |

## Field Documentation

## [◆ ](#a806fdbaf6d26ad269608afaa21c2035f)cb

| [bt\_a2dp\_discover\_ep\_cb](a2dp_8h.md#ae054d7f9fa92e45c7d40ec0e1d8730ed) bt\_a2dp\_discover\_param::cb |
| --- |

discover callback

## [◆ ](#a14b69e2449f1d2379183690246f55a88)info

| struct [bt\_a2dp\_ep\_info](structbt__a2dp__ep__info.md) bt\_a2dp\_discover\_param::info |
| --- |

The discovered endpoint info that is callbacked by cb.

## [◆ ](#a382ce8462958f69af19e325491c6f01b)sep\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_discover\_param::sep\_count |
| --- |

The max count of seps (stream endpoint) that can be got in this call route.

## [◆ ](#ab4174f0b43d1804192cd4647d29779d3)seps\_info

| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md)\* bt\_a2dp\_discover\_param::seps\_info |
| --- |

The max count of remote endpoints that can be got, it save endpoint info internally.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_discover\_param](structbt__a2dp__discover__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
