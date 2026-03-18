---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__flash__internal__interface.html
original_path: doxygen/html/group__flash__internal__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FLASH internal Interface

[Device Driver APIs](group__io__interfaces.md)

FLASH internal Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [flash\_pages\_layout](structflash__pages__layout.md) |
| struct | [flash\_driver\_api](structflash__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [flash\_api\_read](#ga358404d040b7ef30c8d24106e97bc290)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| typedef int(\* | [flash\_api\_write](#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Flash write implementation handler type. |
| typedef int(\* | [flash\_api\_erase](#ga2178a2338e652396ba9811ca449f4cb5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Flash erase implementation handler type. |
| typedef const struct [flash\_parameters](structflash__parameters.md) \*(\* | [flash\_api\_get\_parameters](#ga2dee3874cb1be4ef4dab599963c30e70)) (const struct [device](structdevice.md) \*dev) |
| typedef void(\* | [flash\_api\_pages\_layout](#ga7576411536217c9ec3e167e7a5ca82a5)) (const struct [device](structdevice.md) \*dev, const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*layout, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*layout\_size) |
|  | Retrieve a flash device's layout. |
| typedef int(\* | [flash\_api\_sfdp\_read](#gac7b802015885044df6a1872513b89ab5)) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| typedef int(\* | [flash\_api\_read\_jedec\_id](#ga088369ef7593aa7c1fbe4cdad6e5b994)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id) |
| typedef int(\* | [flash\_api\_ex\_op](#gacff972cc16c1afa0a85e3118eff0afb2)) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out) |

## Detailed Description

FLASH internal Interface.

## Typedef Documentation

## [◆ ](#ga2178a2338e652396ba9811ca449f4cb5)flash\_api\_erase

| typedef int(\* flash\_api\_erase) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

`#include <[flash.h](flash_8h.md)>`

Flash erase implementation handler type.

Note
:   Any necessary erase protection management must be performed by the driver, with the driver responsible for ensuring the "erase-protect" after the operation completes (successfully or not) matches the erase-protect state when the operation was started.

The callback is optional for RAM non-volatile devices, which do not require erase by design, but may be provided if it allows device to work more effectively, or if device has a support for internal fill operation the erase in driver uses.

## [◆ ](#gacff972cc16c1afa0a85e3118eff0afb2)flash\_api\_ex\_op

| typedef int(\* flash\_api\_ex\_op) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out) |
| --- |

`#include <[flash.h](flash_8h.md)>`

## [◆ ](#ga2dee3874cb1be4ef4dab599963c30e70)flash\_api\_get\_parameters

| typedef const struct [flash\_parameters](structflash__parameters.md) \*(\* flash\_api\_get\_parameters) (const struct [device](structdevice.md) \*dev) |
| --- |

`#include <[flash.h](flash_8h.md)>`

## [◆ ](#ga7576411536217c9ec3e167e7a5ca82a5)flash\_api\_pages\_layout

| typedef void(\* flash\_api\_pages\_layout) (const struct [device](structdevice.md) \*dev, const struct [flash\_pages\_layout](structflash__pages__layout.md) \*\*layout, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*layout\_size) |
| --- |

`#include <[flash.h](flash_8h.md)>`

Retrieve a flash device's layout.

A flash device layout is a run-length encoded description of the pages on the device. (Here, "page" means the smallest erasable area on the flash device.)

For flash memories which have uniform page sizes, this routine returns an array of length 1, which specifies the page size and number of pages in the memory.

Layouts for flash memories with nonuniform page sizes will be returned as an array with multiple elements, each of which describes a group of pages that all have the same size. In this case, the sequence of array elements specifies the order in which these groups occur on the device.

Parameters
:   | dev | Flash device whose layout to retrieve. |
    | --- | --- |
    | layout | The flash layout will be returned in this argument. |
    | layout\_size | The number of elements in the returned layout. |

## [◆ ](#ga358404d040b7ef30c8d24106e97bc290)flash\_api\_read

| typedef int(\* flash\_api\_read) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[flash.h](flash_8h.md)>`

## [◆ ](#ga088369ef7593aa7c1fbe4cdad6e5b994)flash\_api\_read\_jedec\_id

| typedef int(\* flash\_api\_read\_jedec\_id) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id) |
| --- |

`#include <[flash.h](flash_8h.md)>`

## [◆ ](#gac7b802015885044df6a1872513b89ab5)flash\_api\_sfdp\_read

| typedef int(\* flash\_api\_sfdp\_read) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[flash.h](flash_8h.md)>`

## [◆ ](#gaf6b0c3aa2b6514ac8936aa0c7fda96ba)flash\_api\_write

| typedef int(\* flash\_api\_write) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| --- |

`#include <[flash.h](flash_8h.md)>`

Flash write implementation handler type.

Note
:   Any necessary write protection management must be performed by the driver, with the driver responsible for ensuring the "write-protect" after the operation completes (successfully or not) matches the write-protect state when the operation was started.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
