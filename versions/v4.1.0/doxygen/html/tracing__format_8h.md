---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tracing__format_8h.html
original_path: doxygen/html/tracing__format_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing\_format.h File Reference

`#include <[zephyr/toolchain/common.h](include_2zephyr_2toolchain_2common_8h_source.md)>`

[Go to the source code of this file.](tracing__format_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tracing\_data](structtracing__data.md) |
|  | A structure to represent tracing data format. [More...](structtracing__data.md#details) |

| Macros | |
| --- | --- |
| #define | [TRACING\_STRING](group__subsys__tracing__format__apis.md#gac6aa3236d7aeb8c4a3f0c421899f74e6)(fmt, ...) |
|  | Macro to trace a message in string format. |
| #define | [TRACING\_FORMAT\_DATA](group__subsys__tracing__format__apis.md#ga5cf7507b0040325a4c04600fcdeb3b21)(x) |
|  | Macro to format data to tracing data format. |
| #define | [TRACING\_DATA](group__subsys__tracing__format__apis.md#ga1b9265a15c577024edd687edc368ca82)(...) |
|  | Macro to trace a message in tracing data format. |

| Typedefs | |
| --- | --- |
| typedef struct [tracing\_data](structtracing__data.md) | [tracing\_data\_t](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24) |
|  | A structure to represent tracing data format. |

| Functions | |
| --- | --- |
| void | [tracing\_format\_string](group__subsys__tracing__format__apis.md#gaf372e7223a7be6f938cd6a0263815d44) (const char \*str,...) |
|  | Tracing a message in string format. |
| void | [tracing\_format\_raw\_data](group__subsys__tracing__format__apis.md#gadb864c39916bc50bad341964fead14f5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length) |
|  | Tracing a message in raw data format. |
| void | [tracing\_format\_data](group__subsys__tracing__format__apis.md#ga4072def87e770f60de40062617e96256) ([tracing\_data\_t](group__subsys__tracing__format__apis.md#ga1a947f2e998d283b58a5e056f7edbb24) \*tracing\_data\_array, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Tracing a message in tracing data format. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing\_format.h](tracing__format_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
