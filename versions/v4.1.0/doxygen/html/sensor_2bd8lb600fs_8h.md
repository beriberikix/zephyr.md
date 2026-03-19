---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_2bd8lb600fs_8h.html
original_path: doxygen/html/sensor_2bd8lb600fs_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bd8lb600fs.h File Reference

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](sensor_2bd8lb600fs_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_bd8lb600fs](#aaeae18fce2525ea91a9e02566ab455ea) { [SENSOR\_CHAN\_BD8LB600FS\_OPEN\_LOAD](#aaeae18fce2525ea91a9e02566ab455eaa13ecf27f56653ee4e9d2b7a115a68587) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_CHAN\_BD8LB600FS\_OVER\_CURRENT\_OR\_THERMAL\_SHUTDOWN](#aaeae18fce2525ea91a9e02566ab455eaad9d0c933554c3ca6667508ea32fda3de) } |

## Enumeration Type Documentation

## [◆ ](#aaeae18fce2525ea91a9e02566ab455ea)sensor\_channel\_bd8lb600fs

| enum [sensor\_channel\_bd8lb600fs](#aaeae18fce2525ea91a9e02566ab455ea) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_BD8LB600FS\_OPEN\_LOAD | Open load detected, boolean with one bit per output. |
| SENSOR\_CHAN\_BD8LB600FS\_OVER\_CURRENT\_OR\_THERMAL\_SHUTDOWN | Over current protection or thermal shutdown, boolean with one bit per output. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [bd8lb600fs.h](sensor_2bd8lb600fs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
