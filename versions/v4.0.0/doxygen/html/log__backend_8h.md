---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__backend_8h.html
original_path: doxygen/html/log__backend_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend.h File Reference

`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <stdarg.h>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/logging/log_output.h](log__output_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](log__backend_8h_source.md)

| Data Structures | |
| --- | --- |
| union | [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) |
|  | Argument(s) for backend events. [More...](unionlog__backend__evt__arg.md#details) |
| struct | [log\_backend\_api](structlog__backend__api.md) |
|  | Logger backend API. [More...](structlog__backend__api.md#details) |
| struct | [log\_backend\_control\_block](structlog__backend__control__block.md) |
|  | Logger backend control block. [More...](structlog__backend__control__block.md#details) |
| struct | [log\_backend](structlog__backend.md) |
|  | Logger backend structure. [More...](structlog__backend.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_BACKEND\_DEFINE](group__log__backend.md#ga3a4cc530530d1a8b33dc787842bba119)(\_name, \_api, \_autostart, ...) |
|  | Macro for creating a logger backend instance. |

| Enumerations | |
| --- | --- |
| enum | [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) { [LOG\_BACKEND\_EVT\_PROCESS\_THREAD\_DONE](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6a559c37c58daf13a14f7b43440556f3d3) , [LOG\_BACKEND\_EVT\_MAX](group__log__backend.md#gga04ebbd4416c907e60e05f0364f3bd2f6abbc925931ad8098f3cee651fadd5432a) } |
|  | Backend events. [More...](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) |

| Functions | |
| --- | --- |
| static void | [log\_backend\_init](group__log__backend.md#ga017a2b54d367db037cce31b2693af98c) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Initialize or initiate the logging backend. |
| static int | [log\_backend\_is\_ready](group__log__backend.md#gaf57e7a27a1337815338410db93603e0b) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Poll for backend readiness. |
| static void | [log\_backend\_msg\_process](group__log__backend.md#ga388b0f33208ef1389640836d0bc23d17) (const struct [log\_backend](structlog__backend.md) \*const backend, union [log\_msg\_generic](unionlog__msg__generic.md) \*msg) |
|  | Process message. |
| static void | [log\_backend\_dropped](group__log__backend.md#gab300348c43168de1e7eaae8c770b6950) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cnt) |
|  | Notify backend about dropped log messages. |
| static void | [log\_backend\_panic](group__log__backend.md#gad12906ffa810514c1d43cb26bba5ea4b) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Reconfigure backend to panic mode. |
| static void | [log\_backend\_id\_set](group__log__backend.md#ga8f263b24140229e5cf8e98b322501bca) (const struct [log\_backend](structlog__backend.md) \*const backend, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id) |
|  | Set backend id. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_backend\_id\_get](group__log__backend.md#gae3e1d6eaf21dcc1d0961e85271d5e5f3) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Get backend id. |
| static const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_get](group__log__backend.md#gaf419f3590f42893b7091beed57763c7c) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx) |
|  | Get backend. |
| static int | [log\_backend\_count\_get](group__log__backend.md#gad055c1dc8e0236b604cb553df3e16a52) (void) |
|  | Get number of backends. |
| static void | [log\_backend\_activate](group__log__backend.md#ga3ef0b88b4118f7ee04749ace2646c99b) (const struct [log\_backend](structlog__backend.md) \*const backend, void \*ctx) |
|  | Activate backend. |
| static void | [log\_backend\_deactivate](group__log__backend.md#ga1534fdfabce1e97c829aa79d57739589) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Deactivate backend. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_backend\_is\_active](group__log__backend.md#ga54dd06d48edf92ef191dab946aead216) (const struct [log\_backend](structlog__backend.md) \*const backend) |
|  | Check state of the backend. |
| static int | [log\_backend\_format\_set](group__log__backend.md#gac0a4dc476c3b641ab570ca2dd4f2096f) (const struct [log\_backend](structlog__backend.md) \*backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_type) |
|  | Set logging format. |
| static void | [log\_backend\_notify](group__log__backend.md#gae8203fcde52fee405a4b2e973c989ec7) (const struct [log\_backend](structlog__backend.md) \*const backend, enum [log\_backend\_evt](group__log__backend.md#ga04ebbd4416c907e60e05f0364f3bd2f6) event, union [log\_backend\_evt\_arg](unionlog__backend__evt__arg.md) \*arg) |
|  | Notify a backend of an event. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend.h](log__backend_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
