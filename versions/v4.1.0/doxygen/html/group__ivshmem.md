---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ivshmem.html
original_path: doxygen/html/group__ivshmem.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Inter-VM Shared Memory (ivshmem) reference API

[Device Driver APIs](group__io__interfaces.md)

Inter-VM Shared Memory (ivshmem) reference API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ivshmem\_driver\_api](structivshmem__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [IVSHMEM\_V2\_PROTO\_UNDEFINED](#gad1a29cd2df2107001a3461947032db6c)   0x0000 |
| #define | [IVSHMEM\_V2\_PROTO\_NET](#gae65765ef159aa70ebed6db295a01ce00)   0x0001 |

| Typedefs | |
| --- | --- |
| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)(\* | [ivshmem\_get\_mem\_f](#gaf8f761888728090ab6adb11f3b700057)) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [ivshmem\_get\_id\_f](#ga8a6f4c145426f8a28c0f3a52875b7ea1)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [ivshmem\_get\_vectors\_f](#ga7e25f5db9ac889a2ff05694f60f66e39)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [ivshmem\_int\_peer\_f](#ga1af6d005fac141c84716b18705219bfd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| typedef int(\* | [ivshmem\_register\_handler\_f](#ga842bee3ff990f166665593c384c6bb21)) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ivshmem\_get\_mem](#gaef043cbfbe0aa5061db57f9bbae02eca) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap) |
|  | Get the inter-VM shared memory. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ivshmem\_get\_id](#gab2f0ccd5a2b8203a54ee5707b3afd6cc) (const struct [device](structdevice.md) \*dev) |
|  | Get our VM ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ivshmem\_get\_vectors](#gafee360f2c35abb9a203dd9f4838b8846) (const struct [device](structdevice.md) \*dev) |
|  | Get the number of interrupt vectors we can use. |
| int | [ivshmem\_int\_peer](#gab4e02271f8b854c783c359aca240d20c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Interrupt another VM. |
| int | [ivshmem\_register\_handler](#ga88aacb71bff0375c10fdb48e34b359fe) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Register a vector notification (interrupt) handler. |

## Detailed Description

Inter-VM Shared Memory (ivshmem) reference API.

## Macro Definition Documentation

## [◆ ](#gae65765ef159aa70ebed6db295a01ce00)IVSHMEM\_V2\_PROTO\_NET

| #define IVSHMEM\_V2\_PROTO\_NET   0x0001 |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## [◆ ](#gad1a29cd2df2107001a3461947032db6c)IVSHMEM\_V2\_PROTO\_UNDEFINED

| #define IVSHMEM\_V2\_PROTO\_UNDEFINED   0x0000 |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## Typedef Documentation

## [◆ ](#ga8a6f4c145426f8a28c0f3a52875b7ea1)ivshmem\_get\_id\_f

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* ivshmem\_get\_id\_f) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## [◆ ](#gaf8f761888728090ab6adb11f3b700057)ivshmem\_get\_mem\_f

| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)(\* ivshmem\_get\_mem\_f) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap) |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## [◆ ](#ga7e25f5db9ac889a2ff05694f60f66e39)ivshmem\_get\_vectors\_f

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* ivshmem\_get\_vectors\_f) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## [◆ ](#ga1af6d005fac141c84716b18705219bfd)ivshmem\_int\_peer\_f

| typedef int(\* ivshmem\_int\_peer\_f) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## [◆ ](#ga842bee3ff990f166665593c384c6bb21)ivshmem\_register\_handler\_f

| typedef int(\* ivshmem\_register\_handler\_f) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

## Function Documentation

## [◆ ](#gab2f0ccd5a2b8203a54ee5707b3afd6cc)ivshmem\_get\_id()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ivshmem\_get\_id | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

Get our VM ID.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |

Returns
:   our VM ID or 0 if we are not running on doorbell version

## [◆ ](#gaef043cbfbe0aa5061db57f9bbae02eca)ivshmem\_get\_mem()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ivshmem\_get\_mem | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \* | *memmap* ) |

`#include <[ivshmem.h](ivshmem_8h.md)>`

Get the inter-VM shared memory.

Note: This API is not supported for ivshmem-v2, as the R/W and R/O areas may not be mapped contiguously. For ivshmem-v2, use the ivshmem\_get\_rw\_mem\_section, ivshmem\_get\_output\_mem\_section and ivshmem\_get\_state APIs to access the shared memory.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | memmap | A pointer to fill in with the memory address |

Returns
:   the size of the memory mapped, or 0

## [◆ ](#gafee360f2c35abb9a203dd9f4838b8846)ivshmem\_get\_vectors()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ivshmem\_get\_vectors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ivshmem.h](ivshmem_8h.md)>`

Get the number of interrupt vectors we can use.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |

Returns
:   the number of available interrupt vectors

## [◆ ](#gab4e02271f8b854c783c359aca240d20c)ivshmem\_int\_peer()

| int ivshmem\_int\_peer | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *peer\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vector* ) |

`#include <[ivshmem.h](ivshmem_8h.md)>`

Interrupt another VM.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | peer\_id | The VM ID to interrupt |
    | vector | The interrupt vector to use |

Returns
:   0 on success, a negative errno otherwise

## [◆ ](#ga88aacb71bff0375c10fdb48e34b359fe)ivshmem\_register\_handler()

| int ivshmem\_register\_handler | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [k\_poll\_signal](structk__poll__signal.md) \* | *signal*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vector* ) |

`#include <[ivshmem.h](ivshmem_8h.md)>`

Register a vector notification (interrupt) handler.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69) | A pointer to a valid and ready to be signaled struct [k\_poll\_signal](structk__poll__signal.md). Or NULL to unregister any handler registered for the given vector. |
    | vector | The interrupt vector to get notification from |

Note: The returned status, if positive, to a raised signal is the vector that generated the signal. This lets the possibility to the user to have one signal for all vectors, or one per-vector.

Returns
:   0 on success, a negative errno otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
