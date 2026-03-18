---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/arch/smp/pktqueue/README.html
original_path: samples/arch/smp/pktqueue/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# SMP pktqueue

## Overview

This sample application performs a simplified network layer forwarding function
(essentially checksum calculation from IP Header Validation) of the Internet protocol
suite specified in RFC1812 “Requirements for IP Version 4 Routers” which
can be found at [http://www.faqs.org/rfcs/rfc1812.html](http://www.faqs.org/rfcs/rfc1812.html). This application
provides an indication of the potential performance of a microprocessor in an
IP router system.

At the beginning of the application the array (size defined in SIZE\_OF\_QUEUE)
of packet headers is initialized. Each header contains some random data of size
defined in SIZE\_OF\_HEADER and calculated crc16 header checksum
in appropriate field defined by CRC\_BYTE\_1 and CRC\_BYTE\_2. The contents of
header follows:

> | 0 - 3 | | | | 4 - 7 | | | | 8 - 15 | | | | | | | | 16 - 31 | | | | | | | | | | | | | | | |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | Version | | | | IHL | | | | Type of Service | | | | | | | | Total Length | | | | | | | | | | | | | | | |
> | Identification | | | | | | | | | | | | | | | | Flags | | | Fragment Offset | | | | | | | | | | | | |
> | Time to Live | | | | | | | | Protocol | | | | | | | | Header Checksum | | | | | | | | | | | | | | | |
> | Source Address | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
> | Destination Address | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
> | Options | | | | | | | | | | | | | | | | | | | | | | | | Padding | | | | | | | |

The headers then are stored in multiple “sender” queues (the number is defined
in QUEUE\_NUM). After that for each pair of “sender”/”receiver” queues one thread
is created, which will control “sender” queue processing.

Then in each queue-related thread several(defined in THREADS\_NUM) threads are created. Each
of them first pick the header from “sender” queue, calculates crc and if
crc is correct put the header to “receiver” queue. Only one thread in a
time can access to sender or receiver queue.

As soon as all headers in each pair of queues are moved from “sender” to
“receiver” queue the execution of threads(related to pair) are terminated.

By changing the value of CONFIG\_MP\_MAX\_NUM\_CPUS on SMP systems, you
can see that using more cores takes almost linearly less time
to complete the computational task.

You can also edit the sample source code to change the
number of parallel executed pairs of queues(`QUEUE_NUM`),
the number of threads per pair of queues(`THREADS_NUM`),
the number of headers in queue (`SIZE_OF_QUEUE`), and
size of header in bytes (`SIZE_OF_HEADER`).

## Building and Running

This project outputs total time required for processing all packet headers.
It can be built and executed on QEMU as follows:

```shell
west build -b qemu_x86_64 samples/arch/smp/pktqueue
west build -t run
```

### Sample Output

```shell
Simulating IP header validation on multiple cores.
Each of 2 parallel queues is processed by 3 threads on 2 cores and contain 5000 packet headers.
Bytes in packet header: 24

RESULT: OK
Application ran successfully.
All 20000 packet headers were processed in 89 msec
```
