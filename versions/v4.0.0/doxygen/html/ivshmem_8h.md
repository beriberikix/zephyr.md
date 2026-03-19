---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ivshmem_8h.html
original_path: doxygen/html/ivshmem_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ivshmem.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <zephyr/syscalls/ivshmem.h>`

[Go to the source code of this file.](ivshmem_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ivshmem\_driver\_api](structivshmem__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [IVSHMEM\_V2\_PROTO\_UNDEFINED](group__ivshmem.md#gad1a29cd2df2107001a3461947032db6c)   0x0000 |
| #define | [IVSHMEM\_V2\_PROTO\_NET](group__ivshmem.md#gae65765ef159aa70ebed6db295a01ce00)   0x0001 |

| Typedefs | |
| --- | --- |
| typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)(\* | [ivshmem\_get\_mem\_f](group__ivshmem.md#gaf8f761888728090ab6adb11f3b700057)) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [ivshmem\_get\_id\_f](group__ivshmem.md#ga8a6f4c145426f8a28c0f3a52875b7ea1)) (const struct [device](structdevice.md) \*dev) |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [ivshmem\_get\_vectors\_f](group__ivshmem.md#ga7e25f5db9ac889a2ff05694f60f66e39)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [ivshmem\_int\_peer\_f](group__ivshmem.md#ga1af6d005fac141c84716b18705219bfd)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
| typedef int(\* | [ivshmem\_register\_handler\_f](group__ivshmem.md#ga842bee3ff990f166665593c384c6bb21)) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [ivshmem\_get\_mem](group__ivshmem.md#gaef043cbfbe0aa5061db57f9bbae02eca) (const struct [device](structdevice.md) \*dev, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap) |
|  | Get the inter-VM shared memory. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ivshmem\_get\_id](group__ivshmem.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc) (const struct [device](structdevice.md) \*dev) |
|  | Get our VM ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ivshmem\_get\_vectors](group__ivshmem.md#gafee360f2c35abb9a203dd9f4838b8846) (const struct [device](structdevice.md) \*dev) |
|  | Get the number of interrupt vectors we can use. |
| int | [ivshmem\_int\_peer](group__ivshmem.md#gab4e02271f8b854c783c359aca240d20c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Interrupt another VM. |
| int | [ivshmem\_register\_handler](group__ivshmem.md#ga88aacb71bff0375c10fdb48e34b359fe) (const struct [device](structdevice.md) \*dev, struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector) |
|  | Register a vector notification (interrupt) handler. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtualization](dir_9d22dc9b22b8050a5a1558ed6b8fdf63.md)
- [ivshmem.h](ivshmem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
