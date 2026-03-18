---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__w1__interface.html
original_path: doxygen/html/group__w1__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

1-Wire Interface

[Device Driver APIs](group__io__interfaces.md)

1-Wire Interface
[More...](#details)

| Topics | |
| --- | --- |
|  | [1-Wire Sensor API](group__w1__sensor.md) |
|  | 1-Wire Sensor API |
|  | [1-Wire data link layer](group__w1__data__link.md) |
|  | 1-Wire data link layer |
|  | [1-Wire network layer](group__w1__network.md) |
|  | 1-Wire network layer |

| Enumerations | |
| --- | --- |
| enum | [w1\_settings\_type](#ga382989ef707709b5d26c40a394833612) { [W1\_SETTING\_SPEED](#gga382989ef707709b5d26c40a394833612a788fee2803793832c58951d623d823d5) , [W1\_SETTING\_STRONG\_PULLUP](#gga382989ef707709b5d26c40a394833612ae3293dfeaa3f1976e8cf57e694d5f811) , [W1\_SETINGS\_TYPE\_COUNT](#gga382989ef707709b5d26c40a394833612a814e27d05a04e027c52cb206aaf69b22) } |
|  | Defines the 1-Wire master settings types, which are runtime configurable. [More...](#ga382989ef707709b5d26c40a394833612) |

| Functions | |
| --- | --- |
| static int | [w1\_lock\_bus](#gab18b0f60a126d38c982730d3ad9756c1) (const struct [device](structdevice.md) \*dev) |
|  | Lock the 1-wire bus to prevent simultaneous access. |
| static int | [w1\_unlock\_bus](#ga7230fad2428ab62fa963b50e67388c19) (const struct [device](structdevice.md) \*dev) |
|  | Unlock the 1-wire bus. |

## Detailed Description

1-Wire Interface

Since
:   3.2

Version
:   0.1.0

## Enumeration Type Documentation

## [◆ ](#ga382989ef707709b5d26c40a394833612)w1\_settings\_type

| enum [w1\_settings\_type](#ga382989ef707709b5d26c40a394833612) |
| --- |

`#include <[w1.h](w1_8h.md)>`

Defines the 1-Wire master settings types, which are runtime configurable.

| Enumerator | |
| --- | --- |
| W1\_SETTING\_SPEED | Overdrive speed is enabled in case a value of 1 is passed and disabled passing 0. |
| W1\_SETTING\_STRONG\_PULLUP | The strong pullup resistor is activated immediately after the next written data block by passing a value of 1, and deactivated passing 0. |
| W1\_SETINGS\_TYPE\_COUNT | Number of different settings types. |

## Function Documentation

## [◆ ](#gab18b0f60a126d38c982730d3ad9756c1)w1\_lock\_bus()

| | int w1\_lock\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Lock the 1-wire bus to prevent simultaneous access.

This routine locks the bus to prevent simultaneous access from different threads. The calling thread waits until the bus becomes available. A thread is permitted to lock a mutex it has already locked.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

## [◆ ](#ga7230fad2428ab62fa963b50e67388c19)w1\_unlock\_bus()

| | int w1\_unlock\_bus | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1.h](w1_8h.md)>`

Unlock the 1-wire bus.

This routine unlocks the bus to permit access to bus line.

Parameters
:   | [in] | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Negative error code on error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
