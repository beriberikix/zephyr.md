---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bootmode_8h_source.html
original_path: doxygen/html/bootmode_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bootmode.h

[Go to the documentation of this file.](bootmode_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_RETENTION\_BOOTMODE\_

13#define ZEPHYR\_INCLUDE\_RETENTION\_BOOTMODE\_

14

15#include <[stdint.h](stdint_8h.md)>

16#include <stddef.h>

17#include <[zephyr/kernel.h](kernel_8h.md)>

18#include <[zephyr/device.h](device_8h.md)>

19#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

20

21#ifdef \_\_cplusplus

22extern "C" {

23#endif

24

31

[ 32](group__boot__mode__interface.md#ga0ef8476e9ece13f7bf8bd83dd6290cbf)enum [BOOT\_MODE\_TYPES](group__boot__mode__interface.md#ga0ef8476e9ece13f7bf8bd83dd6290cbf) {

[ 34](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241) [BOOT\_MODE\_TYPE\_NORMAL](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241) = 0x00,

35

[ 37](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa36dc141ab12f3e759be685de443bda13) [BOOT\_MODE\_TYPE\_BOOTLOADER](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa36dc141ab12f3e759be685de443bda13),

38};

39

[ 49](group__boot__mode__interface.md#gaf48099813e4857baf1c049f4e64cf608)int [bootmode\_check](group__boot__mode__interface.md#gaf48099813e4857baf1c049f4e64cf608)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode);

50

[ 59](group__boot__mode__interface.md#gaab5686ba28fa96363129be82c646d0da)int [bootmode\_set](group__boot__mode__interface.md#gaab5686ba28fa96363129be82c646d0da)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode);

60

[ 68](group__boot__mode__interface.md#ga8d40754ab808ea63882c356b0d851c75)int [bootmode\_clear](group__boot__mode__interface.md#ga8d40754ab808ea63882c356b0d851c75)(void);

69

73

74#ifdef \_\_cplusplus

75}

76#endif

77

78#endif /\* ZEPHYR\_INCLUDE\_RETENTION\_BOOTMODE\_ \*/

[device.h](device_8h.md)

[BOOT\_MODE\_TYPES](group__boot__mode__interface.md#ga0ef8476e9ece13f7bf8bd83dd6290cbf)

BOOT\_MODE\_TYPES

**Definition** bootmode.h:32

[bootmode\_clear](group__boot__mode__interface.md#ga8d40754ab808ea63882c356b0d851c75)

int bootmode\_clear(void)

Clear boot mode value (sets to 0) - which corresponds to BOOT\_MODE\_TYPE\_NORMAL.

[bootmode\_set](group__boot__mode__interface.md#gaab5686ba28fa96363129be82c646d0da)

int bootmode\_set(uint8\_t boot\_mode)

Sets boot mode of device.

[bootmode\_check](group__boot__mode__interface.md#gaf48099813e4857baf1c049f4e64cf608)

int bootmode\_check(uint8\_t boot\_mode)

Checks if the boot mode of the device is set to a specific value.

[BOOT\_MODE\_TYPE\_BOOTLOADER](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa36dc141ab12f3e759be685de443bda13)

@ BOOT\_MODE\_TYPE\_BOOTLOADER

Bootloader boot mode (e.g.

**Definition** bootmode.h:37

[BOOT\_MODE\_TYPE\_NORMAL](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241)

@ BOOT\_MODE\_TYPE\_NORMAL

Default (normal) boot, to user application.

**Definition** bootmode.h:34

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [retention](dir_acb4c99582103da541bc87f13e94ee5a.md)
- [bootmode.h](bootmode_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
