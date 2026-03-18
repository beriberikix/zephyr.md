---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structpm__device__isr.html
original_path: doxygen/html/structpm__device__isr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_device\_isr Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [Device](group__subsys__pm__device.md)

Runtime PM info for device with synchronous PM.
[More...](#details)

`#include <[device.h](pm_2device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [pm\_device\_base](structpm__device__base.md) | [base](#ad501eabcd3370e9edb6b0851928fd7ac) |
|  | Base info. |
| struct [k\_spinlock](structk__spinlock.md) | [lock](#a24d7dd68bb57794be25450389fc95b33) |
|  | Lock to synchronize the synchronous get/put operations. |

## Detailed Description

Runtime PM info for device with synchronous PM.

Synchronous PM can be used with devices which suspend and resume operations can be performed in the critical section as they are short and non-blocking. Runtime PM API can be used from any context in that case.

## Field Documentation

## [◆ ](#ad501eabcd3370e9edb6b0851928fd7ac)base

| struct [pm\_device\_base](structpm__device__base.md) pm\_device\_isr::base |
| --- |

Base info.

## [◆ ](#a24d7dd68bb57794be25450389fc95b33)lock

| struct [k\_spinlock](structk__spinlock.md) pm\_device\_isr::lock |
| --- |

Lock to synchronize the synchronous get/put operations.

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[device.h](pm_2device_8h_source.md)

- [pm\_device\_isr](structpm__device__isr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
