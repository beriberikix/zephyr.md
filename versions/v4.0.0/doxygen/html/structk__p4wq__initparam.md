---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__p4wq__initparam.html
original_path: doxygen/html/structk__p4wq__initparam.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_p4wq\_initparam Struct Reference

`#include <[p4wq.h](p4wq_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [num](#a399e8da451f26b06d2abf6a7a76b66b4) |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | [stack\_size](#af317fe946a9a03e02608d521c46763ff) |
| struct [k\_p4wq](structk__p4wq.md) \* | [queue](#ac4c282b6fb6e343823d3ae68398df35a) |
| struct [k\_thread](structk__thread.md) \* | [threads](#a8dd0451e7bcc9819d4940db3cc7c0beb) |
| struct z\_thread\_stack\_element \* | [stacks](#a50f2337a6597bfb9f2d74e5b49718217) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a5962a73928834e1548ea8045945274c2) |

## Field Documentation

## [◆ ](#a5962a73928834e1548ea8045945274c2)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_p4wq\_initparam::flags |
| --- |

## [◆ ](#a399e8da451f26b06d2abf6a7a76b66b4)num

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_p4wq\_initparam::num |
| --- |

## [◆ ](#ac4c282b6fb6e343823d3ae68398df35a)queue

| struct [k\_p4wq](structk__p4wq.md)\* k\_p4wq\_initparam::queue |
| --- |

## [◆ ](#af317fe946a9a03e02608d521c46763ff)stack\_size

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) k\_p4wq\_initparam::stack\_size |
| --- |

## [◆ ](#a50f2337a6597bfb9f2d74e5b49718217)stacks

| struct z\_thread\_stack\_element\* k\_p4wq\_initparam::stacks |
| --- |

## [◆ ](#a8dd0451e7bcc9819d4940db3cc7c0beb)threads

| struct [k\_thread](structk__thread.md)\* k\_p4wq\_initparam::threads |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[p4wq.h](p4wq_8h_source.md)

- [k\_p4wq\_initparam](structk__p4wq__initparam.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
