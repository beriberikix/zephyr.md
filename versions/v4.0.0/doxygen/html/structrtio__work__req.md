---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structrtio__work__req.html
original_path: doxygen/html/structrtio__work__req.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_work\_req Struct Reference

RTIO Work request.
[More...](#details)

`#include <[work.h](work_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_p4wq\_work](structk__p4wq__work.md) | [work](#a35fc6d43ec653ca463ebd513145e9051) |
|  | Work item used to submit unit of work. |
| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | [iodev\_sqe](#ae6ea29d7fb3b205dc36cd3155d5e885a) |
|  | Handle to IODEV SQE containing the operation. |
| [rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906) | [handler](#acdd57e58b85bbc9a75b9b62d4cb3f771) |
|  | Callback handler where synchronous operation may be executed. |

## Detailed Description

RTIO Work request.

This RTIO Work request to perform a work operation decoupled from its submission in the RTIO work-queues.

## Field Documentation

## [◆ ](#acdd57e58b85bbc9a75b9b62d4cb3f771)handler

| [rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906) rtio\_work\_req::handler |
| --- |

Callback handler where synchronous operation may be executed.

This is filled inside [rtio\_work\_req\_submit](work_8h.md#a62035ecd9def621b4e70b699d9027140 "rtio_work_req_submit").

## [◆ ](#ae6ea29d7fb3b205dc36cd3155d5e885a)iodev\_sqe

| struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md)\* rtio\_work\_req::iodev\_sqe |
| --- |

Handle to IODEV SQE containing the operation.

This is filled inside [rtio\_work\_req\_submit](work_8h.md#a62035ecd9def621b4e70b699d9027140 "rtio_work_req_submit").

## [◆ ](#a35fc6d43ec653ca463ebd513145e9051)work

| struct [k\_p4wq\_work](structk__p4wq__work.md) rtio\_work\_req::work |
| --- |

Work item used to submit unit of work.

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[work.h](work_8h_source.md)

- [rtio\_work\_req](structrtio__work__req.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
