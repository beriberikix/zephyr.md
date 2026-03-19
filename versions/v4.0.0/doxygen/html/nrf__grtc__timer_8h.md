---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nrf__grtc__timer_8h.html
original_path: doxygen/html/nrf__grtc__timer_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_grtc\_timer.h File Reference

`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`

[Go to the source code of this file.](nrf__grtc__timer_8h_source.md)

| Functions | |
| --- | --- |
| int | [nrf\_grtc\_timer\_clock\_driver\_init](#a104efab2f0186b68694a14b118c6fd8e) (void) |
|  | Initialize the GRTC clock timer driver from an application- defined function. |

## Function Documentation

## [◆ ](#a104efab2f0186b68694a14b118c6fd8e)nrf\_grtc\_timer\_clock\_driver\_init()

| int nrf\_grtc\_timer\_clock\_driver\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize the GRTC clock timer driver from an application- defined function.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -errno | Negative error code on failure. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [nrf\_grtc\_timer.h](nrf__grtc__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
