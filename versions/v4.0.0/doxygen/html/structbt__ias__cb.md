---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__ias__cb.html
original_path: doxygen/html/structbt__ias__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_ias\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Immediate Alert Service (IAS)](group__bt__ias.md)

Immediate Alert Service callback structure.
[More...](#details)

`#include <[ias.h](ias_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [no\_alert](#ae0719b1f44f094ff0bbd3abea2bfdf15) )(void) |
|  | Callback function to stop alert. |
| void(\* | [mild\_alert](#aeffe89f9e5a9b87efbdd0af471de980d) )(void) |
|  | Callback function for alert level value. |
| void(\* | [high\_alert](#ad2974bbd16e8d4425370a57f62601af5) )(void) |
|  | Callback function for alert level value. |

## Detailed Description

Immediate Alert Service callback structure.

## Field Documentation

## [◆ ](#ad2974bbd16e8d4425370a57f62601af5)high\_alert

| void(\* bt\_ias\_cb::high\_alert) (void) |
| --- |

Callback function for alert level value.

This callback is called when peer commands to alert in the strongest possible way.

## [◆ ](#aeffe89f9e5a9b87efbdd0af471de980d)mild\_alert

| void(\* bt\_ias\_cb::mild\_alert) (void) |
| --- |

Callback function for alert level value.

This callback is called when peer commands to alert.

## [◆ ](#ae0719b1f44f094ff0bbd3abea2bfdf15)no\_alert

| void(\* bt\_ias\_cb::no\_alert) (void) |
| --- |

Callback function to stop alert.

This callback is called when peer commands to disable alert.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[ias.h](ias_8h_source.md)

- [bt\_ias\_cb](structbt__ias__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
