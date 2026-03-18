---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__w1__data__link.html
original_path: doxygen/html/group__w1__data__link.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

1-Wire data link layer

[Device Driver APIs](group__io__interfaces.md) » [1-Wire Interface](group__w1__interface.md)

1-Wire data link layer
[More...](#details)

| Functions | |
| --- | --- |
| int | [w1\_reset\_bus](#gab4eccd585c6f14330807055ccc151fd6) (const struct [device](structdevice.md) \*dev) |
|  | Reset the 1-Wire bus to prepare slaves for communication. |
| int | [w1\_read\_bit](#ga0f2b37163f3d7c9816371942765509b4) (const struct [device](structdevice.md) \*dev) |
|  | Read a single bit from the 1-Wire bus. |
| int | [w1\_write\_bit](#ga3671d8bbf9d044c60d7e96e4190ba2fa) (const struct [device](structdevice.md) \*dev, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bit) |
|  | Write a single bit to the 1-Wire bus. |
| int | [w1\_read\_byte](#ga868980684bb98149af5b59e3fa8a83b6) (const struct [device](structdevice.md) \*dev) |
|  | Read a single byte from the 1-Wire bus. |
| int | [w1\_write\_byte](#ga978a8f14fb8cb3a569f8b731b20cc840) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte) |
|  | Write a single byte to the 1-Wire bus. |
| int | [w1\_read\_block](#ga2967c99ec93b7c31beb9cf2a327a23f4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Read a block of data from the 1-Wire bus. |
| int | [w1\_write\_block](#gab30a58c42c06088da9e0845de7d089ce) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Write a block of data from the 1-Wire bus. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [w1\_get\_slave\_count](#ga65892855c763dccc27b508d870c1d144) (const struct [device](structdevice.md) \*dev) |
|  | Get the number of slaves on the bus. |
| int | [w1\_configure](#gae989e0deebe5666edc9ff8a3839cf216) (const struct [device](structdevice.md) \*dev, enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Configure parameters of the 1-Wire master. |

## Detailed Description

1-Wire data link layer

## Function Documentation

## [◆ ](#gae989e0deebe5666edc9ff8a3839cf216)w1\_configure()

| int w1\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612) | *type*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) |

`#include <[w1.h](w1_8h.md)>`

Configure parameters of the 1-Wire master.

Allowed configuration parameters are defined in enum [w1\_settings\_type](group__w1__interface.md#ga382989ef707709b5d26c40a394833612 "Defines the 1-Wire master settings types, which are runtime configurable."), but master devices may not support all types.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | type | Enum specifying the setting type. |
    |  | value | The new value for the passed settings type. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | The master doesn't support the configuration of the supplied type. |
    | -EIO | General input / output error, failed to configure master devices. |

## [◆ ](#ga65892855c763dccc27b508d870c1d144)w1\_get\_slave\_count()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) w1\_get\_slave\_count | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Get the number of slaves on the bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | slave\_count | Positive Number of connected 1-Wire slaves on success. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga0f2b37163f3d7c9816371942765509b4)w1\_read\_bit()

| int w1\_read\_bit | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Read a single bit from the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | rx\_bit | The read bit value on success. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga2967c99ec93b7c31beb9cf2a327a23f4)w1\_read\_block()

| int w1\_read\_block | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[w1.h](w1_8h.md)>`

Read a block of data from the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | buffer | Pointer to receive buffer. |
    |  | len | Length of receiving buffer (in bytes). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga868980684bb98149af5b59e3fa8a83b6)w1\_read\_byte()

| int w1\_read\_byte | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Read a single byte from the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | rx\_byte | The read byte value on success. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#gab4eccd585c6f14330807055ccc151fd6)w1\_reset\_bus()

| int w1\_reset\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Reset the 1-Wire bus to prepare slaves for communication.

This routine resets all 1-Wire bus slaves such that they are ready to receive a command. Connected slaves answer with a presence pulse once they are ready to receive data.

In case the driver supports both standard speed and overdrive speed, the reset routine takes care of sendig either a short or a long reset pulse depending on the current state. The speed can be changed using *[w1\_configure()](#gae989e0deebe5666edc9ff8a3839cf216)*.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | 0 | If no slaves answer with a present pulse. |
    | --- | --- |
    | 1 | If at least one slave answers with a present pulse. |
    | -errno | Negative error code on error. |

## [◆ ](#ga3671d8bbf9d044c60d7e96e4190ba2fa)w1\_write\_bit()

| int w1\_write\_bit | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *bit* ) |

`#include <[w1.h](w1_8h.md)>`

Write a single bit to the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | bit | Transmitting bit value 1 or 0. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#gab30a58c42c06088da9e0845de7d089ce)w1\_write\_block()

| int w1\_write\_block | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[w1.h](w1_8h.md)>`

Write a block of data from the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [in] | buffer | Pointer to transmitting buffer. |
    |  | len | Length of transmitting buffer (in bytes). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga978a8f14fb8cb3a569f8b731b20cc840)w1\_write\_byte()

| int w1\_write\_byte | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *byte* ) |

`#include <[w1.h](w1_8h.md)>`

Write a single byte to the 1-Wire bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    |  | byte | Transmitting byte. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
