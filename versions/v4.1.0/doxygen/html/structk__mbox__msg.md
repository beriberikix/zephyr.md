---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__mbox__msg.html
original_path: doxygen/html/structk__mbox__msg.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mbox\_msg Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Mailbox APIs](group__mailbox__apis.md)

Mailbox Message Structure.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size](#aeabf45e9599a64852a1cfd656b1ece8e) |
|  | size of message (in bytes) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [info](#aa79f2bf71431b474ec4551ade4d7a8dd) |
|  | application-defined information value |
| void \* | [tx\_data](#a74b0edeed4c44cb5932eb292efc9d9c2) |
|  | sender's message data buffer |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [rx\_source\_thread](#a9eb145a242ac66e80d90286d83fe7a61) |
|  | source thread id |
| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | [tx\_target\_thread](#a73236acb7d27bb0233f5abb7214fb19c) |
|  | target thread id |

## Detailed Description

Mailbox Message Structure.

## Field Documentation

## [◆ ](#aa79f2bf71431b474ec4551ade4d7a8dd)info

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mbox\_msg::info |
| --- |

application-defined information value

## [◆ ](#a9eb145a242ac66e80d90286d83fe7a61)rx\_source\_thread

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_mbox\_msg::rx\_source\_thread |
| --- |

source thread id

## [◆ ](#aeabf45e9599a64852a1cfd656b1ece8e)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_mbox\_msg::size |
| --- |

size of message (in bytes)

## [◆ ](#a74b0edeed4c44cb5932eb292efc9d9c2)tx\_data

| void\* k\_mbox\_msg::tx\_data |
| --- |

sender's message data buffer

## [◆ ](#a73236acb7d27bb0233f5abb7214fb19c)tx\_target\_thread

| [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) k\_mbox\_msg::tx\_target\_thread |
| --- |

target thread id

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_mbox\_msg](structk__mbox__msg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
