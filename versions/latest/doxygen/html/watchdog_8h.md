---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/watchdog_8h.html
original_path: doxygen/html/watchdog_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

watchdog.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/watchdog.h>`

[Go to the source code of this file.](watchdog_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [wdt\_window](structwdt__window.md) |
|  | Watchdog timeout window. [More...](structwdt__window.md#details) |
| struct | [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) |
|  | Watchdog timeout configuration. [More...](structwdt__timeout__cfg.md#details) |

| Macros | |
| --- | --- |
| Watchdog options | |
|  | |
| #define | [WDT\_OPT\_PAUSE\_IN\_SLEEP](group__watchdog__interface.md#gafe8472573a7d77a283974cd3843c3c01)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Pause watchdog timer when CPU is in sleep state. |
| #define | [WDT\_OPT\_PAUSE\_HALTED\_BY\_DBG](group__watchdog__interface.md#ga6d6e1b7cd126a6ca55a955b783962339)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Pause watchdog timer when CPU is halted by the debugger. |
| Watchdog behavior flags | |
|  | |
| #define | [WDT\_FLAG\_RESET\_NONE](group__watchdog__interface.md#ga46a9d878848572cacde89a777977c86b)   (0 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: none. |
| #define | [WDT\_FLAG\_RESET\_CPU\_CORE](group__watchdog__interface.md#ga24e1f60628198d8e763cf7ec14afed2e)   (1 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: CPU core. |
| #define | [WDT\_FLAG\_RESET\_SOC](group__watchdog__interface.md#ga71845f454594fac290599f3537d563c9)   (2 << WDT\_FLAG\_RESET\_SHIFT) |
|  | Reset: SoC. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486)) (const struct [device](structdevice.md) \*dev, int channel\_id) |
|  | Watchdog callback. |

| Functions | |
| --- | --- |
| int | [wdt\_setup](group__watchdog__interface.md#ga822239f3d73585e2d01312657dbbb782) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) options) |
|  | Set up watchdog instance. |
| int | [wdt\_disable](group__watchdog__interface.md#ga32c32cc911e6a0e20cb2dfdd3945be4e) (const struct [device](structdevice.md) \*dev) |
|  | Disable watchdog instance. |
| static int | [wdt\_install\_timeout](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5) (const struct [device](structdevice.md) \*dev, const struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \*cfg) |
|  | Install a new timeout. |
| int | [wdt\_feed](group__watchdog__interface.md#ga87265e8988e928eaa380ea29afb6eabe) (const struct [device](structdevice.md) \*dev, int channel\_id) |
|  | Feed specified watchdog timeout. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [watchdog.h](watchdog_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
