---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/README.html
original_path: samples/subsys/portability/cmsis_rtos_v2/timer_synchronization/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Synchronization using CMSIS RTOS V2 APIs

## Overview

The sample project illustrates usage of timers and message queues using
CMSIS RTOS V2 APIs.

The main thread creates a preemptive thread which writes message to message queue
and on timer expiry, message is read by main thread.

## Building and Running Project

This project outputs to the console. It can be built and executed
on QEMU as follows:

```shell
west build -b qemu_x86 samples/philosophers
west build -t run
```

### Sample Output

```shell
Wrote to message queue: 5
Read from message queue: 5

Wrote to message queue: 6
Read from message queue: 6

Wrote to message queue: 7
Read from message queue: 7

Wrote to message queue: 8
Read from message queue: 8

Wrote to message queue: 9
Read from message queue: 9

Wrote to message queue: 10
Read from message queue: 10

Wrote to message queue: 11
Read from message queue: 11

Wrote to message queue: 12
Read from message queue: 12

Wrote to message queue: 13
Read from message queue: 13

Wrote to message queue: 14
Read from message queue: 14

Wrote to message queue: 15
Read from message queue: 15

Sample execution successful
```

Exit QEMU by pressing `CTRL+A` `x`.
