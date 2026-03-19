---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structanalog__axis__calibration.html
original_path: doxygen/html/structanalog__axis__calibration.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

analog\_axis\_calibration Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Analog axis API](group__input__analog__axis.md)

Analog axis calibration data structure.
[More...](#details)

`#include <[input_analog_axis.h](input__analog__axis_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [in\_min](#a2a0b2c3ec62b66c05b187411a8b3e4db) |
|  | Input value that corresponds to the minimum output value. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [in\_max](#a67a595a038b2a244d16e759aecf5856a) |
|  | Input value that corresponds to the maximum output value. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [in\_deadzone](#a8c583137a2605d7ba48da2291de46590) |
|  | Input value center deadzone. |

## Detailed Description

Analog axis calibration data structure.

Holds the calibration data for a single analog axis. Initial values are set from the devicetree and can be changed by the applicatoin in runtime using [analog\_axis\_calibration\_set](group__input__analog__axis.md#gaae496bde41a58d92521b0a24f762caeb "analog_axis_calibration_set") and [analog\_axis\_calibration\_get](group__input__analog__axis.md#gad359f00fa9c46219a55a218d26d0407a "analog_axis_calibration_get").

## Field Documentation

## [◆ ](#a8c583137a2605d7ba48da2291de46590)in\_deadzone

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) analog\_axis\_calibration::in\_deadzone |
| --- |

Input value center deadzone.

## [◆ ](#a67a595a038b2a244d16e759aecf5856a)in\_max

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) analog\_axis\_calibration::in\_max |
| --- |

Input value that corresponds to the maximum output value.

## [◆ ](#a2a0b2c3ec62b66c05b187411a8b3e4db)in\_min

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) analog\_axis\_calibration::in\_min |
| --- |

Input value that corresponds to the minimum output value.

---

The documentation for this struct was generated from the following file:

- zephyr/input/[input\_analog\_axis.h](input__analog__axis_8h_source.md)

- [analog\_axis\_calibration](structanalog__axis__calibration.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
