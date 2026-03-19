---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpsa__storage__info__t.html
original_path: doxygen/html/structpsa__storage__info__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psa\_storage\_info\_t Struct Reference

Metadata associated with a specific entry.
[More...](#details)

`#include <[storage_common.h](storage__common_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [capacity](#a1b2d4b80f2989c0c182bf519442090ae) |
|  | The allocated capacity of the storage associated with an entry. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a2a18bf8e7a44cc050e088fb34a453a1d) |
|  | The size of an entry's data. |
| [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) | [flags](#a3dfb41a4b9bf931f3b3fe96f13c1d289) |
|  | The flags used when the entry was created. |

## Detailed Description

Metadata associated with a specific entry.

## Field Documentation

## [◆ ](#a1b2d4b80f2989c0c182bf519442090ae)capacity

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) psa\_storage\_info\_t::capacity |
| --- |

The allocated capacity of the storage associated with an entry.

## [◆ ](#a3dfb41a4b9bf931f3b3fe96f13c1d289)flags

| [psa\_storage\_create\_flags\_t](storage__common_8h.md#a1f53bd4fd1ba72bd88e9d7d9eb7da211) psa\_storage\_info\_t::flags |
| --- |

The flags used when the entry was created.

## [◆ ](#a2a18bf8e7a44cc050e088fb34a453a1d)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) psa\_storage\_info\_t::size |
| --- |

The size of an entry's data.

---

The documentation for this struct was generated from the following file:

- /tmp/zephyrproject/zephyr/subsys/secure\_storage/include/psa/[storage\_common.h](storage__common_8h_source.md)

- [psa\_storage\_info\_t](structpsa__storage__info__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
