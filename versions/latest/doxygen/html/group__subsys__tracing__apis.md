---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__apis.html
original_path: doxygen/html/group__subsys__tracing__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Tracing APIs

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md)

Tracing APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Conditional Variable Tracing APIs](group__subsys__tracing__apis__condvar.md) |
|  | Conditional Variable Tracing APIs. |
|  | [Event Tracing APIs](group__subsys__tracing__apis__event.md) |
|  | Event Tracing APIs. |
|  | [FIFO Tracing APIs](group__subsys__tracing__apis__fifo.md) |
|  | FIFO Tracing APIs. |
|  | [Heap Tracing APIs](group__subsys__tracing__apis__heap.md) |
|  | Heap Tracing APIs. |
|  | [LIFO Tracing APIs](group__subsys__tracing__apis__lifo.md) |
|  | LIFO Tracing APIs. |
|  | [Mailbox Tracing APIs](group__subsys__tracing__apis__mbox.md) |
|  | Mailbox Tracing APIs. |
|  | [Memory Slab Tracing APIs](group__subsys__tracing__apis__mslab.md) |
|  | Memory Slab Tracing APIs. |
|  | [Message Queue Tracing APIs](group__subsys__tracing__apis__msgq.md) |
|  | Message Queue Tracing APIs. |
|  | [Mutex Tracing APIs](group__subsys__tracing__apis__mutex.md) |
|  | Mutex Tracing APIs. |
|  | [PM Device Runtime Tracing APIs](group__subsys__tracing__apis__pm__device__runtime.md) |
|  | PM Device Runtime Tracing APIs. |
|  | [Pipe Tracing APIs](group__subsys__tracing__apis__pipe.md) |
|  | Pipe Tracing APIs. |
|  | [Poll Tracing APIs](group__subsys__tracing__apis__poll.md) |
|  | Poll Tracing APIs. |
|  | [Queue Tracing APIs](group__subsys__tracing__apis__queue.md) |
|  | Queue Tracing APIs. |
|  | [Semaphore Tracing APIs](group__subsys__tracing__apis__sem.md) |
|  | Semaphore Tracing APIs. |
|  | [Stack Tracing APIs](group__subsys__tracing__apis__stack.md) |
|  | Stack Tracing APIs. |
|  | [Syscall Tracing APIs](group__subsys__tracing__apis__syscall.md) |
|  | Syscall Tracing APIs. |
|  | [System PM Tracing APIs](group__subsys__tracing__apis__pm__system.md) |
|  | System PM Tracing APIs. |
|  | [Thread Tracing APIs](group__subsys__tracing__apis__thread.md) |
|  | Thread Tracing APIs. |
|  | [Timer Tracing APIs](group__subsys__tracing__apis__timer.md) |
|  | Timer Tracing APIs. |
|  | [Work Delayable Tracing APIs](group__subsys__tracing__apis__work__delayable.md) |
|  | Work Delayable Tracing APIs. |
|  | [Work Poll Tracing APIs](group__subsys__tracing__apis__work__poll.md) |
|  | Work Poll Tracing APIs. |
|  | [Work Queue Tracing APIs](group__subsys__tracing__apis__work__q.md) |
|  | Work Queue Tracing APIs. |
|  | [Work Tracing APIs](group__subsys__tracing__apis__work.md) |
|  | Work Tracing APIs. |

| Functions | |
| --- | --- |
| void | [sys\_trace\_isr\_enter](#ga37f43a02961a847af3b7de6c474a8da4) (void) |
|  | Called when entering an ISR. |
| void | [sys\_trace\_isr\_exit](#ga7113e2760b1a7ffb1bfa108ad9bfb4be) (void) |
|  | Called when exiting an ISR. |
| void | [sys\_trace\_isr\_exit\_to\_scheduler](#ga303fe60fd4de8ddcc02c6920656e326d) (void) |
|  | Called when exiting an ISR and switching to scheduler. |
| void | [sys\_trace\_idle](#gac9b542f78ed796b4b572de19d295c824) (void) |
|  | Called when the cpu enters the idle state. |

## Detailed Description

Tracing APIs.

## Function Documentation

## [◆ ](#gac9b542f78ed796b4b572de19d295c824)sys\_trace\_idle()

| void sys\_trace\_idle | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Called when the cpu enters the idle state.

## [◆ ](#ga37f43a02961a847af3b7de6c474a8da4)sys\_trace\_isr\_enter()

| void sys\_trace\_isr\_enter | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Called when entering an ISR.

## [◆ ](#ga7113e2760b1a7ffb1bfa108ad9bfb4be)sys\_trace\_isr\_exit()

| void sys\_trace\_isr\_exit | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Called when exiting an ISR.

## [◆ ](#ga303fe60fd4de8ddcc02c6920656e326d)sys\_trace\_isr\_exit\_to\_scheduler()

| void sys\_trace\_isr\_exit\_to\_scheduler | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing.h](tracing_2tracing_8h.md)>`

Called when exiting an ISR and switching to scheduler.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
