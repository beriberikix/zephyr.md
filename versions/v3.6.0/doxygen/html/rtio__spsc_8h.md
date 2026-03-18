---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rtio__spsc_8h.html
original_path: doxygen/html/rtio__spsc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_spsc.h File Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md) » [RTIO SPSC API](group__rtio__spsc.md)

A lock-free and type safe power of 2 fixed sized single producer single consumer (SPSC) queue using a ringbuffer and atomics to ensure coherency.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/toolchain/common.h](common_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](rtio__spsc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RTIO\_SPSC\_INITIALIZER](group__rtio__spsc.md#ga54a199d7030fad8387acf057539f2854)(sz, buf) |
|  | Statically initialize an rtio\_spsc. |
| #define | [RTIO\_SPSC\_DECLARE](group__rtio__spsc.md#ga6d1f8fb2f7caf60680e434557b1947ad)(name, type) |
|  | Declare an anonymous struct type for an rtio\_spsc. |
| #define | [RTIO\_SPSC\_DEFINE](group__rtio__spsc.md#ga03de50debdf6a3acca9f02f4bc9b7ad9)(name, type, sz) |
|  | Define an rtio\_spsc with a fixed size. |
| #define | [rtio\_spsc\_size](group__rtio__spsc.md#gad47e0fcf59138828b74b29f7c59c55c2)(spsc) |
|  | Size of the SPSC queue. |
| #define | [rtio\_spsc\_reset](group__rtio__spsc.md#ga803ff0ddddc3ca3fc37b6e39e9b65746)(spsc) |
|  | Initialize/reset a spsc such that its empty. |
| #define | [rtio\_spsc\_acquire](group__rtio__spsc.md#ga31521b366a5ab60852b799dfa8d1fca4)(spsc) |
|  | Acquire an element to produce from the SPSC. |
| #define | [rtio\_spsc\_produce](group__rtio__spsc.md#gaf7ac949ed6a896b2cb39141109f43f2f)(spsc) |
|  | Produce one previously acquired element to the SPSC. |
| #define | [rtio\_spsc\_produce\_all](group__rtio__spsc.md#ga9eb327619c7dc567d5a70d538db95f2c)(spsc) |
|  | Produce all previously acquired elements to the SPSC. |
| #define | [rtio\_spsc\_drop\_all](group__rtio__spsc.md#ga4f2be93f9b094269db5a844a0038b582)(spsc) |
|  | Drop all previously acquired elements. |
| #define | [rtio\_spsc\_consume](group__rtio__spsc.md#ga163a7a6eedff934a2bc7b093c0bc8de5)(spsc) |
|  | Consume an element from the spsc. |
| #define | [rtio\_spsc\_release](group__rtio__spsc.md#gad6e8916b9bdd9dbd00fddacec39b8898)(spsc) |
|  | Release a consumed element. |
| #define | [rtio\_spsc\_release\_all](group__rtio__spsc.md#ga3d0ab7e1a3e777c22c60e711350e9d4a)(spsc) |
|  | Release all consumed elements. |
| #define | [rtio\_spsc\_acquirable](group__rtio__spsc.md#gaa214fb1ca3172d16ba6b6c07fb1d0053)(spsc) |
|  | Count of acquirable in spsc. |
| #define | [rtio\_spsc\_consumable](group__rtio__spsc.md#ga69cdbead4d23d77d952490ab6045c046)(spsc) |
|  | Count of consumables in spsc. |
| #define | [rtio\_spsc\_peek](group__rtio__spsc.md#ga614c7cc6abc2222735e2a9581b5b347f)(spsc) |
|  | Peek at the first available item in queue. |
| #define | [rtio\_spsc\_next](group__rtio__spsc.md#ga91e8862b750c8bdad27b93023d484b68)(spsc, item) |
|  | Peek at the next item in the queue from a given one. |
| #define | [rtio\_spsc\_prev](group__rtio__spsc.md#gaf02b036e6131ca3a320e085221e665b9)(spsc, item) |
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
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [rtio\_spsc.h](rtio__spsc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
