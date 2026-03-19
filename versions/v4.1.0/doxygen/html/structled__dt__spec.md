---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structled__dt__spec.html
original_path: doxygen/html/structled__dt__spec.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

led\_dt\_spec Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [LED Interface](group__led__interface.md)

Container for an LED information specified in devicetree.
[More...](#details)

`#include <[led.h](drivers_2led_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [dev](#ad92b9ee24cb31fcc0a2352bcf831cecb) |
|  | LED device instance. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [index](#a72c5ff64b89344ca9644fd2b4f4c9515) |
|  | Index of the LED on the controller. |

## Detailed Description

Container for an LED information specified in devicetree.

This type contains a pointer to and LED device and an LED index.

See also
:   [LED\_DT\_SPEC\_GET](group__led__interface.md#ga537f733ae3070fbe279834c76cda35ae "Static initializer for a struct led_dt_spec.")
:   [LED\_DT\_SPEC\_GET\_OR](group__led__interface.md#gade3059194ce428783ea3e9900ed0be52 "Like LED_DT_SPEC_GET(), with a fallback value if the node does not exist.")

## Field Documentation

## [◆ ](#ad92b9ee24cb31fcc0a2352bcf831cecb)dev

| const struct [device](structdevice.md)\* led\_dt\_spec::dev |
| --- |

LED device instance.

## [◆ ](#a72c5ff64b89344ca9644fd2b4f4c9515)index

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) led\_dt\_spec::index |
| --- |

Index of the LED on the controller.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[led.h](drivers_2led_8h_source.md)

- [led\_dt\_spec](structled__dt__spec.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
