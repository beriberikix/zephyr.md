---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__a2dp__stream.html
original_path: doxygen/html/structbt__a2dp__stream.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_stream Struct Reference

A2DP Stream.
[More...](#details)

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \* | [local\_ep](#aa490bb24525c50cf8c1675a01223420c) |
|  | local endpoint |
| struct [bt\_a2dp\_ep](structbt__a2dp__ep.md) \* | [remote\_ep](#a4ea9de245b573b7d0c495aacd7534099) |
|  | remote endpoint |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [remote\_ep\_id](#a3361f68c31075014c2c3cf62494ff3ec) |
|  | remote endpoint's Stream End Point ID |
| struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md) \* | [ops](#aa51509d9f0c50118177345988ddb8fa5) |
|  | Audio stream operations. |
| struct bt\_a2dp \* | [a2dp](#ab62b3f17a198600e683c26cf3d3e87e2) |
|  | the a2dp connection |
| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) | [codec\_config](#aff775fe292618da4de467aa96cbf79b0) |
|  | the stream current configuration |

## Detailed Description

A2DP Stream.

## Field Documentation

## [◆ ](#ab62b3f17a198600e683c26cf3d3e87e2)a2dp

| struct bt\_a2dp\* bt\_a2dp\_stream::a2dp |
| --- |

the a2dp connection

## [◆ ](#aff775fe292618da4de467aa96cbf79b0)codec\_config

| struct [bt\_a2dp\_codec\_ie](structbt__a2dp__codec__ie.md) bt\_a2dp\_stream::codec\_config |
| --- |

the stream current configuration

## [◆ ](#aa490bb24525c50cf8c1675a01223420c)local\_ep

| struct [bt\_a2dp\_ep](structbt__a2dp__ep.md)\* bt\_a2dp\_stream::local\_ep |
| --- |

local endpoint

## [◆ ](#aa51509d9f0c50118177345988ddb8fa5)ops

| struct [bt\_a2dp\_stream\_ops](structbt__a2dp__stream__ops.md)\* bt\_a2dp\_stream::ops |
| --- |

Audio stream operations.

## [◆ ](#a4ea9de245b573b7d0c495aacd7534099)remote\_ep

| struct [bt\_a2dp\_ep](structbt__a2dp__ep.md)\* bt\_a2dp\_stream::remote\_ep |
| --- |

remote endpoint

## [◆ ](#a3361f68c31075014c2c3cf62494ff3ec)remote\_ep\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_stream::remote\_ep\_id |
| --- |

remote endpoint's Stream End Point ID

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_stream](structbt__a2dp__stream.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
