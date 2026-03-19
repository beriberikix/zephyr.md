---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__sensing__api.html
original_path: doxygen/html/group__sensing__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sensing Subsystem API

[Sensing](group__sensing.md)

Sensing Subsystem API .
[More...](#details)

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
| #define | [SENSING\_SENSOR\_VERSION](#ga180bc8c822f125204964f3c667464273)(\_major, \_minor, \_hotfix, \_build) |
|  | Macro to create a sensor version value. |
| #define | [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT](#ga498dcf4dbd0eb42d8ca399df4acc2e5e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Sensor flag indicating if this sensor is on event reporting data. |
| #define | [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE](#ga8b9766509e66fd8b8fa8e718a1544137)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Sensor flag indicating if this sensor is on change reporting data. |
| #define | [SENSING\_SENSITIVITY\_INDEX\_ALL](#ga16ac7bd397836280f7e8b4aa82f8eb4c)   -1 |
|  | SENSING\_SENSITIVITY\_INDEX\_ALL indicating sensitivity of each data field should be set. |

| Typedefs | |
| --- | --- |
| typedef void \* | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) |
|  | Define Sensing subsystem sensor handle. |
| typedef void(\* | [sensing\_data\_event\_t](#ga5440a8914b664209d62388183b3c89ea)) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) handle, const void \*buf, void \*context) |
|  | Sensor data event receive callback. |

| Enumerations | |
| --- | --- |
| enum | [sensing\_sensor\_state](#gabc9657708851e6a744a7cd73319efe06) { [SENSING\_SENSOR\_STATE\_READY](#ggabc9657708851e6a744a7cd73319efe06a735fe339796ea7b4d2387d931382ce93) = 0 , [SENSING\_SENSOR\_STATE\_OFFLINE](#ggabc9657708851e6a744a7cd73319efe06af23a28e861a8fa2d49b18a0fbe62600e) = 1 } |
|  | Sensing subsystem sensor state. [More...](#gabc9657708851e6a744a7cd73319efe06) |
| enum | [sensing\_sensor\_attribute](#ga69d2ae9f45215742654bfc7e4676e6f2) { [SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL](#gga69d2ae9f45215742654bfc7e4676e6f2a8c9870b1303008b45e2caeb33f5c44a3) = 0 , [SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY](#gga69d2ae9f45215742654bfc7e4676e6f2abc39825a643b9d1452162f057f79774b) = 1 , [SENSING\_SENSOR\_ATTRIBUTE\_LATENCY](#gga69d2ae9f45215742654bfc7e4676e6f2a2ccb8b476935ce27b2eedbb889e25476) = 2 , [SENSING\_SENSOR\_ATTRIBUTE\_MAX](#gga69d2ae9f45215742654bfc7e4676e6f2a072ff2aa9640503bfd8cbc8f7d271980) } |
|  | Sensing subsystem sensor config attribute. [More...](#ga69d2ae9f45215742654bfc7e4676e6f2) |

| Functions | |
| --- | --- |
| int | [sensing\_get\_sensors](#gaf3b6c66c2db12115f3ebec0cdba32e86) (int \*num\_sensors, const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*\*info) |
|  | Get all supported sensor instances' information. |
| int | [sensing\_open\_sensor](#ga8e427d28efc492f15d762af3308d78cd) (const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*info, struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list, [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Open sensor instance by sensing sensor info. |
| int | [sensing\_open\_sensor\_by\_dt](#ga4218453664fee0aa61697018e3193e7a) (const struct [device](structdevice.md) \*dev, struct [sensing\_callback\_list](structsensing__callback__list.md) \*cb\_list, [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Open sensor instance by device. |
| int | [sensing\_close\_sensor](#ga98e49ea0e84e93867df20033d01ee66c) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \*handle) |
|  | Close sensor instance. |
| int | [sensing\_set\_config](#ga46591a2d29f5b5e160a72bbe289884ab) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) handle, struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count) |
|  | Set current config items to Sensing subsystem. |
| int | [sensing\_get\_config](#gaf4037066c9a7a9f3eb1c79a4d8ae0920) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) handle, struct [sensing\_sensor\_config](structsensing__sensor__config.md) \*configs, int count) |
|  | Get current config items from Sensing subsystem. |
| const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \* | [sensing\_get\_sensor\_info](#ga4399f2e03d4d9444045b705b13cb6dfd) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) handle) |
|  | Get sensor information from sensor instance handle. |

## Detailed Description

Sensing Subsystem API .

## Macro Definition Documentation

## [◆ ](#ga16ac7bd397836280f7e8b4aa82f8eb4c)SENSING\_SENSITIVITY\_INDEX\_ALL

| #define SENSING\_SENSITIVITY\_INDEX\_ALL   -1 |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

SENSING\_SENSITIVITY\_INDEX\_ALL indicating sensitivity of each data field should be set.

## [◆ ](#ga8b9766509e66fd8b8fa8e718a1544137)SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE

| #define SENSING\_SENSOR\_FLAG\_REPORT\_ON\_CHANGE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Sensor flag indicating if this sensor is on change reporting data.

Reporting sensor data when the sensor data changes.

Exclusive with [SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT](#ga498dcf4dbd0eb42d8ca399df4acc2e5e)

## [◆ ](#ga498dcf4dbd0eb42d8ca399df4acc2e5e)SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT

| #define SENSING\_SENSOR\_FLAG\_REPORT\_ON\_EVENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Sensor flag indicating if this sensor is on event reporting data.

Reporting sensor data when the sensor event occurs, such as a motion detect sensor reporting a motion or motionless detected event.

## [◆ ](#ga180bc8c822f125204964f3c667464273)SENSING\_SENSOR\_VERSION

| #define SENSING\_SENSOR\_VERSION | ( |  | *\_major*, |
| --- | --- | --- | --- |
|  |  |  | *\_minor*, |
|  |  |  | *\_hotfix*, |
|  |  |  | *\_build* ) |

`#include <[sensing.h](sensing_8h.md)>`

**Value:**

([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(31, 24), \_major) | \

FIELD\_PREP([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 16), \_minor) | \

FIELD\_PREP([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(15, 8), \_hotfix) | \

FIELD\_PREP([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0), \_build))

[GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)

#define GENMASK(h, l)

Create a contiguous bitmask starting at bit position l and ending at position h.

**Definition** util.h:79

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:15

Macro to create a sensor version value.

## Typedef Documentation

## [◆ ](#ga5440a8914b664209d62388183b3c89ea)sensing\_data\_event\_t

| typedef void(\* sensing\_data\_event\_t) ([sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) handle, const void \*buf, void \*context) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Sensor data event receive callback.

Parameters
:   | handle | The sensor instance handle. |
    | --- | --- |
    | buf | The data buffer with sensor data. |
    | context | User provided context pointer. |

## [◆ ](#gac959e076fcdc105dfaac1d7a984ba293)sensing\_sensor\_handle\_t

| typedef void\* [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Define Sensing subsystem sensor handle.

## Enumeration Type Documentation

## [◆ ](#ga69d2ae9f45215742654bfc7e4676e6f2)sensing\_sensor\_attribute

| enum [sensing\_sensor\_attribute](#ga69d2ae9f45215742654bfc7e4676e6f2) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Sensing subsystem sensor config attribute.

| Enumerator | |
| --- | --- |
| SENSING\_SENSOR\_ATTRIBUTE\_INTERVAL | The interval attribute of a sensor configuration. |
| SENSING\_SENSOR\_ATTRIBUTE\_SENSITIVITY | The sensitivity attribute of a sensor configuration. |
| SENSING\_SENSOR\_ATTRIBUTE\_LATENCY | The latency attribute of a sensor configuration. |
| SENSING\_SENSOR\_ATTRIBUTE\_MAX | The maximum number of attributes that a sensor configuration can have. |

## [◆ ](#gabc9657708851e6a744a7cd73319efe06)sensing\_sensor\_state

| enum [sensing\_sensor\_state](#gabc9657708851e6a744a7cd73319efe06) |
| --- |

`#include <[sensing.h](sensing_8h.md)>`

Sensing subsystem sensor state.

| Enumerator | |
| --- | --- |
| SENSING\_SENSOR\_STATE\_READY | The sensor is ready. |
| SENSING\_SENSOR\_STATE\_OFFLINE | The sensor is offline. |

## Function Documentation

## [◆ ](#ga98e49ea0e84e93867df20033d01ee66c)sensing\_close\_sensor()

| int sensing\_close\_sensor | ( | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \* | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensing.h](sensing_8h.md)>`

Close sensor instance.

Parameters
:   | handle | The sensor instance handle need to close. |
    | --- | --- |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#gaf4037066c9a7a9f3eb1c79a4d8ae0920)sensing\_get\_config()

| int sensing\_get\_config | ( | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) | *handle*, |
| --- | --- | --- | --- |
|  |  | struct [sensing\_sensor\_config](structsensing__sensor__config.md) \* | *configs*, |
|  |  | int | *count* ) |

`#include <[sensing.h](sensing_8h.md)>`

Get current config items from Sensing subsystem.

Parameters
:   | handle | The sensor instance handle. |
    | --- | --- |
    | configs | The configs to be get according to config attribute. |
    | count | count of configs. |

Returns
:   0 on success or negative error value on failure, not support etc.

## [◆ ](#ga4399f2e03d4d9444045b705b13cb6dfd)sensing\_get\_sensor\_info()

| const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \* sensing\_get\_sensor\_info | ( | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) | *handle* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sensing.h](sensing_8h.md)>`

Get sensor information from sensor instance handle.

Parameters
:   | handle | The sensor instance handle. |
    | --- | --- |

Returns
:   a const pointer to [sensing\_sensor\_info](structsensing__sensor__info.md "sensing_sensor_info") on success or NULL on failure.

## [◆ ](#gaf3b6c66c2db12115f3ebec0cdba32e86)sensing\_get\_sensors()

| int sensing\_get\_sensors | ( | int \* | *num\_sensors*, |
| --- | --- | --- | --- |
|  |  | const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \*\* | *info* ) |

`#include <[sensing.h](sensing_8h.md)>`

Get all supported sensor instances' information.

This API just returns read only information of sensor instances, pointer info will directly point to internal buffer, no need for caller to allocate buffer, no side effect to sensor instances.

Parameters
:   | num\_sensors | Get number of sensor instances. |
    | --- | --- |
    | info | For receiving sensor instances' information array pointer. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga8e427d28efc492f15d762af3308d78cd)sensing\_open\_sensor()

| int sensing\_open\_sensor | ( | const struct [sensing\_sensor\_info](structsensing__sensor__info.md) \* | *info*, |
| --- | --- | --- | --- |
|  |  | struct [sensing\_callback\_list](structsensing__callback__list.md) \* | *cb\_list*, |
|  |  | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \* | *handle* ) |

`#include <[sensing.h](sensing_8h.md)>`

Open sensor instance by sensing sensor info.

Application clients use it to open a sensor instance and get its handle. Support multiple Application clients for open same sensor instance, in this case, the returned handle will different for different clients. meanwhile, also register sensing callback list

Parameters
:   | info | The sensor info got from [sensing\_get\_sensors](#gaf3b6c66c2db12115f3ebec0cdba32e86) |
    | --- | --- |
    | cb\_list | callback list to be registered to sensing, must have a static lifetime. |
    | handle | The opened instance handle, if failed will be set to NULL. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga4218453664fee0aa61697018e3193e7a)sensing\_open\_sensor\_by\_dt()

| int sensing\_open\_sensor\_by\_dt | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sensing\_callback\_list](structsensing__callback__list.md) \* | *cb\_list*, |
|  |  | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) \* | *handle* ) |

`#include <[sensing.h](sensing_8h.md)>`

Open sensor instance by device.

Application clients use it to open a sensor instance and get its handle. Support multiple Application clients for open same sensor instance, in this case, the returned handle will different for different clients. meanwhile, also register sensing callback list.

Parameters
:   | dev | pointer device get from device tree. |
    | --- | --- |
    | cb\_list | callback list to be registered to sensing, must have a static lifetime. |
    | handle | The opened instance handle, if failed will be set to NULL. |

Returns
:   0 on success or negative error value on failure.

## [◆ ](#ga46591a2d29f5b5e160a72bbe289884ab)sensing\_set\_config()

| int sensing\_set\_config | ( | [sensing\_sensor\_handle\_t](#gac959e076fcdc105dfaac1d7a984ba293) | *handle*, |
| --- | --- | --- | --- |
|  |  | struct [sensing\_sensor\_config](structsensing__sensor__config.md) \* | *configs*, |
|  |  | int | *count* ) |

`#include <[sensing.h](sensing_8h.md)>`

Set current config items to Sensing subsystem.

Parameters
:   | handle | The sensor instance handle. |
    | --- | --- |
    | configs | The configs to be set according to config attribute. |
    | count | count of configs. |

Returns
:   0 on success or negative error value on failure, not support etc.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
