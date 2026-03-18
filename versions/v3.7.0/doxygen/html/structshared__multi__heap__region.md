---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshared__multi__heap__region.html
original_path: doxygen/html/structshared__multi__heap__region.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shared\_multi\_heap\_region Struct Reference

[Operating System Services](group__os__services.md) » [Heap Management](group__heaps.md) » [Shared multi-heap interface](group__shared__multi__heap.md)

SMH region struct.
[More...](#details)

`#include <[shared_multi_heap.h](shared__multi__heap_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [attr](#a5fcdce28a57be4b652a9a53a70ae796f) |
|  | Memory heap attribute. |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [addr](#a905df61648eaa18cebf53bb10dcde91d) |
|  | Memory heap starting virtual address. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#a3f6565062f70b2c8d25c3a0be579482c) |
|  | Memory heap size in bytes. |

## Detailed Description

SMH region struct.

This struct is carrying information about the memory region to be added in the multi-heap pool.

## Field Documentation

## [◆ ](#a905df61648eaa18cebf53bb10dcde91d)addr

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) shared\_multi\_heap\_region::addr |
| --- |

Memory heap starting virtual address.

## [◆ ](#a5fcdce28a57be4b652a9a53a70ae796f)attr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) shared\_multi\_heap\_region::attr |
| --- |

Memory heap attribute.

## [◆ ](#a3f6565062f70b2c8d25c3a0be579482c)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shared\_multi\_heap\_region::size |
| --- |

Memory heap size in bytes.

---

The documentation for this struct was generated from the following file:

- zephyr/multi\_heap/[shared\_multi\_heap.h](shared__multi__heap_8h_source.md)

- [shared\_multi\_heap\_region](structshared__multi__heap__region.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
