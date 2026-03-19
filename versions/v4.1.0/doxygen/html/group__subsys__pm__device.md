---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__subsys__pm__device.html
original_path: doxygen/html/group__subsys__pm__device.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Device

[Operating System Services](group__os__services.md) » [Power Management (PM)](group__subsys__pm.md)

Device Power Management API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pm\_device\_base](structpm__device__base.md) |
|  | Device PM info. [More...](structpm__device__base.md#details) |
| struct | [pm\_device](structpm__device.md) |
|  | Runtime PM info for device with generic PM. [More...](structpm__device.md#details) |
| struct | [pm\_device\_isr](structpm__device__isr.md) |
|  | Runtime PM info for device with synchronous PM. [More...](structpm__device__isr.md#details) |

| Macros | |
| --- | --- |
| #define | [PM\_DEVICE\_ISR\_SAFE](#ga18bb96fc4d5003516ab2eaf73cb35912)   1 |
|  | Flag indicating that runtime PM API for the device can be called from any context. |
| #define | [PM\_DEVICE\_DEFINE](#gae85fb5a7c31863a3663cef8dd7229c6c)(dev\_id, pm\_action\_cb, ...) |
|  | Define device PM resources for the given device name. |
| #define | [PM\_DEVICE\_DT\_DEFINE](#gaa2bd2c490fee99a6fc2b23605e799ef0)(node\_id, pm\_action\_cb, ...) |
|  | Define device PM resources for the given node identifier. |
| #define | [PM\_DEVICE\_DT\_INST\_DEFINE](#ga5b201836d9c19a1c87cdde93631a4b0c)(idx, pm\_action\_cb, ...) |
|  | Define device PM resources for the given instance. |
| #define | [PM\_DEVICE\_GET](#gaa94d19d0590659b7aba83566de9bd0c5)(dev\_id) |
|  | Obtain a reference to the device PM resources for the given device. |
| #define | [PM\_DEVICE\_DT\_GET](#gad244d742bc6b9874bfb90a2c3c87c4e8)(node\_id) |
|  | Obtain a reference to the device PM resources for the given node. |
| #define | [PM\_DEVICE\_DT\_INST\_GET](#ga52892f2c34f6ccc9598002625baf12ce)(idx) |
|  | Obtain a reference to the device PM resources for the given instance. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [pm\_device\_action\_cb\_t](#ga81d4ee32f5bbb1b343234b9b3afc0179)) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) action) |
|  | Device PM action callback. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pm\_device\_action\_failed\_cb\_t](#ga9cfb6437873089714635d2b26aafefac)) (const struct [device](structdevice.md) \*dev, int err) |
|  | Device PM action failed callback. |

| Enumerations | |
| --- | --- |
| enum | [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) { [PM\_DEVICE\_STATE\_ACTIVE](#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7) , [PM\_DEVICE\_STATE\_SUSPENDED](#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) , [PM\_DEVICE\_STATE\_SUSPENDING](#gga561c0789071e3c3963f21f4c4a1bb2c6a51a5904aff980deff73d29568b6f7deb) , [PM\_DEVICE\_STATE\_OFF](#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2) } |
|  | Device power states. [More...](#ga561c0789071e3c3963f21f4c4a1bb2c6) |
| enum | [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) { [PM\_DEVICE\_ACTION\_SUSPEND](#ggaee5546eacb9be7caa9d59ab63926cc4ca5b7ae11deaee85eb0b8452bc89383790) , [PM\_DEVICE\_ACTION\_RESUME](#ggaee5546eacb9be7caa9d59ab63926cc4ca757c6ab81eeac0d6afae479d6a0ac564) , [PM\_DEVICE\_ACTION\_TURN\_OFF](#ggaee5546eacb9be7caa9d59ab63926cc4ca2bcd7dee3a85b27157bbc465bacf521e) , [PM\_DEVICE\_ACTION\_TURN\_ON](#ggaee5546eacb9be7caa9d59ab63926cc4cac7690e0ffd27742acf58fdbdb7b89544) } |
|  | Device PM actions. [More...](#gaee5546eacb9be7caa9d59ab63926cc4c) |

| Functions | |
| --- | --- |
| const char \* | [pm\_device\_state\_str](#gad109511e4314fa6145ee97dd655ec7bb) (enum [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get name of device PM state. |
| int | [pm\_device\_action\_run](#ga3840d6e7832a00b93763247a5951bfde) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) action) |
|  | Run a pm action on a device. |
| void | [pm\_device\_children\_action\_run](#ga765a5412f66070ccefd8e80ed9f62b1b) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) action, [pm\_device\_action\_failed\_cb\_t](#ga9cfb6437873089714635d2b26aafefac) failure\_cb) |
|  | Run a pm action on all children of a device. |
| int | [pm\_device\_state\_get](#gaffcf0aea5df10657235d4ed1f8c74d5a) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Obtain the power state of a device. |
| static void | [pm\_device\_init\_suspended](#ga4c366f49e326a8b8e01d90cb2ee424ba) (const struct [device](structdevice.md) \*dev) |
|  | Initialize a device state to [PM\_DEVICE\_STATE\_SUSPENDED](#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5). |
| static void | [pm\_device\_init\_off](#gafb12ecf4679dd449e2faad0ede2c75fd) (const struct [device](structdevice.md) \*dev) |
|  | Initialize a device state to [PM\_DEVICE\_STATE\_OFF](#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2). |
| void | [pm\_device\_busy\_set](#ga7ea002352f3d1c90aecff1d54c255a06) (const struct [device](structdevice.md) \*dev) |
|  | Mark a device as busy. |
| void | [pm\_device\_busy\_clear](#ga8b527314f0c61b85602876b4f5a52275) (const struct [device](structdevice.md) \*dev) |
|  | Clear a device busy status. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_any\_busy](#gae59a1fbcd2399717076fbfcee1e5e411) (void) |
|  | Check if any device is busy. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_busy](#ga8ff7c3197d5ded860878302d00ac709c) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is busy. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_enable](#ga74fde62f71393fb9863916b3a2e5c460) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable or disable a device as a wake up source. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_is\_enabled](#ga0716c6158804ac48022280d8d237f8c1) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is enabled as a wake up source. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_wakeup\_is\_capable](#gac818aafb748b57d70909808b45d89379) (const struct [device](structdevice.md) \*dev) |
|  | Check if a device is wake up capable. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_on\_power\_domain](#ga32eb5e210d2f0ba533b0185a94c8744e) (const struct [device](structdevice.md) \*dev) |
|  | Check if the device is on a switchable power domain. |
| int | [pm\_device\_power\_domain\_add](#gaa10a3f1ce71409cb591db416a1611377) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*domain) |
|  | Add a device to a power domain. |
| int | [pm\_device\_power\_domain\_remove](#ga1d7ab9b0b497e016b9b22d2506cd23f9) (const struct [device](structdevice.md) \*dev, const struct [device](structdevice.md) \*domain) |
|  | Remove a device from a power domain. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pm\_device\_is\_powered](#ga9e926dffd7eafc567499ce1ea537486b) (const struct [device](structdevice.md) \*dev) |
|  | Check if the device is currently powered. |
| int | [pm\_device\_driver\_init](#gad563094c2d4ad066bc4ce30586e13fb3) (const struct [device](structdevice.md) \*dev, [pm\_device\_action\_cb\_t](#ga81d4ee32f5bbb1b343234b9b3afc0179) action\_cb) |
|  | Setup a device driver into the lowest valid power mode. |

## Detailed Description

Device Power Management API.

## Macro Definition Documentation

## [◆ ](#gae85fb5a7c31863a3663cef8dd7229c6c)PM\_DEVICE\_DEFINE

| #define PM\_DEVICE\_DEFINE | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pm\_action\_cb*, |
|  |  |  | ... ) |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

Z\_PM\_DEVICE\_DEFINE([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, pm\_action\_cb, \

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:83

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)

#define IS\_EMPTY(...)

Check if a macro has a replacement expression.

**Definition** util\_macro.h:301

Define device PM resources for the given device name.

Note
:   This macro is a no-op if `CONFIG_PM_DEVICE` is not enabled.

Parameters
:   | dev\_id | Device id. |
    | --- | --- |
    | pm\_action\_cb | PM control callback. |
    | ... | Optional flag to indicate that ISR safe. Use [PM\_DEVICE\_ISR\_SAFE](#ga18bb96fc4d5003516ab2eaf73cb35912) or 0. |

See also
:   [PM\_DEVICE\_DT\_DEFINE](#gaa2bd2c490fee99a6fc2b23605e799ef0), [PM\_DEVICE\_DT\_INST\_DEFINE](#ga5b201836d9c19a1c87cdde93631a4b0c)

## [◆ ](#gaa2bd2c490fee99a6fc2b23605e799ef0)PM\_DEVICE\_DT\_DEFINE

| #define PM\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *pm\_action\_cb*, |
|  |  |  | ... ) |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

Z\_PM\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), pm\_action\_cb, \

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

Define device PM resources for the given node identifier.

Note
:   This macro is a no-op if `CONFIG_PM_DEVICE` is not enabled.

Parameters
:   | node\_id | Node identifier. |
    | --- | --- |
    | pm\_action\_cb | PM control callback. |
    | ... | Optional flag to indicate that device is isr\_ok. Use [PM\_DEVICE\_ISR\_SAFE](#ga18bb96fc4d5003516ab2eaf73cb35912) or 0. |

See also
:   [PM\_DEVICE\_DT\_INST\_DEFINE](#ga5b201836d9c19a1c87cdde93631a4b0c), [PM\_DEVICE\_DEFINE](#gae85fb5a7c31863a3663cef8dd7229c6c)

## [◆ ](#gad244d742bc6b9874bfb90a2c3c87c4e8)PM\_DEVICE\_DT\_GET

| #define PM\_DEVICE\_DT\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

[PM\_DEVICE\_GET](#gaa94d19d0590659b7aba83566de9bd0c5)(Z\_DEVICE\_DT\_DEV\_ID(node\_id))

[PM\_DEVICE\_GET](#gaa94d19d0590659b7aba83566de9bd0c5)

#define PM\_DEVICE\_GET(dev\_id)

Obtain a reference to the device PM resources for the given device.

**Definition** device.h:378

Obtain a reference to the device PM resources for the given node.

Parameters
:   | node\_id | Node identifier. |
    | --- | --- |

Returns
:   Reference to the device PM resources (NULL if device `CONFIG_PM_DEVICE` is disabled).

## [◆ ](#ga5b201836d9c19a1c87cdde93631a4b0c)PM\_DEVICE\_DT\_INST\_DEFINE

| #define PM\_DEVICE\_DT\_INST\_DEFINE | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *pm\_action\_cb*, |
|  |  |  | ... ) |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

Z\_PM\_DEVICE\_DEFINE([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(idx), \

Z\_DEVICE\_DT\_DEV\_ID([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(idx)), \

pm\_action\_cb, \

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(\_\_VA\_ARGS\_\_), (0), (\_\_VA\_ARGS\_\_)))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Define device PM resources for the given instance.

Note
:   This macro is a no-op if `CONFIG_PM_DEVICE` is not enabled.

Parameters
:   | idx | Instance index. |
    | --- | --- |
    | pm\_action\_cb | PM control callback. |
    | ... | Optional flag to indicate that device is isr\_ok. Use [PM\_DEVICE\_ISR\_SAFE](#ga18bb96fc4d5003516ab2eaf73cb35912) or 0. |

See also
:   [PM\_DEVICE\_DT\_DEFINE](#gaa2bd2c490fee99a6fc2b23605e799ef0), [PM\_DEVICE\_DEFINE](#gae85fb5a7c31863a3663cef8dd7229c6c)

## [◆ ](#ga52892f2c34f6ccc9598002625baf12ce)PM\_DEVICE\_DT\_INST\_GET

| #define PM\_DEVICE\_DT\_INST\_GET | ( |  | *idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

[PM\_DEVICE\_DT\_GET](#gad244d742bc6b9874bfb90a2c3c87c4e8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(idx))

[PM\_DEVICE\_DT\_GET](#gad244d742bc6b9874bfb90a2c3c87c4e8)

#define PM\_DEVICE\_DT\_GET(node\_id)

Obtain a reference to the device PM resources for the given node.

**Definition** device.h:389

Obtain a reference to the device PM resources for the given instance.

Parameters
:   | idx | Instance index. |
    | --- | --- |

Returns
:   Reference to the device PM resources (NULL if device `CONFIG_PM_DEVICE` is disabled).

## [◆ ](#gaa94d19d0590659b7aba83566de9bd0c5)PM\_DEVICE\_GET

| #define PM\_DEVICE\_GET | ( |  | *dev\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

**Value:**

Z\_PM\_DEVICE\_GET(dev\_id)

Obtain a reference to the device PM resources for the given device.

Parameters
:   | dev\_id | Device id. |
    | --- | --- |

Returns
:   Reference to the device PM resources (NULL if device `CONFIG_PM_DEVICE` is disabled).

## [◆ ](#ga18bb96fc4d5003516ab2eaf73cb35912)PM\_DEVICE\_ISR\_SAFE

| #define PM\_DEVICE\_ISR\_SAFE   1 |
| --- |

`#include <[device.h](pm_2device_8h.md)>`

Flag indicating that runtime PM API for the device can be called from any context.

If [PM\_DEVICE\_ISR\_SAFE](#ga18bb96fc4d5003516ab2eaf73cb35912) flag is used for device definition, it indicates that PM actions are synchronous and can be executed from any context. This approach can be used for cases where suspending and resuming is short as it is executed in the critical section. This mode requires less resources (~80 byte less RAM) and allows to use device runtime PM from any context (including interrupts).

## Typedef Documentation

## [◆ ](#ga81d4ee32f5bbb1b343234b9b3afc0179)pm\_device\_action\_cb\_t

| typedef int(\* pm\_device\_action\_cb\_t) (const struct [device](structdevice.md) \*dev, enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) action) |
| --- |

`#include <[device.h](pm_2device_8h.md)>`

Device PM action callback.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | action | Requested action. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If the requested action is not supported. |
    | Errno | Other negative errno on failure. |

## [◆ ](#ga9cfb6437873089714635d2b26aafefac)pm\_device\_action\_failed\_cb\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* pm\_device\_action\_failed\_cb\_t) (const struct [device](structdevice.md) \*dev, int err) |
| --- |

`#include <[device.h](pm_2device_8h.md)>`

Device PM action failed callback.

Parameters
:   | dev | Device that failed the action. |
    | --- | --- |
    | err | Return code of action failure. |

Returns
:   True to continue iteration, false to halt iteration.

## Enumeration Type Documentation

## [◆ ](#gaee5546eacb9be7caa9d59ab63926cc4c)pm\_device\_action

| enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) |
| --- |

`#include <[device.h](pm_2device_8h.md)>`

Device PM actions.

| Enumerator | |
| --- | --- |
| PM\_DEVICE\_ACTION\_SUSPEND | Suspend. |
| PM\_DEVICE\_ACTION\_RESUME | Resume. |
| PM\_DEVICE\_ACTION\_TURN\_OFF | Turn off.  Note  Action triggered only by a power domain. |
| PM\_DEVICE\_ACTION\_TURN\_ON | Turn on.  Note  Action triggered only by a power domain. |

## [◆ ](#ga561c0789071e3c3963f21f4c4a1bb2c6)pm\_device\_state

| enum [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) |
| --- |

`#include <[device.h](pm_2device_8h.md)>`

Device power states.

| Enumerator | |
| --- | --- |
| PM\_DEVICE\_STATE\_ACTIVE | Device is in active or regular state. |
| PM\_DEVICE\_STATE\_SUSPENDED | Device is suspended.  Note  Device context may be lost. |
| PM\_DEVICE\_STATE\_SUSPENDING | Device is being suspended. |
| PM\_DEVICE\_STATE\_OFF | Device is turned off (power removed).  Note  Device context is lost. |

## Function Documentation

## [◆ ](#ga3840d6e7832a00b93763247a5951bfde)pm\_device\_action\_run()

| int pm\_device\_action\_run | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) | *action* ) |

`#include <[device.h](pm_2device_8h.md)>`

Run a pm action on a device.

This function calls the device PM control callback so that the device does the necessary operations to execute the given action.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | action | Device pm action. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | If requested state is not supported. |
    | -EALREADY | If device is already at the requested state. |
    | -EBUSY | If device is changing its state. |
    | -ENOSYS | If device does not support PM. |
    | -EPERM | If device has power state locked. |
    | Errno | Other negative errno on failure. |

## [◆ ](#ga8b527314f0c61b85602876b4f5a52275)pm\_device\_busy\_clear()

| void pm\_device\_busy\_clear | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Clear a device busy status.

Parameters
:   | dev | Device instance. |
    | --- | --- |

See also
:   [pm\_device\_busy\_set()](#ga7ea002352f3d1c90aecff1d54c255a06)

## [◆ ](#ga7ea002352f3d1c90aecff1d54c255a06)pm\_device\_busy\_set()

| void pm\_device\_busy\_set | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Mark a device as busy.

Devices marked as busy will not be suspended when the system goes into low-power states. This can be useful if, for example, the device is in the middle of a transaction.

Parameters
:   | dev | Device instance. |
    | --- | --- |

See also
:   [pm\_device\_busy\_clear()](#ga8b527314f0c61b85602876b4f5a52275)

## [◆ ](#ga765a5412f66070ccefd8e80ed9f62b1b)pm\_device\_children\_action\_run()

| void pm\_device\_children\_action\_run | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [pm\_device\_action](#gaee5546eacb9be7caa9d59ab63926cc4c) | *action*, |
|  |  | [pm\_device\_action\_failed\_cb\_t](#ga9cfb6437873089714635d2b26aafefac) | *failure\_cb* ) |

`#include <[device.h](pm_2device_8h.md)>`

Run a pm action on all children of a device.

This function calls all child devices PM control callback so that the device does the necessary operations to execute the given action.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | action | Device pm action. |
    | failure\_cb | Function to call if a child fails the action, can be NULL. |

## [◆ ](#gad563094c2d4ad066bc4ce30586e13fb3)pm\_device\_driver\_init()

| int pm\_device\_driver\_init | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [pm\_device\_action\_cb\_t](#ga81d4ee32f5bbb1b343234b9b3afc0179) | *action\_cb* ) |

`#include <[device.h](pm_2device_8h.md)>`

Setup a device driver into the lowest valid power mode.

This helper function is intended to be called at the end of a driver init function to automatically setup the device into the lowest power mode. It assumes that the device has been configured as if it is in [PM\_DEVICE\_STATE\_OFF](#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2), or [PM\_DEVICE\_STATE\_SUSPENDED](#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) if device can never be powered off.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | action\_cb | Device PM control callback function. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -errno | Error code from *action\_cb* on failure. |

## [◆ ](#gafb12ecf4679dd449e2faad0ede2c75fd)pm\_device\_init\_off()

| | void pm\_device\_init\_off | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Initialize a device state to [PM\_DEVICE\_STATE\_OFF](#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2).

By default device state is initialized to [PM\_DEVICE\_STATE\_ACTIVE](#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7). In general, this makes sense because the device initialization function will resume and configure a device, leaving it operational. However, when power domains are enabled, the device may be connected to a switchable power source, in which case it won't be powered at boot. This function can therefore be used to notify the PM subsystem that the device is in [PM\_DEVICE\_STATE\_OFF](#gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2) instead of the default.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#ga4c366f49e326a8b8e01d90cb2ee424ba)pm\_device\_init\_suspended()

| | void pm\_device\_init\_suspended | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Initialize a device state to [PM\_DEVICE\_STATE\_SUSPENDED](#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5).

By default device state is initialized to [PM\_DEVICE\_STATE\_ACTIVE](#gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7). However in order to save power some drivers may choose to only initialize the device to the suspended state, or actively put the device into the suspended state. This function can therefore be used to notify the PM subsystem that the device is in [PM\_DEVICE\_STATE\_SUSPENDED](#gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) instead of the default.

Parameters
:   | dev | Device instance. |
    | --- | --- |

## [◆ ](#gae59a1fbcd2399717076fbfcee1e5e411)pm\_device\_is\_any\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_is\_any\_busy | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if any device is busy.

Return values
:   | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If no device is busy |
    | --- | --- |
    | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If one or more devices are busy |

## [◆ ](#ga8ff7c3197d5ded860878302d00ac709c)pm\_device\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_is\_busy | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if a device is busy.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the device is not busy |
    | --- | --- |
    | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the device is busy |

## [◆ ](#ga9e926dffd7eafc567499ce1ea537486b)pm\_device\_is\_powered()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_is\_powered | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if the device is currently powered.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If device is currently powered, or is assumed to be powered (i.e. it does not support PM or is not under a PM domain) |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If device is not currently powered |

## [◆ ](#ga32eb5e210d2f0ba533b0185a94c8744e)pm\_device\_on\_power\_domain()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_on\_power\_domain | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if the device is on a switchable power domain.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If device is on a switchable power domain. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If device is not on a switchable power domain. |

## [◆ ](#gaa10a3f1ce71409cb591db416a1611377)pm\_device\_power\_domain\_add()

| int pm\_device\_power\_domain\_add | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *domain* ) |

`#include <[device.h](pm_2device_8h.md)>`

Add a device to a power domain.

This function adds a device to a given power domain.

Parameters
:   | dev | Device to be added to the power domain. |
    | --- | --- |
    | domain | Power domain. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EALREADY | If device is already part of the power domain. |
    | -ENOSYS | If the application was built without power domain support. |
    | -ENOSPC | If there is no space available in the power domain to add the device. |

## [◆ ](#ga1d7ab9b0b497e016b9b22d2506cd23f9)pm\_device\_power\_domain\_remove()

| int pm\_device\_power\_domain\_remove | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *domain* ) |

`#include <[device.h](pm_2device_8h.md)>`

Remove a device from a power domain.

This function removes a device from a given power domain.

Parameters
:   | dev | Device to be removed from the power domain. |
    | --- | --- |
    | domain | Power domain. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If the application was built without power domain support. |
    | -ENOENT | If device is not in the given domain. |

## [◆ ](#gaffcf0aea5df10657235d4ed1f8c74d5a)pm\_device\_state\_get()

| int pm\_device\_state\_get | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) \* | *state* ) |

`#include <[device.h](pm_2device_8h.md)>`

Obtain the power state of a device.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Pointer where device power state will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If device does not implement power management. |

## [◆ ](#gad109511e4314fa6145ee97dd655ec7bb)pm\_device\_state\_str()

| const char \* pm\_device\_state\_str | ( | enum [pm\_device\_state](#ga561c0789071e3c3963f21f4c4a1bb2c6) | *state* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Get name of device PM state.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State id which name should be returned |
    | --- | --- |

## [◆ ](#ga74fde62f71393fb9863916b3a2e5c460)pm\_device\_wakeup\_enable()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_wakeup\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[device.h](pm_2device_8h.md)>`

Enable or disable a device as a wake up source.

A device marked as a wake up source will not be suspended when the system goes into low-power modes, thus allowing to use it as a wake up source for the system.

Parameters
:   | dev | Device instance. |
    | --- | --- |
    | enable | `true` to enable or `false` to disable |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the wakeup source was successfully enabled. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the wakeup source was not successfully enabled. |

## [◆ ](#gac818aafb748b57d70909808b45d89379)pm\_device\_wakeup\_is\_capable()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_wakeup\_is\_capable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if a device is wake up capable.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If the device is wake up capable. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | If the device is not wake up capable. |

## [◆ ](#ga0716c6158804ac48022280d8d237f8c1)pm\_device\_wakeup\_is\_enabled()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pm\_device\_wakeup\_is\_enabled | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[device.h](pm_2device_8h.md)>`

Check if a device is enabled as a wake up source.

Parameters
:   | dev | Device instance. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the wakeup source is enabled. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the wakeup source is not enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
