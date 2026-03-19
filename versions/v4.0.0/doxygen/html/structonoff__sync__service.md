---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structonoff__sync__service.html
original_path: doxygen/html/structonoff__sync__service.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

onoff\_sync\_service Struct Reference

[Kernel APIs](group__kernel__apis.md) » [On-Off Service APIs](group__resource__mgmt__onoff__apis.md)

State used when a driver uses the on-off service API for synchronous operations.
[More...](#details)

`#include <[onoff.h](onoff_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#ac08d780a80fed2d89c1334cc3c65eeed) |
|  | Mutex protection for other fields. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [count](#adff029426035dffb57fda0de44f2abae) |
|  | Negative is error, non-negative is reference count. |

## Detailed Description

State used when a driver uses the on-off service API for synchronous operations.

This is useful when a subsystem API uses the on-off API to support asynchronous operations but the transitions required by a particular driver are isr-ok and not sleep. It serves as a substitute for [onoff\_manager](structonoff__manager.md "State associated with an on-off manager."), with locking and persisted state updates supported by [onoff\_sync\_lock()](group__resource__mgmt__onoff__apis.md#ga174cadf7dfa5d3c4dc5c8185994f3825 "Lock a synchronous onoff service and provide its state.") and [onoff\_sync\_finalize()](group__resource__mgmt__onoff__apis.md#gae3331bdad9d03309ee78e86c487b7f26 "Process the completion of a transition in a synchronous service and release lock.").

## Field Documentation

## [◆ ](#adff029426035dffb57fda0de44f2abae)count

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) onoff\_sync\_service::count |
| --- |

Negative is error, non-negative is reference count.

## [◆ ](#ac08d780a80fed2d89c1334cc3c65eeed)lock

| struct [k\_spinlock](structk__spinlock.md) onoff\_sync\_service::lock |
| --- |

Mutex protection for other fields.

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[onoff.h](onoff_8h_source.md)

- [onoff\_sync\_service](structonoff__sync__service.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
