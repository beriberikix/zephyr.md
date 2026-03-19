---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2i2c_2rtio_8h.html
original_path: doxygen/html/drivers_2i2c_2rtio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/i2c.h](drivers_2i2c_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`

[Go to the source code of this file.](drivers_2i2c_2rtio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i2c\_rtio](structi2c__rtio.md) |
|  | Driver context for implementing i2c with rtio. [More...](structi2c__rtio.md#details) |

| Macros | |
| --- | --- |
| #define | [I2C\_RTIO\_DEFINE](#a35c491a1dd04108ec30710d05c5e581c)(\_name, \_sq\_sz, \_cq\_sz) |
|  | Statically define an [i2c\_rtio](structi2c__rtio.md "Driver context for implementing i2c with rtio.") context. |

| Functions | |
| --- | --- |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [i2c\_rtio\_copy](#a1fc6344eba89f6121c61172698c19093) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Copy an array of i2c\_msgs to rtio submissions and a transaction. |
| void | [i2c\_rtio\_init](#a27f7ee3efcc8b7077670370862121998) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx, const struct [device](structdevice.md) \*dev) |
|  | Initialize an i2c rtio context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_rtio\_complete](#a2b1a7d3c9a5c9cfee05cdd1159db2350) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx, int status) |
|  | Signal that the current (ctx->txn\_curr) submission has been completed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i2c\_rtio\_submit](#abe490f290a1c1e42981d7984275883c8) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit, atomically, a submission to work on at some point. |
| int | [i2c\_rtio\_configure](#ac72265eb9d2ee19de5ba176da59f4cfc) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i2c\_config) |
|  | Configure the I2C bus controller. |
| int | [i2c\_rtio\_transfer](#a727ef05b9b3fce1b803db521c049ee31) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx, struct [i2c\_msg](structi2c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Transfer i2c messages in a blocking call. |
| int | [i2c\_rtio\_recover](#ae8d5f8a031c7aabcf5108760eab06456) (struct [i2c\_rtio](structi2c__rtio.md) \*ctx) |
|  | Perform an I2C bus recovery in a blocking call. |

## Macro Definition Documentation

## [◆ ](#a35c491a1dd04108ec30710d05c5e581c)I2C\_RTIO\_DEFINE

| #define I2C\_RTIO\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_sq\_sz*, |
|  |  |  | *\_cq\_sz* ) |

**Value:**

[RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(\_name, \_r), \_sq\_sz, \_cq\_sz); \

static struct [i2c\_rtio](structi2c__rtio.md) \_name = { \

.r = &[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(\_name, \_r), \

};

[RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)

#define RTIO\_DEFINE(name, sq\_sz, cq\_sz)

Statically define and initialize an RTIO context.

**Definition** rtio.h:836

[CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)

#define CONCAT(...)

Concatenate input arguments.

**Definition** util.h:311

[i2c\_rtio](structi2c__rtio.md)

Driver context for implementing i2c with rtio.

**Definition** rtio.h:21

Statically define an [i2c\_rtio](structi2c__rtio.md "Driver context for implementing i2c with rtio.") context.

Parameters
:   | \_name | Symbolic name of the context |
    | --- | --- |
    | \_sq\_sz | Submission queue entry pool size |
    | \_cq\_sz | Completion queue entry pool size |

## Function Documentation

## [◆ ](#a2b1a7d3c9a5c9cfee05cdd1159db2350)i2c\_rtio\_complete()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i2c\_rtio\_complete | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

Signal that the current (ctx->txn\_curr) submission has been completed.

Parameters
:   | ctx | I2C RTIO driver context |
    | --- | --- |
    | status | Completion status, negative values are errors |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No more submissions to work on |

## [◆ ](#ac72265eb9d2ee19de5ba176da59f4cfc)i2c\_rtio\_configure()

| int i2c\_rtio\_configure | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *i2c\_config* ) |

Configure the I2C bus controller.

Provides a compatible API for the existing i2c\_configure API, and blocks the caller until the transfer completes.

See [i2c\_configure()](group__i2c__interface.md#ga75326a6f38c011d35df9f3e72f2259e9 "Configure operation of a host controller.").

## [◆ ](#a1fc6344eba89f6121c61172698c19093)i2c\_rtio\_copy()

| struct [rtio\_sqe](structrtio__sqe.md) \* i2c\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
|  |  | const struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) |

Copy an array of i2c\_msgs to rtio submissions and a transaction.

Return values
:   | sqe | Last sqe setup in the copy |
    | --- | --- |
    | NULL | Not enough memory to copy the transaction |

## [◆ ](#a27f7ee3efcc8b7077670370862121998)i2c\_rtio\_init()

| void i2c\_rtio\_init | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *dev* ) |

Initialize an i2c rtio context.

Parameters
:   | ctx | I2C RTIO driver context |
    | --- | --- |
    | dev | I2C bus |

## [◆ ](#ae8d5f8a031c7aabcf5108760eab06456)i2c\_rtio\_recover()

| int i2c\_rtio\_recover | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Perform an I2C bus recovery in a blocking call.

Provides a compatible API for the existing i2c\_recover API, and blocks the caller until the process completes.

See i2c\_recover().

## [◆ ](#abe490f290a1c1e42981d7984275883c8)i2c\_rtio\_submit()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i2c\_rtio\_submit | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

Submit, atomically, a submission to work on at some point.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No new submission to start or submissions are in progress already |

## [◆ ](#a727ef05b9b3fce1b803db521c049ee31)i2c\_rtio\_transfer()

| int i2c\_rtio\_transfer | ( | struct [i2c\_rtio](structi2c__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [i2c\_msg](structi2c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) |

Transfer i2c messages in a blocking call.

Provides a compatible API for the existing i2c\_transfer API, and blocks the caller until the transfer completes.

See [i2c\_transfer()](group__i2c__interface.md#ga2958e6fe92ffb17851052d5c9a5c058e "Perform data transfer to another I2C device in controller mode.").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2c](dir_d0e9f61c1b95aed307ec1c726ffb3f96.md)
- [rtio.h](drivers_2i2c_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
