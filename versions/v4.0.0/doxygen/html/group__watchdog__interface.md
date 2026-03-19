---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__watchdog__interface.html
original_path: doxygen/html/group__watchdog__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Watchdog Interface

[Device Driver APIs](group__io__interfaces.md)

Watchdog Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [wdt\_window](structwdt__window.md) |
|  | Watchdog timeout window. [More...](structwdt__window.md#details) |
| struct | [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) |
|  | Watchdog timeout configuration. [More...](structwdt__timeout__cfg.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [wdt\_callback\_t](#ga11a942c8e7ee7ceae87c4601dbea8486)) (const struct [device](structdevice.md) \*dev, int channel\_id) |
|  | Watchdog callback. |

| Functions | |
| --- | --- |
| int | [wdt\_setup](#ga822239f3d73585e2d01312657dbbb782) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options) |
|  | Set up watchdog instance. |
| int | [wdt\_disable](#ga32c32cc911e6a0e20cb2dfdd3945be4e) (const struct [device](structdevice.md) \*dev) |
|  | Disable watchdog instance. |
| static int | [wdt\_install\_timeout](#ga5be7aa7f1987be0e69c74b62d1c126a5) (const struct [device](structdevice.md) \*dev, const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg) |
|  | Install a new timeout. |
| int | [wdt\_feed](#ga87265e8988e928eaa380ea29afb6eabe) (const struct [device](structdevice.md) \*dev, int channel\_id) |
|  | Feed specified watchdog timeout. |

| Watchdog options | |
| --- | --- |
|  | |
| #define | [WDT\_OPT\_PAUSE\_IN\_SLEEP](#gafe8472573a7d77a283974cd3843c3c01)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Pause watchdog timer when CPU is in sleep state. |
| #define | [WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG](#ga6d6e1b7cd126a6ca55a955b783962339)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Pause watchdog timer when CPU is halted by the debugger. |

| Watchdog behavior flags | |
| --- | --- |
|  | |
| #define | [WDT\_FLAG\_RESET\_NONE](#ga46a9d878848572cacde89a777977c86b)   (0 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: none. |
| #define | [WDT\_FLAG\_RESET\_CPU\_CORE](#ga24e1f60628198d8e763cf7ec14afed2e)   (1 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: CPU core. |
| #define | [WDT\_FLAG\_RESET\_SOC](#ga71845f454594fac290599f3537d563c9)   (2 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: SoC. |

## Detailed Description

Watchdog Interface.

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga24e1f60628198d8e763cf7ec14afed2e)WDT\_FLAG\_RESET\_CPU\_CORE

| #define WDT\_FLAG\_RESET\_CPU\_CORE   (1 << WDT\_FLAG\_RESET\_SHIFT) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Reset: CPU core.

## [◆ ](#ga46a9d878848572cacde89a777977c86b)WDT\_FLAG\_RESET\_NONE

| #define WDT\_FLAG\_RESET\_NONE   (0 << WDT\_FLAG\_RESET\_SHIFT) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Reset: none.

## [◆ ](#ga71845f454594fac290599f3537d563c9)WDT\_FLAG\_RESET\_SOC

| #define WDT\_FLAG\_RESET\_SOC   (2 << WDT\_FLAG\_RESET\_SHIFT) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Reset: SoC.

## [◆ ](#ga6d6e1b7cd126a6ca55a955b783962339)WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG

| #define WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Pause watchdog timer when CPU is halted by the debugger.

## [◆ ](#gafe8472573a7d77a283974cd3843c3c01)WDT\_OPT\_PAUSE\_IN\_SLEEP

| #define WDT\_OPT\_PAUSE\_IN\_SLEEP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Pause watchdog timer when CPU is in sleep state.

## Typedef Documentation

## [◆ ](#ga11a942c8e7ee7ceae87c4601dbea8486)wdt\_callback\_t

| typedef void(\* wdt\_callback\_t) (const struct [device](structdevice.md) \*dev, int channel\_id) |
| --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Watchdog callback.

Parameters
:   | dev | Watchdog device instance. |
    | --- | --- |
    | channel\_id | Channel identifier. |

## Function Documentation

## [◆ ](#ga32c32cc911e6a0e20cb2dfdd3945be4e)wdt\_disable()

| int wdt\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Disable watchdog instance.

This function disables the watchdog instance and automatically uninstalls all timeouts. To set up a new watchdog, install timeouts and call [wdt\_setup()](#ga822239f3d73585e2d01312657dbbb782) again. Not all watchdogs can be restarted after they are disabled.

Parameters
:   | dev | Watchdog device instance. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EFAULT | If watchdog instance is not enabled. |
    | -EPERM | If watchdog can not be disabled directly by application code. |
    | -errno | In case of any other failure. |

## [◆ ](#ga87265e8988e928eaa380ea29afb6eabe)wdt\_feed()

| int wdt\_feed | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *channel\_id* ) |

`#include <[watchdog.h](watchdog_8h.md)>`

Feed specified watchdog timeout.

Parameters
:   | dev | Watchdog device instance. |
    | --- | --- |
    | channel\_id | Channel index. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EAGAIN | If completing the feed operation would stall the caller, for example due to an in-progress watchdog operation such as a previous [wdt\_feed()](#ga87265e8988e928eaa380ea29afb6eabe) call. |
    | -EINVAL | If there is no installed timeout for supplied channel. |
    | -errno | In case of any other failure. |

## [◆ ](#ga5be7aa7f1987be0e69c74b62d1c126a5)wdt\_install\_timeout()

| | int wdt\_install\_timeout | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \* | *cfg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[watchdog.h](watchdog_8h.md)>`

Install a new timeout.

Note
:   This function must be used before [wdt\_setup()](#ga822239f3d73585e2d01312657dbbb782). Changes applied here have no effects until [wdt\_setup()](#ga822239f3d73585e2d01312657dbbb782) is called.

Parameters
:   |  | dev | Watchdog device instance. |
    | --- | --- | --- |
    | [in] | cfg | Timeout configuration. |

Return values
:   | channel\_id | If successful, a non-negative value indicating the index of the channel to which the timeout was assigned. This value is supposed to be used as the parameter in calls to [wdt\_feed()](#ga87265e8988e928eaa380ea29afb6eabe). |
    | --- | --- |
    | -EBUSY | If timeout can not be installed while watchdog has already been setup. |
    | -ENOMEM | If no more timeouts can be installed. |
    | -ENOTSUP | If any of the set flags is not supported. |
    | -EINVAL | If any of the window timeout value is out of possible range. This value is also returned if watchdog supports only one timeout value for all timeouts and the supplied timeout window differs from windows for alarms installed so far. |
    | -errno | In case of any other failure. |

## [◆ ](#ga822239f3d73585e2d01312657dbbb782)wdt\_setup()

| int wdt\_setup | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *options* ) |

`#include <[watchdog.h](watchdog_8h.md)>`

Set up watchdog instance.

This function is used for configuring global watchdog settings that affect all timeouts. It should be called after installing timeouts. After successful return, all installed timeouts are valid and must be serviced periodically by calling [wdt\_feed()](#ga87265e8988e928eaa380ea29afb6eabe).

Parameters
:   | dev | Watchdog device instance. |
    | --- | --- |
    | options | Configuration options (see [WDT\_OPT](#WDT_OPT)). |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If any of the set options is not supported. |
    | -EBUSY | If watchdog instance has been already setup. |
    | -errno | In case of any other failure. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
