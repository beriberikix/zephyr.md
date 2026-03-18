---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/modem_2stats_8h.html
original_path: doxygen/html/modem_2stats_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stats.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](modem_2stats_8h_source.md)

| Functions | |
| --- | --- |
| void | [modem\_stats\_buffer\_init](#ac97a44071b31768bd2d39bef27bfd746) (struct modem\_stats\_buffer \*buffer, const char \*name, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size) |
|  | Initialize modem statistics buffer. |
| void | [modem\_stats\_buffer\_advertise\_length](#af4ccdf8a97586021431d858565a8f28f) (struct modem\_stats\_buffer \*buffer, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) length) |
|  | Advertise modem statistics buffer size. |

## Function Documentation

## [◆ ](#af4ccdf8a97586021431d858565a8f28f)modem\_stats\_buffer\_advertise\_length()

| void modem\_stats\_buffer\_advertise\_length | ( | struct modem\_stats\_buffer \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *length* ) |

Advertise modem statistics buffer size.

Parameters
:   | buffer | Modem statistics buffer instance |
    | --- | --- |
    | length | Length of buffer |

Note
:   Invoke when buffer size changes
:   Safe to invoke from ISR

## [◆ ](#ac97a44071b31768bd2d39bef27bfd746)modem\_stats\_buffer\_init()

| void modem\_stats\_buffer\_init | ( | struct modem\_stats\_buffer \* | *buffer*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *size* ) |

Initialize modem statistics buffer.

Parameters
:   | buffer | Modem statistics buffer instance |
    | --- | --- |
    | name | Name of buffer instance |
    | size | Size of buffer |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [stats.h](modem_2stats_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
