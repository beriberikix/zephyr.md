---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usb__bc12_8h.html
original_path: doxygen/html/usb__bc12_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_bc12.h File Reference

Public APIs for the USB BC1.2 battery charging detect drivers.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/usb_bc12.h>`

[Go to the source code of this file.](usb__bc12_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bc12\_partner\_state](structbc12__partner__state.md) |
|  | BC1.2 detected partner state. [More...](structbc12__partner__state.md#details) |

| Macros | |
| --- | --- |
| BC1.2 constants | |
| #define | [BC12\_CHARGER\_VOLTAGE\_UV](group__b12__interface.md#gae32f7af00346f7baf968287eb874d880)   5000 \* 1000 |
|  | BC1.2 USB charger voltage. |
| #define | [BC12\_CHARGER\_MIN\_CURR\_UA](group__b12__interface.md#ga5ebbce02f5cb47de4565ef17d57ca25a)   2500 |
|  | BC1.2 USB charger minimum current. |
| #define | [BC12\_CHARGER\_MAX\_CURR\_UA](group__b12__interface.md#gaa327167a6bb6ee0c44b98faab708d1f2)   1500 \* 1000 |
|  | BC1.2 USB charger maximum current. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661)) (const struct [device](structdevice.md) \*dev, struct [bc12\_partner\_state](structbc12__partner__state.md) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), void \*user\_data) |
|  | BC1.2 callback for charger configuration. |

| Enumerations | |
| --- | --- |
| enum | [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) { [BC12\_DISCONNECTED](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a376830bcd04da44b9a2215a6f10dcf22) , [BC12\_PORTABLE\_DEVICE](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a8be0fd9ef5bc456b25964367388e3e48) , [BC12\_CHARGING\_PORT](group__b12__interface.md#gga035f4e4ba27f76094145571ebea97d73a2d7dffa7a9a134e55d48bf3c699d96ef) } |
|  | BC1.2 device role. [More...](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) |
| enum | [bc12\_type](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) {     [BC12\_TYPE\_NONE](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba55bff2c1d47018dc7d175c178c6eefe6) , [BC12\_TYPE\_SDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba4109f85b375b5dbfd2eada250fc06425) , [BC12\_TYPE\_DCP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba6ad9973121a077d239f8db7ecd7b76f3) , [BC12\_TYPE\_CDP](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba2b231ba4723445006b5993431064eb9c) ,     [BC12\_TYPE\_PROPRIETARY](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba08527a826ab4639e4e6a72dc54c51bb2) , [BC12\_TYPE\_UNKNOWN](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba25c692e9f22c761de33f738e08bf4e30) , [BC12\_TYPE\_COUNT](group__b12__interface.md#gga9ae800d490c2cbd3234a81c503649bdba672c2ed7c64ca4f13e1eb96456585d50)   } |
|  | BC1.2 charging partner type. [More...](group__b12__interface.md#ga9ae800d490c2cbd3234a81c503649bdb) |

| Functions | |
| --- | --- |
| int | [bc12\_set\_role](group__b12__interface.md#ga2a879017d34392308d4c078178db8407) (const struct [device](structdevice.md) \*dev, enum [bc12\_role](group__b12__interface.md#ga035f4e4ba27f76094145571ebea97d73) role) |
|  | Set the BC1.2 role. |
| int | [bc12\_set\_result\_cb](group__b12__interface.md#ga0db43c4cc595cb76738cf24d97fa5228) (const struct [device](structdevice.md) \*dev, [bc12\_callback\_t](group__b12__interface.md#gaeb039486c7826fe493e7f402212f2661) cb, void \*user\_data) |
|  | Register a callback for BC1.2 results. |

## Detailed Description

Public APIs for the USB BC1.2 battery charging detect drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [usb\_bc12.h](usb__bc12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
