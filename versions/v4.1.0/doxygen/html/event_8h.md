---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/event_8h.html
original_path: doxygen/html/event_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

event.h File Reference

hawkBit event header file
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](event_8h_source.md)

| Macros | |
| --- | --- |
| #define | [HAWKBIT\_EVENT\_CREATE\_CALLBACK](group__hawkbit__event.md#ga05eec89437dfd13a022ba2eac6b1e0d9)(\_callback, \_handler, \_event) |
|  | Macro to create and initialize a struct hawkbit\_event\_callback properly. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458)) (struct hawkbit\_event\_callback \*cb, enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) event) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) {     [HAWKBIT\_EVENT\_ERROR](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd) , [HAWKBIT\_EVENT\_ERROR\_NETWORKING](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214) , [HAWKBIT\_EVENT\_ERROR\_PERMISSION](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a) , [HAWKBIT\_EVENT\_ERROR\_METADATA](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8) ,     [HAWKBIT\_EVENT\_ERROR\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c) , [HAWKBIT\_EVENT\_ERROR\_ALLOC](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639) , [HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4) , [HAWKBIT\_EVENT\_NO\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e) ,     [HAWKBIT\_EVENT\_CANCEL\_UPDATE](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b) , [HAWKBIT\_EVENT\_START\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55) , [HAWKBIT\_EVENT\_END\_DOWNLOAD](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984) , [HAWKBIT\_EVENT\_START\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3) ,     [HAWKBIT\_EVENT\_END\_RUN](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2) , [HAWKBIT\_EVENT\_BEFORE\_REBOOT](group__hawkbit__event.md#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)   } |
|  | hawkBit event type. [More...](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) |

| Functions | |
| --- | --- |
| static void | [hawkbit\_event\_init\_callback](group__hawkbit__event.md#ga0ec141ff3e11c0e1d0e3f8757ace5010) (struct hawkbit\_event\_callback \*callback, [hawkbit\_event\_callback\_handler\_t](group__hawkbit__event.md#ga49064aef93c5383f24ea41819b78c458) handler, enum [hawkbit\_event\_type](group__hawkbit__event.md#ga794d232d73d105bd170b222ab17ce2af) event) |
|  | Helper to initialize a struct hawkbit\_event\_callback properly. |
| int | [hawkbit\_event\_add\_callback](group__hawkbit__event.md#ga646c72464b0761009f42393fa313c880) (struct hawkbit\_event\_callback \*cb) |
|  | Add an application callback. |
| int | [hawkbit\_event\_remove\_callback](group__hawkbit__event.md#gaa19bb74cb46e9aff7742907a86c96359) (struct hawkbit\_event\_callback \*cb) |
|  | Remove an application callback. |

## Detailed Description

hawkBit event header file

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [hawkbit](dir_a48dfaa3f142fb7c063e17169510ae85.md)
- [event.h](event_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
