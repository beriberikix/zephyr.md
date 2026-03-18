---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/flash_8h.html
original_path: doxygen/html/flash_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

flash.h File Reference

Public API for FLASH drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/flash.h>`

[Go to the source code of this file.](flash_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [flash\_pages\_layout](structflash__pages__layout.md) |
| struct | [flash\_parameters](structflash__parameters.md) |
|  | Flash memory parameters. [More...](structflash__parameters.md#details) |
| struct | [flash\_driver\_api](structflash__driver__api.md) |
| struct | [flash\_pages\_info](structflash__pages__info.md) |

| Macros | |
| --- | --- |
| #define | [FLASH\_EX\_OP\_VENDOR\_BASE](group__flash__interface.md#ga67418b2d5cbbec83463dce3d426162e3)   0x8000 |
| #define | [FLASH\_EX\_OP\_IS\_VENDOR](group__flash__interface.md#gafc0aa899b7ea452d048d8ee67d2e6f06)(c) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [flash\_api\_read](group__flash__internal__interface.md#ga358404d040b7ef30c8d24106e97bc290)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| typedef int(\* | [flash\_api\_write](group__flash__internal__interface.md#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Flash write implementation handler type. |
| typedef int(\* | [flash\_api\_erase](group__flash__internal__interface.md#ga2178a2338e652396ba9811ca449f4cb5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flash erase implementation handler type. |
| typedef const struct [flash\_parameters](structflash__parameters.md) \*(\* | [flash\_api\_get\_parameters](group__flash__internal__interface.md#ga2dee3874cb1be4ef4dab599963c30e70)) (const struct [device](structdevice.md) \*dev) |
| typedef void(\* | [flash\_api\_pages\_layout](group__flash__internal__interface.md#ga7576411536217c9ec3e167e7a5ca82a5)) (const struct [device](structdevice.md) \*dev, const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*[layout](bindesc_8h.md#af8174bbae9567135fe17f1e55621f641), [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*layout\_size) |
|  | Retrieve a flash device's layout. |
| typedef int(\* | [flash\_api\_sfdp\_read](group__flash__internal__interface.md#gac7b802015885044df6a1872513b89ab5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| typedef int(\* | [flash\_api\_read\_jedec\_id](group__flash__internal__interface.md#ga088369ef7593aa7c1fbe4cdad6e5b994)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id) |
| typedef int(\* | [flash\_api\_ex\_op](group__flash__internal__interface.md#gacff972cc16c1afa0a85e3118eff0afb2)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out) |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f)) (const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data) |
|  | Callback type for iterating over flash pages present on a device. |

| Enumerations | |
| --- | --- |
| enum | [flash\_ex\_op\_types](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51) { [FLASH\_EX\_OP\_RESET](group__flash__interface.md#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) = 0 } |
|  | Enumeration for extra flash operations. [More...](group__flash__interface.md#gae401e7b13d22a0f405e8d2ca0ef33c51) |

| Functions | |
| --- | --- |
| int | [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from flash. |
| int | [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write buffer into flash memory. |
| int | [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Erase part or all of a flash memory. |
| int | [flash\_get\_page\_info\_by\_offs](group__flash__interface.md#gafc959b0363eb27d6a3237e4288d60979) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, struct [flash\_pages\_info](structflash__pages__info.md) \*info) |
|  | Get the size and start offset of flash page at certain flash offset. |
| int | [flash\_get\_page\_info\_by\_idx](group__flash__interface.md#gaae733082fa92f80261d5895d3f81a98b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) page\_index, struct [flash\_pages\_info](structflash__pages__info.md) \*info) |
|  | Get the size and start offset of flash page of certain index. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_get\_page\_count](group__flash__interface.md#gaf750fe20c02758be7e37f36d2d16345e) (const struct [device](structdevice.md) \*dev) |
|  | Get the total number of flash pages. |
| void | [flash\_page\_foreach](group__flash__interface.md#ga275f2346e88b5e4d050dae426f0953fe) (const struct [device](structdevice.md) \*dev, [flash\_page\_cb](group__flash__interface.md#ga41bfc5eb05a8e73873763c36f3e1ec6f) cb, void \*data) |
|  | Iterate over all flash pages on a device. |
| int | [flash\_sfdp\_read](group__flash__interface.md#ga8e9b921299bfb059bf72445a2ffa5a97) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from Serial Flash Discoverable Parameters. |
| int | [flash\_read\_jedec\_id](group__flash__interface.md#gadb273ed317e1088b57adcac3385f50a7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id) |
|  | Read the JEDEC ID from a compatible flash device. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_get\_write\_block\_size](group__flash__interface.md#gaadfb323bc1b4efa39e7bc0a048c472a6) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum write block size supported by the driver. |
| const struct [flash\_parameters](structflash__parameters.md) \* | [flash\_get\_parameters](group__flash__interface.md#ga07b516708224b7a69a5169ef9c5c26e3) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to [flash\_parameters](structflash__parameters.md "Flash memory parameters.") structure. |
| int | [flash\_ex\_op](group__flash__interface.md#ga5571fbed2babb0036255d7a4d5e66f6c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out) |
|  | Execute flash extended operation on given device. |

## Detailed Description

Public API for FLASH drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [flash.h](flash_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
