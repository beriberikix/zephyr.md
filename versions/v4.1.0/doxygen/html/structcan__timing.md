---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcan__timing.html
original_path: doxygen/html/structcan__timing.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_timing Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [CAN Interface](group__can__interface.md)

CAN bus timing structure.
[More...](#details)

`#include <[can.h](drivers_2can_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sjw](#a5af76a4ee9c741642ec19265a47fceb5) |
|  | Synchronisation jump width. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [prop\_seg](#ac009d40fee9788b663963978498b2ee9) |
|  | Propagation segment. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [phase\_seg1](#a9941688e79fa4ce01c4b498433319089) |
|  | Phase segment 1. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [phase\_seg2](#a6ca0caf618d28a761c3c8859ed3a68d6) |
|  | Phase segment 2. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [prescaler](#a74fb8341cbb6d97721c9d0afbc7e1f3a) |
|  | Prescaler value. |

## Detailed Description

CAN bus timing structure.

This struct is used to pass bus timing values to the configuration and bitrate calculation functions.

The propagation segment represents the time of the signal propagation. Phase segment 1 and phase segment 2 define the sampling point. The [prop\_seg](#ac009d40fee9788b663963978498b2ee9) and [phase\_seg1](#a9941688e79fa4ce01c4b498433319089) values affect the sampling point in the same way and some controllers only have a register for the sum of those two. The sync segment always has a length of 1 time quantum (see below).

+---------+----------+------------+------------+

|sync\_seg | prop\_seg | phase\_seg1 | phase\_seg2 |

+---------+----------+------------+------------+

^

Sampling-Point

1 time quantum (tq) has the length of 1/(core\_clock / prescaler). The bitrate is defined by the core clock divided by the prescaler and the sum of the segments:

br = (core\_clock / prescaler) / (1 + prop\_seg + phase\_seg1 + phase\_seg2)

The Synchronization Jump Width (SJW) defines the amount of time quanta the sample point can be moved. The sample point is moved when resynchronization is needed.

## Field Documentation

## [◆ ](#a9941688e79fa4ce01c4b498433319089)phase\_seg1

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_timing::phase\_seg1 |
| --- |

Phase segment 1.

## [◆ ](#a6ca0caf618d28a761c3c8859ed3a68d6)phase\_seg2

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_timing::phase\_seg2 |
| --- |

Phase segment 2.

## [◆ ](#a74fb8341cbb6d97721c9d0afbc7e1f3a)prescaler

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_timing::prescaler |
| --- |

Prescaler value.

## [◆ ](#ac009d40fee9788b663963978498b2ee9)prop\_seg

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_timing::prop\_seg |
| --- |

Propagation segment.

## [◆ ](#a5af76a4ee9c741642ec19265a47fceb5)sjw

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) can\_timing::sjw |
| --- |

Synchronisation jump width.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[can.h](drivers_2can_8h_source.md)

- [can\_timing](structcan__timing.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
