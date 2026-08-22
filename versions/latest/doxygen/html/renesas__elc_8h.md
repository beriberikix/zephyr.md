---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__elc_8h.html
original_path: doxygen/html/renesas__elc_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_elc.h File Reference

Public APIs for the Renesas ELC driver.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/internal/syscall_handler.h](syscall__handler_8h_source.md)>`  
`#include <zephyr/syscalls/renesas_elc.h>`

[Go to the source code of this file.](renesas__elc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [renesas\_elc\_dt\_spec](structrenesas__elc__dt__spec.md) |
|  | Container for Renesas ELC information specified in devicetree. [More...](structrenesas__elc__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME](group__renesas__elc__interface.md#ga32d4b23c3857552a8fe1ca6ce04f97d4)(node\_id, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX](group__renesas__elc__interface.md#ga79a705be3efa01b6fcc1413dd4acfec2)(node\_id, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_NAME\_OR\_NULL](group__renesas__elc__interface.md#ga996e259c97fc2511086664865b4c0e3d)(node\_id, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_GET\_BY\_IDX\_OR\_NULL](group__renesas__elc__interface.md#ga5e79207cee205406247a972e23360110)(node\_id, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME](group__renesas__elc__interface.md#gaab4d583c93f1d5990d4a6733caaded81)(inst, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX](group__renesas__elc__interface.md#ga788709121dbfb2db3f74ccf9a9d51002)(inst, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_NAME\_OR\_NULL](group__renesas__elc__interface.md#ga1d58940758c664c22cb3e183e9810370)(inst, name) |
|  | Get the device pointer from the "renesas-elcs" property by element name for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_DEVICE\_INST\_GET\_BY\_IDX\_OR\_NULL](group__renesas__elc__interface.md#ga65ccb580212ee15dc9329d76e810190e)(inst, idx) |
|  | Get the device pointer from the "renesas-elcs" property by index for a DT\_DRV\_COMPAT instance, or return NULL if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME](group__renesas__elc__interface.md#ga1f196ad20380dedf193c754906c5ed14)(node\_id, name) |
|  | Get the peripheral cell value from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX](group__renesas__elc__interface.md#gace33f51f3a3a2efd42932a816e05be0b)(node\_id, idx) |
|  | Get the peripheral cell value from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_NAME\_OR](group__renesas__elc__interface.md#ga35d7aef6829d74e92fa7c82306711a6c)(node\_id, name, default\_value) |
|  | Get the peripheral cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_GET\_BY\_IDX\_OR](group__renesas__elc__interface.md#ga915d2760bd3c8ecf1b689bed286035d8)(node\_id, idx, default\_value) |
|  | Get the peripheral cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME](group__renesas__elc__interface.md#ga3a0b277cb45636a86bf9b665fd75d133)(inst, name) |
|  | Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX](group__renesas__elc__interface.md#gaeab186e0f09ee56ce87719a7d5566f50)(inst, idx) |
|  | Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_NAME\_OR](group__renesas__elc__interface.md#ga0e1c393825d778fd22a9a190eaedc308)(inst, name, default\_value) |
|  | Get the peripheral cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_PERIPHERAL\_INST\_GET\_BY\_IDX\_OR](group__renesas__elc__interface.md#ga360d362b3fc26afb7cc81bfd28f6fc6a)(inst, idx, default\_value) |
|  | Get the peripheral cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME](group__renesas__elc__interface.md#ga920e3b26fb52a728ed2a3cd1ab5af7f0)(node\_id, name) |
|  | Get the event cell value from the "renesas-elcs" property by element name. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX](group__renesas__elc__interface.md#ga6f3093b0556eb8eb1931e9b8b746245a)(node\_id, idx) |
|  | Get the event cell value from the "renesas-elcs" property by index. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_NAME\_OR](group__renesas__elc__interface.md#ga41c5adcf8817d529b5521727d9937b42)(node\_id, name, default\_value) |
|  | Get the event cell value from the "renesas-elcs" property by element name, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_GET\_BY\_IDX\_OR](group__renesas__elc__interface.md#ga2b0a12781acca4123dd7899446a94b6f)(node\_id, idx, default\_value) |
|  | Get the event cell value from the "renesas-elcs" property by index, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME](group__renesas__elc__interface.md#ga86ded9427001c5d3b315b71dcbfad7d0)(inst, name) |
|  | Get the event cell value by element name for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX](group__renesas__elc__interface.md#gac5dfa5e30e1ac9ac703842e61dd3fa3b)(inst, idx) |
|  | Get the event cell value by index for a DT\_DRV\_COMPAT instance. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_NAME\_OR](group__renesas__elc__interface.md#ga94f2bc95761722c93019371f432da262)(inst, name, default\_value) |
|  | Get the event cell value by element name for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |
| #define | [RENESAS\_ELC\_DT\_SPEC\_EVENT\_INST\_GET\_BY\_IDX\_OR](group__renesas__elc__interface.md#ga7d57a1a3bf47feda6c2831712bfd033c)(inst, idx, default\_value) |
|  | Get the event cell value by index for a DT\_DRV\_COMPAT instance, or return a default value if the property does not exist. |

| Functions | |
| --- | --- |
| int | [renesas\_elc\_software\_event\_generate](group__renesas__elc__interface.md#gab3b55b83b38469854aae726a71f6ad55) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Generate a software event in the Event Link Controller. |
| int | [renesas\_elc\_link\_set](group__renesas__elc__interface.md#ga444e17d01310283e61bcde9a1022c47a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event) |
|  | Create a single event link. |
| int | [renesas\_elc\_link\_break](group__renesas__elc__interface.md#ga65c950ccf0087c514daf6d543a0a7ecf) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peripheral) |
|  | Break an event link. |
| int | [renesas\_elc\_enable](group__renesas__elc__interface.md#gafbffc029fd9482be578bd05cbdb3a03f) (const struct [device](structdevice.md) \*dev) |
|  | Enable the operation of the Event Link Controller. |
| int | [renesas\_elc\_disable](group__renesas__elc__interface.md#gaac75089657f841c80225aa40de9c2a93) (const struct [device](structdevice.md) \*dev) |
|  | Disable the operation of the Event Link Controller. |

## Detailed Description

Public APIs for the Renesas ELC driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [interconn](dir_433d0485cb495c15eb8c324a866644da.md)
- [renesas\_elc](dir_41f42e06f91d3fe7cdafa18f2f825332.md)
- [renesas\_elc.h](renesas__elc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
