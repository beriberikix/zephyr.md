---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structk__work__sync.html
original_path: doxygen/html/structk__work__sync.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_work\_sync Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Work Queue APIs](group__workqueue__apis.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.
[More...](#details)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct z\_work\_flusher   [flusher](#ad81ff57cb9f2f3dc5f2d65917cf04f1c) |  |
| struct z\_work\_canceller   [canceller](#a7e8fd0b9d6736c403aefa8462c7c0835) |  |
| }; |  |

## Detailed Description

A structure holding internal state for a pending synchronous operation on a work item or queue.

Instances of this type are provided by the caller for invocation of [k\_work\_flush()](group__workqueue__apis.md#gabd1cda459bab538fb2d6dfd84a73b253 "Wait for last-submitted instance to complete."), [k\_work\_cancel\_sync()](group__workqueue__apis.md#gab2b05cfe3af08f7d32c3946fa1c808f9 "Cancel a work item and wait for it to complete.") and sibling flush and cancel APIs. A referenced object must persist until the call returns, and be accessible from both the caller thread and the work queue thread.

Note
:   If CONFIG\_KERNEL\_COHERENCE is enabled the object must be allocated in coherent memory; see [arch\_mem\_coherent()](group__arch-userspace.md#ga8c6bb0f6730c115689452b016ac1761f "Detect memory coherence type."). The stack on these architectures is generally not coherent. be stack-allocated. Violations are detected by runtime assertion.

## Field Documentation

## [◆ ](#a9dbb971ab8971c68c17cb0569f619b6e)[union]

| union { ... } [k\_work\_sync](structk__work__sync.md) |
| --- |

## [◆ ](#a7e8fd0b9d6736c403aefa8462c7c0835)canceller

| struct z\_work\_canceller k\_work\_sync::canceller |
| --- |

## [◆ ](#ad81ff57cb9f2f3dc5f2d65917cf04f1c)flusher

| struct z\_work\_flusher k\_work\_sync::flusher |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_work\_sync](structk__work__sync.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
