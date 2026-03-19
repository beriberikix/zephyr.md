---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__ctrl_8h.html
original_path: doxygen/html/log__ctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_ctrl.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/logging/log_backend.h](log__backend_8h_source.md)>`  
`#include <[zephyr/logging/log_msg.h](log__msg_8h_source.md)>`  
`#include <[zephyr/logging/log_internal.h](log__internal_8h_source.md)>`  
`#include <zephyr/syscalls/log_ctrl.h>`

[Go to the source code of this file.](log__ctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOG\_CORE\_INIT](group__log__ctrl.md#gabb1d00fe08bc48ed4d352ce61b0e0582)() |
| #define | [LOG\_INIT](group__log__ctrl.md#ga062ce2496c8e47adec91c0d11744a7a7)() |
| #define | [LOG\_PANIC](group__log__ctrl.md#ga9ee5a99e0487e3f1e6d289b12c19ad5a)() |
| #define | [LOG\_PROCESS](group__log__ctrl.md#gacd14d69929496cea19c699509eb5ea1b)() |

| Typedefs | |
| --- | --- |
| typedef [log\_timestamp\_t](log__msg_8h.md#acbc134e9ee5f3768a534d95a4c8335e8)(\* | [log\_timestamp\_get\_t](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb)) (void) |

| Functions | |
| --- | --- |
| void | [log\_core\_init](group__log__ctrl.md#ga338338de3c3e3ce6d3ea7ca6a6fa83e0) (void) |
|  | Function system initialization of the logger. |
| void | [log\_init](group__log__ctrl.md#ga2508fad025e49f9746b6c178dce6917e) (void) |
|  | Function for user initialization of the logger. |
| void | [log\_thread\_trigger](group__log__ctrl.md#ga173eff0a07bbd1fc2978a1a705cae1fb) (void) |
|  | Trigger the log processing thread to process logs immediately. |
| void | [log\_thread\_set](group__log__ctrl.md#ga5f58516c3c155dde0f44ea9cc7cd8b37) ([k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) process\_tid) |
|  | Function for providing thread which is processing logs. |
| int | [log\_set\_timestamp\_func](group__log__ctrl.md#gaea92150610f900ab1258cbce65662ae6) ([log\_timestamp\_get\_t](group__log__ctrl.md#gae7aaa810aabda4aed6226a85f28d6fbb) timestamp\_getter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq) |
|  | Function for providing timestamp function. |
| void | [log\_panic](group__log__ctrl.md#ga6a4d408fc9d7c55366cd7a02850b03f5) (void) |
|  | Switch the logger subsystem to the panic mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_process](group__log__ctrl.md#ga7276787473a372eac8b77c012ae7226a) (void) |
|  | Process one pending log message. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_buffered\_cnt](group__log__ctrl.md#gab6785b1f77080bbaf9f5ac3bfe0fd23c) (void) |
|  | Return number of buffered log messages. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_src\_cnt\_get](group__log__ctrl.md#ga10b12f5c462f3d0f1cb8d60ead802c9a) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get number of independent logger sources (modules and instances). |
| const char \* | [log\_source\_name\_get](group__log__ctrl.md#ga7047a91d157b329362cff22784472c83) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) source\_id) |
|  | Get name of the source (module or instance). |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [log\_domains\_count](group__log__ctrl.md#ga3fdf07aecb4f559f5119f16c137daf3d) (void) |
|  | Return number of domains present in the system. |
| const char \* | [log\_domain\_name\_get](group__log__ctrl.md#gac20a57745d0a10e6cf100eb47eb9561d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id) |
|  | Get name of the domain. |
| int | [log\_source\_id\_get](group__log__ctrl.md#ga0ae80c298349cc784b890809919ad629) (const char \*name) |
|  | Function for finding source ID based on source name. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_filter\_get](group__log__ctrl.md#ga83b8fe6d2592f02fe8a73faed819c3ce) (struct [log\_backend](structlog__backend.md) const \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) runtime) |
|  | Get source filter for the provided backend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_filter\_set](group__log__ctrl.md#ga32956e4ba4ed92e5e5aeb5503be0047e) (struct [log\_backend](structlog__backend.md) const \*const backend, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Set filter on given source for the provided backend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_frontend\_filter\_get](group__log__ctrl.md#ga826f2176d0ece92617725960db697849) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) runtime) |
|  | Get source filter for the frontend. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_frontend\_filter\_set](group__log__ctrl.md#ga305700387e40548dee873ef197228f9b) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) source\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Set filter on given source for the frontend. |
| void | [log\_backend\_enable](group__log__ctrl.md#gadbd0b5dd8c459c6ef85f9fef4f2bdebf) (struct [log\_backend](structlog__backend.md) const \*const backend, void \*ctx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) level) |
|  | Enable backend with initial maximum filtering level. |
| void | [log\_backend\_disable](group__log__ctrl.md#gaf5d428f18b00138fd2ccca190981191d) (struct [log\_backend](structlog__backend.md) const \*const backend) |
|  | Disable backend. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_backend\_get\_by\_name](group__log__ctrl.md#ga8c374e83492b221eeaf2c2b0f38e3b42) (const char \*backend\_name) |
|  | Get backend by name. |
| const struct [log\_backend](structlog__backend.md) \* | [log\_format\_set\_all\_active\_backends](group__log__ctrl.md#gaeaaaa2e68877837a4af20fa172fc2f06) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) log\_type) |
|  | Sets logging format for all active backends. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_data\_pending](group__log__ctrl.md#ga6d6c48ddd4b6739e34fde2098ad61731) (void) |
|  | Check if there is pending data to be processed by the logging subsystem. |
| int | [log\_set\_tag](group__log__ctrl.md#ga58499087f61cc377615311498eedf1ae) (const char \*tag) |
|  | Configure tag used to prefix each message. |
| int | [log\_mem\_get\_usage](group__log__ctrl.md#ga5f3487ab08e421ae7ce8a8b80310a338) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*buf\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*usage) |
|  | Get current memory usage. |
| int | [log\_mem\_get\_max\_usage](group__log__ctrl.md#ga2d3f29bf2783e70242c8608a20a934ee) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*max) |
|  | Get maximum memory usage. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_ctrl.h](log__ctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
