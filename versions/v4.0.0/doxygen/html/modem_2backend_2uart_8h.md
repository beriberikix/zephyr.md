---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/modem_2backend_2uart_8h.html
original_path: doxygen/html/modem_2backend_2uart_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/uart.h](drivers_2uart_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`  
`#include <[zephyr/modem/stats.h](modem_2stats_8h_source.md)>`

[Go to the source code of this file.](modem_2backend_2uart_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [modem\_backend\_uart\_isr](structmodem__backend__uart__isr.md) |
| struct | [modem\_backend\_uart\_async](structmodem__backend__uart__async.md) |
| struct | [modem\_backend\_uart](structmodem__backend__uart.md) |
| struct | [modem\_backend\_uart\_config](structmodem__backend__uart__config.md) |

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_MODEM\_BACKEND\_UART\_](#a5155dc70533cab6952423061f00513c3) |

| Functions | |
| --- | --- |
| struct modem\_pipe \* | [modem\_backend\_uart\_init](#a7f7550ddcf3a7ea1493c788b635862ba) (struct [modem\_backend\_uart](structmodem__backend__uart.md) \*backend, const struct [modem\_backend\_uart\_config](structmodem__backend__uart__config.md) \*config) |

## Macro Definition Documentation

## [◆ ](#a5155dc70533cab6952423061f00513c3)ZEPHYR\_MODEM\_BACKEND\_UART\_

| #define ZEPHYR\_MODEM\_BACKEND\_UART\_ |
| --- |

## Function Documentation

## [◆ ](#a7f7550ddcf3a7ea1493c788b635862ba)modem\_backend\_uart\_init()

| struct modem\_pipe \* modem\_backend\_uart\_init | ( | struct [modem\_backend\_uart](structmodem__backend__uart.md) \* | *backend*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_backend\_uart\_config](structmodem__backend__uart__config.md) \* | *config* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [backend](dir_ff046e227e385bf86f987d0152997f69.md)
- [uart.h](modem_2backend_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
