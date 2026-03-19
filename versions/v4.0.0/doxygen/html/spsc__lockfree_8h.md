---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/spsc__lockfree_8h.html
original_path: doxygen/html/spsc__lockfree_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spsc\_lockfree.h File Reference

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md) » [SPSC API](group__spsc__lockfree.md)

A lock-free and type safe power of 2 fixed sized single producer single consumer (SPSC) queue using a ringbuffer and atomics to ensure coherency.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](spsc__lockfree_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SPSC\_INITIALIZER](group__spsc__lockfree.md#ga18aecd57468b7e6b3779c86952647238)(sz, buf) |
|  | Statically initialize an spsc. |
| #define | [SPSC\_DECLARE](group__spsc__lockfree.md#gaef8a80e3a9bc0d30e1e3b29ff7b6ba85)(name, type) |
|  | Declare an anonymous struct type for an spsc. |
| #define | [SPSC\_DEFINE](group__spsc__lockfree.md#ga8d1ccd780f9e0656fffc59ffc828fd1f)(name, type, sz) |
|  | Define an spsc with a fixed size. |
| #define | [spsc\_size](group__spsc__lockfree.md#ga4b191cf95a0fdae8a197037ab252a58c)(spsc) |
|  | Size of the SPSC queue. |
| #define | [spsc\_reset](group__spsc__lockfree.md#gaca6733f19cd9d05ff27176d3ef813490)(spsc) |
|  | Initialize/reset a spsc such that its empty. |
| #define | [spsc\_acquire](group__spsc__lockfree.md#gaa9e6c12ab0d83759b1387be9d299462d)(spsc) |
|  | Acquire an element to produce from the SPSC. |
| #define | [spsc\_produce](group__spsc__lockfree.md#ga8f3308d2e1ef28d29f9eabd46ed90bde)(spsc) |
|  | Produce one previously acquired element to the SPSC. |
| #define | [spsc\_produce\_all](group__spsc__lockfree.md#ga971fea8aa902ccaac6a3ac787046d0cd)(spsc) |
|  | Produce all previously acquired elements to the SPSC. |
| #define | [spsc\_drop\_all](group__spsc__lockfree.md#ga30f61cd259725e8a06b920517d23df01)(spsc) |
|  | Drop all previously acquired elements. |
| #define | [spsc\_consume](group__spsc__lockfree.md#gacca4ce3da7128ecadb861b47bd55bf9b)(spsc) |
|  | Consume an element from the spsc. |
| #define | [spsc\_release](group__spsc__lockfree.md#ga4d20e781b0f811a08334375664d74726)(spsc) |
|  | Release a consumed element. |
| #define | [spsc\_release\_all](group__spsc__lockfree.md#ga624be14173fbb26c8b09e50e9e0d46a2)(spsc) |
|  | Release all consumed elements. |
| #define | [spsc\_acquirable](group__spsc__lockfree.md#ga2bed9808d75ed0617e4442fd6d69244c)(spsc) |
|  | Count of acquirable in spsc. |
| #define | [spsc\_consumable](group__spsc__lockfree.md#gae2b68434c49078b1a55930b4a99aacdf)(spsc) |
|  | Count of consumables in spsc. |
| #define | [spsc\_peek](group__spsc__lockfree.md#gac382c3a75dbc1df5d6d40df8c7d54266)(spsc) |
|  | Peek at the first available item in queue. |
| #define | [spsc\_next](group__spsc__lockfree.md#gaba7acaae1e0a8a9b82b73ed15acf89a9)(spsc, item) |
|  | Peek at the next item in the queue from a given one. |
| #define | [spsc\_prev](group__spsc__lockfree.md#gabdcbd5a0dc5ea88811967494361c0bfc)(spsc, item) |
|  | Get the previous item in the queue from a given one. |

## Detailed Description

A lock-free and type safe power of 2 fixed sized single producer single consumer (SPSC) queue using a ringbuffer and atomics to ensure coherency.

This SPSC queue implementation works on an array which wraps using a power of two size and uses a bit mask to perform a modulus. Atomics are used to allow single-producer single-consumer safe semantics without locks. Elements are expected to be of a fixed size. The API is type safe as the underlying buffer is typed and all usage is done through macros.

An SPSC queue may be declared on a stack or statically and work as intended so long as its lifetime outlives any usage. Static declarations should be the preferred method as stack . It is meant to be a shared object between two execution contexts (ISR and a thread for example)

An SPSC queue is safe to produce or consume in an ISR with O(1) push/pull.

Warning
:   SPSC is *not* safe to produce or consume in multiple execution contexts.

Safe usage would be, where A and B are unique execution contexts:

1. ISR A producing and a Thread B consuming.
2. Thread A producing and ISR B consuming.
3. Thread A producing and Thread B consuming.
4. ISR A producing and ISR B consuming.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [spsc\_lockfree.h](spsc__lockfree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
