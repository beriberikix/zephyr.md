---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__a2dp__endpoint.html
original_path: doxygen/html/structbt__a2dp__endpoint.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_a2dp\_endpoint Struct Reference

Stream End Point.
[More...](#details)

`#include <[a2dp.h](a2dp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [codec\_id](#a924c4a4d4e1e90eb032ae327f75aac65) |
|  | Code ID. |
| struct [bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md) | [info](#a5db1b3737f3127669a99013801516413) |
|  | Stream End Point Information. |
| struct [bt\_a2dp\_preset](structbt__a2dp__preset.md) \* | [preset](#a9f502266d67fe501f0dd179b4b9017f1) |
|  | Pointer to preset codec chosen. |
| struct [bt\_a2dp\_preset](structbt__a2dp__preset.md) \* | [caps](#a178e9894c3399cc96340eab917d0ba49) |
|  | Capabilities. |

## Detailed Description

Stream End Point.

## Field Documentation

## [◆ ](#a178e9894c3399cc96340eab917d0ba49)caps

| struct [bt\_a2dp\_preset](structbt__a2dp__preset.md)\* bt\_a2dp\_endpoint::caps |
| --- |

Capabilities.

## [◆ ](#a924c4a4d4e1e90eb032ae327f75aac65)codec\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_a2dp\_endpoint::codec\_id |
| --- |

Code ID.

## [◆ ](#a5db1b3737f3127669a99013801516413)info

| struct [bt\_avdtp\_seid\_lsep](structbt__avdtp__seid__lsep.md) bt\_a2dp\_endpoint::info |
| --- |

Stream End Point Information.

## [◆ ](#a9f502266d67fe501f0dd179b4b9017f1)preset

| struct [bt\_a2dp\_preset](structbt__a2dp__preset.md)\* bt\_a2dp\_endpoint::preset |
| --- |

Pointer to preset codec chosen.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[a2dp.h](a2dp_8h_source.md)

- [bt\_a2dp\_endpoint](structbt__a2dp__endpoint.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
