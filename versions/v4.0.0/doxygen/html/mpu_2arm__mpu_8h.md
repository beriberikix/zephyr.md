---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mpu_2arm__mpu_8h.html
original_path: doxygen/html/mpu_2arm__mpu_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu.h File Reference

[Go to the source code of this file.](mpu_2arm__mpu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mpu\_region](structarm__mpu__region.md) |
| struct | [arm\_mpu\_config](structarm__mpu__config.md) |

| Macros | |
| --- | --- |
| #define | [MPU\_REGION\_ENTRY](#ab0bd4273967fcfcc4c3929157d1775e1)(\_name, \_base, \_attr) |

| Variables | |
| --- | --- |
| const struct [arm\_mpu\_config](structarm__mpu__config.md) | [mpu\_config](#ab4f9746862097dfdc048d75c9c08b795) |

## Macro Definition Documentation

## [◆ ](#ab0bd4273967fcfcc4c3929157d1775e1)MPU\_REGION\_ENTRY

| #define MPU\_REGION\_ENTRY | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_base*, |
|  |  |  | *\_attr* ) |

**Value:**

{\

.name = \_name, \

.base = \_base, \

.attr = \_attr, \

}

## Variable Documentation

## [◆ ](#ab4f9746862097dfdc048d75c9c08b795)mpu\_config

| | const struct [arm\_mpu\_config](structarm__mpu__config.md) mpu\_config | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu.h](mpu_2arm__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
