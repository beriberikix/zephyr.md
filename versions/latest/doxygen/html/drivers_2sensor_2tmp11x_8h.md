---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sensor_2tmp11x_8h.html
original_path: doxygen/html/drivers_2sensor_2tmp11x_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tmp11x.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](drivers_2sensor_2tmp11x_8h_source.md)

| Macros | |
| --- | --- |
| #define | [EEPROM\_TMP11X\_SIZE](#abb06ab7fe6ab207f5b9d77521bef218f)   (4 \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))) |

| Enumerations | |
| --- | --- |
| enum | [sensor\_attribute\_tmp\_11x](#a30cbd49ad5c7286d23453ce6f1167ee9) { [SENSOR\_ATTR\_TMP11X\_ONE\_SHOT\_MODE](#a30cbd49ad5c7286d23453ce6f1167ee9aeb6e8af036fe3a8081504b62f30fb591) = SENSOR\_ATTR\_PRIV\_START , [SENSOR\_ATTR\_TMP11X\_SHUTDOWN\_MODE](#a30cbd49ad5c7286d23453ce6f1167ee9a423099eda7d8c3cd7e3712bf9b4ce024) , [SENSOR\_ATTR\_TMP11X\_CONTINUOUS\_CONVERSION\_MODE](#a30cbd49ad5c7286d23453ce6f1167ee9a001d3256c1daf5275e414bd5a01bd8cb) } |

| Functions | |
| --- | --- |
| int | [tmp11x\_eeprom\_read](#ae08f7c30e516b4b8f36a6ad1883830cf) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
| int | [tmp11x\_eeprom\_write](#abc253a269051ae0aeec8061a050922c9) (const struct [device](structdevice.md) \*dev, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) offset, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |

## Macro Definition Documentation

## [◆ ](#abb06ab7fe6ab207f5b9d77521bef218f)EEPROM\_TMP11X\_SIZE

| #define EEPROM\_TMP11X\_SIZE   (4 \* [sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e))) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a30cbd49ad5c7286d23453ce6f1167ee9)sensor\_attribute\_tmp\_11x

| enum [sensor\_attribute\_tmp\_11x](#a30cbd49ad5c7286d23453ce6f1167ee9) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_ATTR\_TMP11X\_ONE\_SHOT\_MODE | Turn on power saving/one shot mode. |
| SENSOR\_ATTR\_TMP11X\_SHUTDOWN\_MODE | Shutdown the sensor. |
| SENSOR\_ATTR\_TMP11X\_CONTINUOUS\_CONVERSION\_MODE | Turn on continuous conversion. |

## Function Documentation

## [◆ ](#ae08f7c30e516b4b8f36a6ad1883830cf)tmp11x\_eeprom\_read()

| int tmp11x\_eeprom\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

## [◆ ](#abc253a269051ae0aeec8061a050922c9)tmp11x\_eeprom\_write()

| int tmp11x\_eeprom\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *offset*, |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [tmp11x.h](drivers_2sensor_2tmp11x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
