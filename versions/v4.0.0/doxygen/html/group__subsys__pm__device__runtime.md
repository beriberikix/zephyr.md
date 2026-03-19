---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__subsys__pm__device__runtime.html
original_path: doxygen/html/group__subsys__pm__device__runtime.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Device Runtime

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

Device Runtime Power Management API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [pm\_device\_runtime\_auto\_enable](#gadc36f344b2cb40c33d5b37eefd120c98) (const struct [device](structdevice.md) \*dev) |
|  | Automatically enable device runtime based on devicetree properties. |
| int | [pm\_device\_runtime\_enable](#gaabcd2cc694c9e201dd87bf42f02b454c) (const struct [device](structdevice.md) \*dev) |
|  | Enable device runtime PM. |
| int | [pm\_device\_runtime\_disable](#gaa7fc78138e282b0eae7da67876baee80) (const struct [device](structdevice.md) \*dev) |
|  | Disable device runtime PM. |
| int | [pm\_device\_runtime\_get](#ga530d4be65757fb2276ab6f631953e045) (const struct [device](structdevice.md) \*dev) |
|  | Resume a device based on usage count. |
| int | [pm\_device\_runtime\_put](#ga98daba53a992fb6bd2c2b31cb445844f) (const struct [device](structdevice.md) \*dev) |
|  | Suspend a device based on usage count. |
| int | [pm\_device\_runtime\_put\_async](#ga9e90089b0ab78f365905418646e196c6) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) delay) |
|  | Suspend a device based on usage count (asynchronously). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_runtime\_is\_enabled](#ga605cd2a3d0ea31efe6bd0b9a6f723219) (const struct [device](structdevice.md) \*dev) |
|  | Check if device runtime is enabled for a given device. |
| int | [pm\_device\_runtime\_usage](#gad643d0c63b7091cdfa68d6e99b6048a0) (const struct [device](structdevice.md) \*dev) |
|  | Return the current device usage counter. |

## Detailed Description

Device Runtime Power Management API.

## Function Documentation

## [◆ ](#gadc36f344b2cb40c33d5b37eefd120c98)pm\_device\_runtime\_auto\_enable()

| int pm\_device\_runtime\_auto\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Automatically enable device runtime based on devicetree properties.

Note
:   Must not be called from application code. See the zephyr,pm-device-runtime-auto property in pm.yaml and z\_sys\_init\_run\_level.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | 0 | If the device runtime PM is enabled successfully or it has not been requested for this device in devicetree. |
    | --- | --- |
    | -errno | Other negative errno, result of enabled device runtime PM. |

## [◆ ](#gaa7fc78138e282b0eae7da67876baee80)pm\_device\_runtime\_disable()

| | int pm\_device\_runtime\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | pre-kernel-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Disable device runtime PM.

If the device is currently suspended it will be resumed.

Function properties (list may not be complete)

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | 0 | If the device runtime PM is disabled successfully. |
    | --- | --- |
    | -ENOTSUP | If the device does not support PM. |
    | -errno | Other negative errno, result of resuming the device. |

## [◆ ](#gaabcd2cc694c9e201dd87bf42f02b454c)pm\_device\_runtime\_enable()

| | int pm\_device\_runtime\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | pre-kernel-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Enable device runtime PM.

This function will enable runtime PM on the given device. If the device is in [PM\_DEVICE\_STATE\_ACTIVE](group__subsys__pm__device.md#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7 "Device is in active or regular state.") state, the device will be suspended.

Function properties (list may not be complete)

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | 0 | If the device runtime PM is enabled successfully. |
    | --- | --- |
    | -EBUSY | If device is busy. |
    | -ENOTSUP | If the device does not support PM. |
    | -errno | Other negative errno, result of suspending the device. |

See also
:   [pm\_device\_init\_suspended()](group__subsys__pm__device.md#ga4c366f49e326a8b8e01d90cb2ee424ba "Initialize a device state to PM_DEVICE_STATE_SUSPENDED.")

## [◆ ](#ga530d4be65757fb2276ab6f631953e045)pm\_device\_runtime\_get()

| | int pm\_device\_runtime\_get | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | pre-kernel-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Resume a device based on usage count.

This function will resume the device if the device is suspended (usage count equal to 0). In case of a resume failure, usage count and device state will be left unchanged. In all other cases, usage count will be incremented.

If the device is still being suspended as a result of calling [pm\_device\_runtime\_put\_async()](#ga9e90089b0ab78f365905418646e196c6), this function will wait for the operation to finish to then resume the device.

Note
:   It is safe to use this function in contexts where blocking is not allowed, e.g. ISR, provided the device PM implementation does not block.

Function properties (list may not be complete)

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | 0 | If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0. |
    | --- | --- |
    | -EWOUDBLOCK | If call would block but it is not allowed (e.g. in ISR). |
    | -errno | Other negative errno, result of the PM action callback. |

## [◆ ](#ga605cd2a3d0ea31efe6bd0b9a6f723219)pm\_device\_runtime\_is\_enabled()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_runtime\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | pre-kernel-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Check if device runtime is enabled for a given device.

Function properties (list may not be complete)

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If device has device runtime PM enabled. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the device has device runtime PM disabled. |

See also
:   [pm\_device\_runtime\_enable()](#gaabcd2cc694c9e201dd87bf42f02b454c)

## [◆ ](#ga98daba53a992fb6bd2c2b31cb445844f)pm\_device\_runtime\_put()

| | int pm\_device\_runtime\_put | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | pre-kernel-ok |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Suspend a device based on usage count.

This function will suspend the device if the device is no longer required (usage count equal to 0). In case of suspend failure, usage count and device state will be left unchanged. In all other cases, usage count will be decremented (down to 0).

Function properties (list may not be complete)

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | 0 | If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0. |
    | --- | --- |
    | -EALREADY | If device is already suspended (can only happen if get/put calls are unbalanced). |
    | -errno | Other negative errno, result of the action callback. |

See also
:   [pm\_device\_runtime\_put\_async()](#ga9e90089b0ab78f365905418646e196c6)

## [◆ ](#ga9e90089b0ab78f365905418646e196c6)pm\_device\_runtime\_put\_async()

| | int pm\_device\_runtime\_put\_async | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [k\_timeout\_t](structk__timeout__t.md) | *delay* ) | | pre-kernel-okasyncisr-ok |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Suspend a device based on usage count (asynchronously).

This function will schedule the device suspension if the device is no longer required (usage count equal to 0). In all other cases, usage count will be decremented (down to 0).

Note
:   Asynchronous operations are not supported when in pre-kernel mode. In this case, the function will be blocking (equivalent to [pm\_device\_runtime\_put()](#ga98daba53a992fb6bd2c2b31cb445844f)).

Function properties (list may not be complete)
:   ,,

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | delay | Minimum amount of time before triggering the action. |

Return values
:   | 0 | If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0. |
    | --- | --- |
    | -EBUSY | If the device is busy. |
    | -EALREADY | If device is already suspended (can only happen if get/put calls are unbalanced). |

See also
:   [pm\_device\_runtime\_put()](#ga98daba53a992fb6bd2c2b31cb445844f)

## [◆ ](#gad643d0c63b7091cdfa68d6e99b6048a0)pm\_device\_runtime\_usage()

| int pm\_device\_runtime\_usage | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device_runtime.h](device__runtime_8h.md)>`

Return the current device usage counter.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Returns
:   the current usage counter.

Return values
:   | -ENOTSUP | If the device is not using runtime PM. |
    | --- | --- |
    | -ENOSYS | If the runtime PM is not enabled at all. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
