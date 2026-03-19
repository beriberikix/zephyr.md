---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensing_8h.html
original_path: doxygen/html/sensing_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing.h File Reference

`#include <[zephyr/sensing/sensing_datatypes.h](sensing__datatypes_8h_source.md)>`  
`#include <[zephyr/sensing/sensing_sensor_types.h](sensing__sensor__types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](sensing_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sensing\_sensor\_version](structsensing__sensor__version.md) |
|  | Sensor Version. [More...](structsensing__sensor__version.md#details) |
| struct | [sensing\_sensor\_info](structsensing__sensor__info.md) |
|  | Sensor basic constant information. [More...](structsensing__sensor__info.md#details) |
| struct | [sensing\_callback\_list](structsensing__callback__list.md) |
|  | Sensing subsystem event callback list. [More...](structsensing__callback__list.md#details) |
| struct | [sensing\_sensor\_config](structsensing__sensor__config.md) |
|  | Sensing subsystem sensor configure, including interval, sensitivity, latency. [More...](structsensing__sensor__config.md#details) |

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSOR\_VERSION](group__sensing__api.md#ga180bc8c822f125204964f3c667464273)(\_major, \_minor, \_hotfix, \_build) |
|  | Macro to create a sensor version value. |
| #define | [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT](group__sensing__api.md#ga498dcf4dbd0eb42d8ca399df4acc2e5e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Sensor flag indicating if this sensor is on event reporting data. |
| #define | [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE](group__sensing__api.md#ga8b9766509e66fd8b8fa8e718a1544137)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Sensor flag indicating if this sensor is on change reporting data. |
| #define | [SENSING\_SENSITIVITY\_INDEX\_ALL](group__sensing__api.md#ga16ac7bd397836280f7e8b4aa82f8eb4c)   -1 |
|  | SENSING\_SENSITIVITY\_INDEX\_ALL indicating sensitivity of each data field should be set. |

| Typedefs | |
| --- | --- |
| typedef void \* | [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) |
|  | Define Sensing subsystem sensor handle. |
| typedef void(\* | [sensing\_data\_event\_t](group__sensing__api.md#ga5440a8914b664209d62388183b3c89ea)) ([sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle, const void \*buf, void \*context) |
|  | Sensor data event receive callback. |

| Enumerations | |
| --- | --- |
| enum | [sensing\_sensor\_state](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) { [SENSING\_SENSOR\_STATE\_READY](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93) = 0 , [SENSING\_SENSOR\_STATE\_OFFLINE](group__sensing__api.md#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e) = 1 } |
|  | Sensing subsystem sensor state. [More...](group__sensing__api.md#gabc9657708851e6a744a7cd73319efe06) |
| enum | [sensing\_sensor\_attribute](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) { [SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3) = 0 , [SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b) = 1 , [SENSING\_SENSOR\_ATTRIBUTE\_LATENCY](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476) = 2 , [SENSING\_SENSOR\_ATTRIBUTE\_MAX](group__sensing__api.md#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980) } |
|  | Sensing subsystem sensor config attribute. [More...](group__sensing__api.md#ga69d2ae9f45215742654bfc7e4676e6f2) |

| Functions | |
| --- | --- |
| int | [sensing\_get\_sensors](group__sensing__api.md#gaf3b6c66c2db12115f3ebec0cdba32e86) (int \*num\_sensors, const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*\*info) |
|  | Get all supported sensor instances' information. |
| int | [sensing\_open\_sensor](group__sensing__api.md#ga8e427d28efc492f15d762af3308d78cd) (const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*info, struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list, [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Open sensor instance by sensing sensor info. |
| int | [sensing\_open\_sensor\_by\_dt](group__sensing__api.md#ga4218453664fee0aa61697018e3193e7a) (const struct [device](structdevice.md) \*dev, struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list, [sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Open sensor instance by device. |
| int | [sensing\_close\_sensor](group__sensing__api.md#ga98e49ea0e84e93867df20033d01ee66c) ([sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Close sensor instance. |
| int | [sensing\_set\_config](group__sensing__api.md#ga46591a2d29f5b5e160a72bbe289884ab) ([sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle, struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count) |
|  | Set current config items to Sensing subsystem. |
| int | [sensing\_get\_config](group__sensing__api.md#gaf4037066c9a7a9f3eb1c79a4d8ae0920) ([sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle, struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count) |
|  | Get current config items from Sensing subsystem. |
| const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \* | [sensing\_get\_sensor\_info](group__sensing__api.md#ga4399f2e03d4d9444045b705b13cb6dfd) ([sensing\_sensor\_handle\_t](group__sensing__api.md#gac959e076fcdc105dfaac1d7a984ba293) handle) |
|  | Get sensor information from sensor instance handle. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sensing](dir_89ae873b54fa3664e4a65bb9dc3973c9.md)
- [sensing.h](sensing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
