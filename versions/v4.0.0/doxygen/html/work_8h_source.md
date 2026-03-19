---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/work_8h_source.html
original_path: doxygen/html/work_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

work.h

[Go to the documentation of this file.](work_8h.md)

1/\*

2 \* Copyright (c) 2024 Croxel Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_RTIO\_WORKQ\_H\_

8#define ZEPHYR\_INCLUDE\_RTIO\_WORKQ\_H\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[zephyr/device.h](device_8h.md)>

12#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

13#include <[zephyr/sys/p4wq.h](p4wq_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 24](work_8h.md#add537a23ac061970d890f65d76f5f906)typedef void (\*[rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906))(struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

25

[ 32](structrtio__work__req.md)struct [rtio\_work\_req](structrtio__work__req.md) {

[ 34](structrtio__work__req.md#a35fc6d43ec653ca463ebd513145e9051) struct [k\_p4wq\_work](structk__p4wq__work.md) [work](structrtio__work__req.md#a35fc6d43ec653ca463ebd513145e9051);

35

[ 39](structrtio__work__req.md#ae6ea29d7fb3b205dc36cd3155d5e885a) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[iodev\_sqe](structrtio__work__req.md#ae6ea29d7fb3b205dc36cd3155d5e885a);

40

[ 44](structrtio__work__req.md#acdd57e58b85bbc9a75b9b62d4cb3f771) [rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906) [handler](structrtio__work__req.md#acdd57e58b85bbc9a75b9b62d4cb3f771);

45};

46

[ 56](work_8h.md#a705ee008834f10bd4b2ef26e67e1c87f)struct [rtio\_work\_req](structrtio__work__req.md) \*[rtio\_work\_req\_alloc](work_8h.md#a705ee008834f10bd4b2ef26e67e1c87f)(void);

57

[ 65](work_8h.md#a62035ecd9def621b4e70b699d9027140)void [rtio\_work\_req\_submit](work_8h.md#a62035ecd9def621b4e70b699d9027140)(struct [rtio\_work\_req](structrtio__work__req.md) \*req,

66 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[iodev\_sqe](structrtio__work__req.md#ae6ea29d7fb3b205dc36cd3155d5e885a),

67 [rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906) [handler](structrtio__work__req.md#acdd57e58b85bbc9a75b9b62d4cb3f771));

68

[ 74](work_8h.md#a352516812e7bc88b61cceb2f69d9fd3f)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rtio\_work\_req\_used\_count\_get](work_8h.md#a352516812e7bc88b61cceb2f69d9fd3f)(void);

75

76#ifdef \_\_cplusplus

77}

78#endif

79

80#endif /\* ZEPHYR\_INCLUDE\_RTIO\_WORKQ\_H\_ \*/

[device.h](device_8h.md)

[p4wq.h](p4wq_8h.md)

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_p4wq\_work](structk__p4wq__work.md)

P4 Queue Work Item.

**Definition** p4wq.h:29

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:429

[rtio\_work\_req](structrtio__work__req.md)

RTIO Work request.

**Definition** work.h:32

[rtio\_work\_req::work](structrtio__work__req.md#a35fc6d43ec653ca463ebd513145e9051)

struct k\_p4wq\_work work

Work item used to submit unit of work.

**Definition** work.h:34

[rtio\_work\_req::handler](structrtio__work__req.md#acdd57e58b85bbc9a75b9b62d4cb3f771)

rtio\_work\_submit\_t handler

Callback handler where synchronous operation may be executed.

**Definition** work.h:44

[rtio\_work\_req::iodev\_sqe](structrtio__work__req.md#ae6ea29d7fb3b205dc36cd3155d5e885a)

struct rtio\_iodev\_sqe \* iodev\_sqe

Handle to IODEV SQE containing the operation.

**Definition** work.h:39

[rtio\_work\_req\_used\_count\_get](work_8h.md#a352516812e7bc88b61cceb2f69d9fd3f)

uint32\_t rtio\_work\_req\_used\_count\_get(void)

Obtain number of currently used items from the pre-allocated pool.

[rtio\_work\_req\_submit](work_8h.md#a62035ecd9def621b4e70b699d9027140)

void rtio\_work\_req\_submit(struct rtio\_work\_req \*req, struct rtio\_iodev\_sqe \*iodev\_sqe, rtio\_work\_submit\_t handler)

Submit RTIO work request.

[rtio\_work\_req\_alloc](work_8h.md#a705ee008834f10bd4b2ef26e67e1c87f)

struct rtio\_work\_req \* rtio\_work\_req\_alloc(void)

Allocate item to perform an RTIO work request.

[rtio\_work\_submit\_t](work_8h.md#add537a23ac061970d890f65d76f5f906)

void(\* rtio\_work\_submit\_t)(struct rtio\_iodev\_sqe \*iodev\_sqe)

Callback API to execute work operation.

**Definition** work.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [work.h](work_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
