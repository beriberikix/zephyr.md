---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2i3c_2rtio_8h.html
original_path: doxygen/html/drivers_2i3c_2rtio_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/i3c.h](i3c_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`

[Go to the source code of this file.](drivers_2i3c_2rtio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_rtio](structi3c__rtio.md) |
|  | Driver context for implementing i3c with rtio. [More...](structi3c__rtio.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_RTIO\_DEFINE](#a58b045562d60115161e271a504579a97)(\_name, \_sq\_sz, \_cq\_sz) |
|  | Statically define an [i3c\_rtio](structi3c__rtio.md "Driver context for implementing i3c with rtio.") context. |

| Functions | |
| --- | --- |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [i3c\_rtio\_copy](#ab46a231442a7bf60e7e28ca2f52d25fc) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Copy an array of i3c\_msgs to rtio submissions and a transaction. |
| void | [i3c\_rtio\_init](#a31565a85572a08e4b512a5eaafc927e5) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx) |
|  | Initialize an i3c rtio context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_rtio\_complete](#a30a631aef874142d8d23f4e296627ec2) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx, int status) |
|  | Signal that the current (ctx->txn\_curr) submission has been completed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_rtio\_submit](#a1b371f3c804015178b3520f06db3f5eb) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit, atomically, a submission to work on at some point. |
| int | [i3c\_rtio\_configure](#a218d54c01b742a829958c5f05fd367c0) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx, enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) type, void \*config) |
|  | Configure the I3C bus controller. |
| int | [i3c\_rtio\_transfer](#a68b11ee8bd65063b453f4ac73d6699da) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*desc) |
|  | Transfer i3c messages in a blocking call. |
| int | [i3c\_rtio\_recover](#ae6dccc320bd87a95e541308f2a358df3) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx) |
|  | Perform an I3C bus recovery in a blocking call. |
| int | [i3c\_rtio\_ccc](#aa1d010cf1ae98362d320639c0f52760b) (struct [i3c\_rtio](structi3c__rtio.md) \*ctx, struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload) |
|  | Perform an I3C CCC in a blocking call. |

## Macro Definition Documentation

## [◆ ](#a58b045562d60115161e271a504579a97)I3C\_RTIO\_DEFINE

| #define I3C\_RTIO\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_sq\_sz*, |
|  |  |  | *\_cq\_sz* ) |

**Value:**

[RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(\_name, \_r), \_sq\_sz, \_cq\_sz); \

static struct [i3c\_rtio](structi3c__rtio.md) \_name = { \

.r = &[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(\_name, \_r), \

};

[RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)

#define RTIO\_DEFINE(name, sq\_sz, cq\_sz)

Statically define and initialize an RTIO context.

**Definition** rtio.h:908

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)

#define CONCAT(...)

Concatenate input arguments.

**Definition** util.h:311

[i3c\_rtio](structi3c__rtio.md)

Driver context for implementing i3c with rtio.

**Definition** rtio.h:22

Statically define an [i3c\_rtio](structi3c__rtio.md "Driver context for implementing i3c with rtio.") context.

Parameters
:   | \_name | Symbolic name of the context |
    | --- | --- |
    | \_sq\_sz | Submission queue entry pool size |
    | \_cq\_sz | Completion queue entry pool size |

## Function Documentation

## [◆ ](#aa1d010cf1ae98362d320639c0f52760b)i3c\_rtio\_ccc()

| int i3c\_rtio\_ccc | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \* | *payload* ) |

Perform an I3C CCC in a blocking call.

Provides a compatible API for the existing i3c\_do\_ccc API, and blocks the caller until the process completes.

See [i3c\_do\_ccc()](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.").

## [◆ ](#a30a631aef874142d8d23f4e296627ec2)i3c\_rtio\_complete()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_rtio\_complete | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

Signal that the current (ctx->txn\_curr) submission has been completed.

Parameters
:   | ctx | I3C RTIO driver context |
    | --- | --- |
    | status | Completion status, negative values are errors |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No more submissions to work on |

## [◆ ](#a218d54c01b742a829958c5f05fd367c0)i3c\_rtio\_configure()

| int i3c\_rtio\_configure | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | enum [i3c\_config\_type](group__i3c__interface.md#ga5b111bc8fa8c3bee052e621d26dcc54a) | *type*, |
|  |  | void \* | *config* ) |

Configure the I3C bus controller.

Provides a compatible API for the existing i3c\_configure API, and blocks the caller until the transfer completes.

See [i3c\_configure()](group__i3c__interface.md#ga2f176f8440d86f4ec6c94a8911a75352 "Configure the I3C hardware.").

## [◆ ](#ab46a231442a7bf60e7e28ca2f52d25fc)i3c\_rtio\_copy()

| struct [rtio\_sqe](structrtio__sqe.md) \* i3c\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
|  |  | const struct [i3c\_msg](structi3c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) |

Copy an array of i3c\_msgs to rtio submissions and a transaction.

Return values
:   | sqe | Last sqe setup in the copy |
    | --- | --- |
    | [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) | Not enough memory to copy the transaction |

## [◆ ](#a31565a85572a08e4b512a5eaafc927e5)i3c\_rtio\_init()

| void i3c\_rtio\_init | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize an i3c rtio context.

Parameters
:   | ctx | I3C RTIO driver context |
    | --- | --- |

## [◆ ](#ae6dccc320bd87a95e541308f2a358df3)i3c\_rtio\_recover()

| int i3c\_rtio\_recover | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Perform an I3C bus recovery in a blocking call.

Provides a compatible API for the existing i3c\_recover API, and blocks the caller until the process completes.

See i3c\_recover().

## [◆ ](#a1b371f3c804015178b3520f06db3f5eb)i3c\_rtio\_submit()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_rtio\_submit | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

Submit, atomically, a submission to work on at some point.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No new submission to start or submissions are in progress already |

## [◆ ](#a68b11ee8bd65063b453f4ac73d6699da)i3c\_rtio\_transfer()

| int i3c\_rtio\_transfer | ( | struct [i3c\_rtio](structi3c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_msg](structi3c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, |
|  |  | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *desc* ) |

Transfer i3c messages in a blocking call.

Provides a compatible API for the existing i3c\_transfer API, and blocks the caller until the transfer completes.

See [i3c\_transfer()](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8 "Perform data transfer from the controller to a I3C target device.").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [rtio.h](drivers_2i3c_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
