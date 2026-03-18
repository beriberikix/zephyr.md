---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__bas.html
original_path: doxygen/html/group__bt__bas.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Battery Service (BAS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Battery Service (BAS).
[More...](#details)

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_bas\_get\_battery\_level](#gadbe0f52d04d90372d603af66b693e980) (void) |
|  | Read battery level value. |
| int | [bt\_bas\_set\_battery\_level](#gac8d519830c34b9c8370366e2593dbeba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Update battery level value. |

## Detailed Description

Battery Service (BAS).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Function Documentation

## [◆ ](#gadbe0f52d04d90372d603af66b693e980)bt\_bas\_get\_battery\_level()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bas\_get\_battery\_level | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Read battery level value.

Read the characteristic value of the battery level

Returns
:   The battery level in percent.

## [◆ ](#gac8d519830c34b9c8370366e2593dbeba)bt\_bas\_set\_battery\_level()

| int bt\_bas\_set\_battery\_level | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Update battery level value.

Update the characteristic value of the battery level This will send a GATT notification to all current subscribers.

Parameters
:   | level | The battery level in percent. |
    | --- | --- |

Returns
:   Zero in case of success and error code in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
