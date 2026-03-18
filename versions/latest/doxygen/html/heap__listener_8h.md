---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/heap__listener_8h.html
original_path: doxygen/html/heap__listener_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

heap\_listener.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](heap__listener_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [heap\_listener](structheap__listener.md) |

| Macros | |
| --- | --- |
| #define | [HEAP\_ID\_FROM\_POINTER](group__heap__listener__apis.md#ga77e603053a5b69caae2a49e441a525c0)(heap\_pointer) |
|  | Construct heap identifier from heap pointer. |
| #define | [HEAP\_ID\_LIBC](group__heap__listener__apis.md#ga7627d1b500bb7e833770c99071f9255d)   (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))0) |
|  | Libc heap identifier. |
| #define | [HEAP\_LISTENER\_ALLOC\_DEFINE](group__heap__listener__apis.md#ga1854b23cbd41dec0d8262e8f122ebd5d)(name, \_heap\_id, \_alloc\_cb) |
|  | Define heap event listener node for allocation event. |
| #define | [HEAP\_LISTENER\_FREE\_DEFINE](group__heap__listener__apis.md#ga7e5822ebd4c08235b01cf99cd6fe10e8)(name, \_heap\_id, \_free\_cb) |
|  | Define heap event listener node for free event. |
| #define | [HEAP\_LISTENER\_RESIZE\_DEFINE](group__heap__listener__apis.md#gaa4fa9685749e050ca06e7cdc99b7c970)(name, \_heap\_id, \_resize\_cb) |
|  | Define heap event listener node for resize event. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [heap\_listener\_resize\_cb\_t](group__heap__listener__apis.md#gad8addd23bfb3f303c10c13024a8c29ce)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end) |
|  | Callback used when heap is resized. |
| typedef void(\* | [heap\_listener\_alloc\_cb\_t](group__heap__listener__apis.md#ga325f3d6679f9bc6d6d1b2e98c8efd2f6)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Callback used when there is heap allocation. |
| typedef void(\* | [heap\_listener\_free\_cb\_t](group__heap__listener__apis.md#ga8a2e3c13b898647618ba93cd592e406f)) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Callback used when memory is freed from heap. |

| Enumerations | |
| --- | --- |
| enum | [heap\_event\_types](group__heap__listener__apis.md#ga9679320e1c32dcbad726789946565510) {     [HEAP\_EVT\_UNKNOWN](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510ae82b3e0225bde5553f472c5f00985b18) = 0 , [HEAP\_RESIZE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a198aa2475e58078a46cf79ffb0914408) , [HEAP\_ALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a23ece0bd476a164e251ebd1af61f0008) , [HEAP\_FREE](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510a82e2137ada931f068fa36d40245f5a80) ,     [HEAP\_REALLOC](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510aa64f229b21eedbca9a581b60e3da5a50) , [HEAP\_MAX\_EVENTS](group__heap__listener__apis.md#gga9679320e1c32dcbad726789946565510afb3a6f56a29d74c35db90fbeaa61a3b6)   } |

| Functions | |
| --- | --- |
| void | [heap\_listener\_register](group__heap__listener__apis.md#ga63d5470d9ca312ccc80d35c7f8dea200) (struct [heap\_listener](structheap__listener.md) \*listener) |
|  | Register heap event listener. |
| void | [heap\_listener\_unregister](group__heap__listener__apis.md#ga872e123af0a5349e45fcedfd8b83b508) (struct [heap\_listener](structheap__listener.md) \*listener) |
|  | Unregister heap event listener. |
| void | [heap\_listener\_notify\_alloc](group__heap__listener__apis.md#gaebe49e01cba6d327c635da4795e37e22) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Notify listeners of heap allocation event. |
| void | [heap\_listener\_notify\_free](group__heap__listener__apis.md#ga8fd3dc5b65e3bc8bbc1dadaa741d47fc) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*mem, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes) |
|  | Notify listeners of heap free event. |
| void | [heap\_listener\_notify\_resize](group__heap__listener__apis.md#ga9d3062fbcdc10edc3839193e8ea79654) ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) heap\_id, void \*old\_heap\_end, void \*new\_heap\_end) |
|  | Notify listeners of heap resize event. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [heap\_listener.h](heap__listener_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
