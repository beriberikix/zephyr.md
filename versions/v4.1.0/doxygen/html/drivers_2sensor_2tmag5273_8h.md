---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2sensor_2tmag5273_8h.html
original_path: doxygen/html/drivers_2sensor_2tmag5273_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmag5273.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](drivers_2sensor_2tmag5273_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TMAG5273\_ANGLE\_CALC\_NONE](#a6426061b7a7f444ba7f4d87477144bf0)   0 |
|  | Supported values. |
| #define | [TMAG5273\_ANGLE\_CALC\_XY](#ac93519e03635876d3b693a0b4a11904a)   1 |
| #define | [TMAG5273\_ANGLE\_CALC\_YZ](#a863266f03d298268103d394eb37bbac9)   2 |
| #define | [TMAG5273\_ANGLE\_CALC\_XZ](#a84e780517b8fec1845fd145dd0b16f0c)   3 |

| Enumerations | |
| --- | --- |
| enum | [tmag5273\_sensor\_channel](#a3d91dbb6bc6d7dc90ed889651bc34827) { [TMAG5273\_CHAN\_MAGNITUDE](#a3d91dbb6bc6d7dc90ed889651bc34827a72c52112337e191ab9ce906aecdff92d) = SENSOR\_CHAN\_PRIV\_START , [TMAG5273\_CHAN\_MAGNITUDE\_MSB](#a3d91dbb6bc6d7dc90ed889651bc34827a601dad57092c442da3a0a184737d8003) , [TMAG5273\_CHAN\_ANGLE\_MAGNITUDE](#a3d91dbb6bc6d7dc90ed889651bc34827a2c4ff267102871c1d23353bbb6b30dbc) } |
|  | Additional channels supported by the TMAG5273. [More...](#a3d91dbb6bc6d7dc90ed889651bc34827) |
| enum | [tmag5273\_attribute](#a6fadcd6cd3b5fbc9281d27f37bdfe0a2) { [TMAG5273\_ATTR\_ANGLE\_MAG\_AXIS](#a6fadcd6cd3b5fbc9281d27f37bdfe0a2af59c66f9794efa1afa7d7461a134d3d3) = SENSOR\_ATTR\_PRIV\_START } |
|  | Additional attributes supported by the TMAG5273. [More...](#a6fadcd6cd3b5fbc9281d27f37bdfe0a2) |

## Macro Definition Documentation

## [◆ ](#a6426061b7a7f444ba7f4d87477144bf0)TMAG5273\_ANGLE\_CALC\_NONE

| #define TMAG5273\_ANGLE\_CALC\_NONE   0 |
| --- |

Supported values.

## [◆ ](#ac93519e03635876d3b693a0b4a11904a)TMAG5273\_ANGLE\_CALC\_XY

| #define TMAG5273\_ANGLE\_CALC\_XY   1 |
| --- |

## [◆ ](#a84e780517b8fec1845fd145dd0b16f0c)TMAG5273\_ANGLE\_CALC\_XZ

| #define TMAG5273\_ANGLE\_CALC\_XZ   3 |
| --- |

## [◆ ](#a863266f03d298268103d394eb37bbac9)TMAG5273\_ANGLE\_CALC\_YZ

| #define TMAG5273\_ANGLE\_CALC\_YZ   2 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a6fadcd6cd3b5fbc9281d27f37bdfe0a2)tmag5273\_attribute

| enum [tmag5273\_attribute](#a6fadcd6cd3b5fbc9281d27f37bdfe0a2) |
| --- |

Additional attributes supported by the TMAG5273.

| Enumerator | |
| --- | --- |
| TMAG5273\_ATTR\_ANGLE\_MAG\_AXIS | Define axis relation measurements.  Supported values are:   - `TMAG5273_DT_ANGLE_MAG_NONE` (0) - `TMAG5273_DT_ANGLE_MAG_XY` (1) - `TMAG5273_DT_ANGLE_MAG_YZ` (2) - `TMAG5273_DT_ANGLE_MAG_XZ` (3)   Only available if calculation source can be changed during runtime. |

## [◆ ](#a3d91dbb6bc6d7dc90ed889651bc34827)tmag5273\_sensor\_channel

| enum [tmag5273\_sensor\_channel](#a3d91dbb6bc6d7dc90ed889651bc34827) |
| --- |

Additional channels supported by the TMAG5273.

| Enumerator | |
| --- | --- |
| TMAG5273\_CHAN\_MAGNITUDE | Magnitude measurement result between two axis in Gs. |
| TMAG5273\_CHAN\_MAGNITUDE\_MSB | Magnitude measurement MSB as returned by the sensor. |
| TMAG5273\_CHAN\_ANGLE\_MAGNITUDE | Angle result in deg, magnitude result in Gs and magnitude MSB between two axis. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmag5273.h](drivers_2sensor_2tmag5273_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
