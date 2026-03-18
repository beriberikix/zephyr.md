---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structusbc__vbus__driver__api.html
original_path: doxygen/html/structusbc__vbus__driver__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_vbus\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [USB-C VBUS API](group__usbc__vbus__api.md)

`#include <[usbc_vbus.h](usbc__vbus_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [check\_level](#adce9dc1f3065a029b53ee954d734cfac) )(const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level) |
| int(\* | [measure](#a373b4435b3e4a1a88a78a15d24bdcbab) )(const struct [device](structdevice.md) \*dev, int \*vbus\_meas) |
| int(\* | [discharge](#a164ae753995e293460fc408edebe21df) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable](#a5a7e6383279dc17c01d478a063efcac0)) |
| int(\* | [enable](#a5a7e6383279dc17c01d478a063efcac0) )(const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |

## Field Documentation

## [◆ ](#adce9dc1f3065a029b53ee954d734cfac)check\_level

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* usbc\_vbus\_driver\_api::check\_level) (const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level) |
| --- |

## [◆ ](#a164ae753995e293460fc408edebe21df)discharge

| int(\* usbc\_vbus\_driver\_api::discharge) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) [enable](#a5a7e6383279dc17c01d478a063efcac0)) |
| --- |

## [◆ ](#a5a7e6383279dc17c01d478a063efcac0)enable

| int(\* usbc\_vbus\_driver\_api::enable) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
| --- |

## [◆ ](#a373b4435b3e4a1a88a78a15d24bdcbab)measure

| int(\* usbc\_vbus\_driver\_api::measure) (const struct [device](structdevice.md) \*dev, int \*vbus\_meas) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/usb\_c/[usbc\_vbus.h](usbc__vbus_8h_source.md)

- [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
