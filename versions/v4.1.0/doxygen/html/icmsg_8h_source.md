---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/icmsg_8h_source.html
original_path: doxygen/html/icmsg_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 32](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6) [ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6),

33

[ 37](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6) [ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6),

38

[ 43](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7) [ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7),

44

[ 50](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb) [ICMSG\_STATE\_INITIALIZING\_SID\_DETECT](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb),

51

[ 56](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a1e95d66a57e9f7bd2dd818ea8182b2dd) [ICMSG\_STATE\_DISCONNECTED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a1e95d66a57e9f7bd2dd818ea8182b2dd),

57

58 /\* Connected states must be at the end. \*/

59

[ 63](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ac9b07c0dd80a5e4f5029a3984d552bab) [ICMSG\_STATE\_CONNECTED\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ac9b07c0dd80a5e4f5029a3984d552bab),

64

[ 69](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a32fba02984cec57994a5ae94c4e2ab87) [ICMSG\_STATE\_CONNECTED\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a32fba02984cec57994a5ae94c4e2ab87),

70};

71

[ 72](group__ipc__icmsg__api.md#gae14e0b81c90a4bb4fc140a48a48d1b5f)enum [icmsg\_unbound\_mode](group__ipc__icmsg__api.md#gae14e0b81c90a4bb4fc140a48a48d1b5f) {

[ 73](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fac688a38231634863b4f3a5baa73de57a) [ICMSG\_UNBOUND\_MODE\_DISABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fac688a38231634863b4f3a5baa73de57a) = [ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6),

[ 74](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa644f1bdb89f1e3940909a0269c9fca07) [ICMSG\_UNBOUND\_MODE\_ENABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa644f1bdb89f1e3940909a0269c9fca07) = [ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7),

[ 75](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa3dbd2f53889c3d5a40948700df4d5f75) [ICMSG\_UNBOUND\_MODE\_DETECT](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa3dbd2f53889c3d5a40948700df4d5f75) = [ICMSG\_STATE\_INITIALIZING\_SID\_DETECT](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb),

76};

77

