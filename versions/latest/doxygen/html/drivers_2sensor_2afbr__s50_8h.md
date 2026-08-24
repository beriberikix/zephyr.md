---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2afbr__s50_8h.html
original_path: doxygen/html/drivers_2sensor_2afbr__s50_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

afbr\_s50.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](drivers_2sensor_2afbr__s50_8h_source.md)

| Macros | |
| --- | --- |
| #define | [AFBR\_PIXEL\_INVALID\_VALUE](#a026e02d538d6e283b7b1136470e6e478)   0x80000000 |
|  | Disregard pixel reading if contains this value. |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_afbr\_s50](#a2be1db0094a49e8e59310b8c8137e54f) { [SENSOR\_CHAN\_AFBR\_S50\_PIXELS](#a2be1db0094a49e8e59310b8c8137e54fa46394738feb65f3bcc76ecd343448de7) = SENSOR\_CHAN\_PRIV\_START + 1 } |
|  | Private sensor channel to obtain matrix of pixels with readings in meters. [More...](#a2be1db0094a49e8e59310b8c8137e54f) |

## Macro Definition Documentation

## [◆ ](#a026e02d538d6e283b7b1136470e6e478)AFBR\_PIXEL\_INVALID\_VALUE

| #define AFBR\_PIXEL\_INVALID\_VALUE   0x80000000 |
| --- |

Disregard pixel reading if contains this value.

## Enumeration Type Documentation

## [◆ ](#a2be1db0094a49e8e59310b8c8137e54f)sensor\_channel\_afbr\_s50

| enum [sensor\_channel\_afbr\_s50](#a2be1db0094a49e8e59310b8c8137e54f) |
| --- |

Private sensor channel to obtain matrix of pixels with readings in meters.

This sensor supports up to 32 pixels in a single reading (4 x 8 matrix).

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_AFBR\_S50\_PIXELS |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [afbr\_s50.h](drivers_2sensor_2afbr__s50_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
