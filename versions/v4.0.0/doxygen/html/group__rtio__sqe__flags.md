---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__rtio__sqe__flags.html
original_path: doxygen/html/group__rtio__sqe__flags.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

RTIO SQE Flags

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

RTIO SQE Flags.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [RTIO\_SQE\_CHAINED](#gae9191d521d4ab602b53fefb74020d06b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | The next request in the queue should wait on this one. |
| #define | [RTIO\_SQE\_TRANSACTION](#ga07f09cc0c95be6cfdddb23f8acacb1ea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | The next request in the queue is part of a transaction. |
| #define | [RTIO\_SQE\_MEMPOOL\_BUFFER](#ga2802b46584220afffa0e959e149d5a4d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The buffer should be allocated by the RTIO mempool. |
| #define | [RTIO\_SQE\_CANCELED](#ga7f7f9b038ab8409f271b1aebc1b95ee6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The SQE should not execute if possible. |
| #define | [RTIO\_SQE\_MULTISHOT](#ga00f8ead8f043fe40d49d0bc3325fb299)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The SQE should continue producing CQEs until canceled. |
| #define | [RTIO\_SQE\_NO\_RESPONSE](#ga8578ffdb8f53a51b94fa86a6f02d4a11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The SQE does not produce a CQE. |

## Detailed Description

RTIO SQE Flags.

## Macro Definition Documentation

## [◆ ](#ga7f7f9b038ab8409f271b1aebc1b95ee6)RTIO\_SQE\_CANCELED

| #define RTIO\_SQE\_CANCELED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The SQE should not execute if possible.

If possible (not yet executed), the SQE should be canceled by flagging it as failed and returning -ECANCELED as the result.

## [◆ ](#gae9191d521d4ab602b53fefb74020d06b)RTIO\_SQE\_CHAINED

| #define RTIO\_SQE\_CHAINED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The next request in the queue should wait on this one.

Chained SQEs are individual units of work describing patterns of ordering and failure cascading. A chained SQE must be started only after the one before it. They are given to the iodevs one after another.

## [◆ ](#ga2802b46584220afffa0e959e149d5a4d)RTIO\_SQE\_MEMPOOL\_BUFFER

| #define RTIO\_SQE\_MEMPOOL\_BUFFER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The buffer should be allocated by the RTIO mempool.

This flag can only exist if the CONFIG\_RTIO\_SYS\_MEM\_BLOCKS Kconfig was enabled and the RTIO context was created via the [RTIO\_DEFINE\_WITH\_MEMPOOL()](group__rtio.md#gae4c2a9384a9ae4ed16dff914b1184ca8 "Statically define and initialize an RTIO context.") macro. If set, the buffer associated with the entry was allocated by the internal memory pool and should be released as soon as it is no longer needed via a call to rtio\_release\_mempool().

## [◆ ](#ga00f8ead8f043fe40d49d0bc3325fb299)RTIO\_SQE\_MULTISHOT

| #define RTIO\_SQE\_MULTISHOT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The SQE should continue producing CQEs until canceled.

This flag must exist along [RTIO\_SQE\_MEMPOOL\_BUFFER](#ga2802b46584220afffa0e959e149d5a4d) and signals that when a read is complete. It should be placed back in queue until canceled.

## [◆ ](#ga8578ffdb8f53a51b94fa86a6f02d4a11)RTIO\_SQE\_NO\_RESPONSE

| #define RTIO\_SQE\_NO\_RESPONSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The SQE does not produce a CQE.

## [◆ ](#ga07f09cc0c95be6cfdddb23f8acacb1ea)RTIO\_SQE\_TRANSACTION

| #define RTIO\_SQE\_TRANSACTION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[rtio.h](rtio_2rtio_8h.md)>`

The next request in the queue is part of a transaction.

Transactional SQEs are sequential parts of a unit of work. Only the first transactional SQE is submitted to an iodev, the remaining SQEs are never individually submitted but instead considered to be part of the transaction to the single iodev. The first sqe in the sequence holds the iodev that will be used and the last holds the userdata that will be returned in a single completion on failure/success.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
