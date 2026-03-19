---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2spi_2rtio_8h_source.html
original_path: doxygen/html/drivers_2spi_2rtio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h

[Go to the documentation of this file.](drivers_2spi_2rtio_8h.md)

1/\*

2 \* Copyright (c) 2024 Croxel, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DRIVERS\_SPI\_RTIO\_H\_

8#define ZEPHYR\_DRIVERS\_SPI\_RTIO\_H\_

9

10#include <[zephyr/kernel.h](kernel_8h.md)>

11#include <[zephyr/drivers/spi.h](drivers_2spi_8h.md)>

12#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 21](structspi__rtio.md)struct [spi\_rtio](structspi__rtio.md) {

[ 22](structspi__rtio.md#a57d4533fa5b8939cdb8ddb6ab8dfada2) struct [k\_spinlock](structk__spinlock.md) [lock](structspi__rtio.md#a57d4533fa5b8939cdb8ddb6ab8dfada2);

[ 23](structspi__rtio.md#a7438ee10b82f0c31f3cb4f40384e7d11) struct [rtio](structrtio.md) \*[r](structspi__rtio.md#a7438ee10b82f0c31f3cb4f40384e7d11);

[ 24](structspi__rtio.md#afa7ca567196334bf8dc768c69697b79b) struct [mpsc](structmpsc.md) [io\_q](structspi__rtio.md#afa7ca567196334bf8dc768c69697b79b);

[ 25](structspi__rtio.md#a16fa5e36ced62e267bae60faa1230392) struct [rtio\_iodev](structrtio__iodev.md) [iodev](structspi__rtio.md#a16fa5e36ced62e267bae60faa1230392);

[ 26](structspi__rtio.md#a2688d4999533c55e7d6a052b579d5a4b) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_head](structspi__rtio.md#a2688d4999533c55e7d6a052b579d5a4b);

[ 27](structspi__rtio.md#add2905749d8c26f7aedd29bcef27dff0) struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[txn\_curr](structspi__rtio.md#add2905749d8c26f7aedd29bcef27dff0);

[ 28](structspi__rtio.md#a8ea13c0000663a846f3d131a92d5c9ce) struct [spi\_dt\_spec](structspi__dt__spec.md) [dt\_spec](structspi__rtio.md#a8ea13c0000663a846f3d131a92d5c9ce);

29};

30

[ 38](drivers_2spi_2rtio_8h.md#a28c0b0e27872480db3787458b6fbe00d)#define SPI\_RTIO\_DEFINE(\_name, \_sq\_sz, \_cq\_sz) \

39 RTIO\_DEFINE(CONCAT(\_name, \_r), \_sq\_sz, \_cq\_sz); \

40 static struct spi\_rtio \_name = { \

41 .r = &CONCAT(\_name, \_r), \

42 };

43

[ 56](drivers_2spi_2rtio_8h.md#a480b74835587c6c043c9c5f734dbf419)int [spi\_rtio\_copy](drivers_2spi_2rtio_8h.md#a480b74835587c6c043c9c5f734dbf419)(struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2),

57 struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

58 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

59 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs,

60 struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe);

61

[ 68](drivers_2spi_2rtio_8h.md#a2aea05f774dbbe07e57ed7f36ae795ae)void [spi\_rtio\_init](drivers_2spi_2rtio_8h.md#a2aea05f774dbbe07e57ed7f36ae795ae)(struct [spi\_rtio](structspi__rtio.md) \*ctx, const struct [device](structdevice.md) \*dev);

69

[ 79](drivers_2spi_2rtio_8h.md#a3afeeb25a4762f8af9b2b339531ae290)bool [spi\_rtio\_complete](drivers_2spi_2rtio_8h.md#a3afeeb25a4762f8af9b2b339531ae290)(struct [spi\_rtio](structspi__rtio.md) \*ctx, int status);

80

[ 87](drivers_2spi_2rtio_8h.md#a2a2242f192351f81490c3e6114d4faf3)bool [spi\_rtio\_submit](drivers_2spi_2rtio_8h.md#a2a2242f192351f81490c3e6114d4faf3)(struct [spi\_rtio](structspi__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

88

[ 96](drivers_2spi_2rtio_8h.md#ae18ee5f4aafc7c3ce65c987cf2b118b4)int [spi\_rtio\_transceive](drivers_2spi_2rtio_8h.md#ae18ee5f4aafc7c3ce65c987cf2b118b4)(struct [spi\_rtio](structspi__rtio.md) \*ctx,

97 const struct [spi\_config](structspi__config.md) \*[config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e),

98 const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs,

99 const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs);

100

[ 107](drivers_2spi_2rtio_8h.md#ad5091a20de8f3fcf52ea8e872607fdf3)void [spi\_rtio\_iodev\_default\_submit](drivers_2spi_2rtio_8h.md#ad5091a20de8f3fcf52ea8e872607fdf3)(const struct [device](structdevice.md) \*dev,

108 struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe);

109

110#ifdef \_\_cplusplus

111}

112#endif

113

114#endif /\* ZEPHYR\_DRIVERS\_SPI\_RTIO\_H\_ \*/

[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)

workaround assembler barfing for ST r

**Definition** asm-macro-32-bit-gnu.h:24

[spi\_rtio\_submit](drivers_2spi_2rtio_8h.md#a2a2242f192351f81490c3e6114d4faf3)

bool spi\_rtio\_submit(struct spi\_rtio \*ctx, struct rtio\_iodev\_sqe \*iodev\_sqe)

Submit, atomically, a submission to work on at some point.

[spi\_rtio\_init](drivers_2spi_2rtio_8h.md#a2aea05f774dbbe07e57ed7f36ae795ae)

void spi\_rtio\_init(struct spi\_rtio \*ctx, const struct device \*dev)

Initialize a SPI RTIO context.

[spi\_rtio\_complete](drivers_2spi_2rtio_8h.md#a3afeeb25a4762f8af9b2b339531ae290)

bool spi\_rtio\_complete(struct spi\_rtio \*ctx, int status)

Signal that the current (ctx->txn\_curr) submission has been completed.

[spi\_rtio\_copy](drivers_2spi_2rtio_8h.md#a480b74835587c6c043c9c5f734dbf419)

int spi\_rtio\_copy(struct rtio \*r, struct rtio\_iodev \*iodev, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs, struct rtio\_sqe \*\*last\_sqe)

Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

[spi\_rtio\_iodev\_default\_submit](drivers_2spi_2rtio_8h.md#ad5091a20de8f3fcf52ea8e872607fdf3)

void spi\_rtio\_iodev\_default\_submit(const struct device \*dev, struct rtio\_iodev\_sqe \*iodev\_sqe)

Fallback SPI RTIO submit implementation.

[spi\_rtio\_transceive](drivers_2spi_2rtio_8h.md#ae18ee5f4aafc7c3ce65c987cf2b118b4)

int spi\_rtio\_transceive(struct spi\_rtio \*ctx, const struct spi\_config \*config, const struct spi\_buf\_set \*tx\_bufs, const struct spi\_buf\_set \*rx\_bufs)

Perform a SPI Transfer (transceive) in a blocking call.

[spi.h](drivers_2spi_8h.md)

Public API for SPI drivers and applications.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[rtio.h](rtio_2rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

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

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:396

[spi\_buf\_set](structspi__buf__set.md)

SPI buffer array structure.

**Definition** spi.h:471

[spi\_config](structspi__config.md)

SPI controller configuration structure.

**Definition** spi.h:301

[spi\_dt\_spec](structspi__dt__spec.md)

Complete SPI DT information.

**Definition** spi.h:377

[spi\_dt\_spec::config](structspi__dt__spec.md#a88372c17ede2e9dfb0c09c49abebf87e)

struct spi\_config config

Slave specific configuration.

**Definition** spi.h:381

[spi\_rtio](structspi__rtio.md)

Driver context for implementing SPI with RTIO.

**Definition** rtio.h:21

[spi\_rtio::iodev](structspi__rtio.md#a16fa5e36ced62e267bae60faa1230392)

struct rtio\_iodev iodev

**Definition** rtio.h:25

[spi\_rtio::txn\_head](structspi__rtio.md#a2688d4999533c55e7d6a052b579d5a4b)

struct rtio\_iodev\_sqe \* txn\_head

**Definition** rtio.h:26

[spi\_rtio::lock](structspi__rtio.md#a57d4533fa5b8939cdb8ddb6ab8dfada2)

struct k\_spinlock lock

**Definition** rtio.h:22

[spi\_rtio::r](structspi__rtio.md#a7438ee10b82f0c31f3cb4f40384e7d11)

struct rtio \* r

**Definition** rtio.h:23

[spi\_rtio::dt\_spec](structspi__rtio.md#a8ea13c0000663a846f3d131a92d5c9ce)

struct spi\_dt\_spec dt\_spec

**Definition** rtio.h:28

[spi\_rtio::txn\_curr](structspi__rtio.md#add2905749d8c26f7aedd29bcef27dff0)

struct rtio\_iodev\_sqe \* txn\_curr

**Definition** rtio.h:27

[spi\_rtio::io\_q](structspi__rtio.md#afa7ca567196334bf8dc768c69697b79b)

struct mpsc io\_q

**Definition** rtio.h:24

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi](dir_6e08514149e6bc13232e2a845363c07c.md)
- [rtio.h](drivers_2spi_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
