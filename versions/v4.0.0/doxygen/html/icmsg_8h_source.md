---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/icmsg_8h_source.html
original_path: doxygen/html/icmsg_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icmsg.h

[Go to the documentation of this file.](icmsg_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_IPC\_ICMSG\_H\_

8#define ZEPHYR\_INCLUDE\_IPC\_ICMSG\_H\_

9

10#include <stddef.h>

11#include <[stdint.h](stdint_8h.md)>

12#include <[zephyr/kernel.h](kernel_8h.md)>

13#include <[zephyr/drivers/mbox.h](drivers_2mbox_8h.md)>

14#include <[zephyr/ipc/ipc\_service.h](ipc__service_8h.md)>

15#include <[zephyr/ipc/pbuf.h](pbuf_8h.md)>

16#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

17

18#ifdef \_\_cplusplus

19extern "C" {

20#endif

21

28

[ 29](group__ipc__icmsg__api.md#gab26905275fd20a113d1f05d03761f910)enum [icmsg\_state](group__ipc__icmsg__api.md#gab26905275fd20a113d1f05d03761f910) {

[ 30](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6) [ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6),

[ 31](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a21a71b0c9a3b35e1cf7fe07fff4165c7) [ICMSG\_STATE\_BUSY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a21a71b0c9a3b35e1cf7fe07fff4165c7),

[ 32](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a318b7d8e3a9e2a2ddfa3bc37ff57581f) [ICMSG\_STATE\_READY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a318b7d8e3a9e2a2ddfa3bc37ff57581f),

33};

34

[ 35](structicmsg__config__t.md)struct [icmsg\_config\_t](structicmsg__config__t.md) {

[ 36](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181) struct [mbox\_dt\_spec](structmbox__dt__spec.md) [mbox\_tx](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181);

[ 37](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57) struct [mbox\_dt\_spec](structmbox__dt__spec.md) [mbox\_rx](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57);

38};

39

[ 40](structicmsg__data__t.md)struct [icmsg\_data\_t](structicmsg__data__t.md) {

41 /\* Tx/Rx buffers. \*/

[ 42](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b) struct [pbuf](structpbuf.md) \*[tx\_pb](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b);

[ 43](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6) struct [pbuf](structpbuf.md) \*[rx\_pb](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6);

44#ifdef CONFIG\_IPC\_SERVICE\_ICMSG\_SHMEM\_ACCESS\_SYNC

45 struct [k\_mutex](structk__mutex.md) tx\_lock;

46#endif

47

48 /\* Callbacks for an endpoint. \*/

[ 49](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504) const struct [ipc\_service\_cb](structipc__service__cb.md) \*[cb](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504);

[ 50](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42) void \*[ctx](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42);

51

52 /\* General \*/

[ 53](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99) const struct [icmsg\_config\_t](structicmsg__config__t.md) \*[cfg](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99);

54#ifdef CONFIG\_MULTITHREADING

55 struct [k\_work\_delayable](structk__work__delayable.md) notify\_work;

56 struct [k\_work](structk__work.md) mbox\_work;

57#endif

[ 58](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a);

59};

60

[ 85](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8)int [icmsg\_open](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

86 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data,

87 const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx);

88

[ 103](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d)int [icmsg\_close](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

104 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data);

105

[ 124](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b)int [icmsg\_send](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

125 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data,

126 const void \*msg, size\_t len);

127

131

132#ifdef \_\_cplusplus

133}

134#endif

135

136#endif /\* ZEPHYR\_INCLUDE\_IPC\_ICMSG\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[mbox.h](drivers_2mbox_8h.md)

[icmsg\_close](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d)

int icmsg\_close(const struct icmsg\_config\_t \*conf, struct icmsg\_data\_t \*dev\_data)

Close an icmsg instance.

[icmsg\_send](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b)

int icmsg\_send(const struct icmsg\_config\_t \*conf, struct icmsg\_data\_t \*dev\_data, const void \*msg, size\_t len)

Send a message to the remote icmsg instance.

[icmsg\_open](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8)

int icmsg\_open(const struct icmsg\_config\_t \*conf, struct icmsg\_data\_t \*dev\_data, const struct ipc\_service\_cb \*cb, void \*ctx)

Open an icmsg instance.

[icmsg\_state](group__ipc__icmsg__api.md#gab26905275fd20a113d1f05d03761f910)

icmsg\_state

**Definition** icmsg.h:29

[ICMSG\_STATE\_BUSY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a21a71b0c9a3b35e1cf7fe07fff4165c7)

@ ICMSG\_STATE\_BUSY

**Definition** icmsg.h:31

[ICMSG\_STATE\_READY](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a318b7d8e3a9e2a2ddfa3bc37ff57581f)

@ ICMSG\_STATE\_READY

**Definition** icmsg.h:32

[ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6)

@ ICMSG\_STATE\_OFF

**Definition** icmsg.h:30

[ipc\_service.h](ipc__service_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[pbuf.h](pbuf_8h.md)

[stdint.h](stdint_8h.md)

[icmsg\_config\_t](structicmsg__config__t.md)

**Definition** icmsg.h:35

[icmsg\_config\_t::mbox\_tx](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181)

struct mbox\_dt\_spec mbox\_tx

**Definition** icmsg.h:36

[icmsg\_config\_t::mbox\_rx](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57)

struct mbox\_dt\_spec mbox\_rx

**Definition** icmsg.h:37

[icmsg\_data\_t](structicmsg__data__t.md)

**Definition** icmsg.h:40

[icmsg\_data\_t::cb](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504)

const struct ipc\_service\_cb \* cb

**Definition** icmsg.h:49

[icmsg\_data\_t::cfg](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99)

const struct icmsg\_config\_t \* cfg

**Definition** icmsg.h:53

[icmsg\_data\_t::tx\_pb](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b)

struct pbuf \* tx\_pb

**Definition** icmsg.h:42

[icmsg\_data\_t::rx\_pb](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6)

struct pbuf \* rx\_pb

**Definition** icmsg.h:43

[icmsg\_data\_t::ctx](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42)

void \* ctx

**Definition** icmsg.h:50

[icmsg\_data\_t::state](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a)

atomic\_t state

**Definition** icmsg.h:58

[ipc\_service\_cb](structipc__service__cb.md)

Event callback structure.

**Definition** ipc\_service.h:145

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3985

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3957

[mbox\_dt\_spec](structmbox__dt__spec.md)

MBOX specification from DT.

**Definition** mbox.h:87

[pbuf](structpbuf.md)

Scure packed buffer.

**Definition** pbuf.h:96

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [icmsg.h](icmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
