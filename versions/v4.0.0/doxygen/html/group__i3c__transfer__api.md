---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__i3c__transfer__api.html
original_path: doxygen/html/group__i3c__transfer__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Transfer API

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C Transfer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i3c\_msg](structi3c__msg.md) |
|  | One I3C Message. [More...](structi3c__msg.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_MSG\_WRITE](#ga72f9fb65d218521ad006febf3dd6851b)   (0U << 0U) |
|  | Write message to I3C bus. |
| #define | [I3C\_MSG\_READ](#ga6ba89782a8646f96dc1f9fa3b9cd2058)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Read message from I3C bus. |
| #define | [I3C\_MSG\_STOP](#ga0d4ae269a53af945837d158f638d8b5c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Send STOP after this message. |
| #define | [I3C\_MSG\_RESTART](#gad9ff03f4fdcb117b90c17d667a49c295)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | RESTART I3C transaction for this message. |
| #define | [I3C\_MSG\_HDR](#gad827935caf8503aeaedd1aceb53d4e38)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Transfer use HDR mode. |
| #define | [I3C\_MSG\_NBCH](#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Skip I3C broadcast header. |
| #define | [I3C\_MSG\_HDR\_MODE0](#ga18aac0862826869f94e5a71670debcb0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | I3C HDR Mode 0. |
| #define | [I3C\_MSG\_HDR\_MODE1](#ga8eb3dc48237dfdb25fde40a1efa03241)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | I3C HDR Mode 1. |
| #define | [I3C\_MSG\_HDR\_MODE2](#ga15cbd61e7d509c28b22fbc9e0844cb23)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | I3C HDR Mode 2. |
| #define | [I3C\_MSG\_HDR\_MODE3](#ga162fb9ab0e4ed7f8feb0e91d183a88e7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | I3C HDR Mode 3. |
| #define | [I3C\_MSG\_HDR\_MODE4](#gabe45532238bc15672f6454dac70d20cf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | I3C HDR Mode 4. |
| #define | [I3C\_MSG\_HDR\_MODE5](#gac712daa606d0c51ce523d7a687821282)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | I3C HDR Mode 5. |
| #define | [I3C\_MSG\_HDR\_MODE6](#ga7654c1947e13c019c24bf12712b0773b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | I3C HDR Mode 6. |
| #define | [I3C\_MSG\_HDR\_MODE7](#ga08df1d8df82226d1f23b4cc923584672)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | I3C HDR Mode 7. |
| #define | [I3C\_MSG\_HDR\_DDR](#gac7386b21323d30148bd9456b9d180d7a)   [I3C\_MSG\_HDR\_MODE0](#ga18aac0862826869f94e5a71670debcb0) |
|  | I3C HDR-DDR (Double Data Rate). |
| #define | [I3C\_MSG\_HDR\_TSP](#gaa61322f770db296b5ab718c48ab960d3)   [I3C\_MSG\_HDR\_MODE1](#ga8eb3dc48237dfdb25fde40a1efa03241) |
|  | I3C HDR-TSP (Ternary Symbol Pure-bus). |
| #define | [I3C\_MSG\_HDR\_TSL](#gac43a2d266f3a23fd6dfa11405f3fd6f3)   [I3C\_MSG\_HDR\_MODE2](#ga15cbd61e7d509c28b22fbc9e0844cb23) |
|  | I3C HDR-TSL (Ternary Symbol Legacy-inclusive-bus). |
| #define | [I3C\_MSG\_HDR\_BT](#ga8b2fdcb827cbd3325f124a1c615698e7)   [I3C\_MSG\_HDR\_MODE3](#ga162fb9ab0e4ed7f8feb0e91d183a88e7) |
|  | I3C HDR-BT (Bulk Transport). |

| Functions | |
| --- | --- |
| int | [i3c\_transfer](#ga067c0f1e3c9abb6ef34ce48cb7e45cb8) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs) |
|  | Perform data transfer from the controller to a I3C target device. |
| static int | [i3c\_write](#gaa3b61aa9813ccb0df80562b0829d95dd) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write a set amount of data to an I3C target device. |
| static int | [i3c\_read](#gaba39bd08ab50c5737ba617f4d27c3541) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read a set amount of data from an I3C target device. |
| static int | [i3c\_write\_read](#ga3da2e99b667eab4fd92f5c0e1b57a8ea) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const void \*write\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_write, void \*read\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_read) |
|  | Write then read data from an I3C target device. |
| static int | [i3c\_burst\_read](#ga3e4d985a784618efad67f8550f715115) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Read multiple bytes from an internal address of an I3C target device. |
| static int | [i3c\_burst\_write](#gaee773f95fcaf6cb88ced47f5c512c78c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes) |
|  | Write multiple bytes to an internal address of an I3C target device. |
| static int | [i3c\_reg\_read\_byte](#ga87c1f23c94d37dfbaa22e4679fb8130a) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read internal register of an I3C target device. |
| static int | [i3c\_reg\_write\_byte](#gaf7033eb93fd3779ffa98eb83e5a1a1b1) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write internal register of an I3C target device. |
| static int | [i3c\_reg\_update\_byte](#ga4e0488ff21cbe99b206c115017473ed9) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Update internal register of an I3C target device. |
| void | [i3c\_dump\_msgs](#ga61098371d2492a3f35c0fa779a88b348) (const char \*name, const struct [i3c\_msg](structi3c__msg.md) \*msgs, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_msgs, struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Dump out an I3C message. |

## Detailed Description

I3C Transfer API.

## Macro Definition Documentation

## [◆ ](#gad827935caf8503aeaedd1aceb53d4e38)I3C\_MSG\_HDR

| #define I3C\_MSG\_HDR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Transfer use HDR mode.

## [◆ ](#ga8b2fdcb827cbd3325f124a1c615698e7)I3C\_MSG\_HDR\_BT

| #define I3C\_MSG\_HDR\_BT   [I3C\_MSG\_HDR\_MODE3](#ga162fb9ab0e4ed7f8feb0e91d183a88e7) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR-BT (Bulk Transport).

## [◆ ](#gac7386b21323d30148bd9456b9d180d7a)I3C\_MSG\_HDR\_DDR

| #define I3C\_MSG\_HDR\_DDR   [I3C\_MSG\_HDR\_MODE0](#ga18aac0862826869f94e5a71670debcb0) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR-DDR (Double Data Rate).

## [◆ ](#ga18aac0862826869f94e5a71670debcb0)I3C\_MSG\_HDR\_MODE0

| #define I3C\_MSG\_HDR\_MODE0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 0.

## [◆ ](#ga8eb3dc48237dfdb25fde40a1efa03241)I3C\_MSG\_HDR\_MODE1

| #define I3C\_MSG\_HDR\_MODE1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 1.

## [◆ ](#ga15cbd61e7d509c28b22fbc9e0844cb23)I3C\_MSG\_HDR\_MODE2

| #define I3C\_MSG\_HDR\_MODE2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 2.

## [◆ ](#ga162fb9ab0e4ed7f8feb0e91d183a88e7)I3C\_MSG\_HDR\_MODE3

| #define I3C\_MSG\_HDR\_MODE3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 3.

## [◆ ](#gabe45532238bc15672f6454dac70d20cf)I3C\_MSG\_HDR\_MODE4

| #define I3C\_MSG\_HDR\_MODE4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 4.

## [◆ ](#gac712daa606d0c51ce523d7a687821282)I3C\_MSG\_HDR\_MODE5

| #define I3C\_MSG\_HDR\_MODE5   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 5.

## [◆ ](#ga7654c1947e13c019c24bf12712b0773b)I3C\_MSG\_HDR\_MODE6

| #define I3C\_MSG\_HDR\_MODE6   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 6.

## [◆ ](#ga08df1d8df82226d1f23b4cc923584672)I3C\_MSG\_HDR\_MODE7

| #define I3C\_MSG\_HDR\_MODE7   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR Mode 7.

## [◆ ](#gac43a2d266f3a23fd6dfa11405f3fd6f3)I3C\_MSG\_HDR\_TSL

| #define I3C\_MSG\_HDR\_TSL   [I3C\_MSG\_HDR\_MODE2](#ga15cbd61e7d509c28b22fbc9e0844cb23) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR-TSL (Ternary Symbol Legacy-inclusive-bus).

## [◆ ](#gaa61322f770db296b5ab718c48ab960d3)I3C\_MSG\_HDR\_TSP

| #define I3C\_MSG\_HDR\_TSP   [I3C\_MSG\_HDR\_MODE1](#ga8eb3dc48237dfdb25fde40a1efa03241) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

I3C HDR-TSP (Ternary Symbol Pure-bus).

## [◆ ](#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)I3C\_MSG\_NBCH

| #define I3C\_MSG\_NBCH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Skip I3C broadcast header.

Private Transfers only.

## [◆ ](#ga6ba89782a8646f96dc1f9fa3b9cd2058)I3C\_MSG\_READ

| #define I3C\_MSG\_READ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Read message from I3C bus.

## [◆ ](#gad9ff03f4fdcb117b90c17d667a49c295)I3C\_MSG\_RESTART

| #define I3C\_MSG\_RESTART   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

RESTART I3C transaction for this message.

Note
:   Not all I3C drivers have or require explicit support for this feature. Some drivers require this be present on a read message that follows a write, or vice-versa. Some drivers will merge adjacent fragments into a single transaction using this flag; some will not.

## [◆ ](#ga0d4ae269a53af945837d158f638d8b5c)I3C\_MSG\_STOP

| #define I3C\_MSG\_STOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Send STOP after this message.

## [◆ ](#ga72f9fb65d218521ad006febf3dd6851b)I3C\_MSG\_WRITE

| #define I3C\_MSG\_WRITE   (0U << 0U) |
| --- |

`#include <[i3c.h](i3c_8h.md)>`

Write message to I3C bus.

## Function Documentation

## [◆ ](#ga3e4d985a784618efad67f8550f715115)i3c\_burst\_read()

| | int i3c\_burst\_read | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Read multiple bytes from an internal address of an I3C target device.

This routine reads multiple bytes from an internal address of an I3C target device synchronously.

Instances of this may be replaced by [i3c\_write\_read()](#ga3da2e99b667eab4fd92f5c0e1b57a8ea).

Parameters
:   | target | I3C target device descriptor, |
    | --- | --- |
    | start\_addr | Internal address from which the data is being read. |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes being read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#gaee773f95fcaf6cb88ced47f5c512c78c)i3c\_burst\_write()

| | int i3c\_burst\_write | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr*, | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Write multiple bytes to an internal address of an I3C target device.

This routine writes multiple bytes to an internal address of an I3C target device synchronously.

Warning
:   The combined write synthesized by this API may not be supported on all I3C devices. Uses of this API may be made more portable by replacing them with calls to [i3c\_write()](#gaa3b61aa9813ccb0df80562b0829d95dd) passing a buffer containing the combined address and data.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | start\_addr | Internal address to which the data is being written. |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes being written. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga61098371d2492a3f35c0fa779a88b348)i3c\_dump\_msgs()

| void i3c\_dump\_msgs | ( | const char \* | *name*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_msg](structi3c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs*, |
|  |  | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* ) |

`#include <[i3c.h](i3c_8h.md)>`

Dump out an I3C message.

Dumps out a list of I3C messages. For any that are writes (W), the data is displayed in hex.

It looks something like this (with name "testing"):

D: I3C msg: testing, addr=56

D: W len=01:

D: contents:

D: 06 |.

D: W len=0e:

D: contents:

D: 00 01 02 03 04 05 06 07 |........

D: 08 09 0a 0b 0c 0[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) |......

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

Parameters
:   | name | Name of this dump, displayed at the top. |
    | --- | --- |
    | msgs | Array of messages to dump. |
    | num\_msgs | Number of messages to dump. |
    | target | I3C target device descriptor. |

## [◆ ](#gaba39bd08ab50c5737ba617f4d27c3541)i3c\_read()

| | int i3c\_read | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Read a set amount of data from an I3C target device.

This routine reads a set amount of data synchronously.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | buf | Memory pool that stores the retrieved data. |
    | num\_bytes | Number of bytes to read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga87c1f23c94d37dfbaa22e4679fb8130a)i3c\_reg\_read\_byte()

| | int i3c\_reg\_read\_byte | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Read internal register of an I3C target device.

This routine reads the value of an 8-bit internal register of an I3C target device synchronously.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | reg\_addr | Address of the internal register being read. |
    | value | Memory pool that stores the retrieved register value. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga4e0488ff21cbe99b206c115017473ed9)i3c\_reg\_update\_byte()

| | int i3c\_reg\_update\_byte | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Update internal register of an I3C target device.

This routine updates the value of a set of bits from an 8-bit internal register of an I3C target device synchronously.

Note
:   If the calculated new register value matches the value that was read this function will not generate a write operation.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | reg\_addr | Address of the internal register being updated. |
    | mask | Bitmask for updating internal register. |
    | value | Value for updating internal register. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#gaf7033eb93fd3779ffa98eb83e5a1a1b1)i3c\_reg\_write\_byte()

| | int i3c\_reg\_write\_byte | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *reg\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Write internal register of an I3C target device.

This routine writes a value to an 8-bit internal register of an I3C target device synchronously.

Note
:   This function internally combines the register and value into a single bus transaction.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | reg\_addr | Address of the internal register being written. |
    | value | Value to be written to internal register. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)i3c\_transfer()

| int i3c\_transfer | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_msg](structi3c__msg.md) \* | *msgs*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_msgs* ) |

`#include <[i3c.h](i3c_8h.md)>`

Perform data transfer from the controller to a I3C target device.

This routine provides a generic interface to perform data transfer to a target device synchronously. Use [i3c\_read()](#gaba39bd08ab50c5737ba617f4d27c3541)/i3c\_write() for simple read or write.

The array of message `msgs` must not be NULL. The number of message `num_msgs` may be zero, in which case no transfer occurs.

Note
:   Not all scatter/gather transactions can be supported by all drivers. As an example, a gather write (multiple consecutive [i3c\_msg](structi3c__msg.md "One I3C Message.") buffers all configured for [I3C\_MSG\_WRITE](#ga72f9fb65d218521ad006febf3dd6851b)) may be packed into a single transaction by some drivers, but others may emit each fragment as a distinct write transaction, which will not produce the same behavior. See the documentation of [i3c\_msg](structi3c__msg.md "One I3C Message.") for limitations on support for multi-message bus transactions.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | msgs | Array of messages to transfer. |
    | num\_msgs | Number of messages to transfer. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#gaa3b61aa9813ccb0df80562b0829d95dd)i3c\_write()

| | int i3c\_write | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_bytes* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Write a set amount of data to an I3C target device.

This routine writes a set amount of data synchronously.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | buf | Memory pool from which the data is transferred. |
    | num\_bytes | Number of bytes to write. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

## [◆ ](#ga3da2e99b667eab4fd92f5c0e1b57a8ea)i3c\_write\_read()

| | int i3c\_write\_read | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | const void \* | *write\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_write*, | |  |  | void \* | *read\_buf*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_read* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i3c.h](i3c_8h.md)>`

Write then read data from an I3C target device.

This supports the common operation "this is what I want", "now give
it to me" transaction pair through a combined write-then-read bus transaction.

Parameters
:   | target | I3C target device descriptor. |
    | --- | --- |
    | write\_buf | Pointer to the data to be written |
    | num\_write | Number of bytes to write |
    | read\_buf | Pointer to storage for read data |
    | num\_read | Number of bytes to read |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EBUSY | Bus is busy. |
    | -EIO | General input / output error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
