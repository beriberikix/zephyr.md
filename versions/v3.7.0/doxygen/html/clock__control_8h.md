---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/clock__control_8h.html
original_path: doxygen/html/clock__control_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control.h File Reference

Public Clock Control APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [clock\_control\_driver\_api](structclock__control__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [CLOCK\_CONTROL\_SUBSYS\_ALL](group__clock__control__interface.md#ga9aa9a4e00c1e7985a1fea6bed235003e)   NULL |

| Typedefs | |
| --- | --- |
| typedef void \* | [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) |
|  | [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db "clock_control_subsys_t is a type to identify a clock controller sub-system.") is a type to identify a clock controller sub-system. |
| typedef void \* | [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) |
|  | [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1 "clock_control_subsys_rate_t is a type to identify a clock controller sub-system rate.") is a type to identify a clock controller sub-system rate. |
| typedef void(\* | [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) subsys, void \*user\_data) |
|  | Callback called on clock started. |
| typedef int(\* | [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys) |
| typedef int(\* | [clock\_control\_get](group__clock__control__interface.md#ga41087b8914b4bec0c1a61217122cc2a0)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
| typedef int(\* | [clock\_control\_async\_on\_fn](group__clock__control__interface.md#ga0cd408e023fda272784c24d0c644014d)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb, void \*user\_data) |
| typedef enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09)(\* | [clock\_control\_get\_status\_fn](group__clock__control__interface.md#ga0af123fbaa3572a9722f17c331936e9a)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys) |
| typedef int(\* | [clock\_control\_set](group__clock__control__interface.md#ga8ea31ee8a6e3aa69de0098efba63ae2b)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate) |
| typedef int(\* | [clock\_control\_configure\_fn](group__clock__control__interface.md#ga1f7e0aa491a5cccbe49015ed1f5cfef0)) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, void \*data) |

| Enumerations | |
| --- | --- |
| enum | [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) { [CLOCK\_CONTROL\_STATUS\_STARTING](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09aa1d03cc305aa2f510471e6f1ae1fbd52) , [CLOCK\_CONTROL\_STATUS\_OFF](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a44a027c5e5bf19836aebc427098f0cfa) , [CLOCK\_CONTROL\_STATUS\_ON](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a232119a145ecc5d6a1ff0454a97c92db) , [CLOCK\_CONTROL\_STATUS\_UNKNOWN](group__clock__control__interface.md#ggad12829335f0c954ab6d586549db45e09a4c939e7c8c38b5f2c50fe339a60c75cc) } |
|  | Current clock status. [More...](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) |

| Functions | |
| --- | --- |
| static int | [clock\_control\_on](group__clock__control__interface.md#gaec69b0989cefad79ffd5c92f060150b9) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Enable a clock controlled by the device. |
| static int | [clock\_control\_off](group__clock__control__interface.md#gadbebc1c12937be561b761ef4a3b7d8a5) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Disable a clock controlled by the device. |
| static int | [clock\_control\_async\_on](group__clock__control__interface.md#ga03cedb9723e001d01c495f0abb6acfdf) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_cb\_t](group__clock__control__interface.md#ga17257fb3864dc5a33082c3422ad7c275) cb, void \*user\_data) |
|  | Request clock to start with notification when clock has been started. |
| static enum [clock\_control\_status](group__clock__control__interface.md#gad12829335f0c954ab6d586549db45e09) | [clock\_control\_get\_status](group__clock__control__interface.md#ga35be64d09222f44aa00cd1371a39613e) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys) |
|  | Get clock status. |
| static int | [clock\_control\_get\_rate](group__clock__control__interface.md#ga00f6af6d2668c2dfff0640fe176e89ff) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Obtain the clock rate of given sub-system. |
| static int | [clock\_control\_set\_rate](group__clock__control__interface.md#ga3bd25314e8bfcc62f0728d89321bb614) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, [clock\_control\_subsys\_rate\_t](group__clock__control__interface.md#ga05d8b476ef0331e1502702921d2801f1) rate) |
|  | Set the rate of the clock controlled by the device. |
| static int | [clock\_control\_configure](group__clock__control__interface.md#gaf5e4b13798955fcc891c080b9967ab06) (const struct [device](structdevice.md) \*dev, [clock\_control\_subsys\_t](group__clock__control__interface.md#gaa7d3935eaaf18902801a7d94859483db) sys, void \*data) |
|  | Configure a source clock. |

## Detailed Description

Public Clock Control APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control.h](clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
