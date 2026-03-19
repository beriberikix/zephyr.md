---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lc3_8h.html
original_path: doxygen/html/lc3_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_DATA](group__bt__lc3.md#ga8d679b241585ff5ebff0d97bb22dfda9)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu) |
|  | Helper to declare LC3 codec capability. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3\_META](group__bt__lc3.md#ga9b5d5e300a7b41060329dbdd2cd073f6)(\_prefer\_context) |
|  | Helper to declare LC3 codec metadata. |
| #define | [BT\_AUDIO\_CODEC\_CAP\_LC3](group__bt__lc3.md#gac474746e7314ebf7ed77b8937191cdc1)(\_freq, \_duration, \_chan\_count, \_len\_min, \_len\_max, \_max\_frames\_per\_sdu, \_prefer\_context) |
|  | Helper to declare LC3 codec. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_DATA](group__bt__lc3.md#ga497ff0aa1d7dcfeea6ec549e5fb155d6)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu) |
|  | Helper to declare LC3 codec data configuration. |
| #define | [BT\_AUDIO\_CODEC\_CFG\_LC3\_META](group__bt__lc3.md#ga2c00f8bd526305d878624c6f1b8030f8)(\_stream\_context) |
|  | Helper to declare LC3 codec metadata configuration. |
| #define | [BT\_AUDIO\_CODEC\_LC3\_CONFIG](group__bt__lc3.md#ga2c5f1f9e6d80a2eef93f7b08a19ea245)(\_freq, \_duration, \_loc, \_len, \_frames\_per\_sdu, \_stream\_context) |
|  | Helper to declare LC3 codec configuration. |

## Detailed Description

Bluetooth LC3 codec handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [lc3.h](lc3_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
