---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/w1__sensor_8h.html
original_path: doxygen/html/w1__sensor_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

w1\_sensor.h File Reference

Extended public API for 1-Wire Sensors.
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`  
`#include <[zephyr/drivers/w1.h](w1_8h_source.md)>`

[Go to the source code of this file.](w1__sensor_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_w1](group__w1__sensor.md#gae6c6848f94bde562a95f5f987a8c76fc) { [SENSOR\_ATTR\_W1\_ROM](group__w1__sensor.md#ggae6c6848f94bde562a95f5f987a8c76fcaa5456effd0254882ece02da5d25cec36) = SENSOR\_ATTR\_PRIV\_START } |

| Functions | |
| --- | --- |
| static void | [w1\_rom\_to\_sensor\_value](group__w1__sensor.md#ga947aea2687107b1b3471c3e9eded7504) (const struct [w1\_rom](structw1__rom.md) \*rom, struct [sensor\_value](structsensor__value.md) \*val) |
|  | Function to write a [w1\_rom](structw1__rom.md "w1_rom struct.") struct to an sensor value ptr. |
| static void | [w1\_sensor\_value\_to\_rom](group__w1__sensor.md#ga3c0b20580be768bcc45f93a4c01ee9db) (const struct [sensor\_value](structsensor__value.md) \*val, struct [w1\_rom](structw1__rom.md) \*rom) |
|  | Function to write an rom id stored in a sensor value to a struct [w1\_rom](structw1__rom.md "w1_rom struct.") ptr. |

## Detailed Description

Extended public API for 1-Wire Sensors.

This header file exposes an attribute an helper function to allow the runtime configuration of ROM IDs for 1-Wire Sensors.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [w1\_sensor.h](w1__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
