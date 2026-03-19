---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2i2c_2rtio_8h_source.html
original_path: doxygen/html/drivers_2i2c_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h

[Go to the documentation of this file.](drivers_2i2c_2rtio_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_I2C\_RTIO\_H\_

8#define ZEPHYR\_DRIVERS\_I2C\_RTIO\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h.md)>

12#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 21](structi2c__rtio.md)struct [i2c\_rtio](structi2c__rtio.md) {

[ 22](structi2c__rtio.md#a6cc7e4a39d59803334127cf6d2193bd8) struct k\_sem [lock](structi2c__rtio.md#a6cc7e4a39d59803334127cf6d2193bd8);

[ 23](structi2c__rtio.md#a35188f6b135b3feedb1879dd6e0ed76d) struct [k\_spinlock](structk__spinlock.md) [slock](structi2c__rtio.md#a35188f6b135b3feedb1879dd6e0ed76d);

[ 24](structi2c__rtio.md#a984ecd6802234bda30f835e2707571c2) struct [rtio](structrtio.md) \*[r](structi2c__rtio.md#a984ecd6802234bda30f835e2707571c2);

[ 25](structi2c__rtio.md#a35d6b41c23195012c76cf9597f214c60) struct [mpsc](structmpsc.md) [io\_q](structi2c__rtio.md#a35d6b41c23195012c76cf9597f214c60);

[ 26](structi2c__rtio.md#a4d0d75b7f4b9a16b0156386691eb365a) struct [rtio\_iodev](structrtio__iodev.md) [iodev](structi2c__rtio.md#a4d0d75b7f4b9a16b0156386691eb365a);

[ 27](structi2c__rtio.md#aef9f2ffc6128e993d499a4e345c31b05) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_head](structi2c__rtio.md#aef9f2ffc6128e993d499a4e345c31b05);

[ 28](structi2c__rtio.md#abe0c5e8cdebac52f6c5886ead3eabed3) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_curr](structi2c__rtio.md#abe0c5e8cdebac52f6c5886ead3eabed3);

[ 29](structi2c__rtio.md#a962efcae6ce0598bfab3b6fc0a91b467) struct [i2c\_dt\_spec](structi2c__dt__spec.md) [dt\_spec](structi2c__rtio.md#a962efcae6ce0598bfab3b6fc0a91b467);

30};

31

[ 39](drivers_2i2c_2rtio_8h.md#a35c491a1dd04108ec30710d05c5e581c)#define I2C\_RTIO\_DEFINE(\_name, \_sq\_sz, \_cq\_sz) \

40 RTIO\_DEFINE(CONCAT(\_name, \_r), \_sq\_sz, \_cq\_sz); \

41 static struct i2c\_rtio \_name = { \

42 .r = &CONCAT(\_name, \_r), \

43 };

44

[ 51](drivers_2i2c_2rtio_8h.md#a1fc6344eba89f6121c61172698c19093)struct [rtio\_sqe](structrtio__sqe.md) \*[i2c\_rtio\_copy](drivers_2i2c_2rtio_8h.md#a1fc6344eba89f6121c61172698c19093)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), const struct [i2c\_msg](structi2c__msg.md) \*msgs,

52 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs);

53

[ 60](drivers_2i2c_2rtio_8h.md#a27f7ee3efcc8b7077670370862121998)void [i2c\_rtio\_init](drivers_2i2c_2rtio_8h.md#a27f7ee3efcc8b7077670370862121998)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx, const struct [device](structdevice.md) \*dev);

61

[ 71](drivers_2i2c_2rtio_8h.md#a2b1a7d3c9a5c9cfee05cdd1159db2350)bool [i2c\_rtio\_complete](drivers_2i2c_2rtio_8h.md#a2b1a7d3c9a5c9cfee05cdd1159db2350)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx, int status);

72

[ 79](drivers_2i2c_2rtio_8h.md#abe490f290a1c1e42981d7984275883c8)bool [i2c\_rtio\_submit](drivers_2i2c_2rtio_8h.md#abe490f290a1c1e42981d7984275883c8)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

80

[ 89](drivers_2i2c_2rtio_8h.md#ac72265eb9d2ee19de5ba176da59f4cfc)int [i2c\_rtio\_configure](drivers_2i2c_2rtio_8h.md#ac72265eb9d2ee19de5ba176da59f4cfc)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5));

90

[ 99](drivers_2i2c_2rtio_8h.md#a727ef05b9b3fce1b803db521c049ee31)int [i2c\_rtio\_transfer](drivers_2i2c_2rtio_8h.md#a727ef05b9b3fce1b803db521c049ee31)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr);

100

[ 109](drivers_2i2c_2rtio_8h.md#ae8d5f8a031c7aabcf5108760eab06456)int [i2c\_rtio\_recover](drivers_2i2c_2rtio_8h.md#ae8d5f8a031c7aabcf5108760eab06456)(struct [i2c\_rtio](structi2c__rtio.md) \*ctx);

110

111#ifdef \_\_cplusplus

112}

113#endif

114

115#endif /\* ZEPHYR\_DRVIERS\_I2C\_RTIO\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[i2c\_rtio\_copy](drivers_2i2c_2rtio_8h.md#a1fc6344eba89f6121c61172698c19093)

struct rtio\_sqe \* i2c\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct i2c\_msg \*msgs, uint8\_t num\_msgs)

Copy an array of i2c\_msgs to rtio submissions and a transaction.

[i2c\_rtio\_init](drivers_2i2c_2rtio_8h.md#a27f7ee3efcc8b7077670370862121998)

void i2c\_rtio\_init(struct i2c\_rtio \*ctx, const struct device \*dev)

Initialize an i2c rtio context.

[i2c\_rtio\_complete](drivers_2i2c_2rtio_8h.md#a2b1a7d3c9a5c9cfee05cdd1159db2350)

bool i2c\_rtio\_complete(struct i2c\_rtio \*ctx, int status)

Signal that the current (ctx->txn\_curr) submission has been completed.

[i2c\_rtio\_transfer](drivers_2i2c_2rtio_8h.md#a727ef05b9b3fce1b803db521c049ee31)

int i2c\_rtio\_transfer(struct i2c\_rtio \*ctx, struct i2c\_msg \*msgs, uint8\_t num\_msgs, uint16\_t addr)

Transfer i2c messages in a blocking call.

[i2c\_rtio\_submit](drivers_2i2c_2rtio_8h.md#abe490f290a1c1e42981d7984275883c8)

bool i2c\_rtio\_submit(struct i2c\_rtio \*ctx, struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit, atomically, a submission to work on at some point.

[i2c\_rtio\_configure](drivers_2i2c_2rtio_8h.md#ac72265eb9d2ee19de5ba176da59f4cfc)

int i2c\_rtio\_configure(struct i2c\_rtio \*ctx, uint32\_t i2c\_config)

Configure the I2C bus controller.

[i2c\_rtio\_recover](drivers_2i2c_2rtio_8h.md#ae8d5f8a031c7aabcf5108760eab06456)

int i2c\_rtio\_recover(struct i2c\_rtio \*ctx)

Perform an I2C bus recovery in a blocking call.

[i2c.h](drivers_2i2c_8h.md)

Public APIs for the I2C drivers.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[i2c\_dt\_spec](structi2c__dt__spec.md)

Complete I2C DT information.

**Definition** i2c.h:77

[i2c\_msg](structi2c__msg.md)

One I2C Message.

**Definition** i2c.h:184

[i2c\_rtio](structi2c__rtio.md)

Driver context for implementing i2c with rtio.

**Definition** rtio.h:21

[i2c\_rtio::slock](structi2c__rtio.md#a35188f6b135b3feedb1879dd6e0ed76d)

struct k\_spinlock slock

**Definition** rtio.h:23

[i2c\_rtio::io\_q](structi2c__rtio.md#a35d6b41c23195012c76cf9597f214c60)

struct mpsc io\_q

**Definition** rtio.h:25

[i2c\_rtio::iodev](structi2c__rtio.md#a4d0d75b7f4b9a16b0156386691eb365a)

struct rtio\_iodev iodev

**Definition** rtio.h:26

[i2c\_rtio::lock](structi2c__rtio.md#a6cc7e4a39d59803334127cf6d2193bd8)

struct k\_sem lock

**Definition** rtio.h:22

[i2c\_rtio::dt\_spec](structi2c__rtio.md#a962efcae6ce0598bfab3b6fc0a91b467)

struct i2c\_dt\_spec dt\_spec

**Definition** rtio.h:29

[i2c\_rtio::r](structi2c__rtio.md#a984ecd6802234bda30f835e2707571c2)

struct rtio \* r

**Definition** rtio.h:24

[i2c\_rtio::txn\_curr](structi2c__rtio.md#abe0c5e8cdebac52f6c5886ead3eabed3)

struct rtio\_iodev\_sqe \* txn\_curr

**Definition** rtio.h:28

[i2c\_rtio::txn\_head](structi2c__rtio.md#aef9f2ffc6128e993d499a4e345c31b05)

struct rtio\_iodev\_sqe \* txn\_head

**Definition** rtio.h:27

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[mpsc](structmpsc.md)

MPSC Queue.

**Definition** mpsc\_lockfree.h:86

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:429

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:454

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::i2c\_config](structrtio__sqe.md#a07bf344b1b1063b8bea80cf5ba1c1cc5)

uint32\_t i2c\_config

OP\_I2C\_CONFIGURE.

**Definition** rtio.h:288

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:333

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [rtio.h](drivers_2i2c_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
