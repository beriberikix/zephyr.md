---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/swdp_8h.html
original_path: doxygen/html/swdp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

swdp.h File Reference

Serial Wire Debug Port interface driver API.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](swdp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [swdp\_api](structswdp__api.md) |

| Macros | |
| --- | --- |
| #define | [SWDP\_REQUEST\_APnDP](#a8a41667b3516d49ad5785669a659fa0b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SWDP\_REQUEST\_RnW](#adc8522fcb5dd2d68b07d82b60d2324e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [SWDP\_REQUEST\_A2](#a2a48349320bd17c6495e96f53738645c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [SWDP\_REQUEST\_A3](#a30ec6eccc9dc5f4254eceb887b33caf7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [SWDP\_ACK\_OK](#accc95b6569bfdcb9969b62e49e4a7869)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SWDP\_ACK\_WAIT](#aaa8df6e1403dd7ca964acdfd3eba5c42)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [SWDP\_ACK\_FAULT](#a6f67ce6246bda2a4f11fbef88de8050e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [SWDP\_TRANSFER\_ERROR](#a0c5587d14f0b68fa639558f768f24e90)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [SWDP\_SWCLK\_PIN](#a04d9dbfa1c6303adfbf22ea14c589a5d)   0U |
| #define | [SWDP\_SWDIO\_PIN](#af0d50f9d503900ad9a7e3dd0d40aae4e)   1U |
| #define | [SWDP\_nRESET\_PIN](#a2cad01a3a938093f7b7ec2ddc0fcdc2d)   7U |

## Detailed Description

Serial Wire Debug Port interface driver API.

## Macro Definition Documentation

## [◆ ](#a6f67ce6246bda2a4f11fbef88de8050e)SWDP\_ACK\_FAULT

| #define SWDP\_ACK\_FAULT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#accc95b6569bfdcb9969b62e49e4a7869)SWDP\_ACK\_OK

| #define SWDP\_ACK\_OK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#aaa8df6e1403dd7ca964acdfd3eba5c42)SWDP\_ACK\_WAIT

| #define SWDP\_ACK\_WAIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a2cad01a3a938093f7b7ec2ddc0fcdc2d)SWDP\_nRESET\_PIN

| #define SWDP\_nRESET\_PIN   7U |
| --- |

## [◆ ](#a2a48349320bd17c6495e96f53738645c)SWDP\_REQUEST\_A2

| #define SWDP\_REQUEST\_A2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a30ec6eccc9dc5f4254eceb887b33caf7)SWDP\_REQUEST\_A3

| #define SWDP\_REQUEST\_A3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a8a41667b3516d49ad5785669a659fa0b)SWDP\_REQUEST\_APnDP

| #define SWDP\_REQUEST\_APnDP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#adc8522fcb5dd2d68b07d82b60d2324e3)SWDP\_REQUEST\_RnW

| #define SWDP\_REQUEST\_RnW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a04d9dbfa1c6303adfbf22ea14c589a5d)SWDP\_SWCLK\_PIN

| #define SWDP\_SWCLK\_PIN   0U |
| --- |

## [◆ ](#af0d50f9d503900ad9a7e3dd0d40aae4e)SWDP\_SWDIO\_PIN

| #define SWDP\_SWDIO\_PIN   1U |
| --- |

## [◆ ](#a0c5587d14f0b68fa639558f768f24e90)SWDP\_TRANSFER\_ERROR

| #define SWDP\_TRANSFER\_ERROR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [swdp.h](swdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
