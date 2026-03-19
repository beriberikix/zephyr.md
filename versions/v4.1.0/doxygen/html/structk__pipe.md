---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__pipe.html
original_path: doxygen/html/structk__pipe.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_pipe Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Pipe APIs](group__pipe__apis.md)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [waiting](#ac9162db42883d2c14f63cf74ff3c1179) |
| struct [ring\_buf](structring__buf.md) | [buf](#a62556b1fbb907dcb8fbbe29c597d8473) |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#aa2a367a9c8f0be89bcdf1bf6d3b0b875) |
| \_wait\_q\_t | [data](#a8af11082e53b56670f0ce11e581766ff) |
| \_wait\_q\_t | [space](#aa1428192b88b97e0cb5ec83894770f47) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a2ed95fbe24ea20c4f292a66def1d4dde) |

## Field Documentation

## [◆ ](#a62556b1fbb907dcb8fbbe29c597d8473)buf

| struct [ring\_buf](structring__buf.md) k\_pipe::buf |
| --- |

## [◆ ](#a8af11082e53b56670f0ce11e581766ff)data

| \_wait\_q\_t k\_pipe::data |
| --- |

## [◆ ](#a2ed95fbe24ea20c4f292a66def1d4dde)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) k\_pipe::flags |
| --- |

## [◆ ](#aa2a367a9c8f0be89bcdf1bf6d3b0b875)lock

| struct [k\_spinlock](structk__spinlock.md) k\_pipe::lock |
| --- |

## [◆ ](#aa1428192b88b97e0cb5ec83894770f47)space

| \_wait\_q\_t k\_pipe::space |
| --- |

## [◆ ](#ac9162db42883d2c14f63cf74ff3c1179)waiting

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe::waiting |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_pipe](structk__pipe.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
