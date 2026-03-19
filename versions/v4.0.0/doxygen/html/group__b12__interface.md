---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__b12__interface.html
original_path: doxygen/html/group__b12__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BC1.2 driver APIs

[Device Driver APIs](group__io__interfaces.md)

BC1.2 driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bc12\_partner\_state](structbc12__partner__state.md) |
|  | BC1.2 detected partner state. [More...](structbc12__partner__state.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bc12\_callback\_t](#gaeb039486c7826fe493e7f402212f2661)) (const struct [device](structdevice.md) \*dev, struct [bc12\_partner\_state](structbc12__partner__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | BC1.2 callback for charger configuration. |

| Enumerations | |
| --- | --- |
| enum | [bc12\_role](#ga035f4e4ba27f76094145571ebea97d73) { [BC12\_DISCONNECTED](#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22) , [BC12\_PORTABLE\_DEVICE](#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48) , [BC12\_CHARGING\_PORT](#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef) } |
|  | BC1.2 device role. [More...](#ga035f4e4ba27f76094145571ebea97d73) |
| enum | [bc12\_type](#ga9ae800d490c2cbd3234a81c503649bdb) {     [BC12\_TYPE\_NONE](#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6) , [BC12\_TYPE\_SDP](#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425) , [BC12\_TYPE\_DCP](#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3) , [BC12\_TYPE\_CDP](#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c) ,     [BC12\_TYPE\_PROPRIETARY](#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2) , [BC12\_TYPE\_UNKNOWN](#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30) , [BC12\_TYPE\_COUNT](#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)   } |
|  | BC1.2 charging partner type. [More...](#ga9ae800d490c2cbd3234a81c503649bdb) |

| Functions | |
| --- | --- |
| int | [bc12\_set\_role](#ga2a879017d34392308d4c078178db8407) (const struct [device](structdevice.md) \*dev, enum [bc12\_role](#ga035f4e4ba27f76094145571ebea97d73) role) |
|  | Set the BC1.2 role. |
| int | [bc12\_set\_result\_cb](#ga0db43c4cc595cb76738cf24d97fa5228) (const struct [device](structdevice.md) \*dev, [bc12\_callback\_t](#gaeb039486c7826fe493e7f402212f2661) cb, void \*user\_data) |
|  | Register a callback for BC1.2 results. |

| BC1.2 constants | |
| --- | --- |
| #define | [BC12\_CHARGER\_VOLTAGE\_UV](#gae32f7af00346f7baf968287eb874d880)   5000 \* 1000 |
|  | BC1.2 USB charger voltage. |
| #define | [BC12\_CHARGER\_MIN\_CURR\_UA](#ga5ebbce02f5cb47de4565ef17d57ca25a)   2500 |
|  | BC1.2 USB charger minimum current. |
| #define | [BC12\_CHARGER\_MAX\_CURR\_UA](#gaa327167a6bb6ee0c44b98faab708d1f2)   1500 \* 1000 |
|  | BC1.2 USB charger maximum current. |

## Detailed Description

BC1.2 driver APIs.

## Macro Definition Documentation

## [◆ ](#gaa327167a6bb6ee0c44b98faab708d1f2)BC12\_CHARGER\_MAX\_CURR\_UA

| #define BC12\_CHARGER\_MAX\_CURR\_UA   1500 \* 1000 |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 USB charger maximum current.

## [◆ ](#ga5ebbce02f5cb47de4565ef17d57ca25a)BC12\_CHARGER\_MIN\_CURR\_UA

| #define BC12\_CHARGER\_MIN\_CURR\_UA   2500 |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 USB charger minimum current.

Set to match the Isusp of 2.5 mA parameter. This is returned by the driver when either BC1.2 detection fails, or the attached partner is a SDP (standard downstream port).

The application may increase the current draw after determining the USB device state of suspended/unconfigured/configured. Suspended: 2.5 mA Unconfigured: 100 mA Configured: 500 mA (USB 2.0)

## [◆ ](#gae32f7af00346f7baf968287eb874d880)BC12\_CHARGER\_VOLTAGE\_UV

| #define BC12\_CHARGER\_VOLTAGE\_UV   5000 \* 1000 |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 USB charger voltage.

## Typedef Documentation

## [◆ ](#gaeb039486c7826fe493e7f402212f2661)bc12\_callback\_t

| typedef void(\* bc12\_callback\_t) (const struct [device](structdevice.md) \*dev, struct [bc12\_partner\_state](structbc12__partner__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 callback for charger configuration.

Parameters
:   | dev | BC1.2 device which is notifying of the new charger state. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Current state of the BC1.2 client, including BC1.2 type detected, voltage, and current limits. If NULL, then the partner charger is disconnected or the BC1.2 device is operating in host mode. |
    | user\_data | Requester supplied data which is passed along to the callback. |

## Enumeration Type Documentation

## [◆ ](#ga035f4e4ba27f76094145571ebea97d73)bc12\_role

| enum [bc12\_role](#ga035f4e4ba27f76094145571ebea97d73) |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 device role.

| Enumerator | |
| --- | --- |
| BC12\_DISCONNECTED |  |
| BC12\_PORTABLE\_DEVICE |  |
| BC12\_CHARGING\_PORT |  |

## [◆ ](#ga9ae800d490c2cbd3234a81c503649bdb)bc12\_type

| enum [bc12\_type](#ga9ae800d490c2cbd3234a81c503649bdb) |
| --- |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

BC1.2 charging partner type.

| Enumerator | |
| --- | --- |
| BC12\_TYPE\_NONE | No partner connected. |
| BC12\_TYPE\_SDP | Standard Downstream Port. |
| BC12\_TYPE\_DCP | Dedicated Charging Port. |
| BC12\_TYPE\_CDP | Charging Downstream Port. |
| BC12\_TYPE\_PROPRIETARY | Proprietary charging port. |
| BC12\_TYPE\_UNKNOWN | Unknown charging port, BC1.2 detection failed. |
| BC12\_TYPE\_COUNT | Count of valid BC12 types. |

## Function Documentation

## [◆ ](#ga0db43c4cc595cb76738cf24d97fa5228)bc12\_set\_result\_cb()

| int bc12\_set\_result\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bc12\_callback\_t](#gaeb039486c7826fe493e7f402212f2661) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

Register a callback for BC1.2 results.

Parameters
:   | dev | Pointer to the device structure for the BC1.2 driver instance. |
    | --- | --- |
    | cb | Function pointer for the result callback. |
    | user\_data | Requester supplied data which is passed along to the callback. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | general input/output error. |

## [◆ ](#ga2a879017d34392308d4c078178db8407)bc12\_set\_role()

| int bc12\_set\_role | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [bc12\_role](#ga035f4e4ba27f76094145571ebea97d73) | *role* ) |

`#include <[usb_bc12.h](usb__bc12_8h.md)>`

Set the BC1.2 role.

Parameters
:   | dev | Pointer to the device structure for the BC1.2 driver instance. |
    | --- | --- |
    | role | New role for the BC1.2 device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | general input/output error. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
