---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gmap_8h.html
original_path: doxygen/html/gmap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gmap.h File Reference

Header for Bluetooth Gaming Audio Profile (GMAP).
[More...](#details)

`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](gmap_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_gmap\_feat](structbt__gmap__feat.md) |
|  | Broadcast Game Receiver Feature bitfield. [More...](structbt__gmap__feat.md#details) |
| struct | [bt\_gmap\_cb](structbt__gmap__cb.md) |
|  | Hearing Access Service Client callback structure. [More...](structbt__gmap__cb.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) { [BT\_GMAP\_ROLE\_UGG](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a81bd7f519b365fc0c5a561eb65876251) = BIT(0) , [BT\_GMAP\_ROLE\_UGT](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a39dc40eb26231dbaa69c348065df3e7b) = BIT(1) , [BT\_GMAP\_ROLE\_BGS](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56a3af50221c5fccaf312369de84df05fc6) = BIT(2) , [BT\_GMAP\_ROLE\_BGR](group__bt__gmap.md#gga55ecab78bcd6de6c294abdc20ad10e56ad4a06eac5d00ca74aa975b9247ca2091) = BIT(3) } |
|  | Gaming Role bitfield. [More...](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) |
| enum | [bt\_gmap\_ugg\_feat](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145) { [BT\_GMAP\_UGG\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a70a2cdce8a31196964aff898a14aac8e) = BIT(0) , [BT\_GMAP\_UGG\_FEAT\_96KBPS\_SOURCE](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a7b730d9494f970851d089efe3e444331) = BIT(1) , [BT\_GMAP\_UGG\_FEAT\_MULTISINK](group__bt__gmap.md#gga3ef43378bad84bbcd726e318cf0bc145a6a6e57e6f70e9ce083252e972c708be1) = BIT(2) } |
|  | Unicast Game Gateway Feature bitfield. [More...](group__bt__gmap.md#ga3ef43378bad84bbcd726e318cf0bc145) |
| enum | [bt\_gmap\_ugt\_feat](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48) {     [BT\_GMAP\_UGT\_FEAT\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a847ae753a75b4ce0edc9b82b4fe8b231) = BIT(0) , [BT\_GMAP\_UGT\_FEAT\_80KBPS\_SOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a1344dbad5cb457db2e5e4a784f1e3b88) = BIT(1) , [BT\_GMAP\_UGT\_FEAT\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aea4002993773c9aa797e342cb5c1f69c) = BIT(2) , [BT\_GMAP\_UGT\_FEAT\_64KBPS\_SINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a67404b8c790433417f044f9acbf5b604) = BIT(3) ,     [BT\_GMAP\_UGT\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48a130739cfcc245c13ca74011e4e851a3e) = BIT(4) , [BT\_GMAP\_UGT\_FEAT\_MULTISINK](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48ad414ae2069d5443ef74f00135dd68c08) = BIT(5) , [BT\_GMAP\_UGT\_FEAT\_MULTISOURCE](group__bt__gmap.md#gga0fe87d6d1412c15564ba7de29e3d7a48aa9c3b2b1644bea91becd606762bb7045) = BIT(6)   } |
|  | Unicast Game Terminal Feature bitfield. [More...](group__bt__gmap.md#ga0fe87d6d1412c15564ba7de29e3d7a48) |
| enum | [bt\_gmap\_bgs\_feat](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf) { [BT\_GMAP\_BGS\_FEAT\_96KBPS](group__bt__gmap.md#gga3a79c408b283864616a522b1f04cacafa4e383721a606a400d80d135c58c1cae8) = BIT(0) } |
|  | Broadcast Game Sender Feature bitfield. [More...](group__bt__gmap.md#ga3a79c408b283864616a522b1f04cacaf) |
| enum | [bt\_gmap\_bgr\_feat](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c) { [BT\_GMAP\_BGR\_FEAT\_MULTISINK](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca1f75031c1d772852f672760da86be630) = BIT(0) , [BT\_GMAP\_BGR\_FEAT\_MULTIPLEX](group__bt__gmap.md#gga9c1145ad5334e14d4978b6d7d3c84b6ca58455f982bc0356bc47e51e27e0e2ce6) = BIT(1) } |
|  | Broadcast Game Receiver Feature bitfield. [More...](group__bt__gmap.md#ga9c1145ad5334e14d4978b6d7d3c84b6c) |

| Functions | |
| --- | --- |
| int | [bt\_gmap\_cb\_register](group__bt__gmap.md#gacc4853bf69d0a13353fc941aa7e4e190) (const struct [bt\_gmap\_cb](structbt__gmap__cb.md) \*cb) |
|  | Registers the callbacks used by the Gaming Audio Profile. |
| int | [bt\_gmap\_discover](group__bt__gmap.md#gab54963e226753d44085a7d1f5dccdef6) (struct bt\_conn \*conn) |
|  | Discover Gaming Service on a remote device. |
| int | [bt\_gmap\_register](group__bt__gmap.md#ga75211707bbdceff35235c353dc8c7609) (enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
|  | Adds GMAS instance to database and sets the received Gaming Audio Profile role(s). |
| int | [bt\_gmap\_set\_role](group__bt__gmap.md#ga956efe257f06b627615a0a82d44db919) (enum [bt\_gmap\_role](group__bt__gmap.md#ga55ecab78bcd6de6c294abdc20ad10e56) role, struct [bt\_gmap\_feat](structbt__gmap__feat.md) features) |
|  | Set one or multiple Gaming Audio Profile roles and features dynamically. |

## Detailed Description

Header for Bluetooth Gaming Audio Profile (GMAP).

Copyright (c) 2023-2024 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [gmap.h](gmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
