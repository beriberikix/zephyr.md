---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensing__sensor_8h.html
original_path: doxygen/html/sensing__sensor_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`  
`#include <[zephyr/sensing/sensing.h](sensing_8h_source.md)>`

[Go to the source code of this file.](sensing__sensor_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sensing\_sensor\_register\_info](structsensing__sensor__register__info.md) |
|  | Sensor registration information. [More...](structsensing__sensor__register__info.md#details) |

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSORS\_DT\_DEFINE](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654)(node, reg\_ptr, cb\_list\_ptr, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics. |
| #define | [SENSING\_SENSORS\_DT\_INST\_DEFINE](group__sensing__sensor.md#gae3c7a2acba53cc524a4b1043df49fe85)(inst, ...) |
|  | Like [SENSING\_SENSORS\_DT\_DEFINE()](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654 "Like SENSOR_DEVICE_DT_DEFINE() with sensing specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |

| Functions | |
| --- | --- |
| int | [sensing\_sensor\_get\_reporters](group__sensing__sensor.md#gab4c41d02b3731e5829a41e1f5f5154a5) (const struct [device](structdevice.md) \*dev, int type, [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*reporter\_handles, int max\_handles) |
|  | Get reporter handles of a given sensor instance by sensor type. |
| int | [sensing\_sensor\_get\_reporters\_count](group__sensing__sensor.md#ga2c5cfb298b2dfde967edfdd987115021) (const struct [device](structdevice.md) \*dev, int type) |
|  | Get reporters count of a given sensor instance by sensor type. |
| int | [sensing\_sensor\_get\_state](group__sensing__sensor.md#gab9446a3085b6b05da448dce59db50387) (const struct [device](structdevice.md) \*dev, enum [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get this sensor's state. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing\_sensor.h](sensing__sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
