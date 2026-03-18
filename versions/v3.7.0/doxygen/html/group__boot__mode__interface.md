---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__boot__mode__interface.html
original_path: doxygen/html/group__boot__mode__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Boot mode interface

[Operating System Services](group__os__services.md) » [Retention API](group__retention__api.md)

Boot mode interface.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [BOOT\_MODE\_TYPES](#ga0ef8476e9ece13f7bf8bd83dd6290cbf) { [BOOT\_MODE\_TYPE\_NORMAL](#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241) = 0x00 , [BOOT\_MODE\_TYPE\_BOOTLOADER](#gga0ef8476e9ece13f7bf8bd83dd6290cbfa36dc141ab12f3e759be685de443bda13) } |

| Functions | |
| --- | --- |
| int | [bootmode\_check](#gaf48099813e4857baf1c049f4e64cf608) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode) |
|  | Checks if the boot mode of the device is set to a specific value. |
| int | [bootmode\_set](#gaab5686ba28fa96363129be82c646d0da) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) boot\_mode) |
|  | Sets boot mode of device. |
| int | [bootmode\_clear](#ga8d40754ab808ea63882c356b0d851c75) (void) |
|  | Clear boot mode value (sets to 0) - which corresponds to [BOOT\_MODE\_TYPE\_NORMAL](#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241). |

## Detailed Description

Boot mode interface.

## Enumeration Type Documentation

## [◆ ](#ga0ef8476e9ece13f7bf8bd83dd6290cbf)BOOT\_MODE\_TYPES

| enum [BOOT\_MODE\_TYPES](#ga0ef8476e9ece13f7bf8bd83dd6290cbf) |
| --- |

`#include <[bootmode.h](bootmode_8h.md)>`

| Enumerator | |
| --- | --- |
| BOOT\_MODE\_TYPE\_NORMAL | Default (normal) boot, to user application. |
| BOOT\_MODE\_TYPE\_BOOTLOADER | Bootloader boot mode (e.g.  serial recovery for MCUboot) |

## Function Documentation

## [◆ ](#gaf48099813e4857baf1c049f4e64cf608)bootmode\_check()

| int bootmode\_check | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *boot\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bootmode.h](bootmode_8h.md)>`

Checks if the boot mode of the device is set to a specific value.

Parameters
:   | boot\_mode | Expected boot mode to check. |
    | --- | --- |

Return values
:   | 1 | If successful and boot mode matches. |
    | --- | --- |
    | 0 | If boot mode does not match. |
    | -errno | Error code code. |

## [◆ ](#ga8d40754ab808ea63882c356b0d851c75)bootmode\_clear()

| int bootmode\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bootmode.h](bootmode_8h.md)>`

Clear boot mode value (sets to 0) - which corresponds to [BOOT\_MODE\_TYPE\_NORMAL](#gga0ef8476e9ece13f7bf8bd83dd6290cbfa43117c269b0c758fcbaff59d39836241).

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Error code code. |

## [◆ ](#gaab5686ba28fa96363129be82c646d0da)bootmode\_set()

| int bootmode\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *boot\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bootmode.h](bootmode_8h.md)>`

Sets boot mode of device.

Parameters
:   | boot\_mode | Boot mode value to set. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -errno | Error code code. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
