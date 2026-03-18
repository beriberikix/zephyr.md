---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structpm__device.html
original_path: doxygen/html/structpm__device.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pm\_device Struct Reference

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md) » [Device](group__subsys__pm__device.md)

Runtime PM info for device with generic PM.
[More...](#details)

`#include <[device.h](pm_2device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [pm\_device\_base](structpm__device__base.md) | [base](#afb5db0142ebab7891a42f71b59fd55cb) |
|  | Base info. |
| const struct [device](structdevice.md) \* | [dev](#aec09c5708cda21c6e3af2a4e7082b432) |
|  | Pointer to the device. |
| struct k\_sem | [lock](#ab7e54f9195359f60cc0a4b06677df0c7) |
|  | Lock to synchronize the get/put operations. |
| struct [k\_event](structk__event.md) | [event](#aa8ed27c6c0cff89062922bedae4dca35) |
|  | Event var to listen to the sync request events. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [work](#a5dc3b48b3139d546206c8b9cacaf09fd) |
|  | Work object for asynchronous calls. |

## Detailed Description

Runtime PM info for device with generic PM.

Generic PM involves suspending and resuming operations which can be blocking, long lasting or asynchronous. Runtime PM API is limited when used from interrupt context.

## Field Documentation

## [◆ ](#afb5db0142ebab7891a42f71b59fd55cb)base

| struct [pm\_device\_base](structpm__device__base.md) pm\_device::base |
| --- |

Base info.

## [◆ ](#aec09c5708cda21c6e3af2a4e7082b432)dev

| const struct [device](structdevice.md)\* pm\_device::dev |
| --- |

Pointer to the device.

## [◆ ](#aa8ed27c6c0cff89062922bedae4dca35)event

| struct [k\_event](structk__event.md) pm\_device::event |
| --- |

Event var to listen to the sync request events.

## [◆ ](#ab7e54f9195359f60cc0a4b06677df0c7)lock

| struct k\_sem pm\_device::lock |
| --- |

Lock to synchronize the get/put operations.

## [◆ ](#a5dc3b48b3139d546206c8b9cacaf09fd)work

| struct [k\_work\_delayable](structk__work__delayable.md) pm\_device::work |
| --- |

Work object for asynchronous calls.

---

The documentation for this struct was generated from the following file:

- zephyr/pm/[device.h](pm_2device_8h_source.md)

- [pm\_device](structpm__device.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
