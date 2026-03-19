---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structrtio.html
original_path: doxygen/html/structrtio.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

An RTIO context containing what can be viewed as a pair of queues.
[More...](#details)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [cq\_count](#a358de1033ab4396d1f1baee2699c993f) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [xcqcnt](#ac45facdcc6d64cd70113b9b05b2fb086) |
| struct [rtio\_sqe\_pool](structrtio__sqe__pool.md) \* | [sqe\_pool](#a955f012bac623e7c037b5f1dba8e7fda) |
| struct [rtio\_cqe\_pool](structrtio__cqe__pool.md) \* | [cqe\_pool](#a1bce3c3bb0150275ece65975adf3ee4f) |
| struct [mpsc](structmpsc.md) | [sq](#a34fbabfdbef3144f4520bf678684cdfb) |
| struct [mpsc](structmpsc.md) | [cq](#ad6f44a354a170cb04a584beee7728fa9) |

## Detailed Description

An RTIO context containing what can be viewed as a pair of queues.

A queue for submissions (available and in queue to be produced) as well as a queue of completions (available and ready to be consumed).

The rtio executor along with any objects implementing the [rtio\_iodev](structrtio__iodev.md "An IO device with a function table for submitting requests.") interface are the consumers of submissions and producers of completions.

No work is started until [rtio\_submit()](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e "Submit I/O requests to the underlying executor.") is called.

## Field Documentation

## [◆ ](#ad6f44a354a170cb04a584beee7728fa9)cq

| struct [mpsc](structmpsc.md) rtio::cq |
| --- |

## [◆ ](#a358de1033ab4396d1f1baee2699c993f)cq\_count

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) rtio::cq\_count |
| --- |

## [◆ ](#a1bce3c3bb0150275ece65975adf3ee4f)cqe\_pool

| struct [rtio\_cqe\_pool](structrtio__cqe__pool.md)\* rtio::cqe\_pool |
| --- |

## [◆ ](#a34fbabfdbef3144f4520bf678684cdfb)sq

| struct [mpsc](structmpsc.md) rtio::sq |
| --- |

## [◆ ](#a955f012bac623e7c037b5f1dba8e7fda)sqe\_pool

| struct [rtio\_sqe\_pool](structrtio__sqe__pool.md)\* rtio::sqe\_pool |
| --- |

## [◆ ](#ac45facdcc6d64cd70113b9b05b2fb086)xcqcnt

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) rtio::xcqcnt |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio](structrtio.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
