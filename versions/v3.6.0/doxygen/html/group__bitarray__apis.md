---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bitarray__apis.html
original_path: doxygen/html/group__bitarray__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bit array

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

Store and manipulate bits in a bit array.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_BITARRAY\_DEFINE](#gabbe958c6b995023665651e4aa050aa62)(name, total\_bits) |
|  | Create a bitarray object. |
| #define | [SYS\_BITARRAY\_DEFINE\_STATIC](#ga2c55680355b67fc25125299a35f604d1)(name, total\_bits) |
|  | Create a static bitarray object. |

| Typedefs | |
| --- | --- |
| typedef struct sys\_bitarray | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) |
|  | Bitarray structure. |

| Functions | |
| --- | --- |
| int | [sys\_bitarray\_set\_bit](#ga5fe657e79fee3e111284e4184eb6b681) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit) |
|  | Set a bit in a bit array. |
| int | [sys\_bitarray\_clear\_bit](#ga795e8bf81f5717addf523cec124cde4e) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit) |
|  | Clear a bit in a bit array. |
| int | [sys\_bitarray\_test\_bit](#gae024ace00949fe8c565081e62818449d) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*val) |
|  | Test whether a bit is set or not. |
| int | [sys\_bitarray\_test\_and\_set\_bit](#gad1761b9eae8a1d9302893ce5f8591923) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*prev\_val) |
|  | Test the bit and set it. |
| int | [sys\_bitarray\_test\_and\_clear\_bit](#ga40fa4d37f1fb2da8789f70de50c599d5) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bit, int \*prev\_val) |
|  | Test the bit and clear it. |
| int | [sys\_bitarray\_alloc](#gac96766d9441a3b143aa386e2ac79ffd9) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*offset) |
|  | Allocate bits in a bit array. |
| int | [sys\_bitarray\_free](#gaf9a2c34896d3b1866a5a60f78d4166b0) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Free bits in a bit array. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_bitarray\_is\_region\_set](#ga2aa91a9be38b11e74dacbeb2fe5e6d6d) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Test if bits in a region is all set. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sys\_bitarray\_is\_region\_cleared](#ga21cd833e7118f188ca3e06f8cfd13a49) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Test if bits in a region is all cleared. |
| int | [sys\_bitarray\_set\_region](#ga94d1a547b9fe0a01d73acf4a5c4f308b) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Set all bits in a region. |
| int | [sys\_bitarray\_test\_and\_set\_region](#gad18590d2ab0bf251a59996620ed6e6bf) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) to\_set) |
|  | Test if all bits in a region are cleared/set and set/clear them in a single atomic operation. |
| int | [sys\_bitarray\_clear\_region](#gad13bb2c37d0889807e026dbac6a2872d) ([sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \*bitarray, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_bits, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
|  | Clear all bits in a region. |

## Detailed Description

Store and manipulate bits in a bit array.

## Macro Definition Documentation

## [◆ ](#gabbe958c6b995023665651e4aa050aa62)SYS\_BITARRAY\_DEFINE

| #define SYS\_BITARRAY\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *total\_bits* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

**Value:**

\_SYS\_BITARRAY\_DEFINE(name, total\_bits,)

Create a bitarray object.

Parameters
:   | name | Name of the bitarray object. |
    | --- | --- |
    | total\_bits | Total number of bits in this bitarray object. |

## [◆ ](#ga2c55680355b67fc25125299a35f604d1)SYS\_BITARRAY\_DEFINE\_STATIC

| #define SYS\_BITARRAY\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *total\_bits* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

**Value:**

\_SYS\_BITARRAY\_DEFINE(name, total\_bits, static)

Create a static bitarray object.

Parameters
:   | name | Name of the bitarray object. |
    | --- | --- |
    | total\_bits | Total number of bits in this bitarray object. |

## Typedef Documentation

## [◆ ](#ga168a1da9ac2bee523bdc9778e94fd841)sys\_bitarray\_t

| typedef struct sys\_bitarray [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) |
| --- |

`#include <[bitarray.h](bitarray_8h.md)>`

Bitarray structure.

## Function Documentation

## [◆ ](#gac96766d9441a3b143aa386e2ac79ffd9)sys\_bitarray\_alloc()

| int sys\_bitarray\_alloc | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Allocate bits in a bit array.

This finds a number of bits (`num_bits`) in a contiguous of previously unallocated region. If such a region exists, the bits are marked as allocated and the offset to the start of this region is returned via `offset`.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | num\_bits | Number of bits to allocate |
    | [out] | offset | Offset to the start of allocated region if successful |

Return values
:   | 0 | Allocation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. allocating more bits than the bitarray has, trying to allocate 0 bits, etc.) |
    | -ENOSPC | No contiguous region big enough to accommodate the allocation |

## [◆ ](#ga795e8bf81f5717addf523cec124cde4e)sys\_bitarray\_clear\_bit()

| int sys\_bitarray\_clear\_bit | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bit* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Clear a bit in a bit array.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | bit | The bit to be cleared |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to clear exceeds the number of bits in bit array, etc.) |

## [◆ ](#gad13bb2c37d0889807e026dbac6a2872d)sys\_bitarray\_clear\_region()

| int sys\_bitarray\_clear\_region | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Clear all bits in a region.

This clears the number of bits (`num_bits`) in region starting from `offset`.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to test |
    | offset | Starting bit position to test |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to set exceeds the number of bits in bit array, etc.) |

## [◆ ](#gaf9a2c34896d3b1866a5a60f78d4166b0)sys\_bitarray\_free()

| int sys\_bitarray\_free | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Free bits in a bit array.

This marks the number of bits (`num_bits`) starting from `offset` as no longer allocated.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to free |
    | offset | Starting bit position to free |

Return values
:   | 0 | Free is successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. try to free more bits than the bitarray has, trying to free 0 bits, etc.) |
    | -EFAULT | The bits in the indicated region are not all allocated. |

## [◆ ](#ga21cd833e7118f188ca3e06f8cfd13a49)sys\_bitarray\_is\_region\_cleared()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_bitarray\_is\_region\_cleared | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test if bits in a region is all cleared.

This tests if the number of bits (`num_bits`) in region starting from `offset` are all cleared.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to test |
    | offset | Starting bit position to test |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | All bits are cleared. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Not all bits are cleared. |

## [◆ ](#ga2aa91a9be38b11e74dacbeb2fe5e6d6d)sys\_bitarray\_is\_region\_set()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sys\_bitarray\_is\_region\_set | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test if bits in a region is all set.

This tests if the number of bits (`num_bits`) in region starting from `offset` are all set.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to test |
    | offset | Starting bit position to test |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | All bits are set. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Not all bits are set. |

## [◆ ](#ga5fe657e79fee3e111284e4184eb6b681)sys\_bitarray\_set\_bit()

| int sys\_bitarray\_set\_bit | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bit* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Set a bit in a bit array.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | bit | The bit to be set |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to set exceeds the number of bits in bit array, etc.) |

## [◆ ](#ga94d1a547b9fe0a01d73acf4a5c4f308b)sys\_bitarray\_set\_region()

| int sys\_bitarray\_set\_region | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Set all bits in a region.

This sets the number of bits (`num_bits`) in region starting from `offset`.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to test |
    | offset | Starting bit position to test |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to set exceeds the number of bits in bit array, etc.) |

## [◆ ](#ga40fa4d37f1fb2da8789f70de50c599d5)sys\_bitarray\_test\_and\_clear\_bit()

| int sys\_bitarray\_test\_and\_clear\_bit | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bit*, |
|  |  | int \* | *prev\_val* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test the bit and clear it.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | bit | The bit to be tested and cleared |
    | [out] | prev\_val | Previous value of the bit (0 or 1) |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to test exceeds the number of bits in bit array, etc.) |

## [◆ ](#gad1761b9eae8a1d9302893ce5f8591923)sys\_bitarray\_test\_and\_set\_bit()

| int sys\_bitarray\_test\_and\_set\_bit | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bit*, |
|  |  | int \* | *prev\_val* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test the bit and set it.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | bit | The bit to be tested and set |
    | [out] | prev\_val | Previous value of the bit (0 or 1) |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to test exceeds the number of bits in bit array, etc.) |

## [◆ ](#gad18590d2ab0bf251a59996620ed6e6bf)sys\_bitarray\_test\_and\_set\_region()

| int sys\_bitarray\_test\_and\_set\_region | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_bits*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *offset*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *to\_set* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test if all bits in a region are cleared/set and set/clear them in a single atomic operation.

This checks if all the bits (`num_bits`) in region starting from `offset` are in required state. If even one bit is not, -EEXIST is returned. If the whole region is set/cleared it is set to opposite state. The check and set is performed as a single atomic operation.

Parameters
:   | bitarray | Bitarray struct |
    | --- | --- |
    | num\_bits | Number of bits to test and set |
    | offset | Starting bit position to test and set |
    | to\_set | if true the region will be set if all bits are cleared if false the region will be cleard if all bits are set |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to set exceeds the number of bits in bit array, etc.) |
    | -EEXIST | at least one bit in the region is set/cleared, operation cancelled |

## [◆ ](#gae024ace00949fe8c565081e62818449d)sys\_bitarray\_test\_bit()

| int sys\_bitarray\_test\_bit | ( | [sys\_bitarray\_t](#ga168a1da9ac2bee523bdc9778e94fd841) \* | *bitarray*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bit*, |
|  |  | int \* | *val* ) |

`#include <[bitarray.h](bitarray_8h.md)>`

Test whether a bit is set or not.

Parameters
:   | [in] | bitarray | Bitarray struct |
    | --- | --- | --- |
    | [in] | bit | The bit to be tested |
    | [out] | val | The value of the bit (0 or 1) |

Return values
:   | 0 | Operation successful |
    | --- | --- |
    | -EINVAL | Invalid argument (e.g. bit to test exceeds the number of bits in bit array, etc.) |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
