---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structzbus__channel__data.html
original_path: doxygen/html/structzbus__channel__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zbus\_channel\_data Struct Reference

[Operating System Services](group__os__services.md) » [Zbus APIs](group__zbus__apis.md)

Type used to represent a channel mutable data.
[More...](#details)

`#include <[zbus.h](zbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [observers\_start\_idx](#a6329a0af467d83ad488f3310c1002c41) |
|  | Static channel observer list start index. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [observers\_end\_idx](#a5b3c38f70cd99cc7e83f9b641997e1ed) |
|  | Static channel observer list end index. |
| struct k\_sem | [sem](#a6fa71ae5dc260f5934f47383f53891a7) |
|  | Access control semaphore. |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [observers](#aeffcb35769775ee0927c3af9be77d1e1) |
|  | Channel observer list. |
| struct [net\_buf\_pool](structnet__buf__pool.md) \* | [msg\_subscriber\_pool](#a2490c05755696b7ba1f1f1392d27845f) |
|  | Net buf pool for message subscribers. |

## Detailed Description

Type used to represent a channel mutable data.

Every channel has a [zbus\_channel\_data](structzbus__channel__data.md "Type used to represent a channel mutable data.") structure associated.

## Field Documentation

## [◆ ](#a2490c05755696b7ba1f1f1392d27845f)msg\_subscriber\_pool

| struct [net\_buf\_pool](structnet__buf__pool.md)\* zbus\_channel\_data::msg\_subscriber\_pool |
| --- |

Net buf pool for message subscribers.

It can be either the global or a separated one.

## [◆ ](#aeffcb35769775ee0927c3af9be77d1e1)observers

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) zbus\_channel\_data::observers |
| --- |

Channel observer list.

Represents the channel's observers list, it can be empty or have listeners and subscribers mixed in any sequence. It can be changed in runtime.

## [◆ ](#a5b3c38f70cd99cc7e83f9b641997e1ed)observers\_end\_idx

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) zbus\_channel\_data::observers\_end\_idx |
| --- |

Static channel observer list end index.

Considering the ITERABLE SECTIONS allocation order.

## [◆ ](#a6329a0af467d83ad488f3310c1002c41)observers\_start\_idx

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) zbus\_channel\_data::observers\_start\_idx |
| --- |

Static channel observer list start index.

Considering the ITERABLE SECTIONS allocation order.

## [◆ ](#a6fa71ae5dc260f5934f47383f53891a7)sem

| struct k\_sem zbus\_channel\_data::sem |
| --- |

Access control semaphore.

Points to the semaphore used to avoid race conditions for accessing the channel.

---

The documentation for this struct was generated from the following file:

- zephyr/zbus/[zbus.h](zbus_8h_source.md)

- [zbus\_channel\_data](structzbus__channel__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
