---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/modem_2backend_2tty_8h.html
original_path: doxygen/html/modem_2backend_2tty_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tty.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/ring_buffer.h](ring__buffer_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/modem/pipe.h](pipe_8h_source.md)>`

[Go to the source code of this file.](modem_2backend_2tty_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [modem\_backend\_tty](structmodem__backend__tty.md) |
| struct | [modem\_backend\_tty\_config](structmodem__backend__tty__config.md) |

| Macros | |
| --- | --- |
| #define | [ZEPHYR\_MODEM\_BACKEND\_TTY\_](#a69a30337ca00de462fc67e47401334f4) |

| Functions | |
| --- | --- |
| struct modem\_pipe \* | [modem\_backend\_tty\_init](#a507f79d94144e3e4a75ec7fed1501f80) (struct [modem\_backend\_tty](structmodem__backend__tty.md) \*backend, const struct [modem\_backend\_tty\_config](structmodem__backend__tty__config.md) \*config) |

## Macro Definition Documentation

## [◆ ](#a69a30337ca00de462fc67e47401334f4)ZEPHYR\_MODEM\_BACKEND\_TTY\_

| #define ZEPHYR\_MODEM\_BACKEND\_TTY\_ |
| --- |

## Function Documentation

## [◆ ](#a507f79d94144e3e4a75ec7fed1501f80)modem\_backend\_tty\_init()

| struct modem\_pipe \* modem\_backend\_tty\_init | ( | struct [modem\_backend\_tty](structmodem__backend__tty.md) \* | *backend*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_backend\_tty\_config](structmodem__backend__tty__config.md) \* | *config* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [backend](dir_ff046e227e385bf86f987d0152997f69.md)
- [tty.h](modem_2backend_2tty_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
