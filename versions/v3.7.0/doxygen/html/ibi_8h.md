---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ibi_8h.html
original_path: doxygen/html/ibi_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ibi.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](ibi_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_ibi](structi3c__ibi.md) |
|  | Struct for IBI request. [More...](structi3c__ibi.md#details) |
| struct | [i3c\_ibi\_payload](structi3c__ibi__payload.md) |
|  | Structure of payload buffer for IBI. [More...](structi3c__ibi__payload.md#details) |
| struct | [i3c\_ibi\_work](structi3c__ibi__work.md) |
|  | Node about a queued IBI. [More...](structi3c__ibi__work.md#details) |

| Macros | |
| --- | --- |
| #define | [CONFIG\_I3C\_IBI\_MAX\_PAYLOAD\_SIZE](group__i3c__ibi.md#ga7bbbff351dc33d1c00abf6c22bbd50d4)   0 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c)) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ibi\_payload](structi3c__ibi__payload.md) \*payload) |
|  | Function called when In-Band Interrupt received from target device. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_ibi\_type](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) {     [I3C\_IBI\_TARGET\_INTR](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba368e8ad08a003ebf197add6d73ffd43d) , [I3C\_IBI\_CONTROLLER\_ROLE\_REQUEST](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba00235d326559f945d54638b0c0558815) , [I3C\_IBI\_HOTJOIN](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba493d3b1e9669434c3d62f16aa3d6f92f) , [I3C\_IBI\_TYPE\_MAX](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862baab12781f76c743cec6b72ffa7d8c27ee) = I3C\_IBI\_HOTJOIN ,     [I3C\_IBI\_WORKQUEUE\_CB](group__i3c__ibi.md#ggaf4be72fc9c862d996d860c0b7fbc862ba39d8f6a9b69d092eabf9ca9726deec8c)   } |
|  | IBI Types. [More...](group__i3c__ibi.md#gaf4be72fc9c862d996d860c0b7fbc862b) |

| Functions | |
| --- | --- |
| int | [i3c\_ibi\_work\_enqueue](group__i3c__ibi.md#gaafc2fdf9f2402691c3ebe11d06106840) (struct [i3c\_ibi\_work](structi3c__ibi__work.md) \*ibi\_work) |
|  | Queue an IBI work item for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_target\_irq](group__i3c__ibi.md#ga7fbf838ea07516849dc1296d48af65d1) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) payload\_len) |
|  | Queue a target interrupt IBI for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_hotjoin](group__i3c__ibi.md#gab135cb893efd50c7db16c1734b6a0bab) (const struct [device](structdevice.md) \*dev) |
|  | Queue a hot join IBI for future processing. |
| int | [i3c\_ibi\_work\_enqueue\_cb](group__i3c__ibi.md#ga4c6f4516e55d0ab6c539fb800d7ec45a) (const struct [device](structdevice.md) \*dev, [k\_work\_handler\_t](group__workqueue__apis.md#ga5add9ef0dce306a08413c4140fc0bdda) work\_cb) |
|  | Queue a generic callback for future processing. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [ibi.h](ibi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
