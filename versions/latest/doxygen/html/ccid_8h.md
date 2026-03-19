---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ccid_8h.html
original_path: doxygen/html/ccid_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccid.h File Reference

Header for Bluetooth Audio Content Control Identifier.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/gatt.h](gatt_8h_source.md)>`

[Go to the source code of this file.](ccid_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_CCID\_MIN](group__bt__ccid.md#ga1be6ef63b32f44100a77e48c88a9c126)   0 |
|  | Minimum CCID value. |
| #define | [BT\_CCID\_MAX](group__bt__ccid.md#gaae664247d3537ab473c2f533602b2afa)   255 |
|  | Maximum CCID value. |

| Functions | |
| --- | --- |
| int | [bt\_ccid\_alloc\_value](group__bt__ccid.md#gad621dd750e4b1c23791afc72785990fc) (void) |
|  | Allocates a CCID value. |
| const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_ccid\_find\_attr](group__bt__ccid.md#ga07845fe5cc445a35448881430f528609) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Get the GATT attribute of a CCID value. |

## Detailed Description

Header for Bluetooth Audio Content Control Identifier.

Copyright (c) 2020 Bose Corporation Copyright (c) 2021-2024 Nordic Semiconductor ASA

SPDX-License-Identifier: Apache-2.0

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [ccid.h](ccid_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
