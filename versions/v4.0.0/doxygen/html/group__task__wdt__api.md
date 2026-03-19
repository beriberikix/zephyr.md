---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__task__wdt__api.html
original_path: doxygen/html/group__task__wdt__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Task Watchdog APIs

[Operating System Services](group__os__services.md)

Task Watchdog APIs.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef void(\* | [task\_wdt\_callback\_t](#gab9b9e2dd0eb52e324806cc5090507c45)) (int channel\_id, void \*user\_data) |
|  | Task watchdog callback. |

| Functions | |
| --- | --- |
| int | [task\_wdt\_init](#gafa31c31c13478669615ebf0bbdd28a0c) (const struct [device](structdevice.md) \*hw\_wdt) |
|  | Initialize task watchdog. |
| int | [task\_wdt\_add](#ga26484bd148a9e2910d9989a1d9598230) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reload\_period, [task\_wdt\_callback\_t](#gab9b9e2dd0eb52e324806cc5090507c45) callback, void \*user\_data) |
|  | Install new timeout. |
| int | [task\_wdt\_delete](#ga631c1243b5a00a304687cc54e2632c0d) (int channel\_id) |
|  | Delete task watchdog channel. |
| int | [task\_wdt\_feed](#ga00fc594cace06d6308efa1ded45a22fc) (int channel\_id) |
|  | Feed specified watchdog channel. |

## Detailed Description

Task Watchdog APIs.

Since
:   2.5

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#gab9b9e2dd0eb52e324806cc5090507c45)task\_wdt\_callback\_t

| typedef void(\* task\_wdt\_callback\_t) (int channel\_id, void \*user\_data) |
| --- |

`#include <[task_wdt.h](task__wdt_8h.md)>`

Task watchdog callback.

## Function Documentation

## [◆ ](#ga26484bd148a9e2910d9989a1d9598230)task\_wdt\_add()

| int task\_wdt\_add | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reload\_period*, |
| --- | --- | --- | --- |
|  |  | [task\_wdt\_callback\_t](#gab9b9e2dd0eb52e324806cc5090507c45) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[task_wdt.h](task__wdt_8h.md)>`

Install new timeout.

Adds a new timeout to the list of task watchdog channels.

Parameters
:   | reload\_period | Period in milliseconds used to reset the timeout |
    | --- | --- |
    | callback | Function to be called when watchdog timer expired. Pass NULL to use system reset handler. |
    | user\_data | User data to associate with the watchdog channel. |

Return values
:   | channel\_id | If successful, a non-negative value indicating the index of the channel to which the timeout was assigned. This ID is supposed to be used as the parameter in calls to [task\_wdt\_feed()](#ga00fc594cace06d6308efa1ded45a22fc). |
    | --- | --- |
    | -EINVAL | If the reload\_period is invalid. |
    | -ENOMEM | If no more timeouts can be installed. |

## [◆ ](#ga631c1243b5a00a304687cc54e2632c0d)task\_wdt\_delete()

| int task\_wdt\_delete | ( | int | *channel\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[task_wdt.h](task__wdt_8h.md)>`

Delete task watchdog channel.

Deletes the specified channel from the list of task watchdog channels. The channel is now available again for other tasks via [task\_wdt\_add()](#ga26484bd148a9e2910d9989a1d9598230) function.

Parameters
:   | channel\_id | Index of the channel as returned by [task\_wdt\_add()](#ga26484bd148a9e2910d9989a1d9598230). |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If there is no installed timeout for supplied channel. |

## [◆ ](#ga00fc594cace06d6308efa1ded45a22fc)task\_wdt\_feed()

| int task\_wdt\_feed | ( | int | *channel\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[task_wdt.h](task__wdt_8h.md)>`

Feed specified watchdog channel.

This function loops through all installed task watchdogs and updates the internal kernel timer used as for the software watchdog with the next due timeout.

Parameters
:   | channel\_id | Index of the fed channel as returned by [task\_wdt\_add()](#ga26484bd148a9e2910d9989a1d9598230). |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | If there is no installed timeout for supplied channel. |

## [◆ ](#gafa31c31c13478669615ebf0bbdd28a0c)task\_wdt\_init()

| int task\_wdt\_init | ( | const struct [device](structdevice.md) \* | *hw\_wdt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[task_wdt.h](task__wdt_8h.md)>`

Initialize task watchdog.

This function sets up necessary kernel timers and the hardware watchdog (if desired as fallback). It has to be called before [task\_wdt\_add()](#ga26484bd148a9e2910d9989a1d9598230) and [task\_wdt\_feed()](#ga00fc594cace06d6308efa1ded45a22fc).

Parameters
:   | hw\_wdt | Pointer to the hardware watchdog device used as fallback. Pass NULL if no hardware watchdog fallback is desired. |
    | --- | --- |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If assigning a hardware watchdog is not supported. |
    | -Errno | Negative errno if the fallback hw\_wdt is used and the install timeout API fails. See [wdt\_install\_timeout()](group__watchdog__interface.md#ga5be7aa7f1987be0e69c74b62d1c126a5 "Install a new timeout.") API for possible return values. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
