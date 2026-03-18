---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usbc__vbus_8h.html
original_path: doxygen/html/usbc__vbus_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbc\_vbus.h File Reference

USB-C VBUS device APIs.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/drivers/usb_c/usbc_tc.h](usbc__tc_8h_source.md)>`

[Go to the source code of this file.](usbc__vbus_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbc\_vbus\_driver\_api](structusbc__vbus__driver__api.md) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbc\_vbus\_check\_level](group__usbc__vbus__api.md#ga421653274fe9b8e2e6237a4bbe47e3ad) (const struct [device](structdevice.md) \*dev, enum [tc\_vbus\_level](group__usb__type__c.md#ga015455a6c5620dfc96cfb713bbb72161) level) |
|  | Checks if VBUS is at a particular level. |
| static int | [usbc\_vbus\_measure](group__usbc__vbus__api.md#ga0b6c561c5f74a30d54397294cb21660d) (const struct [device](structdevice.md) \*dev, int \*meas) |
|  | Reads and returns VBUS measured in mV. |
| static int | [usbc\_vbus\_discharge](group__usbc__vbus__api.md#ga8414cfcfeee7799ea57854c59c0c1677) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls a pin that discharges VBUS. |
| static int | [usbc\_vbus\_enable](group__usbc__vbus__api.md#ga7c94eac0f28be6cd12717d2f1a50ec54) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Controls a pin that enables VBUS measurements. |

## Detailed Description

USB-C VBUS device APIs.

This file contains the USB-C VBUS device APIs. All USB-C VBUS measurement and control device drivers should implement the APIs described in this file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb\_c](dir_a57818ecbbcbfd5f3cb9a612ed0259e0.md)
- [usbc\_vbus.h](usbc__vbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
