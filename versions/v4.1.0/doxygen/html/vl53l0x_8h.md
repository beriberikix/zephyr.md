---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/vl53l0x_8h.html
original_path: doxygen/html/vl53l0x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vl53l0x.h File Reference

Custom channels and values for VL53L0X ToF Sensor.
[More...](#details)

`#include <[zephyr/drivers/sensor.h](sensor_8h_source.md)>`

[Go to the source code of this file.](vl53l0x_8h_source.md)

| Macros | |
| --- | --- |
| #define | [VL53L0X\_RANGE\_STATUS\_RANGE\_VALID](#ac0ba15e7b164d53a46f88eb3807d015d)   (0) |
| #define | [VL53L0X\_RANGE\_STATUS\_SIGMA\_FAIL](#a4b96413c5d9569b0f8037a4613b220a7)   (1) |
| #define | [VL53L0X\_RANGE\_STATUS\_SIGNAL\_FAIL](#af7317fa7071929096d3413b60f620ea1)   (2) |
| #define | [VL53L0X\_RANGE\_STATUS\_MIN\_RANGE\_FAIL](#a96dd67966d2d8b4d2eb16a5ac8b9724e)   (3) |
| #define | [VL53L0X\_RANGE\_STATUS\_PHASE\_FAIL](#a4d4565e46665ca56a5143b1868aabbda)   (4) |
| #define | [VL53L0X\_RANGE\_STATUS\_HARDWARE\_FAIL](#a6c7cbe25fbf1603f37d53fb81bc606df)   (5) |
| #define | [VL53L0X\_RANGE\_STATUS\_NO\_UPDATE](#a78056dcc0a8aa02321a4acf8c23bd5d1)   (255) |

| Enumerations | |
| --- | --- |
| enum | [sensor\_channel\_vl53l0x](#aca3102e6b764e2a96732648325a93690) {     [SENSOR\_CHAN\_VL53L0X\_RANGE\_DMAX](#aca3102e6b764e2a96732648325a93690adfefa5c75f3cfcceecb3dd8b8b6a9161) = SENSOR\_CHAN\_PRIV\_START , [SENSOR\_CHAN\_VL53L0X\_SIGNAL\_RATE\_RTN\_CPS](#aca3102e6b764e2a96732648325a93690a1d9c4833c2a652401636f0d8813d8172) , [SENSOR\_CHAN\_VL53L0X\_AMBIENT\_RATE\_RTN\_CPS](#aca3102e6b764e2a96732648325a93690afd56fa358ea21be22bf54565afbd6a0e) , [SENSOR\_CHAN\_VL53L0X\_EFFECTIVE\_SPAD\_RTN\_COUNT](#aca3102e6b764e2a96732648325a93690a4a2dd2048c64daa0e80f15f39f008c19) ,     [SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS](#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)   } |

## Detailed Description

Custom channels and values for VL53L0X ToF Sensor.

These channels provide additional sensor data not covered by the standard Zephyr sensor channels. Application must include [vl53l0x.h](vl53l0x_8h.md "Custom channels and values for VL53L0X ToF Sensor.") file to gain access to these channels.

Example usage:

#include <[zephyr/drivers/sensor/vl53l0x.h](vl53l0x_8h.md)>

if ([sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)(dev, [SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS](#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b), &value)) {

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Status: %d\n", value.val1);

}

[sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)

int sensor\_channel\_get(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Get a reading from a sensor device.

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

[vl53l0x.h](vl53l0x_8h.md)

Custom channels and values for VL53L0X ToF Sensor.

[SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS](#aca3102e6b764e2a96732648325a93690a6463303c2528d76f165614d8cb79c75b)

@ SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS

**Definition** vl53l0x.h:35

## Macro Definition Documentation

## [◆ ](#a6c7cbe25fbf1603f37d53fb81bc606df)VL53L0X\_RANGE\_STATUS\_HARDWARE\_FAIL

| #define VL53L0X\_RANGE\_STATUS\_HARDWARE\_FAIL   (5) |
| --- |

## [◆ ](#a96dd67966d2d8b4d2eb16a5ac8b9724e)VL53L0X\_RANGE\_STATUS\_MIN\_RANGE\_FAIL

| #define VL53L0X\_RANGE\_STATUS\_MIN\_RANGE\_FAIL   (3) |
| --- |

## [◆ ](#a78056dcc0a8aa02321a4acf8c23bd5d1)VL53L0X\_RANGE\_STATUS\_NO\_UPDATE

| #define VL53L0X\_RANGE\_STATUS\_NO\_UPDATE   (255) |
| --- |

## [◆ ](#a4d4565e46665ca56a5143b1868aabbda)VL53L0X\_RANGE\_STATUS\_PHASE\_FAIL

| #define VL53L0X\_RANGE\_STATUS\_PHASE\_FAIL   (4) |
| --- |

## [◆ ](#ac0ba15e7b164d53a46f88eb3807d015d)VL53L0X\_RANGE\_STATUS\_RANGE\_VALID

| #define VL53L0X\_RANGE\_STATUS\_RANGE\_VALID   (0) |
| --- |

## [◆ ](#a4b96413c5d9569b0f8037a4613b220a7)VL53L0X\_RANGE\_STATUS\_SIGMA\_FAIL

| #define VL53L0X\_RANGE\_STATUS\_SIGMA\_FAIL   (1) |
| --- |

## [◆ ](#af7317fa7071929096d3413b60f620ea1)VL53L0X\_RANGE\_STATUS\_SIGNAL\_FAIL

| #define VL53L0X\_RANGE\_STATUS\_SIGNAL\_FAIL   (2) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aca3102e6b764e2a96732648325a93690)sensor\_channel\_vl53l0x

| enum [sensor\_channel\_vl53l0x](#aca3102e6b764e2a96732648325a93690) |
| --- |

| Enumerator | |
| --- | --- |
| SENSOR\_CHAN\_VL53L0X\_RANGE\_DMAX |  |
| SENSOR\_CHAN\_VL53L0X\_SIGNAL\_RATE\_RTN\_CPS |  |
| SENSOR\_CHAN\_VL53L0X\_AMBIENT\_RATE\_RTN\_CPS |  |
| SENSOR\_CHAN\_VL53L0X\_EFFECTIVE\_SPAD\_RTN\_COUNT |  |
| SENSOR\_CHAN\_VL53L0X\_RANGE\_STATUS |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor](dir_b6423b3a8fc1c9278ff19cba182cfe6d.md)
- [vl53l0x.h](vl53l0x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
