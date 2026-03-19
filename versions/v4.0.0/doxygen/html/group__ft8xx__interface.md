---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ft8xx__interface.html
original_path: doxygen/html/group__ft8xx__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| typedef void(\* | [ft8xx\_int\_callback](#ga3841a8c74d795b14b7fbdd6115410217)) (void) |
|  | Callback API to inform API user that FT8xx triggered interrupt. |

| Functions | |
| --- | --- |
| void | [ft8xx\_calibrate](#gaa563d0378314c304277e5bf54ab90c47) (struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Calibrate touchscreen. |
| void | [ft8xx\_touch\_transform\_set](#gae45273c4617b565b4712a286f4f77c9c) (const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \*data) |
|  | Set touchscreen calibration data. |
| int | [ft8xx\_get\_touch\_tag](#ga532142aba69b418b1d8f19ca954ba3bf) (void) |
|  | Get tag of recently touched element. |
| void | [ft8xx\_register\_int](#ga02bded8612961be5ff72c8cf3bf4afe3) ([ft8xx\_int\_callback](#ga3841a8c74d795b14b7fbdd6115410217) callback) |
|  | Set callback executed when FT8xx triggers interrupt. |

## Detailed Description

FT8xx driver public APIs.

## Typedef Documentation

## [◆ ](#ga3841a8c74d795b14b7fbdd6115410217)ft8xx\_int\_callback

| typedef void(\* ft8xx\_int\_callback) (void) |
| --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Callback API to inform API user that FT8xx triggered interrupt.

This callback is called from IRQ context.

## Function Documentation

## [◆ ](#gaa563d0378314c304277e5bf54ab90c47)ft8xx\_calibrate()

| void ft8xx\_calibrate | ( | struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Calibrate touchscreen.

Run touchscreen calibration procedure that collects three touches from touch screen. Computed calibration result is automatically applied to the touchscreen processing and returned with `data`.

The content of `data` may be stored and used after reset in [ft8xx\_touch\_transform\_set()](#gae45273c4617b565b4712a286f4f77c9c) to avoid calibrating touchscreen after each device reset.

Parameters
:   | data | Pointer to touchscreen transform structure to populate |
    | --- | --- |

## [◆ ](#ga532142aba69b418b1d8f19ca954ba3bf)ft8xx\_get\_touch\_tag()

| int ft8xx\_get\_touch\_tag | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Get tag of recently touched element.

Returns
:   Tag value 0-255 of recently touched element

## [◆ ](#ga02bded8612961be5ff72c8cf3bf4afe3)ft8xx\_register\_int()

| void ft8xx\_register\_int | ( | [ft8xx\_int\_callback](#ga3841a8c74d795b14b7fbdd6115410217) | *callback* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Set callback executed when FT8xx triggers interrupt.

This function configures FT8xx to trigger interrupt when touch event changes tag value.

When touch event changes tag value, FT8xx activates INT line. The line is kept active until [ft8xx\_get\_touch\_tag()](#ga532142aba69b418b1d8f19ca954ba3bf) is called. It results in single execution of `callback` until [ft8xx\_get\_touch\_tag()](#ga532142aba69b418b1d8f19ca954ba3bf) is called.

Parameters
:   | callback | Pointer to function called when FT8xx triggers interrupt |
    | --- | --- |

## [◆ ](#gae45273c4617b565b4712a286f4f77c9c)ft8xx\_touch\_transform\_set()

| void ft8xx\_touch\_transform\_set | ( | const struct [ft8xx\_touch\_transform](structft8xx__touch__transform.md) \* | *data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx.h](ft8xx_8h.md)>`

Set touchscreen calibration data.

Apply given touchscreen transform data to the touchscreen processing. Data is to be obtained from calibration procedure started with [ft8xx\_calibrate()](#gaa563d0378314c304277e5bf54ab90c47).

Parameters
:   | data | Pointer to touchscreen transform structure to apply |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
