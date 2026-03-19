---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensing__sensor__info.html
original_path: doxygen/html/structsensing__sensor__info.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensing\_sensor\_info Struct Reference

[Sensing](group__sensing.md) » [Sensing Subsystem API](group__sensing__api.md)

Sensor basic constant information.
[More...](#details)

`#include <[sensing.h](sensing_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [name](#ac7b4f33115f7a7a24095ca90b1e7acfe) |
|  | Name of the sensor instance. |
| const char \* | [friendly\_name](#aa3e056ad9c52c3388e049b08d0844b49) |
|  | Friendly name of the sensor instance. |
| const char \* | [vendor](#a085e8c00586c61245b822c7ea9db9c98) |
|  | Vendor name of the sensor instance. |
| const char \* | [model](#ace77ba2ab5d5eee7c4e385fc2ea74ee8) |
|  | Model name of the sensor instance. |
| const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [type](#a6b20ad8747a95cf1dc7346374de6b855) |
|  | Sensor type. |
| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [minimal\_interval](#a5b2ddf0829031098301e244f60741f2b) |
|  | Minimal report interval in micro seconds. |

## Detailed Description

Sensor basic constant information.

## Field Documentation

## [◆ ](#aa3e056ad9c52c3388e049b08d0844b49)friendly\_name

| const char\* sensing\_sensor\_info::friendly\_name |
| --- |

Friendly name of the sensor instance.

## [◆ ](#a5b2ddf0829031098301e244f60741f2b)minimal\_interval

| const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sensing\_sensor\_info::minimal\_interval |
| --- |

Minimal report interval in micro seconds.

## [◆ ](#ace77ba2ab5d5eee7c4e385fc2ea74ee8)model

| const char\* sensing\_sensor\_info::model |
| --- |

Model name of the sensor instance.

## [◆ ](#ac7b4f33115f7a7a24095ca90b1e7acfe)name

| const char\* sensing\_sensor\_info::name |
| --- |

Name of the sensor instance.

## [◆ ](#a6b20ad8747a95cf1dc7346374de6b855)type

| const [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) sensing\_sensor\_info::type |
| --- |

Sensor type.

## [◆ ](#a085e8c00586c61245b822c7ea9db9c98)vendor

| const char\* sensing\_sensor\_info::vendor |
| --- |

Vendor name of the sensor instance.

---

The documentation for this struct was generated from the following file:

- zephyr/sensing/[sensing.h](sensing_8h_source.md)

- [sensing\_sensor\_info](structsensing__sensor__info.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
