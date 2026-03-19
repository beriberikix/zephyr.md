---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__cts.html
original_path: doxygen/html/group__bt__cts.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Current Time Service (CTS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Current Time Service (CTS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_cts\_time\_format](structbt__cts__time__format.md) |
|  | Current Time service data format, Please refer to specifications for more details. [More...](structbt__cts__time__format.md#details) |
| struct | [bt\_cts\_cb](structbt__cts__cb.md) |
|  | Current Time Service callback structure. [More...](structbt__cts__cb.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_cts\_update\_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7) {     [BT\_CTS\_UPDATE\_REASON\_UNKNOWN](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309) = 0 , [BT\_CTS\_UPDATE\_REASON\_MANUAL](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83) = BIT(0) , [BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a) = BIT(1) , [BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f) = BIT(2) ,     [BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING](#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c) = BIT(3)   } |
|  | CTS time update reason bits as defined in the specification. [More...](#gacc2bf34a4dcd8faf7956b0ff246e4cf7) |

| Functions | |
| --- | --- |
| int | [bt\_cts\_init](#ga26e1e7bb9fcd4d723cdc3458743da5a0) (const struct [bt\_cts\_cb](structbt__cts__cb.md) \*cb) |
|  | This API should be called at application init. |
| int | [bt\_cts\_send\_notification](#ga0a1eac245cf4b9d0dd07cfe45f133513) (enum [bt\_cts\_update\_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7) reason) |
|  | Notify all connected clients that have enabled the current time update notification. |
| int | [bt\_cts\_time\_to\_unix\_ms](#ga07893fdc07e448608cde663f3a54d587) (const struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*unix\_ms) |
|  | Helper API to decode CTS formatted time into milliseconds since epoch. |
| int | [bt\_cts\_time\_from\_unix\_ms](#ga90e1e2859695731b0213fe3dda4c5e52) (struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) unix\_ms) |
|  | Helper API to encode milliseconds since epoch to CTS formatted time. |

## Detailed Description

Current Time Service (CTS).

## Enumeration Type Documentation

## [◆ ](#gacc2bf34a4dcd8faf7956b0ff246e4cf7)bt\_cts\_update\_reason

| enum [bt\_cts\_update\_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7) |
| --- |

`#include <[cts.h](cts_8h.md)>`

CTS time update reason bits as defined in the specification.

| Enumerator | |
| --- | --- |
| BT\_CTS\_UPDATE\_REASON\_UNKNOWN |  |
| BT\_CTS\_UPDATE\_REASON\_MANUAL |  |
| BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF |  |
| BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE |  |
| BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING |  |

## Function Documentation

## [◆ ](#ga26e1e7bb9fcd4d723cdc3458743da5a0)bt\_cts\_init()

| int bt\_cts\_init | ( | const struct [bt\_cts\_cb](structbt__cts__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cts.h](cts_8h.md)>`

This API should be called at application init.

it is safe to call this API before or after bt\_enable API

Parameters
:   | cb | pointer to required callback |
    | --- | --- |

Returns
:   0 on success
:   negative error codes on failure

## [◆ ](#ga0a1eac245cf4b9d0dd07cfe45f133513)bt\_cts\_send\_notification()

| int bt\_cts\_send\_notification | ( | enum [bt\_cts\_update\_reason](#gacc2bf34a4dcd8faf7956b0ff246e4cf7) | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cts.h](cts_8h.md)>`

Notify all connected clients that have enabled the current time update notification.

Parameters
:   | reason | update reason to be sent to the clients |
    | --- | --- |

Returns
:   0 on success
:   negative error codes on failure

## [◆ ](#ga90e1e2859695731b0213fe3dda4c5e52)bt\_cts\_time\_from\_unix\_ms()

| int bt\_cts\_time\_from\_unix\_ms | ( | struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \* | *ct\_time*, |
| --- | --- | --- | --- |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) | *unix\_ms* ) |

`#include <[cts.h](cts_8h.md)>`

Helper API to encode milliseconds since epoch to CTS formatted time.

Note
:   ```
    CONFIG_BT_CTS_HELPER_API
    ```

    needs to be enabled to use this API.

Parameters
:   | ct\_time | [OUT] Pointer to store CTS formatted time |
    | --- | --- |
    | unix\_ms | [IN] milliseconds since epoch to be converted |

Returns
:   0 on success
:   negative error codes on failure

## [◆ ](#ga07893fdc07e448608cde663f3a54d587)bt\_cts\_time\_to\_unix\_ms()

| int bt\_cts\_time\_to\_unix\_ms | ( | const struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \* | *ct\_time*, |
| --- | --- | --- | --- |
|  |  | [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \* | *unix\_ms* ) |

`#include <[cts.h](cts_8h.md)>`

Helper API to decode CTS formatted time into milliseconds since epoch.

Note
:   ```
    CONFIG_BT_CTS_HELPER_API
    ```

    needs to be enabled to use this API.

Parameters
:   | ct\_time | [IN] cts time formatted time |
    | --- | --- |
    | unix\_ms | [OUT] pointer to store parsed millisecond since epoch |

Returns
:   0 on success
:   negative error codes on failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
