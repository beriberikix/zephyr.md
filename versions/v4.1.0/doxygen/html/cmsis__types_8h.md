---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cmsis__types_8h.html
original_path: doxygen/html/cmsis__types_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsis\_types.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <zephyr/portability/cmsis_os2.h>`

[Go to the source code of this file.](cmsis__types_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cmsis\_rtos\_thread\_cb](structcmsis__rtos__thread__cb.md) |
|  | Control block for a CMSIS-RTOSv2 thread. [More...](structcmsis__rtos__thread__cb.md#details) |
| struct | [cmsis\_rtos\_timer\_cb](structcmsis__rtos__timer__cb.md) |
|  | Control block for a CMSIS-RTOSv2 timer. [More...](structcmsis__rtos__timer__cb.md#details) |
| struct | [cmsis\_rtos\_mutex\_cb](structcmsis__rtos__mutex__cb.md) |
|  | Control block for a CMSIS-RTOSv2 mutex. [More...](structcmsis__rtos__mutex__cb.md#details) |
| struct | [cmsis\_rtos\_semaphore\_cb](structcmsis__rtos__semaphore__cb.md) |
|  | Control block for a CMSIS-RTOSv2 semaphore. [More...](structcmsis__rtos__semaphore__cb.md#details) |
| struct | [cmsis\_rtos\_mempool\_cb](structcmsis__rtos__mempool__cb.md) |
|  | Control block for a CMSIS-RTOSv2 memory pool. [More...](structcmsis__rtos__mempool__cb.md#details) |
| struct | [cmsis\_rtos\_msgq\_cb](structcmsis__rtos__msgq__cb.md) |
|  | Control block for a CMSIS-RTOSv2 message queue. [More...](structcmsis__rtos__msgq__cb.md#details) |
| struct | [cmsis\_rtos\_event\_cb](structcmsis__rtos__event__cb.md) |
|  | Control block for a CMSIS-RTOSv2 event flag. [More...](structcmsis__rtos__event__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [CMSIS\_OBJ\_NAME\_MAX\_LEN](#a3df1d8e10c95ee9d6ac04e757327e051)   16 |
|  | Size for names of RTOS objects. |

## Macro Definition Documentation

## [◆ ](#a3df1d8e10c95ee9d6ac04e757327e051)CMSIS\_OBJ\_NAME\_MAX\_LEN

| #define CMSIS\_OBJ\_NAME\_MAX\_LEN   16 |
| --- |

Size for names of RTOS objects.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [portability](dir_01227ef4652825ef85eafb29606f54aa.md)
- [cmsis\_types.h](cmsis__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
