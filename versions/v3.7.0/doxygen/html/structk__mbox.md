---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__mbox.html
original_path: doxygen/html/structk__mbox.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mbox Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Mailbox APIs](group__mailbox__apis.md)

Mailbox Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| \_wait\_q\_t | [tx\_msg\_queue](#a0bca912a50120707ddafa66d740ade96) |
|  | Transmit messages queue. |
| \_wait\_q\_t | [rx\_msg\_queue](#a808a14c31892a2d042cdb0723a2956e2) |
|  | Receive message queue. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a2c549d5bd7216b62d81ad2198e0d79e4) |

## Detailed Description

Mailbox Structure.

## Field Documentation

## [◆ ](#a2c549d5bd7216b62d81ad2198e0d79e4)lock

| struct [k\_spinlock](structk__spinlock.md) k\_mbox::lock |
| --- |

## [◆ ](#a808a14c31892a2d042cdb0723a2956e2)rx\_msg\_queue

| \_wait\_q\_t k\_mbox::rx\_msg\_queue |
| --- |

Receive message queue.

## [◆ ](#a0bca912a50120707ddafa66d740ade96)tx\_msg\_queue

| \_wait\_q\_t k\_mbox::tx\_msg\_queue |
| --- |

Transmit messages queue.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_mbox](structk__mbox.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
