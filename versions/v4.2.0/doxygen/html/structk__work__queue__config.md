---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structk__work__queue__config.html
original_path: doxygen/html/structk__work__queue__config.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_work\_queue\_config Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Work Queue APIs](group__workqueue__apis.md)

A structure holding optional configuration items for a work queue.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#a0929d83372efff6798bc69bb7ca1eaaa) |
|  | The name to be given to the work queue thread. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [no\_yield](#afcf64d6e69d1ddfff8cbd749dafa4d13) |
|  | Control whether the work queue thread should yield between items. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [essential](#a5aa4a80d91ef36498443c163428b02c0) |
|  | Control whether the work queue thread should be marked as essential thread. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [work\_timeout\_ms](#a517d9895f211d886de4b18f2f16d06c3) |
|  | Controls whether work queue monitors work timeouts. |

## Detailed Description

A structure holding optional configuration items for a work queue.

This structure, and values it references, are not retained by [k\_work\_queue\_start()](group__workqueue__apis.md#gadfc56554f9bfe7b52309d79660188593 "Initialize a work queue.").

## Field Documentation

## [◆ ](#a5aa4a80d91ef36498443c163428b02c0)essential

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_queue\_config::essential |
| --- |

Control whether the work queue thread should be marked as essential thread.

## [◆ ](#a0929d83372efff6798bc69bb7ca1eaaa)name

| const char\* k\_work\_queue\_config::name |
| --- |

The name to be given to the work queue thread.

If left null the thread will not have a name.

## [◆ ](#afcf64d6e69d1ddfff8cbd749dafa4d13)no\_yield

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) k\_work\_queue\_config::no\_yield |
| --- |

Control whether the work queue thread should yield between items.

Yielding between items helps guarantee the work queue thread does not starve other threads, including cooperative ones released by a work item. This is the default behavior.

Set this to `true` to prevent the work queue thread from yielding between items. This may be appropriate when a sequence of items should complete without yielding control.

## [◆ ](#a517d9895f211d886de4b18f2f16d06c3)work\_timeout\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_work\_queue\_config::work\_timeout\_ms |
| --- |

Controls whether work queue monitors work timeouts.

If non-zero, and CONFIG\_WORKQUEUE\_WORK\_TIMEOUT is enabled, the work queue will monitor the duration of each work item. If the work item handler takes longer than the specified time to execute, the work queue thread will be aborted, and an error will be logged if CONFIG\_LOG is enabled.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_work\_queue\_config](structk__work__queue__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
