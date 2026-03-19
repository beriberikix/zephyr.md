---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsched__poll.html
original_path: doxygen/html/structsched__poll.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sched\_poll Struct Reference

`#include <[sched.h](xen_2public_2sched_8h_source.md)>`

| Public Member Functions | |
| --- | --- |
|  | [XEN\_GUEST\_HANDLE](#ae3edf9e983927d88d84aea48015e7619) ([evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f)) ports |

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [nr\_ports](#a2dd2e52e0db41c71033a2d64fe984f16) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timeout](#a1cd79e2b5d5d58b16bc65869fb629e81) |

## Member Function Documentation

## [◆ ](#ae3edf9e983927d88d84aea48015e7619)XEN\_GUEST\_HANDLE()

| sched\_poll::XEN\_GUEST\_HANDLE | ( | [evtchn\_port\_t](event__channel_8h.md#aaad5124a66f37437561260d1170ab33f) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Field Documentation

## [◆ ](#a2dd2e52e0db41c71033a2d64fe984f16)nr\_ports

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int sched\_poll::nr\_ports |
| --- |

## [◆ ](#a1cd79e2b5d5d58b16bc65869fb629e81)timeout

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sched\_poll::timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[sched.h](xen_2public_2sched_8h_source.md)

- [sched\_poll](structsched__poll.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
