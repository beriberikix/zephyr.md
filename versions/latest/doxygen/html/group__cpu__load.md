---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__cpu__load.html
original_path: doxygen/html/group__cpu__load.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CPU load monitor

[Operating System Services](group__os__services.md) » [Debug](group__debug.md)

Module for monitoring CPU Load.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [cpu\_load\_cb\_t](#ga83f2e3099de11b8e6b66395ae69f394a)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) percent) |

| Functions | |
| --- | --- |
| void | [cpu\_load\_on\_enter\_idle](#ga28a73232eb45cdf6ce057e1e4c84190d) (void) |
|  | Hook called by the application specific hook on entering CPU idle. |
| void | [cpu\_load\_on\_exit\_idle](#ga8a8c97914a72b6eb5a7e1862710a0c6d) (void) |
|  | Hook called by the application specific hook on exiting CPU idle. |
| int | [cpu\_load\_get](#gaf44501a292aeef7749b68c706b34119f) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reset) |
|  | Get CPU load. |
| void | [cpu\_load\_log\_control](#gabc95920fb1a666b1496618cf5afbfbff) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Control periodic CPU statistics report. |
| int | [cpu\_load\_cb\_reg](#gaec80c70d8dd6ea130edde48618ed2463) ([cpu\_load\_cb\_t](#ga83f2e3099de11b8e6b66395ae69f394a) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) threshold\_percent) |
|  | Optional registration of callback when load is greater or equal to the threshold. |

## Detailed Description

Module for monitoring CPU Load.

This module allow monitoring of the CPU load.

## Typedef Documentation

## [◆ ](#ga83f2e3099de11b8e6b66395ae69f394a)cpu\_load\_cb\_t

| typedef void(\* cpu\_load\_cb\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) percent) |
| --- |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

## Function Documentation

## [◆ ](#gaec80c70d8dd6ea130edde48618ed2463)cpu\_load\_cb\_reg()

| int cpu\_load\_cb\_reg | ( | [cpu\_load\_cb\_t](#ga83f2e3099de11b8e6b66395ae69f394a) | *cb*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *threshold\_percent* ) |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

Optional registration of callback when load is greater or equal to the threshold.

Parameters
:   | cb | Pointer to the callback function. NULL will cancel the callback. |
    | --- | --- |
    | threshold\_percent | Threshold [0...100]. CPU load equal or greater that this will trigger the callback. |

Return values
:   | 0 | - Callback registered/cancelled. |
    | --- | --- |
    | -EINVAL | if the threshold is invalid. |

## [◆ ](#gaf44501a292aeef7749b68c706b34119f)cpu\_load\_get()

| int cpu\_load\_get | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reset* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

Get CPU load.

CPU load is measured using a timer which tracks amount of time spent in the CPU idle. Since it is a software tracking there is some small overhead. Precision depends on the frequency of the timer in relation to the CPU frequency.

Parameters
:   | reset | Reset the measurement after reading. |
    | --- | --- |

Return values
:   | Positive | number - CPU load in per mille. |
    | --- | --- |
    | Negative | number - error code. |

## [◆ ](#gabc95920fb1a666b1496618cf5afbfbff)cpu\_load\_log\_control()

| void cpu\_load\_log\_control | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

Control periodic CPU statistics report.

Report logging is by default enabled.

Parameters
:   | enable | true to enable report logging and false to disable. |
    | --- | --- |

## [◆ ](#ga28a73232eb45cdf6ce057e1e4c84190d)cpu\_load\_on\_enter\_idle()

| void cpu\_load\_on\_enter\_idle | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

Hook called by the application specific hook on entering CPU idle.

## [◆ ](#ga8a8c97914a72b6eb5a7e1862710a0c6d)cpu\_load\_on\_exit\_idle()

| void cpu\_load\_on\_exit\_idle | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/debug/cpu_load.h](cpu__load_8h.md)>`

Hook called by the application specific hook on exiting CPU idle.

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
