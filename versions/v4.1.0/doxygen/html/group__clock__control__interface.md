---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__clock__control__interface.html
original_path: doxygen/html/group__clock__control__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Clock Control Interface

[Device Driver APIs](group__io__interfaces.md)

Clock Control Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [LiteX Clock Control driver interface](group__clock__control__litex__interface.md) |
|  | LiteX Clock Control driver interface. |

| Data Structures | |
| --- | --- |
| struct | [clock\_control\_driver\_api](structclock__control__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [CLOCK\_CONTROL\_SUBSYS\_ALL](#ga9aa9a4e00c1e7985a1fea6bed235003e)   [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |

| Typedefs | |
| --- | --- |
| typedef void \* | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) |
|  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) is a type to identify a clock controller sub-system. |
| typedef void \* | [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) |
|  | [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) is a type to identify a clock controller sub-system rate. |
| typedef void(\* | [clock\_control\_cb\_t](#ga17257fb3864dc5a33082c3422ad7c275)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) subsys, void \*user\_data) |
|  | Callback called on clock started. |
| typedef int(\* | [clock\_control](#ga459b95cb726892b95537d15273413099)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
| typedef int(\* | [clock\_control\_get](#ga41087b8914b4bec0c1a61217122cc2a0)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
| typedef int(\* | [clock\_control\_async\_on\_fn](#ga0cd408e023fda272784c24d0c644014d)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_cb\_t](#ga17257fb3864dc5a33082c3422ad7c275) cb, void \*user\_data) |
| typedef enum [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09)(\* | [clock\_control\_get\_status\_fn](#ga0af123fbaa3572a9722f17c331936e9a)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
| typedef int(\* | [clock\_control\_set](#ga8ea31ee8a6e3aa69de0098efba63ae2b)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) rate) |
| typedef int(\* | [clock\_control\_configure\_fn](#ga1f7e0aa491a5cccbe49015ed1f5cfef0)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, void \*data) |

| Enumerations | |
| --- | --- |
| enum | [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09) { [CLOCK\_CONTROL\_STATUS\_STARTING](#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52) , [CLOCK\_CONTROL\_STATUS\_OFF](#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa) , [CLOCK\_CONTROL\_STATUS\_ON](#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db) , [CLOCK\_CONTROL\_STATUS\_UNKNOWN](#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc) } |
|  | Current clock status. [More...](#gad12829335f0c954ab6d586549db45e09) |

| Functions | |
| --- | --- |
| static int | [clock\_control\_on](#gaec69b0989cefad79ffd5c92f060150b9) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Enable a clock controlled by the device. |
| static int | [clock\_control\_off](#gadbebc1c12937be561b761ef4a3b7d8a5) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Disable a clock controlled by the device. |
| static int | [clock\_control\_async\_on](#ga03cedb9723e001d01c495f0abb6acfdf) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_cb\_t](#ga17257fb3864dc5a33082c3422ad7c275) cb, void \*user\_data) |
|  | Request clock to start with notification when clock has been started. |
| static enum [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09) | [clock\_control\_get\_status](#ga35be64d09222f44aa00cd1371a39613e) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Get clock status. |
| static int | [clock\_control\_get\_rate](#ga00f6af6d2668c2dfff0640fe176e89ff) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Obtain the clock rate of given sub-system. |
| static int | [clock\_control\_set\_rate](#ga3bd25314e8bfcc62f0728d89321bb614) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) rate) |
|  | Set the rate of the clock controlled by the device. |
| static int | [clock\_control\_configure](#gaf5e4b13798955fcc891c080b9967ab06) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, void \*data) |
|  | Configure a source clock. |

## Detailed Description

Clock Control Interface.

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga9aa9a4e00c1e7985a1fea6bed235003e)CLOCK\_CONTROL\_SUBSYS\_ALL

| #define CLOCK\_CONTROL\_SUBSYS\_ALL   [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## Typedef Documentation

## [◆ ](#ga459b95cb726892b95537d15273413099)clock\_control

| typedef int(\* clock\_control) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga0cd408e023fda272784c24d0c644014d)clock\_control\_async\_on\_fn

| typedef int(\* clock\_control\_async\_on\_fn) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_cb\_t](#ga17257fb3864dc5a33082c3422ad7c275) cb, void \*user\_data) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga17257fb3864dc5a33082c3422ad7c275)clock\_control\_cb\_t

| typedef void(\* clock\_control\_cb\_t) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) subsys, void \*user\_data) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Callback called on clock started.

Parameters
:   | dev | Device structure whose driver controls the clock. |
    | --- | --- |
    | subsys | Opaque data representing the clock. |
    | user\_data | User data. |

## [◆ ](#ga1f7e0aa491a5cccbe49015ed1f5cfef0)clock\_control\_configure\_fn

| typedef int(\* clock\_control\_configure\_fn) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, void \*data) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga41087b8914b4bec0c1a61217122cc2a0)clock\_control\_get

| typedef int(\* clock\_control\_get) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga0af123fbaa3572a9722f17c331936e9a)clock\_control\_get\_status\_fn

| typedef enum [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09)(\* clock\_control\_get\_status\_fn) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga8ea31ee8a6e3aa69de0098efba63ae2b)clock\_control\_set

| typedef int(\* clock\_control\_set) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) rate) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

## [◆ ](#ga05d8b476ef0331e1502702921d2801f1)clock\_control\_subsys\_rate\_t

| typedef void\* [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

[clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) is a type to identify a clock controller sub-system rate.

Such data pointed is opaque and relevant only to set the clock controller rate of the driver instance being used.

## [◆ ](#gaa7d3935eaaf18902801a7d94859483db)clock\_control\_subsys\_t

| typedef void\* [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

[clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) is a type to identify a clock controller sub-system.

Such data pointed is opaque and relevant only to the clock controller driver instance being used.

## Enumeration Type Documentation

## [◆ ](#gad12829335f0c954ab6d586549db45e09)clock\_control\_status

| enum [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09) |
| --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Current clock status.

| Enumerator | |
| --- | --- |
| CLOCK\_CONTROL\_STATUS\_STARTING |  |
| CLOCK\_CONTROL\_STATUS\_OFF |  |
| CLOCK\_CONTROL\_STATUS\_ON |  |
| CLOCK\_CONTROL\_STATUS\_UNKNOWN |  |

## Function Documentation

## [◆ ](#ga03cedb9723e001d01c495f0abb6acfdf)clock\_control\_async\_on()

| | int clock\_control\_async\_on | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys*, | |  |  | [clock\_control\_cb\_t](#ga17257fb3864dc5a33082c3422ad7c275) | *cb*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Request clock to start with notification when clock has been started.

Function is non-blocking and can be called from any context. User callback is called when clock is started.

Parameters
:   | dev | Device. |
    | --- | --- |
    | sys | A pointer to an opaque data representing the sub-system. |
    | cb | Callback. |
    | user\_data | User context passed to the callback. |

Return values
:   | 0 | if start is successfully initiated. |
    | --- | --- |
    | -EALREADY | if clock was already started and is starting or running. |
    | -ENOTSUP | If the requested mode of operation is not supported. |
    | -ENOSYS | if the interface is not implemented. |
    | other | negative errno on vendor specific error. |

## [◆ ](#gaf5e4b13798955fcc891c080b9967ab06)clock\_control\_configure()

| | int clock\_control\_configure | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys*, | |  |  | void \* | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Configure a source clock.

This function is non-blocking and can be called from any context. On success, the selected clock is configured as per caller's request.

It is caller's responsibility to ensure that subsequent calls to the API provide the right information to allows [clock\_control](#ga459b95cb726892b95537d15273413099) driver to perform the right action (such as using the right clock source on clock\_control\_get\_rate call).

`data` is implementation specific and could be used to convey supplementary information required for expected clock configuration.

Parameters
:   | dev | Device structure whose driver controls the clock |
    | --- | --- |
    | sys | Opaque data representing the clock |
    | data | Opaque data providing additional input for clock configuration |

Return values
:   | 0 | On success |
    | --- | --- |
    | -ENOSYS | If the device driver does not implement this call |
    | -errno | Other negative errno on failure. |

## [◆ ](#ga00f6af6d2668c2dfff0640fe176e89ff)clock\_control\_get\_rate()

| | int clock\_control\_get\_rate | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *rate* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Obtain the clock rate of given sub-system.

Parameters
:   |  | dev | Pointer to the device structure for the clock controller driver instance |
    | --- | --- | --- |
    |  | sys | A pointer to an opaque data representing the sub-system |
    | [out] | rate | Subsystem clock rate |

Return values
:   | 0 | on successful rate reading. |
    | --- | --- |
    | -EAGAIN | if rate cannot be read. Some drivers do not support returning the rate when the clock is off. |
    | -ENOTSUP | if reading the clock rate is not supported for the given sub-system. |
    | -ENOSYS | if the interface is not implemented. |

## [◆ ](#ga35be64d09222f44aa00cd1371a39613e)clock\_control\_get\_status()

| | enum [clock\_control\_status](#gad12829335f0c954ab6d586549db45e09) clock\_control\_get\_status | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Get clock status.

Parameters
:   | dev | Device. |
    | --- | --- |
    | sys | A pointer to an opaque data representing the sub-system. |

Returns
:   Status.

## [◆ ](#gadbebc1c12937be561b761ef4a3b7d8a5)clock\_control\_off()

| | int clock\_control\_off | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Disable a clock controlled by the device.

This function is non-blocking and can be called from any context. On success, the clock is disabled when this function returns.

Parameters
:   | dev | Device structure whose driver controls the clock |
    | --- | --- |
    | sys | Opaque data representing the clock |

Returns
:   0 on success, negative errno on failure.

## [◆ ](#gaec69b0989cefad79ffd5c92f060150b9)clock\_control\_on()

| | int clock\_control\_on | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Enable a clock controlled by the device.

On success, the clock is enabled and ready when this function returns. This function may sleep, and thus can only be called from thread context.

Use [clock\_control\_async\_on()](#ga03cedb9723e001d01c495f0abb6acfdf) for non-blocking operation.

Parameters
:   | dev | Device structure whose driver controls the clock. |
    | --- | --- |
    | sys | Opaque data representing the clock. |

Returns
:   0 on success, negative errno on failure.

## [◆ ](#ga3bd25314e8bfcc62f0728d89321bb614)clock\_control\_set\_rate()

| | int clock\_control\_set\_rate | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [clock\_control\_subsys\_t](#gaa7d3935eaaf18902801a7d94859483db) | *sys*, | |  |  | [clock\_control\_subsys\_rate\_t](#ga05d8b476ef0331e1502702921d2801f1) | *rate* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[clock_control.h](clock__control_8h.md)>`

Set the rate of the clock controlled by the device.

On success, the new clock rate is set and ready when this function returns. This function may sleep, and thus can only be called from thread context.

Parameters
:   | dev | Device structure whose driver controls the clock. |
    | --- | --- |
    | sys | Opaque data representing the clock. |
    | rate | Opaque data representing the clock rate to be used. |

Return values
:   | -EALREADY | if clock was already in the given rate. |
    | --- | --- |
    | -ENOTSUP | If the requested mode of operation is not supported. |
    | -ENOSYS | if the interface is not implemented. |
    | other | negative errno on vendor specific error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
