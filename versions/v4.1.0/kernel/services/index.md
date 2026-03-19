---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/services/index.html
original_path: kernel/services/index.html
---

# Kernel Services

The Zephyr kernel lies at the heart of every Zephyr application. It provides
a low footprint, high performance, multi-threaded execution environment
with a rich set of available features. The rest of the Zephyr ecosystem,
including device drivers, networking stack, and application-specific code,
uses the kernel’s features to create a complete application.

The configurable nature of the kernel allows you to incorporate only those
features needed by your application, making it ideal for systems with limited
amounts of memory (as little as 2 KB!) or with simple multi-threading
requirements (such as a set of interrupt handlers and a single background task).
Examples of such systems include: embedded sensor hubs, environmental sensors,
simple LED wearable, and store inventory tags.

Applications requiring more memory (50 to 900 KB), multiple communication
devices (like Wi-Fi and Bluetooth Low Energy), and complex multi-threading,
can also be developed using the Zephyr kernel. Examples of such systems
include: fitness wearables, smart watches, and IoT wireless gateways.

## Scheduling, Interrupts, and Synchronization

These pages cover basic kernel services related to thread scheduling and
synchronization.

## Data Passing

These pages cover kernel objects which can be used to pass data between
threads and ISRs.

The following table summarizes their high-level features.

| Object | Bidirectional? | Data structure | Data item size | Data Alignment | ISRs can receive? | ISRs can send? | Overrun handling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FIFO | No | Queue | Arbitrary [1] | 4 B [2] | Yes [3] | Yes | N/A |
| LIFO | No | Queue | Arbitrary [1] | 4 B [2] | Yes [3] | Yes | N/A |
| Stack | No | Array | Word | Word | Yes [3] | Yes | Undefined behavior |
| Message queue | No | Ring buffer | Arbitrary [6] | Power of two | Yes [3] | Yes | Pend thread or return -errno |
| Mailbox | Yes | Queue | Arbitrary [1] | Arbitrary | No | No | N/A |
| Pipe | No | Ring buffer [4] | Arbitrary | Arbitrary | Yes [5] | Yes [5] | Pend thread or return -errno |

[1] Callers allocate space for queue overhead in the data
elements themselves.

[2] Objects added with k\_fifo\_alloc\_put() and k\_lifo\_alloc\_put()
do not have alignment constraints, but use temporary memory from the
calling thread’s resource pool.

[3] ISRs can receive only when passing K\_NO\_WAIT as the timeout
argument.

[4] Optional.

[5] ISRS can send and/or receive only when passing K\_NO\_WAIT as the
timeout argument.

[6] Data item size must be a multiple of the data alignment.

## Memory Management

See [Memory Management](../memory_management/index.md#memory-management-api).

## Timing

These pages cover timing related services.

## Other

These pages cover other kernel services.
