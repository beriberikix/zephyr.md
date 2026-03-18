---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__usbc__vbus__api.html
original_path: doxygen/html/group__usbc__vbus__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB-C VBUS API

[Device Driver APIs](group__io__interfaces.md)

USB-C VBUS API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbc\_vbus\_check\_level](#ga421653274fe9b8e2e6237a4bbe47e3ad) (const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level) |
|  | Checks if VBUS is at a particular level. |
| static int | [usbc\_vbus\_measure](#ga0b6c561c5f74a30d54397294cb21660d) (const struct [device](structdevice.md) \*dev, int \*meas) |
|  | Reads and returns VBUS measured in mV. |
| static int | [usbc\_vbus\_discharge](#ga8414cfcfeee7799ea57854c59c0c1677) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls a pin that discharges VBUS. |
| static int | [usbc\_vbus\_enable](#ga7c94eac0f28be6cd12717d2f1a50ec54) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls a pin that enables VBUS measurements. |

## Detailed Description

USB-C VBUS API.

Since
:   3.3

Version
:   0.1.0

## Function Documentation

## [◆ ](#ga421653274fe9b8e2e6237a4bbe47e3ad)usbc\_vbus\_check\_level()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbc\_vbus\_check\_level | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) | *level* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_vbus.h](usbc__vbus_8h.md)>`

Checks if VBUS is at a particular level.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | level | The level voltage to check against |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if VBUS is at the level voltage |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if VBUS is not at that level voltage |

## [◆ ](#ga8414cfcfeee7799ea57854c59c0c1677)usbc\_vbus\_discharge()

| | int usbc\_vbus\_discharge | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_vbus.h](usbc__vbus_8h.md)>`

Controls a pin that discharges VBUS.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | Discharge VBUS when true |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOENT | if discharge pin isn't defined |

## [◆ ](#ga7c94eac0f28be6cd12717d2f1a50ec54)usbc\_vbus\_enable()

| | int usbc\_vbus\_enable | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_vbus.h](usbc__vbus_8h.md)>`

Controls a pin that enables VBUS measurements.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | enable | enable VBUS measurements when true |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |
    | -ENOENT | if enable pin isn't defined |

## [◆ ](#ga0b6c561c5f74a30d54397294cb21660d)usbc\_vbus\_measure()

| | int usbc\_vbus\_measure | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | int \* | *meas* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbc_vbus.h](usbc__vbus_8h.md)>`

Reads and returns VBUS measured in mV.

Parameters
:   | dev | Runtime device structure |
    | --- | --- |
    | meas | pointer where the measured VBUS voltage is stored |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EIO | on failure |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
