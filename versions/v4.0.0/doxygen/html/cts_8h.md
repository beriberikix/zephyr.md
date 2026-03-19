---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cts_8h.html
original_path: doxygen/html/cts_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cts.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/posix/time.h](include_2zephyr_2posix_2time_8h_source.md)>`

[Go to the source code of this file.](cts_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_cts\_time\_format](structbt__cts__time__format.md) |
|  | Current Time service data format, Please refer to specifications for more details. [More...](structbt__cts__time__format.md#details) |
| struct | [bt\_cts\_cb](structbt__cts__cb.md) |
|  | Current Time Service callback structure. [More...](structbt__cts__cb.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_cts\_update\_reason](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7) {     [BT\_CTS\_UPDATE\_REASON\_UNKNOWN](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7ab196da4c0761eacbc80db5cd59482309) = 0 , [BT\_CTS\_UPDATE\_REASON\_MANUAL](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7af8282fe3f18a5555c1ffa767384a9f83) = BIT(0) , [BT\_CTS\_UPDATE\_REASON\_EXTERNAL\_REF](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a56967059590b25812f7ae098bb21653a) = BIT(1) , [BT\_CTS\_UPDATE\_REASON\_TIME\_ZONE\_CHANGE](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a2e842670bcdf69184948d33fc3418d9f) = BIT(2) ,     [BT\_CTS\_UPDATE\_REASON\_DAYLIGHT\_SAVING](group__bt__cts.md#ggacc2bf34a4dcd8faf7956b0ff246e4cf7a82443c4229393642ac9f9aae165f0b0c) = BIT(3)   } |
|  | CTS time update reason bits as defined in the specification. [More...](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7) |

| Functions | |
| --- | --- |
| int | [bt\_cts\_init](group__bt__cts.md#ga26e1e7bb9fcd4d723cdc3458743da5a0) (const struct [bt\_cts\_cb](structbt__cts__cb.md) \*cb) |
|  | This API should be called at application init. |
| int | [bt\_cts\_send\_notification](group__bt__cts.md#ga0a1eac245cf4b9d0dd07cfe45f133513) (enum [bt\_cts\_update\_reason](group__bt__cts.md#gacc2bf34a4dcd8faf7956b0ff246e4cf7) reason) |
|  | Notify all connected clients that have enabled the current time update notification. |
| int | [bt\_cts\_time\_to\_unix\_ms](group__bt__cts.md#ga07893fdc07e448608cde663f3a54d587) (const struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) \*unix\_ms) |
|  | Helper API to decode CTS formatted time into milliseconds since epoch. |
| int | [bt\_cts\_time\_from\_unix\_ms](group__bt__cts.md#ga90e1e2859695731b0213fe3dda4c5e52) (struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*ct\_time, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) unix\_ms) |
|  | Helper API to encode milliseconds since epoch to CTS formatted time. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [cts.h](cts_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
