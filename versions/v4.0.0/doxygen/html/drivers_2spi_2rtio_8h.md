---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2spi_2rtio_8h.html
original_path: doxygen/html/drivers_2spi_2rtio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/drivers/spi.h](drivers_2spi_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`

[Go to the source code of this file.](drivers_2spi_2rtio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [spi\_rtio](structspi__rtio.md) |
|  | Driver context for implementing SPI with RTIO. [More...](structspi__rtio.md#details) |

| Macros | |
| --- | --- |
| #define | [SPI\_RTIO\_DEFINE](#a28c0b0e27872480db3787458b6fbe00d)(\_name, \_sq\_sz, \_cq\_sz) |
|  | Statically define a [spi\_rtio](structspi__rtio.md "Driver context for implementing SPI with RTIO.") context. |

| Functions | |
| --- | --- |
| int | [spi\_rtio\_copy](#a480b74835587c6c043c9c5f734dbf419) (struct [rtio](structrtio.md) \*[r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2), struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs, struct [rtio\_sqe](structrtio__sqe.md) \*\*last\_sqe) |
|  | Copy the tx\_bufs and rx\_bufs into a set of RTIO requests. |
| void | [spi\_rtio\_init](#a2aea05f774dbbe07e57ed7f36ae795ae) (struct [spi\_rtio](structspi__rtio.md) \*ctx, const struct [device](structdevice.md) \*dev) |
|  | Initialize a SPI RTIO context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_rtio\_complete](#a3afeeb25a4762f8af9b2b339531ae290) (struct [spi\_rtio](structspi__rtio.md) \*ctx, int status) |
|  | Signal that the current (ctx->txn\_curr) submission has been completed. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [spi\_rtio\_submit](#a2a2242f192351f81490c3e6114d4faf3) (struct [spi\_rtio](structspi__rtio.md) \*ctx, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Submit, atomically, a submission to work on at some point. |
| int | [spi\_rtio\_transceive](#ae18ee5f4aafc7c3ce65c987cf2b118b4) (struct [spi\_rtio](structspi__rtio.md) \*ctx, const struct [spi\_config](structspi__config.md) \*config, const struct [spi\_buf\_set](structspi__buf__set.md) \*tx\_bufs, const struct [spi\_buf\_set](structspi__buf__set.md) \*rx\_bufs) |
|  | Perform a SPI Transfer (transceive) in a blocking call. |
| void | [spi\_rtio\_iodev\_default\_submit](#ad5091a20de8f3fcf52ea8e872607fdf3) (const struct [device](structdevice.md) \*dev, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Fallback SPI RTIO submit implementation. |

## Macro Definition Documentation

## [◆ ](#a28c0b0e27872480db3787458b6fbe00d)SPI\_RTIO\_DEFINE

| #define SPI\_RTIO\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_sq\_sz*, |
|  |  |  | *\_cq\_sz* ) |

**Value:**

[RTIO\_DEFINE](group__rtio.md#ga338df088eabf3b8f7fefb4ac517b21d4)([CONCAT](group__sys-util.md#ga770b921e59b3151931ee939a1ecf450e)(\_name, \_r), \_sq\_sz, \_cq\_sz); \

static struct [spi\_rtio](structspi__rtio.md) \_name = { \

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

[spi\_rtio](structspi__rtio.md)

Driver context for implementing SPI with RTIO.

**Definition** rtio.h:21

Statically define a [spi\_rtio](structspi__rtio.md "Driver context for implementing SPI with RTIO.") context.

Parameters
:   | \_name | Symbolic name of the context |
    | --- | --- |
    | \_sq\_sz | Submission queue entry pool size |
    | \_cq\_sz | Completion queue entry pool size |

## Function Documentation

## [◆ ](#a3afeeb25a4762f8af9b2b339531ae290)spi\_rtio\_complete()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_rtio\_complete | ( | struct [spi\_rtio](structspi__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | int | *status* ) |

Signal that the current (ctx->txn\_curr) submission has been completed.

Parameters
:   | ctx | SPI RTIO driver context |
    | --- | --- |
    | status | Completion status, negative values are errors |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No more submissions to work on |

## [◆ ](#a480b74835587c6c043c9c5f734dbf419)spi\_rtio\_copy()

| int spi\_rtio\_copy | ( | struct [rtio](structrtio.md) \* | *r*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev](structrtio__iodev.md) \* | *iodev*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs*, |
|  |  | struct [rtio\_sqe](structrtio__sqe.md) \*\* | *last\_sqe* ) |

Copy the tx\_bufs and rx\_bufs into a set of RTIO requests.

Parameters
:   | [in] | [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2) | rtio context |
    | --- | --- | --- |
    | [in] | iodev | iodev to transceive with |
    | [in] | tx\_bufs | transmit buffer set |
    | [in] | rx\_bufs | receive buffer set |
    | [out] | last\_sqe | last sqe submitted, NULL if not enough memory |

Return values
:   | Number | of submission queue entries |
    | --- | --- |
    | -ENOMEM | out of memory |

## [◆ ](#a2aea05f774dbbe07e57ed7f36ae795ae)spi\_rtio\_init()

| void spi\_rtio\_init | ( | struct [spi\_rtio](structspi__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *dev* ) |

Initialize a SPI RTIO context.

Parameters
:   | ctx | SPI RTIO driver context |
    | --- | --- |
    | dev | SPI bus |

## [◆ ](#ad5091a20de8f3fcf52ea8e872607fdf3)spi\_rtio\_iodev\_default\_submit()

| void spi\_rtio\_iodev\_default\_submit | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

Fallback SPI RTIO submit implementation.

Default RTIO SPI implementation for drivers who do no yet have native support. For details, see [spi\_iodev\_submit](group__spi__interface.md#ga8b23855bdc7dab7d02b8f7daa7db651b "spi_iodev_submit").

## [◆ ](#a2a2242f192351f81490c3e6114d4faf3)spi\_rtio\_submit()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) spi\_rtio\_submit | ( | struct [spi\_rtio](structspi__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe* ) |

Submit, atomically, a submission to work on at some point.

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Next submission is ready to start |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | No new submission to start or submissions are in progress already |

## [◆ ](#ae18ee5f4aafc7c3ce65c987cf2b118b4)spi\_rtio\_transceive()

| int spi\_rtio\_transceive | ( | struct [spi\_rtio](structspi__rtio.md) \* | *ctx*, |
| --- | --- | --- | --- |
|  |  | const struct [spi\_config](structspi__config.md) \* | *config*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *tx\_bufs*, |
|  |  | const struct [spi\_buf\_set](structspi__buf__set.md) \* | *rx\_bufs* ) |

Perform a SPI Transfer (transceive) in a blocking call.

Provides a compatible API for the existing spi\_transceive API by blocking the caller until the operation is complete. For details see [spi\_transceive](group__spi__interface.md#gad51054c1ba259db5a64619788506a6f5 "spi_transceive").

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [spi](dir_6e08514149e6bc13232e2a845363c07c.md)
- [rtio.h](drivers_2spi_2rtio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
