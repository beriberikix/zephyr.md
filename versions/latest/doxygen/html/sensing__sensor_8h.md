---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sensing__sensor_8h.html
original_path: doxygen/html/sensing__sensor_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| struct | [sensing\_connection](structsensing__connection.md) |
|  | Connection between a source and sink of sensor data. [More...](structsensing__connection.md#details) |
| struct | [sensing\_sensor](structsensing__sensor.md) |
|  | Internal sensor instance data structure. [More...](structsensing__sensor.md#details) |
| struct | [sensing\_submit\_config](structsensing__submit__config.md) |

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSOR\_INFO\_NAME](group__sensing__sensor.md#ga4a11557e9d28c75e67f2d21af8dd24d7)(node, idx) |
| #define | [SENSING\_SENSOR\_INFO\_DEFINE](group__sensing__sensor.md#ga46b8830de0d42506c8804307c515c00b)(node, idx) |
| #define | [SENSING\_CONNECTIONS\_NAME](group__sensing__sensor.md#ga11f2d720e050f2212b67f2e11fa9677b)(node) |
| #define | [SENSING\_SENSOR\_SOURCE\_NAME](group__sensing__sensor.md#ga256546e178d1b2e507cb862876fec2d0)(idx, node) |
| #define | [SENSING\_SENSOR\_SOURCE\_EXTERN](group__sensing__sensor.md#ga3df3d46d0102ec114d9125dcb1474745)(idx, node) |
| #define | [SENSING\_CONNECTION\_INITIALIZER](group__sensing__sensor.md#ga11ddd317f3aef5edc0f80bad11738612)(source\_name, cb\_list\_ptr) |
| #define | [SENSING\_CONNECTION\_DEFINE](group__sensing__sensor.md#ga791ffbf312fa2eae23350cd9add0afc3)(idx, node, cb\_list\_ptr) |
| #define | [SENSING\_CONNECTIONS\_DEFINE](group__sensing__sensor.md#ga5c932e7be9361293a7b5ff3124e9799d)(node, num, cb\_list\_ptr) |
| #define | [SENSING\_SUBMIT\_CFG\_NAME](group__sensing__sensor.md#gaa0c5eb169a6e3922c091a4bf6ff82478)(node, idx) |
| #define | [SENSING\_SENSOR\_IODEV\_NAME](group__sensing__sensor.md#ga8c15780ceb1988ab7192c3c3ca70ac82)(node, idx) |
| #define | [SENSING\_SENSOR\_IODEV\_DEFINE](group__sensing__sensor.md#gafd8cbf368e9fa541ce67013d0e8624f2)(node, idx) |
| #define | [SENSING\_SENSOR\_NAME](group__sensing__sensor.md#ga4f8a39411260fbfd55258241de9bbb37)(node, idx) |
| #define | [SENSING\_SENSOR\_DEFINE](group__sensing__sensor.md#gae3588d8dce25ad800bf0633f1b3c6bf7)(node, prop, idx, reg\_ptr, cb\_list\_ptr) |
| #define | [SENSING\_SENSORS\_DEFINE](group__sensing__sensor.md#ga6fd18be5f503ad4a744df6583495c3fe)(node, reg\_ptr, cb\_list\_ptr) |
| #define | [SENSING\_SENSORS\_DT\_DEFINE](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654)(node, reg\_ptr, cb\_list\_ptr, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [SENSOR\_DEVICE\_DT\_DEFINE()](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c "Like DEVICE_DT_DEFINE() with sensor specifics.") with sensing specifics. |
| #define | [SENSING\_SENSORS\_DT\_INST\_DEFINE](group__sensing__sensor.md#gae3c7a2acba53cc524a4b1043df49fe85)(inst, ...) |
|  | Like [SENSING\_SENSORS\_DT\_DEFINE()](group__sensing__sensor.md#gad5a9ccb04d96efc57078e880ca28b654 "Like SENSOR_DEVICE_DT_DEFINE() with sensing specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |

| Enumerations | |
| --- | --- |
| enum | { [EVENT\_CONFIG\_READY](group__sensing__sensor.md#ggaafa611add600aa3b2fba2c3e08562a02a78480d5dce2873492e587176880531d8) } |
| enum | { [SENSOR\_LATER\_CFG\_BIT](group__sensing__sensor.md#ggaf3548dcc45caf8e64b2ecec463bea7e6a079aade4a76672cd9a96d777534fb584) } |

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