[ 78](structicmsg__config__t.md)struct [icmsg\_config\_t](structicmsg__config__t.md) {

[ 79](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181) struct [mbox\_dt\_spec](structmbox__dt__spec.md) [mbox\_tx](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181);

[ 80](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57) struct [mbox\_dt\_spec](structmbox__dt__spec.md) [mbox\_rx](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57);

[ 81](structicmsg__config__t.md#afdbe5d280cb60eb7cfddd8c7cf27f71b) enum [icmsg\_unbound\_mode](group__ipc__icmsg__api.md#gae14e0b81c90a4bb4fc140a48a48d1b5f) [unbound\_mode](structicmsg__config__t.md#afdbe5d280cb60eb7cfddd8c7cf27f71b);

82};

83

[ 84](structicmsg__data__t.md)struct [icmsg\_data\_t](structicmsg__data__t.md) {

85 /\* Tx/Rx buffers. \*/

[ 86](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b) struct [pbuf](structpbuf.md) \*[tx\_pb](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b);

[ 87](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6) struct [pbuf](structpbuf.md) \*[rx\_pb](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6);

88#ifdef CONFIG\_IPC\_SERVICE\_ICMSG\_SHMEM\_ACCESS\_SYNC

89 struct [k\_mutex](structk__mutex.md) tx\_lock;

90#endif

91

92 /\* Callbacks for an endpoint. \*/

[ 93](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504) const struct [ipc\_service\_cb](structipc__service__cb.md) \*[cb](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504);

[ 94](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42) void \*[ctx](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42);

95

96 /\* General \*/

[ 97](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99) const struct [icmsg\_config\_t](structicmsg__config__t.md) \*[cfg](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99);

98#ifdef CONFIG\_MULTITHREADING

99 struct [k\_work](structk__work.md) mbox\_work;

100#endif

[ 101](structicmsg__data__t.md#a26c86f7bfa3cc8931051c7239ddddbd5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [remote\_sid](structicmsg__data__t.md#a26c86f7bfa3cc8931051c7239ddddbd5);

[ 102](structicmsg__data__t.md#a511835de55ae6123ee5b91d66da3d441) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [local\_sid](structicmsg__data__t.md#a511835de55ae6123ee5b91d66da3d441);

[ 103](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a);

104};

105

[ 130](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8)int [icmsg\_open](group__ipc__icmsg__api.md#ga6017af391a3135c02cec7929620789e8)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

131 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data,

132 const struct [ipc\_service\_cb](structipc__service__cb.md) \*cb, void \*ctx);

133

[ 148](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d)int [icmsg\_close](group__ipc__icmsg__api.md#ga0d8f5626406ca660e616de131f54e29d)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

149 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data);

150

[ 169](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b)int [icmsg\_send](group__ipc__icmsg__api.md#ga13b8669034ee51044df7f0623907c03b)(const struct [icmsg\_config\_t](structicmsg__config__t.md) \*conf,

170 struct [icmsg\_data\_t](structicmsg__data__t.md) \*dev\_data,

171 const void \*msg, size\_t len);

172

176

177#ifdef \_\_cplusplus

178}

179#endif

180

181#endif /\* ZEPHYR\_INCLUDE\_IPC\_ICMSG\_H\_ \*/

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

[icmsg\_unbound\_mode](group__ipc__icmsg__api.md#gae14e0b81c90a4bb4fc140a48a48d1b5f)

icmsg\_unbound\_mode

**Definition** icmsg.h:72

[ICMSG\_STATE\_DISCONNECTED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a1e95d66a57e9f7bd2dd818ea8182b2dd)

@ ICMSG\_STATE\_DISCONNECTED

Instance was closed on remote side.

**Definition** icmsg.h:56

[ICMSG\_STATE\_CONNECTED\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a32fba02984cec57994a5ae94c4e2ab87)

@ ICMSG\_STATE\_CONNECTED\_SID\_ENABLED

Instance is connected with session handshake support.

**Definition** icmsg.h:69

[ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6108f7fe29d982a2f52653c4e97205b6)

@ ICMSG\_STATE\_INITIALIZING\_SID\_DISABLED

Instance is initializing without session handshake.

**Definition** icmsg.h:37

[ICMSG\_STATE\_INITIALIZING\_SID\_DETECT](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a6795026f474f701d404e38f5ad4766eb)

@ ICMSG\_STATE\_INITIALIZING\_SID\_DETECT

Instance is initializing with detection of session handshake support on remote side.

**Definition** icmsg.h:50

[ICMSG\_STATE\_OFF](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910a7167bae7aee28ffa39494cb0ca1175b6)

@ ICMSG\_STATE\_OFF

Instance is not initialized yet.

**Definition** icmsg.h:32

[ICMSG\_STATE\_CONNECTED\_SID\_DISABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ac9b07c0dd80a5e4f5029a3984d552bab)

@ ICMSG\_STATE\_CONNECTED\_SID\_DISABLED

Instance is connected without session handshake support.

**Definition** icmsg.h:63

[ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED](group__ipc__icmsg__api.md#ggab26905275fd20a113d1f05d03761f910ae9e45a00a479eb8be2d82ea2ac848dc7)

@ ICMSG\_STATE\_INITIALIZING\_SID\_ENABLED

Instance is initializing with session handshake.

**Definition** icmsg.h:43

[ICMSG\_UNBOUND\_MODE\_DETECT](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa3dbd2f53889c3d5a40948700df4d5f75)

@ ICMSG\_UNBOUND\_MODE\_DETECT

**Definition** icmsg.h:75

[ICMSG\_UNBOUND\_MODE\_ENABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fa644f1bdb89f1e3940909a0269c9fca07)

@ ICMSG\_UNBOUND\_MODE\_ENABLE

**Definition** icmsg.h:74

[ICMSG\_UNBOUND\_MODE\_DISABLE](group__ipc__icmsg__api.md#ggae14e0b81c90a4bb4fc140a48a48d1b5fac688a38231634863b4f3a5baa73de57a)

@ ICMSG\_UNBOUND\_MODE\_DISABLE

**Definition** icmsg.h:73

[ipc\_service.h](ipc__service_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[pbuf.h](pbuf_8h.md)

[stdint.h](stdint_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[icmsg\_config\_t](structicmsg__config__t.md)

**Definition** icmsg.h:78

[icmsg\_config\_t::mbox\_tx](structicmsg__config__t.md#a2d88a58f961bedb4a05360523e0bd181)

struct mbox\_dt\_spec mbox\_tx

**Definition** icmsg.h:79

[icmsg\_config\_t::mbox\_rx](structicmsg__config__t.md#a50a893102c1acf24ea2634ef8bcdae57)

struct mbox\_dt\_spec mbox\_rx

**Definition** icmsg.h:80

[icmsg\_config\_t::unbound\_mode](structicmsg__config__t.md#afdbe5d280cb60eb7cfddd8c7cf27f71b)

enum icmsg\_unbound\_mode unbound\_mode

**Definition** icmsg.h:81

[icmsg\_data\_t](structicmsg__data__t.md)

**Definition** icmsg.h:84

[icmsg\_data\_t::cb](structicmsg__data__t.md#a08ff5a45a78c16a14bf936d47f84f504)

const struct ipc\_service\_cb \* cb

**Definition** icmsg.h:93

[icmsg\_data\_t::remote\_sid](structicmsg__data__t.md#a26c86f7bfa3cc8931051c7239ddddbd5)

uint16\_t remote\_sid

**Definition** icmsg.h:101

[icmsg\_data\_t::local\_sid](structicmsg__data__t.md#a511835de55ae6123ee5b91d66da3d441)

uint16\_t local\_sid

**Definition** icmsg.h:102

[icmsg\_data\_t::cfg](structicmsg__data__t.md#a5b2a3b2d49dbd74fd5cc7e8c9792dc99)

const struct icmsg\_config\_t \* cfg

**Definition** icmsg.h:97

[icmsg\_data\_t::tx\_pb](structicmsg__data__t.md#ac0551d82090f4070c32cfdf99ad9b58b)

struct pbuf \* tx\_pb

**Definition** icmsg.h:86

[icmsg\_data\_t::rx\_pb](structicmsg__data__t.md#ac71b717be840600d70a11c13ff039ff6)

struct pbuf \* rx\_pb

**Definition** icmsg.h:87

[icmsg\_data\_t::ctx](structicmsg__data__t.md#aebbec88dbc8ad410ea1905627c6e9d42)

void \* ctx

**Definition** icmsg.h:94

[icmsg\_data\_t::state](structicmsg__data__t.md#af5962a316ede669331bd34bacabb615a)

atomic\_t state

**Definition** icmsg.h:103

[ipc\_service\_cb](structipc__service__cb.md)

Event callback structure.

**Definition** ipc\_service.h:145

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4006

[mbox\_dt\_spec](structmbox__dt__spec.md)

MBOX specification from DT.

**Definition** mbox.h:87

[pbuf](structpbuf.md)

Scure packed buffer.

**Definition** pbuf.h:99

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [ipc](dir_a601f58076b93c8a02c94df35dc60a45.md)
- [icmsg.h](icmsg_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
