---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i3c__addresses.html
original_path: doxygen/html/group__i3c__addresses.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Address-related Helper Code

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C Address-related Helper Code.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i3c\_addr\_slots](structi3c__addr__slots.md) |
|  | Structure to keep track of addresses on I3C bus. [More...](structi3c__addr__slots.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_BROADCAST\_ADDR](#gad516c48319d08db1886719645a682787)   0x7E |
|  | Broadcast Address on I3C bus. |
| #define | [I3C\_MAX\_ADDR](#ga85a120abff94213b57ce4912f58d5ed8)   0x7F |
|  | Maximum value of device addresses. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) {     [I3C\_ADDR\_SLOT\_STATUS\_FREE](#ggaacbed5bbaae3b36d6f3ba175074aecd0a847927f32a28341e0d356c9ec1ccfb2e) = 0U , [I3C\_ADDR\_SLOT\_STATUS\_RSVD](#ggaacbed5bbaae3b36d6f3ba175074aecd0a0af543ae2b67f2e8055d496689437d45) , [I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV](#ggaacbed5bbaae3b36d6f3ba175074aecd0a38b0fd286477bcc936132c25d787749a) , [I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV](#ggaacbed5bbaae3b36d6f3ba175074aecd0ac8d91073cf590626b58bbf5f5b8d9c55) ,     [I3C\_ADDR\_SLOT\_STATUS\_MASK](#ggaacbed5bbaae3b36d6f3ba175074aecd0a2093cda582c682b292deb065956ca280) = 0x03U   } |
|  | Enum to indicate whether an address is reserved, has I2C/I3C device attached, or no device attached. [More...](#gaacbed5bbaae3b36d6f3ba175074aecd0) |

| Functions | |
| --- | --- |
| int | [i3c\_addr\_slots\_init](#gaf2be07d40d885f60997b5eb5edcf910f) (const struct [device](structdevice.md) \*dev) |
|  | Initialize the I3C address slots struct. |
| void | [i3c\_addr\_slots\_set](#gae4eb7e22abde57c9bcfdc8407c0da68d) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr, enum [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) status) |
|  | Set the address status of a device. |
| enum [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) | [i3c\_addr\_slots\_status](#ga3dc021699fc489995b0bbe299753a33e) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr) |
|  | Get the address status of a device. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_addr\_slots\_is\_free](#gadc2539a0b8793ec5b5ff34e57e68fb60) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_addr) |
|  | Check if the address is free. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i3c\_addr\_slots\_next\_free\_find](#gad7eddb7aebf337a31f336ccf3f78cad1) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_addr) |
|  | Find the next free address. |
| static void | [i3c\_addr\_slots\_mark\_free](#gaf384836871625543aaa3f087e688f1b4) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as free (not used) in device list. |
| static void | [i3c\_addr\_slots\_mark\_rsvd](#gac976f542afb29d2360fc2c8d797dbac5) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as reserved in device list. |
| static void | [i3c\_addr\_slots\_mark\_i3c](#gae10e6aba3335b78a2be728a5f495b436) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as I3C device in device list. |
| static void | [i3c\_addr\_slots\_mark\_i2c](#gad5fc6b00171a4fdf76de20e6da3fbb32) (struct [i3c\_addr\_slots](structi3c__addr__slots.md) \*addr\_slots, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Mark the address as I2C device in device list. |

## Detailed Description

I3C Address-related Helper Code.

## Macro Definition Documentation

## [◆ ](#gad516c48319d08db1886719645a682787)I3C\_BROADCAST\_ADDR

| #define I3C\_BROADCAST\_ADDR   0x7E |
| --- |

`#include <[addresses.h](addresses_8h.md)>`

Broadcast Address on I3C bus.

## [◆ ](#ga85a120abff94213b57ce4912f58d5ed8)I3C\_MAX\_ADDR

| #define I3C\_MAX\_ADDR   0x7F |
| --- |

`#include <[addresses.h](addresses_8h.md)>`

Maximum value of device addresses.

## Enumeration Type Documentation

## [◆ ](#gaacbed5bbaae3b36d6f3ba175074aecd0)i3c\_addr\_slot\_status

| enum [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) |
| --- |

`#include <[addresses.h](addresses_8h.md)>`

Enum to indicate whether an address is reserved, has I2C/I3C device attached, or no device attached.

| Enumerator | |
| --- | --- |
| I3C\_ADDR\_SLOT\_STATUS\_FREE | Address has not device attached. |
| I3C\_ADDR\_SLOT\_STATUS\_RSVD | Address is reserved. |
| I3C\_ADDR\_SLOT\_STATUS\_I3C\_DEV | Address is associated with an I3C device. |
| I3C\_ADDR\_SLOT\_STATUS\_I2C\_DEV | Address is associated with an I2C device. |
| I3C\_ADDR\_SLOT\_STATUS\_MASK | Bit masks used to filter status bits. |

## Function Documentation

## [◆ ](#gaf2be07d40d885f60997b5eb5edcf910f)i3c\_addr\_slots\_init()

| int i3c\_addr\_slots\_init | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[addresses.h](addresses_8h.md)>`

Initialize the I3C address slots struct.

This clears out the assigned address bits, and set the reserved address bits according to the I3C specification.

Parameters
:   | dev | Pointer to controller device driver instance. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EINVAL | if duplicate addresses. |

## [◆ ](#gadc2539a0b8793ec5b5ff34e57e68fb60)i3c\_addr\_slots\_is\_free()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_addr\_slots\_is\_free | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *slots*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dev\_addr* ) |

`#include <[addresses.h](addresses_8h.md)>`

Check if the address is free.

Parameters
:   | slots | Pointer to the address slots structure. |
    | --- | --- |
    | dev\_addr | Device address. |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if address is free. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if address is not free. |

## [◆ ](#gaf384836871625543aaa3f087e688f1b4)i3c\_addr\_slots\_mark\_free()

| | void i3c\_addr\_slots\_mark\_free | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *addr\_slots*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addresses.h](addresses_8h.md)>`

Mark the address as free (not used) in device list.

Parameters
:   | addr\_slots | Pointer to the address slots struct. |
    | --- | --- |
    | addr | Device address. |

## [◆ ](#gad5fc6b00171a4fdf76de20e6da3fbb32)i3c\_addr\_slots\_mark\_i2c()

| | void i3c\_addr\_slots\_mark\_i2c | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *addr\_slots*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addresses.h](addresses_8h.md)>`

Mark the address as I2C device in device list.

Parameters
:   | addr\_slots | Pointer to the address slots struct. |
    | --- | --- |
    | addr | Device address. |

## [◆ ](#gae10e6aba3335b78a2be728a5f495b436)i3c\_addr\_slots\_mark\_i3c()

| | void i3c\_addr\_slots\_mark\_i3c | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *addr\_slots*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addresses.h](addresses_8h.md)>`

Mark the address as I3C device in device list.

Parameters
:   | addr\_slots | Pointer to the address slots struct. |
    | --- | --- |
    | addr | Device address. |

## [◆ ](#gac976f542afb29d2360fc2c8d797dbac5)i3c\_addr\_slots\_mark\_rsvd()

| | void i3c\_addr\_slots\_mark\_rsvd | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *addr\_slots*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[addresses.h](addresses_8h.md)>`

Mark the address as reserved in device list.

Parameters
:   | addr\_slots | Pointer to the address slots struct. |
    | --- | --- |
    | addr | Device address. |

## [◆ ](#gad7eddb7aebf337a31f336ccf3f78cad1)i3c\_addr\_slots\_next\_free\_find()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_addr\_slots\_next\_free\_find | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *slots*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_addr* ) |

`#include <[addresses.h](addresses_8h.md)>`

Find the next free address.

This can be used to find the next free address that can be assigned to a new device.

Parameters
:   | slots | Pointer to the address slots structure. |
    | --- | --- |
    | start\_addr | Where to start searching |

Returns
:   The next free address, or 0 if none found.

## [◆ ](#gae4eb7e22abde57c9bcfdc8407c0da68d)i3c\_addr\_slots\_set()

| void i3c\_addr\_slots\_set | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *slots*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dev\_addr*, |
|  |  | enum [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) | *status* ) |

`#include <[addresses.h](addresses_8h.md)>`

Set the address status of a device.

Parameters
:   | slots | Pointer to the address slots structure. |
    | --- | --- |
    | dev\_addr | Device address. |
    | status | New status for the address `dev_addr`. |

## [◆ ](#ga3dc021699fc489995b0bbe299753a33e)i3c\_addr\_slots\_status()

| enum [i3c\_addr\_slot\_status](#gaacbed5bbaae3b36d6f3ba175074aecd0) i3c\_addr\_slots\_status | ( | struct [i3c\_addr\_slots](structi3c__addr__slots.md) \* | *slots*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dev\_addr* ) |

`#include <[addresses.h](addresses_8h.md)>`

Get the address status of a device.

Parameters
:   | slots | Pointer to the address slots structure. |
    | --- | --- |
    | dev\_addr | Device address. |

Returns
:   Address status for the address `dev_addr`.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
