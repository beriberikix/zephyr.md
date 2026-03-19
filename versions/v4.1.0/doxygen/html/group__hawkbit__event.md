---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__hawkbit__event.html
original_path: doxygen/html/group__hawkbit__event.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkBit event API

[Third-party](group__third__party.md) » [hawkBit Firmware Over-the-Air](group__hawkbit.md)

hawkBit event API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [HAWKBIT\_EVENT\_CREATE\_CALLBACK](#ga05eec89437dfd13a022ba2eac6b1e0d9)(\_callback, \_handler, \_event) |
|  | Macro to create and initialize a struct hawkbit\_event\_callback properly. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [hawkbit\_event\_callback\_handler\_t](#ga49064aef93c5383f24ea41819b78c458)) (struct hawkbit\_event\_callback \*cb, enum [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) event) |
|  | Define the application callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) {     [HAWKBIT\_EVENT\_ERROR](#gga794d232d73d105bd170b222ab17ce2afa4ab9fcb6bebf167eff6fb2311da735dd) , [HAWKBIT\_EVENT\_ERROR\_NETWORKING](#gga794d232d73d105bd170b222ab17ce2afad8ed1ca4798bcd479f11d613a20e2214) , [HAWKBIT\_EVENT\_ERROR\_PERMISSION](#gga794d232d73d105bd170b222ab17ce2afa435e07a36fec3d4a1d94926d8caa9d7a) , [HAWKBIT\_EVENT\_ERROR\_METADATA](#gga794d232d73d105bd170b222ab17ce2afafc267582eeed1249830e888e0f8a6bd8) ,     [HAWKBIT\_EVENT\_ERROR\_DOWNLOAD](#gga794d232d73d105bd170b222ab17ce2afa70e2d5b23859484b758c446d0e7c624c) , [HAWKBIT\_EVENT\_ERROR\_ALLOC](#gga794d232d73d105bd170b222ab17ce2afa0a6f33bbaeff8c0e3b1c6aba0cdf0639) , [HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED](#gga794d232d73d105bd170b222ab17ce2afa645bec5a542a24f3696241921f89d3a4) , [HAWKBIT\_EVENT\_NO\_UPDATE](#gga794d232d73d105bd170b222ab17ce2afa516265be2515ca5f1b95517b04d0522e) ,     [HAWKBIT\_EVENT\_CANCEL\_UPDATE](#gga794d232d73d105bd170b222ab17ce2afae7cbf7ba78059186080e633965244e8b) , [HAWKBIT\_EVENT\_START\_DOWNLOAD](#gga794d232d73d105bd170b222ab17ce2afaaa1680961ce8487c98dc4299003b0b55) , [HAWKBIT\_EVENT\_END\_DOWNLOAD](#gga794d232d73d105bd170b222ab17ce2afa9f01289c7aa75e335e1fb8b05e5ec984) , [HAWKBIT\_EVENT\_START\_RUN](#gga794d232d73d105bd170b222ab17ce2afab6e6a48faa3ed32b8fef2b4cce4c29d3) ,     [HAWKBIT\_EVENT\_END\_RUN](#gga794d232d73d105bd170b222ab17ce2afa0b5b571646812e7b31953899d512b4e2) , [HAWKBIT\_EVENT\_BEFORE\_REBOOT](#gga794d232d73d105bd170b222ab17ce2afa27254d0c181c7736de5fa9c281fc92cf)   } |
|  | hawkBit event type. [More...](#ga794d232d73d105bd170b222ab17ce2af) |

| Functions | |
| --- | --- |
| static void | [hawkbit\_event\_init\_callback](#ga0ec141ff3e11c0e1d0e3f8757ace5010) (struct hawkbit\_event\_callback \*callback, [hawkbit\_event\_callback\_handler\_t](#ga49064aef93c5383f24ea41819b78c458) handler, enum [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) event) |
|  | Helper to initialize a struct hawkbit\_event\_callback properly. |
| int | [hawkbit\_event\_add\_callback](#ga646c72464b0761009f42393fa313c880) (struct hawkbit\_event\_callback \*cb) |
|  | Add an application callback. |
| int | [hawkbit\_event\_remove\_callback](#gaa19bb74cb46e9aff7742907a86c96359) (struct hawkbit\_event\_callback \*cb) |
|  | Remove an application callback. |

## Detailed Description

hawkBit event API.

## Macro Definition Documentation

## [◆ ](#ga05eec89437dfd13a022ba2eac6b1e0d9)HAWKBIT\_EVENT\_CREATE\_CALLBACK

| #define HAWKBIT\_EVENT\_CREATE\_CALLBACK | ( |  | *\_callback*, |
| --- | --- | --- | --- |
|  |  |  | *\_handler*, |
|  |  |  | *\_event* ) |

`#include <[event.h](event_8h.md)>`

**Value:**

struct hawkbit\_event\_callback \_callback = { \

.handler = \_handler, \

.event = \_event, \

}

Macro to create and initialize a struct hawkbit\_event\_callback properly.

This macro can be used instead of [hawkbit\_event\_init\_callback()](#ga0ec141ff3e11c0e1d0e3f8757ace5010).

Parameters
:   | \_callback | Name of the callback structure |
    | --- | --- |
    | \_handler | A valid handler function pointer. |
    | \_event | The event of [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) that will trigger the callback |

## Typedef Documentation

## [◆ ](#ga49064aef93c5383f24ea41819b78c458)hawkbit\_event\_callback\_handler\_t

| typedef void(\* hawkbit\_event\_callback\_handler\_t) (struct hawkbit\_event\_callback \*cb, enum [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) event) |
| --- |

`#include <[event.h](event_8h.md)>`

Define the application callback handler function signature.

Parameters
:   | cb | Original struct hawkbit\_event\_callback owning this handler |
    | --- | --- |
    | event | The event that triggered the callback |

Note: cb pointer can be used to retrieve private data through [CONTAINER\_OF()](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f "Get a pointer to a structure containing the element.") if original struct hawkbit\_event\_callback is stored in another private structure.

## Enumeration Type Documentation

## [◆ ](#ga794d232d73d105bd170b222ab17ce2af)hawkbit\_event\_type

| enum [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) |
| --- |

`#include <[event.h](event_8h.md)>`

hawkBit event type.

These events are used to register the callback functions.

| Enumerator | |
| --- | --- |
| HAWKBIT\_EVENT\_ERROR | Event triggered when there was an error. |
| HAWKBIT\_EVENT\_ERROR\_NETWORKING | Event triggered when there was a networking error. |
| HAWKBIT\_EVENT\_ERROR\_PERMISSION | Event triggered when there was a permission error. |
| HAWKBIT\_EVENT\_ERROR\_METADATA | Event triggered when there was a metadata error. |
| HAWKBIT\_EVENT\_ERROR\_DOWNLOAD | Event triggered when there was a download error. |
| HAWKBIT\_EVENT\_ERROR\_ALLOC | Event triggered when there was an allocation error. |
| HAWKBIT\_EVENT\_UPDATE\_DOWNLOADED | Event triggered when a new update was downloaded. |
| HAWKBIT\_EVENT\_NO\_UPDATE | Event triggered when there is no update available. |
| HAWKBIT\_EVENT\_CANCEL\_UPDATE | Event triggered when the update was canceled by the server. |
| HAWKBIT\_EVENT\_START\_DOWNLOAD | Event triggered before the download starts. |
| HAWKBIT\_EVENT\_END\_DOWNLOAD | Event triggered after the download ends. |
| HAWKBIT\_EVENT\_START\_RUN | Event triggered before the hawkBit run starts. |
| HAWKBIT\_EVENT\_END\_RUN | Event triggered after the hawkBit run ends. |
| HAWKBIT\_EVENT\_BEFORE\_REBOOT | Event triggered before hawkBit does a reboot. |

## Function Documentation

## [◆ ](#ga646c72464b0761009f42393fa313c880)hawkbit\_event\_add\_callback()

| int hawkbit\_event\_add\_callback | ( | struct hawkbit\_event\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[event.h](event_8h.md)>`

Add an application callback.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

## [◆ ](#ga0ec141ff3e11c0e1d0e3f8757ace5010)hawkbit\_event\_init\_callback()

| | void hawkbit\_event\_init\_callback | ( | struct hawkbit\_event\_callback \* | *callback*, | | --- | --- | --- | --- | |  |  | [hawkbit\_event\_callback\_handler\_t](#ga49064aef93c5383f24ea41819b78c458) | *handler*, | |  |  | enum [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) | *event* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[event.h](event_8h.md)>`

Helper to initialize a struct hawkbit\_event\_callback properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | event | The event of [hawkbit\_event\_type](#ga794d232d73d105bd170b222ab17ce2af) that will trigger the callback. |

## [◆ ](#gaa19bb74cb46e9aff7742907a86c96359)hawkbit\_event\_remove\_callback()

| int hawkbit\_event\_remove\_callback | ( | struct hawkbit\_event\_callback \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[event.h](event_8h.md)>`

Remove an application callback.

Parameters
:   | cb | A valid application's callback structure pointer. |
    | --- | --- |

Returns
:   0 if successful, negative errno code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
