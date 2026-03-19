---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm__clock__control_8h.html
original_path: doxygen/html/arm__clock__control_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_clock\_control.h File Reference

Clock subsystem IDs for ARM family SoCs.
[More...](#details)

`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](arm__clock__control_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_clock\_control\_t](structarm__clock__control__t.md) |

| Enumerations | |
| --- | --- |
| enum | [arm\_bus\_type\_t](#af000c4220627db6eee0117062c6c50ef) { [CMSDK\_AHB](#af000c4220627db6eee0117062c6c50efa945c5ee4f308f798cc7d14c3471e0393) = 0 , [CMSDK\_APB](#af000c4220627db6eee0117062c6c50efa58c832e59253102458c445fc49e02d80) } |
| enum | [arm\_soc\_state\_t](#a0a2c04415a74486aa29a4d1d0d7679e1) { [SOC\_ACTIVE](#a0a2c04415a74486aa29a4d1d0d7679e1a440a3f8e72f1edcabd1c0acfb6fbebbf) = 0 , [SOC\_SLEEP](#a0a2c04415a74486aa29a4d1d0d7679e1a3ac4c2f680ed21227a058286db3ea094) , [SOC\_DEEPSLEEP](#a0a2c04415a74486aa29a4d1d0d7679e1afdb90f70cdbc1b44b88a934bafae2c98) } |

## Detailed Description

Clock subsystem IDs for ARM family SoCs.

## Enumeration Type Documentation

## [◆ ](#af000c4220627db6eee0117062c6c50ef)arm\_bus\_type\_t

| enum [arm\_bus\_type\_t](#af000c4220627db6eee0117062c6c50ef) |
| --- |

| Enumerator | |
| --- | --- |
| CMSDK\_AHB |  |
| CMSDK\_APB |  |

## [◆ ](#a0a2c04415a74486aa29a4d1d0d7679e1)arm\_soc\_state\_t

| enum [arm\_soc\_state\_t](#a0a2c04415a74486aa29a4d1d0d7679e1) |
| --- |

| Enumerator | |
| --- | --- |
| SOC\_ACTIVE |  |
| SOC\_SLEEP |  |
| SOC\_DEEPSLEEP |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [arm\_clock\_control.h](arm__clock__control_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
