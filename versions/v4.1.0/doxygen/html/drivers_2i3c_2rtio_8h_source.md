---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2i3c_2rtio_8h_source.html
original_path: doxygen/html/drivers_2i3c_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h

[Go to the documentation of this file.](drivers_2i3c_2rtio_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \* Copyright (c) 2024 Meta Platforms

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef ZEPHYR\_DRIVERS\_I3C\_RTIO\_H\_

9#define ZEPHYR\_DRIVERS\_I3C\_RTIO\_H\_

10

11#include <[zephyr/kernel.h](kernel_8h.md)>

12#include <[zephyr/drivers/i3c.h](i3c_8h.md)>

13#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

[ 22](structi3c__rtio.md)struct [i3c\_rtio](structi3c__rtio.md) {

[ 23](structi3c__rtio.md#af72118faec547f438b213aff87d5de50) struct k\_sem [lock](structi3c__rtio.md#af72118faec547f438b213aff87d5de50);

[ 24](structi3c__rtio.md#a4ded14f281371d0daa3e7dcf477ab0c9) struct [k\_spinlock](structk__spinlock.md) [slock](structi3c__rtio.md#a4ded14f281371d0daa3e7dcf477ab0c9);

[ 25](structi3c__rtio.md#a9e084adb1e963cd713165c4404aabe5f) struct [rtio](structrtio.md) \*[r](structi3c__rtio.md#a9e084adb1e963cd713165c4404aabe5f);

[ 26](structi3c__rtio.md#ac8f7b2b24c07147d886c307e7af99d4d) struct [mpsc](structmpsc.md) [io\_q](structi3c__rtio.md#ac8f7b2b24c07147d886c307e7af99d4d);

[ 27](structi3c__rtio.md#a1c73add1e0c1dbf67a5c7a6e4ee1e507) struct [rtio\_iodev](structrtio__iodev.md) [iodev](structi3c__rtio.md#a1c73add1e0c1dbf67a5c7a6e4ee1e507);

[ 28](structi3c__rtio.md#aea9fa855d6fd273cf672bf440027adb6) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_head](structi3c__rtio.md#aea9fa855d6fd273cf672bf440027adb6);

[ 29](structi3c__rtio.md#a70a6f131830ffcb274cf6fdabafb6222) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_curr](structi3c__rtio.md#a70a6f131830ffcb274cf6fdabafb6222);

[ 30](structi3c__rtio.md#a24da09d1b6ba078444952566efb9bdbd) struct [i3c\_device\_desc](structi3c__device__desc.md) \*[i3c\_desc](structi3c__rtio.md#a24da09d1b6ba078444952566efb9bdbd);

31};

32

[ 40](drivers_2i3c_2rtio_8h.md#a58b045562d60115161e271a504579a97)#define I3C\_RTIO\_DEFINE(\_name, \_sq\_sz, \_cq\_sz) \

41 RTIO\_DEFINE(CONCAT(\_name, \_r), \_sq\_sz, \_cq\_sz); \

42 static struct i3c\_rtio \_name = { \

43 .r = &CONCAT(\_name, \_r), \

44 };

45

[ 52](drivers_2i3c_2rtio_8h.md#ab46a231442a7bf60e7e28ca2f52d25fc)struct [rtio\_sqe](structrtio__sqe.md) \*[i3c\_rtio\_copy](drivers_2i3c_2rtio_8h.md#ab46a231442a7bf60e7e28ca2f52d25fc)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), const struct [i3c\_msg](structi3c__msg.md) \*msgs,

53 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

54

[ 60](drivers_2i3c_2rtio_8h.md#a31565a85572a08e4b512a5eaafc927e5)void [i3c\_rtio\_init](drivers_2i3c_2rtio_8h.md#a31565a85572a08e4b512a5eaafc927e5)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx);

61

[ 71](drivers_2i3c_2rtio_8h.md#a30a631aef874142d8d23f4e296627ec2)bool [i3c\_rtio\_complete](drivers_2i3c_2rtio_8h.md#a30a631aef874142d8d23f4e296627ec2)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx, int status);

72

[ 79](drivers_2i3c_2rtio_8h.md#a1b371f3c804015178b3520f06db3f5eb)bool [i3c\_rtio\_submit](drivers_2i3c_2rtio_8h.md#a1b371f3c804015178b3520f06db3f5eb)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

80

[ 89](drivers_2i3c_2rtio_8h.md#a218d54c01b742a829958c5f05fd367c0)int [i3c\_rtio\_configure](drivers_2i3c_2rtio_8h.md#a218d54c01b742a829958c5f05fd367c0)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx, enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) [type](structrtio__sqe.md#aa09a0c93a6e8cfc73278a87942e4af33), void \*[config](structrtio__sqe.md#ac07a16c50a067acc90bd4ab08aae4184));

90

[ 99](drivers_2i3c_2rtio_8h.md#a68b11ee8bd65063b453f4ac73d6699da)int [i3c\_rtio\_transfer](drivers_2i3c_2rtio_8h.md#a68b11ee8bd65063b453f4ac73d6699da)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs,

100 struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc);

101

[ 110](drivers_2i3c_2rtio_8h.md#ae6dccc320bd87a95e541308f2a358df3)int [i3c\_rtio\_recover](drivers_2i3c_2rtio_8h.md#ae6dccc320bd87a95e541308f2a358df3)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx);

111

[ 120](drivers_2i3c_2rtio_8h.md#aa1d010cf1ae98362d320639c0f52760b)int [i3c\_rtio\_ccc](drivers_2i3c_2rtio_8h.md#aa1d010cf1ae98362d320639c0f52760b)(struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload);

121

122#ifdef \_\_cplusplus

123}

124#endif

125

126#endif /\* ZEPHYR\_DRVIERS\_I3C\_RTIO\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[i3c\_rtio\_submit](drivers_2i3c_2rtio_8h.md#a1b371f3c804015178b3520f06db3f5eb)

bool i3c\_rtio\_submit(struct i3c\_rtio \*ctx, struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit, atomically, a submission to work on at some point.

[i3c\_rtio\_configure](drivers_2i3c_2rtio_8h.md#a218d54c01b742a829958c5f05fd367c0)

int i3c\_rtio\_configure(struct i3c\_rtio \*ctx, enum i3c\_config\_type type, void \*config)

Configure the I3C bus controller.

[i3c\_rtio\_complete](drivers_2i3c_2rtio_8h.md#a30a631aef874142d8d23f4e296627ec2)

bool i3c\_rtio\_complete(struct i3c\_rtio \*ctx, int status)

Signal that the current (ctx->txn\_curr) submission has been completed.

[i3c\_rtio\_init](drivers_2i3c_2rtio_8h.md#a31565a85572a08e4b512a5eaafc927e5)

void i3c\_rtio\_init(struct i3c\_rtio \*ctx)

Initialize an i3c rtio context.

[i3c\_rtio\_transfer](drivers_2i3c_2rtio_8h.md#a68b11ee8bd65063b453f4ac73d6699da)

int i3c\_rtio\_transfer(struct i3c\_rtio \*ctx, struct i3c\_msg \*msgs, uint8\_t num\_msgs, struct i3c\_device\_desc \*desc)

Transfer i3c messages in a blocking call.

[i3c\_rtio\_ccc](drivers_2i3c_2rtio_8h.md#aa1d010cf1ae98362d320639c0f52760b)

int i3c\_rtio\_ccc(struct i3c\_rtio \*ctx, struct i3c\_ccc\_payload \*payload)

Perform an I3C CCC in a blocking call.

[i3c\_rtio\_copy](drivers_2i3c_2rtio_8h.md#ab46a231442a7bf60e7e28ca2f52d25fc)

struct rtio\_sqe \* i3c\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Copy an array of i3c\_msgs to rtio submissions and a transaction.

[i3c\_rtio\_recover](drivers_2i3c_2rtio_8h.md#ae6dccc320bd87a95e541308f2a358df3)

int i3c\_rtio\_recover(struct i3c\_rtio \*ctx)

Perform an I3C bus recovery in a blocking call.

[i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a)

i3c\_config\_type

Type of configuration being passed to configure function.

**Definition** i3c.h:437

[i3c.h](i3c_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[i3c\_ccc\_payload](structi3c__ccc__payload.md)

Payload structure for one CCC transaction.

**Definition** ccc.h:275

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:888

[i3c\_msg](structi3c__msg.md)

One I3C Message.

**Definition** i3c.h:393

[i3c\_rtio](structi3c__rtio.md)

Driver context for implementing i3c with rtio.

**Definition** rtio.h:22

[i3c\_rtio::iodev](structi3c__rtio.md#a1c73add1e0c1dbf67a5c7a6e4ee1e507)

struct rtio\_iodev iodev

**Definition** rtio.h:27

[i3c\_rtio::i3c\_desc](structi3c__rtio.md#a24da09d1b6ba078444952566efb9bdbd)

struct i3c\_device\_desc \* i3c\_desc

**Definition** rtio.h:30

[i3c\_rtio::slock](structi3c__rtio.md#a4ded14f281371d0daa3e7dcf477ab0c9)

struct k\_spinlock slock

**Definition** rtio.h:24

[i3c\_rtio::txn\_curr](structi3c__rtio.md#a70a6f131830ffcb274cf6fdabafb6222)

struct rtio\_iodev\_sqe \* txn\_curr

**Definition** rtio.h:29

[i3c\_rtio::r](structi3c__rtio.md#a9e084adb1e963cd713165c4404aabe5f)

struct rtio \* r

**Definition** rtio.h:25

[i3c\_rtio::io\_q](structi3c__rtio.md#ac8f7b2b24c07147d886c307e7af99d4d)

struct mpsc io\_q

**Definition** rtio.h:26

[i3c\_rtio::txn\_head](structi3c__rtio.md#aea9fa855d6fd273cf672bf440027adb6)

struct rtio\_iodev\_sqe \* txn\_head

**Definition** rtio.h:28

[i3c\_rtio::lock](structi3c__rtio.md#af72118faec547f438b213aff87d5de50)

struct k\_sem lock

**Definition** rtio.h:23

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[mpsc](structmpsc.md)

MPSC Queue.

**Definition** mpsc\_lockfree.h:86

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:492

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:517

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:286

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:295

[rtio\_sqe::type](structrtio__sqe.md#aa09a0c93a6e8cfc73278a87942e4af33)

int type

**Definition** rtio.h:345

[rtio\_sqe::config](structrtio__sqe.md#ac07a16c50a067acc90bd4ab08aae4184)

void \* config

**Definition** rtio.h:346

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:396

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [rtio.h](drivers_2i3c_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
