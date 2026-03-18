---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/task__wdt_8h.html
original_path: doxygen/html/task__wdt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

task\_wdt.h File Reference

Task watchdog header file.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](task__wdt_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [task\_wdt\_callback\_t](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45)) (int channel\_id, void \*user\_data) |
|  | Task watchdog callback. |

| Functions | |
| --- | --- |
| int | [task\_wdt\_init](group__task__wdt__api.md#gafa31c31c13478669615ebf0bbdd28a0c) (const struct [device](structdevice.md) \*hw\_wdt) |
|  | Initialize task watchdog. |
| int | [task\_wdt\_add](group__task__wdt__api.md#ga26484bd148a9e2910d9989a1d9598230) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reload\_period, [task\_wdt\_callback\_t](group__task__wdt__api.md#gab9b9e2dd0eb52e324806cc5090507c45) callback, void \*user\_data) |
|  | Install new timeout. |
| int | [task\_wdt\_delete](group__task__wdt__api.md#ga631c1243b5a00a304687cc54e2632c0d) (int channel\_id) |
|  | Delete task watchdog channel. |
| int | [task\_wdt\_feed](group__task__wdt__api.md#ga00fc594cace06d6308efa1ded45a22fc) (int channel\_id) |
|  | Feed specified watchdog channel. |

## Detailed Description

Task watchdog header file.

This header file declares prototypes for the task watchdog APIs.

The task watchdog can be used to monitor correct operation of individual threads. It can be used together with a hardware watchdog as a fallback.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [task\_wdt](dir_590994245f36812650ae1f422575e718.md)
- [task\_wdt.h](task__wdt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
