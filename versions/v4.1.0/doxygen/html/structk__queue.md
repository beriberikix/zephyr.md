---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__queue.html
original_path: doxygen/html/structk__queue.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_queue Struct Reference

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) | [data\_q](#a892371af9701ce67619e38446bc2ceae) |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a18fd165fec722384b3748bfdf3332a4c) |
| \_wait\_q\_t | [wait\_q](#a871d734f2b21a9cad3ca4a2ba79e64f1) |

## Field Documentation

## [◆ ](#a892371af9701ce67619e38446bc2ceae)data\_q

| [sys\_sflist\_t](group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) k\_queue::data\_q |
| --- |

## [◆ ](#a18fd165fec722384b3748bfdf3332a4c)lock

| struct [k\_spinlock](structk__spinlock.md) k\_queue::lock |
| --- |

## [◆ ](#a871d734f2b21a9cad3ca4a2ba79e64f1)wait\_q

| \_wait\_q\_t k\_queue::wait\_q |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_queue](structk__queue.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
