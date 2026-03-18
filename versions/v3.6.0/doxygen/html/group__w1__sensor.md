---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__w1__sensor.html
original_path: doxygen/html/group__w1__sensor.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

1-Wire Sensor API

[Device Driver APIs](group__io__interfaces.md) » [1-Wire Interface](group__w1__interface.md)

1-Wire Sensor API
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_w1](#gae6c6848f94bde562a95f5f987a8c76fc) { [SENSOR\_ATTR\_W1\_ROM](#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36) = SENSOR\_ATTR\_PRIV\_START } |

| Functions | |
| --- | --- |
| static void | [w1\_rom\_to\_sensor\_value](#ga947aea2687107b1b3471c3e9eded7504) (const struct [w1\_rom](structw1__rom.md) \*rom, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Function to write a [w1\_rom](structw1__rom.md "w1_rom struct.") struct to an sensor value ptr. |
| static void | [w1\_sensor\_value\_to\_rom](#ga3c0b20580be768bcc45f93a4c01ee9db) (const struct [sensor\_value](structsensor__value.md) \*val, struct [w1\_rom](structw1__rom.md) \*rom) |
|  | Function to write an rom id stored in a sensor value to a struct [w1\_rom](structw1__rom.md "w1_rom struct.") ptr. |

## Detailed Description

1-Wire Sensor API

## Enumeration Type Documentation

## [◆ ](#gae6c6848f94bde562a95f5f987a8c76fc)sensor\_attribute\_w1

| enum [sensor\_attribute\_w1](#gae6c6848f94bde562a95f5f987a8c76fc) |
| --- |

`#include <[w1_sensor.h](w1__sensor_8h.md)>`

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_W1\_ROM | Device unique 1-Wire ROM. |

## Function Documentation

## [◆ ](#ga947aea2687107b1b3471c3e9eded7504)w1\_rom\_to\_sensor\_value()

| | void w1\_rom\_to\_sensor\_value | ( | const struct [w1\_rom](structw1__rom.md) \* | *rom*, | | --- | --- | --- | --- | |  |  | struct [sensor\_value](structsensor__value.md) \* | *val* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1_sensor.h](w1__sensor_8h.md)>`

Function to write a [w1\_rom](structw1__rom.md "w1_rom struct.") struct to an sensor value ptr.

Parameters
:   | rom | Pointer to the rom struct. |
    | --- | --- |
    | val | Pointer to the sensor value. |

## [◆ ](#ga3c0b20580be768bcc45f93a4c01ee9db)w1\_sensor\_value\_to\_rom()

| | void w1\_sensor\_value\_to\_rom | ( | const struct [sensor\_value](structsensor__value.md) \* | *val*, | | --- | --- | --- | --- | |  |  | struct [w1\_rom](structw1__rom.md) \* | *rom* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[w1_sensor.h](w1__sensor_8h.md)>`

Function to write an rom id stored in a sensor value to a struct [w1\_rom](structw1__rom.md "w1_rom struct.") ptr.

Parameters
:   | val | Sensor\_value representing the rom. |
    | --- | --- |
    | rom | The rom struct ptr. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
