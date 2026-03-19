---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ft8xx__interface.html
original_path: doxygen/html/group__ft8xx__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx driver APIs

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md)

FT8xx driver public APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [FT8xx co-processor](group__ft8xx__copro.md) |
|  | FT8xx co-processor engine functions. |
|  | [FT8xx common functions](group__ft8xx__common.md) |
|  | FT8xx functions to write and read memory. |
|  | [FT8xx display list](group__ft8xx__dl.md) |
|  | FT8xx display list commands. |
|  | [FT8xx memory map](group__ft8xx__memory.md) |
|  | FT8xx memory addresses. |
|  | [FT8xx reference API](group__ft8xx__reference__api.md) |
|  | FT8xx reference API. |

| Data Structures | |
| --- | --- |
| struct | [ft8xx\_touch\_transform](structft8xx__touch__transform.md) |
|  | Structure holding touchscreen calibration data. [More...](structft8xx__touch__transform.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [ft8xx\_int\_callback](#ga846a90d72b56f388d5b4f60cf6d658b0)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Callback API to inform API user that FT8xx triggered interrupt. |

| Functions | |
| --- | --- |
| void | [ft8xx\_calibrate](#ga586f6ff1eddd5b596d2e35fb5fdd8148) (const struct [device](structdevice.md) \*dev, struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Calibrate touchscreen. |
| void | [ft8xx\_touch\_transform\_set](#ga1d74a13782c6ab9f8b07a28503058356) (const struct [device](structdevice.md) \*dev, const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Set touchscreen calibration data. |
| int | [ft8xx\_get\_touch\_tag](#gaea3589b5a0aa34a09a81ea15c1595219) (const struct [device](structdevice.md) \*dev) |
|  | Get tag of recently touched element. |
| void | [ft8xx\_register\_int](#gaf392199312ddb82451a4f31e2955079d) (const struct [device](structdevice.md) \*dev, [ft8xx\_int\_callback](#ga846a90d72b56f388d5b4f60cf6d658b0) callback, void \*user\_data) |
|  | Set callback executed when FT8xx triggers interrupt. |

## Detailed Description

FT8xx driver public APIs.

## Typedef Documentation

## [◆ ](#ga846a90d72b56f388d5b4f60cf6d658b0)ft8xx\_int\_callback

| typedef void(\* ft8xx\_int\_callback) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
| --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Callback API to inform API user that FT8xx triggered interrupt.

This callback is called from IRQ context.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | user\_data | Pointer to user data provided during callback registration |

## Function Documentation

## [◆ ](#ga586f6ff1eddd5b596d2e35fb5fdd8148)ft8xx\_calibrate()

| void ft8xx\_calibrate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \* | *data* ) |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Calibrate touchscreen.

Run touchscreen calibration procedure that collects three touches from touch screen. Computed calibration result is automatically applied to the touchscreen processing and returned with `data`.

The content of `data` may be stored and used after reset in [ft8xx\_touch\_transform\_set()](#ga1d74a13782c6ab9f8b07a28503058356) to avoid calibrating touchscreen after each device reset.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | data | Pointer to touchscreen transform structure to populate |

## [◆ ](#gaea3589b5a0aa34a09a81ea15c1595219)ft8xx\_get\_touch\_tag()

| int ft8xx\_get\_touch\_tag | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Get tag of recently touched element.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |

Returns
:   Tag value 0-255 of recently touched element

## [◆ ](#gaf392199312ddb82451a4f31e2955079d)ft8xx\_register\_int()

| void ft8xx\_register\_int | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [ft8xx\_int\_callback](#ga846a90d72b56f388d5b4f60cf6d658b0) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Set callback executed when FT8xx triggers interrupt.

This function configures FT8xx to trigger interrupt when touch event changes tag value.

When touch event changes tag value, FT8xx activates INT line. The line is kept active until [ft8xx\_get\_touch\_tag()](#gaea3589b5a0aa34a09a81ea15c1595219) is called. It results in single execution of `callback` until [ft8xx\_get\_touch\_tag()](#gaea3589b5a0aa34a09a81ea15c1595219) is called.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | callback | Pointer to function called when FT8xx triggers interrupt |
    | user\_data | Pointer to user data to be passed to the `callback` |

## [◆ ](#ga1d74a13782c6ab9f8b07a28503058356)ft8xx\_touch\_transform\_set()

| void ft8xx\_touch\_transform\_set | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \* | *data* ) |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Set touchscreen calibration data.

Apply given touchscreen transform data to the touchscreen processing. Data is to be obtained from calibration procedure started with [ft8xx\_calibrate()](#ga586f6ff1eddd5b596d2e35fb5fdd8148).

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | data | Pointer to touchscreen transform structure to apply |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
