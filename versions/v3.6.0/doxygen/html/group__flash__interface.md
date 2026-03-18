---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__flash__interface.html
original_path: doxygen/html/group__flash__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FLASH Interface

[Device Driver APIs](group__io__interfaces.md)

FLASH Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [flash\_parameters](structflash__parameters.md) |
|  | Flash memory parameters. [More...](structflash__parameters.md#details) |
| struct | [flash\_pages\_info](structflash__pages__info.md) |

| Macros | |
| --- | --- |
| #define | [FLASH\_EX\_OP\_VENDOR\_BASE](#ga67418b2d5cbbec83463dce3d426162e3)   0x8000 |
| #define | [FLASH\_EX\_OP\_IS\_VENDOR](#gafc0aa899b7ea452d048d8ee67d2e6f06)(c) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [flash\_page\_cb](#ga41bfc5eb05a8e73873763c36f3e1ec6f)) (const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data) |
|  | Callback type for iterating over flash pages present on a device. |

| Enumerations | |
| --- | --- |
| enum | [flash\_ex\_op\_types](#gae401e7b13d22a0f405e8d2ca0ef33c51) { [FLASH\_EX\_OP\_RESET](#ggae401e7b13d22a0f405e8d2ca0ef33c51a296527e7d6b431780b9f4d813010bbdd) = 0 } |
|  | Enumeration for extra flash operations. [More...](#gae401e7b13d22a0f405e8d2ca0ef33c51) |

| Functions | |
| --- | --- |
| int | [flash\_read](#gaa7c9382796aad64da0da683f54600b5f) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from flash. |
| int | [flash\_write](#ga76d7880cc5e18ca40237736d3bd94324) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write buffer into flash memory. |
| int | [flash\_erase](#ga05f9c8b0c1ff7273f71797e7ff799c95) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Erase part or all of a flash memory. |
| int | [flash\_get\_page\_info\_by\_offs](#gafc959b0363eb27d6a3237e4288d60979) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, struct [flash\_pages\_info](structflash__pages__info.md) \*info) |
|  | Get the size and start offset of flash page at certain flash offset. |
| int | [flash\_get\_page\_info\_by\_idx](#gaae733082fa92f80261d5895d3f81a98b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) page\_index, struct [flash\_pages\_info](structflash__pages__info.md) \*info) |
|  | Get the size and start offset of flash page of certain index. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_get\_page\_count](#gaf750fe20c02758be7e37f36d2d16345e) (const struct [device](structdevice.md) \*dev) |
|  | Get the total number of flash pages. |
| void | [flash\_page\_foreach](#ga275f2346e88b5e4d050dae426f0953fe) (const struct [device](structdevice.md) \*dev, [flash\_page\_cb](#ga41bfc5eb05a8e73873763c36f3e1ec6f) cb, void \*data) |
|  | Iterate over all flash pages on a device. |
| int | [flash\_sfdp\_read](#ga8e9b921299bfb059bf72445a2ffa5a97) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read data from Serial Flash Discoverable Parameters. |
| int | [flash\_read\_jedec\_id](#gadb273ed317e1088b57adcac3385f50a7) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*id) |
|  | Read the JEDEC ID from a compatible flash device. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [flash\_get\_write\_block\_size](#gaadfb323bc1b4efa39e7bc0a048c472a6) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum write block size supported by the driver. |
| const struct [flash\_parameters](structflash__parameters.md) \* | [flash\_get\_parameters](#ga07b516708224b7a69a5169ef9c5c26e3) (const struct [device](structdevice.md) \*dev) |
|  | Get pointer to [flash\_parameters](structflash__parameters.md "Flash memory parameters.") structure. |
| int | [flash\_ex\_op](#ga5571fbed2babb0036255d7a4d5e66f6c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) code, const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) in, void \*out) |
|  | Execute flash extended operation on given device. |

## Detailed Description

FLASH Interface.

## Macro Definition Documentation

## [◆ ](#gafc0aa899b7ea452d048d8ee67d2e6f06)FLASH\_EX\_OP\_IS\_VENDOR

| #define FLASH\_EX\_OP\_IS\_VENDOR | ( |  | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash.h](flash_8h.md)>`

**Value:**

((c) & [FLASH\_EX\_OP\_VENDOR\_BASE](#ga67418b2d5cbbec83463dce3d426162e3))

[FLASH\_EX\_OP\_VENDOR\_BASE](#ga67418b2d5cbbec83463dce3d426162e3)

#define FLASH\_EX\_OP\_VENDOR\_BASE

**Definition** flash.h:471

## [◆ ](#ga67418b2d5cbbec83463dce3d426162e3)FLASH\_EX\_OP\_VENDOR\_BASE

| #define FLASH\_EX\_OP\_VENDOR\_BASE   0x8000 |
| --- |

`#include <[flash.h](flash_8h.md)>`

## Typedef Documentation

## [◆ ](#ga41bfc5eb05a8e73873763c36f3e1ec6f)flash\_page\_cb

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* flash\_page\_cb) (const struct [flash\_pages\_info](structflash__pages__info.md) \*info, void \*data) |
| --- |

`#include <[flash.h](flash_8h.md)>`

Callback type for iterating over flash pages present on a device.

The callback should return true to continue iterating, and false to halt.

Parameters
:   | info | Information for current page |
    | --- | --- |
    | data | Private data for callback |

Returns
:   True to continue iteration, false to halt iteration.

See also
:   [flash\_page\_foreach()](#ga275f2346e88b5e4d050dae426f0953fe)

## Enumeration Type Documentation

## [◆ ](#gae401e7b13d22a0f405e8d2ca0ef33c51)flash\_ex\_op\_types

| enum [flash\_ex\_op\_types](#gae401e7b13d22a0f405e8d2ca0ef33c51) |
| --- |

`#include <[flash.h](flash_8h.md)>`

Enumeration for extra flash operations.

| Enumerator | |
| --- | --- |
| FLASH\_EX\_OP\_RESET |  |

## Function Documentation

## [◆ ](#ga05f9c8b0c1ff7273f71797e7ff799c95)flash\_erase()

| int flash\_erase | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[flash.h](flash_8h.md)>`

Erase part or all of a flash memory.

Acceptable values of erase size and offset are subject to hardware-specific multiples of page size and offset. Please check the API implemented by the underlying sub driver, for example by using [flash\_get\_page\_info\_by\_offs()](#gafc959b0363eb27d6a3237e4288d60979) if that is supported by your flash driver.

Any necessary erase protection management is performed by the driver erase implementation itself.

Parameters
:   | dev | : flash device |
    | --- | --- |
    | offset | : erase area starting offset |
    | size | : size of area to be erased |

Returns
:   0 on success, negative errno code on fail.

See also
:   [flash\_get\_page\_info\_by\_offs()](#gafc959b0363eb27d6a3237e4288d60979)
:   [flash\_get\_page\_info\_by\_idx()](#gaae733082fa92f80261d5895d3f81a98b)

## [◆ ](#ga5571fbed2babb0036255d7a4d5e66f6c)flash\_ex\_op()

| int flash\_ex\_op | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *code*, |
|  |  | const [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) | *in*, |
|  |  | void \* | *out* ) |

`#include <[flash.h](flash_8h.md)>`

Execute flash extended operation on given device.

Besides of standard flash operations like write or erase, flash controllers also support additional features like write protection or readout protection. These features are not available in every flash controller, what's more controllers can implement it in a different way.

It doesn't make sense to add a separate flash API function for every flash controller feature, because it could be unique (supported on small number of flash controllers) or the API won't be able to represent the same feature on every flash controller.

Parameters
:   | dev | Flash device |
    | --- | --- |
    | code | Operation which will be executed on the device. |
    | in | Pointer to input data used by operation. If operation doesn't need any input data it could be NULL. |
    | out | Pointer to operation output data. If operation doesn't produce any output it could be NULL. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOTSUP | if given device doesn't support extended operation. |
    | -ENOSYS | if support for extended operations is not enabled in Kconfig |
    | negative | value on extended operation errors. |

## [◆ ](#gaf750fe20c02758be7e37f36d2d16345e)flash\_get\_page\_count()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_get\_page\_count | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash.h](flash_8h.md)>`

Get the total number of flash pages.

Parameters
:   | dev | flash device |
    | --- | --- |

Returns
:   Number of flash pages.

## [◆ ](#gaae733082fa92f80261d5895d3f81a98b)flash\_get\_page\_info\_by\_idx()

| int flash\_get\_page\_info\_by\_idx | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *page\_index*, |
|  |  | struct [flash\_pages\_info](structflash__pages__info.md) \* | *info* ) |

`#include <[flash.h](flash_8h.md)>`

Get the size and start offset of flash page of certain index.

Parameters
:   | dev | flash device |
    | --- | --- |
    | page\_index | Index of the page. Index are counted from 0. |
    | info | Page Info structure to be filled |

Returns
:   0 on success, -EINVAL if page of the index doesn't exist.

## [◆ ](#gafc959b0363eb27d6a3237e4288d60979)flash\_get\_page\_info\_by\_offs()

| int flash\_get\_page\_info\_by\_offs | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | struct [flash\_pages\_info](structflash__pages__info.md) \* | *info* ) |

`#include <[flash.h](flash_8h.md)>`

Get the size and start offset of flash page at certain flash offset.

Parameters
:   | dev | flash device |
    | --- | --- |
    | offset | Offset within the page |
    | info | Page Info structure to be filled |

Returns
:   0 on success, -EINVAL if page of the offset doesn't exist.

## [◆ ](#ga07b516708224b7a69a5169ef9c5c26e3)flash\_get\_parameters()

| const struct [flash\_parameters](structflash__parameters.md) \* flash\_get\_parameters | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash.h](flash_8h.md)>`

Get pointer to [flash\_parameters](structflash__parameters.md "Flash memory parameters.") structure.

Returned pointer points to a structure that should be considered constant through a runtime, regardless if it is defined in RAM or Flash. Developer is free to cache the structure pointer or copy its contents.

Returns
:   pointer to [flash\_parameters](structflash__parameters.md "Flash memory parameters.") structure characteristic for the device.

## [◆ ](#gaadfb323bc1b4efa39e7bc0a048c472a6)flash\_get\_write\_block\_size()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) flash\_get\_write\_block\_size | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[flash.h](flash_8h.md)>`

Get the minimum write block size supported by the driver.

The write block size supported by the driver might differ from the write block size of memory used because the driver might implements write-modify algorithm.

Parameters
:   | dev | flash device |
    | --- | --- |

Returns
:   write block size in bytes.

## [◆ ](#ga275f2346e88b5e4d050dae426f0953fe)flash\_page\_foreach()

| void flash\_page\_foreach | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [flash\_page\_cb](#ga41bfc5eb05a8e73873763c36f3e1ec6f) | *cb*, |
|  |  | void \* | *data* ) |

`#include <[flash.h](flash_8h.md)>`

Iterate over all flash pages on a device.

This routine iterates over all flash pages on the given device, ordered by increasing start offset. For each page, it invokes the given callback, passing it the page's information and a private data object.

Parameters
:   | dev | Device whose pages to iterate over |
    | --- | --- |
    | cb | Callback to invoke for each flash page |
    | data | Private data for callback function |

## [◆ ](#gaa7c9382796aad64da0da683f54600b5f)flash\_read()

| int flash\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash.h](flash_8h.md)>`

Read data from flash.

All flash drivers support reads without alignment restrictions on the read offset, the read size, or the destination address.

Parameters
:   | dev | : flash dev |
    | --- | --- |
    | offset | : Offset (byte aligned) to read |
    | data | : Buffer to store read data |
    | len | : Number of bytes to read. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gadb273ed317e1088b57adcac3385f50a7)flash\_read\_jedec\_id()

| int flash\_read\_jedec\_id | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *id* ) |

`#include <[flash.h](flash_8h.md)>`

Read the JEDEC ID from a compatible flash device.

Parameters
:   | dev | device from which id will be read |
    | --- | --- |
    | id | pointer to a buffer of at least 3 bytes into which id will be stored |

Return values
:   | 0 | on successful store of 3-byte JEDEC id |
    | --- | --- |
    | -ENOTSUP | if flash driver doesn't support this function |
    | negative | values for other errors |

## [◆ ](#ga8e9b921299bfb059bf72445a2ffa5a97)flash\_sfdp\_read()

| int flash\_sfdp\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash.h](flash_8h.md)>`

Read data from Serial Flash Discoverable Parameters.

This routine reads data from a serial flash device compatible with the JEDEC JESD216 standard for encoding flash memory characteristics.

Availability of this API is conditional on selecting `CONFIG_FLASH_JESD216_API` and support of that functionality in the driver underlying `dev`.

Parameters
:   | dev | device from which parameters will be read |
    | --- | --- |
    | offset | address within the SFDP region containing data of interest |
    | data | where the data to be read will be placed |
    | len | the number of bytes of data to be read |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOTSUP | if the flash driver does not support SFDP access |
    | negative | values for other errors. |

## [◆ ](#ga76d7880cc5e18ca40237736d3bd94324)flash\_write()

| int flash\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[flash.h](flash_8h.md)>`

Write buffer into flash memory.

All flash drivers support a source buffer located either in RAM or SoC flash, without alignment restrictions on the source address. Write size and offset must be multiples of the minimum write block size supported by the driver.

Any necessary write protection management is performed by the driver write implementation itself.

Parameters
:   | dev | : flash device |
    | --- | --- |
    | offset | : starting offset for the write |
    | data | : data to write |
    | len | : Number of bytes to write |

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
