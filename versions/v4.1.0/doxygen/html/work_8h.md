---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/work_8h.html
original_path: doxygen/html/work_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

work.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h_source.md)>`  
`#include <[zephyr/sys/p4wq.h](p4wq_8h_source.md)>`

[Go to the source code of this file.](work_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [rtio\_work\_req](structrtio__work__req.md) |
|  | RTIO Work request. [More...](structrtio__work__req.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [rtio\_work\_submit\_t](#add537a23ac061970d890f65d76f5f906)) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
|  | Callback API to execute work operation. |

| Functions | |
| --- | --- |
| struct [rtio\_work\_req](structrtio__work__req.md) \* | [rtio\_work\_req\_alloc](#a705ee008834f10bd4b2ef26e67e1c87f) (void) |
|  | Allocate item to perform an RTIO work request. |
| void | [rtio\_work\_req\_submit](#a62035ecd9def621b4e70b699d9027140) (struct [rtio\_work\_req](structrtio__work__req.md) \*req, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe, [rtio\_work\_submit\_t](#add537a23ac061970d890f65d76f5f906) handler) |
|  | Submit RTIO work request. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rtio\_work\_req\_used\_count\_get](#a352516812e7bc88b61cceb2f69d9fd3f) (void) |
|  | Obtain number of currently used items from the pre-allocated pool. |

## Typedef Documentation

## [◆ ](#add537a23ac061970d890f65d76f5f906)rtio\_work\_submit\_t

| typedef void(\* rtio\_work\_submit\_t) (struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*iodev\_sqe) |
| --- |

Callback API to execute work operation.

Parameters
:   | iodev\_sqe | Associated SQE operation. |
    | --- | --- |

## Function Documentation

## [◆ ](#a705ee008834f10bd4b2ef26e67e1c87f)rtio\_work\_req\_alloc()

| struct [rtio\_work\_req](structrtio__work__req.md) \* rtio\_work\_req\_alloc | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Allocate item to perform an RTIO work request.

This allocation utilizes its internal memory slab with pre-allocated elements.

Returns
:   Pointer to allocated item if successful.
:   NULL if allocation failed.

## [◆ ](#a62035ecd9def621b4e70b699d9027140)rtio\_work\_req\_submit()

| void rtio\_work\_req\_submit | ( | struct [rtio\_work\_req](structrtio__work__req.md) \* | *req*, |
| --- | --- | --- | --- |
|  |  | struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \* | *iodev\_sqe*, |
|  |  | [rtio\_work\_submit\_t](#add537a23ac061970d890f65d76f5f906) | *handler* ) |

Submit RTIO work request.

Parameters
:   | req | Item to fill with request information. |
    | --- | --- |
    | iodev\_sqe | RTIO Operation information. |
    | handler | Callback to handler where work operation is performed. |

## [◆ ](#a352516812e7bc88b61cceb2f69d9fd3f)rtio\_work\_req\_used\_count\_get()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_work\_req\_used\_count\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Obtain number of currently used items from the pre-allocated pool.

Returns
:   Number of used items.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [rtio](dir_2c800b92938ab205b51fc9bd951bff11.md)
- [work.h](work_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
