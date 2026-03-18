---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bootmode_8h.html
original_path: doxygen/html/bootmode_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bootmode.h File Reference

Public API for boot mode interface.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](bootmode_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [BOOT\_MODE\_TYPES](group__boot__mode__interface.md#ga0ef8476e9ece13f7bf8bd83dd6290cbf) { [BOOT\_MODE\_TYPE\_NORMAL](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241) = 0x00 , [BOOT\_MODE\_TYPE\_BOOTLOADER](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa36dc141ab12f3e759be685de443bda13) } |

| Functions | |
| --- | --- |
| int | [bootmode\_check](group__boot__mode__interface.md#gaf48099813e4857baf1c049f4e64cf608) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode) |
|  | Checks if the boot mode of the device is set to a specific value. |
| int | [bootmode\_set](group__boot__mode__interface.md#gaab5686ba28fa96363129be82c646d0da) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode) |
|  | Sets boot mode of device. |
| int | [bootmode\_clear](group__boot__mode__interface.md#ga8d40754ab808ea63882c356b0d851c75) (void) |
|  | Clear boot mode value (sets to 0) - which corresponds to [BOOT\_MODE\_TYPE\_NORMAL](group__boot__mode__interface.md#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241 "Default (normal) boot, to user application."). |

## Detailed Description

Public API for boot mode interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [retention](dir_acb4c99582103da541bc87f13e94ee5a.md)
- [bootmode.h](bootmode_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
