---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__sensing__sensor__types.html
original_path: doxygen/html/group__sensing__sensor__types.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Sensor Types

[Sensing](group__sensing.md)

Sensor Types Definition.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT](#gaee0dce0047c15b65556f7a1444c93337)   0x41 |
|  | sensor category light |
| #define | [SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D](#ga6368e8d035eae53d153ebb9dd0c6871e)   0x73 |
|  | sensor category motion |
| #define | [SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D](#gaaa716f0ff9e8ba8fac8ff5a539d3f785)   0x76 |
| #define | [SENSING\_SENSOR\_TYPE\_MOTION\_MOTION\_DETECTOR](#gae562dc942a869d95703893d41dcc2373)   0x77 |
| #define | [SENSING\_SENSOR\_TYPE\_OTHER\_CUSTOM](#gac637e2b7d193603ffa150fa4876e96b9)   0xE1 |
|  | sensor category other |
| #define | [SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D](#ga1dc895e135ec8a07efdfe5d196692898)   0x240 |
| #define | [SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE](#ga1db5105621424ea60ffbc07fe6c25ae3)   0x20B |
| #define | [SENSING\_SENSOR\_TYPE\_ALL](#ga9f6bc03e84167bf0b1ae8ea4fe016223)   0xFFFF |
|  | Sensor type for all sensors. |

## Detailed Description

Sensor Types Definition.

Sensor types definition followed HID standard. [https://usb.org/sites/default/files/hutrr39b\_0.pdf](https://usb.org/sites/default/files/hutrr39b_0.pdf)

TODO: will add more types

## Macro Definition Documentation

## [◆ ](#ga9f6bc03e84167bf0b1ae8ea4fe016223)SENSING\_SENSOR\_TYPE\_ALL

| #define SENSING\_SENSOR\_TYPE\_ALL   0xFFFF |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

Sensor type for all sensors.

This macro defines the sensor type for all sensors.

## [◆ ](#gaee0dce0047c15b65556f7a1444c93337)SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT

| #define SENSING\_SENSOR\_TYPE\_LIGHT\_AMBIENTLIGHT   0x41 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

sensor category light

## [◆ ](#ga6368e8d035eae53d153ebb9dd0c6871e)SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D

| #define SENSING\_SENSOR\_TYPE\_MOTION\_ACCELEROMETER\_3D   0x73 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

sensor category motion

## [◆ ](#gaaa716f0ff9e8ba8fac8ff5a539d3f785)SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D

| #define SENSING\_SENSOR\_TYPE\_MOTION\_GYROMETER\_3D   0x76 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

## [◆ ](#ga1db5105621424ea60ffbc07fe6c25ae3)SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE

| #define SENSING\_SENSOR\_TYPE\_MOTION\_HINGE\_ANGLE   0x20B |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

## [◆ ](#gae562dc942a869d95703893d41dcc2373)SENSING\_SENSOR\_TYPE\_MOTION\_MOTION\_DETECTOR

| #define SENSING\_SENSOR\_TYPE\_MOTION\_MOTION\_DETECTOR   0x77 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

## [◆ ](#ga1dc895e135ec8a07efdfe5d196692898)SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D

| #define SENSING\_SENSOR\_TYPE\_MOTION\_UNCALIB\_ACCELEROMETER\_3D   0x240 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

## [◆ ](#gac637e2b7d193603ffa150fa4876e96b9)SENSING\_SENSOR\_TYPE\_OTHER\_CUSTOM

| #define SENSING\_SENSOR\_TYPE\_OTHER\_CUSTOM   0xE1 |
| --- |

`#include <[sensing_sensor_types.h](sensing__sensor__types_8h.md)>`

sensor category other

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
