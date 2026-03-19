---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__barrier__apis.html
original_path: doxygen/html/group__barrier__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Barrier Services APIs

[Kernel APIs](group__kernel__apis.md)

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_dmem\_fence\_full](#gab0dd6769236babde7cf48c32007edf31) (void) |
|  | Full/sequentially-consistent data memory barrier. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_dsync\_fence\_full](#gaaa6909c1410bc371f59ad3eec21ee5ef) (void) |
|  | Full/sequentially-consistent data synchronization barrier. |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [barrier\_isync\_fence\_full](#gaa916454a2ff58e50b2f51845447177ec) (void) |
|  | Full/sequentially-consistent instruction synchronization barrier. |

## Detailed Description

Since
:   3.4

Version
:   0.1.0

## Function Documentation

## [◆ ](#gab0dd6769236babde7cf48c32007edf31)barrier\_dmem\_fence\_full()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void barrier\_dmem\_fence\_full | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[barrier.h](sys_2barrier_8h.md)>`

Full/sequentially-consistent data memory barrier.

This routine acts as a synchronization fence between threads and prevents re-ordering of data accesses instructions across the barrier instruction.

## [◆ ](#gaaa6909c1410bc371f59ad3eec21ee5ef)barrier\_dsync\_fence\_full()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void barrier\_dsync\_fence\_full | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[barrier.h](sys_2barrier_8h.md)>`

Full/sequentially-consistent data synchronization barrier.

This routine acts as a synchronization fence between threads and prevents re-ordering of data accesses instructions across the barrier instruction like [barrier\_dmem\_fence\_full()](#gab0dd6769236babde7cf48c32007edf31), but has the additional effect of blocking execution of any further instructions, not just loads or stores, or both, until synchronization is complete.

Note
:   When not supported by hardware or architecture, this instruction falls back to a full/sequentially-consistent data memory barrier.

## [◆ ](#gaa916454a2ff58e50b2f51845447177ec)barrier\_isync\_fence\_full()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void barrier\_isync\_fence\_full | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[barrier.h](sys_2barrier_8h.md)>`

Full/sequentially-consistent instruction synchronization barrier.

This routine is used to guarantee that any subsequent instructions are fetched and to ensure any previously executed context-changing operations, such as writes to system control registers, have completed by the time the routine completes. In hardware terms, this might mean that the instruction pipeline is flushed, for example.

Note
:   When not supported by hardware or architecture, this instruction falls back to a compiler barrier.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
