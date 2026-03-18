---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/lc3_8h.html
original_path: doxygen/html/lc3_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lc3.h File Reference

Bluetooth LC3 codec handling.
[More...](#details)

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[zephyr/bluetooth/byteorder.h](bluetooth_2byteorder_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci_types.h](hci__types_8h_source.md)>`

[Go to the source code of this file.](lc3_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](group__BT__AUDIO__CODEC__LC3.md#ga8d679b241585ff5ebff0d97bb22dfda9)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu) |
|  | Helper to declare LC3 codec capability. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_META](group__BT__AUDIO__CODEC__LC3.md#ga9b5d5e300a7b41060329dbdd2cd073f6)(\_prefer\_context) |
|  | Helper to declare LC3 codec metadata. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3](group__BT__AUDIO__CODEC__LC3.md#gac474746e7314ebf7ed77b8937191cdc1)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu, \_prefer\_context) |
|  | Helper to declare LC3 codec. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](group__BT__AUDIO__CODEC__LC3.md#ga497ff0aa1d7dcfeea6ec549e5fb155d6)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu) |
|  | Helper to declare LC3 codec data configuration. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_META](group__BT__AUDIO__CODEC__LC3.md#ga2c00f8bd526305d878624c6f1b8030f8)(\_stream\_context) |
|  | Helper to declare LC3 codec metadata configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__BT__AUDIO__CODEC__LC3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context) |
|  | Helper to declare LC3 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_1](group__BT__AUDIO__CODEC__LC3.md#gaee65a79f2bb704bf5296b778a0e3ad2c)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 8.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_8\_2](group__BT__AUDIO__CODEC__LC3.md#gae279ffa1d4eef72d94083bdae968c102)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 8.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_1](group__BT__AUDIO__CODEC__LC3.md#gaff29f4ccabab99c7e25fcbf9d10cc789)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_16\_2](group__BT__AUDIO__CODEC__LC3.md#gabf16c8c87682fd9faf180af129bddfd5)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 16.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_1](group__BT__AUDIO__CODEC__LC3.md#ga0655c6ca0c99002493a854cb88969a2b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 24.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_24\_2](group__BT__AUDIO__CODEC__LC3.md#gae8c8a34377b910f52d851dadb9f4216b)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 24.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_1](group__BT__AUDIO__CODEC__LC3.md#ga57a7bf0bbf38e70cfc27e1c267092277)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_32\_2](group__BT__AUDIO__CODEC__LC3.md#ga25879311182d38adaca5238cdf016ac4)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 32.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_1](group__BT__AUDIO__CODEC__LC3.md#gad046616ed5367d1e2c674df545def632)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 441.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_441\_2](group__BT__AUDIO__CODEC__LC3.md#ga7789d2447105581e5e520c930f19f8ed)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 441.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_1](group__BT__AUDIO__CODEC__LC3.md#ga613c2f21212b626f83e37c5614e7129e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.1 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_2](group__BT__AUDIO__CODEC__LC3.md#gab5342debdef776007a78576f8d0917dd)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.2 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_3](group__BT__AUDIO__CODEC__LC3.md#ga60f65e6c9b9f940a66756f91c82cd64e)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.3 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_4](group__BT__AUDIO__CODEC__LC3.md#gaefa8bdddf5b56cad4b9096eac1abb49d)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.4 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_5](group__BT__AUDIO__CODEC__LC3.md#ga3366230cd60d3e3b05e7cb2a56cfdd26)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.5 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG\_48\_6](group__BT__AUDIO__CODEC__LC3.md#ga428a49b8528e62f6f686837dc95ba1b6)(\_loc, \_stream\_context) |
|  | Helper to declare LC3 48.6 codec configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5](group__BT__AUDIO__CODEC__LC3.md#ga5bfa82c8858a4fb3fcd7ce26afbd7601)(\_framing, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 7.5ms interval. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_7\_5\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#gac5e29e3c02fc24e5bb1208ea12c1f707)(\_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 7.5ms interval unframed input. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_10](group__BT__AUDIO__CODEC__LC3.md#gad951d0fb06dfe085db73228eef500bbc)(\_framing, \_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 10ms frame internal. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_QOS\_10\_UNFRAMED](group__BT__AUDIO__CODEC__LC3.md#ga57083d5045a806cc710b899b8de54b7d)(\_sdu, \_rtn, \_latency, \_pd) |
|  | Helper to declare LC3 codec QoS for 10ms interval unframed input. |

## Detailed Description

Bluetooth LC3 codec handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [lc3.h](lc3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
