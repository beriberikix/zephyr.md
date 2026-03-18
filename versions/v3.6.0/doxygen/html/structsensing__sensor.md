---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsensing__sensor.html
original_path: doxygen/html/structsensing__sensor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor Struct Reference

[Sensing](group__sensing.md) » [Sensing Sensor API](group__sensing__sensor.md)

Internal sensor instance data structure.
[More...](#details)

`#include <[sensing_sensor.h](sensing__sensor_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#a08f7ce5927273e550e095b86d21c9abd) |
| const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \* | [info](#aee23cc4afccaf3cbbbe00afa54575098) |
| const struct [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md) \* | [register\_info](#ad87ede91d87dac49cc53a91cf08c6565) |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [reporter\_num](#a229ec163e8e8f3842495ab039e869ca9) |
| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) | [client\_list](#a0874639b380cce49fb8a9bd9ae2dd68d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [interval](#a1f975314ddbaec330a284d0865946f85) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sensitivity\_count](#aa21babb895f8aca56d415e862d4b79f7) |
| int | [sensitivity](#a2bba0047276fbb6b3586f301ec9d5e8c) [CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT] |
| enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) | [state](#aa7d285c1c281f0c3ab8fc1d8ad8fea5b) |
| struct [rtio\_iodev](structrtio__iodev.md) \* | [iodev](#aa62ec63a776d0debd76acee9b7459712) |
| struct k\_timer | [timer](#a7e28a435642cafa2641b84186d28e21f) |
| struct [rtio\_sqe](structrtio__sqe.md) \* | [stream\_sqe](#ab8d7a1a062241fd56e94defd13357302) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flag](#af8ae1aaef2e5d96cf00145901124f6aa) |
| struct [sensing\_connection](structsensing__connection.md) \* | [conns](#a7a10e55364207ff3e6464784933c874f) |

## Detailed Description

Internal sensor instance data structure.

Each sensor instance will have its unique data structure for storing all it's related information.

Sensor management will enumerate all these instance data structures, build report relationship model base on them, etc.

## Field Documentation

## [◆ ](#a0874639b380cce49fb8a9bd9ae2dd68d)client\_list

| [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) sensing\_sensor::client\_list |
| --- |

## [◆ ](#a7a10e55364207ff3e6464784933c874f)conns

| struct [sensing\_connection](structsensing__connection.md)\* sensing\_sensor::conns |
| --- |

## [◆ ](#a08f7ce5927273e550e095b86d21c9abd)dev

| const struct [device](structdevice.md)\* sensing\_sensor::dev |
| --- |

## [◆ ](#af8ae1aaef2e5d96cf00145901124f6aa)flag

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) sensing\_sensor::flag |
| --- |

## [◆ ](#aee23cc4afccaf3cbbbe00afa54575098)info

| const struct [sensing\_sensor\_info](structsensing__sensor__info.md)\* sensing\_sensor::info |
| --- |

## [◆ ](#a1f975314ddbaec330a284d0865946f85)interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor::interval |
| --- |

## [◆ ](#aa62ec63a776d0debd76acee9b7459712)iodev

| struct [rtio\_iodev](structrtio__iodev.md)\* sensing\_sensor::iodev |
| --- |

## [◆ ](#ad87ede91d87dac49cc53a91cf08c6565)register\_info

| const struct [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md)\* sensing\_sensor::register\_info |
| --- |

## [◆ ](#a229ec163e8e8f3842495ab039e869ca9)reporter\_num

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensing\_sensor::reporter\_num |
| --- |

## [◆ ](#a2bba0047276fbb6b3586f301ec9d5e8c)sensitivity

| int sensing\_sensor::sensitivity[CONFIG\_SENSING\_MAX\_SENSITIVITY\_COUNT] |
| --- |

## [◆ ](#aa21babb895f8aca56d415e862d4b79f7)sensitivity\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sensing\_sensor::sensitivity\_count |
| --- |

## [◆ ](#aa7d285c1c281f0c3ab8fc1d8ad8fea5b)state

| enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) sensing\_sensor::state |
| --- |

## [◆ ](#ab8d7a1a062241fd56e94defd13357302)stream\_sqe

| struct [rtio\_sqe](structrtio__sqe.md)\* sensing\_sensor::stream\_sqe |
| --- |

## [◆ ](#a7e28a435642cafa2641b84186d28e21f)timer

| struct k\_timer sensing\_sensor::timer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing\_sensor.h](sensing__sensor_8h_source.md)

- [sensing\_sensor](structsensing__sensor.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
